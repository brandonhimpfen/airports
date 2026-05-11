# Contributing

Contributions are welcome. Please keep changes small, verifiable, and consistent with the dataset schema.

Before opening a pull request:

1. Update `data/airports.csv`.
2. Run `python scripts/export_json.py`.
3. Run `python scripts/generate_stats.py`.
4. Run `python scripts/validate.py`.
5. Document any source or methodology changes in `docs/sources.md`.

When adding or correcting records, include a reliable source in the pull request description.
