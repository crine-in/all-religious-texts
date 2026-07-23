# ECOSYSTEM ARCHITECTURE SPECIFICATION

**Organization**: CRINE ([github.com/crine-in](https://github.com/crine-in) | [www.crine.in](https://www.crine.in))

---

## High-Level Architecture Overview

The **All Religious Texts (ART)** platform is designed as a distributed, multi-repository digital humanities archive and computational platform.

```
                   +---------------------------------------+
                   |         all-religious-texts           |
                   |   Canonical Standard & Specification   |
                   +-------------------+-------------------+
                                       |
           +---------------------------+---------------------------+
           |                           |                           |
+----------v----------+     +----------v----------+     +----------v----------+
|     art-hinduism    |     |     art-buddhism    |     |   art-christianity  |
| (Corpus Repositories)|     | (Corpus Repositories)|     | (Corpus Repositories)|
+---------------------+     +---------------------+     +---------------------+
```

### Key Architectural Principles

1. **Decoupled Corpus Data**: Core schemas, CLI validation tools, and API specifications live in `all-religious-texts`. Specific scripture datasets reside in dedicated downstream repositories (`art-hinduism`, `art-buddhism`, `art-christianity`, etc.).
2. **Schema-Driven Compliance**: Every dataset must strictly validate against `schemas/verse.schema.json` and `schemas/metadata.schema.json`.
3. **Immutable Identifiers**: Verse IDs follow deterministic global paths (`religion:collection:book:citation`).
4. **Multi-Format Ingestion**: Ingest TXT, XML, TEI, MD, CSV, EPUB, PDF into standardized JSON.
