#!/usr/bin/env python3
"""Read-only manifest of a locally installed Forever client. No game files copied."""
import argparse, hashlib, json
from pathlib import Path
from datetime import datetime, timezone

def main():
    p=argparse.ArgumentParser()
    p.add_argument("client", type=Path, help="Installed client folder, e.g. _classic_beta_")
    p.add_argument("--output", type=Path, default=Path("client-manifest.json"))
    p.add_argument("--hash", action="store_true", help="Hash small metadata files only")
    a=p.parse_args(); root=a.client.resolve()
    if not root.is_dir(): raise SystemExit("Client folder not found")
    if a.output.resolve().is_relative_to(root): raise SystemExit("Output must be outside game folder")
    files=[]
    for path in sorted(root.rglob("*")):
        if not path.is_file(): continue
        rel=path.relative_to(root).as_posix()
        if any(part.lower() in {"wtf","screenshots","logs"} for part in path.relative_to(root).parts): continue
        if path.suffix.lower() not in {".toc",".lua",".xml",".build.info",".db2"} and path.name not in {".build.info","WowB.exe"}: continue
        item={"path":rel,"size":path.stat().st_size}
        if a.hash and path.stat().st_size <= 1024*1024 and path.suffix.lower() in {".toc",".xml"}:
            item["sha256"]=hashlib.sha256(path.read_bytes()).hexdigest()
        files.append(item)
    output={"collected_at":datetime.now(timezone.utc).isoformat(),"source":"local authorized client","status":"metadata only","files":files}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(output,indent=2),encoding="utf-8")
    print(f"Indexed {len(files)} file paths; no client assets copied")
if __name__=="__main__": main()
