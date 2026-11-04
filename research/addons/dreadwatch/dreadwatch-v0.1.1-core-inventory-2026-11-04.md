# Dreadwatch 0.1.1-bigtest: complete packaged core/module inventory

**Inspected:** 2026-11-04. **Source:** supplied `Dreadwatch-v0.1.1-bigtest.zip`, SHA-256 `aa23d52fbf7a14af0165aa7602c8ce2c9aca9f4e5b25ceb935fcba7d32ac7eed`. **SC** source-confirmed; **IN** inferred; **UN** unknown; **OL** no live validation. This is a **complete five-Lua-file packaged prototype inventory**, not a complete inventory of the current GitHub repository.

## Load order and dependencies

`Dreadwatch/Dreadwatch.toc` declares interface 16001, SavedVariables `DreadwatchDB`, and loads **Core.lua → Modules.lua → Diagnostics.lua → TestHarness.lua → UI.lua**. No required addon dependencies. All files use the shared addon namespace `ns.DW`. Synthetic test functionality is intentionally present; there is no live boss script or encounter-event registration (SC).

## Function, event and data-flow inventory

| File | Functions and handlers | Data flow / effects | Evidence |
|---|---|---|---|
| `Core.lua` (104 lines) | `safe`, `log`, `DW:On`, `DW:Emit`, `DW:StartEncounter`, `DW:EndEncounter`, `DW:Schedule`, `DW:Warn`, `DW:Probe`; frame `OnEvent`; `SlashCmdList.DREADWATCH` | Maintains one active `encounter`, `timers`, callbacks, capabilities, module catalog, history, phase and testing flag. `Emit` uses `pcall` per callback. Only `ADDON_LOADED` and `PLAYER_ENTERING_WORLD` registered. Initializes `DreadwatchDB.enabled/sound/scale`. Slash `/dw` supports help/test/bigtest/next/diagnose/modules/stop/status/on/off/sound/move. | SC |
| `Modules.lua` (30 lines) | `DW:RegisterModule`, `DW:ListModules` | Static encounter ID/name/zone catalog (Hall of Thanes, Ragefire Chasm, Stockade); not encounter scripts or verified boss timers. | SC |
| `Diagnostics.lua` (20 lines) | `safeString`, `DW:Diagnose` | Prints build/API presence and explicitly says no combat-log listeners/comms/protected-data probing. | SC |
| `TestHarness.lua` (30 lines) | `DW:RunBigTest`, `DW:LoadTestPhase`, `DW:NextTestPhase` | Three synthetic phases with fixed warning labels and countdowns; no real event injection or network. | SC |
| `UI.lua` (91 lines) | drag-start/stop, `update`, 0.1s `OnUpdate`, callbacks for start/end/warning/move, login initialization | Six visible timer bars; sorts all active timers by remaining time, hides expired timers, persists drag coordinates, reads UI scale. | SC |

## Call graph

`ADDON_LOADED` → initialize DB defaults → `Probe`; `PLAYER_LOGIN` → restore UI position/scale → `update`. `/dw bigtest` → `RunBigTest` → `StartEncounter` → `Emit(start)` → UI `update`; then `LoadTestPhase` → `Warn` → `Emit(warning)` and repeated `Schedule` → `Emit(timer)`. `UI.OnUpdate` polls every 0.1s and removes expired timers. `/dw next` loads the next synthetic phase; `/dw stop` → `EndEncounter` → `Emit(end)` → hide UI. `PLAYER_ENTERING_WORLD` ends a nonsynthetic encounter if one existed. **There is no `ENCOUNTER_START`/END event registration, `LoggingCombat`, SmartSync transport, or native timeline adapter in this package** (SC).

## Error, performance and restricted-client findings

- **SC:** callback errors are isolated with `pcall`; some UI API calls are not protected, including `SetShown`, `GetTime`, and timer-bar updates.
- **SC:** `safe` and `safeString` check `issecretvalue` before formatting some inputs; `DW:Warn` validates string length. This does not certify handling of all secret-value payloads.
- **SC:** UI refresh sorts the active timer list every 0.1s and shows only six bars; timer count has no explicit cap in `Schedule`. This is acceptable for a synthetic prototype but should be bounded/optimized for live encounters (IN).
- **SC:** `DW:StartEncounter` replaces an existing encounter and `DW:EndEncounter` clears all timers. There is no multi-encounter state or explicit event ID/timer ownership guard.
- **SC:** `DreadwatchDB` stores enabled/sound/scale and window position; there is no schema version/migration, logger ownership, or saved encounter evidence.
- **UN:** actual current GitHub HEAD contents and real Forever runtime compatibility. Do not mistake this pinned prototype for an installed release.

## Actionable next steps

1. Compare this pinned ZIP against current Dreadwatch GitHub HEAD, documenting added/removed functions.
2. Build original native event adapter and safe encounter lifecycle with explicit encounter-ID/timer ownership, no copying of DBM/BigWigs source.
3. Implement Automatic native logging as a separate zone-scoped service, with ownership and reload/transition tests; see [DBM combat-logging audit](dbm-combat-detection-logging-2026-11-04.md).
4. Add secret-safe native warning/timeline adapter, scheduler and bounded UI refresh.
5. Add synthetic regression tests for timer replacement, callback failures, world transitions, multiple encounters, missing APIs and all logging states.
