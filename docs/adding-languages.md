# ADDING NEW LANGUAGES & SCRIPTS

**Organization**: CRINE ([www.crine.in](https://www.crine.in))

---

## Adding Languages to Registry

1. Open `metadata/languages.json`.
2. Add language record with ISO 639-1 / ISO 639-3 codes.
3. Open `metadata/scripts.json` if a new script is required (ISO 15924).
4. Run `python validators/validate_ids.py` to confirm uniqueness.
