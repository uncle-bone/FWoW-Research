# WoW Forever local research scan

Scan date: 2026-11-03 (America/Los_Angeles)
Client: `C:\Program Files (x86)\World of Warcraft\_forever_`; flavor marker is `wowf`; executable and build metadata report version `1.60.1.70707`, meeting the repository required Forever build floor.

## What this installation contains

- `Interface\AddOns\DBM-Party-Forever`: custom Forever DBM package with 24 boss modules. The modules register an encounter ID, zone ID, and generic `combat` trigger, but the inspected modules contain no active creature-ID registration, spell-event handlers, ability timers, or warnings. Treat them as registration shells, not ready timers.
- `Interface\AddOns\NaowhForever_DungeonJournal\Data\Dungeons`: 35 readable dungeon/raid reference Lua files. Extracted boss name, NPC ID (where listed), encounter ID (where listed), and entrance map IDs to `dungeon-boss-catalog.json`. This is addon-authored catalog data, not proof the live server spawns every listed NPC or uses the stock encounter mechanics.
- `Interface\AddOns\ForeverDungeonJournal\Data\Dungeons.lua` and `Data\Bosses.lua`: custom Forever instance quests, boss names, some custom NPC IDs, loot, level bands, routes and map pins. Example: Hall of Thanes contains custom NPC IDs 261306, 261311, 261319 and comments an alias between Magmatus and the client encounter label Infurnus. It does not provide boss ability schedules.
- `Interface\AddOns\AtlasLootClassic_DungeonsAndRaids\forever.lua`: separate Forever dungeons and raids loot catalog; custom entries include Hall of Thanes and Ruins of Lordaeron. The file itself labels its custom loot section as incomplete.
- `Interface\AddOns\DBM-Raids-Vanilla`: 120 Lua files of stock Vanilla DBM raid references. Useful as a mechanic/timer candidate source only; not verification of WoW Forever tuning.
- `Interface\AddOns\DBM-WorldEvents\Holidays`: DBM holiday-boss references including Headless Horseman, Ahune, Apothecary Trio, Coren Direbrew, Greench and Omen. Treat as stock baseline until server-specific behavior is observed.
- `Interface\AddOns\ForeverQuest`: quest/map/NPC/item reference database (including `source\classicQuestDB.lua`, `classicNpcDB.lua`, `classicObjectDB.lua`, and `classicItemDB.lua`); `Questie` is also installed. These are useful starting points for quest and objective cross-referencing.
- `ForeverDungeonJournal`, `NaowhForever_DungeonJournal`, AtlasLoot, Questie and the installed `NaowhForever_*Data` packages also provide route, quest, loot, entrance, journey, discovery and map references.

## Extracted counts

- Journal files: 35.
- Named NPC/catalog rows extracted from the 35 journal files: 311 (not all rows are confirmed bosses; some are objects, trash, or entries without IDs).
- Rows with explicit NPC IDs: 279.
- Rows with explicit encounter IDs: 201.
- Custom Forever DBM modules with encounter IDs: 24.
- Timestamped combat logs found: 0. Eight `Blizzard_CombatLog.lua`/`.bak` files are settings files under SavedVariables, not event logs; their contents were not read.
- Spell IDs, cast timing candidates, phase transitions and warnings from the custom DBM Forever modules: 0 extracted; the modules are shells.

The entrance map ID is an addon UI map pin, not necessarily an instance map ID. Difficulty coverage (Normal/Heroic/Mythic/Mythic+) was not verified from these catalogs. No cast schedules or mechanics are inferred from the journal roster.

## Local log evidence

The client `Logs` directory has telemetry files such as `Hotfix.log` and `QuestCache.log`, not a `WoWCombatLog.txt` timestamped encounter log. WTF combat-log SavedVariables are preferences, not event records; they were not read. No actual combat-log observations are included in this package.

## Recommended research use

1. Import the roster JSON as `addon-catalog` evidence and preserve each original absolute source path.
2. Reconcile the NPC/encounter entries against WoW Forever server scripts and in-game GUID observations.
3. Use stock DBM and DBM-WorldEvents only as candidate behavior references; mark them `stock-db-derived` until confirmed on WoW Forever.
4. Collect timestamped combat logs at each supported difficulty before adding first-cast or repeat timers.
5. Check licensing and attribution before redistributing third-party addon data or source files. This bundle contains extracted index records and audit notes, not copies of the installed addon folders.

## Bundle files

- `dungeon-boss-catalog.json`: journal NPC/encounter catalog extract with source paths, source hashes, confidence and build metadata.
- `dbm-forever-module-audit.json`: the installed Forever DBM module registration audit.



## Relevant addon inventory

| Installed addon | Files / Lua files | Data value |
|---|---:|---|
| `DBM-Party-Forever` | 36 / 35 | 24 custom encounter registration modules; currently no active spell/timer mechanics |
| `NaowhForever_DungeonJournal` | 204 / 140 | Broad classic and Forever instance catalog, NPC/encounter IDs, items, zones and entrance pins |
| `ForeverDungeonJournal` | 138 / 54 | Forever custom instance quest chains, boss aliases, quest rewards, routes and map pins |
| `ForeverQuest` | 37 / 26 | Classic quest, NPC, object, item and area/map references |
| `Questie` | 512 / 342 | Broad quest/NPC/object reference and corrections |
| `AtlasLootClassic_DungeonsAndRaids` | 18 / 15 | Loot catalog, including a Forever-specific `forever.lua` file |
| `DBM-Raids-Vanilla` | 135 / 120 | Stock Vanilla DBM mechanic references, not Forever verification |
| `DBM-WorldEvents` | 41 / 40 | Stock holiday and world-boss references, including Headless Horseman |

The full `Interface` tree contains 23,810 files (~1.4 GB). The scan inventoried the full tree, then content-audited the focused addon/data sources above; it did not copy the tree or expand CASC archives.

## FWoW-Research repository alignment

The connected repository README says this is a source-discovery/documentation-stage project and that no full client had yet been scanned. This local scan verifies an installed `wowf` client at build `1.60.1.70707`, above the README's stated Forever build threshold. This source-attributed scan report and factual metadata are being added to the repository; no client assets are included.

