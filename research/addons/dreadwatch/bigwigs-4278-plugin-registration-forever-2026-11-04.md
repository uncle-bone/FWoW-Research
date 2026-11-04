# BigWigs 427.8 — plugin registrations and Forever branch source pass

**Pinned source:** supplied BigWigs-v427.8.zip. Direct numbered-line inspection of exact ZIP members. SC=source-confirmed; UN=runtime unknown. Reference-only; no Dreadwatch addon work. DBM warning/timeline trace is owned by another workstream.

## Messages.lua (1030 lines)
`OnPluginEnable:794–809` registers `BigWigs_Message`, profile and configuration messages. It registers `ENCOUNTER_WARNING` and Block/AllowBlizzMessages **if `BigWigsLoader.isModern`**, which in this archive includes Forever. Handler `BigWigs_Message:940–979` processes addon warnings; `ENCOUNTER_WARNING:982–1019` processes Blizzard warnings. **Comparison:** exact DBM-Core 12.1.19 registers its analogous adapter only under `private.isRetail`, even though DBM restricted mode includes Forever. Registration conditions differ; event delivery and secret-safe runtime remain UN.

## Sound.lua (655 lines): voice/audio consumer
`OnPluginEnable:304–399` loads profile/media, registers `ADDON_RESTRICTION_STATE_CHANGED`, `BigWigs_Sound`, profile/module/aura messages, and on **isModern** registers `ENCOUNTER_WARNING` plus Block/AllowBlizzMessages. `BigWigs_Sound:625–629` resolves a media path and plays it. `ENCOUNTER_WARNING:638–646` reads `shouldPlaySound` and `severity`, maps severity to alert/alarm/warning, and plays sound only when allowed. This is an independent native-warning consumer from Messages.lua. No separate `Voice.lua` member exists in this ZIP; voice countdowns live in `Countdown.lua`.

## Countdown.lua (754 lines)
`OnPluginEnable:539–576` preloads configured countdown sound assets with zero-delay timers, then registers StartCountdown, StopCountdown, boss disable/wipe, ClearNameplate, profile/config. `StartCountdown:645–700` uses module/text and optional GUID timer identity, cancels older countdown logically, schedules per-second callbacks; `StopCountdown:701–714` and boss disable 715+ invalidate state. See existing countdown report for lifecycle details.

## InfoBox.lua (705 lines)
`OnPluginEnable:369–378` subscribes Show/HideInfoBox, boss disable/wipe and profile. `ShowInfoBox:388–410` closes previous opener, dynamically subscribes six update messages (title, line, table, table-with-bars, bar, timer-bar), sets opener, enumerates group names and shows frame. `Close:624–643` unregisters those six update messages; `OnPluginDisable:380–382` closes. `BigWigs_OnBossDisable:686+` closes for owner. **State boundary:** the update-message subscriptions exist only while a box is open, unlike the permanent show/hide subscriptions.

## AutoReply.lua (404 lines)
`OnPluginEnable:143–150` subscribes boss engage, win/wipe, disable and profile. `OnBossEngage:163–171` checks options and valid boss context, sets current module/difficulty, resets throttles and registers `CHAT_MSG_WHISPER` and `CHAT_MSG_BN_WHISPER` only during encounter. `WinOrWipe:201–205` and `OnBossDisable:257–261` unregister whisper listeners. `OnPluginDisable:153–157` resets module, throttle and health-pool state. **UN:** secret-sensitive player/group health and chat behavior on Forever requires runtime verification.

## Proximity.lua (985 lines)
`OnPluginEnable:622–632` subscribes Show/HideProximity, boss wipe/disable and profile; `OnPluginDisable:635–638` clears custom-target state and closes. `Close:850–856` unregisters group-roster and raid-target frame events; proximity activation later registers group-roster update around 896. The options block at 644+ is commented in this source; do not infer live controls from those comments.

## BossBlock.lua (1373 lines): explicit Forever gates
`isForever=loader.isForever` line 55. Several option entries are hidden for Classic **or Forever** (123,131,183); `TALKINGHEAD_REQUESTED` registration is guarded by `not isForever` (454–455). Boss engage/disable/wipe subscriptions 385–392, plus BOSS_KILL and cinematic/toast events around 433–451. These explicit gates show that even where BigWigs groups Forever with modern clients, individual plugins may require separate Forever exclusions.

## BattleRes.lua (1632 lines)
`OnPluginEnable:1538–1552` loads profile and starts delayed instance check; `OnPluginDisable:1555–1566` hides frame, stops updater and cooldown and only unregisters combat-log listener when `not isModern`. Other paths 1488–1522 register encounter start/end, combat state, challenge-mode and optional combat log. **UN:** runtime eligibility of each native event on Forever.

## AltPower.lua (885 lines)
`OnPluginEnable:470–476` subscribes start/show/hide power, boss disable/wipe and profile; `ShowAltPower:649+` adds plugin comm and group roster; `Close:790–801` removes group roster and plugin comm. Per-encounter subscriptions are not permanent.

## Mythic+, Range and Transcriptor paths
No standalone `Mythic.lua`, `Range.lua`, `Voice.lua` or `Transcriptor.lua` Lua member exists in this supplied ZIP. Actual Mythic+ reference paths include `BigWigs/Tools/Keystones.lua` and `BigWigs/Libs/LibKeystone/LibKeystone.lua`; range behavior is integrated into Proximity and boss prototype methods. Do not fabricate missing plugin files. Transcriptor integration must be searched by call site rather than assuming a dedicated module. Those deeper call graphs remain open.

## Cross-source compatibility
| Behavior | BigWigs 427.8 source | DBM-Core 12.1.19 comparator |
|---|---|---|
| Forever client distinction | `isForever` true, `isModern=isRetail or isForever` | `private.isForever` separate, `IsRestricted()` includes both |
| Native encounter warning registration | Messages and Sound register under `isModern` | User-audited adapter registered under `private.isRetail` |
| Legacy combat-log subscription | Some prototype functions return on `isModern` | Health unit event registration on Forever remains unverified/filtered |
| Runtime payload safety | UN | UN; secret-aware display does not prove adapter formatting safe |

**Remaining:** Keystones and LibKeystone source lifecycle; all other plugin message paths, Transcriptor references, exact secret value handling and measured Forever behavior. This report is partial, not exhaustive certification of 173 Lua files.
