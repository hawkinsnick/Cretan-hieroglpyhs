# Cretan Hieroglyphic Open Corpus

**2.0.0 — evidence-enrichment and audit platform**

A provenance-first research corpus for Cretan Hieroglyphic, designed for reproducible source checking and conservative comparison with Linear A, Cypro-Minoan and Linear B.

## What 2.0 adds
The stable 1.0 catalogue/sign identity contract is retained. 2.0 adds a formal ingestion lifecycle, verification events, field-level evidence packets, disagreement sets, corpus audit snapshots, evidence-readiness gates, and explicit derived-data lineage.

The corpus still distinguishes **coverage from verification**. All 331 CHIC catalogue identifiers are represented, while source-checked transcription/occurrence coverage remains whatever the committed audit actually demonstrates. No phonetic value is introduced by architecture or cross-script comparison.

## Evidence lifecycle
`catalogued → metadata-checked → transcription-checked → occurrence-checked → independently-reviewed`

A record may advance only with attributable evidence. Later stages do not erase earlier source readings or disagreements.

## Research family
This repository remains independent from `hawkinsnick/Linear-A`, `hawkinsnick/Cypro-Minoan`, and `hawkinsnick/Linear-B`. Shared Aegean interoperability is a projection layer, never a reason to merge native identifiers.

Primary catalogue reference: J.-P. Olivier and L. Godart, with J.-C. Poursat, *Corpus Hieroglyphicarum Inscriptionum Cretae*, Études Crétoises 31 (1996).
