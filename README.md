# Warcraft Forever Research Database

Maintainer: Uncle Bone

Research and source-backed data for developing World of Warcraft: Forever addons. **Not an official Blizzard project.**

## Sources
- [Wowhead](https://www.wowhead.com/) — editorial coverage, item/quest/spell references, and corroboration. Forever-specific records must be verified against the matching client build; Classic/retail records are not automatically Forever records.
- [ForeverDiff builds](https://foreverdiff.com/builds/) — client-build comparisons and DB2 record coverage.
- [WoW Forever datamining pipeline](https://github.com/herodope/wow-datamine) — extraction and comparison tools for a locally installed authorized client.
- [Everloot](https://github.com/Everloot/everloot) — observation data and collector design (respect AGPL code and CC BY-SA data licenses).
- [Forever Addon Kit](https://github.com/Thunderz96/forever-addon-kit) — beta API reference.
- [Blizzard installation instructions](https://news.blizzard.com/en-us/article/24304160/the-world-of-warcraft-forever-beta-now-live) — install through Battle.net.

## Game client scanning
Blizzard's Battle.net app is the verified source of an authorized client install. Select World of Warcraft → Game Version → World of Warcraft: Forever Beta (when available to your account). Scan your own installation locally. Do not upload executables, CASC archives, encrypted assets, credentials, or copyrighted client bundles to this repository.

The `wow_classic_beta` product code has hosted other games: verify the client version starts with `1.60.` and the build ID is at least 69876 before tagging records as Forever. See the datamining pipeline for the detailed detection rule.

## Data integrity
Every imported record should carry `source_url`, `observed_build`, `collected_at`, `method`, `license`, and `confidence`. Keep beta-only, client-extracted, community-observed, and confirmed-live records distinct. Store independently authored summaries and permitted factual metadata, not bulk copies of third-party protected content.

## WoW-Professions Forever archive

The [profession source archive](research/professions/2026-11-09-FOREVER-PROFESSIONS-DETAILED-SOURCE-ARCHIVE.md) inventories all 15 linked pages: all 13 profession guide pages plus Camping and Merchant's Favor. It records page structures, source caveats, Forever-specific findings, and current extraction gaps. It is an original research index and summary, not a full offline mirror; the source guide pages remain linked because they contain their complete material lists, route maps, and article details. Guide recommendations are beta/editorial claims until verified against a matching Forever client build.

## Local client scan

A locally installed Forever client was verified as flavor `wowf`, version `1.60.1.70707` (build 70707). The first scan’s source-attributed, addon-derived catalog records and audit are in [research/local-client-scans/2026-11-03](research/local-client-scans/2026-11-03/README.md). The scan found 35 dungeon journal instance files, 311 named NPC/catalog rows (279 with explicit NPC IDs; 201 with encounter IDs), and 24 custom DBM Forever registration modules. These static addon records are not live-mechanics verification. No client archives, executable, or addon folders were added.

## Status

One authorized local Forever client build has been scanned and its source-attributed factual metadata documented. Continued work should add client database extraction and live observations while preserving build and confidence provenance.

### Encounter cross-reference (2026-11-03)

[Read the encounter audit](research/local-client-scans/2026-11-03/ENCOUNTER-AUDIT.md) or [download the machine-readable joins](research/local-client-scans/2026-11-03/encounter-cross-reference.json). All 24 installed DBM-Party-Forever registration modules match catalog encounter IDs by exact numeric ID. The catalog has 201 rows with encounter IDs, 216 assignments and 215 distinct encounter IDs; 191 catalog IDs lack a module in this 24-module set. Encounter ID 2742 occurs twice (Sneed and Sneed's Shredder). Static matches are **not** live-confirmed mechanics, boss spawns, creature triggers, timers or warnings. The audit preserves source names and provenance without changing original extracts.

### Dreadwatch encounter source audit (2026-11-03)

The client has since updated to build 70755. The addon/source comparison and build-specific caveats are in the [Dreadwatch source audit](research/encounter-source-audits/2026-11-03-dreadwatch-forever-source-audit.md) and [machine-readable JSON](research/encounter-source-audits/2026-11-03-dreadwatch-forever-source-audit.json). The existing dungeon catalog remains attributed to build 70707 until re-extracted for 70755.

A focused follow-up records the [Headless Horseman module candidates](research/encounter-source-audits/2026-11-03-headless-horseman-source-candidates.md) and [machine-readable candidates](research/encounter-source-audits/2026-11-03-headless-horseman-source-candidates.json). They are source-only or historical; the installed DBM-WorldEvents TOC does not target interface 16001.

A follow-up catalogs the [KwikTip Forever static encounter records](research/encounter-source-audits/2026-11-03-kwiktip-forever-coverage.md) and [machine-readable coverage](research/encounter-source-audits/2026-11-03-kwiktip-forever-coverage.json). It contributes 13 normal-mode encounter ID/name candidates for Hall of Thanes, Ragefire Chasm, and Stormwind Stockade; its own documentation says the package is not client-tested and has zero complete dungeons.

### Addon reverse engineering

Two source-audit workstreams are underway in this repository. See the [addon research index](research/addons/README.md) for evidence standards and coverage expectations, [Dreadwatch](research/addons/dreadwatch/README.md), and [BoneUI addon studies](research/addons/boneui/README.md). These analyses track source evidence and unresolved runtime verification separately.

## Addon reverse-engineering research

[Addon research index](research/addons/README.md) · [EllesmereUI 9.7.3](research/addons/ellesmereui/README.md) · [ForeverAuras 1.1.0](research/addons/foreverauras/README.md) · [FojjiCore 4.0.3](research/addons/fojjicore/README.md). These are source-grounded, **incomplete** studies; no live certification is claimed.

### Dreadwatch source audits (2026-11-04)

- [DBM-Core 12.1.19 combat detection and logging ownership](research/addons/dreadwatch/dbm-combat-detection-logging-2026-11-04.md)
- [Dreadwatch 0.1.1 packaged core inventory](research/addons/dreadwatch/dreadwatch-v0.1.1-core-inventory-2026-11-04.md)

- [Dreadwatch HEAD vs engine ZIP](research/addons/dreadwatch/github-head-vs-bigtest-2026-11-04.md) and [registry/encounter/scheduler call graph](research/addons/dreadwatch/registry-activation-scheduler-trace-2026-11-04.md) — pinned source comparison and prototype execution paths.
