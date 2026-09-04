---
name: just-use-it
description: Experience a source-accessible library or developer tool hands-on before reading its implementation, cover its shipped public capabilities, and report observable problems or capability gaps without repairing or publishing them.
disable-model-invocation: true
---

# Just Use It

Use first. Read source last.

Run a **Usage-First Audit** of one source-accessible library, framework, CLI, or developer tool. Exercise its **Capability Surface** through the interfaces a user receives, then inspect the source only to find public capabilities the hands-on passes missed.

The audit owns experience, coverage evidence, and session-scoped Finding Packets. It does not diagnose or repair findings, create or update tracker entries, or claim source inspection as usage. A user may separately invoke a recording workflow such as `$yak-shaving-triage`; co-use keeps both skills independent.

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

## 2. Follow the Documentation

Build an initial Capability Surface from the public documentation without reading behavioral implementation source. Give every documented capability the initial state `Not Exercised`.

Follow each documented path exactly as a user would:

- When the target exposes an interactive UI, read [references/ui-experience.md](references/ui-experience.md) before controlling it. Use browser control for every browser-reachable UI; use another real user-control surface for native or terminal UI when the environment provides one, otherwise mark that UI coverage Blocked.
- When the target has no UI, or its UI covers only part of the surface, read [references/programmatic-experience.md](references/programmatic-experience.md) before creating a consumer workspace.
- As soon as behavior may be an Audit Finding, read [references/finding-packets.md](references/finding-packets.md) before expanding the investigation.

Record the observed state of every capability as `Verified`, `Finding`, `Blocked`, or `Not Exercised`. A documentation error is a Finding even when the implementation works through an undocumented correction. Do not use source knowledge to silently rescue the documented journey.

During an active audit, `Not Exercised` is pending; `Verified`, `Finding`, and `Blocked` are terminal. `Not Exercised` may remain only in a partial report after interruption.

**Complete when:** every documented capability and journey has been exercised through its public interface or has an explicit Blocked reason.

## 3. Explore Freely

Keep implementation source and the target issue tracker closed. Read [references/exploration-lenses.md](references/exploration-lenses.md), then build a small, capability-shaped exploration matrix from the visible product, public help, and feedback it provides. Exercise the main path plus each materially applicable lens without multiplying unrelated dimensions into an exhaustive Cartesian product.

Add newly discoverable public capabilities to the Capability Surface. Continue until additional user actions repeat already observed states and behavior rather than revealing a new capability, transition, or interaction.

**Complete when:** every capability discoverable without source has a terminal state, every materially applicable exploration lens has an exercised path or explicit exclusion, and further hands-on exploration is behaviorally redundant.

## 4. Reconcile with Source

Open the implementation source only now. Inspect public exports, routes, commands, flags, feature registration, examples, and tests to find shipped public capabilities missing from the current surface. Treat a capability reachable through a shipped package export, executable, route, or browser global as public unless the project marks it internal, test-only, or unreleased. A hidden help entry is a discoverability signal, not by itself proof that the capability is private. Report unresolved public intent explicitly.

Map every source-confirmed public entrypoint to an existing capability, an explicit exclusion, or a newly added capability. Exercise every newly added capability through the interface available to a user. Treat source evidence as a lead: observable use confirms a Finding; source-only suspicion remains an unverified lead in the report.

After the source surface is accounted for, the target project's public issue history may be sampled as a final coverage calibration. Re-exercise relevant paths through the public interface. Label behavior first encountered there as a known-issue reproduction rather than independent discovery, and keep issue reading separate from tracker mutation or publication.

**Complete when:** every source-confirmed public entrypoint is accounted for and every included capability has a terminal state.

## 5. Report and Clean Up

For a large surface, work in coherent feature groups without asking the user to approve each group. If the audit is interrupted, report the completed groups and leave all remaining capabilities as `Not Exercised`; never describe partial coverage as complete.

Return a conversational audit report containing:

- the target and environment;
- the Capability Surface with each terminal state;
- functional, documentation, visual, interaction, operational, Capability Gap, and Intermittent Findings with their evidence;
- Blocked and, for a partial run, Not Exercised capabilities;
- tracker links only when a separately active recording workflow published them; and
- cleanup results.

Keep the report conversational unless the user explicitly requests a repository artifact. When asked to save it, use the exact requested destination and repository conventions. Persistent finding publication remains outside this skill.

Before deleting disposable state, move required evidence into the conversation, the requested report, or an independently authorized recording workflow. Then remove only the exact temporary paths and stop only the processes, servers, tabs, or browser contexts created for this audit. Preserve user-owned browser state. Report every cleanup failure with the residual path or running resource.

**Complete when:** the report's coverage claims match the ledger, every Finding Packet is available to the user or the selected recording workflow, and every disposable path and running resource is removed or reported as residual state.
