# BigWigs 427.8 message routing: complete archive-wide sender/receiver census

**Source:** supplied BigWigs-v427.8.zip. **SC** lexical/source-confirmed, **IN** inferred, **UN** runtime unverified. Every one of 173 Lua files was scanned for `RegisterMessage`, `SendMessage` and matching function definitions for the listed messages. Counts are **files containing send/subscribe/handler occurrences**, not counts of runtime listeners; callbacks may be dynamically registered. Dreadwatch work remains paused.

| Message | Matching Lua files | Explicit receiver / key producers |
|---|---:|---|
| BigWigs_StartBar | 30 | Bars.lua:1460/1883; BossPrototype.lua, BossPrototype_Classic.lua, Timeline.lua, Pull.lua, Break.lua, Wipe.lua, Statistics.lua, API.lua, Keystones.lua, 20+ modern boss scripts |
| BigWigs_StopBar | 28 | Bars.lua:1463; both boss prototypes, Timeline.lua, Pull.lua, Break.lua, Nameplates.lua, Statistics.lua, modern boss scripts |
| BigWigs_StopBars | 4 | Bars.lua:1464, Nameplates.lua:1828, both boss prototypes |
| BigWigs_PauseBar | 24 | Bars.lua:1461; Timeline.lua, both prototypes, modern boss scripts |
| BigWigs_ResumeBar | 24 | Bars.lua:1462; Timeline.lua, both prototypes, modern boss scripts |
| BigWigs_Timer | 7 | API.lua, Keystones.lua, both prototypes, Bars.lua, Wipe.lua, Statistics.lua |
| BigWigs_Message | 11 | Messages.lua:801/940; both prototypes, Victory, Break, BossBlock, Pull, Timeline, Bars, Keystones and one modern boss script |
| BigWigs_StartCountdown | 5 | Countdown.lua:568/645/753; both prototypes, Pull.lua, Keystones.lua |
| BigWigs_BarCreated | 1 | Bars.lua:1915; **Retail-only** broadcast |
| BigWigs_BarEmphasized | 1 | Bars.lua:1866/1919; 1919 path Retail-only; inspect 1866 condition separately |

**Important:** `BigWigs_Timer` is a timer-analysis/observer message, not necessarily a bar renderer; `BigWigs_StartCountdown` is consumed by Countdown.lua rather than Bars.lua. Bars.lua owns visual bars and LibCandyBar expiry callbacks; Messages.lua owns warning text. `BigWigs_StopBars` is also subscribed to by Nameplates.lua, so module cleanup extends beyond bars. These are distinct consumer channels.

## Precise source call sites

- Bars.lua 1455–1477 subscribes bar lifecycle and cross-addon custom timer messages; 1532–1594 handles pause/resume/stop/module cleanup; 1798–1922 builds and starts bars, enforces eventId for secret labels.
- Messages.lua 794–810 subscribes warning messages; 940–979 renders them; 982–1019 separately handles native `ENCOUNTER_WARNING` when enabled.
- Countdown.lua 568, 645, 753 contains the StartCountdown registration/handling paths; inspect its stop/cleanup behavior in the next deeper pass.
- Nameplates.lua 1828 references `BigWigs_StopBars`; check whether this is subscription, send or both in deeper pass.
- `BigWigs_BarCreated` only originates from Bars.lua and is explicitly emitted under `if isRetail`; do not treat as Forever behavior.
- A large number of modern Midnight boss scripts emit native timeline-related bar messages directly; their Retail-only TOCs are not Forever support evidence.

## Outstanding deep-review gaps

**UN:** dynamically named messages, full Countdown.lua state machine, Nameplates.lua cleanup, LibCandyBar implementation and expiry callback ordering, the options/UI paths in 2,125-line Bars.lua, timer-message observers, message transport reentrancy and secret-value propagation into downstream display APIs. No live Forever validation. Do not infer registration solely from handler presence.
