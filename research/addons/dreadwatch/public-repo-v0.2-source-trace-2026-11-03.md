# DreadwatchPTR v0.2.0 — current public source trace

**Reviewed:** 2026-11-03  
**Evidence:** SC = source-confirmed from the pinned repository commit below. No live-client behavior was exercised in this report.  
**Source baseline:** [uncle-bone/Dreadwatch commit dff13365b188f73471e42eb2a5e87c9c4e222422](https://github.com/uncle-bone/Dreadwatch/commit/dff13365b188f73471e42eb2a5e87c9c4e222422), authored 2026-11-03.  
**Files in the released folder:** [DreadwatchPTR.toc](https://github.com/uncle-bone/Dreadwatch/blob/dff13365b188f73471e42eb2a5e87c9c4e222422/DreadwatchPTR/DreadwatchPTR.toc) (blob `c8b434c8a969a925810b73b188fa15fdc244aa77`) and [Core.lua](https://github.com/uncle-bone/Dreadwatch/blob/dff13365b188f73471e42eb2a5e87c9c4e222422/DreadwatchPTR/Core.lua) (blob `50aa40ac8fe64d4be029805f72ec6af6316a854b`). The TOC declares interface 16001, version `0.2.0-ptr`, SavedVariable `DreadwatchPTRDB`, and loads only `Core.lua`.

## Scope and relationship to the larger project

**SC:** At this public revision, the installable `DreadwatchPTR` package is a conservative capability-diagnostics addon. It is not a dungeon encounter engine: its event list deliberately excludes encounter warning/timeline events, its commands report those capabilities as unverified, and its report states that no addon messages are sent. This conclusion applies to the pinned public package and does not erase other prototypes or archives that may exist elsewhere.

**SC:** The separate [PTR test plan](https://github.com/uncle-bone/Dreadwatch/blob/dff13365b188f73471e42eb2a5e87c9c4e222422/research/warcraft-forever/PTR-TEST-PLAN.md) says source implementation is not yet live-client tested, defers dungeon boss testing until access is available, and calls namespace presence insufficient evidence of encounter signals.

## Load and state lifecycle

1. **File scope / namespace (SC):** The TOC loads one Lua file. It captures the addon folder name from the chunk vararg, creates one frame, and keeps runtime state in locals: event counts, samples, and the SavedVariables reference.
2. **Event registration (SC):** The frame always registers `ADDON_LOADED`, `PLAYER_LOGIN`, then seven declared events: entering-world, zone-change, combat-start/end, and three unit-spellcast events. It does not conditionally register based on detected client build.
3. **Initialization (SC):** On the matching `ADDON_LOADED`, `initialize()` replaces malformed database/root fields with tables/numbers, sets schema to 1 if not numeric, increments `launchCount`, and prints a load notice. There is no migration chain for older or higher numeric schema values.
4. **Login status (SC):** On `PLAYER_LOGIN`, `status()` prints `GetBuildInfo()`, `WOW_PROJECT_ID`, the Lua types of selected `C_*` namespaces and secrecy helpers, and database fields. The namespace check answers “is this global nil/table/etc.?”; it does not check whether a specific function exists, can be called, or works in a particular situation.
5. **Runtime-only collection (SC):** `record(event,...)` increments a per-event count unconditionally. Spell/NPC sampling happens only after `/dwptr test combat` sets `sample.enabled=true`. Counts and sample sets are locals and are discarded on reload. No raw combat payload is retained.
6. **Reset (SC):** `/dwptr reset` replaces the runtime counts and sample tables; it does not clear SavedVariables. It effectively disables sampling again because the replacement sample has no `enabled` field.
7. **Persistent data (SC):** `DreadwatchPTRDB.marker` can be set with `/dwptr marker TEXT`; `launchCount` increments at addon load. A `records` table is initialized but not read or written elsewhere in this file. No sampled spell or NPC ID is persisted.

## Secret/access guard and sampled spellcast path

**SC:** `safe(v)` calls `issecretvalue(v)` and `canaccessvalue(v)` under `pcall` when those helpers exist. A thrown check or a positive secret/restricted result returns false. When a helper is absent, that helper is skipped. `readable(v)` increments `sample.restricted` on false and `sample.readable` on true; these are counts of guard outcomes, not counts of unique readable game values.

For the three `UNIT_SPELLCAST_*` events, `record` follows this sequence:

- Unpack `unit, castGUID, spellID`.
- After the access guard, accept unit values only when they are strings naming `target`, `focus`, `player`, or matching `boss%d+`.
- Call `UnitGUID(unit)` inside `pcall`; after the access guard, parse Creature or Vehicle GUID layouts and keep only the NPC-ID component in the in-memory set.
- After the access guard, keep numeric spell IDs in the range 1–9,999,999 in the in-memory set.
- Deliberately do not inspect or persist `castGUID`.

**SC:** The source comment and slash output both frame the feature as targeted opt-in diagnostics, with no raw event payload persistence. **UN:** This static path does not establish that these values arrive readable, that the event signatures match the target client in every case, or that the GUID layouts cover Forever's current forms.

## Slash command surface and user data

| Command | Source behavior (SC) | State effect |
|---|---|---|
| `help` / empty | Prints supported commands. | None. |
| `status` | Prints client/build/interface, project ID, namespace/helper types, and SavedVariables summary. | None. |
| `events` | Prints counts for the declared events and says encounter events are not registered. | Reads runtime counters. |
| `scan` | Prints namespace-type availability only; explicitly says it is not proof of callable APIs. | None. |
| `test combat` | Enables this-session sampling and clears spell/NPC sample sets and access counters. | Runtime only. |
| `report` | Lists sorted spell/NPC IDs (up to 12 shown), access-check counts, and unverified encounter/sync status. | Reads runtime samples. |
| `marker TEXT` | Stores non-empty text up to 80 bytes/characters as `db.marker`. | SavedVariables. |
| `reset` | Clears runtime counters and samples; SavedVariables remain. | Runtime only. |

The marker value is printed through `status()` using `tostring`. The command limits its length but does not filter WoW chat-format control characters. Since the marker is user-controlled and local, the practical risk appears limited, but output encoding/sanitization is a possible hardening point. **IN:** “launchCount” is a load counter, not necessarily a distinct application launch count, because it increments when the addon receives `ADDON_LOADED`.

## Function coverage and findings

| Function / block | Disposition |
|---|---|
| `say`, `safe`, `readable` | Traced. Chat output is guarded by presence of `DEFAULT_CHAT_FRAME`; helper checks are protected by `pcall` but missing helpers fail open. |
| `initialize` | Traced. Type-repairs selected root fields; schema is defaulted but not version-migrated. |
| `namespace`, `status` | Traced. Reports global namespace types and build metadata; does not capability-probe methods. `GetBuildInfo` and output formatting are not protected by `pcall`. |
| `record` | Traced. Always counts registered event names; opt-in branch samples guarded spell/NPC data only. `UnitGUID` call is protected. |
| `listSamples` | Traced. Sorts ID strings and prints at most 12 values per category. |
| Slash handler | Traced for each documented command and fallback. Marker length is bounded; user-supplied marker formatting characters are not filtered. |
| TOC loader | Traced: interface 16001, one SavedVariables root, one Lua file, no explicit dependency. |

## Compatibility, safety and performance boundaries

- **SC:** This revision registers only the seven explicit general/combat/spellcast events and does not register encounter events.
- **SC:** It transmits no addon messages and leaves encounter payloads, boss mechanics, and sync unverified.
- **SC:** Sampling is opt-in and volatile; spell/NPC sample sets contain IDs only.
- **SC:** The file has no periodic `OnUpdate` loop, timer, or database scan. Cost is limited to the registered event callbacks and explicit status/report commands.
- **IN:** If the target client omitted either secrecy helper, `safe` would permit inspection through that absent check. The current status output can reveal helper presence, but no runtime evidence here confirms the live target's helper behavior.
- **UN:** No evidence in this source establishes which encounter/timeline APIs are supported or safe to register, how warnings should be dispatched, or whether communication is permitted in any instance.
- **UN:** There are no test files in the install folder or source-level injected API fixtures in this pinned package; live taint, combat-lockdown, and actual Forever observations are not established by reading this code.

## Next useful work

1. Preserve this diagnostic package as a distinct research baseline; do not describe it as the older `Dreadwatch-v0.1.1-bigtest.zip` engine without comparing their source trees.
2. Inspect that supplied prototype/archive (if still in scope), hash it, inventory its files and APIs, and reconcile it with public commit `dff1336`.
3. If changing the diagnostics addon, consider fail-closed policy for absent secrecy helpers, stronger schema migration handling, clearer “check outcomes” labels, and sanitizing marker output. Treat these as review findings, not changes made here.
4. Perform the documented open-world and dungeon tests only on the authorized target client and record build, exact command sequence, results, and errors. Keep “namespace exists” separate from “callable API” and “observed encounter signal.”
5. Continue the production-engine function inventory separately from the PTR capability lab; the latter currently has one loaded source file and does not establish that the full design is implemented.

## Reproduction and license notes

This report summarizes source behavior and names functions without reproducing the implementation. Sources inspected were the pinned Dreadwatch TOC, Core.lua, and PTR test-plan entry above. No game client files or third-party addon code are included.
