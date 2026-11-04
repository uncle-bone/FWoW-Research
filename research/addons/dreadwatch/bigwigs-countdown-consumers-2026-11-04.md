# BigWigs 427.8 Countdown and Nameplates consumers

Reference source: supplied BigWigs-v427.8.zip. SC means archive source-confirmed; UN means runtime unverified. No Dreadwatch addon work.

## Countdown.lua (754 lines)

SC: OnPluginEnable (539–576) registers StartCountdown, StopCountdown, OnBossDisable, OnBossWipe (disable alias), ClearNameplate, profile and configuration messages. StartCountdown (645–700) stores expiry as GetTime()+time under module/text, optionally GUID. Replacing an existing countdown marks its previous table canceled. It schedules one SimpleTimer callback per countdown second. Each callback checks cancellation and LowestCountdown before text/audio. StopCountdown (701–714) sets cancellation flag and clears the display only if it belongs to the latest countdown. OnBossDisable (715+) marks all module countdowns canceled and removes their maps. Scheduled callbacks are logically invalidated; independent cancellation of each scheduled callback was not observed at these call sites. Countdown identity is not Bars eventId.

## Nameplates.lua (2144 lines)

SC: OnPluginEnable (1822–1831) subscribes StartNameplate, StopNameplate, ClearNameplate, StopBars (mapped to StopModuleNameplates), OnBossDisable, OnBossWipe and profile updates. Module-wide bar stopping therefore also initiates nameplate cleanup. OnPluginDisable starts at 1838. Deeper pending-callback cleanup remains unreviewed.

## Statistics.lua (595 lines)

SC: OnPluginEnable (336–345) subscribes boss engage/win/wipe/disable. Lines 455–456 emit StartBar and Timer for best-time comparisons; line 479 emits StopBar. Plugins, not only boss scripts, produce timer messages.

## Consumer separation

Bars.lua owns visual bars matched by module/text or eventId; Countdown.lua owns voice/text countdowns matched by module/text/GUID; Nameplates.lua owns nameplate indicators; Statistics.lua produces comparison bars. The lifecycle and cancellation signals overlap but their internal state is distinct.

UN: Forever runtime delivery, downstream secret-value handling, scheduled callback memory overhead. Do not infer live support from source handler presence.
