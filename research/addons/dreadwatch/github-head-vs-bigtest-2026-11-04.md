# Current Dreadwatch GitHub HEAD versus v0.1.1-bigtest engine ZIP

**Audit date:** 2026-11-04. **GitHub commit:** [`5002ef2fd2c64b0ebdac588f143da5ed412463ad`](https://github.com/uncle-bone/Dreadwatch/commit/5002ef2fd2c64b0ebdac588f143da5ed412463ad). **ZIP:** `Dreadwatch-v0.1.1-bigtest.zip`, SHA-256 `aa23d52fbf7a14af0165aa7602c8ce2c9aca9f4e5b25ceb935fcba7d32ac7eed`. **SC** source-confirmed, **IN** inferred, **UN** unknown, **OL** live-observed (none). Retired DreadwatchPTR is explicitly **out of scope**.

## Method and complete tree

Queried the connected GitHub commit history (17 commits), inspected the initial commit `1437a45ecdf70e193a9639ccfa5d3bced192cca2`, and compared that initial commit with HEAD. The initial commit added only `README.md`; the compare response lists exactly three added files, with no deletions/renames. All four HEAD files were individually fetched at the pinned SHA, and candidate engine paths returned 404. This **reconstructs the complete tracked tree** from initial commit plus GitHub compare rather than relying on search-index absence alone.

```text
README.md
research/warcraft-forever/CLIENT-API-COMPATIBILITY.md
research/warcraft-forever/MASTER-RESEARCH-REPORT.md
research/warcraft-forever/UNRESOLVED-RESEARCH-GAPS.md
```

Pinned blob SHAs: README `f0dd54621ad3fb0472d2df4284473c2c54a07c6d`; CLIENT-API `11d18971662006be9dbf17ce701837d0ddaeabe9`; MASTER `132706bba3a36fb84ef42b9911940a51decf9594`; UNRESOLVED `0c7998e28e3645ec345ac9b445fe39812388d297`. [Repository](https://github.com/uncle-bone/Dreadwatch).

## Every Lua/TOC file compared

| ZIP path | HEAD path/status | Behavioral difference |
|---|---|---|
| `Dreadwatch/Dreadwatch.toc` | **Absent** (SC) | No installable addon manifest or load order published |
| `Dreadwatch/Core.lua` | **Absent** (SC) | No published event bus, synthetic encounter state, warning/scheduling or slash commands |
| `Dreadwatch/Modules.lua` | **Absent** (SC) | No published module registry or static encounter catalog |
| `Dreadwatch/Diagnostics.lua` | **Absent** (SC) | No published API/build diagnostics |
| `Dreadwatch/TestHarness.lua` | **Absent** (SC) | No published synthetic bigtest phases |
| `Dreadwatch/UI.lua` | **Absent** (SC) | No published timer-bar rendering or draggable window |

ZIP additionally contains `README.txt`; GitHub has `README.md` and three research Markdown documents, which are not runtime equivalents. There are **zero common Lua/TOC paths**, so no meaningful per-file diff or line-level behavioral regression can be calculated. All runtime behavior described in [prototype inventory](dreadwatch-v0.1.1-core-inventory-2026-11-04.md) is **archive-only**, not behavior delivered by HEAD. **UN:** whether an independently distributed GitHub release asset contains the prototype; this report verifies repository source, not all release assets.

## Impact and disposition

- **SC:** Current GitHub HEAD is a research-only source tree; there is no installable Dreadwatch engine in tracked files.
- **IN:** a source checkout alone cannot run the ZIP's slash commands, UI or synthetic tests.
- **UN:** published release ZIP assets, any untracked private engine branch, and actual live Forever behavior.
- **Next engineering action:** decide whether to publish the original v0.1.1-bigtest engine as a baseline (with its explicitly synthetic/test status) or implement production systems first; do not silently promote synthetic encounters to live boss support.
- Do not resurrect DreadwatchPTR or reuse its retired test plan.

## Coverage update

**HEAD tree inventory: complete for pinned revision** (SC, four files). **ZIP Lua/TOC comparison: complete** (SC, six paths). **Runtime behavior diff: not applicable** (no shared runtime files). **Release asset and live certification: unknown**.
