# FojjiCore — scoped research inventory

**Upstream distribution:** https://www.curseforge.com/wow/addons/fojjicore. **Research date:** 2026-11-03. **Source:** user-uploaded `FojjiCore_4.0.3.zip`. The old third-party mirror is **not** an authoritative current source. No verified current official GitHub source repo.

| Area | Source locations | Evidence | Status |
|---|---|---|---|
| Manifest/dependencies | FojjiCore package `.toc` files; Forever flavor declares `OptionalDeps: ForeverAuras` | source-confirmed | manifest inventory, runtime gating pending |
| ForeverAuras bridge | `Forever/Backend.lua`, `Forever/Scripts.lua`, `Forever/Sync.lua` | source-confirmed | `ForeverAuras.ScanEvents` call sites identified; end-to-end test pending |
| Raid pack layout | `RaidTools/RaidPacks.lua`, `RaidTools/RaidPacksLayout.lua` | source-confirmed | pending complete import and state trace |
| User settings | `Options.lua` and package-specific config | source-confirmed | schema and migrations pending |
| Transport/validation | `Forever/Sync.lua` | source-confirmed static review | source-specific constraints need regression tests; no live peer verification |

**Completion:** partial static analysis only. `OptionalDeps` does not mean all FojjiCore features require ForeverAuras. No observed-live findings, no complete execution certification. Research notes are independently authored; no upstream code/assets included.
