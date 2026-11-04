# LittleWigs v12.1.22 — manifest and archive coverage inventory

**Source:** supplied `LittleWigs-v12.1.22.zip`. **SC** source-confirmed; **IN** inference; **UN** unknown. This is the first inventory pass, **not** an exhaustive function-level review of 907 Lua files. Dreadwatch addon analysis remains stopped; DreadwatchPTR retired.

## Manifest and compatibility gates

**SC:** `LittleWigs/LittleWigs.toc` declares version `v12.1.22`, `Dependencies: BigWigs`, `LoadOnDemand: 1`, `X-BigWigs-Minimum: 427`. Interface values include 11508/11509, 20505/20506, 30405, 38002, 40402, 50503/50504 and 120100/120105/120107, **not Forever 16001**. Manifest has `X-BigWigs-LoadOn-InstanceId` plus conditional `[AllowLoadGameType standard]` and expansion-specific file lines. **SC:** `X-License` says All Rights Reserved with GitHub fork/modify allowance and permission required for other use. No blanket license to copy into another addon.

## Archive enumeration

**SC:** 907 Lua files. Top-level folder counts (including localization and option files) include `!Locales` 120, `Midnight` 75, `Delves` 55, `Stratholme` 14, `DireMaul` 14, `Deadmines` 13, `Karazhan` 12, `KarazhanCrypts` 11, `AssaultOnVioletHold` 9, `Mechagon` 9, `Tazavesh` 9, `DawnOfTheInfinite` 9. **SC:** archive-wide string scan found `ENCOUNTER_START` in 12 Lua files, `:Engage(` in 7, and `:Log(` in 679. These are **lexical counts, not verified handler counts**; inherited BigWigs methods mean many modules rely on framework lifecycle rather than declaring their own event handlers.

## Relevant lifecycle pattern

**SC:** `TBC/TheMechanar/Pathaleon.lua` (previously inspected in reference matrix) demonstrates explicit `ENCOUNTER_START`/`ENCOUNTER_END` and boss win/wipe paths with spell-event callbacks. This is a **historical module pattern**, not evidence it runs under Forever. **SC:** the shared BigWigs framework supplies `NewBoss`, `SetEncounterID`, `Log`, `OnBossEnable`, `OnEngage`, `OnWin`, `OnWipe`, timers, cleanup and event routing; exact module-specific choices vary by expansion and game type. LittleWigs modules should be classified by manifest condition and actual API use before claiming portability.

## Unknowns and required systematic next pass

1. Parse all TOC conditional sections into file→game-type/instance inclusion table; separate current Retail/Midnight and Classic modules.
2. For each nonlocale boss/trash Lua file, extract `NewBoss` / `SetEncounterID` / `OnBossEnable` / `OnEngage` / `OnWin` / `OnWipe`, `RegisterEvent` / `Log` / `RegisterUnitEvent` call sites, timer/message/secret API use; record file path and line.
3. Classify Forever viability separately: 16001 absent from manifest; conditional game type, API availability and restricted payload safety **UN**. A historical module is not automatically Forever-compatible.
4. Cross-reference pinned BigWigs 427.8 framework behavior; do not infer native combat recording from `:Log` combat-log event listeners.

**Coverage:** manifest requirements and archive enumeration **SC complete**; 907-file function inventory **partial**; live Forever compatibility **UN**.
