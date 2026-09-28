# Evidence ingestion workflow — v2

1. **Catalogue**: create/confirm canonical identity only.
2. **Metadata check**: verify archaeological/object metadata against cited source locations.
3. **Transcription check**: encode a source reading without silently normalizing it.
4. **Occurrence check**: segment/order sign occurrences, preserving damage and uncertainty.
5. **Independent review**: a distinct review event evaluates the encoded evidence.

Each transition produces a verification event. Disagreement creates parallel attributable positions rather than destructive replacement. Derived fields state their transformation and upstream evidence.

A record's highest stage is not a confidence score. It reports completed workflow, while individual assertions retain their own uncertainty.
