# EllesmereUI 9.7.3 — click-cast migration to runtime consumer

**Baseline:** uploaded `EllesmereUI-9.7.3.zip`; **date:** 2026-11-03; **method:** direct line-by-line inspection of migration body and cross-file searches for affected fields. **Evidence:** source-confirmed unless labeled inferred. No live execution.

## Migration producer

`EllesmereUI/EllesmereUI_Migration.lua:193-240` registers `clickcast_frame_spell_reaction_v1`, `scope="global"`. The body accesses `ctx.db.clickCast` and returns if it is not a table. It processes `clickCast.globals` and every list in `clickCast.specs` when present. It snapshots each list's initial length, only processes table entries without `reactionSeeded`, and limits eligible entries to spell, item, or hovercast macro bindings. For `hovercast == "both"`, it appends a frame-only copy, changes the original to hover-only, sets friendly/enemy flags, and marks both records `reactionSeeded`. It skips entries already marked. **Source-confirmed.**

**Idempotence nuance:** a successfully completed pass stamps the global migration flag through the runner, and per-binding `reactionSeeded` prevents re-splitting on later executions. However, the append precedes the original's marker update. **Inferred risk:** if an error interrupts the body after append but before the original is marked, a retry may append a second frame binding. This is a possible non-transactional failure mode, not a reproduced defect.

## Runtime consumer

`EllesmereUIRaidFrames/EUI_RaidFrames_ClickCast.lua` reads the transformed binding fields. In particular:
- `:354-357` classifies hovercast versus frame-cast paths using `binding.hovercast`.
- `:376` tests binding type and hovercast eligibility.
- `:485` propagates the hovercast value into a constructed binding.
- `:508-515` contains a **separate runtime** splitting path for `hovercast == "both"`, creating frame-only and hover-only representations.
- `:956` and `:1147` read `binding.hovercast` during later processing.
- `:1814` includes hovercast in a binding signature.

**Source-confirmed downstream linkage:** the migration writes `hovercast` and the RaidFrames click-cast implementation reads that field. **Not yet proven:** exact active-profile/global/spec merge order, whether the runtime split runs on already-migrated records, and whether the signature prevents redundant secure attribute writes. Those require a full `EUI_RaidFrames_ClickCast.lua` caller trace.

## Distinguish completion marker from runtime data

The exact `reactionSeeded` token appears only in `EllesmereUI_Migration.lua:211,221,232` among inspected Lua files. The runtime click-cast module reads `hovercast`, not the migration marker. **Source-confirmed lexical search.** Thus the marker is migration bookkeeping, not demonstrated as a runtime dispatch condition.

## Additional migration downstream entrypoint

`spec_overrides_fresh_start_v1` (`EllesmereUI_Migration.lua:394-406`) calls `RearmRBAdvancedMigration`, then removes `specOverrideGroups`, `specOverrides`, and `specUnlockOverrides` from each profile. The next registration `rb_adv_remigrate_after_wipe_v1` (`:413-429`) checks for an existing ResourceBars module entry and may re-arm migration. `EllesmereUI_Profiles.lua:4089-4090,4270-4271` calls `SpecOverrides_OnSpecChanged`, whose implementation is at `EUI_SpecOverrides_Harvest.lua:593`. This is a **confirmed spec-override subsystem consumer chain**, but the exact three deleted fields' later readers and full re-arm helper effects still require inspection.

## Coverage

| Trace | Status |
|---|---|
| Click-cast migration inputs/guards/transform | source-confirmed |
| Per-binding success idempotence | source-confirmed conditional behavior |
| Partial failure/retry duplication | inferred risk; not tested |
| Runtime click-cast field consumer | source-confirmed |
| Runtime global/spec/profile selection | unknown |
| Spec-override migration to spec-change subsystem | partially traced |
| All 114 migration consumer links | **not complete** |
| Matching live client | not tested |

No upstream code or artwork reproduced; independently authored technical summary only.
