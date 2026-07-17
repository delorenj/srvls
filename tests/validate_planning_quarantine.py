#!/usr/bin/env python3
"""Fail closed when retired epics are discoverable as implementation stories."""

from __future__ import annotations

import hashlib
from pathlib import Path
import re


REPO_ROOT = Path(__file__).resolve().parents[1]
PLANNING_ROOT = REPO_ROOT / "_bmad-output/planning-artifacts"
TOMBSTONE = PLANNING_ROOT / "epics.md"
ARCHIVE = REPO_ROOT / "_bmad-output/retired-artifacts/epics-pre-canonical-prd-2026-07-15.md"
ARCHIVE_SHA256 = "9a256682785733c23fbf017c138115b067ec894fe8b697da75da134905d7effd"
ASSIGNABLE_HEADING = re.compile(r"^#{1,6}\s+(?:Epic|Story)(?:\s|$)", re.MULTILINE)
WORKFLOW = (
    REPO_ROOT
    / "_bmad/bmm/workflows/4-implementation/sprint-planning/workflow.yaml"
)
INSTRUCTIONS = WORKFLOW.with_name("instructions.md")
WHOLE_GLOB = "*epic*.md"
SHARDED_GLOB = "*epic*/*.md"


def fail(message: str) -> None:
    raise SystemExit(f"planning quarantine validation failed: {message}")


def discover_inputs() -> list[Path]:
    return sorted(
        {
            *PLANNING_ROOT.glob(WHOLE_GLOB),
            *PLANNING_ROOT.glob(SHARDED_GLOB),
        }
    )


def main() -> None:
    if not TOMBSTONE.is_file() or not ARCHIVE.is_file():
        fail("tombstone or archived historical epics are missing")
    tombstone = TOMBSTONE.read_text(encoding="utf-8")
    required = [
        "status: superseded",
        "assignable: false",
        "implementationAuthority: false",
        f"archivedArtifact: {ARCHIVE.relative_to(REPO_ROOT)}",
        f"archivedSha256: {ARCHIVE_SHA256}",
    ]
    if any(token not in tombstone for token in required):
        fail("planning-root tombstone does not fail closed")
    if ASSIGNABLE_HEADING.search(tombstone):
        fail("planning-root tombstone contains an assignable epic/story heading")
    workflow = WORKFLOW.read_text(encoding="utf-8")
    instructions = INSTRUCTIONS.read_text(encoding="utf-8")
    required_workflow_tokens = [
        'epics_pattern: "*epic*.md"',
        'whole: "{output_folder}/*epic*.md"',
        'sharded: "{output_folder}/*epic*/*.md"',
    ]
    if any(workflow.count(token) != 1 for token in required_workflow_tokens):
        fail("sprint-planning workflow differs from the exact discovery set")
    if "user-stories.md" not in instructions or "**No fuzzy aliases**" not in instructions:
        fail("sprint-planning instructions do not reject fuzzy story aliases")
    discovered = discover_inputs()
    if discovered != [TOMBSTONE]:
        fail("an epic artifact remains inside implementation-workflow discovery roots")
    archive_bytes = ARCHIVE.read_bytes()
    if hashlib.sha256(archive_bytes).hexdigest() != ARCHIVE_SHA256:
        fail("archived historical epics no longer preserve the quarantined bytes")
    print(
        "planning quarantine: PASS "
        "(2 exact discovery globs, 1 non-assignable tombstone, 1 byte-exact archive)"
    )


if __name__ == "__main__":
    main()
