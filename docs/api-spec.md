# REST & GRAPHQL API SPECIFICATION

**Organization**: CRINE ([www.crine.in](https://www.crine.in))

---

## Endpoint Overview

Complete OpenAPI 3.0 specification is available in `api/openapi.yaml`.

### Primary Endpoints:
* `GET /religions` - List supported religious traditions
* `GET /collections` - List text collections
* `GET /books` - Query books & scriptures
* `GET /books/{id}` - Get book structural metadata
* `GET /verses` - Query verses by citation, collection, or religion
* `GET /search` - Full-text and vector semantic search
* `GET /random` - Return random verse
* `GET /translations` - List available verse translations
* `GET /commentaries` - Query verse commentaries
