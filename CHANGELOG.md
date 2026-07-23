# CHANGELOG

All notable changes to the **`all-religious-texts`** specification, schemas, tools, and validation suite will be documented in this file.

The project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-07-23

### Added
* Initialized canonical repository foundation for **CRINE** ([www.crine.in](https://www.crine.in)).
* Defined Draft 2020-12 JSON Schemas in `schemas/`:
  * `verse.schema.json`
  * `book.schema.json`
  * `translation.schema.json`
  * `commentary.schema.json`
  * `metadata.schema.json`
  * `license.schema.json`
  * `cross-reference.schema.json`
  * `contributor.schema.json`
  * `language.schema.json`
  * `script.schema.json`
  * `edition.schema.json`
* Master metadata registries in `metadata/`:
  * `religions.json`, `collections.json`, `languages.json`, `scripts.json`, `licenses.json`.
* Python CLI Validation suite in `validators/`:
  * `run_all.py`, `validate_json.py`, `validate_schema.py`, `validate_ids.py`, `validate_utf8.py`, `validate_filenames.py`, `validate_metadata.py`.
* Multiformat ingestion utilities in `tools/`:
  * `txt_to_json.py`, `xml_to_json.py`, `md_to_json.py`, `csv_to_json.py`, `tei_to_json.py`, `epub_parser.py`, `pdf_metadata.py`.
* Dataset formatting & maintenance scripts in `scripts/`:
  * `format_json.py`, `generate_checksums.py`, `renumber_verses.py`, `link_checker.py`, `bulk_convert.py`.
* OpenAPI 3.0 API Specification in `api/openapi.yaml`.
* Packages specifications and stubs in `packages/` (JS, Python, Go, Rust, Flutter).
* CI GitHub Actions workflows in `.github/workflows/` (`validate.yml`, `lint.yml`, `release.yml`).
* Complete developer and architecture documentation in `docs/`.
