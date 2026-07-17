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
OID = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")
APPROVAL_KEYS = {
    "schema", "storyId", "rowIds", "oracleBindings", "reviewerCommit",
    "fixtureAuthorCommit", "criterionSha256", "verdict",
}
BINDING_KEYS = {"oraclePath", "fixturePath", "fixtureSha256", "expectedResultPath", "expectedResultSha256"}
COMPLETION_KEYS = {"schema", "storyId", "approvalCommit", "implementationCommit", "oracleResults", "verdict"}
RESULT_KEYS = {"oraclePath", "runnerPath", "runnerSha256", "exitCode", "resultPath", "resultSha256"}


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
    if data["sourceArtifact"] != "_bmad-output/planning-artifacts/epics.md":
        fail("acceptance registry sourceArtifact mismatch")
    rows = {row["rowId"]: row for row in data["rows"]}
    epics = EPICS.read_text(encoding="utf-8")
    stories = re.findall(r"^### Story (\d+\.\d+):", epics, re.MULTILINE)
    expected_ids = {f"AC-{story}-{kind}" for story in stories for kind in ("P01", "N01")}
    if len(stories) != 75 or data["rowCount"] != 150 or set(rows) != expected_ids:
        fail("acceptance registry must contain the exact P01/N01 rows for 75 canonical stories")
    for row_id, row in rows.items():
        if set(row) != {"rowId", "storyId", "kind", "criterionMarkdown", "criterionSha256"}:
            fail(f"{row_id} has unknown or missing keys")
        match = re.fullmatch(r"AC-(\d+\.\d+)-(P01|N01)", row_id)
        expected_kind = "positive" if match and match.group(2) == "P01" else "negative"
        if not match or row["storyId"] != match.group(1) or row["kind"] != expected_kind:
            fail(f"{row_id} identity metadata is inconsistent")
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


def committer_email(commit: str) -> str:
    return git("show", "-s", "--format=%ce", commit)


def principal_email(commit: str) -> str:
    author, committer = author_email(commit), committer_email(commit)
    if author != committer:
        fail(f"commit {commit} has inconsistent author/committer identity")
    return committer


def git_file_hash(commit: str, path: str) -> str:
    try:
        content = subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)
    except subprocess.CalledProcessError:
        fail(f"{path} is absent from declared commit {commit}")
    return hashlib.sha256(content).hexdigest()


def git_path_exists(commit: str, path: str) -> bool:
    return subprocess.run(
        ["git", "cat-file", "-e", f"{commit}:{path}"], cwd=ROOT,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    ).returncode == 0


def declared_oracles(story: str) -> list[str]:
    text = EPICS.read_text(encoding="utf-8")
    section = re.search(
        rf"^### Story {re.escape(story)}:.*?(?=^### Story |^## Epic |\Z)",
        text, re.MULTILINE | re.DOTALL,
    )
    if not section:
        fail(f"Story {story} section is missing")
    line = re.search(r"^\*\*Validation Expectations:\*\* (.*)$", section.group(), re.MULTILINE)
    oracles = re.findall(r"tests/[A-Za-z0-9_.\-/]+", line.group(1) if line else "")
    if not oracles:
        fail(f"Story {story} has no parseable owning oracle")
    return list(dict.fromkeys(path.rstrip(".,;`)'") for path in oracles))


def within_oracle(path: str, oracle: str) -> bool:
    return path == oracle or path.startswith(oracle.rstrip("/") + "/") or path.startswith(oracle + ".expected")


def validate_approval(story: str, rows: dict[str, dict[str, str]]) -> tuple[str, dict[str, object]]:
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
    expected_criteria = [rows[row_id]["criterionSha256"] for row_id in data["rowIds"]]
    if data["criterionSha256"] != expected_criteria:
        fail(f"Story {story} approval does not bind current criterion bytes")
    if data["verdict"] != "approved":
        fail(f"Story {story} is not approved")
    oracles = declared_oracles(story)
    bindings = data["oracleBindings"]
    if not isinstance(bindings, list) or [b.get("oraclePath") for b in bindings if isinstance(b, dict)] != oracles:
        fail(f"Story {story} must bind every declared oracle exactly once and in order")
    for binding in bindings:
        if set(binding) != BINDING_KEYS:
            fail(f"Story {story} oracle binding schema is invalid")
        oracle = binding["oraclePath"]
        for path_key, hash_key in (("fixturePath", "fixtureSha256"), ("expectedResultPath", "expectedResultSha256")):
            if not isinstance(binding[hash_key], str) or not SHA.fullmatch(binding[hash_key]):
                fail(f"Story {story} {hash_key} is invalid")
            if not within_oracle(binding[path_key], oracle):
                fail(f"Story {story} {path_key} is outside {oracle}")
            target = (ROOT / binding[path_key]).resolve()
            if not target.is_file() or ROOT not in target.parents:
                fail(f"Story {story} {path_key} is missing or outside the repository")
            if hashlib.sha256(target.read_bytes()).hexdigest() != binding[hash_key]:
                fail(f"Story {story} {hash_key} does not match repository bytes")
            committed_clean(target)
    approval_commit = committed_clean(path)
    commits = [data[k] for k in ("reviewerCommit", "fixtureAuthorCommit")]
    if any(not OID.fullmatch(value) for value in commits) or len(set(commits)) != 2:
        fail(f"Story {story} reviewer and fixture author commits are not distinct")
    for commit in commits + [approval_commit]:
        git("cat-file", "-e", f"{commit}^{{commit}}")
    if len({principal_email(commit) for commit in commits}) != 2:
        fail(f"Story {story} reviewer and fixture author Git committer identities are not distinct")
    if principal_email(approval_commit) != principal_email(data["reviewerCommit"]):
        fail(f"Story {story} approval commit is not committed by the declared reviewer")
    if any(subprocess.run(["git", "merge-base", "--is-ancestor", commit, approval_commit], cwd=ROOT).returncode for commit in commits):
        fail(f"Story {story} approval does not descend from its author and reviewer evidence")
    for binding in bindings:
        for path_key, hash_key in (("fixturePath", "fixtureSha256"), ("expectedResultPath", "expectedResultSha256")):
            if git_file_hash(data["fixtureAuthorCommit"], binding[path_key]) != binding[hash_key]:
                fail(f"Story {story} {path_key} bytes are not bound to fixtureAuthorCommit")
    return approval_commit, data


def validate_assignment(story: str, rows: dict[str, dict[str, str]]) -> None:
    approval_commit, _ = validate_approval(story, rows)
    for dependency in declared_dependencies(story):
        dependency_completion = validate_completion(dependency, rows)
        if subprocess.run(["git", "merge-base", "--is-ancestor", dependency_completion, approval_commit], cwd=ROOT).returncode:
            fail(f"Story {story} approval predates completed predecessor {dependency}")
    print(f"Story {story} fixture approval: PASS ({approval_commit})")


def validate_completion(story: str, rows: dict[str, dict[str, str]]) -> str:
    approval_path = APPROVALS / f"{story}-v1.json"
    completion_path = APPROVALS / f"{story}-completed-v1.json"
    if not completion_path.is_file():
        fail(f"Story {story} has no completion provenance")
    data = json.loads(completion_path.read_text(encoding="utf-8"))
    if set(data) != COMPLETION_KEYS or data["schema"] != "srvls-story-completion-v1" or data["storyId"] != story or data["verdict"] != "completed":
        fail(f"Story {story} completion schema is invalid")
    approval_commit, approval = validate_approval(story, rows)
    completion_commit = committed_clean(completion_path)
    if data["approvalCommit"] != approval_commit or not OID.fullmatch(data["implementationCommit"]):
        fail(f"Story {story} completion does not bind its approval and implementation")
    if len({approval_commit, data["implementationCommit"], completion_commit}) != 3:
        fail(f"Story {story} approval, implementation, and completion commits are not distinct")
    git("cat-file", "-e", f"{data['implementationCommit']}^{{commit}}")
    if subprocess.run(["git", "merge-base", "--is-ancestor", approval_commit, data["implementationCommit"]], cwd=ROOT).returncode:
        fail(f"Story {story} implementation does not descend from approval")
    if subprocess.run(["git", "merge-base", "--is-ancestor", data["implementationCommit"], completion_commit], cwd=ROOT).returncode:
        fail(f"Story {story} completion provenance does not descend from implementation")
    results = data["oracleResults"]
    bindings = approval["oracleBindings"]
    if not isinstance(results, list) or len(results) != len(bindings):
        fail(f"Story {story} completion must contain one result per oracle")
    for binding, result in zip(bindings, results, strict=True):
        if set(result) != RESULT_KEYS or result["oraclePath"] != binding["oraclePath"]:
            fail(f"Story {story} completion result binding is invalid")
        if result["exitCode"] != 0 or not within_oracle(result["runnerPath"], result["oraclePath"]):
            fail(f"Story {story} completion lacks an approved successful oracle runner")
        if git_file_hash(approval["fixtureAuthorCommit"], result["runnerPath"]) != result["runnerSha256"]:
            fail(f"Story {story} runner bytes are not fixture-author approved")
        if not within_oracle(result["resultPath"], result["oraclePath"]):
            fail(f"Story {story} executed result escapes its owning oracle")
        if git_path_exists(approval_commit, result["resultPath"]):
            fail(f"Story {story} executed result is not fresh implementation evidence")
        runner = (ROOT / result["runnerPath"]).resolve()
        fixture = (ROOT / binding["fixturePath"]).resolve()
        executed = subprocess.run([str(runner), str(fixture)], cwd=ROOT, capture_output=True)
        if executed.returncode != result["exitCode"] or hashlib.sha256(executed.stdout).hexdigest() != result["resultSha256"]:
            fail(f"Story {story} approved runner replay does not reproduce the attested result")
        if result["resultSha256"] != binding["expectedResultSha256"]:
            fail(f"Story {story} executed result differs from approved expectation")
        if git_file_hash(data["implementationCommit"], result["resultPath"]) != result["resultSha256"]:
            fail(f"Story {story} implementation commit lacks its executed result bytes")
    for binding in bindings:
        for path_key in ("fixturePath", "expectedResultPath"):
            relative = binding[path_key]
            if subprocess.run(["git", "diff", "--quiet", approval_commit, data["implementationCommit"], "--", relative], cwd=ROOT).returncode:
                fail(f"Story {story} implementation changed approved {path_key}")
    return completion_commit


def main() -> None:
    rows = canonical_rows()
    if len(sys.argv) == 1:
        print("story acceptance registry: PASS (75 stories, 150 canonical-criterion-bound rows)")
        return
    if sys.argv[1:2] == ["--complete"]:
        if len(sys.argv) != 3 or not STORY.fullmatch(sys.argv[2]):
            fail("--complete requires exactly one Story ID")
        commit = validate_completion(sys.argv[2], rows)
        print(f"Story {sys.argv[2]} completion provenance: PASS ({commit})")
        return
    for story in sys.argv[1:]:
        validate_assignment(story, rows)


if __name__ == "__main__":
    main()
