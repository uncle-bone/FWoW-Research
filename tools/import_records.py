#!/usr/bin/env python3
"""Normalize independently collected Forever records; stdlib only."""
import argparse, csv, hashlib, json
from datetime import datetime, timezone
from pathlib import Path

KINDS = {"items", "quests", "creatures", "spells", "talents", "zones", "objects", "recipes", "loot", "api"}
REQUIRED = {"source_url", "observed_build", "method", "license"}
def normalize(record, kind):
    if not isinstance(record, dict): raise ValueError("record must be an object")
    if kind not in KINDS: raise ValueError("unknown category")
    missing = [k for k in REQUIRED if not record.get(k)]
    if missing: raise ValueError("missing provenance: " + ", ".join(missing))
    rid = record.get("id")
    if rid is None or isinstance(rid, bool) or not str(rid).strip(): raise ValueError("missing record id")
    record = dict(record)
    record["id"] = str(rid)
    record["kind"] = kind
    record.setdefault("confidence", "unverified")
    if record["confidence"] not in {"unverified", "client-extracted", "community-observed", "confirmed-live"}:
        raise ValueError("invalid confidence")
    record.setdefault("collected_at", datetime.now(timezone.utc).isoformat())
    record["record_key"] = hashlib.sha256((kind + ":" + record["observed_build"] + ":" + record["id"] + ":" + record["source_url"]).encode()).hexdigest()[:20]
    return record

def load(path):
    if path.suffix.lower() == ".jsonl":
        with path.open(encoding="utf-8") as f:
            for line in f:
                if line.strip(): yield json.loads(line)
    elif path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8-sig") as f: yield from csv.DictReader(f)
    else:
        value = json.loads(path.read_text(encoding="utf-8"))
        yield from value if isinstance(value, list) else [value]

def main():
    p=argparse.ArgumentParser()
    p.add_argument("input", type=Path); p.add_argument("--kind", required=True, choices=sorted(KINDS))
    p.add_argument("--output", type=Path, required=True)
    a=p.parse_args(); records=[]; errors=[]
    for i, raw in enumerate(load(a.input), 1):
        try: records.append(normalize(raw, a.kind))
        except (ValueError, TypeError) as e: errors.append(f"record {i}: {e}")
    if errors: raise SystemExit("\n".join(errors))
    a.output.parent.mkdir(parents=True, exist_ok=True)
    with a.output.open("w", encoding="utf-8") as f:
        for record in records: f.write(json.dumps(record, ensure_ascii=False, sort_keys=True)+"\n")
    print(f"Imported {len(records)} {a.kind} records -> {a.output}")
if __name__ == "__main__": main()
