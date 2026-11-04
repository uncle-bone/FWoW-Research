# EllesmereUI 9.7.3 — profile export, import validation, and switch boundaries

**Source:** uploaded 9.7.3 ZIP, `EllesmereUI/EllesmereUI_Profiles.lua`. **Date:** 2026-11-03. **Method:** inspect function bodies and documented branch boundaries. Source-confirmed unless marked unknown. No runtime tests.

## Export profile snapshot

`ExportProfile(profileName, includedFolders, includeLayout, includeCDM, cdmSpecs, includeGlobals, includeOverrides, includeBlizzSkin)` starts at `:2185`. Missing inclusion flags default **true** for layout, overrides, CDM, globals and Blizzard skins (`:2186-2207`); callers in the interactive UI can explicitly override those defaults. It retrieves `db.profiles[profileName]`, returns nil when absent (`:2208-2210`), and when exporting the active profile snapshots fonts, custom colors, dark mode and unlock layout into the stored profile before deep-copying it (`:2211-2218`). It strips recipient-local `_importEstablishPending` and several stale payload flags from the export copy (`:2219-2230`). **Implication:** active-profile export has an intentional saved-state write before serialization, rather than being strictly read-only.

## Synchronous decode guards

`DecodeImportString` at `:2915-2947` rejects absent/short strings, old `!EUICDM_` layouts, wrong prefix, missing LibDeflate, printable decoding failure, decompression failure and non-table deserialization. It rejects payload versions below 3 or above 4, then strips private addon data if `payload.data` is a table. **Unknown:** whether all downstream import paths validate `payload.data` structure after a direct table payload bypasses this decoder.

## Async decode lifecycle

`DecodeImportStringAsync` at `:2983` uses an 8ms slice budget and 65,536-character printable decode chunks (`:2968-2970`). It validates cheaply before constructing a run; on starting a new run it calls `StopRun(active)` (`:2983-3005`). Its coroutine yields only when the running coroutine is the owned run, guarding a serializer hook from yielding unrelated synchronous deserializations (`:3006-3016`). The source contract says the returned handle can cancel and suppress completion; the full `StopRun` and frame/ticker cleanup branches need manual tracing before treating that as proven.

## Import payload and concurrent session

`ImportProfile(importStr, profileName)` starts at `:3313`. If an interactive API import session is active and not committing, it calls `_FinishApiImportSession(false)` and attempts `_ProfilesResetToMain` inside `pcall` (`:3314-3324`). It accepts either a decoded table or a string; the table path bypasses `DecodeImportString` (`:3325-3334`). It canonicalizes addon folder keys, reconciles imported media and rejects payload type `cdm_spells` (`:3336-3351`). It then determines the current specialization for auto-assignment and auto-apply decisions (`:3353-3362`). **Potential validation surface:** a direct table may carry malformed nested data; the downstream branches, not the decoder, must enforce structure. This is a review question, not a confirmed exploit.

## Profile switch state and refresh

`SwitchProfile(name)` at `:3952` returns immediately for a missing profile (`:3953-3954`), discards an active unlock session, closes spec-override edit sessions, harvests current overrides, snapshots outgoing fonts and unlock layout (`:3956-3988`). With dirty settings and synchronized module targets it flushes outgoing sync groups and may require reload (`:3990-4025`); otherwise it repoints the active DB. Public `SetProfile` simply forwards to `SwitchProfile` (`:4889-4891`). The spec event owner `specFrame` is registered in `:4075-4078` and processes combat-pending spec changes on `PLAYER_REGEN_ENABLED` (`:4082-4127`), with `RefreshAllAddons` downstream. **Unknown:** atomic rollback when a downstream addon refresh throws or the user changes spec twice during combat.

## Coverage matrix

| Path | State |
|---|---|
| Export defaults, active-profile snapshot, export-local field stripping | source-confirmed |
| Sync decode prefix/codec/version/private-data guards | source-confirmed |
| Async run creation and yield ownership | source-confirmed |
| Async cancellation/cleanup and exactly-once completion | pending deeper trace |
| Import direct-table path and session cancellation | source-confirmed |
| Nested table schema/merge and all import errors | pending |
| Switch outgoing harvest and dirty-sync branch | source-confirmed |
| Switch/spec refresh failure recovery | pending |
| Matching Forever runtime | not tested |

**Next queue:** async decoder cleanup and import transaction branches; secure protected-frame guard audit; remaining exact function coverage.