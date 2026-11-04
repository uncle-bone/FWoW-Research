# Dreadwatch 0.1.1-bigtest: module registry, encounter activation and warning scheduler

**Source:** supplied `Dreadwatch-v0.1.1-bigtest.zip` (SHA-256 `aa23d52fbf7a14af0165aa7602c8ce2c9aca9f4e5b25ceb935fcba7d32ac7eed`), `Dreadwatch/Core.lua` lines 1–104, `Dreadwatch/Modules.lua` lines 1–30, `Dreadwatch/TestHarness.lua` lines 1–30, and `Dreadwatch/UI.lua` lines 1–91. **SC** source-confirmed; **IN** inferred; **UN** unknown; **OL** no live observations. This is the **actual packaged prototype engine**, **not** the retired DreadwatchPTR. [HEAD comparison](github-head-vs-bigtest-2026-11-04.md): these Lua files are not present in the pinned GitHub repository.

## Registry and initialization

**SC:** TOC loads Core before Modules; Core creates frame `DW`, initializes `modules={}`, `callbacks={}`, `timers={}`, `encounter=nil`, `phase=1`, `testing=false`. `Modules.lua:4–8` `DW:RegisterModule(id,name,zone,source)` accepts numeric IDs and string names; overwrites an existing entry with the same ID without collision warning, preserving supplied zone/source or fallbacks. `Modules.lua:9–23` seeds **13** identities (four Hall of Thanes, four Ragefire Chasm, five Stormwind Stockade) from static KwikTip/70707 catalog. `ListModules` counts map keys and prints static entries, explicitly not live boss scripts. **SC:** no per-module event handlers, `encounterID → module` activation, encounter-zone gate, phase callbacks, or difficulty-specific mechanics exist. **IN risk:** ambiguous ID aliases or duplicate IDs could silently replace registry metadata.

## Encounter state and callbacks

- `Core.lua:24–27` `DW:On(name,fn)` rejects nonstring event names/nonfunction callbacks; appends valid callbacks, no unsubscription or maximum.
- `Core.lua:29–33` `DW:Emit(name,...)` loops callbacks in insertion order; each runs inside `pcall`, logs errors and continues; no return aggregation.
- `Core.lua:35–39` `DW:StartEncounter(id,title,simulated)` ends existing encounter with reason `replaced`, then creates a new one with secret-guarded id/title, timestamp from `GetTime()`, boolean simulated flag, resets phase to 1 and emits `start`. **SC:** does not look up `self.modules[id]`, enforce `DreadwatchDB.enabled`, or register a live encounter event. An arbitrary caller can start any ID.
- `Core.lua:41–47` `DW:EndEncounter(reason)` is a no-op without active encounter; otherwise clears encounter/timers, emits `end`, and resets `testing`. **SC:** no wipe/win classification, multi-boss tracking or delayed logging ownership transition.
- `Core.lua:63–78` only `ADDON_LOADED` and `PLAYER_ENTERING_WORLD` are registered. Addon load initializes enabled/sound/scale defaults and probes API names. World entry ends a **nonsimulated** active encounter with reason `zone change`; synthetic encounters persist through that event. **SC:** no `ENCOUNTER_START`, `ENCOUNTER_END`, `BOSS_KILL`, `INSTANCE_ENCOUNTER_ENGAGE_UNIT`, `ENCOUNTER_WARNING`, or timeline registrations.
- `Core.lua:80–104` slash commands `/dw test`, `bigtest`, `next`, `stop`, `on/off`, `modules`, `status`, `diagnose`, `sound on/off`, `move`. These commands are in the archive only, not GitHub HEAD.

## Warning and timer scheduling

- `Core.lua:49–53` `DW:Schedule(key,label,seconds)` validates string key/label and numeric duration in (0,3600], then writes `self.timers[key]={label,deadline=GetTime()+seconds,duration=seconds}`, emits `timer`, returns true. **SC:** key reuse silently replaces a timer; there is no encounter guard, owner ID, timer cap, callback-on-expiry, cancellation API, priority, repeat schedule, or anti-spam.
- `Core.lua:55–57` `DW:Warn(message)` accepts a string up to 200 bytes and emits `warning`. **SC:** no encounter guard, severity, target attribution, sound, deduplication, cooldown, privacy/secret check of message, or localization.
- `TestHarness.lua:9–14` `RunBigTest` creates synthetic encounter, loads phase 1, and emits UI state; `LoadTestPhase` at 16–24 requires a synthetic encounter, **clears all timers** then emits warning and schedules phase bars. `NextTestPhase` at 26–30 advances through three phases or ends. **SC:** phase changes can discard prior timers without `timer-canceled` callbacks.
- `UI.lua:48–80` listens to `start`, `end`, `warning`, `move`; its 0.1-second `OnUpdate` calculates remaining time and renders up to six sorted timer bars. It does **not** register a `timer` callback; instead it polls `DW.timers`. **SC:** timers can expire visually without removal from the timer table until encounter/phase reset. **IN:** stale timer records can grow and increase per-refresh sorting work in long sessions.

## Behavioral call graph and guards

`/dw test` → `StartEncounter(synthetic)` → `Emit(start)` → UI reset; `Warn` → `Emit(warning)` → UI text; `Schedule` → `Emit(timer)` → no subscribed timer callback; UI polling renders. `/dw bigtest` → `RunBigTest` → `StartEncounter` → `LoadTestPhase(1)` → warning + six timers; `/dw next` → phase 2/3 or `EndEncounter`. `/dw stop` → `EndEncounter` → `Emit(end)` → hide UI. `PLAYER_ENTERING_WORLD` → end nonsynthetic only.

**Error boundaries (SC):** `Emit` isolates callback exceptions with `pcall`; optional sound uses `pcall`. `GetTime`, timer table mutation, `Schedule` and frame update operations are not all guarded. **Secret handling (SC):** `StartEncounter` passes ID/title through `safe`, but `Warn` performs string length/type checks directly and no general native event normalization exists. **Performance (IN):** the UI sorts active timers every 0.1 seconds; no timer or callback cap. **SavedVariables (SC):** only basic UI preferences/position, not encounter/timer histories.

## Exact completion and design gaps

| Group | Source coverage | Unresolved |
|---|---|---|
| Registry creation, 13 seed entries, list, ID overwrite | Complete for ZIP (SC) | Collision/provenance checks, runtime lookup |
| Callback registration/emission/error isolation | Complete for ZIP (SC) | Unsubscribe, caps, event schema |
| Encounter start/end/world entry | Complete for ZIP (SC) | Native event integration, IDs, wipe/win, multi-boss |
| Schedule/warn/phase transitions | Complete for ZIP (SC) | Ownership, cancellation, expiry, anti-spam |
| UI consumer | Partial here; full UI function inventory in [prototype inventory](dreadwatch-v0.1.1-core-inventory-2026-11-04.md) | Frame lifecycle, rendering edge-case tests |
| Live Forever activation | UN | Actual client event delivery, restricted payloads |
| GitHub engine source | Absent at pinned HEAD (SC) | Decide publication path |

## Independent engineering recommendations (IN)

1. Introduce a verified native encounter adapter with event-ID/zone matching, module activation and conservative fallback behavior; never treat static catalog identity as a verified mechanic.
2. Track encounter generation and timer owner so late warning/cancel events cannot modify a newer encounter.
3. Add timer cancel/expiry semantics and bounded storage; decouple UI render cadence from scheduler state.
4. Add warning severity/deduplication with secret-safe normalization and explicit unsupported payload handling.
5. Keep native combat logging as a separate zone-level service, per [DBM-Core 12.1.19 logging audit](dbm-combat-detection-logging-2026-11-04.md).
6. Preserve synthetic tests as explicitly synthetic; do not copy DBM/BigWigs implementations or revive DreadwatchPTR.
