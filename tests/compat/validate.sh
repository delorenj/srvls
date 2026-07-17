#!/usr/bin/env bash
# Offline, read-only validation of frozen fixtures, goldens, and provenance.
set -euo pipefail

COMPAT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export LC_ALL=C
export TZ=UTC
export PYTHONDONTWRITEBYTECODE=1

exec python3 "$COMPAT_ROOT/replay_oracle.py" validate
