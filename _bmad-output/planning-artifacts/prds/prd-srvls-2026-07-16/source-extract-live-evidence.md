---
title: "srvls Live Product Evidence Extract"
project: "srvls"
artifact_type: "source-extract-live-evidence"
evidence_date: "2026-07-16"
evidence_head: "a1dafe2a253023f511a8ddfaafaecb4f0466fd4d"
status: "analysis-only"
---

<!-- markdownlint-disable MD013 MD025 MD033 -->

# srvls Live Product Evidence Extract

## Purpose and boundary

This report extracts product evidence from the current srvls worktree for use in a future PRD. It is not a PRD, UX specification, architecture amendment, epic rewrite, or readiness reassessment. Candidate concepts below are intentionally unnumbered and non-canonical.

All source paths are repository-relative. Current executable behavior and tests are treated as the authority for what srvls does today. README and brownfield documentation explain that behavior. The architecture spine and epics describe a proposed Rust/ratatui future; they do not prove current implementation or canonical product intent. The readiness report is authoritative for the state of the planning gate.

For readable line citations, three filename aliases are used below and expand to these exact paths:

- <code>ARCHITECTURE-SPINE.md</code> → <code>_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md</code>
- <code>epics.md</code> → <code>_bmad-output/planning-artifacts/epics.md</code>
- <code>implementation-readiness-report-2026-07-15.md</code> → <code>_bmad-output/planning-artifacts/implementation-readiness-report-2026-07-15.md</code>

The evidence baseline was branch <code>feature-agent-buttercup-prd-evidence</code> at <code>a1dafe2a253023f511a8ddfaafaecb4f0466fd4d</code> before this report was added.

## Evidence method and source recency

Filesystem creation times were not useful for ranking evidence because this linked worktree materialized the files together. Per-file Git history and source role were used instead.

| Evidence set | Last source commit | Role in this extract |
| --- | --- | --- |
| <code>README.md</code>, <code>srvls</code>, <code>tests/test_smoke.sh</code>, <code>mise.toml</code>, and the original <code>docs/</code> scan | <code>63757c5</code>, 2026-07-14 | Current Python product behavior, public usage, operations, and known limitations |
| <code>docs/taskforce-ferris-review.md</code> | <code>4c3fba3</code>, 2026-07-14 | Brownfield compatibility and safety review |
| <code>_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md</code> | <code>db7f83c</code>, 2026-07-14 | Proposed Rust/ratatui technical contract |
| <code>tasks.md</code> and <code>_bmad-output/planning-artifacts/epics.md</code> | <code>f6ec819</code>, 2026-07-15 | Work ledger and candidate requirement/story inventory |
| <code>_bmad-output/planning-artifacts/implementation-readiness-report-2026-07-15.md</code> | <code>a1dafe2</code>, 2026-07-16 | Latest planning-gate assessment |

Read-only verification on 2026-07-16 also passed:

    PYTHONPYCACHEPREFIX=/tmp/srvls-prd-evidence-pycache python3 -m py_compile srvls
    bash tests/test_smoke.sh

The smoke run passed all assertions. Its host item and sample counts are deliberately excluded from product conclusions: the suite and development guide identify those values as host-dependent observations, not success metrics (<code>tests/test_smoke.sh:12-25</code>, <code>docs/development-guide.md:29-45</code>).

## Executive evidence finding

The evidence supports a narrower and stronger problem than “replace a Python script with Rust and add a TUI”:

> A Linux operator needs one current, explainable view of background work across otherwise separate control planes, with an honest account of what could not be observed and a safe path from diagnosis to verified action.

The first half is implemented today. srvls combines cron, systemd, Docker, and PM2 into one inventory and exposes human and automation-friendly views (<code>README.md:3-17</code>, <code>srvls:39-191</code>, <code>srvls:194-250</code>). The second half is the central product gap. Current collector errors, denials, malformed responses, and timeouts generally become empty strings or empty collections, so missing inventory can look identical to a genuinely empty subsystem (<code>srvls:31-36</code>, <code>srvls:89-103</code>, <code>docs/architecture.md:48-58</code>, <code>docs/deployment-guide.md:40-58</code>).

The proposed architecture and epics explicitly recognize that gap. They make snapshot completeness, per-provider diagnostics, stale-state handling, stable identity, action revalidation, and post-action verification part of the runtime model (<code>ARCHITECTURE-SPINE.md:69-79</code>, <code>epics.md:291-338</code>, using the full architecture path listed above). That is the evidence-backed center of gravity for the PRD.

No repository source establishes adoption, incident frequency, time saved, acceptable refresh latency, or another quantified product outcome. Those measures must be elicited rather than inferred.

## Evidence-backed problem framing

### Fragmented host truth

The public rationale says background work accumulates across user/root cron, systemd system and user scopes, Docker, and PM2, while stock tools expose those systems separately. During a host problem, the operator otherwise has to remember where to look and reconstruct the picture manually (<code>README.md:9-17</code>).

The implementation validates that fragmentation by calling multiple unrelated host interfaces and normalizing their output into a common record (<code>srvls:41-191</code>). The brownfield architecture describes the implemented pipeline as sequential collectors feeding normalized records and renderers/actions (<code>docs/architecture.md:19-44</code>).

### Visibility is useful only when absence is trustworthy

The README describes “every” background task and “one view” (<code>README.md:3-5</code>), but the runtime is explicitly best-effort:

- The process wrapper ignores child return codes, discards stderr, and returns an empty string on exceptions or timeouts (<code>srvls:31-36</code>).
- Root cron is attempted with non-interactive sudo and disappears when access is unavailable (<code>srvls:65-66</code>, <code>docs/deployment-guide.md:13-21</code>).
- Systemd JSON parse failures become empty lists (<code>srvls:89-103</code>, <code>srvls:117-138</code>).
- Missing Docker IDs or malformed Docker inspection rows simply produce fewer entries (<code>srvls:141-166</code>).
- Missing PM2 and malformed PM2 JSON both produce an empty PM2 inventory (<code>srvls:169-186</code>).

The result is operationally ambiguous: empty can mean absent tooling, denied access, timeout, parse failure, or no resources (<code>docs/deployment-guide.md:48-58</code>). The taskforce review identifies this as a migration-defining contract rather than a minor implementation detail (<code>docs/taskforce-ferris-review.md:17-21</code>).

### Inventory is both an incident surface and an automation surface

The default table and inspection flow support immediate triage, while JSON, Prometheus, and Markdown support scripts, monitoring, and drift history (<code>README.md:40-78</code>, <code>README.md:108-151</code>). This means a rewrite can improve the interactive experience only if it preserves or deliberately versions the non-interactive contracts used by timers and redirected output (<code>epics.md:53-59</code>, <code>ARCHITECTURE-SPINE.md:81-103</code>).

### Acting from the same view raises the safety bar

Current lifecycle commands are immediate, provider-specific mutations. They do not confirm, bind to a captured resource identity, revalidate the target, verify the postcondition, or record an audit result (<code>srvls:253-276</code>, <code>docs/deployment-guide.md:40-46</code>). The same public verb also has materially different meanings: disable means systemd disable, Docker stop, or PM2 delete (<code>srvls:255-264</code>).

The planning artifacts therefore treat stable identity, capability checks, confirmation, revalidation, execution, and verification as one product safety chain (<code>ARCHITECTURE-SPINE.md:75-79</code>, <code>ARCHITECTURE-SPINE.md:117-133</code>, <code>epics.md:512-670</code>).

## Operator jobs

The sources support the following jobs. “Current” means implemented by the checked-in Python CLI. “Proposed” means present only in architecture/epics and still subject to PRD validation.

| Operator job | Current support | Proposed extension | Evidence |
| --- | --- | --- | --- |
| See background work across control planes without running each native tool separately | Unified cron, systemd, Docker, and PM2 inventory | Preserve the coverage in a typed Rust model | <code>README.md:3-17</code>; <code>srvls:39-191</code>; <code>epics.md:25-35</code> |
| Identify failed, unhealthy, restarting, or errored work during triage | Table tallies problems; Prometheus emits per-unit problem gauges; inspect exposes provider detail | Make degraded providers and partial snapshots visible rather than empty-looking | <code>srvls:196-234</code>; <code>srvls:296-314</code>; <code>epics.md:35-57</code> |
| Know whether the view is complete enough to trust | Not supported; failures are largely silent | Per-collector completeness, diagnostics, stale state, and strict-mode policy | <code>docs/architecture.md:48-58</code>; <code>ARCHITECTURE-SPINE.md:69-73</code>; <code>epics.md:291-312</code> |
| Understand which resources belong to the same workload | Operators infer relationships from provider names and source fields | Deterministic, evidence-bearing stack projections with an explicit Ungrouped section | <code>srvls:111-185</code>; <code>ARCHITECTURE-SPINE.md:63-67</code>; <code>epics.md:344-372</code> |
| Inspect status and recent detail without leaving the inventory | Provider-specific inspect commands; Docker includes recent logs | Bounded, sanitized, structured inspection plus collection diagnostics | <code>srvls:279-314</code>; <code>epics.md:456-480</code> |
| Start, stop, restart, or disable an individual resource from the unified surface | Immediate CLI/fzf actions; cron is read-only | Typed action planning, exact identity, confirmation where destructive, revalidation, and verification | <code>README.md:77-106</code>; <code>srvls:253-276</code>; <code>epics.md:512-670</code> |
| Feed monitoring and compare host drift over time | Flat JSON, fixed Prometheus families, and Markdown snapshots | Preserve machine-output purity and deterministic compatibility | <code>README.md:57-75</code>; <code>README.md:108-151</code>; <code>tests/test_smoke.sh:12-66</code>; <code>epics.md:314-338</code> |
| Install or upgrade without breaking existing timer consumers | Clone plus symlink; operational units are manual examples | Versioned binary, checksum, staged smoke, atomic switch, automation validation, and rollback | <code>README.md:19-26</code>; <code>docs/deployment-guide.md:23-38</code>; <code>epics.md:672-775</code> |

## Current behavior

### Runtime and distribution

- srvls is one executable Python file with Python 3.8+ and standard-library-only as the documented runtime constraint (<code>README.md:7</code>, <code>README.md:19-26</code>, <code>docs/project-overview.md:7-17</code>).
- The supported install is a repository clone and symlink to <code>~/.local/bin/srvls</code>; no package manifest or repository-managed release/deployment automation exists (<code>README.md:19-26</code>, <code>docs/project-overview.md:30-35</code>, <code>docs/deployment-guide.md:60-62</code>).
- The mise test task is a thin wrapper over the smoke script. Other checked-in tasks manage agent links and generic Git-tag versioning; they do not build or release the product (<code>mise.toml:24-57</code>, <code>docs/development-guide.md:70-80</code>).

### Collection

Collection is sequential and concatenates providers in this order: cron, system systemd, user systemd, Docker, PM2 (<code>srvls:189-191</code>).

| Provider | Current discovery behavior | Important limitation |
| --- | --- | --- |
| Cron | Parses invoking-user crontab, passwordless-root crontab, <code>/etc/crontab</code>, and regular files in <code>/etc/cron.d</code>; ignores comments and environment assignments | Uses whitespace/user heuristics; names are derived from command basenames; duplicate or same-name entries are not given stable identities (<code>srvls:41-80</code>) |
| systemd | Reads services, unit files, and timers in system and user scopes as JSON; excludes inactive services unless enabled | Parse/command failure becomes an empty source; timer state is inferred from the next timestamp (<code>srvls:83-138</code>) |
| Docker | Lists all container IDs, then performs one formatted inspect for state, health, restart policy, Compose metadata, and healthcheck interval | An empty/failed list and malformed rows silently reduce inventory; one batch inspect couples container results (<code>srvls:141-166</code>) |
| PM2 | Uses <code>pm2 jlist</code> when PM2 is on PATH and records name, status, restart count, cwd, and executable | Visibility is invoking-user scoped; absence and malformed output are both empty; display name is used for actions (<code>srvls:169-186</code>) |

No collector deduplicates entries or returns source completeness. Fixed subprocess timeouts are implementation constants, not validated product latency targets (<code>srvls:31-36</code>, <code>srvls:141-153</code>, <code>docs/architecture.md:52-58</code>).

### Output and interaction

- Bare srvls always performs collection and prints the legacy table; it does not currently select a UI based on terminal capability (<code>srvls:338-360</code>).
- <code>--json</code> pretty-prints the normalized item list. <code>--prom</code> emits aggregate inventory gauges, problem gauges, load averages, and a collection timestamp. <code>--md</code> emits a timestamped snapshot grouped by type (<code>srvls:211-250</code>, <code>srvls:347-353</code>).
- <code>--fzf</code> requires an installed fzf binary, previews inspection, and binds stop/restart/disable through fzf command strings (<code>srvls:317-335</code>).
- Explicit inspect/start/stop/restart/disable routes before inventory collection. Cron mutation is refused. User systemd, system systemd, Docker, and PM2 map to distinct native commands (<code>srvls:253-276</code>, <code>srvls:338-345</code>).
- Unknown flags, including <code>--help</code> and <code>--version</code>, currently fall through to inventory/table behavior; extra non-action arguments are ignored. Mode precedence is hard-coded rather than parser-governed (<code>srvls:338-360</code>, <code>docs/architecture.md:102-110</code>).

## Current compatibility contracts

These are observable baseline behaviors, not a recommendation that every quirk remain forever. The compatibility ledger proposed by the architecture should classify each as preserve, deliberately change, deprecate, or leave unspecified.

| Contract surface | Observable baseline | Evidence and test strength |
| --- | --- | --- |
| Executable identity and install path | Command is <code>srvls</code>; documented installation symlinks the repository script into <code>~/.local/bin</code> | Publicly documented in <code>README.md:19-26</code>; relied on by timer examples at <code>README.md:108-147</code> |
| Supported type identifiers | <code>cron</code>, <code>sys-svc</code>, <code>sys-timer</code>, <code>usr-svc</code>, <code>usr-timer</code>, <code>docker</code>, <code>pm2</code> | Declared in <code>srvls:17</code> and <code>docs/component-inventory.md:25-31</code> |
| Flat item projection | Every normal item has <code>type</code>, <code>name</code>, <code>state</code>, <code>schedule</code>, <code>source</code>, and <code>detail</code> | Implemented across <code>srvls:59-63</code>, <code>srvls:110-136</code>, <code>srvls:159-185</code>; smoke checks required keys only on the first item at <code>tests/test_smoke.sh:12-25</code> |
| Provider and encounter ordering | Provider buckets are fixed by <code>collect_all()</code>; most outputs preserve adapter encounter order, while Prometheus aggregates are sorted and Markdown sorts type/name | <code>srvls:189-191</code>, <code>srvls:211-250</code>; architecture explicitly treats ordering as compatibility at <code>ARCHITECTURE-SPINE.md:93-103</code> |
| Default table | Prints dynamic-width columns and a final item/failed/unhealthy summary | <code>srvls:196-208</code>; smoke asserts the summary form at <code>tests/test_smoke.sh:63-66</code> |
| JSON | Pretty-printed list of flat six-field records | <code>srvls:347-350</code>; smoke validates list shape and the first item at <code>tests/test_smoke.sh:12-25</code> |
| Prometheus | Exact allowed families are <code>srvls_items</code>, optional <code>srvls_unit_problem</code>, <code>srvls_loadavg</code>, and <code>srvls_collect_timestamp_seconds</code> | <code>srvls:211-234</code>; exact family allowlist enforced at <code>tests/test_smoke.sh:27-55</code> |
| Markdown | Header begins <code># Background Task Inventory</code>; one table per present type; rows are name-sorted | <code>srvls:237-250</code>; smoke asserts header/table at <code>tests/test_smoke.sh:57-61</code> |
| Explicit lifecycle verbs | Public verbs are inspect, start, stop, restart, and disable. Cron is read-only. Disable maps to systemd disable, Docker stop, and PM2 delete | <code>README.md:87-106</code>; <code>srvls:253-276</code> |
| Inspection behavior | Provider tools are invoked with argv arrays; Docker includes recent logs; missing/error output is swallowed and inspect returns zero | <code>srvls:279-314</code>; smoke covers real cron when present and direct hostile names at <code>tests/test_smoke.sh:68-90</code> |
| Argument quirks | Unknown flags run normal inventory; explicit modes use fixed precedence; undocumented <code>--fzf-lines</code> exists | <code>srvls:338-360</code>; risk catalogued at <code>docs/taskforce-ferris-review.md:13-17</code> |
| Partial failure and exits | Most collection failures still yield successful partial/empty output; direct action exit follows the child command | <code>srvls:31-36</code>, <code>srvls:267-276</code>; operational warning at <code>docs/deployment-guide.md:40-46</code> |
| Machine-output channel purity | Current renderers write product output to stdout; collection errors are suppressed rather than diagnosed | <code>srvls:31-36</code>, <code>srvls:194-250</code>; future preservation concept at <code>epics.md:314-338</code> |

Compatibility weaknesses that require deliberate treatment include Markdown pipe escaping, Prometheus label escaping, fzf command-string interpolation, leading-dash option injection, and incomplete stdout/stderr/exit coverage (<code>docs/architecture.md:102-110</code>, <code>docs/taskforce-ferris-review.md:31-45</code>).

The current smoke suite is a useful executable baseline, but it is not yet a migration oracle. It is live-host dependent, checks the JSON schema only on the first record, does not inject collector failures, and avoids mutation coverage (<code>tests/test_smoke.sh:12-90</code>, <code>docs/architecture.md:98-110</code>, <code>docs/taskforce-ferris-review.md:43-47</code>). Its Markdown assertion also assumes at least one type table even though the JSON test explicitly allows a clean host to return zero items (<code>tests/test_smoke.sh:12-14</code>, <code>tests/test_smoke.sh:57-60</code>).

## Runtime-promise thesis

### Candidate thesis

srvls should be specified as a runtime trust loop, not as a language rewrite or screen design:

1. **Coverage truth:** state which providers and sub-sources were checked, which were unavailable or denied, and whether the snapshot is complete enough for its intended use.
2. **State truth:** show what was observed, when it was observed, and when retained information is stale.
3. **Context truth:** explain why resources are grouped together and leave ambiguous resources visibly ungrouped.
4. **Action truth:** bind a mutation to a stable observed identity, make its provider-native meaning clear, revalidate immediately, and report the verified or unverified result.
5. **Continuity truth:** keep existing scripts, metrics, snapshots, and timers working across the migration unless an intentional versioned change is recorded.

This is a synthesis, not an approved requirement. It is supported by the public one-view/drift promise (<code>README.md:9-17</code>, <code>README.md:108-151</code>), the current silent-failure hazard (<code>docs/architecture.md:77-88</code>, <code>docs/deployment-guide.md:40-58</code>), and the planned snapshot/action/compatibility rules (<code>ARCHITECTURE-SPINE.md:69-103</code>, <code>epics.md:291-338</code>, <code>epics.md:512-670</code>).

### Why this thesis matters

Rust, ratatui, grouping, icons, and concurrency are implementation or experience choices. They create product value only when they strengthen the trust loop:

- Rust and typed ports can make provider outcomes and identities explicit.
- Bounded concurrency can reduce sequential waiting, but no source yet defines an acceptable user-facing latency threshold.
- Ratatui can keep context, inspection, and action in one place, but it also introduces stale-selection, terminal-restoration, and privilege hazards.
- Grouping can reduce cognitive load only when evidence and ambiguity remain visible.
- Lifecycle controls can shorten recovery only when they cannot target a replacement resource or hide an unverified result.

The architecture addresses these mechanisms in detail (<code>ARCHITECTURE-SPINE.md:43-133</code>). The PRD still needs to establish which outcomes matter, who needs them, and where the product boundary belongs.

## Conflicts and staleness

| Conflict or stale statement | Evidence | Reconciliation for PRD work |
| --- | --- | --- |
| Task ledger says the architecture and 23 stories are completed and validated; readiness says the product plan is not ready | <code>tasks.md:5-11</code> versus <code>implementation-readiness-report-2026-07-15.md:210-238</code> | “Completed” means the artifacts were authored, not that requirements and UX readiness passed |
| Architecture spine is marked final although no canonical PRD or UX source exists | <code>ARCHITECTURE-SPINE.md:1-23</code> versus <code>implementation-readiness-report-2026-07-15.md:22-75</code> and <code>implementation-readiness-report-2026-07-15.md:122-141</code> | Treat the spine as a strong technical proposal whose product assumptions must be reconciled, not as proof of product intent |
| Epics call the brief user-confirmed and define 18 FRs, 10 NFRs, and 8 UX requirements; readiness finds every FR identifier orphaned from a PRD | <code>epics.md:15-113</code> versus <code>implementation-readiness-report-2026-07-15.md:77-120</code> | Reuse the inventory as candidate requirements only; assign canonical identifiers after PRD decisions |
| Brownfield docs describe the current Python CLI while later artifacts describe a Rust/ratatui target | <code>docs/project-overview.md:3-35</code>, <code>docs/architecture.md:1-18</code> versus <code>ARCHITECTURE-SPINE.md:1-30</code> | Preserve an explicit “today” and “target” split; do not write future behavior as current capability |
| The Taskforce Ferris review says no <code>_bmad-output</code> or architecture draft existed at reviewed HEAD | <code>docs/taskforce-ferris-review.md:3-9</code> | Its context statement is historical to <code>63757c5</code>; its brownfield findings remain useful, but it is not a current artifact inventory |
| Generated docs index calls <code>tasks.md</code> a current documentation workflow claim, but the ledger now records completed work and an external Plane launch item | <code>docs/index.md:33-38</code> versus <code>tasks.md:1-11</code> | The documentation scan predates the architecture/epic/readiness sequence and should not be treated as a current planning index |
| README promises “every” task in one view; implementation can silently omit an entire subsystem | <code>README.md:3-17</code> versus <code>srvls:31-36</code> and <code>docs/deployment-guide.md:40-58</code> | Make completeness part of the product promise or narrow the public claim |
| Bare srvls is currently a table and <code>--fzf</code> requires fzf; planned behavior makes bare interactive terminals open ratatui and turns <code>--fzf</code> into an alias | <code>README.md:40-85</code>, <code>srvls:317-360</code> versus <code>ARCHITECTURE-SPINE.md:81-85</code> | This is a deliberate compatibility decision, not transparent implementation parity |
| Current installation is clone-plus-symlink; planned installation is a versioned release with atomic activation and rollback | <code>README.md:19-26</code> versus <code>epics.md:672-775</code> | Specify migration and ownership of existing symlinks as product behavior |
| Architecture locks Rust/crate/platform versions, but no Rust manifest, lockfile, or CI exists and the first story assumes a crate already exists | <code>ARCHITECTURE-SPINE.md:149-163</code>, <code>epics.md:202-224</code>, <code>implementation-readiness-report-2026-07-15.md:160-180</code> | Treat versions as target constraints; add the missing bootstrap/early gate before implementation |
| Historical smoke documents contain host-specific inventory counts that differ across environments/runs | <code>docs/development-guide.md:29-45</code>, <code>docs/project-scan-report.json:29-39</code>, <code>docs/taskforce-ferris-review.md:7-10</code> | Counts demonstrate environment dependence, not product scale, quality, or success |

## Readiness gaps

### Source-confirmed gate failures

The latest readiness report concludes <strong>NOT READY</strong> for full implementation (<code>implementation-readiness-report-2026-07-15.md:210-218</code>). Its evidence-backed gaps are:

1. No canonical PRD exists, so requirement completeness, goals, non-goals, and product traceability cannot be established (<code>implementation-readiness-report-2026-07-15.md:22-75</code>).
2. No dedicated UX artifact exists for an explicitly interactive product; information architecture, focus, modal behavior, responsive thresholds, primary states, confirmations, and usability acceptance remain distributed across epics (<code>implementation-readiness-report-2026-07-15.md:122-141</code>).
3. The story sequence assumes a Rust crate that no story creates, and locked MSRV/current-stable gates arrive after most implementation (<code>implementation-readiness-report-2026-07-15.md:160-169</code>).
4. The TUI has no defined way to initiate start, despite start being in FR13 and provider action stories (<code>implementation-readiness-report-2026-07-15.md:170-173</code>).
5. Story 1.6 combines subprocess safety, concurrency, outcome reduction, ordering, and strict-mode policy; Story 3.5 combines multiple safety-critical interaction and verification seams (<code>implementation-readiness-report-2026-07-15.md:174-180</code>).
6. Internal story traceability is strong but non-canonical because all identifiers originate in <code>epics.md</code> (<code>implementation-readiness-report-2026-07-15.md:182-184</code>).

The report records nine actionable issues across four categories and recommends a lean PRD, focused UX contract, targeted epic changes, and a readiness rerun rather than discarding the architecture (<code>implementation-readiness-report-2026-07-15.md:220-238</code>).

### Product-evidence gaps not to fill by invention

- **Trigger evidence:** <code>README.md:9-17</code> gives a compelling generic incident scenario, but the repository contains no dated operator incident, command trail, prevented outcome, interview, or observational study.
- **Target user:** sources consistently say operator and describe a long-lived Linux server, but no canonical persona, environment range, team context, or buyer/user distinction exists.
- **Outcome measures:** no source defines adoption, incident-recovery, completeness, safety, usability, or latency success thresholds. Existing timeout values and historical host counts are implementation observations, not targets.
- **Priority and boundary:** architecture defers group actions, plugins, persistent grouping overrides, theme files, broad portability, and multi-crate structure, but a PRD has not approved these as product non-goals (<code>ARCHITECTURE-SPINE.md:227-235</code>).
- **Provider criticality:** the architecture models Required versus Optional availability and stories call Docker/PM2 optional, but there is no canonical policy for which sources make a default snapshot trustworthy (<code>ARCHITECTURE-SPINE.md:69-73</code>, <code>epics.md:247-289</code>).
- **Default degraded behavior:** planned strict mode is defined, but the desired default diagnostics, exit policy, and automation experience under partial collection remain product decisions (<code>epics.md:291-338</code>).
- **Action scope:** the technical design specifies safe individual actions and read-only groups, but the PRD has not established whether mutation is core launch scope or a later capability.
- **Platform scope:** the architecture targets one verified Linux/glibc baseline; demand for other distributions, architectures, or packaging channels is not evidenced (<code>ARCHITECTURE-SPINE.md:111-115</code>, <code>ARCHITECTURE-SPINE.md:227-235</code>).

## Candidate requirement concepts

These concepts are grounded in sources but are not approved requirements and intentionally have no FR/NFR identifiers.

| Candidate concept | Evidence basis | Decision still required |
| --- | --- | --- |
| Unified background-work inventory across supported cron, systemd, Docker, and PM2 scopes | Implemented and documented at <code>README.md:3-17</code> and <code>srvls:39-191</code> | Define the minimum provider set and what “all” means when access/tooling is unavailable |
| Honest snapshot completeness and provider diagnostics | Current ambiguity at <code>docs/deployment-guide.md:40-58</code>; proposed model at <code>ARCHITECTURE-SPINE.md:69-73</code> | Define required versus optional sources, default exit behavior, diagnostic visibility, and automation semantics |
| Compatibility-first migration with explicit intentional deviations | Brownfield review at <code>docs/taskforce-ferris-review.md:13-19</code>; proposed ledger at <code>epics.md:183-200</code> | Decide which quirks are promises, which are defects, and the version/deprecation boundary for changes |
| Flat, clean, deterministic automation outputs | Current modes at <code>srvls:194-250</code>; tested subset at <code>tests/test_smoke.sh:12-66</code> | Define semantic versus byte compatibility and how partial diagnostics use stderr/exit codes |
| Stack-first context with evidence and an explicit Ungrouped state | Proposed at <code>ARCHITECTURE-SPINE.md:63-67</code> and <code>epics.md:344-372</code> | Validate that automatic grouping solves the primary job and determine how operators correct or challenge inference |
| Terminal-aware interactive triage with accessible non-color fallbacks | Proposed at <code>ARCHITECTURE-SPINE.md:81-91</code> and <code>epics.md:374-506</code> | Confirm default TUI versus explicit opt-in, layout/focus model, and supported terminal constraints in UX |
| Bounded, sanitized inspection and visible collection problems | Current inspect at <code>srvls:279-314</code>; proposed at <code>epics.md:456-480</code> | Define useful detail per provider, redaction policy, content limits, and remediation guidance |
| Safe individual lifecycle control tied to observed identity | Current immediate actions at <code>srvls:253-276</code>; proposed safety chain at <code>epics.md:512-670</code> | Confirm launch scope, start interaction, confirmation policy, verification expectations, and audit requirement |
| Preserve monitoring and drift-history consumers through migration | Operational patterns at <code>README.md:108-151</code>; planned validation at <code>epics.md:725-749</code> | Identify actual deployed consumers and define the supported upgrade/rollback contract |
| Reversible installation and release provenance | Current symlink at <code>README.md:19-26</code>; planned release flow at <code>epics.md:676-775</code> | Confirm supported platform/channel, foreign-install ownership rules, and rollback state location |

### Candidate non-goals requiring product confirmation

The architecture defers the following. A PRD may adopt them as initial non-goals only after product confirmation:

- Multi-resource or stack actions.
- Persistent manual grouping overrides.
- User-authored theme files.
- Plugin or dynamic collector loading.
- Grouped machine-output schemas.
- Broader Linux/glibc portability.
- Multi-crate structure.
- Interactive privilege escalation inside the TUI.

Source: <code>ARCHITECTURE-SPINE.md:227-235</code>, with the single-package threshold also stated at <code>ARCHITECTURE-SPINE.md:111-115</code>.

## PRD decision queue

The evidence is sufficient to draft around the product problem, but not to close these decisions without owner input:

1. What recent real incident best represents the trigger, commands used, uncertainty encountered, and bad outcome avoided?
2. Who is the primary operator: the single-host owner represented by big-chungus, a broader self-hosting operator, or a team managing multiple hosts?
3. Is the core promise unified visibility, honest completeness, safe control, or the full runtime trust loop? Which parts are launch-critical?
4. Which current CLI/output behaviors are compatibility commitments, and which are defects to change with a ledger entry?
5. Should bare srvls open ratatui on a terminal, or should the TUI remain explicit?
6. Which providers/sub-sources are required for a trustworthy default snapshot, and how should partial results affect stdout, stderr, and exit status?
7. Is automatic stack inference essential at launch, and how should an operator understand or override an uncertain grouping?
8. Is start CLI-only or available from the TUI, and what gesture/action model exposes it?
9. Which actions require confirmation, audit, and verified postconditions?
10. What user-facing outcome and performance measures should define success? No numeric target should be copied from current timeouts, host counts, or planning prose.
11. Which deployed timers, scripts, dashboards, snapshot repositories, and install layouts must be treated as named compatibility consumers?
12. Is the initial platform intentionally limited to the recorded big-chungus Linux/glibc target?

## Suggested PRD spine from this evidence

A lean canonical PRD can now be organized without treating the epics as intent:

1. **Problem and trigger:** fragmented host control planes plus untrustworthy silent absence.
2. **Primary operator and context:** to be validated from a real incident.
3. **Runtime promise:** coverage, state, context, action, and continuity truth.
4. **Goals and non-goals:** approve or reject the candidate scope above.
5. **Current compatibility baseline:** executable, types/schema, outputs, ordering, arguments, actions, install, and automation consumers.
6. **Functional outcomes:** start from the candidate concepts, then reconcile against the 18 epic FRs.
7. **Quality and safety outcomes:** completeness, deterministic automation, identity, terminal safety, privilege, sanitization, verification, and rollback.
8. **UX contract:** follow with a separate focused TUI artifact rather than leaving UX embedded in stories.
9. **Success evidence:** elicit measures and acceptance thresholds; do not derive them from host-specific smoke output.
10. **Traceability and change policy:** assign canonical requirement identifiers, reconcile epics, record intentional compatibility deviations, and rerun readiness.

## Source index

### Work ledger and public product documentation

- <code>tasks.md</code>
- <code>README.md</code>

### Current implementation and validation

- <code>srvls</code>
- <code>tests/test_smoke.sh</code>
- <code>mise.toml</code>

### Brownfield project documentation

- <code>docs/index.md</code>
- <code>docs/project-overview.md</code>
- <code>docs/architecture.md</code>
- <code>docs/component-inventory.md</code>
- <code>docs/source-tree-analysis.md</code>
- <code>docs/development-guide.md</code>
- <code>docs/deployment-guide.md</code>
- <code>docs/taskforce-ferris-review.md</code>
- <code>docs/project-scan-report.json</code>

### Current planning artifacts

- <code>_bmad-output/planning-artifacts/implementation-readiness-report-2026-07-15.md</code>
- <code>_bmad-output/planning-artifacts/architecture/architecture-srvls-2026-07-14/ARCHITECTURE-SPINE.md</code>
- <code>_bmad-output/planning-artifacts/epics.md</code>

## Bottom line

The live product already proves the value of collapsing fragmented host background work into one view and reusable exports. It does not yet make that view honest about missing sources or make mutations safe enough for a continuously refreshing interface. The PRD should therefore canonize the runtime trust promise and the operator job first, then decide which Rust/TUI/grouping/action mechanisms belong in the initial product. The existing architecture and epics are strong implementation candidates, but the readiness evidence is correct: they cannot substitute for that product decision.
