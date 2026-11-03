# Dreadwatch / Warcraft Forever encounter-source audit

Collected: 2026-11-03  
Target client verified locally: Warcraft Forever flavor `wowf`, version `1.60.1.70755`, interface `16001`.  
Scope: local encounter-related addon inventory plus current public GitHub source and DBM release history. No copyrighted client archives or addon folders were copied into this repository.

## Findings

### Local client

- `DBM-Core` and `DBM-Party-Forever` are installed. The Forever pack TOC is interface 16001, version 270.
- The local Forever pack has 24 boss module scripts: City of Dalaran (9), Excavation Site (4), Hall of Thanes (4), and Ruins of Lordaeron (7).
- Across those scripts: 24 encounter registrations, 24 zone registrations, 24 generic-trash enables, zero active creature-ID declarations, zero boss spell/event handlers, and zero boss-specific timers or warnings.
- The one checked upstream module illustrates the pattern: `SetEncounterID`, `SetZone`, `RegisterCombat("combat")`, and `EnableGenericTrash()`; its creature-ID line is commented. The current upstream scripts contain no ability spell IDs or boss timer schedules.
- This is stronger than the earlier r264/r270 module-count-only audit, but it still says nothing about whether generic trash alerts fire correctly in live Forever combat.
- `DreadwatchPTR` 0.2.0-ptr is installed. It is a conservative diagnostics addon, not a functional boss-mod core. It intentionally does not register speculative encounter events or store raw combat payloads. Presence of this folder is not live-test evidence.
- The current build changed from the earlier 70707 scan to 70755. All old client-derived metadata remains tied to 70707 unless re-extracted and labeled for 70755.

### Dreadwatch repository

The public `uncle-bone/Dreadwatch` main branch contains the PTR diagnostic addon and research documents, but no functional encounter engine, boss modules, warning/timer implementation, release, or gameplay-verified encounter data. Its current research correctly treats namespace availability and prior open-world probe results separately from dungeon encounter verification.

Latest inspected repository commit: [dff1336](https://github.com/uncle-bone/Dreadwatch/commit/dff13365b188f73471e42eb2a5e87c9c4e222422), “Document v0.2.0 capability lab and deferred dungeon tests.” The most recent Dreadwatch source addition is [c3e186b](https://github.com/uncle-bone/Dreadwatch/commit/c3e186b995d8059de7456f56f755168076f9be7c).

### Current DBM source and history

Inspected [DeadlyBossMods/DBM-Dungeons](https://github.com/DeadlyBossMods/DBM-Dungeons/tree/master/DBM-Party-Forever), current `master` (head commit [f143f5d8](https://github.com/DeadlyBossMods/DBM-Dungeons/commit/f143f5d8)). The current branch still has the same 24 Forever boss scripts and no active boss-specific spell handlers, timers, or warnings. The latest published pack is [DBM-Dungeons 270](https://github.com/DeadlyBossMods/DBM-Dungeons/releases/tag/270), published 2026-11-03. Its release notes describe a bug fix and pack-icon/Forever WorldEvents fixes, not new Forever boss mechanics.

Relevant history:
- [483b43b4](https://github.com/DeadlyBossMods/DBM-Dungeons/commit/483b43b4): September 17 Forever preparation added the current registration-only module set among a larger change.
- [r264](https://github.com/DeadlyBossMods/DBM-Dungeons/releases/tag/r264): September 20 TOC refactoring and Forever-specific load filtering.
- [r268](https://github.com/DeadlyBossMods/DBM-Dungeons/releases/tag/r268): October 19 enabled DBM generic-trash support for Forever bosses. This is shared framework behavior, not evidence of per-boss timers.
- [r269](https://github.com/DeadlyBossMods/DBM-Dungeons/releases/tag/r269): October 26 included general changes and a Headless Horseman localization entry; localization alone is not a Horseman mechanic.
- [270](https://github.com/DeadlyBossMods/DBM-Dungeons/releases/tag/270): November 3, no custom-dungeon boss mechanic additions in the notes.

The local install and current upstream both report version 270. They were compared structurally; this note does not claim byte-for-byte equivalence.

### BigWigs, LittleWigs, and aura sources

- Inspected current [BigWigs](https://github.com/BigWigsMods/BigWigs) and [LittleWigs](https://github.com/BigWigsMods/LittleWigs) default-branch trees. BigWigs is a general boss-mod core; the current tree has no Forever-specific dungeon or raid encounter modules. LittleWigs has no Forever dungeon module set in its current tree. Core client compatibility must not be counted as encounter coverage.
- Inspected [ForeverAuras](https://github.com/neroxrw/ForeverAuras), its public source tree, and the installed local component version 1.1.0. The source is an aura engine/platform; this scan did not establish a matching public or installed boss-mechanics pack with verified Forever dungeon schedules.
- Forever Addon Kit and forever-addons were checked as API/probe references. They can support addon compatibility research but do not supply verified encounter timings in the files reviewed.
- Public beta guides and dungeon articles were found for the four test dungeons, including [Wowhead’s Ruins of Lordaeron walkthrough](https://www.wowhead.com/ptr/news/the-ruins-of-lordaeron-new-dungeon-walkthrough-for-wow-forever-383021). These support encounter discovery and contextual follow-up, not exact spell IDs or repeat timers.

## Coverage and evidence

| Evidence item | Count/status |
|---|---:|
| Forever-specific DBM boss scripts in current pack | 24 |
| Custom dungeons represented | 4 |
| Active boss-specific spell/event handlers in those scripts | 0 |
| Boss-specific timer/warning declarations in those scripts | 0 |
| Active creature-ID declarations in those scripts | 0 |
| Live-verified custom dungeon mechanics from this pass | 0 |
| Dreadwatch functional boss modules found | 0 |
| LittleWigs Forever-specific dungeon modules in current tree | 0 |

The counts above describe inspected code, not total Forever encounters or game content. Classic DBM modules, DBM world-event modules, and generic trash facilities may contain reusable behavior, but their mechanics must be checked against Forever before labeling them verified.

## Identity conflicts to preserve

Do not silently normalize the known catalog aliases: encounter 3301 ManaElemental / Arcanic Enigma; 3495 Infurnus / Magmatus; 3355 TheButcher / The Baron; and 2742 Sneed / Sneed's Shredder. The audit does not resolve these names.

## Still unresolved

1. Re-scan the post-update client catalog and addon tree under build 70755 before reusing any build-70707 data as current.
2. Obtain permitted, timestamped observations from actual Forever dungeon/raid pulls and validate encounter start/end, spell visibility, phases, and timing.
3. Verify whether DBM's generic trash implementation produces meaningful and safe warnings in build 70755.
4. Inspect DBM-Vanilla and DBM-WorldEvents per encounter before reusing Classic or holiday mechanics.
5. Verify DreadwatchPTR 0.2.0 in the current client; namespace existence is not proof of callable APIs, readable payloads, or encounter support.
6. Search or obtain actual public aura exports and other boss-tip packages, then cite their exact revisions and separate source-derived claims from live observations.

## Source links

- [DBM Forever module directory](https://github.com/DeadlyBossMods/DBM-Dungeons/tree/master/DBM-Party-Forever)
- [DBM-Dungeons latest release 270](https://github.com/DeadlyBossMods/DBM-Dungeons/releases/tag/270)
- [Dreadwatch](https://github.com/uncle-bone/Dreadwatch)
- [FWoW-Research](https://github.com/uncle-bone/FWoW-Research)
- [BigWigs](https://github.com/BigWigsMods/BigWigs)
- [LittleWigs](https://github.com/BigWigsMods/LittleWigs)
- [ForeverAuras](https://github.com/neroxrw/ForeverAuras)
- [Forever Addon Kit](https://github.com/Thunderz96/forever-addon-kit)
- [Forever Addon probes and examples](https://github.com/mparke/forever-addons)

