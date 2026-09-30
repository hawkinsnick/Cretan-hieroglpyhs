# Current-state integrity milestone

Repository version: 5.2.3.

331 catalogue identities, 96 sign registry entries, zero critical readings and zero source-checked occurrence objects. DBAS metadata/rights boundaries are documented; structural and comparative experiments remain blocked.

The current-state validator parses every committed JSON file, checks schema validity, citation/family metadata, evidence digests, interchange positive/negative fixtures, native committed counts where available, and blocked-claim boundaries. Regression tests deliberately corrupt metadata and restore it. CI runs these checks on pushes and pull requests.

Artifact content versions are independent of the repository release. Unchanged inscription records, historical baselines, protocols and audits retain their content versions. Mutable current metadata (VERSION, citation, current status, family member version, current index/API examples/manifest) follows the repository version. A software validation pass does not certify epigraphic correctness or open a scientific gate.
