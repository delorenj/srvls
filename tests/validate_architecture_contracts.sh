#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "$repo_root"

export PYTHONDONTWRITEBYTECODE=1

bash tests/compat/validate.sh
python3 tests/validate_planning_quarantine.py
python3 tests/validate_story_fixture_approvals.py
python3 tests/fixtures/contracts/validate.py
python3 tests/fixtures/contracts/release-transaction-v1/validate_oracles.py
bash tests/test_smoke.sh

if [[ -f Cargo.toml ]]; then
  if [[ ! -f tests/architecture_boundaries.rs ]]; then
    printf '%s\n' \
      'architecture contract gate: Rust crate exists without tests/architecture_boundaries.rs' >&2
    exit 1
  fi
  cargo test --locked --all-targets
fi

printf '%s\n' 'architecture contract gate: PASS'
