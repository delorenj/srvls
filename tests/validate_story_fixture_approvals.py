#!/usr/bin/env python3
"""Validate canonical AC rows and fail closed before Story assignment."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EPICS = ROOT / "_bmad-output/planning-artifacts/epics.md"
REGISTRY = ROOT / "_bmad-output/planning-artifacts/story-acceptance-registry.json"
APPROVALS = ROOT / "_bmad-output/implementation-artifacts/fixture-approvals"
STORY = re.compile(r"^\d+\.\d+$")
SHA = re.compile(r"^[0-9a-f]{64}$")
APPROVAL_KEYS = {
    "schema", "storyId", "rowIds", "fixturePath", "fixtureSha256",
    "expectedResultPath", "expectedResultSha256", "reviewerCommit",
    "fixtureAuthorCommit", "implementerCommit", "verdict",
}


def fail(message: str) -> None:
    raise SystemExit(f"story fixture approval validation failed: {message}")


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def canonical_rows() -> dict[str, dict[str, str]]:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if set(data) != {"schema", "sourceArtifact", "rowCount", "rows"}:
        fail("acceptance registry has unknown or missing top-level keys")
    if data["schema"] != "srvls-story-acceptance-registry-v1":
        fail("acceptance registry schema mismatch")
    rows = {row["rowId"]: row for row in data["rows"]}
    if data["rowCount"] != 150 or len(rows) != 150:
        fail("acceptance registry must contain 150 unique rows")
    epics = EPICS.read_text(encoding="utf-8")
    for row_id, row in rows.items():
        if set(row) != {"rowId", "storyId", "kind", "criterionMarkdown", "criterionSha256"}:
            fail(f"{row_id} has unknown or missing keys")
        actual = hashlib.sha256(row["criterionMarkdown"].encode()).hexdigest()
        if actual != row["criterionSha256"] or row["criterionMarkdown"] not in epics:
            fail(f"{row_id} does not bind the canonical criterion bytes")
    return rows


def committed_clean(path: Path) -> str:
    relative = str(path.relative_to(ROOT))
    if subprocess.run(["git", "ls-files", "--error-unmatch", "--", relative], cwd=ROOT,
                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode:
        fail(f"{relative} is not tracked")
    if subprocess.run(["git", "diff", "--quiet", "--", relative], cwd=ROOT).returncode:
        fail(f"{relative} has uncommitted changes")
    if subprocess.run(["git", "diff", "--cached", "--quiet", "--", relative], cwd=ROOT).returncode:
        fail(f"{relative} has staged changes")
    commit = git("log", "-1", "--format=%H", "--", relative)
    if not commit:
        fail(f"{relative} is not committed")
    return commit


def declared_dependencies(story: str) -> list[str]:
    text = EPICS.read_text(encoding="utf-8")
    match = re.search(
        rf"^### Story {re.escape(story)}:.*?^\*\*Dependencies:\*\* (.*?)\.$",
        text, re.MULTILINE | re.DOTALL,
    )
    if not match:
        fail(f"Story {story} has no parseable dependency declaration")
    return re.findall(r"Story (\d+\.\d+)", match.group(1))


def author_email(commit: str) -> str:
    return git("show", "-s", "--format=%ae", commit)


def validate_assignment(story: str, rows: dict[str, dict[str, str]]) -> None:
    if not STORY.fullmatch(story):
        fail(f"invalid Story ID {story!r}")
    path = APPROVALS / f"{story}-v1.json"
    if not path.is_file():
        fail(f"Story {story} has no C-23 approval")
    data = json.loads(path.read_text(encoding="utf-8"))
    if set(data) != APPROVAL_KEYS or data["schema"] != "srvls-fixture-approval-v1":
        fail(f"Story {story} approval schema/keys are invalid")
    if data["storyId"] != story or data["rowIds"] != [f"AC-{story}-P01", f"AC-{story}-N01"]:
        fail(f"Story {story} approval row binding is invalid")
    if data["verdict"] != "approved":
        fail(f"Story {story} is not approved")
    for key in ("fixtureSha256", "expectedResultSha256"):
        if not SHA.fullmatch(data[key]):
            fail(f"Story {story} {key} is invalid")
    for path_key, hash_key in (("fixturePath", "fixtureSha256"), ("expectedResultPath", "expectedResultSha256")):
        target = (ROOT / data[path_key]).resolve()
        if not target.is_file() or ROOT not in target.parents:
            fail(f"Story {story} {path_key} is missing or outside the repository")
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != data[hash_key]:
            fail(f"Story {story} {hash_key} does not match repository bytes")
        committed_clean(target)
    approval_commit = committed_clean(path)
    commits = [data[k] for k in ("reviewerCommit", "fixtureAuthorCommit", "implementerCommit")]
    if any(not SHA.fullmatch(value) for value in commits) or len(set(commits)) != 3:
        fail(f"Story {story} identities are not three distinct Git commits")
    for commit in commits + [approval_commit]:
        git("cat-file", "-e", f"{commit}^{{commit}}")
    if len({author_email(commit) for commit in commits}) != 3:
        fail(f"Story {story} reviewer, fixture author, and implementer Git identities are not distinct")
    if subprocess.run(["git", "merge-base", "--is-ancestor", approval_commit, data["implementerCommit"]], cwd=ROOT).returncode:
        fail(f"Story {story} approval is not an ancestor of implementation")
    if rows[f"AC-{story}-P01"]["storyId"] != story:
        fail(f"Story {story} canonical row is missing")
    for dependency in declared_dependencies(story):
        dependency_path = APPROVALS / f"{dependency}-v1.json"
        if not dependency_path.is_file():
            fail(f"Story {story} predecessor {dependency} has no approval artifact")
        dependency_data = json.loads(dependency_path.read_text(encoding="utf-8"))
        dependency_commit = dependency_data.get("implementerCommit", "")
        if not SHA.fullmatch(dependency_commit):
            fail(f"Story {story} predecessor {dependency} has no valid implementation commit")
        if subprocess.run(
            ["git", "merge-base", "--is-ancestor", dependency_commit, data["implementerCommit"]],
            cwd=ROOT,
        ).returncode:
            fail(f"Story {story} predecessor {dependency} is not implemented first")
    print(f"Story {story} fixture approval: PASS ({approval_commit})")


def main() -> None:
    rows = canonical_rows()
    if len(sys.argv) == 1:
        print("story acceptance registry: PASS (75 stories, 150 byte-bound rows)")
        return
    for story in sys.argv[1:]:
        validate_assignment(story, rows)


if __name__ == "__main__":
    main()
