#!/usr/bin/env bash
# Archival capture helper. It deliberately refuses to write inside the repo.
set -euo pipefail

COMPAT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ $# -ne 1 ]]; then
  echo "usage: $0 OUTSIDE_REPOSITORY_CANDIDATE_DIRECTORY" >&2
  exit 64
fi

export LC_ALL=C
export TZ=UTC
export PYTHONDONTWRITEBYTECODE=1

python3 "$COMPAT_ROOT/replay_oracle.py" verify-source
python3 "$COMPAT_ROOT/replay_oracle.py" capture --output "$1"

echo "Candidate outputs only; do not copy them over frozen goldens without" >&2
echo "manual byte review, a compatibility-ledger entry, and new hashes." >&2
