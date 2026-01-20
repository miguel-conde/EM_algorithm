from __future__ import annotations

import argparse
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Optional

import pandas as pd


@dataclass(frozen=True)
class OutputPaths:
    folder: Path
    csv_path: Path
    parquet_path: Path


def _ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def _read_csv_from_zip(zip_path: Path, member: str, **read_csv_kwargs) -> pd.DataFrame:
    with zipfile.ZipFile(zip_path, "r") as zf:
        with zf.open(member) as f:
            return pd.read_csv(f, **read_csv_kwargs)


def _write_paths(df_paths: pd.DataFrame, out: OutputPaths) -> tuple[bool, bool]:
    _ensure_dir(out.csv_path.parent)

    wrote_csv = False
    wrote_parquet = False

    df_paths.to_csv(out.csv_path, index=False)
    wrote_csv = True

    # Parquet is optional (requires pyarrow or fastparquet)
    try:
        df_paths.to_parquet(out.parquet_path, index=False)
        wrote_parquet = True
    except Exception:
        wrote_parquet = False

    return wrote_csv, wrote_parquet


def _paths_from_shapley_marketing(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date_served"] = pd.to_datetime(df["date_served"], errors="coerce")
    df = df.sort_values(["user_id", "date_served"], kind="mergesort")

    # Ensure bool-ish
    if df["converted"].dtype != bool:
        df["converted"] = df["converted"].astype(str).str.lower().isin(["true", "1", "yes", "y"])

    seq = df.groupby("user_id")["marketing_channel"].apply(list)
    converted_any = df.groupby("user_id")["converted"].max().astype(bool)

    out = (
        seq.reset_index(name="channel_path")
        .merge(converted_any.reset_index(name="converted_any"), on="user_id")
    )
    out["n_touches"] = out["channel_path"].apply(len)
    out["path_str"] = out["channel_path"].apply(lambda xs: " > ".join(map(str, xs)))
    return out[["user_id", "n_touches", "converted_any", "path_str"]]


def _paths_from_multi_touch(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
    df = df.sort_values(["User ID", "Timestamp"], kind="mergesort")

    conversion_flag = df["Conversion"].astype(str).str.lower().eq("yes").astype(int)
    seq = df.groupby("User ID")["Channel"].apply(list)
    converted_any = conversion_flag.groupby(df["User ID"]).max().astype(int)

    out = (
        seq.reset_index(name="channel_path")
        .merge(converted_any.reset_index(name="converted_any"), on="User ID")
    )
    out["n_touches"] = out["channel_path"].apply(len)
    out["path_str"] = out["channel_path"].apply(lambda xs: " > ".join(map(str, xs)))
    return out.rename(columns={"User ID": "user_id"})[["user_id", "n_touches", "converted_any", "path_str"]]


def _paths_from_markov_attribution(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["time"] = pd.to_datetime(df["time"], errors="coerce", utc=True)
    df = df.sort_values(["cookie", "time"], kind="mergesort")

    seq = df.groupby("cookie")["channel"].apply(list)
    converted_any = df.groupby("cookie")["conversion"].max().astype(int)

    # conversion_value may be present even for non-conversions; this is a simple total per cookie
    if "conversion_value" in df.columns:
        conversion_value_total = df.groupby("cookie")["conversion_value"].sum(min_count=1)
    else:
        conversion_value_total = pd.Series(index=converted_any.index, data=pd.NA)

    out = (
        seq.reset_index(name="channel_path")
        .merge(converted_any.reset_index(name="converted_any"), on="cookie")
        .merge(conversion_value_total.reset_index(name="conversion_value_total"), on="cookie", how="left")
    )
    out["n_touches"] = out["channel_path"].apply(len)
    out["path_str"] = out["channel_path"].apply(lambda xs: " > ".join(map(str, xs)))
    return out.rename(columns={"cookie": "user_id"})[["user_id", "n_touches", "converted_any", "conversion_value_total", "path_str"]]


def _paths_from_criteo(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.sort_values(["uid", "timestamp"], kind="mergesort")

    seq = df.groupby("uid")["campaign"].apply(list)
    converted_any = df.groupby("uid")["conversion"].max().astype(int)

    out = (
        seq.reset_index(name="campaign_path")
        .merge(converted_any.reset_index(name="converted_any"), on="uid")
    )
    out["n_touches"] = out["campaign_path"].apply(len)
    out["path_str"] = out["campaign_path"].apply(lambda xs: " > ".join(map(str, xs)))
    return out.rename(columns={"uid": "user_id"})[["user_id", "n_touches", "converted_any", "path_str"]]


def _outputs_for_folder(folder: Path) -> OutputPaths:
    derived = folder / "derived"
    return OutputPaths(
        folder=folder,
        csv_path=derived / "paths.csv",
        parquet_path=derived / "paths.parquet",
    )


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Build per-user journey paths from locally downloaded MTA datasets.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="Repository root (defaults to parent of tools/)",
    )
    parser.add_argument(
        "--criteo-max-rows",
        type=int,
        default=200_000,
        help="Max rows to read from the large Criteo TSV to build sample paths (default: 200000).",
    )
    args = parser.parse_args(argv)

    repo_root = args.repo_root or Path(__file__).resolve().parents[1]
    data_dir = repo_root / "data"

    jobs: list[tuple[str, Path, str, dict]] = [
        (
            "KAGGLE_SHAPLEY_MTA",
            data_dir / "KAGGLE_SHAPLEY_MTA" / "archive.zip",
            "marketing.csv",
            {"nrows": 1_000_000},
        ),
        (
            "KAGGLE_MULTI-TOUCH_ATTRIBUTION",
            data_dir / "KAGGLE_MULTI-TOUCH_ATTRIBUTION" / "archive.zip",
            "multi_touch_attribution_data.csv",
            {"nrows": 1_000_000},
        ),
        (
            "KAGGLE_MTA_MODELLING",
            data_dir / "KAGGLE_MTA_MODELLING" / "Markov Chain Attribution Data Set.zip",
            "attribution data.csv",
            {"nrows": 5_000_000},
        ),
        (
            "KAGGLE_CRITEO",
            data_dir / "KAGGLE_CRITEO" / "archive.zip",
            "pcb_dataset_final.tsv",
            {"sep": "\t", "nrows": args.criteo_max_rows, "low_memory": False},
        ),
    ]

    for folder_name, zip_path, member, read_kwargs in jobs:
        folder = data_dir / folder_name
        if not zip_path.exists():
            print(f"SKIP {folder_name}: archive not found at {zip_path}")
            continue

        print(f"BUILD {folder_name}: reading {zip_path.name}::{member}")
        df = _read_csv_from_zip(zip_path, member, **read_kwargs)

        if folder_name == "KAGGLE_SHAPLEY_MTA":
            df_paths = _paths_from_shapley_marketing(df)
        elif folder_name == "KAGGLE_MULTI-TOUCH_ATTRIBUTION":
            df_paths = _paths_from_multi_touch(df)
        elif folder_name == "KAGGLE_MTA_MODELLING":
            df_paths = _paths_from_markov_attribution(df)
        elif folder_name == "KAGGLE_CRITEO":
            df_paths = _paths_from_criteo(df)
            df_paths.attrs["note"] = f"Built from a sample of {len(df):,} rows (criteo-max-rows)."
        else:
            print(f"SKIP {folder_name}: no builder")
            continue

        out = _outputs_for_folder(folder)
        wrote_csv, wrote_parquet = _write_paths(df_paths, out)
        print(f"WROTE {folder_name}: {out.csv_path.relative_to(repo_root)}" + (f" and {out.parquet_path.relative_to(repo_root)}" if wrote_parquet else " (parquet unavailable: install pyarrow)"))

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
