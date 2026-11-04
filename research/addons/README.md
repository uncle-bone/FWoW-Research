# Addon reverse-engineering research

This area holds independently authored, source-backed technical research for addons used with or developed for WoW Forever. The reports describe behavior and evidence; they do not certify untested live behavior.

## Workstreams

- [Dreadwatch](dreadwatch/README.md) — pending comprehensive source inventory and system/module analysis.
- [BoneUI addon studies](boneui/README.md) — pending consolidation and completion of the EllesmereUI, ForeverAuras, and FojjiCore analyses.

Each workstream should maintain its own inventory, report set, evidence labels, and unresolved-work list. Coordinate changes by keeping files in each addon’s directory and linking completed reports here and from the root README.

## Evidence labels

Use one label per factual claim or finding:

- **Source-confirmed** — directly supported by the identified source file, symbol, and inspected version/commit.
- **Client/build-derived** — extracted from a specified authorized client build or its local addon installation; not automatically live behavior.
- **Observed-live** — reproduced in the specified live game/client build with method and date recorded.
- **Inferred** — reasoned from cited evidence but not directly demonstrated.
- **Unknown** — unresolved or unavailable evidence.

Do not upgrade static or historical source evidence into live-confirmed behavior. Record conflicting evidence and build/version differences rather than silently choosing one.

## Minimum report contents

For each addon, record:

1. Exact addon version, source URL/repository, commit or archive identity, inspected date, and method.
2. File/module inventory, manifests, load order, dependencies, and a coverage matrix.
3. Architecture and module responsibilities; public/internal APIs; event registration and handlers.
4. SavedVariables/configuration, important data flows, and representative execution paths.
5. Inter-addon integration, runtime constraints, security/protected-frame behavior, error handling, performance considerations, and compatibility limits where supported by evidence.
6. Source paths and symbols for findings, confidence/evidence labels, citations/links, and unresolved questions.
7. Licenses and redistribution limits. Do not add upstream code dumps, copyrighted assets, credentials, game executables, or client archives. Prefer concise independently written analysis and permitted factual metadata.

“Complete” means every in-scope file/module has a recorded disposition and every major system has an evidence-backed analysis. It does not mean every possible runtime state has been proven. List explicit gaps; do not claim 100% understanding or live certification without evidence.

## Current addon-specific source studies

- [EllesmereUI 9.7.3 — inventory, source traces, and completion matrix](ellesmereui/README.md)
- [ForeverAuras 1.1.0 — scoped inventory and gaps](foreverauras/README.md)
- [FojjiCore 4.0.3 — scoped inventory and gaps](fojjicore/README.md)

These studies are distinct from the [BoneUI workstream](boneui/README.md) and do not modify its addon source.
