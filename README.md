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

## Local client scan

A locally installed Forever client was verified as flavor `wowf`, version `1.60.1.70707` (build 70707). The first scan’s source-attributed, addon-derived catalog records and audit are in [research/local-client-scans/2026-11-03](research/local-client-scans/2026-11-03/README.md). The scan found 35 dungeon journal instance files, 311 named NPC/catalog rows (279 with explicit NPC IDs; 201 with encounter IDs), and 24 custom DBM Forever registration modules. These static addon records are not live-mechanics verification. No client archives, executable, or addon folders were added.

## Status

One authorized local Forever client build has been scanned and its source-attributed factual metadata documented. Continued work should add client database extraction and live observations while preserving build and confidence provenance.
