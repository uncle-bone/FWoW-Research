# EllesmereUI — source-grounded research (in progress)

**Maintainer of this research:** Uncle Bone. **Upstream:** https://github.com/EllesmereGaming/EllesmereUI. **Research date:** 2026-11-03. **Evidence baseline:** user-supplied `EllesmereUI-9.7.3.zip`, whose main `EllesmereUI/EllesmereUI.toc` declares version **9.7.3** and interfaces `120000, 120001, 120005, 120007, 120100, 120105, 16001`. SHA-256 of uploaded archive: `8c572970a01b94d26ab6be30327200b46b4654e40da33303da3677de3749093e`. GitHub default branch was separately observed to declare **9.7.4**; do not conflate the two revisions. **No live client tests were performed.**

## Architecture and execution inventory

| Area | Source locations / symbols to trace | Evidence | Completion / gap |
|---|---|---|---|
| Bootstrap and client gate | `EllesmereUI/EllesmereUI.toc`, `EllesmereUI_ClientGate.lua`, `EllesmereUI_Lite.lua`, `EllesmereUI_Startup.lua` | source-confirmed file/load declarations | Manifest inventory complete; all initialization branches unresolved |
| Saved state and migrations | `EllesmereUI_Migration.lua`, `EllesmereUI_Profiles.lua`, `EllesmereUI_ProfileSync.lua`, `EllesmereUI_SpecOverrides.lua` | source-confirmed named subsystems; `EllesmereUIDB` declared by TOC | Database schema/migration edge cases not certified |
| Positioning and anchors | `EUI_UnlockMode.lua`, `EUI_UnlockMode_Anchors.lua`, `EUI_UnlockMode_Movers.lua`, `EUI_UnlockMode_Positions.lua` | source-confirmed files | Frame ownership, rollback and combat interactions need execution tracing |
| Combat and secure actions | `EllesmereUI_Kick.lua`, `EllesmereUI_AuraKit.lua`, `EllesmereUIActionBars/EUI_ActionBars_Secure.lua`, `EUI_ActionBars_VisibilityDrivers.lua` | source-confirmed file names and static guard references | Taint and secure behavior unknown without targeted runtime tests |
| Shared display infrastructure | `EllesmereUI_PixelPerfect.lua`, `EllesmereUI_UICore.lua`, `EllesmereUI_Colors.lua`, `EllesmereUI_Fonts.lua`, `EllesmereUI_Ticker.lua` | source-confirmed | API contracts and call graph incomplete |
| UI feature packages | ActionBars, AuraBuffReminders, Bags, BlizzardSkin, Chat, CooldownManager, DamageMeters, DataBars, ForeverEssentials, Minimap, Nameplates, Options, QoL, RaidFrames, ResourceBars, UnitFrames, plus others | source-confirmed package directory inventory | Per-module behavioral branches and lifecycle tests incomplete |
| Cross-addon dependency | main and feature `.toc` manifests | source-confirmed: no declared mandatory ForeverAuras dependency in inspected EllesmereUI manifests | Indirect shared-Blizzard-API interactions not proven absent |

## Source-trace checkpoints

- `EllesmereUI/EllesmereUI.lua:432`, `:639`, `:641`, `:979` were indexed as event-registration sites in the earlier static audit. **Evidence: source-confirmed locations, not proof of runtime registration.**
- `EllesmereUI/EllesmereUI.lua:399`, `:595`, `:1029`, `:1033` were indexed as combat-lockdown references. **Evidence: source-confirmed static references; combat safety unknown.**
- `EllesmereUIActionBars/EUI_ActionBars_Bars.lua:29`, `:38`, `:129`, `:131` were indexed as secure-template references. **Evidence: source-confirmed static references.**
- `EllesmereUI/EllesmereUI_Profiles.lua:3858`, `:4889`, `:5136` were indexed as profile API references. **Evidence: source-confirmed static references; complete state semantics unknown.**

## Methods and limits

Methods: inspect supplied source ZIP, enumerate manifests and source files, extract static references and compare with official upstream manifest. Prior chat reports include `EllesmereUI_9.7.3_Static_Source_Audit.md`, `EllesmereUI_Reverse_Engineering_Dossier.md`, and `EllesmereUI_9.7.3_Deep_Source_Trace.md`; they are **not** committed here because the existing repository does not contain them and a static index is not an independently verified execution trace. Source evidence is **source-confirmed** only for literal declarations and code locations; no findings are marked **observed-live**. Version/interface declarations are **client/build-derived metadata**, not evidence of successful client operation. All untraced behavior is **unknown**. Inferred module responsibilities from names must not be presented as confirmed behavior.

## Completion matrix

| Workstream | Status |
|---|---|
| Archive integrity and file inventory | Complete for supplied ZIP |
| TOC/load-order declarations | Indexed; dynamic load paths pending |
| Architecture/module responsibility | Partial |
| Public API signatures and callers | Partial |
| Events/handlers and update cadence | Static locations indexed; dynamic dispatch pending |
| SavedVariables/config and migration | Partial |
| Data flow and execution branches | Partial |
| Inter-addon dependencies | Manifest-level reviewed; runtime integration pending |
| Error handling and rollback | Pending systematic audit |
| Performance, security, combat | Hotspots indexed; behavior unverified |
| Live Forever client validation | Not performed |

**Research completeness:** partial; **not** 100% reverse-engineered or live-certified. Next: function-level call graphs and deterministic mocked-API tests, then a user-facing live test sheet for any remaining client-only claims. Do not redistribute upstream code or artwork.

## Version-specific callback and migration follow-up (2026-11-03)

[Callback dispatch and migration inventory](CALLBACK-AND-MIGRATION-MAP-9.7.3.md) is generated directly from the **uploaded 9.7.3 ZIP**, not from upstream 9.7.4. It maps the EUILite function/string/default callback resolution and event unregister behavior, and records 114 migration registrations by scope. The full 9.7.3 static callback index is available in the conversation artifact; it has not been copied into GitHub because the source-derived index is approximately 709 KB. Remaining gaps are explicitly tracked in the linked report.

## Migration execution follow-up

[9.7.3 migration execution first-pass audit](MIGRATION-EXECUTION-9.7.3.md) enumerates 114 literal registrations (42 global / 59 profile / 13 specProfile) and distinguishes source-indexed bodies from unproven idempotence, downstream consumers, and runtime behavior. The longer per-registration lexical inventory was generated from the uploaded ZIP in the conversation; the GitHub report explicitly records its limitations. Migration coverage is **indexed, not execution-closed**.

## High-impact dispatch and ActionBars closure

[Four 9.7.3 high-impact execution paths](HIGH-IMPACT-EXECUTION-PATHS-9.7.3.md) trace slot-change rerouting, combat-deferred spec/profile switching, secure visibility, and profile selection. [ActionBars deferred-flag consumer](ACTIONBARS-DEFERRED-FLAG-CONSUMER-9.7.3.md) resolves the previously open `ns._eabApplyDeferred` → `PLAYER_REGEN_ENABLED` → `ApplyAll` edge. Explicit event unregistration, extra-bar state-driver teardown, complete migration consumers and live taint remain open.

## Resumed source tracing

[Extra-bar visibility proxy](EXTRA-BAR-VISIBILITY-9.7.3.md) resolves the dynamically assigned secure state callback and distinguishes three separate state drivers. [Click-cast migration to runtime consumer](CLICKCAST-MIGRATION-CONSUMER-9.7.3.md) links a global migration to RaidFrames field readers and records a partial-write retry risk. Both are source-only; remaining migration consumers and package cleanup are open.
