# SKILLS & REPOSITORY TOOLING REGISTRY

**Organization**: CRINE ([www.crine.in](https://www.crine.in))

---

## Agent Skills Overview

This document catalogs the executable tools, parsers, and validation skills available in the **`all-religious-texts`** specification repository.

---

## 1. Validation Skills (`validators/`)

| Skill / Command | File | Description |
| :--- | :--- | :--- |
| `run-all-validations` | `validators/run_all.py` | Runs the full 6-stage validation suite across all JSON files, schemas, IDs, UTF-8 encodings, filenames, and metadata. |
| `validate-json-syntax` | `validators/validate_json.py` | Validates JSON syntax across the repository. |
| `validate-schemas` | `validators/validate_schema.py` | Validates Draft 2020-12 JSON Schemas in `schemas/`. |
| `validate-identifiers` | `validators/validate_ids.py` | Verifies master ID uniqueness in `metadata/`. |
| `validate-utf8` | `validators/validate_utf8.py` | Verifies UTF-8 encoding and Unix line endings (LF). |
| `validate-filenames` | `validators/validate_filenames.py` | Enforces lowercase kebab-case directory naming conventions. |

---

## 2. Ingestion & Conversion Skills (`tools/`)

| Skill / Tool | Command Example | Description |
| :--- | :--- | :--- |
| `enrich-draft-dataset` | `python3 tools/enrich_dataset.py --input <file.json> --output <out.json> --book "<Title>"` | Enriches draft datasets (e.g. `isha.json`, `katha.json`) into canonical `verse.schema.json`. |
| `convert-txt-to-json` | `python3 tools/txt_to_json.py --input <file.txt> --output <out.json>` | Parses plain text or verse-marked text into verse schema. |
| `convert-xml-to-json` | `python3 tools/xml_to_json.py --input <file.xml> --output <out.json>` | Ingests XML verse nodes into JSON schema. |
| `convert-tei-to-json` | `python3 tools/tei_to_json.py --input <file.xml> --output <out.json>` | Parses TEI P5 digital humanities XML markups. |
| `convert-md-to-json` | `python3 tools/md_to_json.py --input <file.md> --output <out.json>` | Converts Markdown verse listings to JSON. |
| `convert-csv-to-json` | `python3 tools/csv_to_json.py --input <file.csv> --output <out.json>` | Ingests tabular CSV scriptures. |

---

## 3. Maintenance & Packaging Skills (`scripts/`)

| Skill / Script | Command Example | Description |
| :--- | :--- | :--- |
| `format-json` | `python3 scripts/format_json.py` | Formats all JSON files with 2-space indent and sorted keys. |
| `generate-checksums` | `python3 scripts/generate_checksums.py` | Generates SHA-256 hashes for all verse text fields. |
| `renumber-verses` | `python3 scripts/renumber_verses.py <file.json>` | Renumbers verse citations and external IDs. |
| `check-links` | `python3 scripts/link_checker.py` | Validates relative links across documentation markdown files. |
