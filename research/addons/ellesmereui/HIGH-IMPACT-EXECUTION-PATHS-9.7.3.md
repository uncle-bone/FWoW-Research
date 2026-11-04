# EllesmereUI 9.7.3 — four high-impact caller/dispatch/cleanup paths

**Baseline:** user-uploaded `EllesmereUI-9.7.3.zip`; **date:** 2026-11-03; **method:** read line-numbered Lua from archive and follow named callbacks, event registration and explicit cleanup. These are **source-confirmed** static paths. No live-client execution or taint measurement. Upstream 9.7.4 is not used.

## A. Action bar slot change → keybinding reroute → combat queue

**Source:** `EllesmereUIActionBars/EUI_ActionBars_Events.lua:1061-1087,1851,2611-2629`; `EllesmereUI/EllesmereUI_Ticker.lua:174-222`.

- Registration: the package's `dispatcher` registers `ACTIONBAR_SLOT_CHANGED` at 1062 and installs a direct anonymous `OnEvent` callback at 1851. **Ownership:** package-local dispatcher, not the EUILite mixin frame.
- Dispatch: the event handler coalesces slot changes via `_empowerReroutePending`, schedules `C_Timer_After(0,...)`, then checks `InCombatLockdown()`. Outside combat it calls `_EmpowerReroute()`; in combat it queues `ns.CombatQueue.Defer("UpdateKeybinds", _EmpowerReroute)`. **Alias:** `_EmpowerReroute` is a local function value captured by the timer and passed to the queue; it is not a method name looked up by EUILite.
- Deferred dispatch: the CombatQueue's own `PLAYER_REGEN_ENABLED` frame drains pending functions by key, using `xpcall`. Duplicate `UpdateKeybinds` keys replace callbacks without increasing queue length. **Cleanup:** queue unregisters `PLAYER_REGEN_ENABLED` before draining; timer is a one-shot. The action bar dispatcher has no unregister in this inspected event block; whether it is intentionally session-long needs package lifecycle confirmation.
- **Unknown:** every protected API called by `_EmpowerReroute`, and whether the package's dispatcher is disabled/unregistered on unload. No taint claim.

## B. Specialization change → combat deferral → profile switch

**Source:** `EllesmereUI/EllesmereUI_Profiles.lua:3952-4033,4061-4135,4235-4270`.

- Registration: `specFrame` registers `PLAYER_SPECIALIZATION_CHANGED`, `PLAYER_ENTERING_WORLD`, and `PLAYER_REGEN_ENABLED` at 4075-4077, with direct anonymous `OnEvent` callback at 4078.
- The specialization handler filters `PLAYER_SPECIALIZATION_CHANGED` to the player at 4135. During combat, it sets `pendingSpecSwitch` and optionally records `pendingOverrideOldSpec` (4247-4254), then returns without switching profiles.
- On `PLAYER_REGEN_ENABLED`, it clears the pending marker, calls `SpecOverrides_OnSpecChanged` if applicable, **re-resolves** target profile, calls `SwitchProfile(targetProfile)`, then `RefreshAllAddons()` (4082-4127). This is a separate local pending-state implementation, **not** the shared CombatQueue.
- `SwitchProfile` closes unlock/edit sessions, harvests outgoing overrides, saves fonts/layout, and repoints the active DB; it may request reload if synced modules require it (3952-4033).
- **Cleanup:** pending marker is cleared on regen; the three `specFrame` event registrations are not unregistered in the inspected handler. No proof of disable-time teardown. **Unknown:** complete rollback on partial profile failure, spec resolution when client APIs return unavailable values.

## C. Action bar visibility → protected-state guard and deferred flag

**Source:** `EllesmereUIActionBars/EUI_ActionBars_VisibilityDrivers.lua:263-269,420-445`.

- A state driver is registered on `_extraBarVisProxy` with state name `extravis` and a pet-battle conditional at line 263. This is a protected driver registration, **not** an ordinary `OnEvent` callback.
- `EAB:ApplyCombatVisibility()` checks combat lockdown and sets `ns._eabApplyDeferred=true` instead of applying during combat (268-269).
- `ns._ixBarSync(barKey,eligOnly)` is a dynamically assigned namespace function, not a local anonymous event handler. It checks bar eligibility; when combat-locked it sets the same deferred flag, otherwise styles eligible buttons (420-439). If eligibility changed, it invokes three texture passes (441-444).
- **Cleanup/dispatch gap:** the inspected file has no `UnregisterStateDriver` match and does not itself show the consumer that drains `ns._eabApplyDeferred`. This is a concrete unresolved cross-file alias/ownership edge. Do not infer the flag is always drained or that driver registration is unsafe.

## D. Profile selection → outgoing state harvest → DB repoint

**Source:** `EllesmereUI/EllesmereUI_Profiles.lua:3952-4033,4050-4058,4889-4891`.

- Public wrapper `EllesmereUI.SetProfile(profileKey)` calls `SwitchProfile(profileKey)` (4889-4891). The switch function closes unlock-mode session with discard semantics, closes spec-override edit sessions, harvests outgoing spec overrides, snapshots fonts and unlock layout, and repoints addon DBs to the selected profile.
- When synced modules are dirty, it flushes outgoing-profile targets, repoints and shows a reload prompt (3990-4025); otherwise it stamps unlock layout, sets `activeProfile` and repoints (4030-4033).
- `AutoSaveActiveProfile` is an intentionally empty compatibility stub (4050-4058); callers relying on it do not create a second snapshot. **Source-confirmed.**
- **Cleanup:** editor sessions are closed before switching; the underlying per-package event handlers are not automatically unregistered by DB repoint. **Unknown:** exact downstream readers of each of the 114 migration fields, and full import/error rollback.

## Explicit coverage / alias map

| Edge | Alias/owner | Cleanup | Confidence |
|---|---|---|---|
| `ACTIONBAR_SLOT_CHANGED` | local `dispatcher` → anonymous `OnEvent` → local `_EmpowerReroute` | timer one-shot; combat queue event unregisters after drain; package dispatcher teardown unknown | source-confirmed except teardown |
| `PLAYER_SPECIALIZATION_CHANGED` | local `specFrame` → anonymous `OnEvent` → `SwitchProfile` | pending marker cleared on regen; frame remains registered in inspected code | source-confirmed |
| Extra-bar visibility | `_extraBarVisProxy` → state driver; `EAB:ApplyCombatVisibility`; `ns._ixBarSync` | state-driver unregister not located in inspected module; deferred-flag drain unresolved | source-confirmed registration, cleanup unknown |
| `SetProfile` | public wrapper → `SwitchProfile` → `RepointAllDBs` | outgoing edit/unlock sessions closed | source-confirmed |

## Migration downstream-consumer coverage

The previously indexed 114 migration registrations (42 global, 59 profile, 13 specProfile) are **not yet** individually mapped to downstream consumers. This report establishes two concrete downstream entrypoints: `SwitchProfile` repoints DB consumers, and the spec event handler invokes `RefreshAllAddons` after a profile switch. This does **not** prove each migration's transformed field reaches a particular reader. Required next step: for every migration write-path, find exact subsequent read sites and distinguish migration-only reads from runtime consumers. Treat dynamically computed field names as unresolved until inspected.

## Next module group

**ActionBars package lifecycle:** locate the construction and destruction of `dispatcher`, the consumer of `ns._eabApplyDeferred`, the caller of `ApplyCombatVisibility`, and secure state-driver unregister ownership. Then continue with `EllesmereUI_Profiles.lua` import/decode/merge failure paths. Do not infer live safety from guards alone.

**Status:** four high-impact paths traced to the stated static boundaries; package-wide callback closure, 114 migration downstream consumers and all module coverage remain open. No upstream code copied.
