# Research database contract

The repository currently stores coverage reports and a small manually verified API fact catalog, **not** 31,962 imported spells or a full quest database.

Record categories: items, quests, creatures, spells, talents, zones, objects, recipes, loot, api.

Required fields: `id`, `source_url`, `observed_build`, `method`, `license`. The importer adds `kind`, `record_key`, `collected_at`, and defaults `confidence` to `unverified`.

Run: `python tools/import_records.py input.json --kind items --output data/items.jsonl`.

Client inventory: `python tools/scan_client.py "C:\\Path\\To\\_classic_beta_" --output client-manifest.json`.

The client scanner is metadata-only, read-only, and skips account data. It does not unpack CASC or extract DB2 content yet. Do not publish full proprietary game assets or credentials. The scanner must run on a computer with the authorized game installed.

Never conflate source coverage counts with imported rows; never silently combine records from different builds.
