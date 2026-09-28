#!/usr/bin/env python3
import json,pathlib
R=pathlib.Path(__file__).resolve().parents[1]
L=lambda p:json.loads((R/p).read_text())
def F(m): print("FAIL:",m);raise SystemExit(1)
v=(R/"VERSION").read_text().strip();cat=L("corpus/chic-catalogue-spine.json");sg=L("signs/chic-core-sign-registry.json");src={x["id"] for x in L("bibliography/sources.json")}
if v!="4.0.1":F("version")
if len(cat)!=331 or [x["id"] for x in cat]!=[f"CHIC-{i:03d}" for i in range(1,332)]:F("catalogue")
c={k:sum(x["series"]==k for x in cat) for k in "HISY"}
if c!={"H":122,"I":57,"S":136,"Y":16}:F("series")
if len(sg)!=96 or len({x["id"] for x in sg})!=96:F("signs")
if any(x.get("phonetic_value") is not None for x in sg):F("phonetic leakage")
for x in cat+sg:
 if set(x.get("source_ids",[]))-src:F("orphan source")
if any(x.get("transitive") is not False for x in L("research/cross-script-claims.json")):F("transitivity")
for p in ["analysis/audit-4.0.1.json","analysis/release-gates-4.0.1.json","analysis/coverage-matrix-4.0.1.json","analysis/research-readiness-4.0.1.json","research/experiment-gates.json","corpus/manifest.json"]:
 if L(p).get("version")!=v:F("version drift "+p)
for g in L("analysis/release-gates-4.0.1.json")["gates"]:
 if not all(k in g for k in ["gate_id","severity","check","expected","status"]):F("gate contract")
if not isinstance(L("analysis/research-readiness-4.0.1.json").get("analyses"),list):F("readiness contract")
print(json.dumps({"version":v,"status":"PASS","catalogue":331,"series":c,"signs":96}))
