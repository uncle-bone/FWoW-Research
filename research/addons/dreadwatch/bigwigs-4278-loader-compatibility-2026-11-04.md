# BigWigs 427.8 loader and Forever compatibility — pinned source audit

**Source:** user-supplied `BigWigs-v427.8.zip`; SHA-256 `49fb2833ed6717f6b4d8931ba43207c7ad648695c909143e24264f72541fb042`. **SC** source-confirmed; **IN** inference; **UN** unverified. This report reviews reference code only. No Dreadwatch engine work, no duplicate DBM warning/timeline audit.

## Archive-wide reproducible inventory

173 Lua files, 12 TOC manifests. `BigWigs/BigWigs.toc`, `BigWigs_Core/BigWigs_Core.toc`, `BigWigs_Options/BigWigs_Options.toc` and `BigWigs_Plugins/BigWigs_Plugins.toc` all declare interface **16001** among other client interfaces. Eight included Midnight raid/zone pack manifests list only Retail interfaces 120100/120105/120107. Main TOC declares `BigWigs3DB`, `BigWigsIconDB`, `BigWigsStatsDB`; core is load-on-demand and depends on BigWigs. `X-License`: All Rights Reserved, GitHub fork/modify allowed, ask permission for other use (SC). Archive lexical counts: `isForever` in six Lua files; `issecretvalue` in seven; `ENCOUNTER_TIMELINE` in 23; `BigWigs_StartBar` in 30; `:RegisterEvent(` in 53. Counts include libraries and are not function certification.

## Forever initialization and loader flags

**SC:** `BigWigs/Init_Camelot.lua:3` sets `tbl.isForever=true`; main TOC selects `Init_[Game].lua` and loads `Loader.lua` afterwards. `BigWigs/Loader.lua:43–46` publishes `isRetail`, `isForever`, `isModern=isRetail or isForever`, and `isClassic`. Therefore a Forever client may use modern event/zone logic without claiming that all Retail APIs are safe. The loader's `public.isForever` branch begins at line 248; expansion/instance pack selection is conditional. **UN:** actual game token resolution and each game-type conditional in the running Forever client.

## Load and event path

**SC:** `Loader.lua:708–718` aliases `C_AddOns` APIs for metadata, enabling, loading, dependencies, and error status. `load(index)` at 826 invokes `LoadAddOn(index)`; `loadAddons(tbl)` at 845 loops selected packs and emits `BigWigs_ModulePackLoaded`; `loadZone(zone)` at 860 selects zone packs; `loadAndEnableCore` at 867 ensures core is loaded/enabled; `loadCoreAndOptions` at 878 and `loadCoreAndOpenOptions` at 891 separate UI loading from core. `PLAYER_ENTERING_WORLD` registered at 1228; handler `Loader.lua:1976–2045` selects current zone/instance and core state. `PLAYER_MAP_CHANGED` (2046) reruns world-entry logic when needed; `ZONE_CHANGED` (2055) is used for world bosses. **SC:** `BigWigs_BossModuleRegistered` at 2103 and `BigWigs_CoreEnabled` at 2132 connect registration to zone load. Loader module messages use `RegisterMessage` (1611), `UnregisterMessage` (1636), `SendMessage` (1650); unregister-all hooks on boss disable/wipe and plugin disable at 1664–1675. `CHAT_MSG_ADDON` at 1727 routes BigWigs boss/plugin communications; this is distinct from native combat-log recording.

## Compatibility and safety boundary

**SC:** `Core/Core.lua` and `BossPrototype.lua` consume `loader.isModern` and `loader.isForever` (see [core trace](bigwigs-4278-source-trace-2026-11-04.md)). `BigWigs_Core/PluginPrototype.lua:86–88` defines an `issecretvalue` fallback and `plugin:IsSecret`; `Core.lua:120–122` guards secret mouseover GUID. **UN:** end-to-end secret safety of message recipients and all bars, audio and nameplate plugins. `BigWigs/Loader.lua:1649–1650` uses `securecallfunction` for message fanout; contrast with core event map's direct callback invocation, so exception isolation differs by dispatch channel. **IN:** code copying would be both technically unsafe and license-constrained.

## Coverage matrix

| Reference area | Status |
|---|---|
| Manifest interface and pack gates | SC, 12 TOCs enumerated |
| Forever flags and modern-client selection | SC |
| Core load / zone load / event and message entrypoints | SC, key call sites traced |
| Boss-module lifecycle / Timeline | SC in [separate pinned trace](bigwigs-4278-source-trace-2026-11-04.md) |
| All loader branches, module packs and 173 Lua functions | Partial |
| Actual Forever runtime | UN |

**Next:** inspect `BigWigs_Plugins/Bars.lua` and message consumers, `BossPrototype_Classic.lua` branch, and module-pack selection in detail. Do not start Dreadwatch engine analysis.
