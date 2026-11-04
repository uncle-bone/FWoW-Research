# EllesmereUI 9.7.3: extra-action reparent callback trace

Source: uploaded 9.7.3 archive, EllesmereUIActionBars/EUI_ActionBars_ExtraBars.lua lines 45-120 and 194-280. Source-only finding, not live-tested.

The local ReparentIntoHolder function at lines 109-120 defers on combat via ns.CombatQueue.Defer using a key derived from barKey. Otherwise it reparents each extra frame to holder. The SetParent hook at lines 254-262 calls ReparentIntoHolder only when newParent differs from holder. Consequently its own SetParent(holder) call does not recursively trigger another reparent through that hook. This establishes a local guard, not immunity to other hooks or engine transitions.

The initial position-capture callback at lines 73-100 registers OnUpdate only if immediate bounds capture fails. It clears OnUpdate after success or after more than 300 attempts, establishing an explicit registration/cleanup pair.

The AddFrame, ApplySystemAnchor, Show and SetParent secure hooks at lines 194-262 are not explicitly removable. A separate frame registers PLAYER_REGEN_ENABLED at lines 273-280 and does not unregister it within the inspected file. Whether the setup path executes more than once and whether hooks accumulate are still unverified.

Status: local reentrancy and temporary OnUpdate cleanup source-confirmed; package-wide event lifetime and live combat safety unresolved.