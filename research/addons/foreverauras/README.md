# ForeverAuras — scoped research inventory

**Upstream:** https://github.com/neroxrw/foreverauras. **Research date:** 2026-11-03. **Source:** user-uploaded `ForeverAuras-1.1.0.zip`; `ForeverAuras/ForeverAuras.toc` declares **1.1.0**, interface **16001, 120105**, `SavedVariables: ForeverAurasSaved`, GPL-2.0. **Evidence:** source-confirmed manifest; not observed-live.

| Area | Source locations | Evidence | Status |
|---|---|---|---|
| Startup/load order | `ForeverAuras.toc`, `Init.lua`, `ClientAPI.lua`, `Compatibility.lua` | source-confirmed | manifest indexed, runtime branches pending |
| Trigger and aura state | `BuffTrigger2.lua`, `GenericTrigger.lua`, `SecretAuraTrigger.lua`, `Conditions.lua` | source-confirmed | pending exhaustive tracing |
| Display/regions | `RegionTypes/`, `SubRegionTypes/`, `BaseRegions/` | source-confirmed | pending |
| Saved data/imports | `ForeverAuras.lua`, `Transmission.lua`, `Modernize.lua` | source-confirmed | schema and malicious input paths pending |
| Client-protected aura handling | `Secrets.lua`, `SecretAura*.lua`, `CDMSetup.lua` | source-confirmed | combat/live behavior unknown |
| External integrations | `API.lua`, `BossMods.lua`, optional dependency list in TOC | source-confirmed | integration tests pending |

**Completion:** inventory/manifest partial, implementation-level and live verification unfinished. Do not equate optional dependencies with mandatory requirements. Preserve GPL attribution and avoid bulk code copying. No live tests claimed.
