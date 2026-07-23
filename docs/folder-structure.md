# DIRECTORY & FILE NAMING CONVENTIONS

**Organization**: CRINE ([www.crine.in](https://www.crine.in))

---

## Ecosystem Repository Layout

Downstream corpus repositories (e.g. `art-hinduism`, `art-buddhism`) strictly mirror this directory layout:

```text
data/
└── <religion-id>/
    └── <collection-id>/
        └── <book-id>/
            ├── metadata.json       # Required book-level metadata
            ├── LICENSE             # Text edition license
            ├── ATTRIBUTION.md      # Provenance and source notes
            ├── sources.md          # Bibliographic details
            ├── iast.json           # Primary script dataset
            ├── devanagari.json     # Original script dataset
            └── english/            # Translations sub-directory
                ├── max-muller.json
                └── translator-name.json
```

## Naming Standards

1. **Directories**: Lowercase kebab-case (`katha-upanishad`, `dhammapada`, `genesis`).
2. **Schema Files**: `lowercase.schema.json` in `schemas/`.
3. **Master Registries**: `lowercase-plural.json` in `metadata/`.
4. **Python Code**: `snake_case.py` in `validators/`, `tools/`, `scripts/`.
