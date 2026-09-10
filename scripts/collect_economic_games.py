"""Download the economic-games reading list without running upstream code.

Usage: python3 scripts/collect_economic_games.py [--verify]
Each source has an independent record. Re-running preserves existing snapshots.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import hashlib
import json
import os
import subprocess
import urllib.request
from pathlib import Path

from collect import Extract

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "sources/economic-games"


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def fetch(url, target):
    if not target.exists():
        request = urllib.request.Request(url, headers={"User-Agent": "ResearchArchive/1.0"})
        with urllib.request.urlopen(request, timeout=55) as response:
            data, resolved = response.read(), response.url
        if target.suffix == ".pdf" and not data.startswith(b"%PDF"):
            raise ValueError("Response is not a PDF")
        target.write_bytes(data)
    else:
        data, resolved = target.read_bytes(), url
    return {"url": url, "resolved_url": resolved, "path": str(target.relative_to(ROOT)),
            "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def collect(item):
    folder = BASE / item["kind"] / item["id"]
    folder.mkdir(parents=True, exist_ok=True)
    record_path = folder / "record.json"
    if record_path.exists():
        previous = json.loads(record_path.read_text())
        if previous.get("status") == "ok":
            if previous.get("checkout") and not (ROOT / previous["checkout"] / ".git").exists():
                checkout = ROOT / previous["checkout"]
                subprocess.run(["git", "init", str(checkout)], check=True, capture_output=True)
                subprocess.run(["git", "-C", str(checkout), "remote", "add", "origin", item["url"] + ".git"],
                               check=True, capture_output=True)
                subprocess.run(["git", "-C", str(checkout), "fetch", "--depth", "1", "origin", previous["commit"]],
                               check=True, capture_output=True, timeout=240,
                               env={**os.environ, "GIT_TERMINAL_PROMPT": "0"})
                subprocess.run(["git", "-C", str(checkout), "checkout", "--detach", "FETCH_HEAD"],
                               check=True, capture_output=True,
                               env={**os.environ, "GIT_LFS_SKIP_SMUDGE": "1"})
            return previous
    record = {**item, "retrieved_at": now(), "artifacts": [], "status": "ok"}
    try:
        if item["kind"] == "repositories":
            checkout = folder / "checkout"
            if not (checkout / ".git").exists():
                subprocess.run(
                    ["git", "clone", "--depth", "1", item["url"] + ".git", str(checkout)],
                    check=True, capture_output=True, text=True, timeout=240,
                    env={**os.environ, "GIT_TERMINAL_PROMPT": "0", "GIT_LFS_SKIP_SMUDGE": "1"},
                )
            def git(*args):
                return subprocess.check_output(["git", "-C", str(checkout), *args], text=True).strip()
            record.update(commit=git("rev-parse", "HEAD"), commit_date=git("show", "-s", "--format=%cI"),
                          checkout=str(checkout.relative_to(ROOT)), experiments_reproduced=False)
            record["license_files"] = [str(p.relative_to(checkout)) for p in checkout.iterdir()
                                       if p.is_file() and p.name.lower().startswith(("license", "copying"))]
            for path in checkout.iterdir():
                if path.is_file() and path.name.lower().startswith(("readme", "license", "copying")):
                    target = folder / path.name
                    target.write_bytes(path.read_bytes())
                    record["artifacts"].append(fetch(item["url"] + "/blob/" + record["commit"] + "/" + path.name, target))
        else:
            for name, url in [("page.html", item.get("page_url")), ("paper.pdf", item.get("pdf_url"))]:
                if not url:
                    continue
                try:
                    target = folder / name
                    record["artifacts"].append(fetch(url, target))
                    if name.endswith("html"):
                        parser = Extract()
                        parser.feed(target.read_text(errors="replace"))
                        (folder / "page.txt").write_text(parser.text())
                        record["metadata"] = parser.meta
                    else:
                        subprocess.run(["pdftotext", "-layout", str(target), str(folder / "paper.txt")],
                                       check=True, capture_output=True, timeout=60)
                        record["extracted_text_characters"] = len((folder / "paper.txt").read_text().strip())
                        record["text_searchable"] = record["extracted_text_characters"] >= 200
                except Exception as error:
                    record.setdefault("errors", []).append({"url": url, "error": str(error)})
            if record.get("errors"):
                record["status"] = "partial" if record["artifacts"] else "failed"
    except Exception as error:
        record["status"] = "failed"
        record["error"] = str(error)
    record_path.write_text(json.dumps(record, indent=2) + "\n")
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    manifest_path = BASE / "manifest.json"
    if args.verify:
        manifest = json.loads(manifest_path.read_text())
        checked = 0
        for item in manifest["items"]:
            for artifact in item["artifacts"]:
                path = ROOT / artifact["path"]
                if hashlib.sha256(path.read_bytes()).hexdigest() != artifact["sha256"]:
                    raise ValueError(f"Checksum mismatch: {path}")
                checked += 1
            if item.get("checkout"):
                commit = subprocess.check_output(
                    ["git", "-C", str(ROOT / item["checkout"]), "rev-parse", "HEAD"], text=True).strip()
                if commit != item["commit"]:
                    raise ValueError(f"Commit mismatch: {item['id']}")
        print(f"Verified {checked} archived artifacts and all recorded repository commits.")
        return
    plan = json.loads((BASE / "collection-plan.json").read_text())
    records = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for record in pool.map(collect, plan["items"]):
            records.append(record)
            print(record["id"], record["status"], flush=True)
            manifest_path.write_text(json.dumps({"updated_at": now(), "items": records}, indent=2) + "\n")


if __name__ == "__main__":
    main()
