# Terminal Accessibility and Operator-Safety Review — srvls

- **Reviewer:** SyntaxSorcerer, Team Argus
- **Review date:** 2026-07-16
- **Review type:** adversarial documentation-only gate
- **Verdict:** **FAIL**
- **Finding count:** 0 critical, 2 high, 2 medium, 0 low

## Verdict

**FAIL.** The spine pair is strong and internally testable for keyboard-only
navigation, focus recovery, conservative confirmation, exact-target
revalidation, text-first state semantics, hostile-text handling, clean stdout,
and every state named by FR-34. It is not yet safe to hand to implementation
without downstream invention: the user-visible disposition of an in-flight
operation on quit or signal is undefined, and the claimed linear alternative
for terminal screen-reader users has no end-to-end content or acceptance
contract.

The two high findings are implementation-readiness blockers because different
reasonable implementations can produce materially different mutation and
accessibility outcomes. The two medium findings are deterministic interaction
gaps that should be closed in the same update.

## Scope and evidence boundary

This review read the validation instructions and every requested artifact in
full. It did not inspect or modify product code, the source spines, the PRD,
source extracts, `.memlog.md`, or task tracking.

Reviewed artifacts:

- `.agents/skills/bmad-ux/references/validate.md`
- `DESIGN.md`
- `EXPERIENCE.md`
- `reconcile-source-inputs.md`
- `source-extract-legacy-live-ux.md`
- `source-extract-prd-ux.md`
- `../../prds/prd-srvls-2026-07-16/prd.md`
- `../../prds/prd-srvls-2026-07-16/addendum.md`
- `.memlog.md`

The final PRD and addendum are canonical product sources
(`reconcile-source-inputs.md:19-31`). DESIGN.md owns visual semantics and
EXPERIENCE.md owns behavior (`reconcile-source-inputs.md:13-17`). Findings below
therefore cite the canonical sources and final spine pair; extracts are used
only to confirm provenance or a previously identified closure obligation.

## Severity-ranked findings

### High

#### H-01 — Quit and signal behavior is undefined while a lifecycle operation is in flight

##### H-01 evidence

- A pending action persists by operation ID while the operator navigates, and
  duplicate submission is suppressed (`EXPERIENCE.md:181-182`).
- `q` exits from the base Brief after terminal restoration, while modal `q` is
  input or ignored (`EXPERIENCE.md:245-263`).
- The action lifecycle separates Pending, Revalidate, Execute, Verify, and one
  canonical Outcome (`EXPERIENCE.md:319-339`).
- Terminal restoration is required for normal exit, error, panic, Ctrl-C,
  SIGINT, and SIGTERM (`EXPERIENCE.md:384-392`).
- The PRD requires each asynchronous operation to remain isolated and to end in
  exactly one canonical Action Outcome (`../../prds/prd-srvls-2026-07-16/prd.md:576-605`).
- A targeted search for any quit/exit rule coupled to pending, operation, or
  in-flight state returned no match; see **Deterministic command results**.

##### H-01 gate impact

The contract says how the terminal is restored but not what happens to an
operation in Execute or Verify when the operator presses `q`, sends Ctrl-C, or
the process receives SIGTERM. An implementation could refuse exit, detach the
operation, cancel a not-yet-launched operation, forward a signal to a Provider
child, or terminate locally while mutation continues. Those choices produce
different audit, reaping, verification, and outcome behavior. The omission can
therefore turn a clean terminal exit into an unreported or misclassified Host
mutation.

##### H-01 required closure

Specify the observable rule for `q`, Esc, Ctrl-C/SIGINT, and SIGTERM in each
operation phase. The rule must state whether exit is refused, confirmed,
detached, or deferred; whether any signal reaches a Provider child; how bounded
termination/reaping works; where the eventual canonical outcome is persisted
and retrieved; and how a repeated exit signal behaves. Terminal restoration
must remain unconditional.

#### H-02 — The terminal screen-reader alternative is named but not specified end to end

##### H-02 evidence

- The contract correctly acknowledges that alternate-screen TUIs vary across
  terminal screen readers and calls redirected table and Markdown “first-class
  linear alternatives” (`EXPERIENCE.md:370-375`).
- Its accessibility acceptance list covers redirected stdout and `TERM=dumb`,
  but does not define a screen-reader scenario, linear-output fixture, or
  equivalent inspection/action path (`EXPERIENCE.md:390-392`).
- The redirected default is specifically the deterministic **legacy table**
  (`EXPERIENCE.md:394-406`), while the contract does not state which linear
  format carries the eight Brief answers, completeness, exact identity,
  Safe-to-stop reasons, every FR-34 state, and the evidence drill-down needed by
  the core operator journeys.
- The canonical PRD requires all eight morning answers and drill-down paths
  (`../../prds/prd-srvls-2026-07-16/prd.md:472-480`) and accessible terminal
  communication without reliance on a large terminal
  (`../../prds/prd-srvls-2026-07-16/prd.md:730-733`).
- The PRD extraction explicitly identified screen-reader expectations and a
  terminal/backend matrix as an unclosed accessibility detail
  (`source-extract-prd-ux.md:262-271`).

##### H-02 gate impact

An undecorated legacy table is not, by itself, proof that a terminal
screen-reader user can complete the morning handoff, inspect missing evidence,
judge safety, or retrieve an action outcome. “First-class” is currently a
claim without a content mapping or acceptance path. Downstream consumers must
guess whether Markdown is a full linear Brief, whether table output is only a
compatibility view, and which deterministic commands replace TUI drill-down.

##### H-02 required closure

Name the supported linear human path and its exact command/flag sequence. Map
the Brief, completeness, filters or equivalent query, exact-item inspection,
action planning/confirmation, and canonical outcomes onto that path without
requiring ANSI, cursor movement, Unicode, or prose parsing. Add a deterministic
linear-output fixture or named terminal screen-reader acceptance scenario.
Preserve the legacy table unchanged where FR-16 requires it; use Markdown or a
separate explicit human-linear surface if necessary.

### Medium

#### M-01 — Below-minimum resize makes `q` active while the modal contract says it cannot bypass a modal

##### M-01 evidence

- The global key contract permits `q` to quit only from the base Brief; in an
  overlay or modal it is input or ignored and never bypasses confirmation
  (`EXPERIENCE.md:245-263`).
- The accessibility floor repeats that `q` cannot bypass a modal
  (`EXPERIENCE.md:365-368`).
- Resizing below the minimum preserves the model and focus, replaces the
  current content with a resize diagnostic, and says to “keep q and resize
  active” (`EXPERIENCE.md:394-405`).

##### M-01 impact

If the terminal drops below 60 by 20 while a confirmation, baseline override,
or another modal is open, the underlying modal still exists but the visible
surface changes. The two clauses do not establish whether `q` is ignored,
cancels the modal, or exits. This creates divergent keyboard and safety behavior
at exactly the geometry boundary where the operator has the least context.

##### M-01 required closure

Define event priority for the below-minimum diagnostic. A safe deterministic
rule is to preserve modal semantics, show that `q` is unavailable with its
reason, allow Esc to cancel the underlying modal, and require a subsequent `q`
from the restored base Brief. Reconcile the rule with H-01 for pending or
verifying operations.

#### M-02 — ASCII and no-animation semantics are testable, but their activation controls are undefined

##### M-02 evidence

- DESIGN.md defines `NO_COLOR` and ASCII behavior
  (`DESIGN.md:122-148`).
- The help overlay promises to document ASCII/NO_COLOR modes
  (`EXPERIENCE.md:146-167`).
- The accessibility floor defines ASCII markers, optional-spinner suppression
  under a “reduced/no-animation configuration,” and acceptance across
  Unicode/ASCII and monochrome (`EXPERIENCE.md:357-392`).
- The approved legacy/architecture evidence names deterministic `NO_COLOR` and
  `--ascii` fallbacks (`source-extract-legacy-live-ux.md:45-54`).
- Neither spine names `--ascii`, `--no-animation`, an equivalent environment
  variable, automatic capability rule, or precedence between them; the exact
  switch search returned no match.

##### M-02 impact

The renderer semantics are sound, but an implementer and a test author cannot
deterministically enter two of the promised modes. The help contract also
cannot document exact controls from the spine. Different implementations may
conflate color, character-set, and motion preferences even though they are
orthogonal.

##### M-02 required closure

Name the activation and precedence contract. For example: `NO_COLOR` controls
color only; an explicit `--ascii` (plus any documented config/environment
equivalent) controls glyph choice; and v1 either has no spinner at all or names
an explicit no-animation control. State whether `TERM=dumb` implies ASCII and
which explicit option wins. Add exact invocations to acceptance.

## Concern coverage matrix

| Concern | Result | Exact contract evidence | Review note |
| --- | --- | --- | --- |
| Keyboard-only core use | **PASS** | `EXPERIENCE.md:245-266`, `EXPERIENCE.md:365-368` | Navigation, region order, overlays, text input, help, back, and quit have keyboard rules. |
| Focus visibility and recovery | **PASS** | `DESIGN.md:130-148`, `EXPERIENCE.md:193-208` | `>` is semantic; refresh, disappearance, filtering, and overlay closure recover by exact identity and announce movement. |
| Confirmation default and repeated-key hazards | **PASS** | `EXPERIENCE.md:284-304` | Cancel is default; Esc cancels; typed acknowledgement, shortcut suppression, immediate disable, and idempotent duplicate handling are explicit. |
| Known unsafe versus unknown safety | **PASS** | `EXPERIENCE.md:210-225` | Known unsafe is disabled with reasons; unknown is selectable only after typed resolved-verb acknowledgement; neither authorizes mutation. |
| Exact identity and refresh races | **PASS** | `EXPERIENCE.md:36-45`, `EXPERIENCE.md:188-208`, `EXPERIENCE.md:300-336` | Identity plus generation binds plans; focus is identity-based; drift refuses; refresh and verification remain separate lanes. |
| `NO_COLOR`, ASCII, and monochrome | **PARTIAL — M-02** | `DESIGN.md:122-148`, `EXPERIENCE.md:357-392` | Meaning is text-first and acceptance modes are named; ASCII and no-animation activation is not. |
| Terminal screen readers and redirected alternatives | **PARTIAL — H-02** | `EXPERIENCE.md:370-375`, `EXPERIENCE.md:394-406` | Linear alternatives exist in principle; core-journey content and acceptance parity are not specified. |
| Small and resizing terminals | **PARTIAL — M-01** | `DESIGN.md:167-195`, `EXPERIENCE.md:394-411` | Breakpoints, collapse order, startup refusal, model/focus preservation, and recovery are strong; below-minimum `q` priority conflicts. |
| Progress without animation | **PASS** | `DESIGN.md:307-313`, `EXPERIENCE.md:173-187`, `EXPERIENCE.md:384-392`, `EXPERIENCE.md:455-463` | Persistent words, elapsed time, counts, phases, and numeric feedback budgets carry meaning. |
| Terminal restoration | **PARTIAL — H-01** | `EXPERIENCE.md:384-392`, `../../prds/prd-srvls-2026-07-16/prd.md:722-725` | Restoration paths are explicit; observable in-flight operation disposition at those exits is not. |
| Hostile controls, redaction, and truncation | **PASS** | `DESIGN.md:245-249`, `DESIGN.md:315-326`, `EXPERIENCE.md:191`, `EXPERIENCE.md:377-382` | Controls and invalid input are sanitized, sensitive content is excluded/redacted, bounds are disclosed before content, and exact identity is preserved. |
| Clean stdout | **PASS** | `DESIGN.md:301-305`, `EXPERIENCE.md:231-243`, `EXPERIENCE.md:341-355`, `EXPERIENCE.md:394-406` | Machine and redirected stdout exclude ANSI, icons, progress, logs, cursor control, and human diagnostics; human diagnostics use stderr. |
| Every named FR-34 state | **PASS** | `../../prds/prd-srvls-2026-07-16/prd.md:527-535`, `EXPERIENCE.md:169-191` | All 14 canonical names occur exactly once as explicit state rows; responsive and text-first behavior applies across them. |

## FR-34 state coverage matrix

The canonical list is defined at
`../../prds/prd-srvls-2026-07-16/prd.md:527-535`. Responsive preservation is
defined at `EXPERIENCE.md:394-411`; text/no-animation independence is defined
at `EXPERIENCE.md:357-392`.

| FR-34 state | UX evidence | Explicit treatment | Result |
| --- | --- | --- | --- |
| `loading` | `EXPERIENCE.md:175` | Brief shell, loading text, elapsed time, Collector completed/total, help and quit available | **PASS** |
| `refreshing` | `EXPERIENCE.md:176` | Prior Snapshot stays visible and stale-marked; new-generation progress is separate; navigation continues; stale actions disable | **PASS** |
| `stale` | `EXPERIENCE.md:177` | Last success, failed-refresh reason, and affected scope shown; no current-truth claim or mutation | **PASS** |
| `partial-failure` | `EXPERIENCE.md:178` | Successful evidence remains; incomplete scopes and withheld conclusions are named | **PASS** |
| `unavailable-Provider` | `EXPERIENCE.md:179` | Other Providers remain; obligation, outcome, bounded diagnostic, and retry guidance shown | **PASS** |
| `empty` | `EXPERIENCE.md:180` | Empty claim appears only after sufficient required collection; completeness remains visible | **PASS** |
| `filtered-empty` | `EXPERIENCE.md:181` | Active constraints and unfiltered count shown; Clear all receives focus | **PASS** |
| `pending-action` | `EXPERIENCE.md:182` | Operation ID persists during navigation; duplicate submit suppressed; no optimistic truth change | **PASS** |
| `verified` | `EXPERIENCE.md:183` | Fresh evidence proving the exact expected effect is shown | **PASS** |
| `executed-unverified` | `EXPERIENCE.md:184` | Execution, insufficient verification reason, and next safe step are explicit | **PASS** |
| `refused` | `EXPERIENCE.md:185` | No-mutation result plus canonical reason and recovery is shown | **PASS** |
| `timed-out` | `EXPERIENCE.md:186` | Timed-out phase and whether execution may have occurred are explicit; rollback is never implied | **PASS** |
| `failed` | `EXPERIENCE.md:187` | Failed operation/invariant, bounded diagnostic, and next safe step are shown | **PASS** |
| `baseline-unavailable` | `EXPERIENCE.md:190` | First-run, incompatible, incomplete, missing, or unreadable reason is shown; change is not fabricated | **PASS** |

## Deterministic command results

Commands ran on branch `feature-syntaxsorcerer-ux-a11y`. Commands using bare
artifact names or `../../prds` ran from the UX workspace; commands using
`_bmad-output/...` paths and Git commands ran from the worktree root.

### Required-source baseline

```text
$ wc -l DESIGN.md EXPERIENCE.md reconcile-source-inputs.md \
  source-extract-legacy-live-ux.md source-extract-prd-ux.md .memlog.md \
  ../../prds/prd-srvls-2026-07-16/prd.md \
  ../../prds/prd-srvls-2026-07-16/addendum.md
   328 DESIGN.md
   705 EXPERIENCE.md
   109 reconcile-source-inputs.md
    88 source-extract-legacy-live-ux.md
   323 source-extract-prd-ux.md
    18 .memlog.md
   823 ../../prds/prd-srvls-2026-07-16/prd.md
    63 ../../prds/prd-srvls-2026-07-16/addendum.md
  2457 total
exit: 0
```

SHA-256 baselines:

```text
f89d8300abdd227fa2ff3533ceebb570c21c77dabcc343a197dd84d97f6534d8  DESIGN.md
a499e0de5206e78b692cc7d2d900d2ea0008de2338284831b8b8f097932ce9a7  EXPERIENCE.md
818137c6f8f81d6ba9e57c2a75c8e31ec00f072233808870934a9fdadeb97f58  reconcile-source-inputs.md
7a33599919323a0c65292e5d51e8495a69e5d451b81122ff4c8a27cde3fdc253  source-extract-legacy-live-ux.md
27886de5a04c01451539183a64bef30f635b99076493e306c8629e094b9902c2  source-extract-prd-ux.md
ddc945063430811668d88fc47fa9f47475c8d912dbc299c15e88052cd30a50f6  .memlog.md
576186a6068c4a7c7cc087b16530b76269e62ab898a7b2c61db65e389ccdb6d7  ../../prds/prd-srvls-2026-07-16/prd.md
1848ab1351fe8e26edf127da34b0cda4dd3f63d4a17af03f96619f5d8671ae9d  ../../prds/prd-srvls-2026-07-16/addendum.md
exit: 0
```

Frontmatter source links resolve:

```text
$ realpath --canonicalize-existing \
  ../../prds/prd-srvls-2026-07-16/prd.md \
  ../../prds/prd-srvls-2026-07-16/addendum.md
/home/delorenj/code/srvls/worktrees/team-argus/worktrees/syntaxsorcerer-ux-a11y/_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md
/home/delorenj/code/srvls/worktrees/team-argus/worktrees/syntaxsorcerer-ux-a11y/_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/addendum.md
exit: 0
```

### FR-34 exact-row coverage

```text
$ for state in loading refreshing stale partial-failure unavailable-Provider \
  empty filtered-empty pending-action verified executed-unverified refused \
  timed-out failed baseline-unavailable; do \
    count=$(rg -F -c "| $state |" EXPERIENCE.md); \
    printf '%s=%s\n' "$state" "$count"; \
  done
loading=1
refreshing=1
stale=1
partial-failure=1
unavailable-Provider=1
empty=1
filtered-empty=1
pending-action=1
verified=1
executed-unverified=1
refused=1
timed-out=1
failed=1
baseline-unavailable=1
exit: 0
```

### Negative probes supporting findings

```text
$ rg -n -e '(--ascii|--no-animation)' DESIGN.md EXPERIENCE.md
[no matches]
exit: 1

$ rg -n -i -e \
  '(quit.*(pending|operation)|(pending|operation).*(quit|exit)|in-flight.*(quit|exit)|exit.*in-flight)' \
  EXPERIENCE.md
[no matches]
exit: 1

$ rg -n -i 'screen.?reader' EXPERIENCE.md
370:**UX-A11Y-3 — Terminal assistive alternatives.** srvls uses ordinary text
372:screen readers, redirected table and Markdown are first-class linear
exit: 0
```

### Final report checks

```text
$ markdownlint-cli2 review-terminal-accessibility.md
markdownlint-cli2 v0.20.0 (markdownlint v0.40.0)
Finding: review-terminal-accessibility.md
Linting: 1 file(s)
Summary: 0 error(s)
exit: 0

$ sha256sum -c - <<'SHA256'
f89d8300abdd227fa2ff3533ceebb570c21c77dabcc343a197dd84d97f6534d8  _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/DESIGN.md
a499e0de5206e78b692cc7d2d900d2ea0008de2338284831b8b8f097932ce9a7  _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md
818137c6f8f81d6ba9e57c2a75c8e31ec00f072233808870934a9fdadeb97f58  _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/reconcile-source-inputs.md
7a33599919323a0c65292e5d51e8495a69e5d451b81122ff4c8a27cde3fdc253  _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/source-extract-legacy-live-ux.md
27886de5a04c01451539183a64bef30f635b99076493e306c8629e094b9902c2  _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/source-extract-prd-ux.md
ddc945063430811668d88fc47fa9f47475c8d912dbc299c15e88052cd30a50f6  _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/.memlog.md
576186a6068c4a7c7cc087b16530b76269e62ab898a7b2c61db65e389ccdb6d7  _bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md
1848ab1351fe8e26edf127da34b0cda4dd3f63d4a17af03f96619f5d8671ae9d  _bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/addendum.md
SHA256
_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/DESIGN.md: OK
_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/EXPERIENCE.md: OK
_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/reconcile-source-inputs.md: OK
_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/source-extract-legacy-live-ux.md: OK
_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/source-extract-prd-ux.md: OK
_bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/.memlog.md: OK
_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/prd.md: OK
_bmad-output/planning-artifacts/prds/prd-srvls-2026-07-16/addendum.md: OK
exit: 0

$ rg -n '[[:blank:]]+$' review-terminal-accessibility.md
[no matches]
exit: 1

$ git status --short
?? _bmad-output/planning-artifacts/ux-designs/ux-srvls-2026-07-16/review-terminal-accessibility.md
exit: 0
```

The source re-hash proves that this review did not modify either spine, either
source extract, the reconciliation ledger, `.memlog.md`, the canonical PRD, or
the addendum.

## Gate disposition

Do not advance this spine pair as terminal-accessibility and operator-safety
complete until H-01 and H-02 are closed and re-reviewed. M-01 and M-02 should be
closed in the same documentation update because both affect deterministic
acceptance. No amendment is required for the fourteen FR-34 state treatments,
the conservative safety split, destructive confirmation defaults, exact-target
revalidation, hostile-control handling, or stdout purity.
