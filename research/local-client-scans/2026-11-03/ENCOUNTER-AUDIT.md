# DBM-Forever encounter cross-reference — 2026-11-03

Source: [Naowh catalog](dungeon-catalog.json) and [installed DBM audit](dbm-forever-module-audit.json), client `1.60.1.70707`. Full machine-readable results: [encounter-cross-reference.json](encounter-cross-reference.json).

## Findings

- 35 catalog instance files, 311 catalog rows, 201 rows with encounter IDs.
- 216 encounter-ID assignments, 215 distinct IDs. This explains why row counts, assignments and distinct IDs differ.
- **24/24 DBM modules matched** by exact encounter ID; 191 catalog IDs have no corresponding module in the 24-module DBM-Forever scan.
- 1 repeated encounter ID in catalog: 2742 (Sneed's Shredder / Sneed).
- These are **static cross-source matches**, not live confirmations. None of the 24 DBM modules supplies working ability timers/warnings.

## Matches and aliases

| Encounter ID | DBM module | Catalog boss | Catalog NPC ID | Instance | Name differs |
|---:|---|---|---:|---|---|
| 3298 | ArcaneAnomaly | Arcane Anomaly | 245999 | City of Dalaran | No |
| 3311 | AtrexistheGraveKnight | Atrexis the Grave Knight | 247126 | City of Dalaran | No |
| 3299 | FelAncient | Fel Ancient | 246003 | City of Dalaran | No |
| 3310 | LyntheIgnored | Lyn the Ignored | 247032 | City of Dalaran | No |
| 3300 | ManaDevourer | Mana Devourer | 246008 | City of Dalaran | No |
| 3301 | ManaElemental | Arcanic Enigma | 246016 | City of Dalaran | Yes |
| 3312 | ManaWraith | Mana Wraith | 246931 | City of Dalaran | No |
| 3303 | ShadeoftheArchmage | Shade of the Archmage | 246020 | City of Dalaran | No |
| 3302 | UnstableSentinel | Unstable Sentinel | 246017 | City of Dalaran | No |
| 3644 | HighlandHorror | Highland Horror | 260808 | Excavation Site: Wetlands | No |
| 3482 | RelicGuardian | Relic Guardian | 260326 | Excavation Site: Wetlands | No |
| 3480 | Saltspine | Saltspine | 260322 | Excavation Site: Wetlands | No |
| 3481 | Shadetooth | Shadetooth | 260325 | Excavation Site: Wetlands | No |
| 3496 | DurgenDirgehammer | Durgen Dirgehammer | 261319 | The Hall of Thanes | No |
| 3493 | FaldrimAnvilmar | Faldrim Anvilmar | 261306 | The Hall of Thanes | No |
| 3495 | Infurnus | Magmatus | 261316 | The Hall of Thanes | Yes |
| 3494 | Plunder | Plunder | 261311 | The Hall of Thanes | No |
| 3412 | Bjork | Bjork | 256097 | Ruins of Lordaeron | No |
| 3408 | LordaeronCaptain | Lordaeron Captain | 255699 | Ruins of Lordaeron | No |
| 3354 | Rathmael | Rath'mael | 250657 | Ruins of Lordaeron | No |
| 3357 | TheAbandoned | The Abandoned | 250631 | Ruins of Lordaeron | No |
| 3355 | TheButcher | The Baron | 250660 | Ruins of Lordaeron | Yes |
| 3411 | ViktortheVile | Viktor the Vile | 256035 | Ruins of Lordaeron | No |
| 3353 | Witherfang | Witherfang | 250483 | Ruins of Lordaeron | No |

**Priority alias investigations:** `ManaElemental` ↔ `Arcanic Enigma` (3301), `Infurnus` ↔ `Magmatus` (3495), `TheButcher` ↔ `The Baron` (3355). Names are kept exactly as supplied by each source. Other punctuation/spacing differences are shown in JSON for review.

## Next implementation work

1. Build a read-only in-game 70707 encounter probe: record encounter start/end, available timeline/events metadata, zone/instance identifiers and safe observable spell IDs; avoid secret-value operations and restricted combat logging.
2. Validate alias and NPC-ID relationships during real encounters; do not activate creature-ID triggers solely from addon catalog entries.
3. Resolve Deadmines ID 2742 shared by Sneed and Sneed's Shredder using encounter observations or reliable encounter metadata.
4. Gather observed ability IDs, triggers, timings and phase boundaries for the 24 shells before creating functional timers/warnings.
5. Expand coverage to catalog encounter IDs not present in DBM-Forever, prioritizing accessible instances; keep closed instances explicitly unavailable.
6. Reconcile ForeverDungeonJournal, Questie/ForeverQuest and AtlasLoot records as separately attributed candidates, not independent live verification.

## Provenance and caveats

Every match in the JSON retains module source file, line, SHA-256, catalog source file, line and SHA-256. The scan is **static-addon-source-extraction**. No timestamped gameplay combat logs were provided. Closed instances and journal map pins must not be treated as validated encounter/instance identifiers. No original source JSON was modified by this audit.
