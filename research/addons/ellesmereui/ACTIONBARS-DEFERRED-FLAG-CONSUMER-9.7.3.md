# EllesmereUI 9.7.3 — ActionBars deferred-apply consumer resolved

**Source:** uploaded 9.7.3 ZIP; **date:** 2026-11-03. **Method:** search all ActionBars Lua files for `_eabApplyDeferred` and `ApplyCombatVisibility`, then inspect the consuming event handler. **Evidence:** source-confirmed; no live testing.

## Complete producer → consumer edge

1. Producers include `EUI_ActionBars_VisibilityDrivers.lua:268-269` (`EAB:ApplyCombatVisibility`) and `:420-439` (`ns._ixBarSync`), `EUI_ActionBars_Apply.lua:89,1038`, `EUI_ActionBars_Layout.lua:274`, `EUI_ActionBars_Controllers.lua:258`, `EUI_ActionBars_Visibility.lua:148,161,294,340`, `EUI_ActionBars_Pushed.lua:272`, `EUI_ActionBars_Setup.lua:355`, and `EUI_ActionBars_ApplyAll.lua:103`. They set `ns._eabApplyDeferred` when work cannot safely run in combat. **Source-confirmed lexical references; each branch's runtime reachability is not proven.**
2. **Consumer resolved:** `EUI_ActionBars_Setup.lua:819-847` registers `PLAYER_REGEN_ENABLED` through `self:RegisterEvent(..., function() ... end)`, a function-valued EUILite callback, not a string alias. At 827-830 the handler checks and clears `ns._eabApplyDeferred`, clears `ns._eabMainBarAsbOwed`, and calls local `ApplyAll()`. The callback also handles alternate AlwaysShow repair, pet reconciliation, drag state, quick-keybind reassertion and empower attribute reassertion.
3. `EUI_ActionBars_ApplyAll.lua:95` calls `EAB:ApplyCombatVisibility()` when out of combat, while line 103 records deferred work when in combat. This closes the direct producer→event→reapply chain for the shared flag.
4. **Cleanup:** the pending boolean is cleared *before* `ApplyAll()`; the event remains registered by the addon object in the inspected code. The EUILite `UnregisterEvent` API exists but no explicit unregister for this particular registration was established. Event lifetime and addon disable behavior remain open.
5. `EUI_ActionBars_Bars.lua:213,244,249` explicitly calls `UnregisterStateDriver(frame,"page")` for **page** drivers. This does **not** prove cleanup of the separate `extravis` state driver registered on `_extraBarVisProxy` in `EUI_ActionBars_VisibilityDrivers.lua:263`; that remains unresolved.

## Alias and ownership resolution

| Callback | Owner | Dynamic alias | Cleanup |
|---|---|---|---|
| Combat-end deferred apply | EAB addon object, registered in `EUI_ActionBars_Setup.lua:819` | function closure passed to `self:RegisterEvent` | deferred flag cleared; event unregister unverified |
| `ns._ixBarSync` | ActionBars shared `ns`, assigned in VisibilityDrivers at 420 | direct namespace function value | called conditionally; teardown unverified |
| `ApplyAll` | local function captured by regen handler | lexical local function, not EUILite method lookup | invoked after flag cleared |
| Page driver | individual bar frame | secure state driver named `page` | explicit unregister sites in Bars.lua |
| Extra visibility driver | `_extraBarVisProxy` | secure state driver named `extravis` | unregister not found in inspected ActionBars files |

**Status:** shared deferred-flag consumer is now source-resolved. Full per-package cleanup and combat taint remain unverified. Independently authored summary, no upstream code reproduced.
