- [Multitouch Attribution Modelling](https://www.kaggle.com/code/hughhuyton/multitouch-attribution-modelling/notebook)
- Data is here: [](https://www.dropbox.com/scl/fo/jrw7atq517jxzqrn2gxz5/ALfzBkRA90d2z7UmLcLqQRs?rlkey=6qg8wfcdrwuy9kfya6kejcq11&e=2&dl=0)

## Local data (manual download)

Archive found in this folder:

- `Markov Chain Attribution Data Set.zip`
	- Contains: `attribution data.csv`
	- Format: CSV (comma-separated)
	- Columns (6): `cookie`, `time`, `interaction`, `conversion`, `conversion_value`, `channel`

Notes for MTA:

- Each row is a touchpoint event for a user (`cookie`) at a given `time` on a given `channel`.
- `conversion` indicates whether the event is a conversion (0/1), and `conversion_value` is the value (often 0.0 for non-conversions).
- Typical Markov-attribution preprocessing groups by `cookie`, sorts by `time`, and uses `channel` as the state sequence.

Quick load (Pandas):

```python
import pandas as pd

df = pd.read_csv(
		"data/KAGGLE_MTA_MODELLING/Markov Chain Attribution Data Set.zip",
)
```

## Data dictionary (sample)

Profiled from a `nrows=20000` sample (types/missing may differ on full data):

| column | dtype (sample) | missing (sample) | example values |
|---|---:|---:|---|
| cookie | object | 0.0% | 00000FkCnDfDDf0iC97iC703B, 00000FkCnDfDDf0iC97iC703B, 00000FkCnDfDDf0iC97iC703B |
| time | object | 0.0% | 2018-07-03T13:02:11Z, 2018-07-17T19:15:07Z, 2018-07-24T15:51:46Z |
| interaction | object | 0.0% | impression, impression, impression |
| conversion | int64 | 0.0% | 0, 0, 0 |
| conversion_value | float64 | 0.0% | 0.0, 0.0, 0.0 |
| channel | object | 0.0% | Instagram, Online Display, Online Display |

## Journey / path construction

Suggested mapping:

- User / path id: `cookie`
- Time: `time` (parse ISO timestamps)
- Channel/state: `channel`
- Outcome: `conversion` (0/1) and optionally `conversion_value`

Typical preprocessing steps:

- Sort by (`cookie`, `time`).
- Build per-cookie sequences of `channel` (optionally filtered by `interaction` if you only want, e.g., clicks).
- For Markov attribution, represent conversions as terminal events (e.g. append `CONVERSION` to the path if any row has `conversion==1`, otherwise append `NULL`).

Example (sketch):

```python
import pandas as pd

df = pd.read_csv("data/KAGGLE_MTA_MODELLING/Markov Chain Attribution Data Set.zip")
df["time"] = pd.to_datetime(df["time"], errors="coerce", utc=True)
df = df.sort_values(["cookie", "time"])

seq = df.groupby("cookie")["channel"].apply(list)
converted = df.groupby("cookie")["conversion"].max().astype(int)
paths = seq.reset_index(name="channel_path").merge(converted.rename("converted_any"), on="cookie")
```

## Derived artifacts

This folder includes a derived per-user journey table:

- `derived/paths.csv` (generated)
	- Columns: `user_id`, `n_touches`, `converted_any`, `conversion_value_total`, `path_str`

Regenerate it from the repo root:

```bash
.venv/bin/python tools/build_ready_paths.py
```