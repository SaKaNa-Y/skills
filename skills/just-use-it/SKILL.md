---
name: just-use-it
description: Experience a source-accessible library or developer tool through outcome-oriented slices before reading its implementation, and report honest coverage and observable findings without repairing or publishing them.
disable-model-invocation: true
---

# Just Use It

Use first. Read source last.

Run a **Usage-First Audit** of one source-accessible library, framework, CLI, or developer tool. Exercise its **Capability Surface** through the interfaces a user receives, then inspect the source only to find public capabilities the hands-on passes missed.

The audit owns experience, coverage evidence, and session-scoped Finding Packets. It does not diagnose or repair findings, create or update tracker entries, or claim source inspection as usage. A user may separately invoke a recording workflow such as `$yak-shaving-triage`; co-use keeps both skills independent.

Work **slice-first**. Complete one user-outcome **Capability Journey**, its Discriminating Variation, and the applicable exploration before moving to another Capability Group. Opening an entry point or container verifies only that entry point; it does not verify the capabilities inside it.

## 1. Frame and Isolate

Identify the target, its intended user, its user-facing documentation, and the environment needed to exercise it. Infer these from the request and workspace; ask only when more than one materially different target remains.

Keep behavioral implementation source and the target project's issue tracker closed during the first two passes. Follow repository instructions and read public documentation plus entrypoint metadata needed to launch the tool. If the documented launch path fails, preserve that result before using operational metadata to make the target runnable; implementation remains closed until the source pass.

Source-closed means behaviorally blind, not safety-blind. Inspect the minimum install hooks, launch scripts, permissions, and external effects needed to decide whether execution is safe, without using them to infer product behavior. If safe execution requires broader source inspection, disclose that the blind sequence cannot be preserved rather than claiming a Usage-First Audit followed it.

When a required runtime, compiler toolchain, SDK, system package, container runtime, or similar prerequisite is absent, read [references/prerequisites.md](references/prerequisites.md) before installing anything or abandoning the affected capability.

Prefer disposable state:

- When the user explicitly opened a browser or tab and asked to use it, select that existing session before creating another.
- Keep the target checkout's tracked files unchanged. Use an existing safe running instance, a disposable copy or worktree, or a consumer workspace outside the target as appropriate.
- Record every temporary path, process, server, and browser context created by the audit so the exact resources can be cleaned on completion, failure, or interruption.
- Keep external effects inside disposable projects, test data, or sandboxes. Preserve every existing authorization checkpoint; mark a capability Blocked when it cannot be exercised safely.

**Complete when:** the target, public starting material, browser choice, isolation boundary, cleanup targets, and every known prerequisite decision are explicit.

## 2. Map the Documented Surface

Build the initial Capability Surface from public documentation without reading behavioral implementation source. Give every documented capability the initial state `Not Exercised`.

Group Capability Journeys by the user outcome they serve, not by their panel, route, menu, command group, or documentation section. Order the groups by the product's primary user tasks. Start a compact **Coverage Ledger** with each known Capability Group, its intended outcome, interfaces and modes, current state, and next action.

Keep implementation source and the target issue tracker closed. Source-closed means behaviorally blind: public documentation and the entrypoint metadata needed for safe launch remain available.

**Complete when:** every documented capability belongs to a user-outcome group, every group starts as `Not Exercised`, and the first Vertical Capability Slice is explicit.

## 3. Complete Vertical Slices

Keep implementation source and the target issue tracker closed while completing the hands-on slices. For each Capability Group, in priority order:

When the group uses an interactive UI, read [references/ui-experience.md](references/ui-experience.md) before controlling it. Do not terminalize an interactive slice until its **UI Journey Gate** closes: relevant nested controls and scroll boundaries, material rendered interaction states, browser- or operating-system-native overlays, and applicable sibling visual modes all need observable evidence or an explicit exclusion or `Blocked` reason. When document-level browser capture omits a material native overlay, use an available authorized full-window or screen-level observation; if it remains unavailable, mark that visual evidence `Blocked` instead of inferring its appearance.

When the target has no UI, or its UI leaves part of the surface accessible only through a CLI or public API, read [references/programmatic-experience.md](references/programmatic-experience.md) before creating a consumer workspace.

1. Follow its documented Capability Journey exactly through the public interface until it produces an observable user result.
2. Exercise one Discriminating Variation that changes a single input, state, mode, or recovery condition and should produce an observably different result. Record an explicit exclusion when the capability has no material variation.
3. Read [references/exploration-lenses.md](references/exploration-lenses.md), then explore freely inside the active Capability Group. Build a small capability-shaped matrix and continue until further public actions repeat known states instead of revealing another capability, transition, or interaction.
4. Add newly discoverable public capabilities to the Capability Surface. Keep capabilities serving the active outcome in the current slice; add independently useful outcomes to the Coverage Ledger as new `Not Exercised` groups.
5. Before assigning the first `Verified` state, read [references/verification-traces.md](references/verification-traces.md). A capability becomes `Verified` only with a complete Verification Trace. As soon as behavior may be an Audit Finding, read [references/finding-packets.md](references/finding-packets.md) before expanding the investigation.
6. Give every capability in the slice a terminal state, update the Coverage Ledger, and only then move to the next group. `Verified`, `Finding`, and `Blocked` are terminal; `Not Exercised` remains pending.

For a large surface, complete coherent slices without asking the user to approve each group. Use slice boundaries as pause points. A temporary pause that will resume before tracker reconciliation keeps the target tracker closed. When interruption instead concludes the run with known capabilities `Not Exercised`, preserve the current slice and next action, freeze completed Finding Packets, and report a Partial Audit. A separately active recording workflow may reconcile those frozen packets; audit work after it reads tracker history, including any later resume, is tracker-informed rather than behaviorally blind.

A documentation error is a Finding even when the implementation works through an undocumented correction. Do not use operational metadata or source knowledge to silently rescue a documented journey.

**Complete when:** every capability discoverable without source has a terminal state, every materially applicable exploration lens has an exercised path or explicit exclusion, every `Verified` capability has a Verification Trace, and further hands-on exploration is behaviorally redundant.

## 4. Reconcile with Source

Open the implementation source only now. Inspect public exports, routes, commands, flags, feature registration, examples, and tests to find shipped public capabilities missing from the current surface. Treat a capability reachable through a shipped package export, executable, route, or browser global as public unless the project marks it internal, test-only, or unreleased. A hidden help entry is a discoverability signal, not by itself proof that the capability is private. Report unresolved public intent explicitly.

Map every source-confirmed public entrypoint to an existing capability, an explicit exclusion, or a newly added capability. Exercise every newly added capability through the interface available to a user. Treat source evidence as a lead: observable use confirms a Finding; source-only suspicion remains an unverified lead in the report.

Group newly added capabilities by user outcome and complete them slice-first. Label their Verification Traces as source-discovered so they do not masquerade as blind discovery.

After every source-confirmed public entrypoint is accounted for, freeze the independently observed Finding Packets. This opens the Audit Reconciliation Gate for a separately active recording workflow, which owns batch reconciliation and tracker writes; matching an existing record does not change the finding's independent provenance.

After the source surface is accounted for, the target project's public issue history may be sampled as a final coverage calibration. Re-exercise relevant paths through the public interface. Label behavior first encountered there as a known-issue reproduction rather than independent discovery, and keep issue reading separate from tracker mutation or publication.

**Complete when:** every source-confirmed public entrypoint is accounted for, every included capability has a terminal state, and the independently observed Finding Packets are frozen.

## 5. Report and Clean Up

Return a conversational audit report containing:

- the target and environment;
- the Coverage Ledger and Capability Surface with each state;
- a compact Verification Trace for every `Verified` capability;
- functional, documentation, visual, interaction, operational, Capability Gap, and Intermittent Findings with their evidence;
- Blocked and, for a partial run, Not Exercised capabilities;
- tracker links or identifiers returned by a separately active recording workflow for Reused records or successfully published mutations; and
- cleanup results.

When any known capability remains `Not Exercised`, call the result a **Partial Audit**. Name the completed Vertical Capability Slices, but do not describe the whole Capability Surface as complete.

Keep the report conversational unless the user explicitly requests a repository artifact. When asked to save it, use the exact requested destination and repository conventions. Persistent finding publication remains outside this skill.

Before deleting disposable state, move required evidence into the conversation, the requested report, or an independently authorized recording workflow. Then remove only the exact temporary paths and stop only the processes, servers, tabs, or browser contexts created for this audit. Preserve user-owned browser state. Report every cleanup failure with the residual path or running resource.

**Complete when:** the report's coverage claims match the ledger, every Finding Packet is available to the user or the selected recording workflow, and every disposable path and running resource is removed or reported as residual state.
