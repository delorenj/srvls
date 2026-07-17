#!/usr/bin/env python3
"""Compute the frozen pass-3 substantive review digest without writing files."""

from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path


SCRIPT = Path(__file__).resolve()
REPO = next(
    candidate
    for candidate in (SCRIPT.parent, *SCRIPT.parents)
    if (candidate / ".git").exists()
)
SPINE = REPO / (
    "_bmad-output/planning-artifacts/architecture/"
    "architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md"
)

FIXED_REPO_FILES = (
    ".agents/skills/bmad-architecture/SKILL.md",
    ".agents/skills/bmad-architecture/customize.toml",
    ".agents/skills/bmad-architecture/references/headless.md",
    ".agents/skills/bmad-architecture/references/reviewer-gate.md",
    "README.md",
    "docs/architecture.md",
    "mise.toml",
    "srvls",
    "tests/test_smoke.sh",
    "tests/validate_architecture_contracts.sh",
    "tests/validate_planning_quarantine.py",
    "_bmad-output/planning-artifacts/epics.md",
    "_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md",
    "_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/addendum.md",
    "_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/DESIGN.md",
    "_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md",
    "_bmad/bmm/workflows/4-implementation/sprint-planning/instructions.md",
    "_bmad/bmm/workflows/4-implementation/sprint-planning/workflow.yaml",
)
REPO_TREES = (
    "_bmad-output/retired-artifacts",
    "tests/compat",
    "tests/fixtures/contracts",
)
EXTERNAL_FILES = (
    Path("/home/delorenj/code/srvls/AGENTS.md"),
)


def architecture_body() -> bytes:
    raw = SPINE.read_bytes()
    if not raw.startswith(b"---\n"):
        raise ValueError("architecture frontmatter start is missing")
    end = raw.find(b"\n---\n", 4)
    if end < 0:
        raise ValueError("architecture frontmatter terminator is missing")
    return raw[end + 5 :]


def iter_files() -> dict[str, Path]:
    selected: dict[str, Path] = {}
    for relative in FIXED_REPO_FILES:
        path = REPO / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        selected[relative] = path
    for relative_root in REPO_TREES:
        root = REPO / relative_root
        if not root.is_dir():
            raise FileNotFoundError(relative_root)
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            if "__pycache__" in path.parts or path.suffix == ".pyc":
                continue
            relative = path.relative_to(REPO).as_posix()
            selected[relative] = path
    for path in EXTERNAL_FILES:
        if not path.is_file():
            raise FileNotFoundError(path)
        selected[f"external:{path}"] = path
    return selected


def manifest() -> tuple[bytes, str, int]:
    body = architecture_body()
    body_hash = hashlib.sha256(body).hexdigest()
    rows = [
        f"{body_hash} mode=body "
        "_bmad-output/planning-artifacts/architecture/"
        "architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md#body\n"
    ]
    for label, path in sorted(iter_files().items()):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        mode = os.lstat(path).st_mode & 0o777
        rows.append(f"{digest} mode={mode:04o} {label}\n")
    rows.sort(key=lambda row: row.split(" ", 2)[2])
    return "".join(rows).encode("utf-8"), body_hash, len(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected")
    parser.add_argument("--manifest", action="store_true")
    args = parser.parse_args()

    data, body_hash, count = manifest()
    digest = hashlib.sha256(data).hexdigest()
    if args.manifest:
        print(data.decode("utf-8"), end="")
    print(f"substantive_digest={digest}")
    print(f"architecture_body_sha256={body_hash}")
    print(f"substantive_entries={count}")
    if args.expected is not None and digest != args.expected:
        print(f"expected={args.expected}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
