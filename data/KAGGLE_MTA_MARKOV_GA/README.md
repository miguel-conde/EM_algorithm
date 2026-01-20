[Multitouch Attribution Markov Google Analytics](https://www.kaggle.com/code/alyassi/multitouch-attribution-markov-google-analytics/input)

Data from: https://bigquery.cloud.google.com/table/bigquery-public-data:google_analytics_sample.ga_sessions_20170801

## Local data (manual download)

No local archive (`.zip`) was found in this folder.

Notes:

- The referenced source is a public BigQuery table (`bigquery-public-data.google_analytics_sample.ga_sessions_20170801`).
- To work locally, you typically export a query result to CSV/Parquet (e.g., flattening hits into event-level rows), then place the exported file(s) in this folder and document them here.

## Journey / path construction

When exporting GA sessions, you typically aim to build event-level rows with:

- User / path id: `fullVisitorId` (or `clientId` depending on export)
- Time: hit timestamp (or session start + hit offset)
- Channel/state: a marketing channel dimension (e.g., `trafficSource.medium` / `source` / `channelGrouping`)
- Outcome: a conversion event (e.g., transaction/revenue, goal completion)

Then:

- Sort by (user id, time) and build per-user sequences.
- Add terminal states (`CONVERSION`/`NULL`) for Markov attribution.

## Derived artifacts

No `derived/paths.csv` is generated for this folder yet because there is no local export file present.

If you export the GA table to an event-level CSV/Parquet and place it here, we can extend `tools/build_ready_paths.py` with a GA builder.