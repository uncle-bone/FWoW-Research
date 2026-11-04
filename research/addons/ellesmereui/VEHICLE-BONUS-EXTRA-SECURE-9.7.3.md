# EllesmereUI 9.7.3 — vehicle, bonus and extra-action secure ownership

**Baseline:** uploaded 9.7.3 ZIP only. **Date:** 2026-11-03. **Method:** inspect actual Lua call sites in `EllesmereUIActionBars`. All findings source-confirmed unless labeled unknown/inferred. No client tests.

## 1. Vehicle / override / possess controller

**Source:** `EUI_ActionBars_Controllers.lua:275-350`. A persistent local `OverrideController` frame is created with `SecureHandlerAttributeTemplate` at 281-284. Its dynamically installed `_onattributechanged` snippet at 286-307 propagates `overrideui`, `petbattleui` and `overridepage` into registered bar frames, while other changes re-evaluate vehicle, override and temporary shapeshift page APIs. The controller registers **eight** attribute drivers at 314-325: `form`, `overridebar`, `overrideui`, `possessbar`, `sstemp`, `vehicle`, `vehicleui`, `petbattleui`. These are **attribute** drivers, not the separate `RegisterStateDriver` calls counted in the package event audit.

**Dynamic alias / owner:** `RegisterBarWithOverrideController` at 330-344 is exported as `I.RegisterBarWithOverrideController` at 349 and imported by `EUI_ActionBars_Bars.lua:20`, which invokes it for each constructed bar at `:156`. It sets a frame ref and uses secure `Execute` to deduplicate frame entries before appending. The source explicitly notes the secure frame list cannot be pruned (`:328-329`); therefore removal/replacement of registered bar frames is a **lifecycle constraint**. A full teardown path was not established. **Inferred risk:** repeatedly constructing distinct bar frames may leave stale entries in the secure list; this is not proven to happen.

## 2. Secure paging and bonus bars

**Source:** `EUI_ActionBars_Bars.lua:75-120,125-159,205-250`; `EUI_ActionBars_Paging.lua:89-145`. Main-bar `_onstate-page` updates its own actionpage, child buttons through `ChildUpdate`, and the Blizzard main bar frame ref; registration at `Bars.lua:93`. Configured other bars use `_onstate-page` and a `page` driver at `:111-120`. `Paging.lua:130` builds bonus-bar conditions mapping `bonusbar:1..4` to pages 7..10, and `:144` adds bonusbar 5 → page 11 under its conditional branch. The code does **not** demonstrate these branches occur on every client build.

**Reconfiguration / cleanup:** `Bars.lua:213-214` explicitly unregisters and re-registers the MainBar page driver; `:244-245` does the same for custom paging; `:249-250` unregisters and restores a fixed actionpage when custom paging is removed. A distinct `eabvis` state driver is registered on each bar at `:141-152`, with no unregister shown in these paths. **Important distinction:** page-driver cleanup does not clean `eabvis` or the controller's eight attribute drivers.

## 3. Vehicle exit button event owner

**Source:** `EUI_ActionBars_Vehicle.lua:32-70`. When `MainMenuBarVehicleLeaveButton` exists, the addon reparents it to UIParent, takes a shell frame (`ns.TakeShell()`), and registers `UNIT_ENTERED_VEHICLE`, `UNIT_EXITED_VEHICLE`, `PLAYER_ENTERING_WORLD`, `PLAYER_REGEN_ENABLED` at 37-40. Its anonymous `OnEvent` filters non-player unit events and, outside combat, compares current visibility to `CanExitVehicle()` before calling protected `SetShown` only on a transition. `PLAYER_REGEN_ENABLED` is the retry trigger after combat. **Cleanup:** no explicit unregister appears in this block; shell lifecycle/disable-time cleanup remains unverified. This is **not** the shared CombatQueue.

## 4. Extra action container hooks and reentrancy

**Source:** `EUI_ActionBars_ExtraBars.lua:166-259`. `RefreshExtraActionButton` refreshes the hotkey/cooldown and optionally calls `ns.RefreshBroadcaster` (166-185). `ExtraAbilityContainer.AddFrame` is hooked at 194-200, with a one-frame `C_Timer_After(0, RefreshExtraActionButton)`. `ApplySystemAnchor` hook (214-229) calls `RepositionExtraContainer` only when anchored away from the addon holder; `Show` hook (234-239) does likewise, then refreshes. `RepositionExtraContainer` guards `InCombatLockdown()` before reparenting (204-210). Each managed extra frame gets a `SetParent` hook (254-259) that calls `ReparentIntoHolder` when stolen. **Potential reentrancy:** a reparent triggers `SetParent` hooks; whether `ReparentIntoHolder` has an effective recursion guard in every branch needs separate full-function trace. The shown anchor check is one reentrancy guard; no proof of global safety. `hooksecurefunc` hooks have no normal unhook API; their lifetime and repeated installation must be assessed against initialization guards, not assumed to be cleaned on disable.

## Unresolved teardown / protected behavior

- Controller attribute drivers: no unregister demonstrated; persistent controller and secure list may be deliberate lifetime ownership.
- `page` driver: explicit reconfiguration cleanup **confirmed**; `eabvis` and `extravis` teardown not proven.
- Vehicle shell: handler event unregister not established.
- Extra-action `hooksecurefunc` sites: no removal API; need determine one-time installation guard and reentrant `SetParent` behavior.
- Blizzard protected transitions and taint: **not tested**. Source comments about avoiding taint are design intent, not independent verification.

**Next ordered queue:** migration field→runtime reader matrix; profile import/export/switch error recovery; protected frame call-site audit.