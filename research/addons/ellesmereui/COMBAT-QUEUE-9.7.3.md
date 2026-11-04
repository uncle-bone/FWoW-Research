# EllesmereUI 9.7.3 — combat deferral queue execution path

**Source:** uploaded `EllesmereUI-9.7.3.zip` (SHA-256 `8c572970a01b94d26ab6be30327200b46b4654e40da33303da3677de3749093e`), `EllesmereUI/EllesmereUI_Ticker.lua:174-222`. **Method:** direct manual line-by-line source inspection, 2026-11-03. All implementation findings are **source-confirmed**, not observed-live.

`EllesmereUI.NewCombatQueue(frame)` creates an isolated closure over `fns`, `index`, and `count`. The parent creates `EllesmereUI.CombatQueue` with its own frame at line 222. The source says child packages construct separate queues; their individual call sites have not all been traced.

### Registration → dispatch → cleanup

1. `q.Defer(key,fn)` rejects falsey keys and nonfunction callbacks. A duplicate pending key **replaces** its callback while retaining FIFO position. A new key appends and, on transition from empty to nonempty, registers `PLAYER_REGEN_ENABLED` on the queue frame (`:200-211`).
2. On `PLAYER_REGEN_ENABLED`, the frame unregisters that event, snapshots the pending callbacks, **resets** queue storage, then invokes each callback through `xpcall` and `geterrorhandler` (`:191-198`). A callback can enqueue new work without changing the current drain's snapshot.
3. `q.Has(key)` only checks whether a key is currently pending (`:213-215`). **There is no cancellation API** in this implementation.
4. **Important edge case, source-confirmed:** `Defer` does **not** check `InCombatLockdown()`. Calling it out of combat still waits for a future `PLAYER_REGEN_ENABLED`. Callers must gate it themselves, as the source comment explicitly states (`:180-182`).
5. **Inferred risk requiring a test:** a callback can be replaced with a newer closure that refers to changed state; stale closures may also persist until combat ends. Whether any actual caller violates the state re-read expectation is unknown.
6. **Source-confirmed error isolation:** one callback throwing does not stop later callbacks from being attempted, because each invocation has its own `xpcall`. The error handler's behavior itself depends on the game API.

### Completion matrix

| Area | Status |
|---|---|
| Parent queue construction and frame ownership | traced |
| Enqueue, deduplication and FIFO behavior | traced |
| Event registration and event cleanup | traced |
| Error isolation and reentrant queue behavior | traced |
| Cancellation semantics | confirmed absent in this implementation |
| Child package queue construction and all callers | pending |
| Combat lockdown correctness and protected-frame taint | unverified live |
| Tests on actual WoW Forever build | not performed |

No upstream implementation code is copied here.