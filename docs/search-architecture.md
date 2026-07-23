# SEARCH & VECTOR DATABASE ARCHITECTURE

**Organization**: CRINE ([www.crine.in](https://www.crine.in))

---

## Overview

The ART schema is optimized for ingestion into:
* **SQLite / PostgreSQL**: FTS5 / pg_trgm full-text indexing on `text` and `citation`.
* **Meilisearch / Typesense**: Fast instant search and fuzzy matching.
* **Vector Databases (Qdrant, Pinecone, Milvus)**: Dense embedding vectors stored in verse records.
* **Knowledge Graphs (Neo4j, RDF)**: Inter-textual cross references and thematic links.
