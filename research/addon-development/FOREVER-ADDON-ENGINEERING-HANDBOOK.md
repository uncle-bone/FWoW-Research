# WoW Forever addon engineering handbook
Research compiled 2026-11-03. Target: WoW Forever 1.60.1.70707, interface 16001. This is a research and engineering standard, not a claim that all listed APIs were tested on build 70707.

## 1. Evidence hierarchy and version matrix
- [LIVE-70707]: directly inspected or exercised on installed live build 70707; [TEST-build]: author supplied repeatable in-game test with exact build; [API-DUMP-build]: signature exists, runtime behavior unproven; [UI-SOURCE-build]: Blizzard UI calls API; [COMMUNITY]: report; [INFERENCE]: hypothesis.
- Beta 69893: forever-addon-kit API baseline, old _classic_beta_/WowB.exe and early errors.
- Beta 69913/70170: Atraeau generated APIDocumentation snapshots (counts differ across revisions; do not mix counts).
- Beta 70009: secure snippet fix and controlled _Camelot.toc precedence test.
- Beta 70338: ForeverPlusPlus self tests and aura secrecy failures.
- UI source 70532: Forever branch references.
- Live 70707: wowf, _forever_, Wow.exe, interface 16001; local file evidence from ForeverPlusPlus.
- Whenever sources disagree, record both and test against 70707; avoid retroactively labeling beta results as live.

## 2. Client detection and TOC
- `WOW_PROJECT_ID == WOW_PROJECT_MAINLINE` is NOT enough: Forever and Retail both report mainline.
- `local _, build, _, iface = GetBuildInfo(); local isForever = type(iface)=="number" and iface>=16000 and iface<17000` plus explicit API feature probes.
- Minimal `AddonName.toc`: `## Interface: 16001`, `## Title: AddonName`, `## Version: 0.1.0`, `## SavedVariables: AddonNameDB`, `Core.lua`. Add optional `## Dependencies` / `## OptionalDeps` only when needed.
- Multiple game variants may use `AddonName_Camelot.toc`; precedence tested in beta 70009, must retest in 70707.
- TOC file order matters. Ship an AddonName/ folder at ZIP root with TOC and referenced files, not a nested payload.
- Don't assume a Retail-style `>=100000` interface check works: Forever reports 16001.
- Confirm exact addon metadata support (`## X-GameType: camelot` or game-type directives) from working addon TOCs; do not invent metadata requirements.

## 3. Language, API, and UI
- Modern Retail/Midnight-derived API surface, not Classic 1.12 or Wrath 3.3.5a. The exact Lua runtime/dialect in 70707 needs direct verification; use the current client and tools to test syntax.
- Start with `C_Spell`, `C_SpellBook`, `C_UnitAuras`, `C_Traits`, `C_Container`, `C_Item`, `C_QuestLog`, `C_Map`, `C_ChatInfo`, `C_EncounterInfo`, `C_EncounterTimeline`, `C_EncounterEvents`, `C_EncounterWarnings` where relevant.
- Legacy globals `GetSpellInfo`, `UnitAura`, `GetTalentInfo`, `GetMerchantItemInfo`, `CombatLogGetCurrentEventInfo` are absent in documented early tests. Verify individually before porting.
- Forever talent and Legacy trees use `C_Traits`; no standard Retail specialization API guarantee. Do not key custom classes on Retail spec IDs.
- Use current Blizzard UI source for mixins, widgets, events, frame templates, Edit Mode and secure patterns. Source presence alone does not imply third-party permission.
- Prefer events over polling; bound repeated work and avoid per-frame full scans. Cache safe static metadata, not restricted combat secrets.

## 4. Secret values, protected actions, taint
- Modern combat restrictions may make health, auras, unit fields, and combat values secret, even for the player. A secret table may contain secret values and vice versa.
- Explore `issecretvalue`, `issecrettable`, `canaccessvalue`, `C_Secrets`, `C_RestrictedActions` on the actual build. Guard BEFORE comparisons, indexing, serialization, concatenation, arithmetic or formatting; do not log secret payloads.
- `pcall` may catch errors but is not a mechanism to extract or bypass protected data.
- Investigate DurationObjects and native cooldown widgets for sanctioned presentation without converting secret durations to ordinary numbers.
- Do not perform protected targeting, spellcasting, clicks, or restricted Blizzard frame operations from insecure addon code.
- Secure snippet bug reported early beta was fixed in 70009; verify current behavior.
- Combat log events and full traditional CLEU data cannot be assumed available. For encounter addons, test official encounter/timeline/warning APIs before designing architecture.

## 5. Events, diagnostics, and startup
- Test `ADDON_LOADED`, `PLAYER_LOGIN`, `PLAYER_ENTERING_WORLD`, `PLAYER_LOGOUT`, `ENCOUNTER_START`, `ENCOUNTER_END`, and selected documented events; never assume a name exists or has Retail payloads.
- Event registration may reject invalid names. Add a dev-only registration probe with `pcall(frame.RegisterEvent, frame, name)` and record success/failure without flooding chat.
- Instrument addon loading phases, elapsed time, handler errors, memory, and diagnostic counters; gate debug messages and cap buffers.
- Reproduce in and out of combat, in parties and raids, after zone transitions, and on login/reload.
- Avoid overwriting existing addon globals, monkey-patching Blizzard secure functions, or relying on frame load order without checking `IsAddOnLoaded`/modern equivalent.

## 6. SavedVariables and migrations
- Early beta reported SavedVariables not surviving cold restart. Do not infer live 70707 behavior.
- Test account-level and character-level SavedVariables separately; mutate during session, /reload, logout, fully exit client, relaunch, switch characters, then verify schema.
- Store only serializable plain values and approved, nonsecret data. Never serialize functions, userdata, secret data, or frame references.
- Version schema, migrate copies safely, preserve unknown future keys, and validate malformed/partial data.
- For data-sharing addons, keep protocol/schema versions independent of addon versions; validate all inbound data, cap size/rate, and maintain compatibility with older peers.

## 7. Chat, addon messaging and synchronization
- Probe `C_ChatInfo` registration, send/receive behavior, prefix limits, message length, group channel restrictions, and combat lockdown on 70707.
- Never assume Wrath-era `SendAddonMessage`, channel joining, or background sync techniques behave identically.
- Build a read-only packet echo test with two consenting clients before designing database synchronization. Do not send private data or hidden combat values.
- Treat remote packets as untrusted: explicit schemas, fingerprints, collision-safe IDs, deduplication, bounds, backoff, and abuse limits.

## 8. Research by feature area
- UI and settings: Blizzard frame templates, settings categories, slash commands, Edit Mode integration, accessibility and scaling.
- Spells, auras, talents: spell ID mapping, C_Spell, C_SpellBook, C_UnitAuras, C_Traits, and secrecy state.
- Inventory and loot: C_Container, C_Item, async item info, bags/bank availability, secure item interactions, item ID provenance.
- Quests/maps: C_QuestLog, C_Map, pins, map IDs, journal availability, phased/instance content.
- Encounters: C_EncounterInfo, C_EncounterTimeline, C_EncounterEvents, C_EncounterWarnings, ENCOUNTER_START/END, instance/zone identifiers, journal IDs, event secrecy.
- Group/guild/social: group roster, chat APIs, messaging restrictions, privacy, permissions.
- Performance: frame creation count, event churn, allocations, SavedVariables size, throttling, UI error budget.

## 9. Tooling and repeatable build pipeline
- Atraeau/WoW-Addons provides WowApiExport (/apiexport then /reload), docs/api.json, API Markdown generation, Lua Language Server definitions, luacheck globals, scaffolding, build-addons.lua, tests and CI examples.
- Thunderz96/forever-addon-kit provides 69893 captured baseline, api_scan.py, port_to_beta.py, ForeverBeacon and bug reproduction notes.
- mparke/forever-addons (archived 2026-10-01) provides ForeverProbe, ForeverKit, busted tests, luacheck and TDD conventions; its GPL-3.0 license requires care before reusing code.
- ForeverPlusPlus maintains evidence-tagged client identity, TOC precedence, secrets, event and API notes, and newer build tests.
- Gethe/wow-ui-source forever branch is the primary UI implementation reference; capture source commit/build used.
- Pin tool versions, run Lua syntax/static analysis, test pure logic separately, check TOC file references and case, and inspect ZIP paths and version strings.
- Avoid automatic junction-link deployment over an existing live addon. Work in a separate development client or copy with explicit backup.

## 10. Minimal safe starter (not yet in-game tested)
TOC:
```toc
## Interface: 16001
## Title: ForeverDiagnostics
## Version: 0.1.0
## SavedVariables: ForeverDiagnosticsDB
Core.lua
```
Lua:
```lua
local addonName = ...
local f = CreateFrame("Frame")
f:RegisterEvent("ADDON_LOADED")
f:RegisterEvent("PLAYER_LOGIN")
f:SetScript("OnEvent", function(_, event, arg1)
  if event == "ADDON_LOADED" and arg1 == addonName then
    ForeverDiagnosticsDB = type(ForeverDiagnosticsDB) == "table" and ForeverDiagnosticsDB or {schema=1}
  elseif event == "PLAYER_LOGIN" then
    local version, build, _, iface = GetBuildInfo()
    print("ForeverDiagnostics:", version, build, iface, "C_Secrets", type(C_Secrets))
  end
end)
```
This diagnostic addon is a reference snippet only; do not label it tested or published.

## 11. Live 70707 verification matrix
1. Client identity: /dump GetBuildInfo(), WOW_PROJECT_ID, actual flavor path and loaded TOC.
2. Startup: TOC load order, dependency handling, addon loaded, slash command, errors.
3. Persistence: /reload, logout, full restart, character swap, schema upgrade.
4. APIs: generate 70707 APIDocumentation and diff against 70170; test key signatures.
5. Security: secret predicates, safe in-combat probes, restricted action behavior, secure templates.
6. UI: native settings, tooltip, widget creation, frame anchoring, Edit Mode.
7. Inventory/spells/quests: async results, events, nil cases, combat state.
8. Encounters: available events, payloads, timeline/warnings APIs, instances, group sizes.
9. Networking: addon prefix, message sizes, throttling, combat restrictions, 2-client echo.
10. Packaging: install-ready ZIP, exact TOC version, no nested folder, release integrity and source tag.

## 12. Sources and licensing
- https://github.com/Atraeau/WoW-Addons (workspace, export and CI)
- https://atraeau.github.io/WoW-Addons/ (generated reference; version must be recorded)
- https://github.com/Thunderz96/forever-addon-kit (early beta experiments and porting)
- https://github.com/mparke/forever-addons (archived, GPL-3.0)
- https://github.com/xIGBClutchIx/ForeverPlusPlus/blob/main/docs/forever-api.md (evidence-tagged client notes)
- https://github.com/Gethe/wow-ui-source/tree/forever (Blizzard UI source)
- https://github.com/uncle-bone/FWoW-Research (our existing scan, foundation, and source comparison)
Check every source's license before copying code; research findings and interface descriptions are not blanket permission to relicense third-party code.

## 13. Unresolved research before claiming complete support
- No new direct access to user's live 70707 client in this task; runtime results unverified.
- Fresh 70707 API dump and full diff against 70170 not yet performed.
- Cold-restart SavedVariables, current TOC precedence, combat messaging, event payloads and all protected API behaviors need direct tests.
- Exact Lua version, combat-secret handling edge cases and encounter event semantics must be empirically checked.
