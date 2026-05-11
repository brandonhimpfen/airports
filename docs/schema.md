# Dataset Schema

The main dataset is `data/airports.csv`.

| Field | Type | Description |
|---|---:|---|
| `code` | string | Airport identifier from the original source. Usually an IATA code, but some records use four-character identifiers. |
| `code_type` | string | Inferred code category: `iata`, `icao`, or `local_or_unknown`. |
| `name` | string | Airport name with whitespace normalized. |
| `latitude` | number | Decimal latitude. Must be between -90 and 90. |
| `longitude` | number | Decimal longitude. Must be between -180 and 180. |

## Notes

The original dataset used the field name `airport-id`. This version renames it to `code` because the values are not guaranteed to be numeric IDs. The `code_type` field is inferred from the code format and should be treated as a convenience field, not a verified aviation authority classification.
