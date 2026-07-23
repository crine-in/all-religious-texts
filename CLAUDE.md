# CLAUDE.md - Instructions for Claude Code

## Commands
- Run Validation Suite: `python3 validators/run_all.py`
- Run Tests: `pytest tests/`
- Enrich Draft: `python3 tools/enrich_dataset.py --input isha.json --output examples/isha_enriched.json --book "Isha Upanishad"`
- Format JSON: `python3 scripts/format_json.py`

## Architecture & Code Style
- Schemas: Draft 2020-12 in `schemas/*.schema.json`
- Python: Black line length 120, standard library + jsonschema/pyyaml
- Directory structure: lowercase kebab-case
