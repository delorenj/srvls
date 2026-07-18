# Provenance

- Frozen parent: `598eb0ccd0ad37a9432a2132a14d75aeea0f9f47`
- Parent architecture SHA-256:
  `5907c2f7da67378c6da60de0ed6374b9393d30b7945d271e6e261467ebce9392`
- Current normative architecture-body SHA-256 (every byte after the closing
  frontmatter delimiter, so lifecycle status metadata is excluded):
  `06df98f6d201abd47289d6c6771e15b83fb9d8a6c856a3a67e2e20e178a670aa`
- Capture date: 2026-07-17
- Authoring method: hand-authored independent architecture oracle with
  synthetic, non-secret IDs, paths, timestamps, hashes, process identities,
  unit names, D-Bus names, crash cuts, removal identities, and literal target
  and prior systemd unit-file content bytes. Complete transition envelopes and
  their checksum cascades were produced by a one-use deterministic scratch
  transformation over those hand-authored values, independently inspected,
  and frozen; the scratch helper is not corpus evidence and is not retained.
  The installed-prior additions independently freeze upgrade commit,
  replacement-owner upgrade, failed-upgrade recovery, and the forward,
  recovery, and explicit-rollback FD4 generation roles.
- Product encoder used: none
- Mutable Host capture used for golden bytes: only
  `brownfield-consumer-pairs.json`, whose four source fragment hashes and
  manager-normalized service/timer values were read from the live big-chungus
  user manager on 2026-07-17. The sole byte normalization replaces the literal
  `/home/delorenj` prefix with `/home/test`; candidate contracts then replace
  only the deployed srvls executable path with `/home/test/.local/bin/srvls`.
  The validator reverses that one home substitution on each normalized source
  service/timer fragment and recomputes every listed Host fragment SHA-256;
  basis hashes are therefore derived from the checked-in source bytes rather
  than accepted as free-standing metadata.
  Transaction histories and every other golden remain synthetic and use no
  mutable Host capture.
- Volatile substitutions in golden bytes: none; every synthetic value is
  literal

Primary semantics were reality-checked against:

- Linux man-pages 6.18 `fcntl_locking(2)`: traditional process-associated
  `F_SETLK`/`F_SETLKW` locks, `[0,1)` byte range semantics, `F_GETLK` owner and
  conflicting-type reporting, automatic release on owner termination,
  non-inheritance across `fork`, and owner-side close hazards.
- Linux man-pages 6.18 `fork(2)`: process-associated locks are not inherited;
  OFD and `flock` locks are inherited.
- systemd v257 `org.freedesktop.systemd1` XML: Manager `Subscribe()` enables
  most signals and JobNew/JobRemoved require subscription by at least one
  client. The pending-job recovery trace therefore records a fresh connection,
  exact owner/match installation, successful `Subscribe`, owner recheck, queue
  drain, and only then `ListJobs`/`JobRemoved` recovery.

CanonicalJsonV1 and uppercase-percent bytes are checked by the shared
`../canonical_json_v1.py` implementation and adversarial vectors. Release
envelopes then receive independent schema and cross-record validation for every
nested owner, deadline, admission, D-Bus/timer record, evidence atom, terminal
generation, and chronological boundary; a valid checksum is never semantic
proof by itself.

`validate_oracles.py` additionally performs an ephemeral Linux semantic proof
on an anonymous regular `memfd`. Its expected lock types, owner relationship,
stopped-child state, inherited-descriptor presence, owner-death release, and
contender success are fixed assertions. Runtime PIDs and anonymous inode values
are never written back into the corpus and never become golden bytes.

The validator also performs two live ActionExecutor handoff proofs with
anonymous lock, admission, and marker `memfd` objects. Runtime PIDs and inode
values are not golden bytes. The
negative control changes admission generation between submitter death and late
executor lease acquisition and requires refusal before mutation. The positive
control proves overlapping submitter/executor shared leases, exclusion of the
release writer after submitter death, exact marker readback, and writer
acquisition only after executor unlock.

`stable-toolchain-evidence.json` was authored from the freshly fetched official
`channel-rust-stable.toml` dated 2026-07-16 and the official
`rustc-1.97.1-x86_64-unknown-linux-gnu.tar.xz`. The archive SHA-256 was verified
as `9819d0a32d56bd339585319c80260e332779f5541fd66838ab7e016d6c814819`
before executing that isolated compiler to capture its complete verbose
identity. It is toolchain evidence, not a product artifact or ABI proof; exact
candidate `readelf` and oldest-runtime smoke evidence remains a release-CI
acceptance requirement once a Rust binary exists.

The fixed SHA-256 domains are the literal ASCII token, one zero byte, then the
declared CanonicalJsonV1 preimage. `SHA256SUMS` covers repository file bytes,
including the single terminal line feed. The validator recalculates both
layers independently and rejects every unlisted file.

Fragment and drop-in content uses the AD-24 uppercase-percent raw-byte
encoding. Target and prior content was authored directly in this corpus, not
captured or rendered by product code. The validator decodes those bytes with a
separate standard-library implementation, rejects alternate encodings,
recomputes decoded sizes and ordinary file SHA-256 values, then carries the
result through consumer-contract, KnownGood candidate, commit-decision,
publication-evidence, installed-bundle, KnownGood publication, predecessor,
and outer transaction hashes. Its negative-oracle copies are ephemeral and
never written back into the corpus.

Explicit rollback evidence was authored directionally rather than derived from
the staged target: the restore precondition names the generation-8 displaced
source contract, the restore postcondition names the generation-7 retained
target, and reload plus restored-pair validation continue to name generation 7.
Ephemeral negative copies exercise same, swapped, unknown, reload-source, and
validation-source hashes; none is written into the golden corpus.

Installed upgrade evidence is directional as well: forward consumer rewrite
binds generation-7 source before generation-8 target, while failed-upgrade
restore binds generation-8 target before generation-7 source and keeps reload,
timer, and FD4 validation on restored generation 7. FD4 standalone pairs bind
forward `0 -> 1`, upgrade `7 -> 8`, recovery `7 -> 7`, and explicit rollback
`8 -> 7` to exact pending transition checksums. FirstInstall recovery contains
four separate skipped/no-prior revisions before its real restore path. All
negative copies and the positive synthetic two-pair FirstInstall expansion are
ephemeral and never written back into corpus authority.
