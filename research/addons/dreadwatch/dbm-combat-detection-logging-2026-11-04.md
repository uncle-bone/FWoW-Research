# DBM-Core 12.1.19 combat detection and combat-logging ownership

**Audit date:** 2026-11-04. **Evidence:** SC = source-confirmed; BD = build-derived; IN = inference; UN = unknown; OL = observed live (none). Source is the user-provided **DBM-Core-12.1.19.zip**, SHA-256 `b6ce514bd0e366b57880ab8b83a1266645c9d4c4210c38baeffb91aa50e3db54`. The inspected source paths and line numbers below refer to this exact archive, **not an assumed identical upstream main branch**. Public reference: [DBM Core](https://github.com/DeadlyBossMods/DeadlyBossMods/tree/master/DBM-Core). Independently authored summary; no copied upstream code.

## Manifest, responsibilities and event entrypoints

**SC:** `DBM-Core/modules/CombatDetection.lua` (1,881 lines) implements combat registration, encounter entry/exit, alternative pull detection, wipe handling, and logging. `DBM-Core/modules/Loading.lua` (619 lines) implements zone/difficulty refresh and whole-instance logging triggers. `DBM-Core/modules/UserTimers.lua` (383 lines) handles pre-pull logging and cancellation. `DBM-Core/modules/objects/Difficulties.lua` (667 lines) defines `DBM:IsLogableContent`; `modules/objects/CoreOptions.lua` defaults `AutologBosses=false`, `AdvancedAutologBosses=false`, `RecordOnlyBosses=false` (SC). Logging is **opt-in** in DBM, unlike Dreadwatch's requested default Automatic mode.

**SC:** `CombatDetection.lua:96–108` `module:RegisterCoreEvents()` registers safe `PLAYER_REGEN_DISABLED`, `ENCOUNTER_START`, `ENCOUNTER_END`, `BOSS_KILL`; `SCENARIO_COMPLETED` and `UNIT_HEALTH` for Retail; other health variants for Classic-family branches; `INSTANCE_ENCOUNTER_ENGAGE_UNIT` only when `not DBM:IsRestricted()`. Alternate pull detection also uses loading recovery, monster messages and health checks. These are **encounter detection**, not native log state-change events. **UN:** exact event registration in Forever build 70755 and event payload safety.

## End-to-end trigger graph

1. **World/zone entry:** `Loading.lua:543–559` `DBM:LOADING_SCREEN_DISABLED` unschedules and reschedules `SecondaryLoadCheck` at ~1s and 5s to tolerate incomplete instance information. `SecondaryLoadCheck` at 476–518 refreshes difficulty, compares map ID/difficulty against cached state, and early-returns if unchanged. If changed and `not RecordOnlyBosses`, it calls `StartLogging(0)` when last instance type is party/raid, otherwise `StopLogging()`. `CHALLENGE_MODE_RESET` at 608–614 can force `StartLogging` (SC). **IN risk:** a reload or transition where cached map/difficulty causes early return could bypass a desired re-check; requires runtime test.
2. **Encounter start:** `CombatDetection.lua:329–358` `ENCOUNTER_START` matches registered encounter IDs in the current area and calls `StartCombat`. `StartCombat` at 817–~1070 guards disabled modules, vehicle/timewalking constraints, repeated kills/wipes and active-module membership. It registers in-combat events, inserts module into `inCombat`, invokes `OnCombatStart` or restricted-client `OnLimitedCombatStart`. At line 950–952 it calls `StartLogging(0)` **only if** `RecordOnlyBosses` is true (SC). Non-encounter fallback triggers include regen, monster message, health, and loading-screen recovery.
3. **Pre-pull:** `UserTimers.lua:24–34, 94–108` calls `StartLogging(timer, checkForActualPull)` for a pull countdown when boss-only mode is selected. `StartLogging` schedules the check for `timer+10` if it owns native/Transcriptor logging. If no boss is active after the countdown (and difficulty is not 8), the check calls `StopLogging`. This captures pre-pots without indefinite logging after an abandoned pull (SC).
4. **Encounter end:** `CombatDetection.lua:390–451` `ENCOUNTER_END` and `BOSS_KILL` identify active modules, call `EndCombat`, and deduplicate certain end synchronization. `EndCombat` at 1198 onward removes the module from `inCombat`, unregisters in-combat handlers, stops timers and restores state. At 1470–1474, **only when `#inCombat == 0` and `RecordOnlyBosses`**, it schedules `StopLogging` after 10 seconds to include trailing kill/death log events (SC). Overlapping encounters do not stop logging when the first module ends.
5. **Leaving eligible zone:** `Loading.lua:510–516` calls `StopLogging` for non-party/raid when whole-zone mode is selected. This path relies on a completed `SecondaryLoadCheck`; no standalone native log-state watchdog was found in the reviewed logging call sites (SC).

## Logging state and ownership (exact source behavior)

**SC:** `CombatDetection.lua:618–659` has two **file-local booleans**, `autoLog=false` and `autoTLog=false`. `DBM:StartLogging(timer,checkFunc,force)` first cancels a scheduled stop, checks `IsLogableContent(force)`, then when `AutologBosses` and `not LoggingCombat()`, sets `autoLog=true`, prints a start message, and calls `LoggingCombat(true)`. An independent Transcriptor branch sets `autoTLog` when `AdvancedAutologBosses` and the plugin is available and not already recording. `StopLogging` checks options, `LoggingCombat()` and `autoLog` before setting the flag false and calling `LoggingCombat(false)`; Transcriptor has a parallel conditional stop. There is **no return-value verification, pcall or retry around LoggingCombat(true/false)** in these functions. If the logging API errors or refuses the change, the local ownership flag can become inconsistent (IN). A stop with `AutologBosses=false` or `LoggingCombat()==false` leaves `autoLog` uncleared (SC); this is a possible stale-flag edge case requiring tests (IN).

**SC:** `Difficulties.lua:611–667` `IsLogableContent(force)` checks LFG exclusion, M+ / timewalking / current vs trivial raid and dungeon filters, delve/challenge options, and selected difficulty. `force` only overrides a specific M+ condition, not all content filters. **SC:** `Loading.lua` may invoke StartLogging on party/raid entry but the content filter can still decline it.

**SC:** Neither `autoLog` nor `autoTLog` is in SavedVariables; they reset on Lua reload. No source path here establishes that a pre-existing native log session was started by DBM after reload. **IN:** if DBM had started logging before reload, the game may continue logging while the new Lua instance no longer owns it; native logging persistence itself is **UN** without live testing. If a user or other addon takes over an active session after DBM started it, a boolean alone cannot detect that change; DBM may later stop logging it considers owned (IN).

## Error handling, performance and restrictions

- **SC:** `StartLogging` and `StopLogging` do not wrap native LoggingCombat in `pcall` or check its post-call state. Transcriptor is an optional global dependency. `LOADING_SCREEN_DISABLED` deliberately defers zone checks; `StartCombat` avoids duplicate/false starts via kill/wipe cooldowns.
- **SC:** `StartCombat` branches between normal `OnCombatStart` and restricted `OnLimitedCombatStart`; `RegisterCoreEvents` excludes `INSTANCE_ENCOUNTER_ENGAGE_UNIT` on restricted clients. Do not transplant Classic health/GUID detection to Forever.
- **SC:** The whole-instance path records trash as well as bosses; boss-only mode uses countdown and delayed stop. The 1s/5s zone checks and 10s end delay are bounded scheduling patterns, not evidence of successful Forever logging.
- **UN:** no gameplay log, actual native API return/exception trace, or verified Warcraft Forever logging state transitions were provided.

## Dreadwatch cross-check — pinned prototype

**Source:** user-provided `Dreadwatch-v0.1.1-bigtest.zip`, SHA-256 `aa23d52fbf7a14af0165aa7602c8ce2c9aca9f4e5b25ceb935fcba7d32ac7eed`; `Dreadwatch/Dreadwatch.toc` interface 16001, version 0.1.1-bigtest; `Core.lua`, `Modules.lua`, `Diagnostics.lua`, `TestHarness.lua`, `UI.lua`. **SC:** `Core.lua` only registers `ADDON_LOADED` and `PLAYER_ENTERING_WORLD`; it maintains a synthetic-capable `StartEncounter`/`EndEncounter` lifecycle, basic options and event callbacks. On entering world it ends any nonsynthetic encounter. `Modules.lua` contains static encounter identities rather than live boss scripts. `Diagnostics.lua` explicitly reports no combat-log listeners. **No calls to `LoggingCombat`, native log-state owner flag, zone logging controller, retries, or logging settings were found in this pinned prototype (SC).** This archive may differ from current GitHub HEAD (**UN**, separate verification required). Do not claim that Dreadwatch currently has a working logger.

## Original Dreadwatch design requirements derived from audit (IN recommendations)

1. Default `Automatic` should target **full eligible dungeon/raid session**, beginning before first pull, including trash, boss and wipes. Keep it separate from Dreadwatch's encounter UI lifecycle; boss-only logging is optional future mode.
2. Use an explicit state machine: `inactive`, `pending-entry`, `active-owned`, `active-external`, `pending-exit`, `error`. Record current zone signature and session ownership in runtime state; avoid assuming ownership after reload.
3. Probe `LoggingCombat` safely; call enable only if currently off; verify state after call, retry with a **bounded** interval/window (e.g. up to 30 seconds) for zone-entry API delays. On exit, disable only if ownership is still defensible. Do not stop a log session that was already on at entry.
4. Debounce loading screens and verify `GetInstanceInfo` on delayed callbacks; use a generation token so stale retries/exits cannot toggle logging after a subsequent zone transition. Re-check after reload and unexpected map/difficulty transitions.
5. A local boolean cannot prove exclusive ownership if another addon changes native state. Prefer conservative leave-enabled behavior when ownership becomes ambiguous, and expose a diagnostic explanation.
6. Keep UI warnings/encounter timers, native combat-log recording, and addon-readable combat event collection as three independent systems. Secret combat values must never be coerced, logged or serialized without verified support.
7. Add isolated tests for manual-on before entry, own start, failed start, delayed success, reload while on, manual toggle mid-session, overlapping encounters, dungeon-to-raid transfer, exit during retry, missing APIs, and error recovery.

## Completion matrix for this subsystem

| Component | Status |
|---|---|
| CombatDetection registration / entry / exit / alternate triggers | **Source traced** at principal call sites; 1,881-line file not line-by-line certified |
| StartLogging/StopLogging ownership and options | **Source traced** |
| Loading/zone/reload scheduling | **Source traced** |
| Pre-pull timer and abandoned pull | **Source traced** |
| IsLogableContent filters | **Source traced** |
| Dreadwatch v0.1.1-bigtest logger absence | **Source confirmed** |
| Dreadwatch current HEAD comparison | **Unreviewed** |
| Live Warcraft Forever behavior | **Unverified** |
