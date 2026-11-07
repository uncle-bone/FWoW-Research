# WildQuest — source access and redistribution review

Research date: 2026-11-07. Input: user-provided `Questie-RXPGuides-Zygor.zip` (not redistributed here).

## Why the full ZIP is not in this public repository
The archive combines five independently licensed addon trees, including third-party libraries, databases, and guide content. Uploading the whole archive as-is would redistribute all of that content. The user can access their original uploaded archive in the conversation; this repository contains independently authored analysis and source references.

## Inspected license evidence
- `Questie/LICENSE.md`: historical contribution licensing is complicated; the team says to consider unlicensed contributions all rights reserved when in doubt, while supporting GPLv3 copying subject to caveats. Questie name/logo excluded.
- `QuestieDB/LICENSE.md`: inherited Questie data/provenance and similarly complicated historical contributor permissions. Questie name/logo excluded.
- `QuestieTrace/LICENSE.md`: GPLv3, name/logo excluded.
- `RXPGuides/LICENSE`: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International; scope and additional embedded content should be reviewed before redistribution.
- `ZygorGuidesViewerForever/`: no top-level addon-wide license identified in the supplied ZIP; licenses under `Libs/` and `Skins/` do not automatically license the entire addon.

## Upstream source access
- Questie project: https://github.com/Questie/Questie
- QuestieDB: https://github.com/Questie/QuestieDB
- QuestieTrace: https://github.com/Questie/QuestieTrace
- RestedXP organization: https://github.com/RestedXP
- Zygor: refer to its official distribution or obtain the rightsholder's permission; do not infer permission from the bundled third-party library licenses.

Upstream repositories may not match the exact versions or Forever-specific modifications in the user's archive. Match by version/commit and inspect the original files for accurate comparisons.

## Next research deliverables
Publish original architecture diagrams, per-file indexes (names and hashes only), interface/API compatibility notes, quest schema comparisons, data provenance and independently written feature analysis. Preserve source citations and evidence tiers. Do not copy full guide datasets or addon source into this public research repository unless the specific content's redistribution rights have been checked and required attribution/license terms are met.

**Status:** source-access guidance only; no third-party source uploaded.
