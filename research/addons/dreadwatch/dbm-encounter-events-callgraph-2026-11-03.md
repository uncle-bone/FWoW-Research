# DBM modern encounter warning/timeline adapter: call graph

**Inspected:** 2026-11-03; upstream [DBM-Core/modules/EncounterEvents.lua](https://github.com/DeadlyBossMods/DeadlyBossMods/blob/main/DBM-Core/modules/EncounterEvents.lua), blob `f0c45d80f20d0f2c16ef51ba0ce28976d317a333`, 275 lines. This is **current GitHub source**, not proven byte-identical to the uploaded DBM-Core 12.1.19 archive. Evidence: **SC** source-confirmed; **IN** inferred; **UN** unknown; **OL** none.

## Function inventory and execution paths

| Function and lines | Inputs and routing | State/effects | Evidence |
|---|---|---|---|
| `DBM:ENCOUNTER_WARNING` 26–80 | Structured warning info; reads text/caster/target/GUID/spell/severity; consumes existing target/special warnings, applies 0.5s AntiSpam, IgnoreBlizzAPI/AllowOnce/HideDBMWarnings options | Formats target/caster and dispatches `AddWarning` at severity 0 or `AddSpecialWarning` at higher severity | SC |
| `DBM:ENCOUNTER_TIMELINE_EVENT_ADDED` 90–133 | Event info and remaining duration; looks up `GetEventState`, spell/name/source/color | Honors HideDBMBars, DontShowBossTimers, DontShowUserTimers, IgnoreBlizzAPI; calls `DBT:CreateBar` (variance path conditional), paused if state 1 | SC |
| `DBM:ENCOUNTER_TIMELINE_EVENT_STATE_CHANGED` 141–221 | Event ID; resolves hardcoded mapped timer IDs, bugged IDs, stale mappings; `GetEventState` | Pause/resume/cancel bar or text-only countdown; fire DBM timer events; clear mapping only if still owned by same event | SC |
| `DBM:ENCOUNTER_TIMELINE_EVENT_COLOR_CHANGED` 223–237 | Event ID and color API | Updates bar color conditionally with secret-color check | SC |
| `DBM:ENCOUNTER_TIMELINE_EVENT_REMOVED` 240–250 | Commented-out function | **Not active** in inspected file | SC |
| `DBM:RecoverBlizzardTimers` 254–265 | `HasActiveEvents`, `GetEventList`, `GetEventInfo`, `GetEventTimeRemaining` | Replays event-added handler for currently active timeline events | SC |
| `DBM:GigaTimerTest` 268–275 | Test count/queue settings | Creates scripted timeline events via `C_EncounterTimeline.AddScriptEvent` | SC |

## State and error/security considerations

- **SC:** Warning handler has suppression paths before display, including consuming an already represented warning, 0.5-second anti-spam, module-level Blizzard API suppression and global warning hiding.
- **SC:** `eventInfo` comments mark caster/target/spell/icon fields as secret; timeline event handler comments likewise label spell/name/source/icon fields as secret. The code performs string formatting and debug rendering on these values, so a source-only review **cannot certify** those operations as safe in every Forever combat context.
- **SC:** `ENCOUNTER_TIMELINE_EVENT_ADDED` reads non-secret duration, rounds it for diagnostics, obtains event color through `C_EncounterTimeline.GetEventColor` when not provided, and passes event ID, duration, icon, color, spell name and pause state to DBT.
- **SC:** The state-change handler explicitly protects hardcoded timer IDs against stale pause/resume/cancel notifications when an event ID maps to a newer timer; it also treats known buggy Blizzard timer IDs separately.
- **SC:** Text-only timer lifecycle is handled even if visual bars are hidden; mapping/owner cleanup is conditional to avoid terminating a newer event.
- **IN:** DBM's `RecoverBlizzardTimers` is useful as a reference for UI reload/re-entry reconciliation; whether the same APIs expose active events in Forever 70755 is **UN**.
- **UN:** Registration location and precise DBT implementations, error-handling boundaries around secret operations, and live event payload availability need additional call-graph passes.

## Dreadwatch actionable conclusions

1. Separate event normalization from warning presentation; preserve suppression and duplicate prevention without copying DBM code.
2. Track timeline IDs and timer ownership so stale cancel/pause events cannot affect newer bars.
3. Support active-timeline recovery after UI initialization, contingent on verified Forever API behavior.
4. Keep an explicit compatibility guard for secret values and restricted event payloads; do not log or serialize unknown secret fields.
5. Test all lifecycle branches: added/paused/resumed/canceled/replaced/recovered, duplicate warnings, user-disabled timers, and barless countdowns.

**Remaining:** inspect DBM-Core's actual registration dispatcher, DBT bar implementation and ownership maps, BigWigs timeline adapter, then cross-compare with Forever build 70755. No live tests performed. This report is independently authored and contains no upstream code dumps.
