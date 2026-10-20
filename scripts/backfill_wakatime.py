#!/usr/bin/env python3
"""
Backfill historical coding heartbeats from Antigravity IDE transcripts into WakaTime.
"""

import os
import sys
import glob
import json
import re
import ssl
import time
import base64
import urllib.request
import urllib.error
from datetime import datetime

EXT_LANG_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".jsx": "JSX",
    ".ts": "TypeScript",
    ".tsx": "TSX",
    ".html": "HTML",
    ".htm": "HTML",
    ".css": "CSS",
    ".scss": "SCSS",
    ".json": "JSON",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".sh": "Bash",
    ".bash": "Bash",
    ".md": "Markdown",
    ".go": "Go",
    ".rs": "Rust",
    ".cpp": "C++",
    ".c": "C",
    ".h": "C",
    ".hpp": "C++",
    ".java": "Java",
    ".sql": "SQL",
    ".toml": "TOML",
    ".xml": "XML",
    ".dockerfile": "Docker",
}

def guess_language(file_path):
    base = os.path.basename(file_path)
    if base.lower() == "dockerfile":
        return "Docker"
    ext = os.path.splitext(file_path)[1].lower()
    return EXT_LANG_MAP.get(ext, "Text")

def guess_project(file_path):
    parts = file_path.split("/")
    if "Downloads" in parts:
        idx = parts.index("Downloads")
        if idx + 1 < len(parts):
            proj = parts[idx + 1]
            if not proj.startswith("."):
                return proj
    if len(parts) > 2:
        return parts[-2]
    return "Antigravity Workspace"

def get_api_key():
    key = os.environ.get("WAKATIME_API_KEY", "").strip()
    if not key:
        cfg_path = os.path.expanduser("~/.wakatime.cfg")
        if os.path.exists(cfg_path):
            with open(cfg_path, "r", encoding="utf-8") as f:
                for line in f:
                    if "api_key" in line and "=" in line:
                        key = line.split("=")[1].strip()
                        break
    return key

def collect_events_from_transcripts(brain_dir="~/.gemini/antigravity-ide/brain"):
    brain_dir = os.path.expanduser(brain_dir)
    pattern = os.path.join(brain_dir, "*", ".system_generated", "logs", "transcript.jsonl")
    transcript_files = glob.glob(pattern)
    print(f"Found {len(transcript_files)} Antigravity transcript files.")

    raw_events = []
    for tfile in transcript_files:
        try:
            with open(tfile, "r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    obj = json.loads(line)
                    created = obj.get("created_at")
                    if not created:
                        continue

                    # 1. Active Document
                    content = obj.get("content", "")
                    doc_match = re.search(r"Active Document:\s*([^\s\(\n]+)", content)
                    if doc_match:
                        fpath = doc_match.group(1).strip()
                        if "/" in fpath and not fpath.startswith("/tmp"):
                            raw_events.append((created, fpath, False))

                    # 2. Tool Calls
                    tool_calls = obj.get("tool_calls", [])
                    for tc in tool_calls:
                        args = tc.get("args", {})
                        for k in ["TargetFile", "AbsolutePath"]:
                            if k in args:
                                val = str(args[k]).strip("\"' ")
                                if "/" in val and not val.startswith("/tmp"):
                                    is_write = tc.get("name") in [
                                        "replace_file_content",
                                        "write_to_file",
                                        "multi_replace_file_content",
                                    ]
                                    raw_events.append((created, val, is_write))
        except Exception:
            continue

    print(f"Parsed {len(raw_events)} raw coding events from transcripts.")
    return raw_events

def deduplicate_heartbeats(raw_events, interval_seconds=120):
    """Group events into discrete heartbeat buckets (default 1 per 2 minutes per file)."""
    raw_events.sort(key=lambda x: x[0])
    buckets = {}

    for created, fpath, is_write in raw_events:
        try:
            # Handle ISO timestamps with Z or offset
            clean_ts = created.replace("Z", "+00:00")
            dt = datetime.fromisoformat(clean_ts)
            epoch = dt.timestamp()
            # Quantize by interval
            bucket_key = (int(epoch) // interval_seconds * interval_seconds, fpath)
            if bucket_key not in buckets:
                buckets[bucket_key] = {
                    "entity": fpath,
                    "type": "file",
                    "time": bucket_key[0],
                    "is_write": is_write,
                    "project": guess_project(fpath),
                    "language": guess_language(fpath),
                    "plugin": "Antigravity IDE/1.10 wakatime.vscode-wakatime/30.2.1",
                }
            elif is_write:
                buckets[bucket_key]["is_write"] = True
        except Exception:
            continue

    heartbeats = sorted(buckets.values(), key=lambda h: h["time"])
    print(f"Deduplicated to {len(heartbeats)} distinct heartbeats.")
    return heartbeats

def send_heartbeats_bulk(heartbeats, api_key, batch_size=50):
    ctx = ssl._create_unverified_context()
    auth_header = "Basic " + base64.b64encode(api_key.encode("utf-8")).decode("utf-8")
    url = "https://wakatime.com/api/v1/users/current/heartbeats.bulk"

    total = len(heartbeats)
    sent_count = 0

    print(f"Sending {total} heartbeats to WakaTime in batches of {batch_size}...")

    for i in range(0, total, batch_size):
        batch = heartbeats[i : i + batch_size]
        req = urllib.request.Request(
            url,
            data=json.dumps(batch).encode("utf-8"),
            headers={
                "Authorization": auth_header,
                "Content-Type": "application/json",
                "User-Agent": "wakatime/v1.104.0",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
                if resp.status in (200, 201, 202):
                    sent_count += len(batch)
                    pct = (sent_count / total) * 100
                    print(f"[{pct:5.1f}%] Synced {sent_count}/{total} heartbeats (Status: {resp.status})")
        except urllib.error.HTTPError as e:
            print(f"Batch {i//batch_size + 1} HTTP Error: {e.code} - {e.reason}")
        except Exception as e:
            print(f"Batch {i//batch_size + 1} Error: {e}")

        # Slight pause to avoid aggressive rate limiting
        time.sleep(0.15)

    print(f"Successfully processed {sent_count}/{total} heartbeats.")

def main():
    api_key = get_api_key()
    if not api_key:
        print("Error: No WakaTime API key found in env or ~/.wakatime.cfg", file=sys.stderr)
        sys.exit(1)

    print(f"Using WakaTime API key: {api_key[:8]}...{api_key[-4:]}")
    raw_events = collect_events_from_transcripts()
    if not raw_events:
        print("No events found to backfill.")
        return

    heartbeats = deduplicate_heartbeats(raw_events)
    estimated_hours = (len(heartbeats) * 2) / 60
    print(f"Estimated total coding time being backfilled: ~{estimated_hours:.1f} hours")

    send_heartbeats_bulk(heartbeats, api_key)
    print("Done! Heartbeats have been submitted to WakaTime.")

if __name__ == "__main__":
    main()
