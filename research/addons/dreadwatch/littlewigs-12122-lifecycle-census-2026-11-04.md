# LittleWigs 12.1.22 module lifecycle census — pinned archive

**Source:** `LittleWigs-v12.1.22.zip`, SHA-256 `eb3d3f04c5b9f343988aeb053468fdf75674e13f1e5e2770365636d01a751c7c`. **SC** source-confirmed, **IN** inferred, **UN** unknown. Lexical census of **all 907 Lua files**, including locale/helpers, not a claim of 907 runnable boss modules. Dreadwatch implementation/prototype work suspended.

## All 12 manifests and load gates

| TOC package | Direct Lua lines in TOC | Interfaces (first shown) |
|---|---:|---|
| LittleWigs | 0 | 11508,11509,…120107 |
| LittleWigs_Classic | 0 | 11508,11509,…120107 |
| LittleWigs_BurningCrusade | 66 | 20505,20506,… |
| LittleWigs_WrathOfTheLichKing | 72 | 30405,38002,… |
| LittleWigs_Cataclysm | 64 | 40402,50503,… |
| LittleWigs_MistsOfPandaria | 38 | 50503,50504,… |
| LittleWigs_WarlordsOfDraenor | 40 | 120100,120105,120107 |
| LittleWigs_Legion | 86 | 120100,120105,120107 |
| LittleWigs_BattleForAzeroth | 74 | 120100,120105,120107 |
| LittleWigs_Shadowlands | 50 | 120100,120105,120107 |
| LittleWigs_Dragonflight | 50 | 120100,120105,120107 |
| LittleWigs_TheWarWithin | 100 | 120100,120105,120107 |

Counts are **direct noncomment TOC lines ending in .lua**, not all Lua files reachable through XML or other includes. None of these twelve manifests declares Forever interface **16001** (SC); missing interface alone is not conclusive proof that every client rejects the addon (UN). Main package depends on BigWigs and minimum BigWigs 427.

## Complete archive-wide lexical lifecycle counts

| Pattern | Lua files containing it |
|---|---:|
| `:NewBoss(` | 765 |
| `function mod:OnBossEnable` | 707 |
| `function mod:OnEngage` | 501 |
| `function mod:OnWin` | 33 |
| `function mod:OnWipe` | 1 |
| `ENCOUNTER_START` | 12 |
| `ENCOUNTER_END` | 34 |
| `ENCOUNTER_TIMELINE` | 59 |
| `:Log(` | 679 |
| `issecretvalue` | 0 |

**Method:** decode every `.lua` ZIP member and count files matching each literal/regular-expression token. Counts can include comments, false positives and multiple independent modules per file; they are **not** execution-path or portability evidence. `:Log` denotes BigWigs combat-log event subscription, not enabling native `LoggingCombat()`.

## Source-pattern distinctions

- **SC:** `LittleWigs_BurningCrusade/TheMechanar/Pathaleon.lua`, `Sepethrea.lua`, `HellfireRamparts/Vazruden.lua` are among explicit `ENCOUNTER_START` examples. Explicit `ENCOUNTER_END` appears in classic `Stratholme/TimmyTheCruel.lua`, `Deadmines/Cookie.lua`, `MrSmite.lua` and the Pathaleon module. These are classic/legacy lifecycle patterns and not verified on Forever.
- **SC:** `LittleWigs_TheWarWithin/PrioryOfTheSacredFlame/CaptainDailcry.lua` is the only archive file with a literal `function mod:OnWipe` definition. This does **not** imply other modules lack wipe handling; BigWigs framework provides default wipe and encounter-end machinery.
- **SC:** 59 files contain timeline API identifiers, including `LittleWigs/Midnight/DenOfNalorakk/TheHoardmonger.lua` and other modern modules. These are Retail modern examples, not evidence of Forever event support.
- **SC:** no file contains literal `issecretvalue`, so direct per-module secret guards are absent by this lexical test; safe behavior may be delegated to BigWigs core/plugins (**UN**).

## Reference priority and outstanding exact work

1. Parse every TOC/XML conditional include to distinguish **loaded source** from files merely present in archive; direct TOC count does not settle this.
2. Extract per-file module ID, zone, game-type, registered events, `:Log` events and timer/message calls with line numbers; audit representative Classic, BC, Wrath, Retail and Midnight paths.
3. Trace LittleWigs pack loader into BigWigs `LoadZone`/module enablement; test whether Forever ever selects these packs.
4. Audit secret-value data paths in the shared framework and module callbacks, not just the absence of `issecretvalue` tokens.
5. Preserve licensing restrictions; source is research evidence, not reusable implementation.

**Coverage:** complete ZIP-member lexical census and 12 TOC interface inventory; full 907-file call-graph review **not complete**, runtime Forever viability **UN**.
