#!/usr/bin/env python3
"""Gate and atomically CAS one canonical sprint Story status."""

from __future__ import annotations

import fcntl
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALID = {"backlog", "ready-for-dev", "in-progress", "review", "done"}
EDGES = {
    ("backlog", "ready-for-dev"), ("ready-for-dev", "in-progress"),
    ("in-progress", "review"), ("review", "in-progress"), ("review", "done"),
    ("ready-for-dev", "backlog"), ("in-progress", "backlog"),
    ("review", "backlog"), ("done", "backlog"),
}


def fail(message: str) -> None:
    raise SystemExit(f"story status transition failed: {message}")


if len(sys.argv) != 6:
    fail("usage: STORY_ID STORY_KEY EXPECTED TARGET SPRINT_STATUS")
story_id, story_key, expected, target, raw_status = sys.argv[1:]
if not re.fullmatch(r"\d+\.\d+", story_id) or expected not in VALID or target not in VALID:
    fail("invalid Story ID or status")
if (expected, target) not in EDGES:
    fail(f"illegal Story status edge {expected} -> {target}")
status_path = Path(raw_status).resolve()
if ROOT not in status_path.parents or not status_path.is_file():
    fail("sprint status is missing or outside the repository")
lock_path = status_path.with_suffix(status_path.suffix + ".lock")
with lock_path.open("a+") as lock:
    fcntl.flock(lock, fcntl.LOCK_EX)
    head_before = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    commands = []
    if target != "backlog":
        commands.append(["python3", "tests/validate_story_fixture_approvals.py", story_id])
    if target in {"review", "done"}:
        commands.append(["python3", "tests/validate_story_fixture_approvals.py", "--complete", story_id])
    for command in commands:
        if subprocess.run(command, cwd=ROOT).returncode:
            fail(f"gate rejected {story_id} before {target}")
    if subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() != head_before:
        fail("repository HEAD changed during gated transition")
    body = status_path.read_text(encoding="utf-8")
    pattern = re.compile(rf"^(\s*{re.escape(story_key)}:\s*)(\S+)(\s*)$", re.MULTILINE)
    match = pattern.search(body)
    if not match or match.group(2) != expected:
        fail(f"CAS expected {story_key}={expected}")
    updated = body[:match.start()] + match.group(1) + target + match.group(3) + body[match.end():]
    descriptor, temporary = tempfile.mkstemp(prefix=status_path.name + ".", dir=status_path.parent)
    try:
        if subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() != head_before:
            fail("repository HEAD changed before atomic status replace")
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            stream.write(updated); stream.flush(); os.fsync(stream.fileno())
        os.replace(temporary, status_path)
        directory = os.open(status_path.parent, os.O_RDONLY)
        try:
            try: os.fsync(directory)
            except OSError: pass  # replace already committed; report success and recover by ordinary next read
        finally: os.close(directory)
    finally:
        if os.path.exists(temporary): os.unlink(temporary)
try: print(f"story status transition: PASS ({story_key}: {expected} -> {target})")
except BrokenPipeError: pass
