# tracewise

Tracewise turns MySQL slow query logs into a ranked performance report. It groups similar queries using normalized fingerprints and highlights the biggest hotspots by total time, average time, and execution count.

Built for backend engineers and SREs running Java/Spring services on MySQL (including AWS RDS), tracewise helps you decide what to optimize first from offline slow logs.

## Why tracewise?
Slow query logs are noisy, repetitive, and hard to prioritize. Tracewise aggregates similar statements into fingerprints, ranks them by impact, and produces a concise report you can act on immediately.

## Features
- Parse MySQL slow query logs
- Rank queries by total time, avg time, count
- Output formats: text and JSON
- Query fingerprinting / normalization

## Install
```bash
pip install tracewise
```

Requires Python 3.10+.

## Quickstart
Analyze a slow log and print a text report:
```bash
tracewise analyze --input slow.log
```

Output JSON for scripting and dashboards:
```bash
tracewise analyze --input slow.log --format json
```

Show only the top 20 queries by total time:
```bash
tracewise analyze --input slow.log --top 20
```

Ignore fast queries under 0.5s (Query_time):
```bash
tracewise analyze --input slow.log --min-time 0.5
```

Flag reference:
- `--input`: path to the slow query log file
- `--format`: output format (`text` or `json`)
- `--top`: limit the number of ranked queries
- `--min-time`: minimum Query_time to include (seconds)

## Example output
Text report (top 3):
```
Rank  Total(s)  Avg(s)  Count  P95(s)  RowsExam  Fingerprint
1     245.20    0.98    250    1.84    1200      SELECT * FROM orders WHERE user_id = ? AND status = ?
2     122.55    0.49    250    0.96    3400      UPDATE carts SET updated_at = ? WHERE id = ?
3      88.10    1.76     50    2.30     900      SELECT id, total FROM invoices WHERE created_at > ?
```

JSON snippet:
```json
{
  "fingerprint": "SELECT * FROM orders WHERE user_id = ? AND status = ?",
  "count": 250,
  "total_time": 245.2,
  "avg_time": 0.98,
  "p95_time": 1.84,
  "rows_examined": 1200
}
```

## How it works
1) Parse slow log entries
2) Extract `Query_time`, `Rows_examined`, and SQL text
3) Normalize SQL by replacing literals with `?` to build fingerprints
4) Aggregate metrics per fingerprint and compute percentiles

## Roadmap
- MVP complete
- Better SQL normalization
- Support Percona slow log variations
- Spring Boot correlation module (request ID / endpoint mapping)
- Optional LLM assistant for explanations (opt-in, privacy-friendly)

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for setup and guidelines. Good first issues are labeled `good first issue`. Please follow code style and add tests for new functionality.

## Security & Privacy
Tracewise runs locally and does not send data to external services. Slow logs can contain sensitive data; handle them carefully and consider redacting before sharing.

## License
MIT
