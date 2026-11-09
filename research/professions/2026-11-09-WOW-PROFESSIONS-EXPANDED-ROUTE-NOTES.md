# WoW Forever profession routes — expanded offline notes

Collected 2026-11-09 from the linked Forever guide pages. These are independent notes for addon implementation, not verbatim article copies. The source author states these guides are based on the Forever beta and that some high-skill routes await live testing. Material totals are estimates where recipes turn yellow.

For the complete page inventory, section map, and initial extraction, see [the detailed source archive](2026-11-09-FOREVER-PROFESSIONS-DETAILED-SOURCE-ARCHIVE.md). This supplement records useful details for the guides that previously had section-level notes only. Each page's original text and diagrams remain at the linked URL.

## Engineering

Source: https://www.wow-professions.com/forever/engineering-leveling-guide

- The route is split into Apprentice 1–50, Journeyman 50–150, Expert 150–200, specialization, and Artisan 200–300. Level 35 is required to train above 225; the shopping list is divided accordingly.
- The guide recommends pairing Engineering with Mining because bars and stone dominate its inputs.
- It says the Forever Gnome racial changes to a 20% reduction in device failure/backfire chance rather than the Classic +15 profession skill, so the leveling route is not discounted for Gnomes.
- Carry-forward components are essential: retain early Rough Blasting Powder and Copper Bolts for later bombs; retain the Arclight Spanner for subsequent crafting; retain Coarse Blasting Powder for dynamite.
- The 51–75 bomb section can cross the Journeyman cap depending on skill-up luck; train first or craft while monitoring skill. The guide warns some yellow crafts fail to award a point.
- It compares Silver Contact against a leather/gem alternative when Silver is expensive.
- Starting-zone vendor access can differ; notably, the guide calls out Blacksmith Hammer acquisition in Dun Morogh and on Zephras Isle.

## Leatherworking

Source: https://www.wow-professions.com/forever/leatherworking-leveling-guide

- The route spans Apprentice 1–55, Journeyman 55–130, Expert 130–210, specialization, and Artisan 210–300; the guide splits preparation at character level 35 for the post-225 route.
- Skinning is the recommended pairing because hides and leather account for much of the expense.
- The first bracket branches based on whether the player has scraps, Light Leather, or Light Hides. The selected material path changes both the recipe and what must be reserved.
- Carry-forward notes include retaining cured hides for later leather armor and tracking whether the hide-based alternative already covered a later skill range. The guide also points out that many trade supplies are sold near trainers, with exceptions in Elwynn and Tirisfal.
- Journeyman requires level 10 and 50 profession skill. Some mid-route choices branch between cured Medium Hides and Fine Leather Belts based on whether hides or leather were bought.
- Since alternatives replace a whole shopping-list row, do not add both branches together in the addon shopping list.
- The source has specialization content between Expert and Artisan; specialization requirements and quest steps need to be represented as a distinct decision branch, not ordinary recipe crafts.

## Tailoring

Source: https://www.wow-professions.com/forever/tailoring-leveling-guide

- Skill sections: Apprentice 1–55, Journeyman 55–125, Expert 125–225, Artisan 225–300. Level 35 is required for the above-225 part; the source marks the 225–265 material plan as provisional and says the guide stops at 265 pending further live price testing.
- The route uses cloth bolts as intermediate items. The guide explicitly says to keep early Linen Bolts for belts, and Wool Bolts for later crafts; a tracker must treat these as produced inventory, not consumed permanently at the step where they are made.
- Before crafting the 55–80 bracket, learn Journeyman: yellow-skill variance may carry the character past 75 and further crafts cannot grant points above the learned cap.
- Most trainer areas have a nearby Tailoring Supply vendor. Tirisfal is an exception; the guide directs the player to obtain Coarse Thread in Brill.
- Starting-zone trainer coverage is incomplete in some zones; the page directs some races to capital-city trainers and lists two Skyborne trainers on Zephras Isle.
- If an addon builds an ordered shopping list, list cloth and thread once by total need, but show bolt production steps at the point they are used and preserve bolt carry-forward counts.

## Mining

Source: https://www.wow-professions.com/forever/mining-leveling-guide

- The guide includes trainer progression, Find Minerals setup, skill bonuses, smelting through 105, then ore/node routes through skill 300. Smelting and node collection should be separate step types.
- It says Find Minerals is learned with Mining but is not enabled automatically; the player must activate it from the Mining profession pane. Mining and Herbalism tracking cannot be active at once, according to the page.
- Skill route labels: Copper 1–65; Copper/Tin 65–125; Iron/Gold 125–175; Mithril 175–245; Mithril/Thorium 245–275; Thorium/Rich Thorium 275–300.
- Skyborne can learn Mining through the early Harvesting Windstones quest by choosing the Mining for Dummies reward; there is no trainer in the starting village. Island trainers are listed in Valanaar and Shen'dar Village.
- Some starting-zone trainers teach only through 75. The guide gives nearby upgrade trainers for later brackets.
- The source includes route maps and recommends tracking ore on the minimap; exact map paths should not be invented from textual zone names. Retain every source route option and separately validate it against the live map.

## Skinning

Source: https://www.wow-professions.com/forever/skinning-leveling-guide

- Skill sections: 1–75, 75–150, 150–225, 225–280, and 280–300. The guide lists both trainer progression and the required Skinning skill by target mob level.
- General rule given by the source: from mob level 20 onward, required Skinning is five times the mob level. For mobs below level 20, it provides a separate stepped threshold table.
- Several starting-zone trainers only train to 75; the guide names subsequent trainers or directs the player to a capital. A route should surface the trainer trip when the learned cap blocks further progress.
- Skyborne characters can learn Skinning through the early Harvesting Windstones quest by choosing Pelt Collecting for Beginners; island trainers are listed in Valanaar and Shen'dar Village.
- This is a gathering route based on eligible mob levels and zone progression, not a material shopping-list route. A tracker should check actual skill requirement and skin eligibility rather than infer the next step from broad ranges alone.

## First Aid

Source: https://www.wow-professions.com/forever/first-aid-leveling-guide

- The guide treats First Aid as available to every character without occupying a primary profession slot. It has Apprentice 1–75, Journeyman 75–150, Expert 150–225, and Artisan 225–300.
- Apprentice has no character-level requirement. The guide says each trainer also teaches Journeyman, so no separate Journeyman trainer trip is required at skill 50; Expert/Artisan progression still has level gates and trainer steps.
- Forever-specific distinction: the source says healing potions formerly associated with Alchemy are made under First Aid. The guide provides separate Bandages and Healing Potions recipe tabs, so the data model should allow both craft families.
- Material preparation branches between cloth and herbs. The page's early potion method is yellow before the endpoint, so quantities need a variance buffer; alternative shopping-list rows should not be summed.
- All starting zones and capitals have trainer coverage in the page, including Skyborne trainer locations. This profession should remain visible even when the two primary profession slots are full.

## Cooking

Source: https://www.wow-professions.com/forever/cooking-leveling-guide

- Cooking is a secondary profession that any character can learn. Sections: Apprentice 1–50, Journeyman 50–150, Expert 150–225, Artisan 225–300.
- The page offers multiple recipes per skill bracket because the best route depends on which meat or fish the character already has. A route engine should select among valid recipes based on inventory and price rather than hard-code one universal recipe.
- A campfire is required. The Basic Campfire Kit comes with Cooking; kits are crafted with Simple Wood and Flint and Tinder. Flint and Tinder is used to craft kits, not to place a fire. Check for nearby existing fires before directing the player to craft one.
- The guide lists trainer and supply-vendor locations, including Skyborne. It also states every Cooking trainer teaches Journeyman.
- For Fishing progression, it recommends the combined Fishing + Cooking guide so the caught fish also advances Cooking. Keep combined-route dependencies separate from the standalone Cooking choices.

## Fishing

Source: https://www.wow-professions.com/forever/fishing-leveling-guide

- Route sections: basic Fishing 1–75, 75–150, 150–225, the Artisan Fishing training step, and 225–300.
- The guide characterizes this as time-intensive and low-material: players need a pole and lures, but not a bulk craft shopping list.
- Apprentice has no character-level requirement; Journeyman requires level 10 and all trainers also teach Journeyman per the guide.
- It gives starting-zone trainers next to water, capital trainers, and separate lure/pole vendor locations. The guide includes Horde, Alliance, and Skyborne paths.
- The page directs players who also want Cooking to use the combined route, because the caught fish can be cooked for skill-ups.
- Fishing routes are zone-specific; keep alternatives (including faction and Skyborne routes) as alternatives instead of one forced location. Catches are probabilistic, so expected fish counts are planning estimates.

## Combined Fishing + Cooking route

Source: https://www.wow-professions.com/forever/fishing-and-cooking-leveling-guide

- This guide synchronizes two skill tracks. Its major checkpoints: Fishing to 75; Fishing 75–130 with Cooking 1–100; Fishing 130–205 with Cooking 100–175; Artisan Fishing quest; Fishing 205–255 while Cooking reaches 225; Artisan Cooking quest; Fishing to 300 in Feralas; then Cooking to 300.
- The first fishing segment contains faction/zone alternatives and vendor setup. The page says Mulgore is a compact Horde option; it also gives Durotar, Tirisfal, and Skyborne starts.
- Some early fish are explicitly saved for later Cooking crafts. Those must appear as reserved inventory and not as surplus or shopping-list demand.
- Artisan Fishing and Artisan Cooking are separate unlock checkpoints; the addon must not mark the combined route complete after only one profession reaches its bracket.
- When users already have different skill levels, resume each profession at its own next incomplete step, while preserving shared fish/material dependencies.

## Source-use and offline completeness

- Pages listed here were read for their visible article headings and selected detail. These notes are not an HTML/image mirror and do not duplicate full article text or every recipe table.
- Original maps/screenshots and complete current guide tables remain accessible at the source URLs in the main archive.
- For addon data, extract route facts into original structured records and retain source URL, source section, collection date, evidence tier, estimated flags, and any recipe alternatives. Cross-check against the Forever build before labeling live-confirmed.
