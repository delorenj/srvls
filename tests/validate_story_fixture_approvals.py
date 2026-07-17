#!/usr/bin/env python3
"""Fail closed before assigning a canonical story without C-23 approval."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EPICS = ROOT / "_bmad-output/planning-artifacts/epics.md"
APPROVALS = ROOT / "_bmad-output/implementation-artifacts/fixture-approvals"
STORY = re.compile(r"^\d+\.\d+$")
SHA = re.compile(r"^[0-9a-f]{64}$")


def fail(message: str) -> None:
    raise SystemExit(f"story fixture approval validation failed: {message}")


def validate(story: str) -> None:
    if not STORY.fullmatch(story):
        fail(f"invalid story id {story!r}")
    path = APPROVALS / f"{story}-v1.md"
    if not path.is_file():
        fail(f"Story {story} has no C-23 approval artifact")
    body = path.read_text(encoding="utf-8")
    required = [
        "verdict: approved",
        f"AC-{story}-P01",
        f"AC-{story}-N01",
        "fixtureSha256:",
        "expectedResultSha256:",
        "reviewer:",
        "fixtureAuthor:",
        "implementationCommit:",
    ]
    if any(token not in body for token in required):
        fail(f"Story {story} approval schema is incomplete")
    hashes = re.findall(r"(?:fixtureSha256|expectedResultSha256):\s*([0-9a-f]+)", body)
    if len(hashes) != 2 or any(not SHA.fullmatch(value) for value in hashes):
        fail(f"Story {story} approval hashes are invalid")
    reviewer = re.search(r"reviewer:\s*(\S+)", body).group(1)
    author = re.search(r"fixtureAuthor:\s*(\S+)", body).group(1)
    if reviewer == author:
        fail(f"Story {story} reviewer and fixture author are not independent")
    approval_commit = subprocess.check_output(
        ["git", "log", "-1", "--format=%H", "--", str(path)], cwd=ROOT, text=True
    ).strip()
    implementation = re.search(r"implementationCommit:\s*(\S+)", body).group(1)
    if implementation != "pending" and approval_commit == implementation:
        fail(f"Story {story} approval and implementation share one commit")
    print(f"Story {story} fixture approval: PASS ({approval_commit})")


def main() -> None:
    epics = EPICS.read_text(encoding="utf-8")
    if "Contract C-23: Acceptance Row Identity and Independent Approval" not in epics:
        fail("canonical backlog omits C-23")
    if len(sys.argv) == 1:
        print("story fixture approval enforcement: PASS (invoke with Story ID before assignment)")
        return
    for story in sys.argv[1:]:
        validate(story)


if __name__ == "__main__":
    main()
