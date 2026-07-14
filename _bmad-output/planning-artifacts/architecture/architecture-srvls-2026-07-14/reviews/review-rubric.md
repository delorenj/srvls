# Good-Spine Rubric Review

**Artifact:** `ARCHITECTURE-SPINE.md`  
**Review lens:** BMAD good-spine checklist plus brownfield fit  
**Verdict:** **NEEDS CHANGES** — the spine has a strong, appropriately lean paradigm and passes mechanical lint, but five unresolved invariants can still produce incompatible story implementations or regress the existing CLI.

## Gate summary

- Deterministic lint: **PASS** (`0` findings).
- Critical findings: **0**.
- High findings: **5**.
- Medium findings: **2**.
- Low findings: **0**.
- Brownfield sources checked: `README.md`, `srvls`, `tests/test_smoke.sh`, and `docs/architecture.md`.

## High findings

### H1 — AD-4 does not define a deterministic grouping contract

**Checklist failure:** Rule enforceability; prevention matches stated divergence; no divergence point left open.

AD-4 names evidence tiers and calls the resolver deterministic, but leaves token normalization, generic-token classification, score scale, evidence precedence, conflict meaning, score ties, and stable group-key construction undefined. Two grouping stories can obey the rule and still group the same inventory differently. The phrase “strongest non-conflicting evidence” is not executable without those semantics.

The semantic fallback also requires a shared prefix of at least two tokens. Common stacks such as `paperless-web`, `paperless-worker`, and `paperless-db` share one meaningful token and would remain ungrouped, while numeric suffixes can be interpreted inconsistently as tokens. This undercuts the requested default behavior.

**Evidence:** spine AD-4 (line 67) and the grouping label convention (line 128).

**Disposition:** **Autofix before handoff.** Tighten AD-4 with one canonical normalization/tokenization procedure, ordered evidence precedence, minimum confidence by evidence type, deterministic tie-break, and stable group key. Include 3–5 binding examples, including suffix-number families and a one-token project prefix. Algorithm internals may remain seed, but externally observable grouping decisions cannot.

### H2 — Concurrent collection has no canonical merge/order rule

**Checklist failure:** Real divergence at the level below; brownfield ratification.

AD-10 changes fixed-order sequential collection to concurrent collection but does not define how results are merged. Completion-order merge makes table and JSON order nondeterministic, and different implementers can choose collector registration order, provider order, name order, or arrival order while complying with every AD. The current implementation has fixed collector order (`cron`, system systemd, user systemd, Docker, PM2), and Markdown additionally sorts types and names. Nondeterministic JSON/table order would create noisy snapshots and unstable golden tests even if record contents remain correct.

**Evidence:** spine AD-10 (line 103), AD-9 (line 97); `srvls::collect_all()` fixed concatenation order and `out_md()` sorting; `docs/architecture.md` documents fixed-order collection.

**Disposition:** **Autofix before handoff.** State that collection completion order never affects a snapshot. Define either canonical `Entry` ordering or deterministic collector-bucket merge order, and bind each presenter to its compatibility order. If JSON array order is intentionally not contractual, say so while still making emitted output deterministic.

### H3 — The existing `--fzf` interface has no migration decision

**Checklist failure:** Brownfield fit; no silent capability loss.

`--fzf` is a documented public mode with preview and lifecycle keybindings. The spine makes bare terminal invocation open ratatui and says to preserve “current subcommands,” but `--fzf` is an option, not a subcommand, and is absent from AD-7/Deferred. A story can delete it, preserve the external-fzf implementation, or alias it to the new TUI while still satisfying the spine. The private `--fzf-lines` reload surface is also unclassified.

**Evidence:** `README.md` lines 25 and 77–85; `srvls` lines 13 and 321–357; spine AD-7 (line 85) and AD-12 (line 115).

**Disposition:** **Autofix before handoff.** Recommended rule: retain `--fzf` as a compatibility alias that launches the ratatui UI without requiring `fzf`; retire undocumented `--fzf-lines`. If removal is intended, record it explicitly as a breaking change with a release boundary.

### H4 — TUI refresh results can race and overwrite newer truth

**Checklist failure:** State mutation path; enforceable concurrency rule.

The Elm-style loop establishes a single update owner, but AD-10 does not bind background refresh results to request generations. A slow older refresh can arrive after a newer refresh and replace fresher state. “Cancellation by result abandonment” does not cancel a scoped worker thread or its child process; it only permits ignoring a result, and the rule does not say which results must be ignored. Implementers can therefore make incompatible freshness choices while obeying the spine.

**Evidence:** design paradigm; spine AD-5 (snapshot truth) and AD-10 (line 103).

**Disposition:** **Autofix before handoff.** Require monotonic refresh/request IDs and permit `Update` to accept a snapshot only for the latest active generation (or explicitly serialize refreshes and coalesce requests). Define whether the last good snapshot remains visible during refresh and on partial failure. Replace “cancellation by result abandonment” with the exact observable rule.

### H5 — Terminal lifecycle ownership and recovery are silent

**Checklist failure:** Whole owned dimension left silent; state ownership.

The TUI architecture governs raw mode and terminal logging but never assigns ownership for entering/leaving raw mode, alternate-screen use, cursor restoration, or recovery on normal error/panic/interrupt. This is a load-bearing ratatui invariant: independently implemented startup, event-loop, and error-handling stories can each assume another layer restores the terminal, leaving the user's shell corrupted.

**Evidence:** spine AD-8, logging convention (line 126), and `presentation/tui` structural seed.

**Disposition:** **Autofix before handoff.** Assign terminal lifecycle to one RAII session guard in the composition/presentation boundary; require restoration on every normal and unwind path, define interrupt behavior, and add a focused terminal-lifecycle test seam. This belongs in an AD because multiple stories will touch it.

## Medium findings

### M1 — Distribution/install compatibility is not decided

**Checklist failure:** Operational/environmental envelope is incomplete.

AD-12 decides crate topology, lockfile, MSRV, and gates, but “ship one binary” does not say how the binary reaches `~/.local/bin`, which Linux target/libc is supported, or what replaces the current clone-plus-symlink installation. The existing symlink points directly at the executable Python source; it cannot transparently point at a Cargo source tree. This leaves release and deployment stories free to choose incompatible install paths.

**Evidence:** README install section; `docs/architecture.md` deployment architecture; spine AD-12.

**Disposition:** **Discuss or autofix.** For this small utility, a minimal decision is enough: name the supported build/install command and canonical binary destination, plus the one CI/release target. Defer multi-platform packaging explicitly if it is not planned.

### M2 — `EntryId` stability is asserted without canonical construction

**Checklist failure:** Enforceability and shared identity convergence.

The identity convention says `EntryId` derives deterministically from provider, scope, and provider-native identity, but does not define canonical component encoding, normalization, or collision handling. Different adapters can lowercase, path-normalize, hash, or concatenate differently. That becomes observable once selection state, grouping, refresh reconciliation, or future overrides key by `EntryId`.

**Evidence:** spine AD-2 and identity convention (line 122).

**Disposition:** **Autofix or defer with a revisit condition.** Prefer a typed tuple-like ID with an unambiguous canonical encoding owned by the domain. If IDs are intentionally process-local in v1, state that and prohibit persistence/export until a stable versioned representation is decided.

## Checklist coverage and strengths

- **Paradigm and boundaries:** Strong. Hexagonal dependencies, a unidirectional TUI loop, Strategy, Adapter, and Command are beneficial rather than decorative. AD-1 through AD-3 give the refactor a credible separation spine.
- **Base entry abstraction:** Strong direction. AD-2 correctly uses a composed aggregate instead of inheritance and keeps provider-specific behavior outside the base model.
- **Mutation ownership and shell safety:** Strong. AD-6 ratifies argv-array subprocess safety from the current implementation and improves capability validation and destructive confirmation.
- **Partial collection truth:** Strong intentional brownfield improvement. AD-5 directly fixes the current silent-empty failure mode documented in `docs/architecture.md`.
- **Output compatibility:** Mostly strong. AD-7 and AD-9 protect clean stdout and the flat six-field JSON/metric contracts; H2 is the missing order invariant.
- **Accessibility:** Strong. AD-8 requires text fallbacks, `NO_COLOR`, and ASCII symbols, so color/icon additions do not become semantic dependencies.
- **Testing:** Strong direction. AD-11 moves parsing and presentation below deterministic test seams while preserving live-host tests as opt-in integration coverage. Existing smoke behavior is represented, though future stories should expand it to assert compatibility values rather than schema alone.
- **Deferred section:** The listed items are legitimately deferable and do not by themselves create current divergence. The missing decisions above should not be added to Deferred unless each gets an explicit v1 behavior and revisit condition.
- **Named technology currency:** Versions are pinned, satisfying lint. Independent verification-current evidence is not present in the spine itself and should be accepted or rejected by the configured technology-currency reviewer rather than inferred here.

## Required gate action

Resolve H1–H5 in the spine before marking it final. M1 and M2 may be fixed directly or moved to an explicit open/deferred decision only if v1 behavior is made unambiguous. Re-run deterministic lint and the adversarial divergence lens after revision.
