- [Shapley Value Attribution Modeling](https://www.kaggle.com/code/jasonbrewster/shapley-value-attribution-modeling/input)
- DATA: [Marketing campaign](https://www.kaggle.com/datasets/kavitabhagwani/marketing-campaign)

## Local data (manual download)

Archive found in this folder:

- `archive.zip`
	- Contains: `marketing.csv`
	- Format: CSV (comma-separated)
	- Columns (12): `user_id`, `date_served`, `marketing_channel`, `variant`, `converted`, `language_displayed`, `language_preferred`, `age_group`, `date_subscribed`, `date_canceled`, `subscribing_channel`, `is_retained`

Notes for MTA:

- This dataset is suitable for channel attribution/impact analysis with a conversion outcome.
- `marketing_channel` is the channel/treatment; `converted` is the outcome (TRUE/FALSE).
- If you need path-based MTA (multi-step journeys), you typically need user-level sequences; here you may have 1+ exposures per `user_id` depending on the data.

Quick load (Pandas):

```python
import pandas as pd

df = pd.read_csv(
		"data/KAGGLE_SHAPLEY_MTA/archive.zip",
)
```

## Data dictionary (sample)

Profiled from a `nrows=5000` sample (types/missing may differ on full data):

| column | dtype (sample) | missing (sample) | example values |
|---|---:|---:|---|
| user_id | object | 0.0% | a100000029, a100000030, a100000031 |
| date_served | object | 0.0% | 1/1/18, 1/1/18, 1/1/18 |
| marketing_channel | object | 0.0% | House Ads, House Ads, House Ads |
| variant | object | 0.0% | personalization, personalization, personalization |
| converted | bool | 0.0% | True, True, True |
| language_displayed | object | 0.0% | English, English, English |
| language_preferred | object | 0.0% | English, English, English |
| age_group | object | 0.0% | 0-18 years, 19-24 years, 24-30 years |
| date_subscribed | object | 63.7% | 1/1/18, 1/1/18, 1/1/18 |
| date_canceled | object | 88.6% | 1/18/18, 2/22/18, 3/9/18 |
| subscribing_channel | object | 63.7% | House Ads, House Ads, House Ads |
| is_retained | object | 63.7% | True, True, True |

## Journey / path construction

This dataset is not a pre-built “path” table; you typically construct user-level sequences from repeated exposures.

Suggested mapping:

- User / path id: `user_id`
- Time: `date_served` (parse to datetime)
- Channel/state: `marketing_channel` (optionally split by `variant`)
- Outcome: `converted` (TRUE/FALSE)

Typical preprocessing steps:

- Sort by (`user_id`, `date_served`) and build per-user ordered channel lists.
- Decide the attribution unit: last touch before conversion date, or all touches within a lookback window.
- If you only want one conversion per user, collapse to the first conversion (or last conversion) per `user_id`.

Example (sketch):

```python
import pandas as pd

df = pd.read_csv("data/KAGGLE_SHAPLEY_MTA/archive.zip")
df["date_served"] = pd.to_datetime(df["date_served"], errors="coerce")
df = df.sort_values(["user_id", "date_served"])

paths = (
		df.groupby("user_id")["marketing_channel"]
			.apply(list)
			.reset_index(name="channel_path")
)
labels = df.groupby("user_id")["converted"].max().reset_index(name="converted_any")
```

## Derived artifacts

- `derived/paths.csv`: per-user channel path table (generated).

Regenerate:

```sh
/home/mconde/FORMACIÓN/EM/.venv/bin/python tools/build_ready_paths.py
```