#!/usr/bin/env python3
"""Validate the airports dataset."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

DATASET = Path(__file__).resolve().parents[1] / "data" / "airports.csv"
REQUIRED_FIELDS = ["code", "code_type", "name", "latitude", "longitude"]
VALID_CODE_TYPES = {"iata", "icao", "local_or_unknown"}
CODE_RE = re.compile(r"^[A-Z0-9-]+$")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def main() -> None:
    if not DATASET.exists():
        fail(f"Missing dataset: {DATASET}")

    seen_codes: dict[str, int] = {}
    errors: list[str] = []

    with DATASET.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != REQUIRED_FIELDS:
            fail(f"Expected header {REQUIRED_FIELDS}, found {reader.fieldnames}")

        for row_num, row in enumerate(reader, start=2):
            code = row["code"].strip()
            code_type = row["code_type"].strip()
            name = row["name"].strip()

            if not code:
                errors.append(f"row {row_num}: missing code")
            elif not CODE_RE.fullmatch(code):
                errors.append(f"row {row_num}: invalid code {code!r}")

            if code_type not in VALID_CODE_TYPES:
                errors.append(f"row {row_num}: invalid code_type {code_type!r}")

            if not name:
                errors.append(f"row {row_num}: missing name")
            if name != row["name"]:
                errors.append(f"row {row_num}: name has leading or trailing whitespace")

            try:
                latitude = float(row["latitude"])
                longitude = float(row["longitude"])
            except ValueError:
                errors.append(f"row {row_num}: latitude/longitude must be numeric")
                continue

            if not -90 <= latitude <= 90:
                errors.append(f"row {row_num}: latitude out of range")
            if not -180 <= longitude <= 180:
                errors.append(f"row {row_num}: longitude out of range")

            seen_codes[code] = seen_codes.get(code, 0) + 1

    duplicate_codes = sorted(code for code, count in seen_codes.items() if count > 1)
    if duplicate_codes:
        print(f"WARNING: duplicate codes found: {', '.join(duplicate_codes[:20])}")
        if len(duplicate_codes) > 20:
            print(f"WARNING: {len(duplicate_codes) - 20} more duplicate codes omitted")

    if errors:
        for error in errors[:100]:
            print(f"ERROR: {error}")
        if len(errors) > 100:
            print(f"ERROR: {len(errors) - 100} more errors omitted")
        sys.exit(1)

    print(f"Validated {sum(seen_codes.values())} airport records.")


if __name__ == "__main__":
    main()
