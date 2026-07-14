#!/usr/bin/env bash
# Smoke test for srvls: every output mode runs, parses, and contains what it claims.
# Outputs are captured into variables and checked via herestrings — piping a
# large capture into `grep -q` would SIGPIPE the writer and trip pipefail.
set -euo pipefail

SRVLS="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/srvls"
fail() { echo "FAIL: $*" >&2; exit 1; }

[[ -x "$SRVLS" ]] || fail "$SRVLS is not executable"

# --json is valid JSON and a list; if items exist they are well-formed
# (a clean CI host may legitimately have zero items)
JSON="$("$SRVLS" --json)" || fail "--json exited non-zero"
python3 -m json.tool > /dev/null <<< "$JSON" || fail "--json is not valid JSON"
python3 -c '
import json, sys
items = json.load(sys.stdin)
assert isinstance(items, list), "expected a list"
if items:
    required = {"type", "name", "state", "schedule", "source", "detail"}
    missing = required - set(items[0])
    assert not missing, f"item missing keys: {missing}"
print(f"  --json: {len(items)} items")
' <<< "$JSON" || fail "--json items malformed"

# --prom exposes only the supported metric families. unit_problem is optional
# because a clean host may have no failed or unhealthy units.
PROM="$("$SRVLS" --prom)" || fail "--prom exited non-zero"
python3 -c '
import sys

allowed = {
    "srvls_items",
    "srvls_unit_problem",
    "srvls_loadavg",
    "srvls_collect_timestamp_seconds",
}
required = allowed - {"srvls_unit_problem"}
seen = set()
for line in sys.stdin:
    fields = line.split()
    if not fields:
        continue
    if fields[0] in {"#", "#HELP", "#TYPE"}:
        if len(fields) >= 3 and fields[1] in {"HELP", "TYPE"}:
            seen.add(fields[2])
        continue
    seen.add(fields[0].split("{", 1)[0])
unexpected = seen - allowed
missing = required - seen
assert not unexpected, f"unexpected metric families: {sorted(unexpected)}"
assert not missing, f"missing metric families: {sorted(missing)}"
' <<< "$PROM" || fail "--prom metric-family contract failed"
echo "  --prom: $(grep -c '^srvls_' <<< "$PROM") samples"

# --md renders a markdown snapshot with at least one section table
MD="$("$SRVLS" --md)" || fail "--md exited non-zero"
grep -q '^# Background Task Inventory' <<< "$MD" || fail "--md missing header"
grep -q '^| name | state | schedule | source |' <<< "$MD" || fail "--md missing table"
echo "  --md: ok"

# default table renders with a summary line
TABLE="$("$SRVLS")" || fail "table exited non-zero"
grep -qE '^[0-9]+ items' <<< "$TABLE" || fail "table missing summary line"
echo "  table: ok"

# read-only inspect on a real cron item exits 0 (skipped if host has none)
CRON_NAME="$(python3 -c '
import json, sys
for i in json.load(sys.stdin):
    if i["type"] == "cron":
        print(i["name"]); break
' <<< "$JSON")"
if [[ -n "$CRON_NAME" ]]; then
    "$SRVLS" inspect cron "$CRON_NAME" > /dev/null || fail "inspect cron $CRON_NAME exited non-zero"
    echo "  inspect cron $CRON_NAME: ok"
else
    echo "  inspect: skipped (no cron items on this host)"
fi

# hostile names must never reach a shell (regression for inspect() injection)
HOSTILE='x; echo INJECTED'
for t in pm2 docker usr-svc; do
    OUT="$("$SRVLS" inspect "$t" "$HOSTILE" 2>&1)" || fail "inspect $t hostile name exited non-zero"
    if grep -q '^INJECTED$' <<< "$OUT"; then
        fail "shell injection via inspect $t"
    fi
done
echo "  inspect hostile-name: no injection"

echo "PASS"
