# Artifact versioning

Release version, artifact content version and schema version are distinct. Files such as `analysis/scholarly-risk-register.json` and `research/repertoire-layers.json` intentionally retain 3.0.0 internal content versions because their substantive content did not change. This is not release drift. Release-critical artifacts named by the current manifest must match `VERSION`.
