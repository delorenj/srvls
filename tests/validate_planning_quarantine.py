#!/usr/bin/env python3
"""Discover only canonical epics and quarantine the retired historical copy."""

from __future__ import annotations

import hashlib
from pathlib import Path
import re


REPO_ROOT = Path(__file__).resolve().parents[1]
PLANNING_ROOT = REPO_ROOT / "_bmad-output/planning-artifacts"
CANONICAL = PLANNING_ROOT / "epics.md"
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
    if not CANONICAL.is_file() or not ARCHIVE.is_file():
        fail("canonical or archived historical epics are missing")
    canonical = CANONICAL.read_text(encoding="utf-8")
    draft = all(token in canonical for token in (
        "status: remediated-draft", "assignable: false",
        "implementationAuthority: false"))
    final = all(token in canonical for token in (
        "status: final", "assignable: true", "implementationAuthority: true"))
    if not (draft or final):
        fail("canonical authority fields are not a permitted coherent state")
    if not ASSIGNABLE_HEADING.search(canonical):
        fail("canonical artifact contains no epic/story headings")
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
    if discovered != [CANONICAL]:
        fail("sprint planning does not discover exactly the canonical artifact")
    archive_bytes = ARCHIVE.read_bytes()
    if hashlib.sha256(archive_bytes).hexdigest() != ARCHIVE_SHA256:
        fail("archived historical epics no longer preserve the quarantined bytes")
    print(
        "planning discovery/quarantine: PASS "
        "(2 exact globs, 1 canonical artifact, 1 byte-exact retired archive)"
    )


if __name__ == "__main__":
    main()
