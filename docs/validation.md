# VALIDATION SUITE DOCUMENTATION

**Organization**: CRINE ([www.crine.in](https://www.crine.in))

---

## Validation Tools Overview

Run all checks via CLI:

```bash
python3 validators/run_all.py
```

Checks performed:
1. `validate_json.py`: Syntax check across all `.json` files.
2. `validate_schema.py`: JSON Schema Draft 2020-12 verification.
3. `validate_ids.py`: Master identifier uniqueness check.
4. `validate_utf8.py`: UTF-8 character encoding verification.
5. `validate_filenames.py`: Lowercase kebab-case naming check.
6. `validate_metadata.py`: Registry completeness verification.
