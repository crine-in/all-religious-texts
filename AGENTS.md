# AGENT COORDINATION PROTOCOL

**Organization**: CRINE ([www.crine.in](https://www.crine.in))

---

## Autonomous Agent Instructions

When operating autonomously or in pair programming mode on **`all-religious-texts`**:

1. **Read Knowledge Registries**: Inspect `metadata/` before creating or referencing new religions, languages, scripts, or licenses.
2. **Execute Validation Suite**: Never declare completion of a task without verifying `python3 validators/run_all.py` and `pytest tests/`.
3. **Preserve License Provenance**: Never change original copyright declarations of text editions.
4. **Follow Schema Standards**: Strictly validate output against `schemas/verse.schema.json`.
