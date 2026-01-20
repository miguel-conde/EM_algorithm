[Criteo Attribution Modeling for Bidding Dataset](https://www.kaggle.com/datasets/sharatsachin/criteo-attribution-modeling)

## Local data (manual download)

Archive found in this folder:

- `archive.zip`
	- Contains: `pcb_dataset_final.tsv`
	- Format: TSV (tab-separated)
	- Columns (22): `timestamp`, `uid`, `campaign`, `conversion`, `conversion_timestamp`, `conversion_id`, `attribution`, `click`, `click_pos`, `click_nb`, `cost`, `cpo`, `time_since_last_click`, `cat1`, `cat2`, `cat3`, `cat4`, `cat5`, `cat6`, `cat7`, `cat8`, `cat9`

Notes for MTA:

- Each row represents a (user, campaign) touchpoint sequence with conversion-related fields.
- `uid` can be used as the path/customer identifier; `campaign` as the marketing channel/campaign identifier.
- `conversion` is the conversion flag (0/1).

Quick load (Pandas):

```python
import pandas as pd

df = pd.read_csv(
		"data/KAGGLE_CRITEO/archive.zip",
		sep="\t",
)
```

## Data dictionary (sample)

Profiled from a `nrows=200000` sample (types/missing may differ on full data):

| column | dtype (sample) | missing (sample) | example values |
|---|---:|---:|---|
| timestamp | int64 | 0.0% | 0, 2, 2 |
| uid | int64 | 0.0% | 20073966, 24607497, 28474333 |
| campaign | int64 | 0.0% | 22589171, 884761, 18975823 |
| conversion | int64 | 0.0% | 0, 0, 0 |
| conversion_timestamp | int64 | 0.0% | -1, -1, -1 |
| conversion_id | int64 | 0.0% | -1, -1, -1 |
| attribution | int64 | 0.0% | 0, 0, 0 |
| click | int64 | 0.0% | 0, 0, 0 |
| click_pos | int64 | 0.0% | -1, -1, -1 |
| click_nb | int64 | 0.0% | -1, -1, -1 |
| cost | float64 | 0.0% | 1e-05, 1e-05, 0.000182758497011 |
| cpo | float64 | 0.0% | 0.390793596019, 0.0596001963727, 0.149706229845 |
| time_since_last_click | int64 | 0.0% | -1, 423858, 8879 |
| cat1 | int64 | 0.0% | 5824233, 30763035, 138937 |
| cat2 | int64 | 0.0% | 9312274, 9312274, 9312274 |
| cat3 | int64 | 0.0% | 3490278, 14584482, 10769841 |
| cat4 | int64 | 0.0% | 29196072, 29196072, 29196072 |
| cat5 | int64 | 0.0% | 11409686, 11409686, 5824237 |
| cat6 | int64 | 0.0% | 1973606, 1973606, 138937 |
| cat7 | int64 | 0.0% | 25162884, 22644417, 1795451 |
| cat8 | int64 | 0.0% | 29196072, 9312274, 29196072 |
| cat9 | int64 | 0.0% | 29196072, 21091111, 15351056 |

## Journey / path construction

This file is large and the “journey” definition depends on how you interpret events (impression/click) and conversion identifiers.

Suggested mapping (best-effort):

- User / path id: `uid`
- Time ordering: `timestamp` (and/or `conversion_timestamp`)
- Channel/state: `campaign`
- Outcome: `conversion` (0/1); conversion identity via `conversion_id` (and timestamp via `conversion_timestamp`)

Typical preprocessing ideas:

- Sort by (`uid`, `timestamp`) and build per-user sequences of `campaign`.
- If you want per-conversion journeys (recommended when users can convert multiple times), group by (`uid`, `conversion_id`) and take only events up to `conversion_timestamp`.
- Decide whether to keep all events or only clicked events (`click==1`).

Example (sketch):

```python
import pandas as pd

df = pd.read_csv("data/KAGGLE_CRITEO/archive.zip", sep="\t")
df = df.sort_values(["uid", "timestamp"])

paths = df.groupby("uid")["campaign"].apply(list).reset_index(name="campaign_path")
labels = df.groupby("uid")["conversion"].max().reset_index(name="converted_any")
```

## Derived artifacts

This folder includes a derived per-user journey table:

- `derived/paths.csv` (generated)

Regenerate it from the repo root:

```bash
.venv/bin/python tools/build_ready_paths.py --criteo-max-rows 200000
```

Notes:

- For Criteo, `derived/paths.csv` is built from a row sample by default (the full TSV is very large).
- Increase `--criteo-max-rows` if you want longer paths.