# EllesmereUI framework execution trace — upstream main, distinct from 9.7.3 ZIP

**Inspected:** 2026-11-03. **Source:** official https://github.com/EllesmereGaming/EllesmereUI, default branch observed with `EllesmereUI.toc` version **9.7.4**. These findings refer to upstream main as fetched, **not automatically** to uploaded 9.7.3. Method: direct reading of the first 110 lines of three framework source files. Evidence: **source-confirmed**, no live game testing.

## 1. Lightweight addon framework

**Source:** [`EllesmereUI_Lite.lua`](https://github.com/EllesmereGaming/EllesmereUI/blob/main/EllesmereUI_Lite.lua), symbols `EUILite.NewAddon`, `EUILite.GetAddon`, `GetOrCreateEventFrame`, `EllesmereUI.SnapPanelScale`.

- `EllesmereUI.Lite` is initialized as a shared lightweight addon registry. `NewAddon(name)` returns an existing registered addon if present; otherwise creates an addon object, queues it for initialization, eagerly creates its event frame, and mixes in event registration methods. **Source-confirmed.**
- `GetOrCreateEventFrame` stores one frame per addon, keeps handlers keyed by event name, and dispatches an event directly to the handler with `addon` and `event` arguments. **Source-confirmed.**
- The source comments attribute eager frame creation to addon CPU attribution during event handling. That attribution explanation is an **upstream-authored claim**, not independently measured here.
- `EllesmereUI.IS_FOREVER` uses `EUI_CLIENT_FOREVER`, reportedly stamped by the client gate; `GCD_SPELL` is set to 29515 for Forever and 61304 otherwise. **Source-confirmed assignment; actual game behavior unknown.**
- `SnapPanelScale` validates a numeric input, rounds to 0.05 increments, and clamps between 0.75 and 2.00. Invalid input returns 1.00. **Source-confirmed.**

## 2. Early startup and UI scale

**Source:** [`EllesmereUI_Startup.lua`](https://github.com/EllesmereGaming/EllesmereUI/blob/main/EllesmereUI_Startup.lua), symbols `ApplyScaleSafe`, `SyncMultOnly`, `scaleFrame`.

- An event frame registers `ADDON_LOADED`, `PLAYER_LOGIN`, `PLAYER_ENTERING_WORLD`. It ignores `ADDON_LOADED` for other addons. **Source-confirmed.**
- At its own `ADDON_LOADED`, it initializes `EllesmereUIDB` if absent, reads physical screen height, and if `ppUIScale` is present applies saved scale. Two explicit legacy values (0.53 and 0.71) are converted to more precise constants. **Source-confirmed.**
- `ApplyScaleSafe` defers a scale change through `EllesmereUI.CombatQueue.Defer("StartupScale", ...)` if `InCombatLockdown()` is true; when drained it re-reads the current saved value. Outside combat it invokes `UIParent:SetScale` and refreshes pixel-perfect multiplier when available. **Source-confirmed.**
- At `PLAYER_LOGIN` the returning-user path reapplies saved scale and registers `UI_SCALE_CHANGED`. **Source-confirmed for inspected branch.**
- Source comments explicitly note an earlier ADDON_LOADED-based chat-window drift fix did **not** stop the drift in field testing. Treat this as **upstream-reported field observation**, not an observation reproduced in this research.

## 3. Migration runner

**Source:** [`EllesmereUI_Migration.lua`](https://github.com/EllesmereGaming/EllesmereUI/blob/main/EllesmereUI_Migration.lua), symbols `EllesmereUI.RegisterMigration`, `GetFlagTable`, `RunOne`, `RunMigration`.

- Registration requires a table with nonempty string ID, callable body, and one of `global`, `profile`, or `specProfile` scopes; duplicate IDs are rejected with errors. **Source-confirmed.**
- Each scope stores completion flags under `_migrations` on the relevant host table. A body runs via `pcall`; only successful runs stamp the completion flag. Errors are buffered in `EllesmereUI._migrationErrors` with ID, scope, error string, and time. **Source-confirmed.**
- The runner iterates global DB, all profile tables, or all spec-profile tables according to scope. **Source-confirmed in inspected portion.**
- **Inferred risk to test:** a migration body that partially mutates data and then errors is retried on next run, so the stated idempotency requirement matters. No data-loss claim is made without a test.

## Remaining gaps and evidence levels

| Item | Status |
|---|---|
| Framework constructor and event-dispatch shape | source-confirmed |
| Startup saved scale and combat defer branch | source-confirmed |
| Migration registration and error/retry semantics | source-confirmed |
| Verify these exact branches against uploaded 9.7.3 | **unknown**; version diff required |
| Full file control-flow beyond first 110 lines | **unknown** |
| Live frame attribution, combat taint, scale drift | **unknown** in this research |
| Performance and memory benchmarks | **unknown** |
| Automated mock tests | not performed |

No copyrighted upstream implementation is reproduced here. This is an independently written technical summary with source pointers.