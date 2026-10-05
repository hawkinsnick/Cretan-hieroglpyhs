# Context and review dossiers

Adds 234 source-attributed contextual assertions on 26 CHIC entries from 29 INSCRIBE catalogue pages; three unnumbered pages remain excluded source leads. All 331 identities have reproducible review dossiers. Script alternatives, unknown findspots and chronology qualifiers remain literal. Five readings on two objects and zero independent reviews remain unchanged.

For a readable view, open [record dossiers](RECORD-DOSSIERS.md). For an inscription, find its `record_id` in `research/record-dossiers.json`. Follow `native_ref` to the canonical evidence. Read source-specific assertions and their locators separately from encoded readings/occurrences. Read `missing_evidence` before drawing conclusions. A source-reported findspot, date or script classification is an attributed assertion, not an independent project finding.

Use `analysis/context-coverage-v1.json` to check the denominator. The 26 context objects span H=8, I=1, S=14, Y=3; these metadata counts do not satisfy the representative reading cohort. Unknown findspots and question marks remain explicit. INSCRIBE models, photographs and transnumerations are not added by this metadata-only layer. Three pages without explicit CHIC numbers remain excluded source leads. CHIC/CMS ancestry prevents treating the database as an independent reading witness.

Rebuild: `python scripts/research_dossiers.py --write`. Verify: `python scripts/research_dossiers.py` and `python scripts/test_research_dossiers.py`. The coverage audit pins all native inputs by SHA-256. Counts and dossiers must replay exactly; orphan sources and generated-view tampering are rejected. Independent review, palaeographic adjudication and linguistic interpretation remain separate future work.
