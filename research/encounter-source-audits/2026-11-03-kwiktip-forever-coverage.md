# KwikTip Forever public encounter-data audit

Collected: 2026-11-03  
Repository inspected: [postblink/KwikTip](https://github.com/postblink/KwikTip), branch `master`, head [d409c816](https://github.com/postblink/KwikTip/commit/d409c816daa390203fd9bdf884e5b05a6273addd). Its Forever alpha is `0.1.0-alpha.1`; the README and package metadata target client build 1.60.1.70707/interface 16001.

This is a public encounter-tip package and contains additional useful ID mappings. The package marks client testing as pending and reports zero complete dungeons. Its metadata is static source evidence; it is not proof of live behavior or a complete encounter database.

## Coverage records

The Forever alpha defines 13 normal-difficulty encounter tips:

| Instance | Dungeon | Encounter ID → package name |
|---:|---|---|
| 3065 | Hall of Thanes | 3493 → Faldrim Anvilmar; 3495 → Infurnus; 3494 → Plunder; 3496 → Durgen Dirgehammer |
| 389 | Ragefire Chasm | 2732 → Oggleflint; 2733 → Taragaman the Hungerer; 2734 → Jergosh the Invoker; 2735 → Bazzalan |
| 34 | Stormwind Stockade | 2756 → Targorr the Dread; 2757 → Kam Deepfury; 2758 → Hamhock; 2759 → Dextren Ward; 2760 → Bazil Thredd |

The 3495 Infurnus/Magmatus association is explicitly provisional in the source documentation. Do not silently rename it. The package excludes rare Bruegal Ironknuckle because it lacks a verified encounter mapping. Difficulty scope is `difficultyIDs={1}`; it does not cover alternate difficulties, raids, trash-by-NPC targeting, or room/route detection.

## What it contributes to Dreadwatch research

- Adds a source-attributed list of instance and encounter IDs for two new Forever dungeons and two Classic dungeons.
- Provides brief strategy tips and opt-in instance overviews, but the source does not provide boss spell IDs, cast schedules, repeat cooldowns, phase triggers, or combat logs.
- The addon expects encounter events and uses a persistent tip window for dungeon overviews; its own documentation says in-client load, event names, success/wipe handling, HUD behavior, and settings persistence still need testing.
- Its static ID files target build 70707. They must not be relabeled as build 70755 data without re-extraction from the newer build.

## Provenance

- [Coverage metadata](https://github.com/postblink/KwikTip/blob/master/Forever/Coverage.json)
- [Forever encounter data](https://github.com/postblink/KwikTip/blob/master/Forever/DungeonData.lua)
- [Hall of Thanes build-70707 evidence](https://github.com/postblink/KwikTip/blob/master/docs/FOREVER_HALL_OF_THANES_IDS_70707.json)
- [Ragefire build-70707 evidence](https://github.com/postblink/KwikTip/blob/master/docs/FOREVER_RAGEFIRE_IDS_70707.json)
- [Stockade build-70707 evidence](https://github.com/postblink/KwikTip/blob/master/docs/FOREVER_STOCKADE_IDS_70707.json)
- [Forever readiness and tests](https://github.com/postblink/KwikTip/blob/master/docs/FOREVER_READINESS.md)

No third-party tip prose or addon code is copied into this repository. The machine-readable companion contains only short factual metadata, IDs, classifications, and source paths.
