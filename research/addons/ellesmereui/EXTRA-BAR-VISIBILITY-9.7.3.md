# EllesmereUI 9.7.3 — extra-bar secure visibility callback ownership

**Baseline:** uploaded `EllesmereUI-9.7.3.zip`. **Method:** direct inspection of `EllesmereUIActionBars/EUI_ActionBars_VisibilityDrivers.lua:207-264`, `EUI_ActionBars_Setup.lua:819-847` and `EUI_ActionBars_Bars.lua:135-156,225-250`; cross-file searches for state driver identifiers. **Date:** 2026-11-03. All facts below **source-confirmed** except where marked unknown/inferred; not observed-live.

## Secure-to-insecure dispatch path

- `EAB:ApplyExtraBarVisibility()` in `EUI_ActionBars_VisibilityDrivers.lua:215` lazily creates a single `_extraBarVisProxy` frame (line 217), using `SecureHandlerStateTemplate`. This local proxy persists in the module's closure. **Source-confirmed.**
- The proxy installs `_onstate-extravis` at 218-220, which calls the frame method `OnExtraVisChanged` with `newstate`. The method is dynamically assigned at line 221 as a Lua function on the frame, not registered through EUILite. **Source-confirmed dynamic callback alias resolved.**
- `OnExtraVisChanged` iterates `EXTRA_BARS`; skips entries with `noManagedVisibility`, reads `EAB.db.profile.bars[key]`, skips `IsNever`, resolves managed, Blizzard-movable or named frames, and hides/shows or updates managed suppression depending on pet-battle state (221-260). **Source-confirmed.**
- Each invocation of `ApplyExtraBarVisibility` calls `RegisterStateDriver(_extraBarVisProxy,"extravis","[petbattle] hide; show")` at 263, even if the proxy already exists. **Source-confirmed.** Whether repeated registration is harmless under the matching client is **unknown**.

## Registration and cleanup distinctions

- No `UnregisterStateDriver` for `_extraBarVisProxy` or `"extravis"` was found in the inspected ActionBars Lua sources. This is an **absence in inspected source**, not proof that the engine never releases the driver at addon unload.
- `EUI_ActionBars_Bars.lua:244-249` explicitly unregisters the **different** `"page"` driver when paging conditions change. `:152` registers an **`"eabvis"`** driver on individual bar frames. Neither constitutes cleanup of the `"extravis"` proxy driver. **Source-confirmed.**
- Combat-deferral is separate: `EAB:ApplyCombatVisibility` at `VisibilityDrivers.lua:268-269` sets `ns._eabApplyDeferred` if combat-locked. `EUI_ActionBars_Setup.lua:819-830` drains that flag on `PLAYER_REGEN_ENABLED` by clearing it then invoking `ApplyAll()`. This is not the state driver's dispatch mechanism. **Source-confirmed.**

## Open safety questions

1. Does `OnExtraVisChanged` ever invoke protected operations from a secure handler in a way that taints or fails on the matching Forever client? **Unknown without client test.**
2. Can a profile switch leave old visibility state on frames excluded by `IsNever`? **Inferred possibility; not demonstrated.**
3. Is the extra visibility proxy intentionally lifetime-long? **Inferred from single lazy allocation; no explicit teardown established.**
4. Is repeated `RegisterStateDriver` on the same proxy safe/idempotent? **Unknown; requires client test.**

**Status:** secure proxy ownership, dynamic method alias, state driver registration, and dispatch to frame visibility are source-traced; explicit teardown remains unresolved. No upstream source or assets copied.
