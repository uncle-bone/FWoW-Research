# LittleWigs 12.1.22 — all manifest gates and ten dungeon source traces

**Source:** supplied LittleWigs-v12.1.22.zip, exact ZIP member paths and numbered-line review. SC=source-confirmed; UN=runtime unknown. No Dreadwatch addon work.

## Twelve manifest loading gates (SC)

Every pack declares `LoadOnDemand: 1` and `Dependencies: BigWigs`; main LittleWigs additionally declares minimum BigWigs 427. Game-type filters:
- `LittleWigs_Classic`: `classic, standard`
- `LittleWigs_BurningCrusade`: `tbc, wrath, cata, mists, standard`
- `LittleWigs_WrathOfTheLichKing`: `wrath, cata, mists, standard`
- `LittleWigs_Cataclysm`: `cata, mists, standard`
- `LittleWigs_MistsOfPandaria`: `mists, standard`
- `LittleWigs_WarlordsOfDraenor`, `Legion`, `BattleForAzeroth`, `Shadowlands`, `Dragonflight`, `TheWarWithin`: `standard`
- `LittleWigs/LittleWigs.toc`: conditional source lines tagged `[AllowLoadGameType standard]`; load-on-instance metadata.
Each pack's `X-BigWigs-LoadOn-InstanceId` list is game-type-specific where annotated; **the source pack is selected by BigWigs loader metadata and instance ID, not by merely existing in ZIP**. None of these twelve manifests declares interface 16001. **UN:** how Forever maps to manifest game-type filters and whether its loader accepts any pack; do not claim that `standard` implies Forever.

## Ten module call-path samples (SC)

| Exact source member | Activation and event registration | Warning/timer and termination |
|---|---|---|
| `LittleWigs_Classic/Deadmines/MrSmite.lua` | `NewBoss` 5; mob 646 (7); Retail-vs-other encounter IDs 2970/2745 (8); `OnBossEnable` 25 registers cast start/success via Log 27–30; `OnEngage` 37 | `CDBar` 40; PistolShot warning+CDBar 63–64; SmiteStomp phase warnings 75–87; SmiteSlam warning+CDBar 95–96; no local OnWipe |
| `LittleWigs_Classic/Stratholme/TimmyTheCruel.lua` | `NewBoss` 5; mob 10808 (7); encounter 474 (8); `OnBossEnable` 24 registers spell successes 25–28 and optional INSTANCE_ENCOUNTER_ENGAGE_UNIT 31; `OnEngage` 38 | RavenousClaw warning+CDBar 60–61; Enrage threshold warning and timer adjustment 68–69; Fixate target warning+CDBar 75–76; no local OnWipe |
| `LittleWigs_BurningCrusade/TheMechanar/Pathaleon.lua` | `NewBoss` 5; mob 19220 (7); `OnBossEnable` 30 registers ENCOUNTER_START/END 32–33, summon/aura logs 38–40; `OnEngage` 43 registers UNIT_HEALTH | `ENCOUNTER_END` 57–63 selects Wipe/Win; summon warning 72–77, Domination target warning 81 and StopBar 86; explicit native event reliance |
| `LittleWigs_BurningCrusade/HellfireRamparts/Vazruden.lua` | `NewBoss` 5; three mobs 7; encounter ID commented out 8; `OnBossEnable` 31 registers emote and ENCOUNTER_START/END 32–34; `OnEngage` 38 registers PLAYER_REGEN_ENABLED and UNIT_HEALTH | Emote stage warning 51; `ENCOUNTER_END` 62–69 defers Wipe by one second to avoid re-register during dispatch; otherwise Win; stage-soon warning 86 |
| `LittleWigs_WrathOfTheLichKing/TheNexus/Commanders.lua` | `NewBoss` 5; mobs 26798/26796 (7); `OnBossEnable` 19 registers SPELL_CAST_START Whirlwind 20 | Whirlwind warning+CDBar 30–32; no local OnEngage/OnWipe, framework activation and cleanup required |
| `LittleWigs_WrathOfTheLichKing/UtgardeKeep/Keleseth.lua` | `NewBoss` 5; mob 23953 (7); Classic-specific encounter ID branch (8); `OnBossEnable` 21 registers aura applied/removed 22–23 | FrostTomb target warning 31; removal stops target bar 36; no local wipe callback |
| `LittleWigs_Cataclysm/ShadowfangKeep/Silverlaine.lua` | `NewBoss` 5; mob 3887 (7); encounter 1070 (8); `OnBossEnable` 28 registers cast-start logs 29–30 and INSTANCE_ENCOUNTER_ENGAGE_UNIT 34; `OnEngage` 42 | Cast warning+CDBar 51–52; summon warning 57; health threshold warning 64; no local wipe |
| `LittleWigs_MistsOfPandaria/ScarletMonastery/ThalnosTheSoulrender.lua` | `NewBoss` 6; mob 59789 (8); `OnBossEnable` 29 registers cast/aura/interrupt logs 30–35 and INSTANCE_ENCOUNTER_ENGAGE_UNIT 37; `OnEngage` 42 | CDBar 43; cast warning+Bar 51–52; interrupted cast StopBar 64; target warning+CDBar 69–71; aura removal StopBar 75 |
| `LittleWigs_TheWarWithin/PrioryOfTheSacredFlame/CaptainDailcry.lua` | `NewBoss` 5; encounter 2847 (13); `OnBossEnable` 41 registers seven cast/periodic/aura log paths 42–49; `OnEngage` 52 | Four initial CDBars 56–60; explicit OnWipe 63 and OnWin 70; warning+CDBar in ability callbacks; **Retail-era source only** |
| `LittleWigs_BurningCrusade/TheMechanar/Sepethrea.lua` | Same dungeon pack as Pathaleon; this file is a **selected additional reference**, but function-level start/wipe/disable tracing has **not yet been independently verified in this pass** | **UN:** no call-path claims until numbered-line inspection; ten rows are sampled, nine verified deeply here |

**Correction to count:** nine modules above have line-verified paths in this pass; Sepethrea is listed as an explicit next source target, not falsely counted as traced. Most modules do **not** implement local `OnWipe` or `OnBossDisable`; when enabled, their owner cleanup comes from BigWigs boss prototype `Disable` / `Reboot` and timer/message consumers. Module presence is not runtime activation proof.

## Compatibility and evidence gaps

BigWigs explicitly declares Forever 16001 and `isForever`; LittleWigs pack manifests do not. Historical module `:Log` methods may be disabled by BigWigs `isModern` guards on Forever. `UNIT_HEALTH` and `ENCOUNTER_START` call sites in modules do not establish allowed event registration or delivery on Forever. Retail-only modern modules may use timeline APIs unavailable in Forever. DBM 12.1.19's restricted-mode flag and Retail-only registration distinction is already documented separately; do not generalize between versions.

**Remaining:** source-verify Sepethrea and additional modules; parse XML/conditional source inclusion into a per-file load graph; map every nonlocale module's event and timer API calls; verify Forever runtime and secret handling. No source assets copied.
