# Dreadwatch reverse engineering

Status: **in progress**. **Scope decision (2026-11-04): DreadwatchPTR is retired and excluded from active research, testing, and development.** The Dreadwatch v0.1.1-bigtest engine/prototype is a separate artifact; do not conflate it with the retired PTR diagnostics. This page will index the Dreadwatch source inventory, module/system analyses, reference-addon comparison, compatibility findings, and remaining verification work.

Keep all conclusions evidence-labeled per [the addon research standards](../README.md). Record the exact Dreadwatch revision/archive and source versions inspected. Static comparison with DBM/BigWigs is explanatory evidence only; do not copy their code or claim Forever runtime behavior from source alone.

**Priority override (2026-11-04):** Suspend all Dreadwatch addon/prototype analysis and implementation. Active work is **reference-source reverse engineering only** (BigWigs, LittleWigs, DBM and Forever-specific sources); the separate DBM encounter-warning/timeline audit belongs to the user's other workstream. DreadwatchPTR remains retired.

## Reports

- [BigWigs 427.8 core dispatcher, boss lifecycle, Timeline and Forever compatibility](bigwigs-4278-source-trace-2026-11-04.md) — source call graphs, state, cleanup, secret-value and coverage gaps.
- [LittleWigs 12.1.22 manifest and 907-Lua archive inventory](littlewigs-12122-manifest-inventory-2026-11-04.md) — game-type gates, source classification and remaining full-module work.

- [Pinned GitHub HEAD versus v0.1.1-bigtest engine](github-head-vs-bigtest-2026-11-04.md) — complete four-file tracked tree, six missing Lua/TOC files and archive-only runtime.
- [Module registry, encounter activation and warning scheduler](registry-activation-scheduler-trace-2026-11-04.md) — every packaged function/event path and behavior gaps.

- [DBM-Core 12.1.19 combat detection and logging ownership](dbm-combat-detection-logging-2026-11-04.md) — archive-pinned logging lifecycle, zone/reload transitions, ownership and failure gaps.
- [Dreadwatch v0.1.1 packaged core/module inventory](dreadwatch-v0.1.1-core-inventory-2026-11-04.md) — all five Lua files, function/event/data-flow matrix and prototype limitations.

- [DBM encounter-warning and timeline function call graph](dbm-encounter-events-callgraph-2026-11-03.md) — suppression, bar creation, lifecycle, stale-event guards and recovery.

- [DBM-CoA SmartSync v3 end-to-end source trace](dbm-coa-smartsync3-source-trace-2026-11-03.md) — all H/S/I/K/K2/R/R2/D/A paths, validation, indexing, gating, persistence, simulator and risks.

- [Reference-engine source audit and per-addon coverage matrix](reference-engine-audit-2026-11-03.md) — DBM-Core, DBM-Dungeons Forever, BigWigs, LittleWigs, DBM-CoA and Dreadwatch; source paths, evidence labels and open gaps.

## Completion matrix

See the [per-addon matrix](reference-engine-audit-2026-11-03.md#per-addon-coverage-matrix). All addons remain **partial**; complete function-level inventories and live verification are not claimed.

## Open questions and verification gaps

See [actionable gaps](reference-engine-audit-2026-11-03.md#actionable-gaps).