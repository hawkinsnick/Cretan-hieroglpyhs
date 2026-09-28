# Release policy

Semantic versioning describes the corpus/API contract.

Patch releases correct errors without changing evidence semantics. Minor releases add backward-compatible records, metadata, analyses or optional schema fields. Major releases may change stable identifiers, required fields or evidence semantics and therefore require migration documentation.

Every release must synchronize `VERSION`, `CITATION.cff`, `corpus/manifest.json`, coverage metadata and changelog. Corpus counts are claims and must be reproducible from committed data.
