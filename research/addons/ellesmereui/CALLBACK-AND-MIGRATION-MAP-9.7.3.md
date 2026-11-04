# EllesmereUI 9.7.3: callback dispatch, lifecycle, and migration inventory

**Research date:** 2026-11-03. **Version:** uploaded `EllesmereUI-9.7.3.zip`, SHA-256 `8c572970a01b94d26ab6be30327200b46b4654e40da33303da3677de3749093e` (archive hash previously recorded; independent current-session hash should be checked against the attached archive before reusing). **Method:** direct ZIP inspection, line-numbered first-party Lua scans, manual review of `EllesmereUI/EllesmereUI_Lite.lua`, `EllesmereUI/EllesmereUI_Migration.lua`, and `EllesmereUI/EllesmereUI_Profiles.lua`. All findings below are **source-confirmed** static implementation facts, not observed-live behavior. Do not substitute upstream 9.7.4.

## 1. EUILite callback dispatch and lifecycle

**Source:** `EllesmereUI/EllesmereUI_Lite.lua:63-156`, `:478-555`.

- `NewAddon(name)` returns the registered object if it already exists; otherwise creates the addon object, enqueues initialization and eagerly creates its dedicated event frame.
- `GetOrCreateEventFrame` installs a single `OnEvent` dispatcher, looking up `frame._handlers[event]` and calling it with `(addon,event,...)`.
- `_RegisterEvent(self,eventname,callback)` resolves **function** callbacks by storing the function itself; **string** callbacks by a closure that late-looks up `addon[callback]`; and **omitted** callbacks by a closure that late-looks up `addon[eventname]`. It stores the resolved handler under `_handlers[eventname]` and calls `frame:RegisterEvent(eventname)`. Registering again replaces the stored handler.
- `_UnregisterEvent` clears the stored handler and unregisters the event from that addon's frame. This is not an automatic teardown for unrelated frames, hooks or timers.
- `lifecycleFrame` listens for `ADDON_LOADED` and `PLAYER_LOGIN`. It drains queued `OnInitialize` callbacks with `safecall`; enabled addons are then queued for `OnEnable`. At login, enable flush is synchronous; for post-login `ADDON_LOADED`, enable flush is deferred by `C_Timer.After(0,...)`. The source explains a secure-chain taint concern; that is upstream design rationale, not independently verified taint absence.
- `OnSavedVariablesLoaded(fn)` collects hooks that execute when the parent addon loads, then wipes the hook array.

**Coverage:** dispatcher mechanics source-confirmed. Which runtime branches execute, per-package actual frame ownership, hook teardown, and callback alias resolution are **unknown** until deeper analysis/tests.

## 2. Migration registration and state

**Source:** `EllesmereUI/EllesmereUI_Migration.lua:14-125` and registrations throughout the file.

A static source scan of the uploaded 9.7.3 file identified **114** `RegisterMigration` calls with literal ID/scope pairs: **42 global, 59 profile, 13 specProfile**. The registration validator rejects non-table specs, empty/nonstring IDs, nonfunction bodies, invalid scopes and duplicate IDs. `RunOne` calls bodies inside `pcall`, stamps `_migrations[id]=true` only on success and records failures in `EllesmereUI._migrationErrors`. `RunMigration` walks the appropriate global/profile/specProfile store. **Source-confirmed.** The body of every individual migration and partial-write rollback are **not yet proven safe**. Because the body is retried after a failure, idempotence is a requirement, not a demonstrated property.

## 3. Profile/state API inventory

**Source:** `EllesmereUI/EllesmereUI_Profiles.lua`, source-confirmed function definitions.

| Function / symbol | Line |
|---|---:|
| `PreSeedSpecProfile` | 1015 |
| `SnapshotAllAddons` | 1048 |
| `ApplyProfileData` | 1130 |
| `RefreshAllAddons` | 1541 |
| `OnSpecSwitchComplete` | 1587 |
| `ExportProfile` | 2185 |
| `EncodePayload` | 2372 |
| `ImportFullAccountData` | 2563 |
| `DecodeImportString` | 2915 |
| `DecodeImportStringAsync` | 2983 |
| `ImportProfile` | 3313 |
| `SwitchProfile` | 3952 |
| `GetActiveProfileName` | 4035 |
| `AutoSaveActiveProfile` | 4056 |
| `SetProfile` | 4889 |
| `ImportProfileSilent` | 5057 |
| `RegisterExternalInstaller` | 5180 |

These are **API locations**, not a guarantee of externally stable contracts. Import/export validation, asynchronous completion, profile switch rollback and save timing require further branch tracing.

## 4. Package registration/cleanup mapping: coverage matrix

The first-party static callback index generated from the uploaded ZIP covers **639 non-library Lua files across 25 package directories** (the larger archive contains additional bundled libraries and other Lua). Each file was scanned for literal `RegisterEvent`, `UnregisterEvent`, `SetScript`, `HookScript`, secure hooks, timers, combat guards, addon messages, and cleanup candidates. The full per-file line-numbered index is a separate conversation artifact (`EllesmereUI_9.7.3_Callback_Map.md`); this GitHub report summarizes the verified dispatcher semantics and high-priority trace anchors. **Lexical registration counts are not runtime registrations.** A callback passed through a local alias or table may not be resolved by text scanning.

| Major package | Registration/dispatch path to close | Cleanup / correctness gap | Status |
|---|---|---|---|
| Core framework | `EllesmereUI_Lite.lua` dedicated event frame and lifecycle | parent/child disable, event lifetime, pre-SV hooks | Dispatcher traced; dynamic callers pending |
| ActionBars | `EUI_ActionBars_Events.lua`, `_Secure.lua`, `_VisibilityDrivers.lua` | state-driver unregistration, protected combat edits | Pending |
| CooldownManager | package `Init`, events and CDM hooks | external CDM ownership, combat reconfigure | Pending |
| Nameplates | package event/frame callbacks | recycled nameplate teardown, update frequency | Pending |
| UnitFrames | package frame/event handlers | unit swaps, protected frame edits | Pending |
| RaidFrames | package frame/event handlers | secure headers and roster updates | Pending |
| Minimap | package events and hooks | hooks/scale/frame cleanup | Pending |
| Bags | package events and hooks | open/close and item cache lifetime | Pending |
| Chat | package filters/hooks | duplicate filters and restored UI | Pending |
| DataBars | package ticker/event callbacks | disabled-feature CPU cost | Pending |
| Options | on-demand initialization and widget callbacks | panel teardown and stale closures | Pending |
| ForeverEssentials | Forever-specific gates and event callbacks | game-flavor restrictions | Pending |

Other packages remain indexed in the full first-party inventory, but require the same per-handler tracing. A cleanup call appearing in the same file is **not** proof it unregisters the corresponding handler.

## 5. Exact remaining blockers

1. Build a Lua-aware reference graph for assigned callback variables and string-named methods, then manually validate the unresolved call sites.
2. Pair each registration with the actual owning frame/addon, lifecycle, and teardown; document intentionally session-long registrations.
3. Trace all 114 migration bodies for idempotence and partial writes; mock corrupted and older SavedVariables without touching user data.
4. Trace profile import/decode/merge and switch operations through their success, error and combat-deferred branches.
5. Test protected operations, taint and timing on the matching authorized Forever client. **No observed-live results yet.**
6. Measure idle and combat CPU/memory under reproducible settings. **No benchmarks yet.**

**Completeness:** partial. This report closes the EUILite callback resolution mechanism and registers a version-specific migration inventory; it does **not** claim 100% behavioral understanding or runtime certification. Independently authored research only; no upstream source/asset redistribution.
