# WoW Forever professions — source-indexed research
Research date: 2026-11-07
Source: https://www.wow-professions.com/forever
Status: PUBLIC GUIDE REVIEWED, NOT LIVE VERIFIED. Independent research notes and link index, **not a copy of the website**.

## Coverage and source URLs
The source's Forever landing page lists thirteen 1–300 leveling guides and two supplemental systems guides (15 pages). The author warns that the guides originated in beta and some upper skill ranges have not been verified on live servers.

| Topic | Original page | Research coverage |
|---|---|---|
| Alchemy | https://www.wow-professions.com/forever/alchemy-leveling-guide | Shopping lists, potion/elixir recipes, trainer ranks, Merchant's Favor recipes; 290–300 provisional. |
| Blacksmithing | https://www.wow-professions.com/forever/blacksmithing-leveling-guide | Ore/bar material planning, trainer progression and forging skill ranges. |
| Enchanting | https://www.wow-professions.com/forever/enchanting-leveling-guide | Disenchanting materials, enchant progression, trainer locations. |
| Engineering | https://www.wow-professions.com/forever/engineering-leveling-guide | Parts/components, recipes, trainer ranks and specialization-relevant steps. |
| Leatherworking | https://www.wow-professions.com/forever/leatherworking-leveling-guide | Leather/hide materials, craft progression and trainer ranks. |
| Tailoring | https://www.wow-professions.com/forever/tailoring-leveling-guide | Cloth materials, crafting progression, trainers. |
| Mining | https://www.wow-professions.com/forever/mining-leveling-guide | Ore gathering, route guidance, smelting and trainer progression. |
| Herbalism | https://www.wow-professions.com/forever/herbalism-leveling-guide | Herb gathering routes, level requirements and trainers. |
| Skinning | https://www.wow-professions.com/forever/skinning-leveling-guide | Mob skinning progression, locations and trainers. |
| First Aid | https://www.wow-professions.com/forever/first-aid-leveling-guide | Bandages and Forever-specific potion changes, trainer progression. |
| Fishing + Cooking | https://www.wow-professions.com/forever/fishing-and-cooking-leveling-guide | Combined skill progression and fish-to-food dependencies. |
| Cooking | https://www.wow-professions.com/forever/cooking-leveling-guide | Food recipes, materials, trainers and skill thresholds. |
| Fishing | https://www.wow-professions.com/forever/fishing-leveling-guide | Fishing skill progression, trainer locations and catch guidance. |
| Camping | https://www.wow-professions.com/forever/camping-guide | Forever-specific profession bonuses and buffs. |
| Merchant's Favor | https://www.wow-professions.com/forever/merchants-favor-durotar-supply-azeroth-commerce | Durotar Supply and Logistics / Azeroth Commerce Authority reputation, supply turn-ins and recipe unlocks. |

## Key Forever-specific findings
- Guides target profession skills 1–300 and provide trainer locations, material shopping lists, level/skill gates, and recommended crafting or gathering routes. These are third-party recommendations, not game-server constants.
- **Alchemy:** Source recommends Herbalism pairing. It says Apprentice Alchemy can be learned on a fresh character, Journeyman requires level 10/skill 50, Expert level 20/skill 125, and Artisan level 35/skill 200. The 225+ Alchemy section is explicitly described as not yet live tested, with the final 290–300 route undecided.
- **Alchemy source-specific NPC examples:** Horde capital trainers Whuut (Orgrimmar), Doctor Martin Felben (Undercity), Kray (Thunder Bluff); Alliance capital trainers Tel'Athir (Stormwind), Vosur Brakthel (Ironforge), Milla Fairancora (Darnassus). The guide also identifies Skyborne trainers Iaadaria Bitterwind, Valiena Swiftgale, and Nyassa Swiftdraught on Zephras Isle.
- **Alchemy 225+:** Artisan trainer examples Rogvar (Stonard) and Kylanna Windwhisper (Feathermoon Stronghold). Source notes that some healing potions moved to First Aid in Forever, so copying Classic Alchemy routes directly is unsafe.
- **Merchant's Favor:** The Alchemy page identifies faction-specific recipe vendors Apothecary Durelle (Durotar Supply and Logistics near Crossroads) and Nina Surefire (Azeroth Commerce Authority at Three Corners, Redridge). Research this as a profession/reputation system rather than a generic trainer.
- **Camping:** The source has a standalone Forever-specific profession bonus/buff guide; cross-reference profession interactions and durations with live client evidence.
- **Gathering:** Mining, Herbalism and Skinning have separate leveling guides; routes and node distributions should be revalidated against live build and phase rather than treated as fixed spawns.
- **Fishing + Cooking:** A combined guide exists as well as independent Fishing and Cooking guides; compare their progression dependencies before merging records.

## Proposed normalized research tables
Do not copy prose, full guide text, or proprietary shopping lists wholesale. Create independently validated factual records with these fields:
- `profession`, `skill_min`, `skill_max`, `recipe_or_node_name`, `spell_id`, `item_id`, `npc_id`, `map_id`, `faction`, `required_character_level`, `required_skill`
- `materials` as structured item IDs and quantities, `trainer_name`, `trainer_coordinates`, `vendor_requirements`, `reputation_requirement`
- `source_url`, `source_section`, `observed_build`, `collected_at`, `evidence_tier`, `confidence`, `verification_notes`.
- Do not invent IDs/coordinates or treat editorial shopping estimates as deterministic craft counts.

## Verification and rights
The source's content is © 2026 WoW-Professions.com. This repository links to the original pages and summarizes original findings; it does not mirror or reproduce their complete authored guides. This protects provenance and keeps readers directed to current versions. No automated bulk scraping or live-client validation was performed. Some page-specific statements are beta-based and provisional.

## Next steps
1. Audit trainer pages linked from individual profession guides and extract independently verifiable NPC IDs and map IDs.
2. Cross-reference recipe/item names against current Forever client DB2 and public item databases; record IDs only when verified.
3. Verify 225–300 skill routes on live game, particularly moved Alchemy/First Aid recipes.
4. Reconcile profession reputation vendors, Merchant's Favor rewards, and Camping buffs.
5. Compare source revision dates to client build, flag stale beta instructions and differences in live profession rules.
