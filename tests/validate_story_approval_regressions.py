#!/usr/bin/env python3
"""Mutation-style regression checks for fail-closed Story transitions."""

from __future__ import annotations

import importlib.util
import hashlib
import json
import os
import subprocess
import tempfile
import xml.etree.ElementTree as ET
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
code_review = (ROOT / "_bmad/bmm/workflows/4-implementation/code-review/instructions.xml").read_text()
sprint_status = (ROOT / "_bmad/bmm/workflows/4-implementation/sprint-status/instructions.md").read_text()
require(create.index("validate_story_fixture_approvals.py") < create.index("template-output"),
        "create-story writes before approval")
ET.parse(ROOT / "_bmad/bmm/workflows/4-implementation/create-story/instructions.xml")
ET.parse(ROOT / "_bmad/bmm/workflows/4-implementation/dev-story/instructions.xml")
ET.parse(ROOT / "_bmad/bmm/workflows/4-implementation/code-review/instructions.xml")
require(create.count("validate_story_fixture_approvals.py") >= 5,
        "not every create-story selection branch has a C-23 preflight")
require("<action>HALT</action>" in create and "<action>HALT</action>" in dev,
        "workflow nonzero transition lacks HALT")
require("C-23 validity dominates preservation" in sprint,
        "sprint preservation can bypass approval")
require("--complete {{story_id}}" in code_review and "HALT on non-zero" in code_review,
        "code-review completion transition bypasses provenance")
require("--complete &lt;story_id&gt;" in sprint_status,
        "sprint-status correction bypasses completion provenance")


def hermetic_git_gate() -> None:
    """Execute one valid approval/completion/dependency chain, then mutate it."""
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)

        def commit(message: str, email: str) -> str:
            env = os.environ | {
                "GIT_AUTHOR_NAME": email, "GIT_AUTHOR_EMAIL": email,
                "GIT_COMMITTER_NAME": email, "GIT_COMMITTER_EMAIL": email,
            }
            subprocess.run(["git", "add", "-A"], cwd=root, check=True, env=env)
            subprocess.run(["git", "commit", "-q", "--allow-empty", "-m", message], cwd=root, check=True, env=env)
            return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()

        planning = root / "_bmad-output/planning-artifacts"
        approvals = root / "_bmad-output/implementation-artifacts/fixture-approvals"
        oracle = root / "tests/fixtures/story-v1"; oracle2 = root / "tests/fixtures/story-v2"
        planning.mkdir(parents=True); approvals.mkdir(parents=True); oracle.mkdir(parents=True); oracle2.mkdir(parents=True)
        (planning / "epics.md").write_text(
            "### Story 1.1: First\n**Dependencies:** None.\n"
            "**Validation Expectations:** The owning oracles are tests/fixtures/story-v1 and tests/fixtures/story-v2.\n\n"
            "### Story 1.2: Second\n**Dependencies:** Story 1.1.\n"
            "**Validation Expectations:** The owning oracle is tests/fixtures/story-v1.\n"
        )
        fixture = oracle / "input"; expected = oracle / "expected"
        fixture.write_bytes(b"input"); expected.write_bytes(b"expected")
        (oracle2 / "input").write_bytes(b"input"); (oracle2 / "expected").write_bytes(b"expected")
        runner_bytes = b"#!/bin/sh\nsed 's/input/expected/' \"$1\""
        (oracle / "runner").write_bytes(runner_bytes); (oracle2 / "runner").write_bytes(runner_bytes)
        (oracle / "runner").chmod(0o755); (oracle2 / "runner").chmod(0o755)
        fixture_commit = commit("fixtures", "fixture@example.test")
        reviewer_commit = commit("review evidence", "reviewer@example.test")
        rows = {
            f"AC-{story}-{kind}": {"storyId": story, "criterionSha256": hashlib.sha256(f"{story}-{kind}".encode()).hexdigest()}
            for story in ("1.1", "1.2") for kind in ("P01", "N01")
        }
        approval.ROOT, approval.EPICS, approval.APPROVALS = root, planning / "epics.md", approvals

        def approval_payload(story: str) -> dict[str, object]:
            return {
                "schema": "srvls-fixture-approval-v1", "storyId": story,
                "rowIds": [f"AC-{story}-P01", f"AC-{story}-N01"],
                "criterionSha256": [rows[f"AC-{story}-P01"]["criterionSha256"], rows[f"AC-{story}-N01"]["criterionSha256"]],
                "oracleBindings": [{
                    "oraclePath": path, "fixturePath": f"{path}/input",
                    "fixtureSha256": hashlib.sha256(b"input").hexdigest(),
                    "runnerPath": f"{path}/runner", "runnerSha256": hashlib.sha256(runner_bytes).hexdigest(),
                    "expectedResultPath": f"{path}/expected",
                    "expectedResultSha256": hashlib.sha256(b"expected").hexdigest(),
                } for path in approval.declared_oracles(story)],
                "reviewerCommit": reviewer_commit, "fixtureAuthorCommit": fixture_commit, "verdict": "approved",
            }

        (approvals / "1.1-v1.json").write_text(json.dumps(approval_payload("1.1")))
        approval_commit = commit("approve 1.1", "reviewer@example.test")
        (root / "implementation").write_text("done")
        (oracle / "actual").write_bytes(b"expected"); (oracle2 / "actual").write_bytes(b"expected")
        implementation_commit = commit("implement 1.1", "implementer@example.test")
        (approvals / "1.1-completed-v1.json").write_text(json.dumps({
            "schema": "srvls-story-completion-v1", "storyId": "1.1", "approvalCommit": approval_commit,
            "implementationCommit": implementation_commit,
            "oracleResults": [{
                "oraclePath": path, "exitCode": 0,
                "resultPath": f"{path}/actual", "resultSha256": hashlib.sha256(b"expected").hexdigest(),
            } for path in approval.declared_oracles("1.1")],
            "verdict": "completed",
        }))
        completion_commit = commit("complete 1.1", "reviewer@example.test")
        require(approval.validate_completion("1.1", rows) == completion_commit, "valid completion rejected")
        (approvals / "1.2-v1.json").write_text(json.dumps(approval_payload("1.2")))
        commit("approve 1.2", "reviewer@example.test")
        approval.validate_assignment("1.2", rows)
        same_principal_commit = commit("second fixture-principal commit", "fixture@example.test")
        same_principal = json.loads((approvals / "1.2-v1.json").read_text())
        same_principal["reviewerCommit"] = same_principal_commit
        (approvals / "1.2-v1.json").write_text(json.dumps(same_principal))
        commit("same principal attack", "fixture@example.test")
        try:
            approval.validate_assignment("1.2", rows)
        except SystemExit:
            pass
        else:
            require(False, "same-principal fixture/reviewer attack escaped")
        baseline_completion = json.loads((approvals / "1.1-completed-v1.json").read_text())
        escaped = json.loads(json.dumps(baseline_completion))
        escaped["oracleResults"][0]["resultPath"] = "implementation"
        (approvals / "1.1-completed-v1.json").write_text(json.dumps(escaped))
        commit("result escape attack", "reviewer@example.test")
        try:
            approval.validate_completion("1.1", rows)
        except SystemExit:
            pass
        else:
            require(False, "result-path oracle escape escaped")
        (approvals / "1.1-completed-v1.json").write_text(json.dumps(baseline_completion))
        commit("restore completion", "reviewer@example.test")
        bad_execution = json.loads(json.dumps(baseline_completion))
        bad_execution["oracleResults"][0]["exitCode"] = 1
        (approvals / "1.1-completed-v1.json").write_text(json.dumps(bad_execution))
        commit("false execution attack", "reviewer@example.test")
        try:
            approval.validate_completion("1.1", rows)
        except SystemExit:
            pass
        else:
            require(False, "false runner exit attestation escaped")
        (approvals / "1.1-completed-v1.json").write_text(json.dumps(baseline_completion))
        commit("restore execution", "reviewer@example.test")
        mutated = json.loads((approvals / "1.1-completed-v1.json").read_text())
        mutated["implementationCommit"] = mutated["approvalCommit"]
        (approvals / "1.1-completed-v1.json").write_text(json.dumps(mutated))
        commit("mutate false completion", "reviewer@example.test")
        try:
            approval.validate_completion("1.1", rows)
        except SystemExit:
            pass
        else:
            require(False, "zero-change completion mutation escaped")
        env = os.environ | {
            "GIT_AUTHOR_NAME": "spoof", "GIT_AUTHOR_EMAIL": "spoof@example.test",
            "GIT_COMMITTER_NAME": "fixture", "GIT_COMMITTER_EMAIL": "fixture@example.test",
        }
        subprocess.run(["git", "commit", "-q", "--allow-empty", "-m", "identity mismatch"], cwd=root, check=True, env=env)
        mismatch = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
        try:
            approval.principal_email(mismatch)
        except SystemExit:
            pass
        else:
            require(False, "author/committer identity mismatch escaped")


hermetic_git_gate()
print("story approval regression mutations: PASS")
