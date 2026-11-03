# WoW Forever addon build, compatibility and testing toolchain
Date: 2026-11-03. Target live build 70707, interface 16001. Public-source audit only; tools were not installed or run against the user's client.

## Tool matrix (discovered, source verified)
| Tool/project | Purpose | Verification/status | Link |
|---|---|---|---|
| Atraeau/WoW-Addons | Full multi-addon workspace; scaffold, API exporter, docs, LSP types, luacheck globals, build, deploy, CI | README/source verified; beta flavor path config needs override for live _forever_ | https://github.com/Atraeau/WoW-Addons |
| WowApiExport | Export actual client APIDocumentation via /apiexport, then /reload; generates docs/API JSON | Included under Atraeau src | https://github.com/Atraeau/WoW-Addons |
| BTPCompatCheck | Live API presence probe (/btpcheck) | Included under Atraeau src | https://github.com/Atraeau/WoW-Addons |
| build-addons.lua | Package only TOC/XML-referenced files and assets, --check validates | Atraeau scripts, test-build-addons.lua | https://github.com/Atraeau/WoW-Addons |
| new-addon.ps1 | Scaffold new Forever addon | Atraeau scripts | https://github.com/Atraeau/WoW-Addons |
| deploy.ps1 / deploy.sh | Windows junctions/copy and macOS/Linux symlink/copy; watch support | Do NOT junction-link into user's live install without consent and backup | https://github.com/Atraeau/WoW-Addons |
| generate-api-docs.ps1 | Convert live API dump to searchable Markdown | Atraeau scripts | https://github.com/Atraeau/WoW-Addons |
| generate-lua-definitions.ps1 | LuaCATS/Lua Language Server annotations from dump | Atraeau scripts | https://github.com/Atraeau/WoW-Addons |
| generate-luacheck-globals.ps1 | Exact build-specific globals for luacheck | Atraeau scripts | https://github.com/Atraeau/WoW-Addons |
| API reference website | Search build 70170 API systems/functions/events/types | Older than 70707; signatures only, not runtime guarantee | https://atraeau.github.io/WoW-Addons/ |
| forever-addon-kit | Early-beta API capture, compatibility shim, probes, port scripts, error/saved-variable utilities | Build 69893, some fixes tested 70009; recheck before use | https://github.com/Thunderz96/forever-addon-kit |
| api_scan.py / api_scan_all.py | Scan source calls against captured Forever API; batch rank incompatibilities | Captured 69893 API baseline; refresh before trusting | https://github.com/Thunderz96/forever-addon-kit |
| port_to_beta.py | Copy Retail addon and patch TOC/build checks | Beta-specific; do not apply blindly to 70707 | https://github.com/Thunderz96/forever-addon-kit |
| eui_audit.py | Scan missing frames, unknown events, secure snippet sites | Project-specific but useful patterns | https://github.com/Thunderz96/forever-addon-kit |
| sv_bridge.py / sv_watch.py / sv_diff.py | Early-beta SavedVariables workaround, watcher and diff | Only if live 70707 persistence bug reproduced; workaround executes saved Lua, audit input safety | https://github.com/Thunderz96/forever-addon-kit |
| read_bugs.py | Read BugGrabber logs | Supports diagnosing client errors | https://github.com/Thunderz96/forever-addon-kit |
| ForeverBeacon / fb_extract.py | In-game API/events/NPC/quest/vendor/spell/talent probe; CSV/JSONL export | Beta, opt-in and privacy safeguards needed | https://github.com/Thunderz96/forever-addon-kit |
| FBSVTest | SavedVariables lifecycle regression probe | Beta test case | https://github.com/Thunderz96/forever-addon-kit |
| mparke ForeverProbe | API presence, event payload, secret-value probe | Archived 2026-10-01, GPL-3.0; good test design reference | https://github.com/mparke/forever-addons |
| mparke ForeverKit | Data migrations, locale and event dispatch | Archived GPL-3.0; do not copy without license compliance | https://github.com/mparke/forever-addons |
| mparke toolchain | Make bootstrap/check/watch, busted specs, luacheck, stylua, coverage, type checks, CurseForge pipeline | Archived; reproducible workflow reference | https://github.com/mparke/forever-addons |
| ForeverPlusPlus Self Test | In-game evidence-tagged client compatibility diagnostics, TOC/secure/aura tests | Last described self-test 70338; live identity 70707 | https://github.com/xIGBClutchIx/ForeverPlusPlus |
| Gethe Forever UI source | Actual Blizzard UI implementations, secure templates, event/API usage | Source presence not permission or runtime guarantee | https://github.com/Gethe/wow-ui-source/tree/forever |
| BugLab | In-game debug output, UI inspection and event analysis | CurseForge Forever flavor; alpha/beta, All Rights Reserved | https://www.curseforge.com/wow/addons/buglab |
| BugGrabber | Lua error capture and persisted debugging | Check current Forever-specific file and behavior | https://www.curseforge.com/wow/addons/bug-grabber |
| wowless | Headless WoW Lua/FrameXML interpreter and addon test environment | Pre-alpha; no confirmed Forever target, not a replacement for 70707 | https://github.com/wowless/wowless |
| julius-retzer/forever-addons | CLI addon manager, CF/GitHub install, version check, backup/rollback, local patching, unittest | Tested on macOS, Windows support claimed but not confirmed | https://github.com/julius-retzer/forever-addons |
| Lua Language Server | Static analysis, LuaCATS API autocomplete and type hints | Use generated 70707 types | https://github.com/LuaLS/lua-language-server |
| luacheck | Lua static linting and missing globals detection | Use client-specific globals, avoid false positives | https://github.com/lunarmodules/luacheck |
| StyLua | Lua formatter | Static only | https://github.com/JohnnyMorganz/StyLua |
| busted | Lua unit testing outside game | Mock WoW globals and test pure logic | https://github.com/lunarmodules/busted |
| luac / Lua interpreter | Syntax-check and test pure modules | Match supported Lua dialect; Lua 5.4 tests do not prove live client compatibility | https://www.lua.org/ |
| GitHub Actions | Lint, unit tests, ZIP integrity, tags, releases | Existing Atraeau CI example | https://github.com/Atraeau/WoW-Addons/tree/main/.github/workflows |

## High-priority compatibility failure modes
1. Forever reports interface 16001 but WOW_PROJECT_MAINLINE; naive retail >=100000 check selects wrong branch.
2. Removed Classic global functions, missing frames/events, modern C_* API signature changes.
3. Secret values: forbidden comparisons, stringification, arithmetic, iteration, and combat aura reads.
4. Protected action and secure snippet handling; build 70009 fixed early-beta secure initialization bug.
5. SavedVariables persistence was broken in early beta; re-test cold restart on 70707 before deploying workaround.
6. _Camelot.toc precedence, dependencies, addon load order, optional modules.
7. Versioned data migrations and async item/spell/quest APIs.
8. No assumption that CLEU-based boss tracking or addon messaging is allowed.
9. Error flood may hit client reporting cap; instrument rate-limited diagnostics.
10. ZIP structure and all TOC/XML paths must be verified; source should match release tag.

## Recommended standardized pipeline for Uncle Bone
- Source in uncle-bone/FWoW-Research (shared evidence) and separate addon repos under uncle-bone for shipped addons.
- Extract current live APIDocumentation with WowApiExport and compare signatures to 70170 and 69893 baselines.
- Scaffold a minimal Forever diagnostics addon; run BTPCompatCheck and targeted ForeverProbe experiments, logging build and provenance.
- Configure LuaLS with live API-generated LuaCATS types; run luacheck, StyLua and Lua syntax checks; unit-test pure logic with busted.
- Use API scan and TOC/frame/event static audit, but flag outdated 69893 signatures as low confidence.
- Validate saved data on /reload, logout, cold restart and character swap; test secure behavior both out of and in combat.
- Test UI, party/raid, instance/encounter, combat lockdown, messaging and recovery after disconnect; no protected automation.
- Build a single top-level AddonName/ install-ready ZIP; verify every TOC reference, version, hash, and GitHub release asset; tag exact source.
- Keep a per-build test report (tested live vs static vs not tested) and use backup/rollback. Do not touch existing user installs automatically.

## Pending source-level and live verification
- Full audit of scripts and CI workflows; test runner execution and output verification.
- Client 70707 API export and exact Lua runtime version.
- Current 70707 SavedVariables cold restart, _Camelot.toc precedence, combat event payloads, C_ChatInfo limits.
- Whether wowless can model the Forever secret-value and Camelot systems; assume no until demonstrated.
- Whether BugLab and BugGrabber function properly on live 70707.
- CurseForge API pagination of all development-tool category addons and exact Forever file versions.
- Licenses and dependencies for all tools before vendoring.
