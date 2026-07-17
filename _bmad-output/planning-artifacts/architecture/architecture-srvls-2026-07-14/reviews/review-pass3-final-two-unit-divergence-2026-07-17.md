---
reviewer: SyntaxSorcerer
session: syntaxsorcerer-aegis-divergence-0717-r4
reviewed_digest: 04945fcb968eaba0d866f4c3bd9d0b5883a18fa8a28f1b82a8f70d7263981012
architecture_body_hash: 06df98f6d201abd47289d6c6771e15b83fb9d8a6c856a3a67e2e20e178a670aa
verdict: PASS
severity_counts:
  critical: 0
  high: 0
  medium: 0
  low: 0
  total: 0
---

# Pass-3 Two-Unit Implementation-Divergence Review

## Verdict

**PASS — 0 findings.**

I found no architecture-owned dimension in which two competent implementation units could obey the normative prose and still legally produce observably different contract bytes, persisted states, ordering, identities, deadlines, recovery outcomes, outputs, or side effects.

## Independence and Evidence Integrity

This was a fresh, independent, read-only adversarial review. I was not an author or remediator, made no repository changes, and did not consult historical or peer reports under the architecture `reviews/` tree.

The required verifier was executed exactly at both boundaries.

Start:

```text
substantive_digest=04945fcb968eaba0d866f4c3bd9d0b5883a18fa8a28f1b82a8f70d7263981012
architecture_body_sha256=06df98f6d201abd47289d6c6771e15b83fb9d8a6c856a3a67e2e20e178a670aa
substantive_entries=226
```

End:

```text
substantive_digest=04945fcb968eaba0d866f4c3bd9d0b5883a18fa8a28f1b82a8f70d7263981012
architecture_body_sha256=06df98f6d201abd47289d6c6771e15b83fb9d8a6c856a3a67e2e20e178a670aa
substantive_entries=226
```

The frozen evidence remained unchanged throughout the review.

## Review Basis

The review basis included:

- `/home/delorenj/code/srvls/AGENTS.md`
- Complete `bmad-architecture` skill
- Complete `references/headless.md`
- Complete `references/reviewer-gate.md`
- Complete 3,332-line architecture spine
- Canonical PRD and addendum
- Canonical `DESIGN.md` and `EXPERIENCE.md`
- Current brownfield `srvls` implementation
- Normative project documentation
- Frozen compatibility fixtures, goldens, manifest, ledger, checksums, and replay implementation
- Planning quarantine, canonical epics, retired tombstone, and discovery validator
- Top aggregate contract gate
- Contract fixtures and validator implementation
- Canonical JSON and percent/path codec implementation
- Complete release/recovery corpus, provenance, checksums, traces, manifests, seven transition chains, and the 5,069-line semantic validator
- Representative positive authorities and checksum-resealed negative mutations
- Future Rust implementation boundary, toolchain identity, MSRV/current-stable split, and brownfield replacement constraints

## Command and Gate Results

| Gate | Result |
|---|---|
| Required start digest verification | PASS |
| `tests/validate_architecture_contracts.sh` | PASS |
| Compatibility replay | PASS: providers, outputs, CLI, inspection, actions |
| Compatibility source pins and immutable hashes | PASS |
| AD-9 coverage | PASS: 90 inherited cases plus 4 approved deviations |
| `tests/test_smoke.sh` | PASS |
| Planning quarantine validator | PASS |
| Contract oracle validator | PASS |
| Release oracle validator | PASS |
| Contract fixture `manifest.sha256` | PASS after execution from its owning directory |
| Compatibility `SHA256SUMS` | PASS |
| Release `SHA256SUMS` | PASS |
| Required end digest verification | PASS |

An initial contract checksum invocation was made from the repository root even though its entries are directory-relative; it consequently reported missing paths. Re-execution from `tests/fixtures/contracts/` verified every listed entry successfully. This was an invocation-context error, not evidence corruption.

The release validator reported:

```text
11 crash cuts
7 complete chains
15 standalone authorities
4 traces
1 result
2 live Linux lock modes
2 live ActionExecutor handoff modes
1 positive two-pair FirstInstall proof
5 rollback direction mutations
12 FD4 scalar/binding mutations
22 checksum-resealed release semantic mutations
7 brownfield-pair mutations
3 toolchain mutations
25 CanonicalJsonV1 mutations
1 key-order mutation
11 percent/path mutations
```

PASS output was not treated as sufficient by itself. I inspected the validator logic that enforces exact key registries, canonical reserialization, nested hashes, predecessor relations, manifest revisions, gap-free events and steps, owner publication, cursor identity, state transitions, evidence cardinality, directional consumer bindings, KnownGood publication, FD4 envelopes, Linux locks, ActionExecutor handoff, systemd recovery, and checksum-resealed semantic rejection.

## Unit A / Unit B Divergence Matrix

| Dimension | Unit A / Unit B adversarial counterexample | Normative arbiter | Result |
|---|---|---|---|
| Numeric domain | A accepts only signed `i64`; B accepts arbitrary JSON integers or floats | CanonicalJsonV1 admits exactly `i64` through `u64`; rejects overflow, underflow, float, exponent, non-finite, and negative zero aliases | Closed |
| Object key order | A uses declaration order; B lexicographically sorts | Every contract declares exact schema order; parser reserialization and validators reject reordered objects | Closed |
| Unicode | A preserves decomposed text or escape aliases; B normalizes NFC and emits UTF-8 | NFC-only strings, strict UTF-8, no surrogates, fixed escape spelling, no BOM | Closed |
| Percent/path grammar | A accepts lowercase or over-escaped bytes; B accepts only canonical uppercase spelling | RFC 3986 unreserved set, uppercase percent escapes, normalized absolute raw Linux paths, no NUL/traversal/repeated slash/dot/trailing slash | Closed |
| Framing | A newline-delimits; B uses fixed binary length framing | Exact `u32be` framing, 1 MiB caps, EOF behavior, and frozen frame bytes | Closed |
| Schema closure | A ignores unknown members; B rejects them | Exact key registries and no unknown/defaulted members | Closed |
| Tagged absence | A uses `null` or omitted fields; B uses tagged unions | `null` forbidden; declared present/absent forms and cardinalities enforced | Closed |
| IDs and preimages | A hashes display text; B hashes typed canonical tuples | Exact domains, zero separator, canonical payload/preimage bytes, UUID spelling, and frozen outputs | Closed |
| CollectionPlan | A sorts scopes differently or computes a partial fingerprint; B follows registry order | Exact field order, stable scope ordering, full fingerprint preimage, frozen minimal/nonempty/prior-baseline cases | Closed |
| PolicySnapshot | A hashes resolved values only; B retains full provenance | Exact provenance-bearing preimage and frozen policy fingerprint | Closed |
| ScopeManifest | A emits JSON; B emits binary typed scope bytes | Frozen binary bytes, hex mirrors, and assignment fingerprints | Closed |
| Snapshot/baseline | A chooses latest available baseline; B uses the frozen requested baseline | Exact tagged baseline selection, snapshot preimage, and generation-bound fingerprint | Closed |
| Observation identity | A uses provider display name; B uses typed raw provider identity | Provider-specific tuples, raw bytes, inner hash where required, display derivation, and frozen fingerprints | Closed |
| IPC/FD3 | A allocates attempts after worker readiness; B before spawn | Exact preallocation, hello/ready/request/result state machine, time cuts, one report per scope, and no seventh outcome | Closed |
| Scheduling | A redistributes unused time; B keeps the frozen per-scope budget | Stable limits, fixed ordering, frozen deadlines, and explicit zero-margin case | Closed |
| Evidence | A stores only success summaries; B stores exact pre/post atoms | Exhaustive evidence variants, exact ordering/cardinality, required kinds, and hash linkage | Closed |
| Action handoff | A trusts submitter authorization; B revalidates in executor | Shared lease, executor acknowledgement, generation revalidation, and live positive/negative Linux proof | Closed |
| State DB | A permits sidecar durability; B uses SQLite exclusively | SQLite is sole durable truth owner with migrations, integrity, backup, and recovery rules | Closed |
| State machines | A collapses pending and complete; B persists both | Exact pending/complete/failed/skipped transitions, cursor, events, and terminal mappings | Closed |
| Revision/checksum cascade | A reseals only the final manifest; B links every replacement | Revision-zero absence, exact predecessor checksum, one revision/event per replacement, nested checksum verification | Closed |
| Owner takeover | A overwrites original ownership; B appends recovery ownership | Immutable original owner, gap-free recovery attempts, exact predecessor binding, active owner equals latest attempt | Closed |
| Idempotency/effects | A retries under the same ambiguous effect record; B records attempt identity and evidence | Stable idempotency key, effect attempt, recovery attempt, exact pending-to-terminal identity, readback evidence | Closed |
| Terminal linkage | A sets terminal result without completing terminal step; B links both | Terminal mutation allowed only at successful terminal completion with exact transaction evidence | Closed |
| Singleton/cardinality | A permits duplicate consumer pairs or evidence atoms; B requires exact cardinality | Sorted unique inventories, pair structure, exhaustive arrays, and duplicate rejection | Closed |
| FirstInstall | A fabricates generation zero as an installed release; B uses explicit absence | `FirstInstallAbsentV1`, reserved generation zero, exact absence/state/consumer authority, no fabricated source contract | Closed |
| Reinstall/same generation | A treats it as upgrade; B rejects or completes according to frozen intent | Intent matrix, generation adjacency, immutable installed-prior authority, and admission rules | Closed |
| Upgrade | A activates generation 8 with stale generation-7 consumers; B rewrites and validates | Exact old/new generation relation, directional contracts, timer proof, FD4 validation, KnownGood publication | Closed |
| Explicit rollback | A validates old-to-new direction; B validates restored new-to-old direction | Dedicated rollback chain, rollback target, direction-specific hashes, fresh restored-pair proof | Closed |
| Automatic recovery | A reuses forward evidence; B performs distinct restored validation | Recovery-specific steps/evidence, no forward-evidence substitution, restored generation and contract binding | Closed |
| Forward completion | A can roll back after commit decision; B must finish publication | Commit-decision point is durable and irreversible; publication/readback/admission/terminal completion are mandatory | Closed |
| Paths/artifacts | A aliases candidate/prior paths; B uses distinct role-bound paths | Exact normalized paths, no aliases, candidate/prior binding, schema and checksum relations | Closed |
| StateBackup | A treats plan as completed backup; B requires recorded manifest | Planned versus recorded forms, exact transaction path, DB/WAL/SHM order, integrity/fsync/readback/hash | Closed |
| FD4 | A validates a detached candidate; B binds transaction, owner, pair, generation, request, and deadline | Exact request/result envelopes, capability, attempt, directional hashes, deadline, and single persisted atom | Closed |
| Linux/systemd | A waits on process completion only; B observes manager/job/readback barriers | Live lock modes, manager subscription sequence, owner rechecks, job drain, daemon reload, stable loaded readback | Closed |
| Compatibility bytes | A modernizes output spelling; B preserves deployed bytes | Frozen fixtures/goldens, source pins, immutable hashes, exact routing and 90+4 case accounting | Closed |
| Planning discovery | A discovers retired or arbitrary Markdown; B uses two exact globs | Exact discovery globs, non-assignable tombstone, byte-exact retirement archive | Closed |
| Rust boundary | A regenerates historical oracles from Rust; B treats them as external frozen authority | No Rust encoder captures compatibility fixtures; pinned MSRV/toolchain evidence and replacement-only consumer migration | Closed |

## Seven Complete Release Chains

All seven complete chains were present, checksum-bound, semantically replayed, and terminated in their declared truth:

1. `forward.transitions.jsonl` → `committed`
2. `owner-takeover.transitions.jsonl` → `committed`
3. `first-install-recovery.transitions.jsonl` → `forward-failed-recovered`
4. `explicit-rollback.transitions.jsonl` → `rolled-back`
5. `upgrade.transitions.jsonl` → `committed`
6. `upgrade-owner-takeover.transitions.jsonl` → `committed`
7. `upgrade-recovery.transitions.jsonl` → `forward-failed-recovered`

The chains collectively cover FirstInstall forward completion, FirstInstall recovery, owner takeover, installed-prior upgrade, upgrade owner takeover, automatic recovery, explicit rollback, KnownGood publication, and forward completion after commit decision.

## Named Crash-Cut Coverage

The eleven frozen manifest cuts were validated as exact envelopes of their corresponding transition chains:

- Initial transaction creation
- FirstInstall owner takeover pending validation
- FirstInstall recovery pending consumer removal
- Commit decision complete
- KnownGood publication pending
- KnownGood publication complete
- Ready admission pending
- Explicit rollback ready admission pending
- Upgrade ready admission pending
- Upgrade owner takeover pending validation
- Upgrade recovery pending restored-pair validation

The validator proves that each cut has the exact revision, predecessor, step cursor, event history, evidence, owner history, checksum, and nested authority required at that boundary. Additional live traces cover admission-record locking, manager subscription, systemd job recovery, and ActionExecutor handoff.

## Directional-Hash Replay

The brownfield consumer-pair authority freezes the required directional evidence:

- Forward upgrade and forward-completion source:
  - generation 7
  - contract hash `f3a3f80e…`
- Forward upgrade target:
  - generation 8
  - contract hash `b7a21522…`
- Automatic recovery and explicit rollback source:
  - generation 8
  - contract hash `b7a21522…`
- Restored target:
  - generation 7
  - contract hash `f3a3f80e…`

The forward chains bind old/source to generation 7 and candidate/target to generation 8. Recovery and explicit rollback reverse that relation. Restored daemon reload, loaded-unit readback, timer validation, and FD4 validation remain bound to generation 7.

The validator rejects same-direction hashes, swapped hashes, unknown hashes, wrong generations, cross-bound pair evidence, and directionally stale daemon/timer/FD4 evidence.

## Negative-Mutation Evidence

The inspected validator performs in-memory mutations, recomputes outer checksums where necessary, and then requires semantic rejection. Coverage includes:

- Same, swapped, wrong, and unknown directional consumer hashes
- Wrong source or target generation
- Cross-transaction, cross-owner, cross-attempt, cross-pair, and cross-request FD4 bindings
- Numeric overflow and underflow
- Floats, exponents, non-finite values, and negative zero
- Malformed UTF-8, decomposed Unicode, surrogate aliases, and noncanonical escapes
- Duplicate keys
- Unknown, omitted, reordered, or defaulted schema members
- `null` in place of tagged absence
- Lowercase, truncated, over-escaped, non-ASCII-literal, relative, traversing, repeated-slash, dot-component, NUL, and trailing-slash paths
- Duplicate or malformed consumer pairs
- Wrong predecessor, revision, cursor, event, step, terminal, owner, or recovery-attempt linkage
- State/backup authority changes outside the permitted completed step
- KnownGood candidate or decision changes outside their permitted step
- Toolchain release, manifest, parsed commit, and component-hash drift
- Checksum-resealed release payloads that remain structurally valid JSON but violate semantic contracts
- Action execution after admission-generation change
- Exclusive release attempted while a positive action executor retains its lease

No inspected negative mutation was accepted.

## Compatibility Replay

Compatibility replay passed for:

- Provider behavior
- Output formats
- CLI parsing and routing
- Inspection behavior
- Action behavior
- Exact exit status
- Exact stdout bytes
- Exact stderr bytes
- Terminal-aware routing
- Source pins
- Immutable hashes
- All inherited and approved-deviation cases

Smoke replay also passed JSON, Prometheus, Markdown, table, cron inspection, and hostile-name injection checks.

The architecture keeps legacy compatibility authority separate from new typed contracts. Future Rust code must consume the frozen authority; it cannot redefine compatibility bytes by recapturing fixtures from a Rust encoder.

## Planning and Product-Boundary Replay

Planning quarantine passed with:

- Two exact discovery globs
- One non-assignable tombstone
- One byte-exact retired archive

The canonical PRD/addendum, UX design, experience contract, architecture spine, brownfield behavior, and compatibility ledger agree on the product boundary:

- One-host background-task inventory and Runtime Promise control plane
- Declared intent separated from observed truth
- Provider isolation behind typed ports
- Deterministic snapshot/reconciliation ownership
- Explicit terminal and output routing
- Narrow privilege and evidence-bearing action control
- Crash-recoverable installation, upgrade, recovery, and rollback
- A single future Rust binary without redefining frozen historical compatibility

## No Findings

No critical, high, medium, or low implementation-divergence finding remains.

FINDINGS: 0
VERDICT: PASS