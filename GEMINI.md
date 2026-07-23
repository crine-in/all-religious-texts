# GEMINI AI ASSISTANT REPOSITORY GUIDELINES

**Repository**: `all-religious-texts`  
**Organization**: CRINE ([github.com/crine-in](https://github.com/crine-in) | [www.crine.in](https://www.crine.in))

---

## Identity & Role

You are assisting as an Staff Data Architect, Open Source Maintainer, and Digital Archivist for **CRINE** on the **All Religious Texts (ART)** platform.

---

## Core Mission & Architecture Rules

1. **Specification Authority**: This repository (`all-religious-texts`) is the canonical specification, schema authority, and validation registry for the entire ART ecosystem.
2. **No Actual Corpus Datasets**: Do not store massive text corpora in this repo. Actual scripture datasets belong in downstream repositories (`art-hinduism`, `art-buddhism`, `art-christianity`, etc.). Samples are only permitted in `examples/`.
3. **Strict Schema Compliance**: All verse datasets must validate cleanly against `schemas/verse.schema.json` (Draft 2020-12).
4. **Master Registries**: Any new religion, collection, language, script, or license must be registered in `metadata/`.
5. **No Code Modification without Validation**: Always run `python3 validators/run_all.py` and `pytest tests/` after modifying schemas, tools, or metadata.

---

## Critical Commands

* **Run Full Validation Suite**:
  ```bash
  python3 validators/run_all.py
  ```
* **Run Unit Test Suite**:
  ```bash
  pytest tests/
  ```
* **Enrich Draft Dataset to Schema**:
  ```bash
  python3 tools/enrich_dataset.py --input isha.json --output examples/isha_enriched.json --book "Isha Upanishad"
  ```
* **Format & Checksums**:
  ```bash
  python3 scripts/format_json.py
  python3 scripts/generate_checksums.py
  ```

---

## Coding & Style Standards

* **Python**: Python 3.10+, Black formatting (line length 120), PEP 8, typing annotations.
* **JSON**: 2-space indentation, UTF-8 without BOM, deterministic key order.
* **Markdown**: GitHub Flavored Markdown, relative file links using `file://`.
* **File Naming**: Lowercase kebab-case for directories/schemas, `snake_case.py` for Python scripts.
