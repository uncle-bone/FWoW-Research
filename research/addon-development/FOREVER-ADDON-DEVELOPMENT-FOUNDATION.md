# WoW Forever addon development foundation
Research date: 2026-11-03. Target: live wowf 1.60.1.70707, interface 16001. This is a research guide, not an in-game verification report.

## Verified architecture and packaging
- Forever is a modern Mainline/Midnight-derived Lua addon environment, not the 1.12 or 3.3.5a API.
- Runtime WOW_PROJECT_ID reports WOW_PROJECT_MAINLINE, so this constant alone cannot distinguish Retail and Forever.
- Internal game-type token is camelot. For a Forever-only addon use a normal AddonName.toc with `## Interface: 16001`; for a multi-flavor addon consider AddonName_Camelot.toc (preferred over _Mainline.toc). Check current client behavior before shipping.
- Detect candidate Forever with `local iface = select(4, GetBuildInfo()); local isForever = iface >= 16000 and iface < 17000`; feature-probe each needed API as well.
- Do not rely on retail checks `interface >= 100000`: Forever is modern but reports 16001.
- Current live client reported as product wowf, folder _forever_, executable Wow.exe. Older beta documentation refers to wow_classic_beta, _classic_beta_, WowB.exe and may be obsolete.

## API migration
- Old Classic APIs such as GetSpellInfo, UnitAura, GetTalentInfo, GetSpecialization, GetMerchantItemInfo, and CombatLogGetCurrentEventInfo must not be assumed present.
- Check C_Spell, C_UnitAuras, C_Traits, C_SpellBook, C_Container, C_Item, C_EncounterInfo, C_EncounterEvents, C_EncounterTimeline, C_EncounterWarnings and the current Blizzard UI source for signatures and supported use.
- Unknown event registration can throw: check against client event docs and optionally use pcall around uncertain RegisterEvent calls; log failures.
- Never assume API presence implies unrestricted use or identical Retail behavior.

## Secrets, combat, secure execution
- Forever inherits Midnight-style secret-value restrictions. Health, auras and combat-related data can become secret in combat, including for the player.
- Before handling potentially secret values, use documented secrecy predicates and safe handling. Never compare, concatenate, format, serialize or perform arithmetic on secret values. A normal pcall is not a way to bypass restricted information.
- C_Secrets, C_RestrictedActions and secure templates matter. Do not automate protected gameplay actions or open protected Blizzard frames from tainted callbacks.
- Secure snippet bug in early beta was fixed by build 70009; don't repeat early-beta claims without build checks.
- Traditional CLEU-based DBM architecture cannot simply be transplanted. Study encounter timeline/events/warnings, supported event payloads and permitted combat data first.

## Recommended development procedure
1. Record live client build, product, interface, addon version, and test date.
2. Capture current client APIDocumentation and inspect matching Blizzard UI source (Gethe forever branch); compare with older dumps, noting differences.
3. Build a minimal addon with TOC, Lua entrypoint, addon-loaded event, slash diagnostics and explicit version output. Install only in a test copy or test addon directory; preserve existing addons.
4. Add API capability probes and event registration diagnostics. Record nil/missing APIs and secret-state behavior in and out of combat without accessing forbidden data.
5. Exercise login, reload, character switch, solo/group, entering instances, combat, reload after SavedVariables writes, and UI taint/error scenarios.
6. Run Lua syntax/static checks, TOC/path/case checks, release ZIP structure checks, and inspect game errors; only in-game tests establish runtime correctness.
7. Track provenance per finding: [client-70707], [in-game-build], [API-dump-build], [Blizzard-source-build], [third-party], [inferred]. Never promote inferred mechanics to verified.
8. Version every addon independently; release source and install-ready ZIP only after checks. Keep this research separate from CoA/3.3.5a work.

## Open questions to resolve before a specialized addon
- Refresh API dump from build 70707 or newer and diff against 70170.
- Verify supported encounter event payloads, timeline callbacks, warnings and secret-safe handling with a minimal read-only probe.
- Verify persistence, addon message/chat lockdown rules, restricted frames, secure state drivers and loading order on current client.
- Establish a repeatable test matrix and small capability registry before implementing boss-specific modules.

## Sources (with build caveats)
- https://github.com/Thunderz96/forever-addon-kit (first-week beta 69893; secure fix later 70009)
- https://github.com/mparke/forever-addons/blob/main/docs/research/forever-addon-field-guide.md (build 69913, archived)
- https://github.com/xIGBClutchIx/ForeverPlusPlus/blob/main/docs/forever-api.md (live 70707 identification, earlier runtime tests)
- https://github.com/Atraeau/WoW-Addons/blob/main/docs/api/README.md (API documentation from 70170)
- https://atraeau.github.io/WoW-Addons/ (searchable API documentation)
- https://github.com/Gethe/wow-ui-source/tree/forever (Blizzard UI source mirror)
