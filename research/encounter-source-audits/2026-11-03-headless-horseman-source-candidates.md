# Holiday module candidate audit: Headless Horseman

Collected: 2026-11-03.  
Local client: Warcraft Forever `1.60.1.70755`, flavor `wowf`, interface `16001`.  
Evidence labels below refer to source inspection only; no Horseman encounter was run.

## Local installation result

The local client contains `DBM-WorldEvents/Holidays/HeadlessHorseman.lua`. Its TOC [does not list interface 16001](https://github.com/DeadlyBossMods/DBM-Dungeons/blob/master/DBM-WorldEvents/DBM-WorldEvents.toc) and its allowed game types are `standard, classic`. Therefore the installed WorldEvents package does not declare itself loadable for the current Forever interface/build. File presence in AddOns is not live support.

The current upstream file is [HeadlessHorseman.lua](https://github.com/DeadlyBossMods/DBM-Dungeons/blob/master/DBM-WorldEvents/Holidays/HeadlessHorseman.lua); its local installed copy contains the same legacy and modern branches examined here. Do not copy the candidate values into Dreadwatch as verified Forever mechanics.

## Modern Retail branch: source-only candidates

At lines 6–16, the `IsRetail()` branch registers zone 1004, creature 207438, encounter 2725, combat registration, and gossip handling. The boss spell event registrations at lines 18–23 are commented out. The warning declarations and timer definitions at lines 26–36 are also commented out. The associated handler logic below remains commented.

Candidate spell IDs in that commented rework branch:

| Spell ID | Source label | Source value | Evidence status |
|---:|---|---|---|
| 415262 | Insidious Cackle | Commented timer baseline 41.4 s; commented sequence values 35.3, 54.6, 46.0, 46.2 | Historical/source-only; not Forever-verified |
| 423626 | Hot Head | Commented timer baseline 49 s; sequence values 61.9, 70.4; combat-start code proposes first 62 s | Historical/source-only; not Forever-verified |
| 414844 | Pumpkin Breath | Commented timer baseline 41.4 s; sequence values 6.1, 41.3, 54.6, 55.8; combat-start code proposes first 6 s | Historical/source-only; not Forever-verified |
| 415047 | Vine March | Commented timer baseline 41.4 s; sequence values 20.6, 42.5, 42.5, 54.6; combat-start code proposes first 20 s | Historical/source-only; not Forever-verified |
| 423623 | Hot Head aura | Commented aura warning | Historical/source-only; not Forever-verified |
| 415329 | Pumpkin Breath damage/miss | Commented GTFO warning | Historical/source-only; not Forever-verified |

The file itself includes alternative timing comments and uncertainty around some observed intervals. These values are deliberately preserved as candidates, not merged into a single exact schedule.

## Classic branch: historical implementation

The `else` branch is explicitly labeled “OG fight, for classic” (line 131). It uses zone 189 and creatures 23682/23775 (lines 132–133). It actively registers aura events and has target warnings/timers for 42380 (Conflagration; 4 s target timer) and 42514 (Squash Soul; 15 s target timer), plus body-stage command IDs 42410, 42547, 42548, and 42549. This is a historical Classic implementation, not evidence that Forever uses the same version or timings.

## Practical use for Dreadwatch

- The module’s old fight offers potential comparison material for mechanic naming and event-trigger design.
- The newer branch’s IDs and timing arrays are source artifacts only; they are commented out and the package TOC excludes interface 16001.
- The current r269 release notes mention a Headless Horseman localization change, not an implementation change. Localization is not evidence of a new encounter mechanic.
- Before adapting any of these, verify the current Forever Horseman NPC, zone/map, encounter registration, spell IDs, and ability schedule against build-matched client data or permitted live observation.
