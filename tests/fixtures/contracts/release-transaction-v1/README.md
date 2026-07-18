# Release transaction v1 oracle

This directory is the independent fixed oracle for the AD-23 release authority.
It is assertion input, not output from a Rust or Python `srvls` encoder.

The eleven `*.manifest.json` files are complete `UpgradeTransactionV1`
envelopes at these cuts:

- initial transaction creation with no current step, step record, or event;
- recovery-owner takeover with candidate validation pending;
- first-install prior absence with typed consumer removal pending;
- irreversible commit decision complete;
- KnownGood publication pending and complete;
- ready admission pending; and
- explicit rollback with restored ready admission pending;
- installed-prior upgrade with ready admission pending;
- installed-prior replacement-owner validation pending; and
- installed-prior failure recovery with restored-pair validation pending.

The initial envelope freezes the `current_step=absent` representation. Every
other envelope freezes a present `ReleaseStepCursorV1` containing the final
record's sequence, step, and effect attempt. The first-install
cut records regular fragments and drop-ins with their expected SHA-256 values,
enablement links with exact raw `readlink` targets, and drop-in directory prior
state. The `drop_in_directories` v1 field covers every transaction-created
drop-in and enablement-link parent, including `.wants` and `.requires`. Its
pending step carries byte-equal file, link, and directory evidence before any
unlink or permitted directory prune. The first-install cut exercises both
closed parent states: an absent-prior parent may be pruned after its children,
while a directory-prior parent must remain a nonsymlink directory.

Every `ManagedConsumerUnitContractV1` embeds the canonical uppercase-percent
content, decoded byte size, and raw-byte SHA-256 for both fragments and every
drop-in. The explicit-rollback cut deliberately uses semantically equivalent
but byte-distinct target and prior unit files, so the target can be created and
the prior generation can be restored without consulting the other generation,
loaded manager state, or an implementation-private template. Contract hashes
bind all content, sizes, and file hashes. First-install removal identities bind
their transaction target. Explicit rollback instead records the direction:
`restore-consumers` pre-effect evidence binds the displaced generation-8 source
contract and its post-effect evidence binds the restored generation-7 target;
rollback daemon-reload and restored-pair validation continue to bind that
generation-7 target. The retained installed prior release and staged KnownGood
candidate bind the distinct displaced source contract.

`admission-ready.json` and `admission-recovering.json` freeze both persisted
admission variants. `known-good-first-install.json` and
`known-good-installed.json` freeze both rollback-authority variants; the latter
publishes generation 8 while retaining adjacent installed generation 7.
`fd4-request.json`, `fd4-validated-result.json`, and
`fd4-rejected-result.json` freeze the FirstInstall forward exchange.
`fd4-upgrade-*`, `fd4-recovery-*`, and `fd4-rollback-*` freeze installed
forward `old -> target`, installed recovery `old -> old`, and explicit rollback
`old -> target` roles. Every request is cross-bound to one exact pending
envelope checksum, its persisted evidence UUID and active recovery owner,
directional binary/schema/generation authority, backup, and deadline; a
self-consistent but different or swapped role is rejected. Rejection codes are
the failure-capable subset of the closed ReleaseReasonV1 vocabulary.
`stable-toolchain-evidence.json` freezes the official 2026-07-16 stable
manifest, exact Rust 1.97.1 component archive hash, and complete independently
executed `rustc --version --verbose` identity. `brownfield-consumer-pairs.json`
freezes the normalized 2026-07-17 live user-systemd fragments and manager
properties for both metrics and Snapshot, candidate-path rewrites, sorted
two-pair effect order, and forward/rollback hashes. The full transition chains
use one synthetic metrics pair to isolate crash/recovery semantics; the
brownfield authority closes deployed-pair identity and direction without
claiming that those chains are multi-pair execution tests. For each pair the
candidate is the complete source contract with exactly the two canonical
encoded executable-path occurrences replaced, followed only by fragment size/
hash and contract-hash recomputation. Any other change—including a fully
rehashed `|| true`—fails.
`rollback-unavailable.result.json` freezes the no-transaction
FirstInstallAbsentV1 result. The four trace files freeze shared/exclusive lock
takeover, ActionExecutor handoff, user-bus subscription, and pending systemd-job
recovery barriers. The replacement job-recovery connection must install its
matches, bind the manager owner, successfully invoke `Manager.Subscribe`,
recheck that owner, drain, and only then consume `ListJobs`/`JobRemoved`; it
cannot inherit the vanished owner's subscription.

Each standalone JSON file is its exact canonical object plus one repository
line feed. Each JSONL line is one exact canonical object; each history file
ends with exactly one repository line feed. Those delimiters are not part of
CanonicalJsonV1 or any domain-separated checksum; they are included in
`SHA256SUMS`. The validator rejects any other whitespace, key order, duplicate
key, tagged-option shape, checksum, crash-cut state, semantic postcondition,
trace order, or file hash. It independently decodes canonical content,
recomputes byte sizes and SHA-256 values, recomputes every
consumer/candidate/decision/publication/transaction hash layer, and executes
negative mutations proving that hash-only fragments/drop-ins, mismatched
content/size/hash tuples, correctly rehashed content under a stale contract
hash, CanonicalJsonV1 and percent aliases, string-valued or reordered consumer/
FD4 scalars, stale toolchain identity, missing brownfield pairs, altered shell
behavior, impossible replacement-owner time, mismatched persisted deadlines,
wrong D-Bus paths or trigger units, open or cross-unbound path/artifact/backup/
candidate/decision objects, wrong step order/direction/evidence multiplicity,
embedded rollback-unavailable, wrong recovery terminal linkage, FirstInstall
plan/unit/generation drift, u64 overflow, swapped terminal generations, and
same, swapped, or wrong explicit-rollback directional hashes are rejected. A
separate positive mutation validates two complete FirstInstall service/timer
pairs, proving the schema is not hard-coded to the synthetic metrics pair.

The seven `*.transitions.jsonl` files are complete-envelope histories, not
patches. They freeze every revision from transaction creation through terminal
forward commit, replacement-owner commit, FirstInstall recovery, and explicit
rollback, plus installed-prior forward commit, installed-prior
replacement-owner commit, and failed-upgrade whole-pair recovery. FirstInstall
recovery records stage, checksum, smoke, and candidate validation as four
distinct durable `skipped/no-prior-release` revisions before its real absence
restore effects. Every nonzero revision points to the immediately preceding
payload checksum and appends exactly one event. Pending-to-terminal effects
therefore retain both start/resume and success/failure replacements. Named
crash-cut manifests are required to byte-equal their corresponding chain
envelope.

Installed rollback authorities retain the complete immutable state backup,
exact consumer content, tarball/toolchain hashes, generation, and bundle hash.
FirstInstall state with existing data starts as a deterministic
`StateBackupPlanV1` and may become `restore-recorded` only with a complete
matching backup manifest at the completed backup transition. Unit enablement
freezes both the one-unit mutation and exact readback; the corpus deliberately
uses D-Bus state for the service and raw `systemctl` stdout/status for the
timer.

The validator also executes an independent temp-free Linux reality proof for
both `F_RDLCK` and `F_WRLCK` on an anonymous regular `memfd`. A nested owner
acquires `[0,1)`, forks a child that
stops before its first file action while retaining the descriptor, and is
killed. The controller proves the owner/type with `F_GETLK`, confirms the child
is still stopped with the inherited descriptor, and acquires `F_WRLCK` without
waiting for that child. This test uses only the Python standard library and the
kernel; it imports no product code and derives no expected byte assertion from
an implementation.

A second temp-free live Linux proof uses anonymous lock, admission, and marker
`memfd` objects and covers both ActionExecutor handoff sides. Its
negative case stops the executor before lease acquisition, kills the submitter,
publishes a new admission generation under the exclusive lease, resumes the
executor, and proves refusal before marker mutation. Its positive case obtains
the executor's exact acknowledgement, kills the submitter, proves release stays
excluded while the executor mutates and reads back the marker, then admits the
exclusive contender only after the executor unlocks.

Run on Linux with procfs mounted:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 \
  tests/fixtures/contracts/release-transaction-v1/validate_oracles.py
```

Do not refresh these fixtures from an implementation. A contract change
requires a reviewed new schema version and new immutable oracle set.
