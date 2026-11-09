# WoW Forever: Camping and Merchant's Favor — offline research reference

Collection date: 2026-11-09  
Sources:
- https://www.wow-professions.com/forever/camping-guide
- https://www.wow-professions.com/forever/merchants-favor-durotar-supply-azeroth-commerce

Provenance: Independent factual summary of third-party guides. Source material is © WoW-Professions.com. Not a verbatim copy or replacement for its maps, article text, or full tables. Website statements are editorial/beta-derived and are not live-confirmed by this research.

## Camping system

A player places a campfire. Nearby players can each contribute one profession camp item, then sit beside the fire for about a minute. The camp grants a combined Camp Benefits effect for one hour. Each participant's camp items share a one-hour cooldown after use. Camp sizes accept 3, 5, or 10 contributed items. The guide says these camp buffs do not stack with the corresponding class buffs.

The two starting-zone tutorial quests, The Great Outdoors and Camping 101, are optional for access to the benefits. Fires from those quest givers grant the Camp Tent rested-experience benefit.

### Campfire kits

| Kit | Learn skill | Use skill | Capacity | Recipe / acquisition |
|---|---:|---:|---:|---|
| Basic | 1 | 1 | 3 | Cooking trainer provides it; craft from Simple Wood |
| Journeyman | 90 | 140 | 5 | Blueprint; Star Wood |
| Expert | 200 | 220 | 10 | Blueprint; Thick Logs |

The guide identifies Lord Serpentis in Wailing Caverns as the Journeyman blueprint source. It says the Expert blueprint drop location was not known when the page was written. Confirm current drop sources in-game.

### Profession camp items

The article describes tier unlocks at profession skill 20, 140, and 300. The first tier is learned from the profession trainer or Camping 101; tier 2 and 3 require blueprint items. Tier 2 blueprints are described as dungeon-boss drops. The source's tier 3 blueprint sources were not all known. Each camp item also provides its profession's tier 1 buff; higher-tier objects add profession stations or utility. Cooking is the exception: its first shared item is the campfire, and the article lists two Cooking camp objects.

| Profession | Tier 1 contribution | Tier 2 utility | Tier 3 utility |
|---|---|---|---|
| Alchemy | Mana regeneration | Fermenter station | Alchemy laboratory |
| Blacksmithing | Strength bonus | Anvil | Master Forge |
| Enchanting | Armor, attributes and resistances | Improved disenchanting station | Arcane Forge |
| Engineering | Reagent vendor bot | Repair bot | Higher-tier engineering camp utility |
| Leatherworking | Rested experience | Tanning station | Sewing station |
| Tailoring | Faction-aligned spirit bonus | Spinning station | Loom |
| Herbalism | Intellect bonus | Greenhouse grows planted seeds | Seed processing/multiplication station |
| Mining | Melee attack-power bonus | Slowly generates a common ore node | Molten Foundry for a specialized smelt |
| Skinning | Critical-strike bonus | Field Guide can teach Track Beasts | Trap workbench with a trap |
| Cooking | Campfire serves as the profession's first camp object | Shared stamina-food feast | Advanced oven |
| First Aid | Stamina bonus | Station for healing potions and anti-venom | Further station for healing potions and poultices |
| Fishing | All-attributes bonus | Fishing station supplies uncommon fish and lures | Fishing station supplies rare fish and lures |

Buff conflict examples called out by the article: mana recovery versus Blessing of Wisdom; Strength versus Strength of Earth; broad defensive stats versus Mark of the Wild; spirit versus Divine Spirit; intellect versus Arcane Intellect; attack power versus Blessing of Might; skinning crit versus Moonkin Aura; and all stats versus Blessing of Kings. The camp buff is described as replacing/combining the profession contributions, not stacking with the matching class buff.

Camp stations matter during crafting: they enable recipes that require the station object. This means a guide tracker should expose station prerequisites separately from recipe materials and profession skill.

## Merchant's Favor and faction commerce camps

Merchant's Favor is a character-bound currency. The source describes two faction camps, with the same recipe inventory:
- Horde: Durotar Supply and Logistics, in The Barrens just west of the Crossroads gate.
- Alliance: Azeroth Commerce Authority, at Three Corners on the west side of Redridge Mountains.

The camps have vendors for crafting professions and Cooking. Recipes may require both currency and camp reputation.

### Currency progression

Waylaid Crates appear randomly in the open world and may also be purchased from the Auction House. A crate specifies a material category and accepted bundle(s). Filling and sealing it, then turning it in at the matching faction camp, grants Merchant's Favor. The guide says crate turn-ins do not themselves grant reputation.

The article gives examples of Apprentice crates: cloth/leather, ore, herbs, enchanting materials, cured hides and cloth bolts, ingots, and engineering components. Example accepted bundles include Linen Cloth or Light Leather, Copper or Tin Ore, common low-level herbs, and Copper/Tin/Bronze Bars. Rewards vary by crate tier; its examples show 5 Favor for entry crates and 10 for some higher crate types. A character-level gate applies to later crate tiers.

### Reputation progression

Reputation comes from Craftsman's Writs: an order asks for an item, which can be crafted or bought, then delivered to a marked customer. The guide gives rank rewards of 75 reputation for Journeyman, 125 for Expert, and 200 for Artisan. Each individual writ can be completed once per day; different writs can be completed on the same day. Writs grant reputation and a coin pouch, not Merchant's Favor.

The first crate-fill or writ-start event also provides a Shipping Label quest. Turning it in at the character's camp is listed as granting 2,000 reputation and 50 Favor.

Once Friendly is reached, the camp unlocks an Uncertified Scribe. The guide describes two additional reputation utilities: a receipt that converts an empty Waylaid Crate into reputation, and a quill that rerolls a Craftsman's Writ into another writ of its rank. Its source table lists the receipt at Friendly and the quill at Honored; verify current costs and behavior on the live client.

### Rewards and vendor inventory

The source page groups camp recipes by profession and lists recipe level requirement, required profession skill, Favor price, and reputation gate. Reward categories include:
- Crafting recipes across the listed professions, including stat/role equipment and utility items.
- Alchemy consumables.
- Engineering gadgets and devices.
- Cooking recipes.
- A mount, pet, tabard and titles at higher progression.

The inventory is large and subject to site updates. This summary records the system and table fields, not every recipe row. Refer to the linked original for the full current vendor catalog until each recipe row is independently extracted and matched to Forever client data.

## Data and implementation notes

For an addon or normalized research dataset, keep these separate:
1. Campfire size, required skill, blueprint, material and item capacity.
2. Profession camp contribution, buff/exclusion rules, station function and required profession skill.
3. Waylaid Crate category, accepted bundles, character-level gate and Favor payout.
4. Craftsman's Writ rank, reputation payout, daily repeat limit, delivery behavior and coin reward.
5. Vendor recipe name, profession, skill threshold, character-level threshold, Favor price, reputation gate, faction/vendor, and source evidence.

Do not infer missing blueprint drops, item IDs, NPC IDs, coordinates, or live values from the guide alone. Preserve its unknown/unverified statuses and validate against the target Forever build.

## Remaining completeness work

This independent reference captures the gameplay model and broad camp-item roles, but it is not a full reproduction of every source table, recipe row, material quantity, route map, screenshot, or article paragraph. Full verbatim reproduction is not included. The original pages remain the authority for their complete current articles. For a true data-complete research catalog, independently transcribe factual rows, attach source section and collection date, and cross-check all records against the Forever client or permitted community data.
