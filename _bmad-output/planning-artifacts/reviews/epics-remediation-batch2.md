---
artifact: canonical-epics-remediation
batch: 2
status: complete
sourceReviews:
  - epics-review-product-traceability-r2.md
  - epics-review-story-quality-dependencies-r2.md
  - epics-review-architecture-divergence-r2.md
---

# Canonical Epics Batch 2 Remediation Ledger

All 48 findings were treated as invalidating. The canonical artifact remained
non-assignable throughout remediation.

## Product and traceability findings

| Finding | Disposition                                                                                                                                    |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| F-R2-01 | Added closed Promise lifecycle/trust semantics and exact revise, Lease, Heartbeat, closure, provenance, and Agent-interface outcomes.          |
| F-R2-02 | Closed obligation/outcome precedence, five Provider source consequences, direct-process identity, privilege, provenance, and bounded evidence. |
| F-R2-03 | Added four Promise outcomes, coexistence, duplicate set/cardinality, unmanaged/abandoned, and conservative safety contracts.                   |
| F-R2-04 | Kept Snapshot/current ownership in 4.7, separated baseline domain/TUI adapters, and retained complete Brief/group/navigation ownership.        |
| F-R2-05 | Closed phase projection, revalidation, handoff, command grammar, KnownGood terminalization, FirstInstall, rollback, and two-pair convergence.  |
| F-R2-06 | Replaced tag-only quality ownership with capability-specific storage, budget, recovery, security, portability, and compatibility boundaries.   |
| F-R2-07 | End-to-end journey owners now name their prerequisite chains and aggregate observable outcomes.                                                |
| F-R2-08 | Foundation/IA ownership now follows the actual startup, truth, navigation, and action surfaces.                                                |
| F-R2-09 | Voice/component mappings are constrained to the behavior implemented by their owning stories.                                                  |
| F-R2-10 | Added missing lifecycle, baseline, TUI, action-phase, confirmation, release, and recovery transitions.                                         |
| F-R2-11 | Split read-only versus action budgets and made accessibility/action aggregate ownership explicit.                                              |
| F-R2-12 | Closed quarantine override, dual toolchain lanes, architecture-native release types, and full two-pair crash gate.                             |
| F-R2-13 | Re-audited all prior dispositions; this ledger claims only concrete changes.                                                                   |

## Story quality and dependency findings

| Finding | Disposition                                                                                                                                                       |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R2-01   | Every AC now binds its named oracle's enumerated rows and exact result token/schema/precedence/exit; closed C-15 through C-21 matrices remove implementer choice. |
| R2-02   | Story 1.7 owns aggregate-neutral repository/CAS primitives only.                                                                                                  |
| R2-03   | Story 1.10 owns the authorized canonical-discovery assertion and must finish green.                                                                               |
| R2-04   | Same-uid Unix peer-credential trust is frozen; AgentId is metadata and remote/token trust is excluded.                                                            |
| R2-05   | Story 2.2 now accepts revise success, retry identity, event count, stale revision, and no-write behavior.                                                         |
| R2-06   | Either missing persistence prerequisite rejects with one typed no-write result; expired history is retained and reconciled inactive/unmanaged.                    |
| R2-07   | Obligations and schedule compile before admission; candidate freezes only after strict reduction.                                                                 |
| R2-08   | Contract C-16 closes every obligation/outcome/reason/exit row and repairs malformed GWT prose.                                                                    |
| R2-09   | Contract C-17 adds inactive and limits unresolved to active intent.                                                                                               |
| R2-10   | Duplicate membership never selects an excess action target or grants safety.                                                                                      |
| R2-11   | Story 4.8 owns domain/CLI acceptance; Story 5.3 owns the TUI adapter.                                                                                             |
| R2-12   | Redirected output remains solely in Story 5.1.                                                                                                                    |
| R2-13   | Pre-action UX ownership is narrowed; action-specific rows close in Epic 6.                                                                                        |
| R2-14   | Story 5.1 is the sole terminal-restoration implementation owner.                                                                                                  |
| R2-15   | Story 5.9 owns read-only goldens/budgets only; action budgets close in 6.12.                                                                                      |
| R2-16   | Revalidation preserves safe, acknowledged-unknown, unsafe, and not-applicable branches.                                                                           |
| R2-17   | Story 6.6 owns the shared action lock/read-back handoff; 7.2 owns release exclusivity only.                                                                       |
| R2-18   | Contract C-20 closes all four durable-phase projections.                                                                                                          |
| R2-19   | Separate AD-11 rows own consumer discovery/readback and per-pair rewrite effects.                                                                                 |
| R2-20   | Forward stops at commit-decided; KnownGood/ready/terminal commit close together in 7.10.                                                                          |
| R2-21   | Installed-prior planning excludes FirstInstall; 7.11/7.12 own absence planning/execution.                                                                         |
| R2-22   | Planning stories cite revision-zero plan-only oracles; execution oracles remain downstream.                                                                       |
| R2-23   | Contract C-19 closes per-verb argv/result/exit/confirmation and AD-11 assigns it to 7.3.                                                                          |

## Architecture divergence findings

| Finding | Disposition                                                                                     |
| ------- | ----------------------------------------------------------------------------------------------- |
| D-01    | Added current AD11-CUR-14 for `tests/test_smoke.sh`.                                            |
| D-02    | Added distinct Heartbeat, closure, and Agent-interface AD-11 rows.                              |
| D-03    | Added orthogonal-outcome, unmanaged/abandoned, Safe-to-stop, and grouping rows.                 |
| D-04    | Added future canonical/identity property-suite ownership.                                       |
| D-05    | Added immediate-revalidation and linear/machine parity rows.                                    |
| D-06    | AD-15 now belongs to all Provider collectors and exact-target executors under Contract C-18.    |
| D-07    | Story 6.4 now preserves canonical acknowledged-unknown behavior.                                |
| D-08    | Contract C-19 and Stories 1.1/7.1 require MSRV plus symbolic moving stable.                     |
| D-09    | Architecture-foreign `ManagedConsumerManifestV1` is forbidden and removed from story authority. |
| D-10    | Discovery belongs to 7.4; pair-qualified rewrite acceptance belongs to 7.6.                     |
| D-11    | Story 7.8 ends at commit-decided and 7.10 owns all terminal commit effects.                     |
| D-12    | AD11-FUT-67 executes both deployed pairs through every effect and crash cut.                    |

## Validation checkpoint

- 73 unique dependency-ordered stories and 81 unique AD-11 rows parse from the
  fenced JSON registry.
- All dependencies reference prior stories.
- Prettier and `git diff --check` pass.
- No product implementation file changed.
