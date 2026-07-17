#!/usr/bin/env python3
"""Mutation-style regression checks for fail-closed Story transitions."""

from __future__ import annotations

import importlib.util
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("approval", ROOT / "tests/validate_story_fixture_approvals.py")
assert SPEC and SPEC.loader
approval = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(approval)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"story approval regression failed: {message}")


def rejected(*args: str, contains: str) -> None:
    result = subprocess.run(
        ["python3", "tests/validate_story_fixture_approvals.py", *args],
        cwd=ROOT, text=True, capture_output=True,
    )
    require(result.returncode != 0 and contains in result.stderr + result.stdout,
            f"mutation {args!r} did not fail closed with {contains!r}")


rows = approval.canonical_rows()
require(len(rows) == 150, "registry cardinality mutation escaped")
require(len(approval.declared_oracles("6.7")) == 2, "Story 6.7 lost an oracle binding")
require(len(approval.declared_oracles("7.12")) == 2, "Story 7.12 lost an oracle binding")
require(not approval.within_oracle("tests/fixtures/unrelated", approval.declared_oracles("6.7")[0]),
        "wrong-oracle mutation escaped")
rejected("not-a-story", contains="invalid Story ID")
rejected("1.1", contains="has no C-23 approval")
rejected("--complete", "1.1", contains="has no completion provenance")

create = (ROOT / "_bmad/bmm/workflows/4-implementation/create-story/instructions.xml").read_text()
dev = (ROOT / "_bmad/bmm/workflows/4-implementation/dev-story/instructions.xml").read_text()
sprint = (ROOT / "_bmad/bmm/workflows/4-implementation/sprint-planning/instructions.md").read_text()
require(create.index("validate_story_fixture_approvals.py") < create.index("template-output"),
        "create-story writes before approval")
require("<action>HALT</action>" in create and "<action>HALT</action>" in dev,
        "workflow nonzero transition lacks HALT")
require("C-23 validity dominates preservation" in sprint,
        "sprint preservation can bypass approval")
print("story approval regression mutations: PASS")
