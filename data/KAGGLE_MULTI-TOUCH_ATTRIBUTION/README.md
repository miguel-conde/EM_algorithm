[Multi-Touch Attribution](https://www.kaggle.com/datasets/vivekparasharr/multi-touch-attribution)

## Local data (manual download)

Archive found in this folder:

- `archive.zip`
	- Contains: `multi_touch_attribution_data.csv`
	- Format: CSV (comma-separated)
	- Columns (5): `User ID`, `Timestamp`, `Channel`, `Campaign`, `Conversion`

Notes for MTA:

- Each row is a user touchpoint with a marketing `Channel` and `Campaign` at `Timestamp`.
- `Conversion` is a categorical indicator (`Yes`/`No`). For binary modeling, map to 1/0.

Quick load (Pandas):

```python
import pandas as pd

df = pd.read_csv(
		"data/KAGGLE_MULTI-TOUCH_ATTRIBUTION/archive.zip",
)
```

## Data dictionary (sample)

Profiled from a `nrows=5000` sample (types/missing may differ on full data):

| column | dtype (sample) | missing (sample) | example values |
|---|---:|---:|---|
| User ID | int64 | 0.0% | 83281, 68071, 90131 |
| Timestamp | object | 0.0% | 2025-02-10 07:58:51, 2025-02-10 23:38:48, 2025-02-11 10:41:07 |
| Channel | object | 0.0% | Email, Search Ads, Social Media |
| Campaign | object | 0.0% | New Product Launch, Winter Sale, Brand Awareness |
| Conversion | object | 0.0% | No, No, Yes |

## Journey / path construction

Suggested mapping:

- User / path id: `User ID`
- Time: `Timestamp` (parse to datetime)
- Channel/state: `Channel` (optionally use `Campaign` as a second hierarchy)
- Outcome: `Conversion` (map `Yes`→1, `No`→0)

Typical preprocessing steps:

- Sort by (`User ID`, `Timestamp`) and build per-user ordered sequences of `Channel`.
- Decide whether your “state” is `Channel` only, or `Channel:Campaign`.
- For Markov attribution, you often add explicit `START` and `CONVERSION`/`NULL` terminal states.

Example (sketch):

```python
import pandas as pd

df = pd.read_csv("data/KAGGLE_MULTI-TOUCH_ATTRIBUTION/archive.zip")
df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
df["conversion_flag"] = df["Conversion"].str.lower().eq("yes").astype(int)
df = df.sort_values(["User ID", "Timestamp"])

paths = df.groupby("User ID")["Channel"].apply(list).reset_index(name="channel_path")
labels = df.groupby("User ID")["conversion_flag"].max().reset_index(name="converted_any")
```

## Derived artifacts

This folder includes a derived per-user journey table:

- `derived/paths.csv` (generated)
	- Columns: `user_id`, `n_touches`, `converted_any`, `path_str`

Regenerate it from the repo root:

```bash
.venv/bin/python tools/build_ready_paths.py
```