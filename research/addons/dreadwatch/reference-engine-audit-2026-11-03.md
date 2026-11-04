# Dreadwatch reference-engine reverse engineering — checkpoint

Date: 2026-11-03. Evidence labels: **SC** source-confirmed; **BD** client/build-derived; **OL** observed live; **IN** inferred; **UN** unknown. **No new live tests in this report.** This is not an exhaustive function-level certification.

## Existing research checked

- [Earlier Dreadwatch source audit](../../encounter-source-audits/2026-11-03-dreadwatch-forever-source-audit.md), including Dreadwatch prior commit `dff13365b188f73471e42eb2a5e87c9c4e222422`, build 70755 and DBM-Dungeons upstream `f143f5d8`.
- [70707 encounter ID cross-reference](../../local-client-scans/2026-11-03/ENCOUNTER-AUDIT.md). Preserve conflicting aliases, especially 3301, 3495, 3355 and 2742.
- [Addon research evidence standards](../README.md).

## Per-addon coverage matrix

| Reference and exact version | Manifest / dependencies | Architecture, API and execution path | SavedVariables | Error, security, performance | Outstanding |
|---|---|---|---|---|---|
| Dreadwatch repo, previously audited `dff1336` | Partial (SC prior report) | PTR diagnostics; no production boss-mod engine at prior commit (SC) | UN | UN | Fresh full HEAD inventory, every module/function, actual runtime |
| DBM-Core **12.1.19** supplied ZIP | `DBM-Core/DBM-Core.toc`: interface 16001; DBM-StatusBarTimers dependency (SC) | `DBM-Core.lua`, `modules/EncounterEvents.lua`, `modules/CombatDetection.lua` (SC) | `DBM_AllSavedOptions`, `DBM_MinimapIcon`, `DBM_AnnoyingPopupDisables`, `DBM_Keystones` declared (SC) | Structured secret warning fields; combat logging ownership (SC); actual Forever success UN | Full call graphs, comms, timers, failures |
| BigWigs **427.8** supplied ZIP | `BigWigs.toc`: interface 16001; optional libraries (SC) | `Core/Core.lua` eventMap dispatcher, `Core/BossPrototype.lua` Forever branch, `BigWigs_Plugins/Timeline.lua` (SC) | `BigWigs3DB`, `BigWigsIconDB`, `BigWigsStatsDB` declared (SC) | `issecretvalue` guard on mouseover GUID (SC) | All plugins, communication, migrations, performance |
| LittleWigs **12.1.22** supplied ZIP | `LittleWigs.toc`: requires BigWigs, interface 16001 not listed (SC) | `TBC/TheMechanar/Pathaleon.lua` illustrates start/end/wipe/win and legacy spell handlers (SC) | Shared BigWigs framework likely (IN), details UN | Legacy health/GUID paths not Forever-verified (UN) | Per-dungeon handler inventory, load filters |
| DBM-Dungeons Forever release **270**, upstream `f143f5d8` | `DBM-Party-Forever.toc`: load on demand, DBM-Core dependency, four zones (SC) | 24 encounter registration modules, no boss-specific warning/timer handlers in prior complete module scan (SC) | `DBMPartyForever_AllSavedVars`, `DBMPartyForever_SavedStats` (SC) | Generic-trash live behavior UN | Actual mechanics and timing observations |
| DBM-CoA **v6.0.0** | Classic 3.3.5a lineage (SC documentation) | SmartSync v3 actual source traced: all packet paths, index, gating, simulator (SC; see [full trace](dbm-coa-smartsync3-source-trace-2026-11-03.md)) | README requires preservation (SC documentation) | Forever transport compatibility UN | Learner complete lifecycle, runtime tests, Forever transport validation |

## Traced source behavior

1. **BigWigs dispatcher (SC):** `Core/Core.lua` `core:RegisterEvent` adds module callbacks to `eventMap[event]`; one frame dispatches registered handlers. `mod:ENCOUNTER_START` selects the matching encounter ID, enables and engages its module. Disable/wipe cleanup unregisters handlers. [Source](https://github.com/BigWigsMods/BigWigs/blob/master/Core/Core.lua).
2. **BigWigs restricted-data guard (SC):** `Core/Core.lua` checks `issecretvalue(UnitGUID("mouseover"))` before extracting a creature ID. This does not certify all Forever payloads as accessible. [Source](https://github.com/BigWigsMods/BigWigs/blob/master/Core/Core.lua).
3. **DBM warning adapter (SC):** `DBM-Core/modules/EncounterEvents.lua`, `DBM:ENCOUNTER_WARNING` processes structured warnings with severity and documented secret fields. Any Dreadwatch adapter must avoid unsafe secret-value inspection. [Source](https://github.com/DeadlyBossMods/DeadlyBossMods/blob/master/DBM-Core/modules/EncounterEvents.lua).
4. **DBM Forever encounter registration (SC):** `DBM-Party-Forever/HallofThanes/FaldrimAnvilmar.lua` registers encounter 3493, zone 3065, combat and generic trash; creature-ID declaration is commented out. [Source](https://github.com/DeadlyBossMods/DBM-Dungeons/blob/master/DBM-Party-Forever/HallofThanes/FaldrimAnvilmar.lua).
5. **LittleWigs lifecycle (SC, not Forever):** `TBC/TheMechanar/Pathaleon.lua` registers encounter start/end and maps completion status to wipe/win, alongside combat-log spell handlers. This historical example is not evidence of Forever viability. [Source](https://github.com/BigWigsMods/LittleWigs/blob/master/TBC/TheMechanar/Pathaleon.lua).
6. **Combat logging (SC, prior supplied archive inspection):** DBM `modules/CombatDetection.lua` checks `LoggingCombat()` and tracks whether it started logging. Dreadwatch's requested automatic logger needs original code for ownership, bounded retry, verified start/stop and reload recovery. No Dreadwatch implementation claimed.

## Actionable gaps

- Fresh Dreadwatch repository tree and all-file/function/event inventory; reconcile any prototype archive with actual GitHub revision.
- DBM complete combat detection, warnings, timeline, scheduling, synchronization and error-handling call graphs at pinned version.
- BigWigs loader, BossPrototype, plugins, timeline, transport, profile migrations and event performance at pinned version.
- LittleWigs all-instance/module index, load filters, event handlers and Retail-versus-Forever separation.
- DBM-CoA SmartSync v3 source trace is now [completed at the primary protocol-file level](dbm-coa-smartsync3-source-trace-2026-11-03.md); full Learner lifecycle and dynamic tests remain.
- Client build 70755 live encounter-warning/timeline payload tests and verified automatic combat-log start/stop; never infer observed-live from static source.
- Record archive SHA-256 and upstream commit for every inspected artifact in a subsequent reproducibility pass.

## License and method

Method: inspected prior repository reports, connected GitHub source files and manifests, and findings from supplied versioned addon archives. No bulk code or assets copied. BigWigs/LittleWigs TOCs state All Rights Reserved with limited GitHub fork/modification permission. Treat all source as research evidence, not permission to transplant implementations. GitHub default-branch links may change; pinned SHA/source snapshots remain outstanding.

## 2026-11-04 coverage update

- **DBM-Core combat detection/logging:** source-traced from fixed 12.1.19 archive, including `CombatDetection.lua`, `Loading.lua`, `UserTimers.lua`, `Difficulties.lua` and options; see [pinned archive report](dbm-combat-detection-logging-2026-11-04.md). Live behavior UN.
- **Dreadwatch 0.1.1-bigtest packaged core:** all five Lua files, their functions and event/data flows inventoried; see [prototype inventory](dreadwatch-v0.1.1-core-inventory-2026-11-04.md). Current GitHub HEAD remains UN.
