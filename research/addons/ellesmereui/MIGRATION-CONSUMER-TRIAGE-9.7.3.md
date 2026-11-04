# EllesmereUI 9.7.3 — 114 migration downstream-consumer triage

**Baseline:** uploaded 9.7.3 ZIP only, 2026-11-03. **Method:** for each of 114 literal `RegisterMigration` entries, take the source range from its registration to the next registration, extract candidate literal state-field tokens, build an inverted token index over all other Lua files and record exact external file/line matches. **Evidence:** source-confirmed lexical matches, **not** semantic read/write or execution proofs. A generated 114-row Markdown table and machine-readable JSON are conversation artifacts `EllesmereUI_9.7.3_Migration_Consumer_Candidates.md` and `EllesmereUI_9.7.3_Migration_Consumer_Candidates.json`.

## Coverage and classification

**114/114 registrations were processed.** **98** have one or more other-file token matches, and **16** have no candidate matches under this extraction rule. These categories are **candidate external reader** and **dynamic/no literal match**; neither is a confirmed consumer/no-consumer classification. Shared tokens (e.g. module names) can create false positives; indirect table aliases, bracketed computed keys and helper calls can create false negatives. The registration-to-registration source slice is **not a parsed Lua body span** and can contain helpers or other registrations. Therefore a row is **not closed** until actual writes, downstream reads and same-state identity are manually checked.

## Confirmed consumer example and retry nuance

`EllesmereUI_Migration.lua:193-240` migration `clickcast_frame_spell_reaction_v1` transforms `hovercast` bindings; `EllesmereUIRaidFrames/EUI_RaidFrames_ClickCast.lua:354-357,485,508-515,956,1147,1814` reads or processes `hovercast`. The migration's `reactionSeeded` marker is migration-local bookkeeping. Because appending a split binding precedes marking the original, partial failure could leave a duplicate on retry; **inferred risk, not observed bug**. See [prior focused consumer trace](CLICKCAST-MIGRATION-CONSUMER-9.7.3.md).

## Next semantic verification

1. Parse the actual function body of each registration, including helper calls and nested anonymous functions, rather than treating the next registration as a reliable boundary.
2. Separate **write targets** from guards, reads, comments and string literals; record profile/global/spec store identity.
3. Match exact downstream runtime readers, then trace whether a reader consumes a migrated value, a fresh default or an independently copied field.
4. Classify **direct reader / indirect reader / dynamic reader / migration-only field / no consumer established**; do not infer no consumer from absent literal matches.
5. For each migration, test guard failures and partial mutation against temporary sandboxed SavedVariables; no user data should be modified.

**Status:** 114/114 lexical candidate triage completed; **0/114 additional semantic consumers proven by this automated step**. The previously manual-confirmed click-cast consumer remains established. No live certification.