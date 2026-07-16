<!-- markdownlint-configure-file { "MD013": { "tables": false } } -->

# Current Landscape: srvls Promise Reconciliation and Morning Handoff

**Research date:** 2026-07-16

**Source access date:** 2026-07-16

**Product lens:** agent-runtime promise reconciliation and a terminal-first
morning handoff for Linux operators

## Executive synthesis

The current landscape is capable but partitioned by authority boundary:

- Linux service managers and schedulers describe what their own manager knows
  about definitions, activation, schedules, status, dependencies, and logs.
- Process supervisors describe the applications registered with a particular
  supervisor instance.
- Container tools describe objects visible through a selected daemon, context,
  user, project, or Container Runtime Interface endpoint.
- observability systems collect runtime signals and help explain behavior over
  time, provided the relevant source is instrumented and retained.
- agent platforms describe agent deployments, runs, tool calls, handoffs,
  checkpoints, traces, and platform-level resource behavior.

Those are adjacent answers, not the complete srvls answer. In the reviewed
official sources, no product documents a cross-boundary workflow that takes an
agent-declared intended outcome, tests it against fresh host evidence, exposes
coverage failures, and produces a prioritized operator handoff for a defined
overnight window. This is an evidence-set finding, not proof that no such
product exists.

The strongest differentiation opportunity is therefore not another process
manager, dashboard, trace viewer, or agent control plane. It is an
evidence-backed comparison layer:

> What was expected, what is observable now, what changed, what cannot be
> established, and what deserves the operator's attention?

That positioning lets srvls complement the authoritative managers rather than
pretend to replace them.

## Research boundaries and evidence policy

This report uses current official documentation and upstream project sources.
Vendor documentation is treated as evidence of documented capability, not as
independent validation of reliability or market adoption. Community projects
such as lazydocker and Process Compose are represented by their own maintained
documentation or repository, which is the primary source for their product
scope.

Statements about what a tool does not explain are bounded in two ways:

1. They refer to the documented scope in the reviewed sources.
2. They distinguish missing product semantics from technical impossibility.
   A user can often build custom integrations, labels, queries, or dashboards;
   that does not mean the base product supplies promise reconciliation.

No market-size estimate, implementation architecture, language choice, storage
design, collector protocol, or TUI framework decision is made here.

## The operator questions and today's nearest answers

| Operator question | Nearest current capability | Residual gap |
| --- | --- | --- |
| What is installed or declared? | systemd unit files, crontabs, supervisor configuration, Compose files, and agent deployment definitions | The declarations live in separate namespaces and do not share a workload identity or operator-level purpose. |
| What is active now? | `systemctl`, supervisor status commands, Docker or Podman listings, CRI inspection, and process monitors | Each answer is scoped to a manager, user, daemon, context, endpoint, or instrumentation boundary. |
| What happened? | journals, process logs, container logs, workflow histories, and agent traces | An event record shows an attempted or completed step in its own system; it does not by itself prove that an external outcome remains true. |
| How is it behaving? | host metrics, process metrics, unit metrics, traces, alerts, and dashboards | Runtime behavior does not encode the operator's intended outcome or the agent's promise. |
| What did the agent do? | agent runs, tool-call spans, handoffs, checkpoints, and execution logs | Platform-local execution history is not a host-wide inventory and may stop at the tool boundary. |
| Did the promised result become and remain true? | Custom checks can be written in many products | The reviewed products do not make cross-manager promise-to-evidence comparison their documented product contract. |
| What changed overnight and what should I read first? | Alerts, live dashboards, and per-system history views | There is no common, bounded morning handoff across host managers and agent runtimes in the reviewed source set. |

## 1. Host service and schedule management

### systemd

The current `systemctl` documentation makes several distinctions that matter
for srvls:

- `list-units` lists units systemd currently has in memory, with active,
  pending, and failed units shown by default.
- `list-unit-files` lists installed unit files and their enablement state.
- `list-timers` exposes the next and previous trigger times and the service a
  timer activates.
- `status` is human-oriented current or most-recent invocation information,
  while `show` is intended for machine-parsable properties.
- `cat` can show backing files and drop-ins, but the files on disk can differ
  from the manager's loaded understanding until a reload.
- system and per-user managers have different unit search paths and therefore
  different inventory scopes.

These are unusually rich primitives: configured state, loaded state,
enablement, runtime state, dependencies, process membership, and recent journal
context can all be inspected. The same documentation also demonstrates why a
single green state is insufficient. Enabled and started are orthogonal; active
and low-level substate are distinct; a unit file on disk can be newer than the
loaded manager state; and units may disappear from in-memory inventory through
garbage collection.

What systemd does not explain is the cross-system purpose of a unit, whether an
agent created or promised it, whether a similarly named container or PM2
application is the same logical workload, or whether the service produced the
external business or operator outcome that motivated it.

### cron

Cronie's upstream manual describes schedules distributed across user crontabs,
`/etc/crontab`, `/etc/cron.d/`, and the spool directory. A crontab expresses
when a command should run and the environment in which cron invokes it. Cron
can route output to mail or syslog, but the schedule itself is not a durable
per-run success record.

For srvls, cron is evidence of declared recurring intent, not evidence that the
last invocation succeeded or that its intended side effect still holds. A
complete inventory also has to distinguish “no entry exists” from “the current
collector could not read another user's or system scope.”

### Adjacent capability and unexplained remainder

| Surface | Strong adjacent capability | What it does not explain |
| --- | --- | --- |
| systemd units | Installed definitions, loaded state, enablement, dependencies, runtime state, process groups, and logs | Cross-manager identity, agent provenance, intended external outcome, or a morning-level change narrative |
| systemd timers | Next and last activation plus the activated unit | Whether the activated work achieved its semantic result |
| Cronie | Distributed recurring command declarations across system and user locations | A normalized run state, durable result, or relationship to another supervisor |
| journal and cgroups | Historical events and process membership within systemd's scope | A promise ledger or proof that an external side effect remains valid |

## 2. Process supervisors and local orchestrators

### PM2

PM2 documents process listing, raw JSON output, per-process detail, logs,
metrics, a terminal monitor, restart and stop actions, ecosystem files, and
startup integration. It can persist a process list for resurrection after a
reboot. It also supports multiple independent daemon instances selected by
`PM2_HOME`.

PM2 therefore gives a strong manager-local operational view. The multiple-home
feature is also direct evidence that “PM2 inventory” is incomplete unless the
instance and owning user are named. PM2 does not document discovery of every
PM2 home on a machine, reconciliation with systemd's wrapper service, or
verification of an agent's claimed external result.

### Supervisor

Supervisor manages programs declared in its configuration. `supervisorctl`
provides status, PID, logs, start, stop, restart, signal, reread, and update
operations against a selected supervisord server. Its status command can
return nonzero when a managed process is not running.

This is useful, authoritative state for one Supervisor server. It is not a
machine-wide process inventory: the client can target a particular server URL
and configuration, and processes outside that supervisord instance are outside
its model.

### Process Compose

Process Compose is a scheduler and orchestrator for non-containerized
applications. Its documented TUI reviews status and logs and can start, stop,
or restart declared processes. The broader product includes dependencies,
health checks, recovery policies, namespaces, scheduled processes, an API, and
read-only mode.

It is a close terminal-interface adjacency because it consolidates status,
logs, and actions. Its organizing object is still a Process Compose project:
it manages what was declared to that orchestrator rather than discovering and
reconciling arbitrary host managers or agent promises.

### Process-supervisor conclusion

The process-supervisor landscape is optimized for owning processes. srvls can
differentiate by owning neither the process nor its lifecycle definition. Its
product value is to expose scope, compare evidence, correlate layers, and
prepare a handoff across managers.

## 3. Container runtime inventory and terminal control

### Docker and Compose

`docker container ls` exposes IDs, images, commands, creation time, status,
ports, names, filters, and structured output. It shows running containers by
default and requires `--all` for stopped containers. Docker also distinguishes
container state from health-check state.

Docker contexts make the scope boundary explicit. One client can point at
multiple local or remote daemons, but commands apply to the active or
explicitly selected context. Docker Compose adds a project/service view:
`docker compose ps` is a snapshot of the current state and ports of services
for the selected Compose project.

These tools answer “what does this daemon or project report?” They do not
answer whether all relevant contexts were scanned, whether a running
container's application-level outcome is correct, or whether the same workload
also appears as a systemd unit, process tree, or agent deployment.

### Podman

Podman is daemonless, supports regular-user operation, and lists running or all
containers in its visible storage. Its `ps` documentation includes pods,
restart counts, host PIDs, labels, namespaces, and a `--sync` option that
forces Podman's state to be updated from the OCI runtime when the two diverge.

That synchronization option is especially relevant evidence for srvls:
manager-reported state and lower-level runtime state can disagree. Podman also
has local and remote connection scopes, and rootless operation makes user
identity part of inventory coverage.

### CRI and Kubernetes nodes

Kubernetes documents `crictl` as a node-level inspection and debugging client
for CRI-compatible runtimes. It can list pods, containers, images, logs, and
runtime information, but it requires a selected runtime endpoint. It is
runtime-facing evidence for a Kubernetes node, not a replacement for the
cluster's desired-state view.

Kubernetes controllers provide the strongest established analogy for
reconciliation: they compare current state with desired state and make changes
to move the system toward the latter. That analogy must be used carefully for
srvls because it implies an active control loop. A read-only comparison and
handoff product should not silently inherit the mutation semantics of a
Kubernetes controller.

### Terminal adjacencies

Lazydocker combines Docker and Compose state, logs, metrics, and common actions
in one terminal UI. Glances combines host resource data, process lists, alerts,
and Docker or Podman container monitoring. Both validate demand for an
at-a-glance terminal experience. Neither source documents a promise model,
cross-manager coverage accounting, or an overnight evidence handoff.

## 4. Observability and runtime inventory

### Metrics and telemetry

OpenTelemetry defines traces, metrics, logs, and baggage as different signals:
a trace follows a request path, a metric is a runtime measurement, and a log
records an event. Its Host Metrics Receiver can collect CPU, load, memory,
disk, filesystem, network, paging, aggregate process, and per-process metrics.

Prometheus node_exporter similarly focuses on hardware and operating-system
metrics. It exposes aggregate process statistics and an optional systemd
collector. The related systemd_exporter deliberately sits between machine-wide
and per-process monitoring, exporting systemd unit state and resource metrics.

These systems are excellent evidence sources. They do not define the semantic
success of an operator task. A low error rate, active unit, completed span, or
normal CPU profile may support a promise, but none is equivalent to the
promise unless the expected outcome has been made explicit.

### Runtime exploration

Netdata documents live process drill-down, grouping by systemd service,
container and VM views, systemd-journal access, and per-unit resource metrics.
Glances provides a cross-platform terminal monitor with processes, containers,
resource views, alerts, APIs, and export integrations.

The distinction from srvls remains temporal and semantic:

- a live monitor answers what is consuming resources now;
- an observability backend answers what signals were emitted over time;
- a reconciliation handoff answers which declared outcomes are supported,
  contradicted, stale, unresolved, or out of observable scope.

### Telemetry is evidence, not ground truth

OpenTelemetry's own semantic conventions are still evolving for generative AI,
and some agent-related attributes have moved to a separate GenAI conventions
repository. This is a warning against making one vendor's span schema the
canonical srvls task model. It also reinforces three product principles:

1. Preserve the source and vocabulary of each observation.
2. Treat missing telemetry as unknown unless coverage proves absence.
3. Do not promote a trace or metric to semantic truth without an explicit
   evidence rule.

## 5. Agent runtimes and control-plane products

### OpenAI Agents SDK

The OpenAI Agents SDK documents built-in tracing for model generations, tool
calls, handoffs, guardrails, audio operations, and custom events. The trace
viewer supports debugging, visualization, and production monitoring of an
agent workflow.

This explains the path through an instrumented SDK run. It does not by itself
enumerate unrelated host processes or prove that a tool's external side effect
continues to exist after the span completes.

### LangSmith Deployment

LangSmith's Agent Server exposes assistants, threads, runs, cron jobs,
persistence, checkpoints, and a task queue. Its control plane manages Agent
Server deployments, revisions, environment variables, logs, and resource and
queue metrics.

This is the closest documented “control plane” adjacency in the reviewed set.
Its boundary is explicit: the deployment is an Agent Server instance, and the
control plane manages those deployments. It does not claim to inventory all
systemd, cron, PM2, Supervisor, Docker, or Podman objects on an operator's
machine.

### CrewAI AMP

CrewAI AMP documents managed deployment, monitoring, scaling, execution traces
and logs, APIs, webhooks, and collaboration for CrewAI crews and agents. It
answers how registered crews execute in its production platform. It does not
document cross-manager host reconciliation or independent verification of
effects beyond the crew's observed execution.

### Amazon Bedrock AgentCore

AgentCore combines a hosted runtime with memory, gateway, identity, built-in
tools, policy, observability, and evaluation capabilities. Its observability
documentation covers traces, logs, session and invocation metrics, latency,
errors, token usage, and OpenTelemetry-compatible export.

This is a broad agent platform rather than a Linux host inventory. Even when
an externally hosted agent emits AgentCore-compatible telemetry, the platform
documents agent execution and resources, not an exhaustive reconciliation of
every local service manager or schedule on the host where a side effect lands.

### Microsoft Foundry Agent Service

Microsoft Foundry Agent Service documents a build, test, trace, evaluate,
publish, and monitor lifecycle. Tracing can expose model calls, tool
invocations, decisions, latency, exceptions, prompts, and retrieval activity.
Some hosted and custom-agent tracing paths are documented as preview.

It is strong evidence that agent operations products are converging on tracing
and monitoring. The source does not describe a morning handoff that compares
agent statements against fresh, cross-manager Linux state.

### Temporal

Temporal is not primarily an agent control plane, but it is an important
durable-runtime adjacency. It persists workflow progress and event history so
modeled workflows can resume after failures. That can establish what a
Temporal workflow recorded. It cannot establish unmodeled host state or the
continued truth of an external side effect without an activity or check that
observes that state.

### Agent-platform conclusion

Agent platforms are becoming good at “what happened inside this run?” They are
not documented as answering the wider host question: “does the machine now
match what agents said they accomplished, across every relevant runtime
boundary?” srvls can occupy that bridge without competing as an agent hosting
platform.

## Capability and whitespace matrix

| Capability | Host managers and supervisors | Container tools | Observability systems | Agent control planes | srvls opportunity |
| --- | --- | --- | --- | --- | --- |
| Manager-local inventory | Strong | Strong | Partial and configuration-dependent | Strong for registered deployments | Preserve each authoritative view and show its scope |
| Declared or desired state | Strong within configuration | Strong within Compose or orchestration definitions | Usually indirect | Strong within agent or workflow definitions | Normalize expectations without erasing source semantics |
| Current runtime state | Strong within manager | Strong within selected endpoint | Strong where collected | Strong within platform | Compare fresh observations across boundaries |
| History | Journals and manager logs | Container logs and events | Strong signal history | Strong traces, runs, and checkpoints | Bind history to a handoff window and expected outcome |
| Performance | Partial | Partial | Strong | Strong for platform workloads | Use performance as supporting evidence, not semantic success |
| Agent intent or promise | Absent | Absent | Absent unless custom attributes are added | Partial in instructions, run state, and outputs | Capture a testable operator-facing promise |
| External outcome verification | Custom and local | Custom and local | Custom checks | Tool- or application-specific | Make promise-to-evidence comparison a first-class workflow |
| Cross-manager identity | Weak | Project- or label-local | Correlation depends on metadata | Platform-local | Correlate layered objects while retaining raw identities |
| Coverage and unknowns | Tool-specific errors | Context and endpoint dependent | Instrumentation dependent | Registration dependent | Report unreachable, unauthorized, unscanned, and stale scopes |
| Morning handoff | Not a primary product view | Not a primary product view | Alerts and dashboards, not a common handoff | Run dashboards, not host reconciliation | Prioritized delta with evidence and unresolved questions |

## What the adjacent products do not explain

Across the reviewed source set, the recurring unanswered questions are:

1. **Purpose:** Why does this runtime object exist, and which operator outcome
   is it meant to maintain?
2. **Promise:** What exactly did an agent claim would be true, by when, and in
   which scope?
3. **Persistence of outcome:** Does the claimed side effect still exist now,
   rather than merely having produced a successful tool call or exit code?
4. **Coverage:** Is an object absent, or was its manager, user, daemon,
   endpoint, credential, or telemetry source not observed?
5. **Layering:** Are a systemd unit, PM2 application, container, and OS process
   separate workloads or different representations of one workload?
6. **Overnight change:** Which observations are new, removed, degraded,
   recovered, contradicted, or stale since the last accepted handoff?
7. **Operator priority:** Which discrepancies require action now, which are
   informational, and which need more evidence?
8. **Action safety:** If an operator acts through one manager, what adjacent
   manager can recreate, restart, or still depend on the target?

These are product semantics. They are not solved merely by collecting more
fields.

## Terminology risks

| Term | Existing collision | Product risk | Recommended srvls meaning |
| --- | --- | --- | --- |
| Agent | LLM persona, SDK object, deployed service, background worker, or human representative | Users may assume all “agents” share one runtime or identity model | A named actor that emits a claim or performs work; always retain provider and runtime identity |
| Runtime | Language VM, container runtime, agent SDK loop, hosted agent service, or the current state of a process | “Runtime inventory” can imply a much narrower layer than intended | The observed execution environment, qualified by kind and scope |
| Task, job, run, process | Each manager gives these words different lifecycle semantics | False equivalence across systemd jobs, cron entries, PIDs, containers, and agent runs | Preserve source-native terms; use “work item” only as a neutral umbrella |
| Promise | SLA, guarantee, future, or informal conversational statement | Overstates confidence or creates legal and reliability implications | A recorded, testable claim of an intended observable outcome; not a guarantee |
| Reconciliation | In Kubernetes, a controller normally acts to move current state toward desired state | Users may expect autonomous mutation | Comparison of expected and observed state; mutation is separate and explicit |
| Desired state | A formal declarative spec in orchestration systems | An agent sentence may be mistaken for an authoritative desired-state declaration | Use “expected outcome” unless authority and ownership are explicit |
| Running | PID exists, container state is running, unit is active, or workflow has not completed | Encourages “running equals healthy equals correct” | A source-native lifecycle observation, never semantic success by itself |
| Healthy | Health-check pass, no alert, active unit, or business success | Collapses liveness, readiness, performance, and outcome | Qualify the dimension: lifecycle, liveness, readiness, resource, or outcome |
| Inventory | Installed definitions, loaded objects, running objects, or retained historical entities | A list can appear exhaustive when it is only a selected scope | A timestamped set with explicit source, scope, filters, and collection result |
| Trace | Request path, agent run, audit history, or arbitrary event sequence | A trace may be treated as complete, durable, or independently verified | An execution signal from an instrumented boundary; evidence, not proof |
| Control plane | A system that has authority to deploy, configure, or reconcile resources | Mispositions a read-first terminal product as the owner of workloads | Avoid as the primary category unless srvls actually owns lifecycle authority |
| Handoff | Agent-to-agent delegation, human shift change, or conversation transfer | Product intent can be confused with SDK handoffs | A bounded operator briefing that transfers current evidence and unresolved work |
| Verified | Cryptographic proof, test pass, source agreement, or manual review | Sounds absolute despite stale or partial evidence | Prefer “supported by fresh evidence”; show source, time, and rule |
| Unknown | Missing object, failed collector, denied access, or unsupported source | Unknowns may be hidden as empty results | A first-class result with an explicit reason |

### Recommended reconciliation outcomes

The least misleading outcome vocabulary is:

- **Supported:** fresh evidence matches the testable expected outcome.
- **Contradicted:** fresh evidence conflicts with the expected outcome.
- **Unresolved:** available evidence is insufficient or ambiguous.
- **Stale:** relevant evidence exists but is outside the accepted freshness
  window.
- **Out of scope:** a required source, identity, manager, endpoint, or
  permission was not included or could not be reached.

“Succeeded” and “failed” should remain source-native lifecycle states unless a
product requirement explicitly defines the semantic outcome test.

## Evidence-backed differentiation opportunities

### 1. Promise-to-observation reconciliation

**Evidence:** Agent platforms retain runs, traces, tool calls, and checkpoints;
host managers retain runtime state. The reviewed products document these as
separate scopes.

**Opportunity:** Let an operator record or import a testable claim and compare
it with fresh observations from the systems where the claimed effect should be
visible.

**Confidence:** High that the documented scopes are separate; medium that this
is durable market whitespace beyond the reviewed set.

### 2. Coverage honesty as a feature

**Evidence:** systemd has system and user managers; PM2 can have multiple homes;
Docker has selectable contexts; Podman can be rootless or remote; CRI requires
an endpoint; telemetry requires instrumentation.

**Opportunity:** Make coverage, permissions, timeouts, unsupported sources,
and stale evidence visible beside every conclusion. “Not observed” must not be
silently rendered as “does not exist.”

**Confidence:** High.

### 3. Layer-aware workload correlation

**Evidence:** PM2 commonly integrates with systemd startup; containers expose
host PIDs and cgroup membership; systemd groups processes; observability tools
use their own grouping models.

**Opportunity:** Show when multiple raw runtime objects appear to represent one
logical workload, while preserving every raw identity and making uncertain
matches inspectable.

**Confidence:** High that duplication exists; medium for automatic correlation
quality because local naming and metadata vary.

### 4. Morning delta rather than another live dashboard

**Evidence:** PM2 monit, Process Compose, lazydocker, Glances, Netdata, and
agent control planes already provide live operational views. Their documented
center of gravity is current operation, tracing, or monitoring.

**Opportunity:** Optimize the default experience for a bounded handoff window:
new promises, changed evidence, contradictions, recoveries, new unknowns, and
items that need an operator decision.

**Confidence:** Medium. The source set demonstrates strong live-view supply but
does not constitute exhaustive competitive research for handoff products.

### 5. Evidence drill-down without control-plane pretense

**Evidence:** Authoritative managers already provide status and lifecycle
actions. Kubernetes and LangSmith use “control plane” for systems that manage
state and deployments.

**Opportunity:** Lead with explanation and provenance. Every summary should
drill down to the source-native observation, scope, collection time, and error.
Any lifecycle action should be explicitly separate from reconciliation.

**Confidence:** High.

### 6. Cross-runtime postcondition checks

**Evidence:** A tool call, process exit, workflow event, or completed span
records activity within one system. Podman's explicit state synchronization
and systemd's disk-versus-loaded distinction show that even runtime managers
can hold divergent views.

**Opportunity:** Allow a promise to name the evidence that must be rechecked
after work completes and again at handoff time.

**Confidence:** High for the technical need; medium for how often users will
provide sufficiently testable promises.

### 7. A stable product vocabulary above unstable schemas

**Evidence:** Managers overload state terms, and OpenTelemetry's GenAI
conventions are evolving.

**Opportunity:** Keep a small operator vocabulary for evidence and
reconciliation while retaining source-native fields. Avoid binding product
meaning to any one agent framework's run or span schema.

**Confidence:** High.

## Candidate product requirements

The following are mechanism-neutral requirements suggested by the research.
They are candidates for later PRD review, not adopted requirements in this
report.

1. A handoff must state the evidence window, collection time, source scopes,
   and freshness status.
2. A recorded promise must identify a testable expected outcome, relevant
   scope, and evidence condition, or be marked untestable.
3. Reconciliation must distinguish supported, contradicted, unresolved, stale,
   and out-of-scope outcomes.
4. A collection error, denied scope, unavailable daemon, or unsupported source
   must never be represented as an empty authoritative inventory.
5. The default handoff must prioritize changes and decisions over unchanged
   healthy detail.
6. Every summarized conclusion must be inspectable back to source-native
   observations and collection errors.
7. Layered or duplicate-looking runtime objects must retain their original
   identities even when grouped as one logical workload.
8. “Running,” “healthy,” “completed,” and “tool call succeeded” must not be
   treated as proof of an external outcome without an explicit evidence rule.
9. Reconciliation must be observational by default. Any mutation must be a
   separate, explicit operator action with scope and a post-action recheck.
10. The handoff must remain useful when some sources are missing by surfacing
    uncertainty instead of fabricating completeness.

## Implementation mechanisms explicitly not selected

The requirements above do not decide:

- programming language, terminal UI library, or process architecture;
- direct command execution versus D-Bus, sockets, APIs, files, or libraries;
- snapshot format, database, retention engine, or cache design;
- polling, event subscription, scheduled collection, or hybrid collection;
- deterministic rules, user-authored checks, model-assisted interpretation, or
  any combination of them;
- collector plug-in boundaries or which managers ship in an initial release;
- exact workload-correlation or deduplication algorithm;
- OpenTelemetry, Prometheus, journal, or another telemetry backend;
- agent framework integration protocol;
- privilege escalation, remote execution, or credential strategy.

Those are architecture and implementation choices. They should be evaluated
only after the product contract identifies the evidence, scope, freshness, and
operator outcomes required.

## Positioning implications

The least risky category language is:

**srvls is an evidence-backed morning reconciliation surface for
agent-operated Linux hosts.**

Supporting language can describe it as a terminal product that:

- unifies scoped observations without claiming to replace their managers;
- compares agent-declared expected outcomes with live runtime evidence;
- highlights overnight deltas, contradictions, and unknowns;
- preserves provenance so an operator can trust or challenge every conclusion.

Avoid leading with:

- **universal process manager**, because srvls does not need to own processes;
- **observability platform**, because metrics and traces are inputs rather than
  the primary outcome;
- **agent control plane**, because that implies deployment and reconciliation
  authority;
- **AI ops copilot**, because it obscures the concrete evidence contract;
- **single source of truth**, because the authoritative truth remains
  distributed among managers and external systems.

The defensible promise is not omniscience. It is an honest, inspectable account
of what was checked, what the evidence supports, what it contradicts, and what
could not be known before the operator starts the day.

## Source register

All sources below were accessed on **2026-07-16**.

### systemd and scheduling

| Source title | Publisher or upstream | Relevance | Accessed |
| --- | --- | --- | --- |
| [systemctl — Control the systemd system and service manager](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html) | systemd / freedesktop.org | Loaded units, installed files, timer inventory, status, machine-readable properties, dependencies, and actions | 2026-07-16 |
| [systemd.unit — Unit configuration](https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html) | systemd / freedesktop.org | Unit types, system and user search paths, dependency semantics, drop-ins, garbage collection, and loaded-state caveats | 2026-07-16 |
| [systemd-cgls — Recursively show control group contents](https://www.freedesktop.org/software/systemd/man/latest/systemd-cgls.html) | systemd / freedesktop.org | Unit and process membership through the cgroup hierarchy | 2026-07-16 |
| [journalctl — Print log entries from the systemd journal](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html) | systemd / freedesktop.org | Historical log evidence scoped to units and boots | 2026-07-16 |
| [crontab(5) — files used to schedule the execution of programs](https://man7.org/linux/man-pages/man5/crontab.5.html) | Cronie upstream manual, rendered by man7.org | User and system schedule declarations, environment, locations, and time semantics | 2026-07-16 |
| [cron(8) — daemon to execute scheduled commands](https://man7.org/linux/man-pages/man8/cron.8.html) | Cronie upstream manual, rendered by man7.org | Cron discovery locations, daemon behavior, logging, and change detection | 2026-07-16 |

### Process supervisors and terminal orchestrators

| Source title | Publisher or upstream | Relevance | Accessed |
| --- | --- | --- | --- |
| [PM2 Process Management Quick Start](https://pm2.keymetrics.io/docs/usage/quick-start/) | PM2 | Process lists, JSON output, logs, metrics, terminal monitor, actions, ecosystem files, and startup | 2026-07-16 |
| [PM2 Advanced Topics](https://pm2.keymetrics.io/docs/usage/specifics/) | PM2 | Multiple PM2 daemon instances selected by `PM2_HOME` | 2026-07-16 |
| [Running Supervisor — Supervisor 4.3.0 documentation](https://supervisord.org/running.html) | Supervisor | Manager-scoped status, process control, logs, configuration, and server targeting | 2026-07-16 |
| [Process Compose](https://f1bonacc1.github.io/process-compose/) | Process Compose | Non-containerized scheduling, dependencies, recovery, health, TUI, API, and namespaces | 2026-07-16 |
| [Process Compose TUI](https://f1bonacc1.github.io/tui/) | Process Compose | Status, logs, start, stop, and restart in a terminal interface | 2026-07-16 |

### Containers and node runtime inventory

| Source title | Publisher or upstream | Relevance | Accessed |
| --- | --- | --- | --- |
| [docker container ls](https://docs.docker.com/reference/cli/docker/container/ls/) | Docker | Running versus all containers, lifecycle and health filters, structured output, and object fields | 2026-07-16 |
| [Docker contexts](https://docs.docker.com/engine/manage-resources/contexts/) | Docker | Client-to-daemon scope, local and remote endpoints, and explicit context selection | 2026-07-16 |
| [How Compose works](https://docs.docker.com/compose/intro/compose-application-model/) | Docker | Compose project model and `docker compose ps` state snapshot | 2026-07-16 |
| [podman-ps — Print out information about containers](https://docs.podman.io/en/latest/markdown/podman-ps.1.html) | Podman | User-visible container inventory, pods, host PIDs, restart counts, and runtime synchronization | 2026-07-16 |
| [podman — Simple management tool for pods, containers and images](https://docs.podman.io/en/latest/markdown/podman.1.html) | Podman | Daemonless and rootless operation, remote connections, pods, and systemd integration | 2026-07-16 |
| [Debugging Kubernetes nodes with crictl](https://kubernetes.io/docs/tasks/debug/debug-cluster/crictl/) | Kubernetes | CRI endpoint-scoped pods, containers, images, logs, and node runtime debugging | 2026-07-16 |
| [Controllers](https://kubernetes.io/docs/concepts/architecture/controller/) | Kubernetes | Established desired-versus-current-state and active reconciliation semantics | 2026-07-16 |
| [lazydocker](https://github.com/jesseduffield/lazydocker) | lazydocker upstream | Docker and Compose state, logs, metrics, and lifecycle actions in a terminal UI | 2026-07-16 |

### Observability and runtime exploration

| Source title | Publisher or upstream | Relevance | Accessed |
| --- | --- | --- | --- |
| [Signals](https://opentelemetry.io/docs/concepts/signals/) | OpenTelemetry | Distinctions among traces, metrics, logs, and baggage | 2026-07-16 |
| [Important Components for Kubernetes — Host Metrics Receiver](https://opentelemetry.io/docs/platforms/kubernetes/collector/components/) | OpenTelemetry | Host and per-process metric scrapers and collection scope | 2026-07-16 |
| [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/) | OpenTelemetry | Cross-platform naming and the evolving status of GenAI conventions | 2026-07-16 |
| [Node exporter](https://github.com/prometheus/node_exporter) | Prometheus | Machine metrics, aggregate process statistics, and optional systemd status | 2026-07-16 |
| [Systemd exporter](https://github.com/prometheus-community/systemd_exporter) | Prometheus Community | Per-unit state and resources between node-wide and per-process granularity | 2026-07-16 |
| [Function: Top / Processes](https://learn.netdata.cloud/docs/live-view/processes) | Netdata | Live processes, systemd-service grouping, containers, connections, and journal drill-down | 2026-07-16 |
| [Systemd Services](https://learn.netdata.cloud/docs/collecting-metrics/collectors/operating-systems/systemd-services) | Netdata | Per-systemd-service cgroup resource metrics | 2026-07-16 |
| [Glances — An Eye on your system](https://nicolargo.github.io/glances/) | Glances upstream | Cross-platform terminal process, host, container, alert, API, and export capabilities | 2026-07-16 |

### Agent runtimes and control planes

| Source title | Publisher or upstream | Relevance | Accessed |
| --- | --- | --- | --- |
| [Tracing — OpenAI Agents SDK](https://openai.github.io/openai-agents-python/tracing/) | OpenAI | Model, tool, handoff, guardrail, custom-event, and workflow tracing | 2026-07-16 |
| [Agent Server](https://docs.langchain.com/langsmith/agent-server) | LangChain | Assistants, threads, runs, cron jobs, checkpoints, persistence, and task queues | 2026-07-16 |
| [LangSmith control plane](https://docs.langchain.com/langsmith/control-plane) | LangChain | Deployment, revision, log, resource, restart, queue, and API management | 2026-07-16 |
| [CrewAI AMP](https://docs.crewai.com/enterprise/introduction) | CrewAI | Managed crew deployment, monitoring, scaling, traces, logs, APIs, and webhooks | 2026-07-16 |
| [Host agent or tools with Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) | Amazon Web Services | Agent hosting, sessions, identity, protocol support, and built-in tracing | 2026-07-16 |
| [Observe your agent applications on Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) | Amazon Web Services | Agent traces, logs, workflow steps, sessions, latency, errors, and OpenTelemetry-compatible signals | 2026-07-16 |
| [What is Microsoft Foundry Agent Service?](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) | Microsoft | Managed agent build, test, trace, evaluate, publish, and monitor lifecycle | 2026-07-16 |
| [Set up tracing in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup) | Microsoft | Agent telemetry coverage, storage, and preview boundaries | 2026-07-16 |
| [Temporal Platform Documentation](https://docs.temporal.io/) | Temporal | Durable workflow execution and failure recovery | 2026-07-16 |
| [Temporal History Service architecture](https://github.com/temporalio/temporal/blob/main/docs/architecture/history-service.md) | Temporal upstream | Workflow event history as the recoverable state of a modeled execution | 2026-07-16 |
