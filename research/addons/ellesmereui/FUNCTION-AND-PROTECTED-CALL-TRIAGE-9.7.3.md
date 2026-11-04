# EllesmereUI 9.7.3 — function and protected-call coverage triage

**Baseline:** uploaded 9.7.3 ZIP, SHA-256 `8c572970a01b94d26ab6be30327200b46b4654e40da33303da3677de3749093e`. **Date:** 2026-11-03. **Method:** source-wide line-numbered lexical inventory across 639 non-Libs Lua files. The full per-file definition and protected-call candidate map is the conversation artifact `EllesmereUI_9.7.3_Function_Coverage.md`.

The scan finds **30,448 apparent named/assigned function definitions** and **248 protected-call candidates with a combat/defer token in the preceding 12 lines**. **Crucial limitation:** the 30,448 figure is **not a valid Lua function count**: the lexical pattern can match inside embedded secure Lua snippets, string templates, generated code and conditional blocks. It must not be used as a completion denominator. Likewise, a nearby `InCombatLockdown` token does **not** establish control-flow dominance over a protected operation. The index is navigation data, not semantic proof.

## High-risk path distinctions already source-traced

- `EUI_ActionBars_Controllers.lua:281-349`: secure attribute controller with eight attribute drivers and a persistent deduplicated bar-frame table. The secure list has no pruning path established.
- `EUI_ActionBars_Bars.lua:75-120,205-250`: secure paging snippets and explicit `page` state-driver replacement/removal. This is distinct from `eabvis` and `extravis`.
- `EUI_ActionBars_Vehicle.lua:32-69`: player vehicle events and combat-end retry before protected `SetShown`.
- `EUI_ActionBars_ExtraBars.lua:194-259`: protected reparenting guarded by combat state; secure hooks and potential SetParent reentrancy need whole-function analysis.
- `EllesmereUI_Profiles.lua:3952-4033,4075-4127`: spec/profile switching and combat-pending branch; full downstream rollback unverified.
- `EllesmereUI_Ticker.lua:174-222`: shared combat queue drains after `PLAYER_REGEN_ENABLED`; callers must gate combat themselves.

## Remaining source-closure requirements

1. Build an AST-aware function inventory, excluding comments, quoted strings and secure snippets, with anonymous function ownership and alias propagation.
2. Prove combat guards dominate each protected call along all control-flow branches; classify unguarded, deferred, secure-snippet and intentionally out-of-combat-only sites.
3. Pair each event registration to owning frame, dispatch and teardown (or documented session lifetime).
4. Prove every migration's actual write targets and downstream readers, not token matches.
5. Trace async import cancellation, nested validation, rollback and module refresh.
6. Keep matching-client taint and CPU tests separate from static source evidence.

**Status:** all first-party files indexed; semantic per-function and per-protected-call closure **not achieved**. No live testing.