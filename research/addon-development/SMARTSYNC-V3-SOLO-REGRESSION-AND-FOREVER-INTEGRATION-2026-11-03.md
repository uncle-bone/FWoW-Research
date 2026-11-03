# SmartSync v3 isolated solo regression — cross-project research and Forever integration
Date: 2026-11-03. Evidence classification: SOURCE VERIFIED for cited source files, UNRESOLVED for live-client behavior.

## Scope
Research guidance only. Do not assume WoW Forever implements any CoA protocol. Do not add CoASync to Dreadwatch merely because other addons use it. Preserve real multiplayer wire formats and behavior. No addon implementation, live testing, or network packets performed by this research task.

## Source audit
1. **LootCollector**, `uncle-bone/LootCollector`, `LootCollector/Modules/SmartSync.lua`: explicitly labels itself SmartSync v3, WoW 3.3.5a / Lua 5.1; prefix `LCS3`, channel `CoASync`, HELLO interval 300s, bounded outgoing/incoming queues, independent discovery reconciliation. `tests/smartsync_channel_test.lua` exercises decorated/plain channel HELLO reception and rejects incorrect channel identities. This is SOURCE VERIFIED, not proof of a simulator or live peer-to-peer success.
2. **pfQuest-CoA**, `uncle-bone/pfQuest-CoA`, `tests/pfquest_coasync_test.lua`: distinct `PFQ6:H:pfQuest-CoA-v4:12` HELLO wire fixture, channel `CoASync`, Lua 5.1 test, source path `build/staging/pfQuest/coa_sync.lua`. It is not LootCollector SmartSync v3; inspect its actual generated receive/validation/import source before designing its simulator. Current repo tree exposes build scripts/tests but not that staging file.
3. **Dreadwatch**, `uncle-bone/Dreadwatch`, main tree inspected: PTR diagnostics and research docs only; no SmartSync v3 or CoASync implementation. Any future Forever synchronization is a separate capability-gated design, not a port by assumption.
4. **FWoW-Research**, `uncle-bone/FWoW-Research`: research repository, no live addon receive path or SmartSync implementation.

Sources:
- https://github.com/uncle-bone/LootCollector/blob/main/LootCollector/Modules/SmartSync.lua
- https://github.com/uncle-bone/LootCollector/blob/main/tests/smartsync_channel_test.lua
- https://github.com/uncle-bone/pfQuest-CoA/blob/main/tests/pfquest_coasync_test.lua
- https://github.com/uncle-bone/Dreadwatch/tree/main/DreadwatchPTR

## Required simulator contract (per addon; implementation pending)
- Explicit opt-in, disabled by default, local-only entry point; never send addon/channel messages.
- Run real parser, validation, receive, dedupe, reconciliation, and import functions; do not replace them with test-only approximations.
- Substitute temporary isolated DB, peer registry, outgoing/incoming queues, statistics, indexes and clock. Preserve identity of live objects and restore references on every exit, including Lua errors (pcall/xpcall); avoid mutating nested live objects through shared references.
- Test HELLO and peer discovery; valid import; duplicate rejection; malformed/truncated/oversized packets; invalid schema/identity/channel; reconciliation and version mismatch where implemented.
- Guard *every* outbound transport function with a fail-fast test trap; assert zero sends and unchanged network counters.
- Snapshot/compare live SavedVariables and in-memory state before/after, including error injection; ensure test records cannot persist across reloads.
- Tests must be compatible with the addon runtime (Lua 5.1 for CoA projects). Offline Lua 5.1 checks must cover sandbox rollback, network-send prevention and persistence leakage; tests do not establish multiplayer correctness.
- Retain normal production protocol, message formats, and peer sharing unchanged. Simulator must not switch normal live mode to solo-only.
- Explicitly label source-derived versus PTR/live-game verification.

## WoW Forever integration gate
- First identify the actual Forever addon/client Lua version, addon messaging APIs, group/channel permissions, secret-value restrictions, and persistent storage behavior on the target build.
- Never assume `CHAT_MSG_CHANNEL`, `SendChatMessage`, AceEvent, `LCS3`, `PFQ6`, or channel `CoASync` behave as in 3.3.5a.
- Do not introduce a Forever wire protocol until the target addon has a genuine send/receive implementation, schema, validated import path and evidence of permission-safe handling.
- Once a Forever implementation exists, design a protocol-specific isolated simulator around its own actual functions, with the same no-network/no-persistence guarantees.

## Verification status and gaps
Repository trees and specific files inspected through GitHub connector on 2026-11-03. No Lua tests executed in this research-only change; no simulated packets run; no game clients or real peers tested. Need full source audit of LootCollector handlers/import and pfQuest built source before claiming either simulator is complete. Need PTR verification for Forever messaging and SavedVariables. This document is integration guidance, not a shipped addon feature.
