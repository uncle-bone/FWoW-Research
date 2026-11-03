# WoW Forever addon development: cross-source compilation
Date: 2026-11-03. Target live client 1.60.1.70707, interface 16001. This document compares public evidence; it does not claim fresh in-game tests.

## Source inventory and evidence quality
1. Thunderz96/forever-addon-kit: first-week in-game tests build 69893, 2026-09-17 onward; some retests after 70009. API capture, three sample addons, porting script, bug reproductions. https://github.com/Thunderz96/forever-addon-kit
2. mparke/forever-addons: archived early-beta field guide; useful architectural notes but older than live 70707. https://github.com/mparke/forever-addons/blob/main/docs/research/forever-addon-field-guide.md
3. xIGBClutchIx/ForeverPlusPlus: explicit evidence labels [local], [in-game], [dump], [addon], [web]; build 70707 client identity and tests up through 70338. https://github.com/xIGBClutchIx/ForeverPlusPlus/blob/main/docs/forever-api.md
4. Atraeau/WoW-Addons: generated APIDocumentation from build 70170, 410 systems, 6598 functions, 1806 events, 797 types. Searchable API and Lua type definitions, scaffolding, linting, deployment examples. https://github.com/Atraeau/WoW-Addons and https://github.com/Atraeau/WoW-Addons/blob/main/docs/api/README.md
5. Gethe/wow-ui-source, forever branch: Blizzard UI Lua source, source inspection rather than proof of addon permission at runtime. https://github.com/Gethe/wow-ui-source/tree/forever

## Cross-source conclusions
### Client identification and packaging
- Build 70707 live product wowf, folder _forever_, executable Wow.exe [ForeverPlusPlus local]. Earlier beta product wow_classic_beta, folder _classic_beta_, executable WowB.exe [forever-addon-kit/Atraeau; beta-specific].
- Interface 16001, WOW_PROJECT_ID == WOW_PROJECT_MAINLINE [independent in-game confirmations]. Mainline constant cannot identify Forever.
- Recommended test: local iface=select(4,GetBuildInfo()); local isForever=type(iface)=="number" and iface>=16000 and iface<17000; then feature-probe actual APIs. Do not use >=100000 as sole modern-engine test.
- A plain AddonName.toc with ## Interface: 16001 works. _Camelot.toc won a controlled precedence test in build 70009; older conflicting observations exist. Check installed live addons before shipping dual flavor TOCs.

### API migration
- Retail-derived C_* namespaces replace numerous Classic globals (e.g. GetSpellInfo, UnitAura, GetTalentInfo, GetMerchantItemInfo, CombatLogGetCurrentEventInfo). API presence and permissions must be checked individually.
- Traits and Legacy trees use C_Traits, not old talent APIs; Retail specialization assumptions also break.
- Modern C_UnitAuras, C_Spell, C_SpellBook, C_Container, C_Item, C_EncounterTimeline, C_EncounterEvents, C_EncounterWarnings are research starting points, not blanket guarantees.
- Atraeau generated API reference (70170) is more recent than Thunderz baseline (69893) but predates live 70707. Diff on-client documentation to settle signatures.

### Combat secrets and secure code
- issecretvalue, issecrettable, canaccessvalue and C_Secrets are documented/tested. Combat may mark health, aura tables and individual aura values secret. Branching, formatting, comparison or arithmetic on secret data may throw.
- Per-spell aura secrecy via C_Secrets.GetSpellAuraSecrecy and ShouldSpellAuraBeSecret; some aura reads throw in combat even on player [ForeverPlusPlus in-game 70338].
- For safe visual cooldown display, investigate C_Spell.GetSpellCooldownDuration / C_UnitAuras.GetAuraDuration returning LuaDurationObject and Cooldown:SetCooldownFromDurationObject, rather than manipulating secret numbers.
- Protected UI actions must not be automated. ReloadUI addon button can be blocked; user-typed /reload works in reported beta.
- Secure snippet load-order issue fixed in 70009; avoid propagating older failure as current fact.
- Old CLEU-dependent combat addons cannot be assumed portable; validate supported encounter/timeline/warning events and secret handling before DBM-like work.

### Loading, persistence, errors, deployment
- Early-beta SavedVariables writes reportedly failed to reload on cold start, corroborated by multiple authors. Current 70707 behavior NOT verified by this comparison. Test logout/restart/reload and account/character scopes.
- Early-beta error reporting reportedly pauses after 100 Lua errors; design minimal diagnostics and stop repeated errors.
- Event names and payloads should come from current client docs; handle uncertain RegisterEvent errors and avoid registering nonexistent events.
- Use Lua Language Server stubs and luacheck globals generated from current API, syntax-check, check TOC paths and release ZIP root. Atraeau project provides a practical model.
- Never deploy directly over user's existing addons for experimentation; use separate test install/backup and no destructive junction links.

## Pre-specialization validation matrix
1. Minimal addon loads and prints version, client build, interface and WOW_PROJECT_ID.
2. Plain TOC versus _Camelot precedence; files loaded and TOC metadata.
3. ADDON_LOADED, PLAYER_LOGIN, logout, /reload; SavedVariables persistence across full restart.
4. Presence/signatures of C_Secrets, C_EncounterTimeline, C_EncounterEvents, C_EncounterWarnings, C_UnitAuras and relevant callbacks.
5. Out-of-combat vs combat secret predicates, with no restricted value introspection or leakage.
6. Secure frame/taint behavior, chat restrictions, addon messaging in combat.
7. Group, dungeon, raid, encounter start/end, loading screen, disconnect/reconnect.
8. Lua errors, SavedVariables upgrades, addon enable/disable, independent versioned packaging.

## Explicit unresolved items
- Build 70707 API dump and source/API diff versus 70170.
- Exact live 70707 SavedVariables persistence and TOC precedence.
- Encounter API payloads and which are usable by third-party addons under combat secrets.
- Chat messaging restrictions and addon synchronization protocol behavior.
- What API data is safe to persist or share.
- Exact modern Lua runtime dialect/version in 70707: verify, don't assume 3.3.5a Lua 5.1 semantics.

## Evidence interpretation
[local] direct installed-client files; [in-game] tested live; [dump] documented surface only; [source] Blizzard UI source use; [third-party] author report; [inferred] hypothesis. Record build/date for each; never elevate [dump] to [in-game].
