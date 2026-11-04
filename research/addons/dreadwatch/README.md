# Dreadwatch reverse engineering

Status: **in progress**. This page will index the Dreadwatch source inventory, module/system analyses, reference-addon comparison, compatibility findings, and remaining verification work.

Keep all conclusions evidence-labeled per [the addon research standards](../README.md). Record the exact Dreadwatch revision/archive and source versions inspected. Static comparison with DBM/BigWigs is explanatory evidence only; do not copy their code or claim Forever runtime behavior from source alone.

## Reports

- [DBM-Core 12.1.19 combat detection and logging ownership](dbm-combat-detection-logging-2026-11-04.md) — archive-pinned logging lifecycle, zone/reload transitions, ownership and failure gaps.
- [Dreadwatch v0.1.1 packaged core/module inventory](dreadwatch-v0.1.1-core-inventory-2026-11-04.md) — all five Lua files, function/event/data-flow matrix and prototype limitations.

- [DBM encounter-warning and timeline function call graph](dbm-encounter-events-callgraph-2026-11-03.md) — suppression, bar creation, lifecycle, stale-event guards and recovery.

- [DBM-CoA SmartSync v3 end-to-end source trace](dbm-coa-smartsync3-source-trace-2026-11-03.md) — all H/S/I/K/K2/R/R2/D/A paths, validation, indexing, gating, persistence, simulator and risks.

- [Reference-engine source audit and per-addon coverage matrix](reference-engine-audit-2026-11-03.md) — DBM-Core, DBM-Dungeons Forever, BigWigs, LittleWigs, DBM-CoA and Dreadwatch; source paths, evidence labels and open gaps.

## Completion matrix

See the [per-addon matrix](reference-engine-audit-2026-11-03.md#per-addon-coverage-matrix). All addons remain **partial**; complete function-level inventories and live verification are not claimed.

## Open questions and verification gaps

See [actionable gaps](reference-engine-audit-2026-11-03.md#actionable-gaps).