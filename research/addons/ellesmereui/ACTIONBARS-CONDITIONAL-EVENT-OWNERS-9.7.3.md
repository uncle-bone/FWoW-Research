# EllesmereUI 9.7.3 — conditional event ownership and teardown

Baseline: uploaded 9.7.3 ZIP only. Date: 2026-11-03. Method: inspect register, dispatch and cleanup within ActionBars source. Source-confirmed static analysis; no runtime testing.

## Vehicle visibility watcher

In `EllesmereUIActionBars/EUI_ActionBars_Vehicle.lua:189-210`, `EAB:UpdateVehicleBarWatch()` checks `db.profile.hideBlizzardVehicleBar`. When disabled it unregisters **all** events on the cached `self._eabVehWatch` frame, if present, and reapplies visibility (193-199). On first enable it acquires a frame from `ns.TakeShell()`, installs an `OnEvent` closure that calls `CacheMicroMenuHome` then `ApplyVehicleBarVisibility`, and retains it on `self._eabVehWatch` (201-207). It registers `PLAYER_ENTERING_WORLD` at 209. This is a **confirmed conditional registration→dispatch→disable cleanup pair**; the frame itself is retained and reused rather than destroyed. Additional watcher events and hook behavior below line 210 require continued tracing.

## Neutral faction cap listener

In `EUI_ActionBars_Chrome.lua:430-466`, `ns.AB_CapsEvSync()` scans per-bar chrome state to determine whether faction-cap artwork needs updates. If no bar needs it, the cached `ns._abCapsEv` frame calls `UnregisterAllEvents` (443-445). Otherwise the first call acquires a shell, installs an `OnEvent` handler (448-458), and registers `NEUTRAL_FACTION_SELECT_RESULT` (460). `PLAYER_ENTERING_WORLD` is registered only while faction data is still pending; the handler unregisters that event when all cap states are known (449-456), and the sync function also unregisters it when no longer waiting (461-465). This is **conditional teardown with retained frame ownership**, not a permanent unmatched registration. The neutral-faction event stays active while any cap art needs it.

## Deferred spellbook/macro UI hook installer

In `EUI_ActionBars_Vehicle.lua:520-560`, a private frame registers `PLAYER_LOGIN`; the handler unregisters it on first dispatch (533-537). Outside gamepad mode it tries to hook `PlayerSpellsFrame` and `MacroFrame` and registers `ADDON_LOADED` only if both are not ready (541-542). The `ADDON_LOADED` branch filters to the two relevant Blizzard addon names (544-546), then unregisters when gamepad mode activates or both hooks have installed (547-558). A `hooked[name]` guard (524-529) prevents duplicate OnShow/OnHide hooks for a named frame. This is a **confirmed one-shot event lifecycle with conditional late-load cleanup**. The HookScript hooks themselves are persistent.

## Extra-bar startup

In `EUI_ActionBars_ExtraBars.lua:794-800`, a local frame registers `PLAYER_LOGIN`, unregisters it inside the handler and schedules one delayed `SetupExtraBars` call. This establishes a source-level one-shot startup path. Other callers of setup and hook-installation multiplicity remain to be checked.

## Blizzard broadcaster preservation caveat

`EUI_ActionBars_Disposal.lua:59-165` deliberately **does not** unregister Blizzard's `ACTIONBAR_SLOT_CHANGED` and `PLAYER_ENTERING_WORLD` on `ActionBarButtonEventsFrame` (comments 81-95). `ns.QuietBroadcasters` selectively unregisters other events from that frame and calls `UnregisterAllEvents` on the separate `ActionBarActionEventsFrame` (125-133). On Forever it may postpone this until login, with gamepad/shaman special cases (111-165). Thus blanket claims that ActionBars clears all Blizzard broadcaster events are incorrect. The comments' taint rationale is upstream design intent, not independent taint verification.

## Completion matrix

| Ownership | Dispatch traced | Conditional cleanup | Status |
|---|---|---|---|
| Vehicle watch frame | yes | UnregisterAllEvents on disable | source-confirmed |
| Faction-cap listener | yes | UnregisterAllEvents when no caps; conditional entering-world unregister | source-confirmed |
| Spellbook/macro late hook installer | yes | PLAYER_LOGIN and ADDON_LOADED unregister | source-confirmed |
| Extra-bar startup | yes | PLAYER_LOGIN unregister | source-confirmed |
| Persistent HookScript installations | yes | no unhook; guards in specific paths | lifetime intentional/partially proven |
| Blizzard broadcasters | selectively altered | intentional retained seed events | source-confirmed implementation, taint untested |

**Remaining ordered work:** complete ActionBars watcher additional event and hook branches; extend same semantic pairing to QoL, CooldownManager, UnitFrames and other packages; then migration semantic consumers, profile rollback, and protected operations. No other addon was analyzed.