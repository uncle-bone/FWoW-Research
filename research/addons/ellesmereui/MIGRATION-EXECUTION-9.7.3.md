# EllesmereUI 9.7.3 — migration execution audit, first pass

**Source:** user-supplied `EllesmereUI-9.7.3.zip` SHA-256 `8c572970a01b94d26ab6be30327200b46b4654e40da33303da3677de3749093e`; file `EllesmereUI/EllesmereUI_Migration.lua` (5,407 lines). **Date:** 2026-11-03. **Method:** read uploaded ZIP directly, enumerate all `EllesmereUI.RegisterMigration({ ... })` sites, extract literal `id`, `scope`, description, guards and candidate state paths, review migration-runner semantics. No 9.7.4 findings are silently substituted. No live tests.

## Coverage result

**114 literal migration registrations:** 42 global, 59 profile, 13 specProfile. Every registration has a source location, literal ID, scope and a candidate body section in the generated **EllesmereUI_9.7.3_Migration_Execution_Inventory.md** conversation artifact. **Important limitation:** this is a first-pass lexical source inventory; nested blocks, local aliases, indirect writes and downstream consumer links require Lua-aware tracing. The extracted body boundaries and line ranges must be manually validated before citing them as exhaustive. Do not claim 114 fully verified execution paths.

## Source-confirmed runner semantics

`EllesmereUI_Migration.lua` defines `RegisterMigration`, `RunOne`, `RunMigration`, `GetFlagTable`. Registration validates the spec table, nonempty unique string ID, callable body and scope in `global/profile/specProfile`. The runner visits the corresponding global DB, profile table or spec-profile store; each host stores `_migrations[id]` completion markers. `RunOne` uses `pcall(body, ctx)`; success stamps the flag and failure records a session-local error. **No transactional rollback is implemented by this runner.** If a body partially mutates a table and then raises an error, a later retry sees that partially changed state. The registration comment requires idempotent bodies; it does **not** establish that all bodies meet that requirement.

## Representative body paths (source-confirmed)

- **`clickcast_macro_hover_reaction_v1`** — `scope=profile`, starting at line 159. Reads `ctx.profile.addons`, checks for a click-cast table and iterates bindings, targeting macro hovercast reaction flags. The description states it preserves prior unfiltered behavior. Exact downstream UI/dispatch consumers remain unverified.
- **`clickcast_frame_spell_reaction_v1`** — `scope=global`, starting at line 193. Reads `ctx.db.clickCast`; checks `reactionSeeded` before altering eligible bindings. For `hovercast == "both"`, copies a frame binding into the list and changes the original to hover-only; sets reaction booleans and `reactionSeeded`. This marker makes repeat processing of that binding avoid re-splitting in normal conditions. **Inferred risk:** failure between list append and marker update could cause a duplicate on retry; requires fault-injection verification.
- **`spec_overrides_fresh_start_v1`** — `scope=profile`, source registration around line 394. Its description explicitly calls for wiping spec-override data. This is an intentional destructive transformation of old configuration, not a harmless normalization. Verify downstream readers and backup expectations before migration testing.

## Required per-registration validation checklist

For each of the 114 registrations, validate exact body span and any nested helper definitions; record input assumptions and type guards, all state reads/writes, version and per-entry markers, side effects, failure points, retry/idempotence proof or counterexample, downstream readers and callers, and corrupted-state tests. The lexical inventory captures starting points, **not** all those answers. Dynamically generated or aliased registration calls are **unknown** until a Lua-aware call graph is built.

## Next uncovered modules

1. `EllesmereUI_Profiles.lua`: import/decode, profile switching, spec overrides, persistence and rollback.
2. `EllesmereUI_CombatQueue.lua` and ActionBars secure/visibility modules: deferred operations and cleanup.
3. Each package's event ownership and unregistration map.
4. Dynamic API aliases and module-level function inventory.

## Evidence matrix

| Question | Evidence | State |
|---|---|---|
| Exact 9.7.3 archive identity | client/build-derived archive hash | recorded |
| Literal registration count and scopes | source-confirmed static scan | indexed |
| Per-entry body, first guards and candidate state paths | source-confirmed lexical samples | indexed, manual validation pending |
| Migration flag/error/retry behavior | source-confirmed framework | traced |
| Every body's idempotence and partial-failure safety | unknown | not proven |
| Per-migration downstream consumers | unknown | not closed |
| Dynamic registration aliases | unknown | not closed |
| Matching Forever live runtime | observed-live | none |

No third-party source or artwork is reproduced in this report.