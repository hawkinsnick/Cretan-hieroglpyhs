# Cretan Hieroglyphic Open Corpus

**1.0.0 — stable evidence architecture and catalogue foundation**

A provenance-first, machine-readable research corpus for Cretan Hieroglyphic. The project preserves scholarly disagreement, separates observation from interpretation, and supports reproducible comparison with Linear A, Cypro-Minoan and Linear B without importing decipherment assumptions into native data.

## Stable 1.0 contract
- canonical object IDs are `CHIC-###`;
- the CHIC 1996 catalogue spine contains 331 records;
- H 001–122, I 123–179, S 180–315, Y 316–331 remain explicit catalogue series;
- the numbered core sign registry contains 96 entries and asserts no phonetic values;
- object, surface, sign-occurrence, transcription, assertion and crosswalk layers remain separable;
- source-derived claims require provenance;
- cross-script relationships are attributable claims, never native sign-ID aliases;
- catalogue presence is never represented as source-checked transcription coverage;
- unknown values remain unknown rather than being reconstructed.

## Research family
`hawkinsnick/Linear-A`, `hawkinsnick/Cypro-Minoan`, `hawkinsnick/Linear-B`, and this repository retain independent release histories while sharing an Aegean Epigraphy Interchange boundary.

## Current evidence coverage
1.0.0 establishes a complete catalogue **spine**, not a complete epigraphic edition: 331/331 CHIC identifiers are represented; detailed source-checked transcriptions remain a subsequent enrichment phase. See `corpus/manifest.json` and `QUALITY.md`.

Primary reference: J.-P. Olivier and L. Godart, with J.-C. Poursat, *Corpus Hieroglyphicarum Inscriptionum Cretae*, Études Crétoises 31 (1996).

See `CONTRIBUTING.md`, `RESEARCH_ETHICS.md`, `docs/CORPUS_MODEL.md`, and `docs/INTEROPERABILITY.md` before contributing.
