# DATA LICENSE POLICY

**Organization**: CRINE ([github.com/crine-in](https://github.com/crine-in) | [www.crine.in](https://www.crine.in))  
**Repository**: `all-religious-texts`

---

## Overview

The **All Religious Texts (ART)** ecosystem operates under a strict, clear, transparent, and legal licensing framework designed to protect open digital humanities while respecting intellectual property and original copyright constraints.

---

## 1. Core Repository Infrastructure & Tools

All code, CLI utilities, validation scripts, GitHub actions, OpenAPI specifications, and build tooling contained in this repository are licensed under the **[MIT License](LICENSE)**.

---

## 2. Universal Schemas & Metadata

All original schemas (`schemas/*.schema.json`), metadata structures (`metadata/*.json`), cross-reference indexes, and documentation created by CRINE are published under the **[Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)**.

### Human-Readable Summary of CC BY 4.0:
You are free to:
* **Share** — copy and redistribute the metadata in any medium or format.
* **Adapt** — remix, transform, and build upon the metadata for any purpose, even commercially.

Under the following terms:
* **Attribution** — You must give appropriate credit to **CRINE**, provide a link to the license, and indicate if changes were made.

---

## 3. Imported Texts & Scriptures

Textual corpus datasets residing across the ART ecosystem repositories (`art-hinduism`, `art-buddhism`, `art-christianity`, `art-islam`, etc.) must strictly adhere to the following rules:

1. **Preservation of Original Licenses**: Every imported scripture or translation **must preserve its original license**. We never overwrite, upgrade, or strip existing licenses.
2. **Public Domain Verification**: Sacred texts that are in the Public Domain (e.g. ancient historical texts, classical translations where copyright has expired) are designated as `Public Domain` / `CC0`.
3. **Open Access & Creative Commons**: Translations available under Creative Commons licenses (e.g. CC BY-SA, CC BY-NC) retain their exact license terms and require strict attribution in `ATTRIBUTION.md`.
4. **No Unverified Texts**: No text may be added to any ART repository without verified copyright status and provenance notes.

---

## 4. Provenance & Metadata Requirements

Every text edition in the ART ecosystem must contain a corresponding `metadata.json` specifying:

```json
{
  "title": "Text Title",
  "license": "Public Domain / CC BY 4.0 / CC BY-SA 4.0",
  "sourceUrl": "https://example.org/source",
  "attribution": "Original author / translator attribution notice",
  "provenance": "Details of acquisition, transcription, and verification",
  "retrievalDate": "YYYY-MM-DD"
}
```

---

## 5. Takedown & Integrity Policy

If you believe any text indexed or included in the ART ecosystem violates a valid copyright, please submit an issue or contact CRINE at `legal@crine.in`. We will review and act upon valid requests immediately.
