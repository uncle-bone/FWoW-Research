# EllesmereUI 9.7.3 — all-package event lifecycle audit

**Source:** uploaded `EllesmereUI-9.7.3.zip`, SHA-256 `8c572970a01b94d26ab6be30327200b46b4654e40da33303da3677de3749093e`. **Date:** 2026-11-03. **Method:** line-numbered lexical scan of all **647** Lua files, excluding 8 bundled-library-path Lua files from the first-party count. **Coverage:** **639 first-party Lua files across 25 packages**. Counts include conditionally unreachable code and may include tokens inside strings; they are **not runtime registrations, leak counts, or paired callback proofs**. The detailed package-by-package event and cleanup anchors are in the generated conversation artifact `EllesmereUI_9.7.3_All_Package_Event_Audit.md`.

| Package | Lua | RegisterEvent/UnitEvent tokens | Unregister tokens | OnEvent tokens | Hooks | Timers | Combat guards | State drivers reg/unreg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Core |75|167|87|83|98|158|117|0/0|
| ActionBars |28|168|37|37|103|73|108|6/3|
| AuraBuffReminders |13|101|16|11|8|17|18|0/0|
| Bags |20|50|30|28|66|28|36|0/0|
| BlizzardSkin |24|125|63|59|364|59|23|0/0|
| Chat |14|46|5|19|50|36|21|0/0|
| CooldownManager |45|162|44|39|66|57|37|1/0|
| DamageMeters |14|39|10|14|18|25|12|0/0|
| DataBars |21|11|7|5|5|10|57|5/1|
| ForeverEssentials |25|70|51|26|21|14|27|0/0|
| Friends |1|10|4|5|41|14|5|0/0|
| GroupFinder |3|8|5|5|31|5|11|0/0|
| LoadoutManager |1|2|1|1|0|5|4|0/0|
| Locales |20|0|0|0|0|0|0|0/0|
| Minimap |10|23|5|12|47|18|15|2/2|
| MythicTimer |8|25|21|11|2|16|8|0/0|
| Nameplates |19|106|41|26|19|17|9|0/0|
| Options |101|47|40|42|258|127|68|0/0|
| QoL |17|218|118|70|55|67|44|4/6|
| QuestTracker |7|45|13|10|15|19|15|0/0|
| Quickdraw |13|10|10|1|0|1|14|0/0|
| RaidFrames |38|108|40|24|43|38|89|5/5|
| ResourceBars |23|82|25|9|14|18|11|1/0|
| SimpleLootCouncil |68|55|17|31|84|92|10|0/0|
| UnitFrames |31|149|33|43|30|34|26|1/0|

**Unmatched / conditional teardown review priority:** QoL, ActionBars, core, CooldownManager, UnitFrames, BlizzardSkin, RaidFrames, Nameplates and AuraBuffReminders have many registration sites; Chat has 46 registration vs 5 unregister tokens. These comparisons **do not prove leaks**, because frame-local handlers may deliberately persist, cleanup can occur in a different owner, and a single `UnregisterAllEvents` can clear many events. Distinguish `self:RegisterEvent` (EUILite addon frame), local frame `RegisterEvent`, and secure state/attribute drivers. The generated full audit lists each package's concrete registration and unregistration file:line anchors.

**Verified ownership examples:** ActionBars `EUI_ActionBars_Vehicle.lua:36-69` owns a `vehVis` frame with four registrations and one `OnEvent`; its handler filters non-player vehicle events and gates protected `SetShown` until out of combat. ActionBars `EUI_ActionBars_Bars.lua:213-214,244-250` explicitly unregisters the `page` driver before replacing/removing it. The `eabvis` and `extravis` drivers have no matching unregister in this same file. The exact package teardown for `vehVis` is unverified.

**Status:** archive-wide discovery **complete**; individual event→dispatcher→unregister pairing across all 639 files **not complete**. Source-derived only; no runtime certification or evidence of actual resource leakage. Next queue: vehicle/bonus/extra-action secure ownership, migration downstream consumers, profile import/export and remaining protected paths.