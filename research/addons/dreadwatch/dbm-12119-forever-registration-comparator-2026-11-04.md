# DBM-Core 12.1.19: exact-version Forever registration comparator

**Evidence:** user-supplied exact-version source inspection of `DBM-Core-12.1.19.zip`. **SC-U** = source finding supplied by the parallel DBM auditor; not independently re-traced here. **IN** = inference. This is a narrow cross-source comparator, not a re-audit of DBM `EncounterEvents.lua` handlers. The other workstream owns timer fallback/mapping, secret-safe warnings, and recovery.

## Confirmed registration distinction (SC-U)

- `private.isForever` is separate from `private.isRetail`.
- `DBM:IsRestricted()` treats **Retail OR Forever** as restricted.
- Registration of `ENCOUNTER_TIMELINE_EVENT_ADDED`, `ENCOUNTER_TIMELINE_EVENT_STATE_CHANGED`, `ENCOUNTER_TIMELINE_EVENT_COLOR_CHANGED`, and `ENCOUNTER_WARNING` is nested under `if private.isRetail`.
- Therefore, **handler functions existing in `EncounterEvents.lua` do not imply registration of those four events on Forever in DBM-Core 12.1.19**.

## Non-overlapping BigWigs/LittleWigs comparator

| Question | DBM-Core 12.1.19 (SC-U) | BigWigs 427.8 (SC from separate archive audit) | LittleWigs 12.1.22 (SC from archive manifest audit) |
|---|---|---|---|
| Distinct Forever flag | Yes: `private.isForever` | Yes: `loader.isForever` | No explicit 16001 manifest support |
| Modern/restricted client grouping | `DBM:IsRestricted()` covers Retail and Forever | `loader.isModern = isRetail or isForever` | Depends on BigWigs, but no proven Forever load path |
| Timeline/warning event registration | Four listed events are registered inside **Retail-only** conditional | Timeline plugin has its own dynamic registration of `ENCOUNTER_TIMELINE_EVENT_ADDED/STATE_CHANGED/REMOVED`; **Forever runtime registration not established** | Modern modules contain timeline references; **Forever load/registration not established** |
| What cannot be inferred | Handler presence ≠ Forever event registration | Modern flag ≠ guarantee of Forever event availability | File presence ≠ loadability or API support |

**IN:** A compatibility table must represent *definition*, *registration condition*, *payload safety*, and *observed runtime delivery* as separate fields. A single “supports timeline” checkbox would conceal important version- and client-specific differences.

**Boundary:** No DBM handler call graph, hardcoded timer mapping, secret-safe warning handling or recovery logic is repeated here. Await the separate auditor's findings before updating those rows.

**Reference scope only:** no Dreadwatch addon/prototype work; DreadwatchPTR remains retired.
