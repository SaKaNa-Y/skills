---
name: just-use-it
description: Experience a source-accessible library or developer tool through outcome-oriented slices before reading its implementation, and report honest coverage and observable findings without repairing or publishing them.
disable-model-invocation: true
---

# Just Use It

Use first. Read source last.

Run a **Usage-First Audit** of one source-accessible library, framework, CLI, or developer tool. Exercise its **Capability Surface** through the interfaces a user receives, then inspect the source to find public capabilities and relevant runnable repository environments the hands-on passes missed.

The audit owns experience, coverage evidence, and Finding Packets. Use [assess-findings](../assess-findings/SKILL.md) for evidence qualification and action recommendations, including bounded investigation when a missing fact could change the recommendation. Install it with its `investigate-with-evidence` dependency. If either is unavailable, continue feasible usage and preserve unassessed packets with the missing dependency; assessment remains pending. Product repair and tracker writes require separate authorization. A co-active `$yak-shaving-triage` owns tracker reconciliation and approved recording.

Work **slice-first**. Each execution agent completes one user-outcome **Capability Journey**, its Discriminating Variation, and the applicable exploration within its assigned Capability Group. Independent slices may run concurrently through the delegated workflow below. Opening an entry point or container verifies only that entry point; it does not verify the capabilities inside it.

## 1. Frame and Isolate

Identify the target, its intended user, its user-facing documentation, and the environment needed to exercise it. Infer these from the request and workspace; ask only when more than one materially different target remains.

Establish which revision, release, or running instance the request concerns. When the current checkout is the audit target and no other version is specified, prefer its documented build over an unrelated installed release. An explicit release or instance request takes precedence. Before crediting behavior, confirm the effective executable, imported package, or deployment through available launch or identity metadata. Scope observations to what actually ran; unknown source correspondence limits source attribution, not direct observation.

Keep behavioral implementation source and the target project's issue tracker closed during the first two passes. Follow repository instructions and read public documentation plus entrypoint metadata needed to launch the tool. If the documented launch path fails, preserve that result before using operational metadata to make the target runnable; implementation remains closed until the source pass.

Source-closed means behaviorally blind, not safety-blind. Inspect the minimum install hooks, launch scripts, permissions, and external effects needed to decide whether execution is safe, without using them to infer product behavior. If safe execution requires broader source inspection, disclose that the blind sequence cannot be preserved rather than claiming a Usage-First Audit followed it.

For CLI, public API, or package use, read [references/programmatic-experience.md](references/programmatic-experience.md) before consumer setup, installation, or first invocation, including help and version probes.

When a required runtime, compiler toolchain, SDK, system package, container runtime, or similar prerequisite is absent, read [references/prerequisites.md](references/prerequisites.md) before installing anything or abandoning the affected capability.

Prefer disposable state:

- When the user explicitly opened a browser or tab and asked to use it, select that existing session before creating another.
- Keep the target checkout's tracked files unchanged. Use an existing safe running instance, a disposable copy or worktree, or a consumer workspace outside the target as appropriate.
- Record every temporary path, process, server, and browser context created by the audit so the exact resources can be cleaned on completion, failure, or interruption.
- Keep external effects inside disposable projects, test data, or sandboxes. Preserve every existing authorization checkpoint; mark a capability Blocked when it cannot be exercised safely.

**Complete when:** the target and its runtime correspondence or uncertainty, public starting material, browser choice, isolation boundary, cleanup targets, and every known prerequisite decision are explicit.

## 2. Map the Documented Surface

Build the initial Capability Surface from public documentation without reading behavioral implementation source. Give every documented capability the initial state `Not Exercised`.

Group Capability Journeys by the user outcome they serve, not by their panel, route, menu, command group, or documentation section. Order the groups by the product's primary user tasks. Start a compact **Coverage Ledger** with each known Capability Group, its intended outcome, interfaces and modes, current state, and next action.

Keep implementation source and the target issue tracker closed. Source-closed means behaviorally blind: public documentation and the entrypoint metadata needed for safe launch remain available.

**Complete when:** every documented capability belongs to a user-outcome group, every group starts as `Not Exercised`, and the first Vertical Capability Slice is explicit.

## 3. Complete Vertical Slices

Before assigning or executing slices, read [references/delegated-usage.md](references/delegated-usage.md). By default, the main agent delegates actual product use to fresh subagents, with at most two Just Use It subagents running concurrently unless the user explicitly requests more. This limit belongs to Just Use It; it does not include workers of separately active skills. Assign existing Vertical Capability Slices in priority order, parallelizing only independent work. When delegation is unavailable, retain the same method on the main agent and state that limitation.

An assigned worker follows this skill within its slice; it does not restart the whole audit or delegate again. During the initial source-blind pass, keep implementation source and the target issue tracker closed across all agents. Later assignments retain the audit's established source/tracker phase and provenance rather than restarting the blind sequence. For each assigned Capability Group:

When the group uses an interactive UI, read [references/ui-experience.md](references/ui-experience.md) before controlling it. Complete its **UI Journey Gate** before assigning terminal states to the slice; that reference defines the required observations and the exclusion and `Blocked` paths.

1. Follow its documented Capability Journey exactly through the public interface until it produces an observable user result.
2. Exercise one Discriminating Variation that changes a single input, state, mode, or recovery condition and should produce an observably different result. Record an explicit exclusion when the capability has no material variation.
3. Read [references/exploration-lenses.md](references/exploration-lenses.md), then explore freely inside the active Capability Group. Build a small capability-shaped matrix and continue until further public actions repeat known states instead of revealing another capability, transition, or interaction.
4. Add newly discoverable public capabilities to the Capability Surface. Keep capabilities serving the active outcome in the current slice; add independently useful outcomes to the Coverage Ledger as new `Not Exercised` groups.
5. Before assigning the first `Verified` state, read [references/verification-traces.md](references/verification-traces.md). A capability becomes `Verified` only with a complete Verification Trace. As soon as behavior may be a finding, read [references/finding-packets.md](references/finding-packets.md), preserve its evidence, and hand it to the coordinator for early assessment. Continue usage while the assessor reviews the packet under the current source/tracker phase.
6. Give every capability in the slice a terminal state and return its evidence to the main agent. The main agent checks the handoff, updates the Coverage Ledger, and retires the worker before assigning a new slice to a fresh subagent. `Verified`, `Finding`, `Observed`, and `Blocked` are terminal for usage; `Observed` means the journey was exercised but its problem or improvement judgment is pending. Assessment status remains separate from usage completion; `Not Exercised` remains pending.

Continue across completed slices under the existing authorization while known in-scope capabilities remain feasible. Use slice boundaries for progress updates; a Partial Audit describes incomplete coverage rather than a reason to end the task. End an incomplete audit when the user asks to stop or narrow the scope, or when no meaningful in-scope progress remains possible without unavailable prerequisites, access, or user input. Continue other feasible work when one capability is Blocked. Preserve remaining coverage and resumption conditions when ending. A temporary pause that will resume before tracker reconciliation keeps the target tracker closed. When interruption instead concludes the run with known capabilities `Not Exercised`, preserve the current slice and next action, freeze completed Finding Packets, and report a Partial Audit. A separately active recording workflow may reconcile those frozen packets; audit work after it reads tracker history, including any later resume, is tracker-informed rather than behaviorally blind.

A documentation error is a Finding even when the implementation works through an undocumented correction. Do not use operational metadata or source knowledge to silently rescue a documented journey.

**Complete when:** every capability discoverable without source has a terminal state, every materially applicable exploration lens has an exercised path or explicit exclusion, every `Verified` capability has a Verification Trace, and further hands-on exploration is behaviorally redundant.

## 4. Reconcile with Source

The main agent opens implementation source after all hands-on workers have handed back their slices and the preceding usage completion criterion holds. Announce this phase change to assessment workers; tracker history remains closed. Match source to the experienced artifact where possible and qualify leads from other revisions until exercised on their own artifacts.

Inspect public exports, routes, commands, flags, feature registration, examples, and tests for shipped public capabilities missing from coverage. Treat shipped exports, executables, routes, or browser globals as public unless marked internal, test-only, or unreleased; a hidden help entry alone does not establish privacy. Report unresolved public intent explicitly.

Read [references/repository-environments.md](references/repository-environments.md) to discover runnable repository environments that expose additional capability journeys, component states, or integrations. These environments can provide useful experience without themselves being end-user releases. Keep their evidence scope distinct from the product paths they represent.

Map source-discovered capabilities and relevant environments to existing coverage, a justified exclusion, or newly assigned usage. Complete new slices through the delegated workflow and record their source-discovered provenance. Source inspection supplies leads; actual execution supplies usage evidence. Assessment workers may now investigate source-dependent questions within their assigned recommendation scope while usage workers continue independent slices.

After every source-confirmed public entrypoint and relevant environment is accounted for through usage or explicit exclusion, freeze the independently observed packets and open the Audit Reconciliation Gate. A co-active recording workflow can reconcile the batch and return evidence to the assigned assessor. Without Yak, the assessor may perform the bounded read-only tracker check allowed by its method. Reading tracker history marks subsequent work tracker-informed; a new worker does not restore blind provenance.

Public issue history may also be sampled after the gate as a final coverage calibration. Re-exercise relevant public paths; behavior first encountered there is a known-issue reproduction rather than independent discovery.

**Complete when:** source-discovered coverage is accounted for, all usage slices have a terminal state, and packet provenance and reconciliation eligibility are explicit. Assessment can remain pending on a named prerequisite without blocking the usage phase transition.

## 5. Report and Clean Up

Collect assessment results before the final report using [finding handoff](references/finding-packets.md#hand-off-for-assessment-and-reconciliation). Return a conversational audit report containing:

- the intended target, the artifact or instance actually exercised, and the environment;
- the Coverage Ledger and Capability Surface with each state;
- a compact Verification Trace for every `Verified` capability;
- assessed findings, improvement opportunities, unresolved observations, and excluded claims with their evidence and distinct action recommendations;
- Blocked and, for a partial run, Not Exercised capabilities;
- tracker links or identifiers returned by a separately active recording workflow for Reused records or successfully published mutations; and
- cleanup results.

When any known capability remains `Not Exercised`, call the result a **Partial Audit**. Name the completed Vertical Capability Slices, but do not describe the whole Capability Surface as complete.

Keep the report conversational unless the user explicitly requests a repository artifact. When asked to save it, use the exact requested destination and repository conventions. Persistent finding publication remains outside this skill.

Before ending the audit, stop or retire all audit workers and collect their resource states. Before deleting disposable state, move required evidence into the conversation, the requested report, or an independently authorized recording workflow. Then remove only the exact temporary paths and stop only the processes, servers, tabs, or browser contexts created for this audit. Preserve user-owned browser state. Report every cleanup failure with the residual path or running resource.

**Complete when:** the report's coverage claims match the ledger, every packet has an assessment or an explicit missing-evidence or dependency limitation, and every disposable path and running resource is removed or reported as residual state.
