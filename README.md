# Airports Dataset

[![DOI](https://zenodo.org/badge/361875952.svg)](https://doi.org/10.5281/zenodo.20127440) 
[![Support Open Work](https://img.shields.io/badge/Support-Open%20Work-0A0A0A?style=flat&logo=github)](https://github.com/brandonhimpfen/support) 

A cleaned, structured, open dataset of airports with airport codes, names, and geographic coordinates.

## Dataset Files

| File | Description |
|---|---|
| `data/airports.csv` | Main dataset in CSV format. |
| `data/airports.json` | JSON export for applications and APIs. |
| `data/airport-names.txt` | Plain-text list of airport names. |
| `data/airports.dat` | Pipe-delimited data export. |
| `data/stats.json` | Basic dataset summary statistics. |

## Fields

| Field | Description |
|---|---|
| `code` | Airport identifier from the original dataset. |
| `code_type` | Inferred code category: `iata`, `icao`, or `local_or_unknown`. |
| `name` | Airport name. |
| `latitude` | Decimal latitude. |
| `longitude` | Decimal longitude. |

## Current Size

This release contains **5,571 airport records**.

## Example

```csv
code,code_type,name,latitude,longitude
AAA,iata,Anaa,-17.3542,-145.4961
AAC,iata,EL-ARISH,31.0733,33.8358
```

## Validation

Run the validation script before publishing changes:

```bash
python scripts/validate.py
```

The script checks required headers, coordinates, blank values, code formatting, and leading or trailing whitespace in names.

## Recommended Future Improvements

Future releases could add country, country code, municipality, region, timezone, airport type, operational status, IATA/ICAO reconciliation, and source-level provenance for each record.

## Citation

Citation metadata is available in `CITATION.cff`.

## License

This project is licensed under the MIT License.
