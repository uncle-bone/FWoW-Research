# BigWigs 427.8 — pinned archive source trace (reference only)

**Scope:** supplied `BigWigs-v427.8.zip`, 173 Lua files; primary source `BigWigs_Core/Core.lua` (823 lines), `BigWigs_Core/BossPrototype.lua` (5,407 lines), `BigWigs_Plugins/Timeline.lua` (417 lines). **SC** source-confirmed, **IN** inferred, **UN** unknown. This is a **targeted end-to-end lifecycle trace**, not certification of all 173 files. Dreadwatch engine/prototype work suspended by user priority; retired PTR excluded.

## Core loader, event dispatch and enablement

**SC:** `Core.lua:41–57` one shared `bwUtilityFrame` dispatches an `eventMap[event]` of module→function-name/function callbacks; invokes callbacks directly (no per-callback pcall at this dispatch site). `RegisterEvent` (59–74) validates handler presence, allows replacement, warns if registering during same event dispatch, registers frame event. `UnregisterEvent` (75–83) removes module and only unregisters frame event when last subscriber is gone. `UnregisterAllEvents` (85–96) hooks boss disable/wipe and plugin disable messages. **IN:** a handler error can interrupt the current dispatch; a callback modifying eventMap during iteration needs live regression.

**SC:** `mod:ADDON_LOADED` (245–251) initializes queued modules after owning addon load. `core:Enable` (312–348) registers `ENCOUNTER_START`, whisper/mouseover/world-leave and optional zone/delve events, enables plugins, then for `loader.isModern` enables zone-matching trash modules without NPC scans. `mod:ENCOUNTER_START` (103–112) matches encounter IDs, calls `module:Enable()` then `module:Engage()`, and disables stale enabled but not engaged candidates. `DisableCore` (266–291) unregisters core events, stops configuration, disables bosses/plugins, broadcasts `BigWigs_CoreDisabled`. `PLAYER_LEAVING_WORLD` explicitly disables core; world-boss zone changes have safeguards for dead player, options and active bars (292–300).

## Boss module lifecycle and cleanup

**SC:** `BossPrototype.lua:590–632` `Initialize` registers boss module; `Enable` sets enabled, refreshes data, resets scheduled-event table, adds to enabledModules, subscribes `ENCOUNTER_END` if encounter ID exists, conditionally enables pet/range checks, calls `OnBossEnable`, detects mid-encounter recovery and emits enable message. `Disable` (643–761) calls `OnBossDisable`, removes enabled module, cancels timers, drops scheduled state; when no enabled modules remain, unregisters classic combat-log event and pet/nameplate events and resets shared scanning caches. Clears engagement/win/wipe/stage and other per-fight state; sends disable message except wipe reboot. `Reboot` (763–774) emits wipe message then disables/re-enables. **SC:** this combat-log event registration is **addon event consumption**, not proof of native `LoggingCombat(true)` recording ownership.

**SC:** module functions include `RegisterEnableMob` (217), `SetEncounterID` (306), `GetEncounterID` (332), `IsEncounterID` (344), `Engage`, `EncounterEnd`, `Wipe`, `Win`, `RegisterBossEvent` (1894), `Log` (1501), `RemoveLog` (1524), `ScheduleTimer` (5154), `ScheduleRepeatingTimer` (5169), `CancelTimer` (5182), `CancelAllTimers` (5189). Normal and restricted/modern branches differ; these are reference call sites, not Forever runtime proof.

## Timeline plugin event/data paths

**SC:** `Timeline.lua:252–289` `UpdateBarsShown` selects native timeline bars based on `timersMode` and active custom-timer encounter IDs; conditionally registers/unregisters `ENCOUNTER_TIMELINE_EVENT_ADDED`, `_STATE_CHANGED`, `_REMOVED`, then starts/stops bars and broadcasts visibility. **SC:** `OnRegister` (295–305) changes encounter warning CVars and unregisters default warning frames; `OnPluginEnable` (307–326) installs profile/boss hooks, can reparent Blizzard timeline to a hidden frame, and sets CVars; `OnPluginDisable` (328–330) stops bars but does not visibly restore all those global CVars/frames at this site (**IN** potential global-side-effect lifecycle issue).

**SC:** `StartBars` (332–349) enumerates `C_EncounterTimeline.GetEventList`, replays active/paused entries using state/info/time remaining; emits `BigWigs_StartBar` and pause. `StopBars` (351–355) emits stop for each listed event. `EVENT_ADDED` (361–388) skips source=Script, tracks ID in `validIDs`, passes spellName/icon and duration into bar message and handles paused. `STATE_CHANGED` (390–410) ignores unknown IDs, emits resume/pause/stop for Active/Paused/Canceled/Finished; EditMode finish generates test warning. `REMOVED` (412–417) deletes tracked ID and stops bar. **IN:** `validIDs` is not explicitly cleared in `StopBars`, so stale IDs may remain across visibility transitions; live behavior needs test.

**SC:** plugin comments distinguish nonsecret `eventInfo.source/id/duration/maxQueueDuration` from secret `spellName/icon`; secret values are forwarded to message consumers, not formatted here except EditMode generated names. `BossPrototype.lua:5140–5141` exposes `issecretvalue`; `Core.lua:120–122` avoids inspecting secret mouseover GUID. **UN:** whether every downstream bar/message consumer can safely accept secret payloads on Forever.

## Forever compatibility and performance

**SC:** `BossPrototype.lua:34` reads `loader.isClassic/isRetail/isForever/isModern`. Range item tables at 2683/2689/2700 explicitly select Forever-compatible item IDs. `Core.lua:335–344` modern clients enable trash by zone rather than NPC scanning. `Core.lua:120–122` secret GUID guard. `BossPrototype.lua:658–674` unregisters combat-log listeners only when no enabled modules remain. **UN:** which modern/Forever flags are set on a particular Warcraft Forever build, API security of other helper functions, or measured CPU/memory. Do not transplant API branches without testing.

## Reference-coverage matrix

| Area | Status |
|---|---|
| Core event map and enable/disable path | **SC traced** |
| Module enable/disable/reboot and cleanup | **SC traced** |
| Timeline plugin event replay, modes and cleanup | **SC traced** |
| Selected Forever-specific branches and secret guards | **SC traced** |
| All 173 Lua files / full boss prototype helpers | **Partial; not exhaustive** |
| Other plugin consumers and transport | **UN/not yet traced** |
| Live Warcraft Forever behavior | **UN** |

**License:** inspect for compatibility research; do not copy source/assets. This audit does not implement or design Dreadwatch.
