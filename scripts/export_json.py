#!/usr/bin/env python3
"""Export data/airports.csv to data/airports.json."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "airports.csv"
JSON_PATH = ROOT / "data" / "airports.json"


def main() -> None:
    with CSV_PATH.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))

    for row in rows:
        row["latitude"] = float(row["latitude"])
        row["longitude"] = float(row["longitude"])

    JSON_PATH.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Exported {len(rows)} records to {JSON_PATH}")


if __name__ == "__main__":
    main()
