#!/usr/bin/env python3
"""Generate summary statistics for the airports dataset."""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "airports.csv"
STATS_PATH = ROOT / "data" / "stats.json"


def main() -> None:
    with CSV_PATH.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))

    stats = {
        "record_count": len(rows),
        "field_count": len(rows[0]) if rows else 0,
        "code_type_counts": dict(Counter(row["code_type"] for row in rows)),
        "generated_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    }
    STATS_PATH.write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {STATS_PATH}")


if __name__ == "__main__":
    main()
