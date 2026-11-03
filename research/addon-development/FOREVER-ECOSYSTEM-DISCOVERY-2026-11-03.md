# WoW Forever addon/tool ecosystem discovery — 2026-11-03

## Scope and confidence
Searched CurseForge public WoW addon listings, including the Forever flavor filter (gameVersionTypeId=88568), project pages, and GitHub repository discovery using three queries. This is a **discovery inventory**, not a complete platform crawl or a claim that each addon was downloaded, inspected, installed or tested. Github queries returned up to 100 results per broad query (capped), with overlap and false positives; additional pages, code search and repo-by-repo source audits are still required. CurseForge search-indexed pages are not an exhaustive listing. The client launches 2026-11-04; functionality is mostly prelaunch/unverified.

## Highest-priority findings
- Official DBM-Core lists Forever flavor, as do Details!, Questie, Auctionator, RareScanner, TomTom, AtlasLoot Classic Forever, BugGrabber and RestedXP. **Flavor tag means published compatibility claim, not verified live support**.
- Official DBM Core 12.1.19 was listed as a Forever file on Nov 3; separate DBM-Forever modules still require actual boss mechanics testing.
- Questie had a Forever-flavored release dated Nov 2; don't assume unofficial Questie forks are required without checking current official version.
- ForeverPath includes client-extracted item/recipe data and a lazily loaded CMaNGOS classic DB; treat classic data as candidates for Forever.
- Terminal documents useful real-world constraints: combat can close restricted UI; profession data is read when the player opens the window; addon updates adding files require full restart; optional provider API documented in its GitHub source.
- Forever AIO, Naowh Forever, AtlasLoot Classic Forever, FojjiCore, Forever Leveling BiS and ForeverPath may contain complementary data about quests, loot, items, bosses, maps and trainer spells. Source availability and licenses vary.
- UI frameworks and multi-flavor addons (ElvUI-Forever, ShestakUI_Forever, NDui Classic, ItemRack-Universal) are useful examples for Camelot TOC and secure UI migration.
- BugGrabber and addon API-export projects are important for launch-day validation.

## CurseForge candidate inventory (verified listing/title or Forever flavor in search results)
- DBM-Core: https://www.curseforge.com/wow/addons/deadly-boss-mods
- Details!: https://www.curseforge.com/wow/addons/details
- Auctionator: https://www.curseforge.com/wow/addons/auctionator
- Questie: https://www.curseforge.com/wow/addons/questie
- RareScanner: https://www.curseforge.com/wow/addons/rarescanner
- TomTom: https://www.curseforge.com/wow/addons/tomtom
- AtlasLoot Classic Forever: https://www.curseforge.com/wow/addons/atlasloot-classic-forever
- BugGrabber: https://www.curseforge.com/wow/addons/bug-grabber
- RestedXP: https://www.curseforge.com/wow/addons/rxp-guides
- Forever AIO: https://www.curseforge.com/wow/addons/forever-aio
- ForeverPlus: https://www.curseforge.com/wow/addons/foreverplus
- Naowh Forever: https://www.curseforge.com/wow/addons/naowhforever
- Forever Leveling BiS: https://www.curseforge.com/wow/addons/forever-leveling-bis
- Forever Suite: https://www.curseforge.com/wow/addons/wow-forever-suite
- XE QoL Forever: https://www.curseforge.com/wow/addons/xe-qol-forever
- Cursive Forever: https://www.curseforge.com/wow/addons/cursive-forever
- Quartermaster Forever: https://www.curseforge.com/wow/addons/quartermaster-forever
- Node Sight: https://www.curseforge.com/wow/addons/node-sight
- Forever Loot Sparkles: https://www.curseforge.com/wow/addons/forever-loot-sparkles
- Forever Quest Tint: https://www.curseforge.com/wow/addons/forever-quest-tint
- What's Training?: https://www.curseforge.com/wow/addons/whats-training
- NDui Classic: https://www.curseforge.com/wow/addons/ndui-classic
- ForeverPath Goal Planner: https://www.curseforge.com/wow/addons/foreverpath-goal-planner
- Terminal: https://www.curseforge.com/wow/addons/terminal
- FojjiCore: https://www.curseforge.com/wow/addons/fojjicore
- OpenMap: https://www.curseforge.com/wow/addons/openmap
- Lore Forever: https://www.curseforge.com/wow/addons/lore-forever
- Spoken: https://www.curseforge.com/wow/addons/spoken

**Note:** Some normalized slug URLs above are search-derived candidates (not all individually opened). Verify destination and Forever flavor before adding to a user-facing recommendation or relying on a specific version. Strongest independently retrieved pages: DBM, Questie, AtlasLoot, Forever AIO, ForeverPlus, Naowh Forever, Forever Leveling BiS, Cursive Forever, Forever Suite, Node Sight, Terminal, ForeverPath, NDui, XE QoL, Quartermaster, FojjiCore, OpenMap, What's Training, Forever Loot Sparkles, Forever Quest Tint.

CurseForge Forever-filter search: https://www.curseforge.com/wow/search?class=addons&gameVersionTypeId=88568&page=1&pageSize=50&sortBy=relevancy

## GitHub discovered candidates (repository-search matches, not audited or tested)
- https://github.com/neroxrw/foreverauras
- https://github.com/dnl-gentile/olympus-addon
- https://github.com/ForeverArtisan/ForeverArtisan
- https://github.com/DurtsGaming/Catnip
- https://github.com/swirllyman/DoesItDie
- https://github.com/PhenomDevel/BlizzHUDTweaks
- https://github.com/Topher121/AddonForge
- https://github.com/Atraeau/WoW-Addons
- https://github.com/skittlenicks/JourneyTracker
- https://github.com/Krelock/NodeSight
- https://github.com/GalacticWandererAddon/Waymark
- https://github.com/PhenomDevel/PhenomRaidTools
- https://github.com/Thaoky/Altoholic_Forever
- https://github.com/smoergi/OneForAll_Forever
- https://github.com/hastecraft/super-tweaks
- https://github.com/TylerHampton/aux-forever
- https://github.com/orbit0r/ElvUI-Forever
- https://github.com/CryptoLogiq/SkillsAlreadyKnown
- https://github.com/krilar1/ForeverTools
- https://github.com/prezus/ForeverGuide
- https://github.com/amptie/EasyRaidForever
- https://github.com/RevoltLive85/ForeverSwingTimer
- https://github.com/Scoots/CHUDForever
- https://github.com/peligwen/auction-hound
- https://github.com/yellmourn/PetSmart
- https://github.com/Chairface30/ChairCraft
- https://github.com/zmsl/hekili
- https://github.com/fitzforge/wowforever-openmap
- https://github.com/ClassicWoWCommunity/forever-bugs
- https://github.com/Wetxius/ShestakUI_Forever
- https://github.com/ssablon/ForeverRotation
- https://github.com/sage3648/mythicsim-forever-engine
- https://github.com/gunba/wow-forever-sim
- https://github.com/hastecraft/forever-icons
- https://github.com/PixelCattt/Forever-Launcher
- https://github.com/Argorlant/forever-practice-yard
- https://github.com/krebs3r/umbra-unit-frames
- https://github.com/bnetworking/MMT
- https://github.com/Jreese702/DS-Forever
- https://github.com/cjber/tweaks-forever
- https://github.com/bySQT/forever-tracker
- https://github.com/pacco971/ForeverGuild
- https://github.com/pacco971/LvL-Guide
- https://github.com/Hitshade/BuffTap
- https://github.com/cjber/skillup-forever
- https://github.com/Geraldlol/witchcraft
- https://github.com/Kamikaetzchen/KamiUI
- https://github.com/Redbu11dev/UnitPlates-forever
- https://github.com/darkdracos/ForeverContentTracker
- https://github.com/james-attree/wowf_dps_sim
- https://github.com/Imemoth/wow-foreverdb
- https://github.com/GuybrushGit/ForeverSim
- https://github.com/th3pajay/soundalerter-forever
- https://github.com/Naths-Analytics/forever-market-terminal
- https://github.com/laurencestokes/forever-route-lab
- https://github.com/Bl4ut0/ItemRack-Universal
- https://github.com/tysongoulding/Questie-Forever
- https://github.com/Thunderz96/forever-addon-kit
- https://github.com/mparke/forever-addons
- https://github.com/xIGBClutchIx/ForeverPlusPlus
- https://github.com/Gethe/wow-ui-source

## Suggested source-inspection order
1. Development: Atraeau/WoW-Addons, Thunderz96/forever-addon-kit, mparke/forever-addons, xIGBClutchIx/ForeverPlusPlus, Gethe/wow-ui-source.
2. Combat/encounters: official DBM, PhenomRaidTools, foreverauras, EasyRaidForever, Cursive, Details, FojjiCore.
3. World data: NaowhForever, ForeverPath, AtlasLoot, Forever AIO, OneForAll_Forever, Questie official and Questie-Forever.
4. UI/secure frames: ElvUI-Forever, ShestakUI_Forever, NDui Classic, Forever Suite, ForeverPlus.
5. Character/item persistence and communication: Altoholic_Forever, ItemRack-Universal, Quartermaster Forever, ForeverPath, Terminal.
6. Bugs and testing: ClassicWoWCommunity/forever-bugs, RestedXP issue #384 (reported Forever Lua cast error), BugGrabber.

## Required next audit fields per addon
Name; source URL; CurseForge project ID; latest Forever-specific file ID and version; date; license; repository; last commit; build/interface/TOC; API namespaces; secrets/secure handling; SavedVariables; dependencies; data assets; tests; known issues; direct verified source; confidence; reuse constraints. Avoid copying All Rights Reserved code or proprietary data without permission.

## Cross-source observations
- Modern secret values and secure restrictions are recurring blockers; inspect how successful addons use native duration/cooldown widgets and event-driven updates rather than reading secret combat values.
- Multi-module addons use separate folders and optional load-on-demand components; ZIP packaging needs exact folder validation.
- Some authors report no automatic profession scans at login; user-opened profession windows are a safer trigger.
- Raid/quest/loot data in third-party addons are *candidates*, not live confirmation. Track original source and client build.
- Distinguish flavor-support listings from current functional compatibility, and addon descriptions from verified implemented features.

## Discovery gaps
- No complete CurseForge API pagination/export was performed, no bulk source downloads, and no comprehensive GitHub code search.
- Search results capped at 100 for broad GitHub queries. Some matches are guides, utilities, simulators, bots, and unrelated projects, not Lua addons.
- Current launch-day runtime tests and updated API dump not available.
- The complete inventory should be expanded and deduplicated by repository/project ID, not by title alone.
