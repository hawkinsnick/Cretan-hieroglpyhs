#!/usr/bin/env python3
import hashlib,json,pathlib
R=pathlib.Path(__file__).resolve().parents[1]
P=["VERSION","CITATION.cff","corpus/chic-catalogue-spine.json","signs/chic-core-sign-registry.json","corpus/manifest.json","analysis/audit-4.0.1.json","analysis/release-gates-4.0.1.json","analysis/coverage-matrix-4.0.1.json","analysis/research-readiness-4.0.1.json","bibliography/sources.json","provenance/source-lineage.json","research/experiment-gates.json","research/cross-script-claims.json"]
o={"version":"4.0.1","hash_algorithm":"sha256","artifacts":{}}
for p in P:
 b=(R/p).read_bytes();o["artifacts"][p]={"sha256":hashlib.sha256(b).hexdigest(),"bytes":len(b)}
print(json.dumps(o,indent=2,sort_keys=True))
