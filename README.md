# Cretan Hieroglyphic Open Corpus

## AI research skill

This corpus project includes a vendor-neutral, evidence-first AI research skill in [`ai-skill/`](ai-skill/). The corpus remains the scholarly source of truth; the skill is an interface to it, not a second corpus and not an independent authority.

Researchers using ChatGPT, Claude, Gemini, or another capable model can provide the repository (or its AI-ready bundle) together with [`ai-skill/SKILL.md`](ai-skill/SKILL.md). The skill requires the model to preserve provenance, uncertainty, exclusions, source dependence, rights, and this project's scientific gates. Before substantive use, check [`ai-skill/generated/source-state.json`](ai-skill/generated/source-state.json) and the generated research-bundle index for the corpus commit represented by the AI package.

For questions spanning multiple corpus projects, use the **Combined Corpus Research AI** documented in the Linear A repository under [`combined-ai-skill/`](https://github.com/hawkinsnick/Linear-A/tree/ai-skill-v0.1/combined-ai-skill). It orchestrates the registered individual skills while keeping their evidence models and rights separate. Membership in the combined system does **not** imply linguistic relationship, sign equivalence, chronology, decipherment, or independent replication.

## Current status — 5.2.6

Adds five printed CHIC1996 transnumerations on two Knossos medallions from public publisher pages 91 and 93, with source-image digests and exact locators. Literal X marks, hyphenated groups and numerical notation remain preserved. This H-series convenience pilot has zero independent reviews; representative and comparative experiments remain blocked.

Family contract 1.2 aligns all five projects with [Phaistos Disc 1.6.0](https://github.com/hawkinsnick/Phaistos-Disc/releases/tag/v1.6.0). The shared readiness report preserves native sampling units, source rights and blocked linguistic controls. It authorizes no pooling or linguistic relationship claim. See [`research/family-readiness-v1.json`](research/family-readiness-v1.json).

The authoritative current gate summary is [`analysis/current-status.json`](analysis/current-status.json). Historical release reports below retain their original versions and claims.

Validate this checkout with:

```sh
python -m pip install -r requirements-validation.txt
python scripts/validate_current_state.py
python scripts/test_current_state.py
```


**5.0.0 — critical corpus production contract**

A provenance-first, source-critical and reproducible research corpus for Cretan Hieroglyphic.

5.0 turns the mature 4.x engineering platform into a stable production contract for inscription-level critical evidence. It adds exact-locator critical readings, source-access and redistribution controls, versioned corpus snapshots, explicit research boundaries and compatibility with the cross-project matched-information-environment protocol.

The foundation remains 331 CHIC catalogue-spine records and a 96-entry numbered core registry inside the broader multi-repertoire model. No native phonetic values are asserted. At the historical 5.0 baseline, critical readings, source-checked occurrences and independent reviews were zero. The current source-access pilot above adds readings while independent review remains pending.

**Blocked is a valid scientific result.** Internal structural analysis, CH–Linear A comparison and fine matched-degradation experiments remain blocked by their predeclared evidence requirements.


The shared family report now targets the Disc [2.0.0-rc.2 prerelease](https://github.com/hawkinsnick/Phaistos-Disc/releases/tag/v2.0.0-rc.2). Final independently reviewed Disc 2.0 remains blocked; compatibility does not confer linguistic equivalence or independent review. Native evidence and this repository’s release version are unchanged.

### Research evidence workbench 1.0

Download the research workbench ZIP, extract it, and open [workbench/evidence.html](workbench/evidence.html). It includes searchable pinned evidence, coverage definitions and unverified inspection-note export. See the [reading and review guide](research/workbench-guide.md). This engineering milestone grants no independent epigraphic acceptance.

### Research workbench 1.1

Download the [research workbench 1.1 package](https://github.com/hawkinsnick/Cretan-hieroglpyhs/releases/tag/research-workbench-v1.1.0), extract it, and open `workbench/evidence.html`. It adds snapshot-bound inspection collections and includes the immutable release correction tracker. The Disc explorer also presents readable scenario comparisons. This engineering release grants no scientific acceptance.
