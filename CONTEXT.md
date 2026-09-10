# Agent Skill Workflows

This context defines the language used to design skills that keep agent work aligned with the problem the user asked the current conversation to solve.

## Language

**Yak Shaving Triage**:
The continuous, silent discipline of checking newly discovered problems and contemplated task switches against the User Problem, preparing each distinct Discovered Problem for reconciliation and user-approved recording instead of silently ignoring it or switching over to repair it. It stays active from explicit invocation through the current User Problem without judging investigation depth, displaying a separate problem anchor, or managing another skill.
_Avoid_: Recurring scope report, task switching, silent dismissal

**User Problem**:
The problem the user has authorized the current conversation to solve, together with the conditions that show it is resolved and the agreed boundaries. It changes when the user explicitly revises the request.
_Avoid_: User Goal, original prompt, immutable task

**Discovered Problem**:
An observable problem encountered while working on the User Problem that falls outside the work required to resolve it and can be deferred without blocking that resolution. Yak Shaving Triage preserves it instead of switching over to repair it.
_Avoid_: Side quest, tangent, speculation

**Issue-ready Problem**:
A Discovered Problem preserved with enough verified context for an agent without the originating conversation to understand the problem, locate or reproduce the evidence, and verify a future resolution. It requires observable evidence and acceptance criteria, not a known root cause or chosen solution.
_Avoid_: Issue exploration, speculative issue

**Issue Reconciliation**:
The mandatory act of checking every Issue-ready Problem against the canonical tracker selected by Tracker Guidance before proposing any persistent tracker mutation. Reuse a complete existing record without mutation, prepare only materially useful missing evidence when an update is needed, and never propose a duplicate merely to preserve the current conversation's version.
_Avoid_: Duplicate issue, unconditional comment

**Problem Identity**:
The reconciliation boundary between one problem expressed through multiple observations and independently resolvable problems. Finding Packets share an identity when one resolution and acceptance boundary would resolve them together; different wording, entry points, or reproduction paths alone do not split them, while the ability to resolve one without the other does.
_Avoid_: Title match, shared-component bucket, suspected-root-cause merge

**Audit Reconciliation Gate**:
The boundary after a Usage-First Audit has reconciled its source-confirmed public surface or explicitly ended as a Partial Audit, and frozen its independently observed findings, at which co-active Yak Shaving Triage may begin tracker-informed Issue Reconciliation. Finding Packets may be handed off before this gate, but target tracker history remains closed until it is reached; once that history is read, the remaining current audit work and any later resume are tracker-informed.
_Avoid_: Per-slice issue lookup, early duplicate search, silent blind resume

**Reconciliation Disposition**:
The per-problem result of Issue Reconciliation: Reused, Proposed Update, Proposed New, or Reconciliation Blocked. A checkpoint presents dispositions together, identifies the canonical record for Reused results, and keeps approval separable for every proposed mutation.
_Avoid_: Blanket approval, per-finding interruption, implicit write

**Reconciliation Blocked**:
A Reconciliation Disposition used when the canonical tracker cannot be searched well enough to rule out an existing record. The Issue-ready draft remains available, but no creation or update may be proposed until reconciliation becomes possible.
_Avoid_: Duplicate-risk warning, silent search skip, discarded finding

**Evidence Capture**:
A bounded act of preserving evidence already encountered or cheaply reconfirmed, without diagnosing or solving the Discovered Problem.
_Avoid_: Root-cause analysis, issue investigation

**Tracker Guidance**:
Project-provided instructions that identify where and how Issue-ready Problems are recorded.
_Avoid_: Assumed tracker, default GitHub

**Tracker Write Approval**:
The user's confirmation of an exact proposed set of persistent tracker mutations after reconciliation and draft review. Activating a skill does not grant this approval; it applies whether Tracker Guidance selects an external tracker or an explicitly requested repository Markdown record.
_Avoid_: Skill invocation, implicit write authorization, blanket future approval

**Capture Checkpoint**:
A natural boundary between active steps where accumulated Issue-ready Problems can be reconciled, proposed tracker mutations can receive Tracker Write Approval, and approved records can be written without abandoning the current work. Reconciliation begins only when every active independence gate is open; otherwise the problems remain ready for a later checkpoint.
_Avoid_: Immediate context switch, end-only backlog

**Urgent Discovered Problem**:
A Discovered Problem with credible security, data-loss, or destructive risk that warrants immediate notice and sanitized draft preparation without silently expanding the current repair scope or bypassing Issue Reconciliation or Tracker Write Approval.
_Avoid_: Silent deferral, unauthorized repair

**Co-active Skill**:
A skill used alongside one or more other skills in the same conversation. Co-active skills remain independent; co-use does not mean one skill invokes, routes, orders, limits, monitors, or manages another. Each skill keeps its own responsibility, and genuine instruction conflicts require user direction.
_Avoid_: Caller skill, router skill

**Explicit-only Skill**:
A skill activated only by direct user selection when the client supports that invocation policy.
_Avoid_: Always-on skill, implicit skill

**Usage-First Audit**:
An evaluation of a source-accessible library or developer tool that exercises its user-facing behavior before inspecting implementation details, then uses the source to find public capabilities the experience may have missed.
_Avoid_: Source-first review, static bug scan, implementation audit

**Just Use It**:
The Explicit-only Skill that performs a Usage-First Audit, using a user-requested existing browser session first when the target exposes a UI. It produces coverage evidence and Finding Packets but does not repair findings or write tracker items.
_Avoid_: Source reviewer, bug fixer, issue publisher

**Capability Surface**:
The set of shipped public behaviors identified from user documentation, exposed UI, CLI, or API entry points, and source-confirmed public interfaces. Internal helpers, test-only interfaces, dead code, and unreleased feature flags are not part of the surface.
_Avoid_: Every code path, source inventory, feature count

**Capability Journey**:
An outcome-oriented path through a Capability Surface that reaches an observable user result through the relevant entry points, interactions, and states. Reaching or opening an entry point alone does not complete the journey.
_Avoid_: Entry click, control inventory, surface visit

**Capability Group**:
A set of Capability Journeys that serve the same user outcome. A panel, route, menu, or documentation section is not by itself a Capability Group boundary.
_Avoid_: UI container, navigation section, control collection

**Discriminating Variation**:
A one-variable change to a Capability Journey whose correct behavior produces an observably different result, state, or recovery path. Repeating a default or choosing an equivalent value is not discriminating.
_Avoid_: Random second input, ceremonial retry, exhaustive combination

**Vertical Capability Slice**:
A coherent feature-group audit unit built around a primary Capability Journey and one discriminating variation or recovery path. It reaches a terminal coverage state before the audit moves to another feature group.
_Avoid_: Shallow feature sweep, panel tour, exhaustive state matrix

**Slice-First Audit**:
A Usage-First Audit traversal that completes the documented journeys and free exploration for one Vertical Capability Slice before moving to the next, while keeping implementation source closed until the hands-on slices finish.
_Avoid_: Global entrance sweep, source-interleaved audit, phase-wide button tour

**Coverage Ledger**:
A compact, resumable account of each Vertical Capability Slice's coverage state and next action, preserving honest boundaries between completed, active, blocked, and unexercised work.
_Avoid_: Raw browser transcript, screenshot archive, implied coverage

**Verification Trace**:
Compact positive evidence for a verified Capability Journey: its initial conditions, material interactions, observable result, discriminating variation, and covered modes.
_Avoid_: Status-only claim, full interaction transcript, success screenshot archive

**Partial Audit**:
An audit report with one or more known capabilities still Not Exercised. It may claim completion for named Vertical Capability Slices but not for the full Capability Surface.
_Avoid_: Complete audit, representative completion, implied full coverage

**Surface Discovery Pass**:
A bounded inspection within the active Vertical Capability Slice that reveals reachable controls, nested surfaces, and off-screen behaviors without treating discovery as verification.
_Avoid_: Whole-product button tour, control verification, unbounded browsing

**Mode Parity Probe**:
A replay of a completed Capability Journey's outcome and key interaction states in a sibling mode, expanding only when a material difference appears. Switching modes without replaying the journey is not a parity probe.
_Avoid_: Mode toggle, full mode matrix, visual glance

**Reference Audit Scenario**:
A concrete product experience used to derive and validate a general Usage-First Audit contract without changing audit behavior for that product.
_Avoid_: Product-specific rule, anecdote, special-case adapter

**Reference Audit Suite**:
A bounded set of complementary Vertical Capability Slices and Mode Parity Probes drawn from one or more Reference Audit Scenarios to validate a general audit contract through real use. It never introduces target detection or scenario-specific branches into that contract.
_Avoid_: Exhaustive product audit, prose walkthrough, product-specific contract

**Generalization Gate**:
The admission boundary for promoting scenario-derived learning into a general skill contract: the rule must be expressible through shared outcomes, journeys, states, modes, or interaction boundaries without target-specific names, detection, or branches.
_Avoid_: Sample patch, product heuristic, second-project prerequisite

**Audit Finding**:
An observable functional failure, documentation mismatch, visual or interaction defect, operational problem, Capability Gap, unusable path, or product- or documentation-caused blocked capability confirmed while exercising a Capability Surface. It belongs to the Usage-First Audit even when repairing the underlying problem does not; an audit-environment limitation remains Blocked coverage without becoming a Finding.
_Avoid_: Speculation, source-only suspicion, fix task

**Capability Gap**:
An Audit Finding where actual use shows that shipped behaviors cannot be combined, scoped, or controlled finely enough to complete a concrete practical path. It records the reproducible limitation and impact without labeling it a bug unless a public promise or consistent product contract is contradicted.
_Avoid_: Feature wish, automatic bug label, solution design

**Finding Packet**:
The session-scoped evidence for an Audit Finding, including the affected capability, prerequisites, reproduction path, expected behavior, observed behavior, reproduction attempts, and available evidence. It supports handoff and final reporting without itself publishing or updating a tracker item.
_Avoid_: Tracker issue, diagnosis, implementation plan

**Intermittent Finding**:
An Audit Finding observed through actual use but not reproduced consistently under the recorded conditions. Its Finding Packet preserves the observed event, attempt results, relevant state, and uncertainty without claiming stable reproduction or a known cause.
_Avoid_: Stable reproduction, dismissed flake, confirmed cause

**Decision Load**:
The human effort and synchronous interruption required to resolve choices during an agent workflow. Reducing Decision Load does not imply reducing model reasoning time or eliminating the underlying decisions.
_Avoid_: Question count, reasoning latency

**Substantive Message**:
A user-visible question or answer that materially affects the user's understanding, judgment, authorization, or next action. Greetings and acknowledgements without a material status change are not Substantive Messages.
_Avoid_: Substantive Interaction, every message

**Context Sufficiency**:
The condition where a Substantive Message contains the relevant background, term meanings, evidence, examples, consequences, and action detail needed for the user to understand, judge, or act without first requesting clarification. Sufficiency is proportional to the current purpose, not exhaustive coverage of the topic.
_Avoid_: Context Completeness, exhaustive explanation, context dump

**Modifier Skill**:
An Explicit-only Skill that deliberately specializes named parts of the current task workflow without taking ownership of the User Problem or expanding the agent's authority. Its specialization governs ordinary process rules, while the task skill retains its work and mandatory safety, authorization, external-effect, and human checkpoints.
_Avoid_: Co-active Skill, wrapper skill

**Decision Boundary**:
The rule separating user-owned decisions that require synchronous input from delegated choices the agent may resolve. A conservative Decision Boundary delegates only evidence-backed, local, reversible implementation choices that do not change scope, acceptance criteria, user-visible behavior, domain rules, public contracts, persistent data, authorization, or external effects.
_Avoid_: Question limit, autonomy budget

**Decision Ledger**:
A compact checkpoint or completion summary of material delegated choices, with enough context for the user to veto them. Routine implementation details are omitted so the ledger does not recreate the Decision Load it removes.
_Avoid_: Assumption dump, question transcript

**Decision Pruning**:
The selective removal of candidate questions from synchronous interaction after they are found answerable, redundant, premature, or safely delegated across the Decision Boundary. It preserves user-owned decisions and mandatory checkpoints rather than deleting decisions to meet a question count.
_Avoid_: Question cutting, decision deletion

**Anchor Project**:
The project whose users, capabilities, necessary boundaries, and cross-project possibilities are being examined. It may be named by the user or inferred from the active workspace.
_Avoid_: User-supplied candidate list, project to expand at all costs

**Expansion Aim**:
The one-sentence user-owned statement of which existing value from the Anchor Project should become useful in more concrete contexts. It guides discovery without naming or presupposing a candidate project or solution.
_Avoid_: Search query, feature request, mandatory growth target

**Necessary Boundary**:
A framework, domain, platform, or experience constraint whose removal would change the value or identity the Anchor Project is meant to preserve. It may remain specific even when underlying capabilities become reusable.
_Avoid_: Limitation to remove, accidental coupling, obstacle to growth

**Incidental Constraint**:
A historical or technical restriction that narrows where an Anchor Project's existing value can apply without being necessary to that value. Removing it may enlarge the eligible contexts without redefining the project.
_Avoid_: Necessary Boundary, missing feature, arbitrary inconvenience

**Universal Core**:
A stable mechanism supported by evidence from more than one concrete project or usage context, while each project may retain its specific integrations and experience. A larger feature set or audience is not by itself a Universal Core.
_Avoid_: Bigger scope, feature union, generic abstraction

**Bounded Discovery**:
Agent-owned research that starts from an Anchor Project and Expansion Aim, investigates a finite set of real adjacent projects through declared technical, shared-problem, complementary-capability, and cross-ecosystem search paths, and stops under an explicit limit or evidence condition. The user may supply useful seeds but is not responsible for finding candidates.
_Avoid_: User-dependent search, open-ended browsing, exhaustive ecosystem search

**Candidate Evidence**:
Traceable evidence from both the Anchor Project and at least one real adjacent project that shows a shared or complementary problem and a plausible stable mechanism or integration seam. Conceptual similarity or technical connectability alone is insufficient.
_Avoid_: One-sided evidence, plausible idea, shared technology

**Expansion Candidate**:
An hypothesis supported by Candidate Evidence that an Anchor Project could serve another concrete context as a Universal Core, Adapter Opportunity, or Platform Opportunity. It is an exploration result, not authorization to change or combine projects.
_Avoid_: Scope expansion, feature idea, implementation authorization

**Evidence-adjusted Value**:
The comparative value of an Expansion Candidate after accounting for Candidate Evidence, preserved Necessary Boundaries, concrete additional contexts, maintenance burden, and reversibility. Reach or abstraction elegance alone does not establish it.
_Avoid_: Audience size, reuse score, technical elegance

**Adapter Opportunity**:
An Expansion Candidate where the Anchor Project keeps its specific core and a bounded integration seam makes that core useful to another concrete project or context. It does not claim that the integrated behavior is universal.
_Avoid_: Universal Core, merged project, duplicated implementation

**Platform Opportunity**:
An Expansion Candidate where a stable interface or protocol could let a family of specific projects participate while retaining their own integrations and experience.
_Avoid_: One-off adapter, feature bundle, ecosystem branding

**Recommended Candidate**:
An Expansion Candidate with sufficient Evidence-adjusted Value and a plausible maintenance model covering ownership, verification scope, compatibility commitments, and an exit path. Candidates may remain in the report without qualifying for recommendation.
_Avoid_: Interesting candidate, highest-reach idea, implementation commitment

**Candidate Card**:
A self-contained account of one Expansion Candidate covering its type, Candidate Evidence, shared or complementary problem, preserved Necessary Boundaries, proposed seam, maintenance model, material risks, and next experiment.
_Avoid_: Ranked idea, score row, project summary

**Candidate Disposition**:
The qualitative decision assigned to a Candidate Card: Recommended when it passes the recommendation gate, Needs Evidence when its Evidence Boundary names a resolvable gap, or Rejected when a material boundary or cost defeats it. It communicates judgment without a pseudo-precise numeric score.
_Avoid_: Candidate score, rank alone, confidence percentage

**Rejection Record**:
A compact explanation of a material rejected candidate and the evidence, Necessary Boundary, or maintenance cost that defeated it. Discovery Reports preserve only the most decision-relevant rejections rather than dumping the raw candidate pool.
_Avoid_: Rejected idea list, omitted candidate, exhaustive search log

**Experiment Ladder**:
A progressive plan that first verifies the second context and its problem, then tests one proposed seam against both concrete cases, and recommends a throwaway prototype only when the cheaper checks pass. Bounded Discovery designs this ladder without executing implementation.
_Avoid_: Automatic prototype, implementation plan, proof by demo

**Evidence Boundary**:
The explicit limit of a discovery result, stating which search paths were checked, which material evidence remains unavailable, and how that uncertainty limits recommendation. It supports a No-expansion Result or a non-recommended candidate without transferring search work to the user.
_Avoid_: Research disclaimer, speculative fill-in, user homework

**Exploration Checkpoint**:
The user decision after a discovery result to select a candidate, authorize targeted additional research, or accept a No-expansion Result. Implementation begins only after the User Problem is explicitly revised to include it.
_Avoid_: Automatic handoff, highest-score selection, implementation approval

**Discovery Report**:
The conversational deliverable of Bounded Discovery containing Candidate Cards, recommendations, the Evidence Boundary, and Experiment Ladders. It becomes a repository artifact only when the user explicitly asks to save it.
_Avoid_: Automatic report file, implementation specification, ecosystem catalog

**No-expansion Result**:
A valid terminal result of Bounded Discovery when no Expansion Candidate has sufficient shared-problem evidence, a stable seam, and acceptable maintenance cost.
_Avoid_: Failed search, lack of imagination, mandatory opportunity

**Set Theory for Projects**:
The explicit, read-only discovery skill inspired by Antfu's "The Set Theory" that applies Bounded Discovery to an Anchor Project, distinguishes its Necessary Boundaries from Incidental Constraints, and proposes evidence-backed Universal Core, Adapter, or Platform opportunities. Its name preserves the source concept while identifying the project-discovery context; it is not an official Antfu publication and does not require expansion.
_Avoid_: Mathematical set theory, Antfu-authored skill, project combination mandate

**Tool Decision**:
A repository-context choice among keeping the current approach, proceeding without an external tool, or adopting an external tool to address a concrete need.
_Avoid_: Tool replacement, mandatory adoption, popularity contest

**Current Baseline**:
The present way a repository handles the need behind a Tool Decision, whether through an existing tool, local implementation, manual work, or deliberate absence of a tool.
_Avoid_: Default candidate, legacy failure, do-nothing option

**No-change Result**:
A valid Tool Decision outcome in which the Current Baseline has stronger contextual fit than the available alternatives, or no alternative has enough evidence to justify change.
_Avoid_: Failed search, fallback recommendation, missing winner

**Progressive Adoption Path**:
A staged, reversible route for trying or adopting a tool through bounded use, coexistence, migration checkpoints, and an explicit exit path.
_Avoid_: Big-bang migration, automatic implementation, irreversible rollout

**Tool Decision Report**:
The decision artifact for a Tool Decision, containing the Current Baseline, candidate evidence and dispositions, material uncertainty, and any Progressive Adoption Path.
_Avoid_: Implementation authorization, feature comparison table, unconditional recommendation

**Tool Fit**:
The contextual value of a tool for a specific Tool Decision after its benefits, total use and change costs, hard compatibility constraints, and Progressive Adoption Path are considered against the Current Baseline.
_Avoid_: Best tool, popularity, feature count, universal score

**Candidate Seed**:
A user-provided or repository-discovered tool that starts candidate discovery without limiting the search or receiving guaranteed finalist status.
_Avoid_: Finalist, exhaustive shortlist, required recommendation

**Candidate Gate**:
A non-negotiable compatibility condition that a tool must satisfy before qualitative Tool Fit comparison, such as an applicable runtime, license, security, compliance, or data boundary.
_Avoid_: Weighted criterion, preference, score penalty

**Evidence Saturation**:
The bounded-search condition where additional independent search paths no longer produce a materially different qualified candidate for the Tool Decision.
_Avoid_: Exhaustive search, fixed top three, arbitrary timeout

**Material Tool Opportunity**:
An evidence-backed Tool Decision discovered during repository-wide audit, grounded in an observable problem, risk, duplicated capability, or maintenance burden rather than the mere existence of an alternative tool.
_Avoid_: Dependency suggestion, modernization idea, available replacement

**Tool Fit for Projects**:
The explicit-only, read-only skill that resolves concrete Tool Decisions or audits a repository for Material Tool Opportunities, applies category-relevant Candidate Gates, searches to Evidence Saturation, and returns a Tool Decision Report without implementing its recommendations.
_Avoid_: Dependency updater, best-tools list, automatic migration

**Tool Category Profile**:
A category-specific set of Candidate Gates and comparison concerns used within the shared Tool Decision workflow for code and developer tools, data and infrastructure, cloud and deployment platforms, or hosted and commercial services.
_Avoid_: Universal checklist, product catalog, improvised criteria

**Tool Candidate Card**:
A self-contained account of one finalist covering repository evidence, passed and unresolved Candidate Gates, expected benefit, total adoption cost, material risk, and any Progressive Adoption Path.
_Avoid_: Feature table, score row, marketing summary

**Tool Choice Checkpoint**:
The user decision after a Tool Decision Report to select a candidate, keep the Current Baseline, authorize targeted evidence gathering, or end the decision without a change.
_Avoid_: Automatic selection, implementation approval, recommendation acceptance by silence

**Tool Decision Context**:
The concrete repository work, affected users, desired outcome, constraints, and success conditions that make Tool Fit meaningful for a Tool Decision.
_Avoid_: Product comparison, tool category, generic best practice

**Decision Depth**:
The evidence and analysis intensity proportional to a Tool Decision's change radius, reversibility, and external risk: Quick for local reversible choices, Standard for workflow or multi-module choices, and High-stakes for architectural, data, platform, identity, or critical-service choices.
_Avoid_: Fixed report length, tool popularity tier, arbitrary effort level

**Tool Candidate Disposition**:
The qualitative judgment assigned to a tool candidate: Recommended, Viable Alternative, Trial, Needs Evidence, or Rejected. Trial requires a bounded repository experiment; Needs Evidence requires a missing fact or user-owned constraint.
_Avoid_: Numeric rank, pass/fail score, recommendation confidence

**Read-only Validation**:
Evidence gathering that may inspect repository state and run existing checks or benchmarks without installing a candidate, changing source or configuration, or creating a prototype implementation.
_Avoid_: Trial execution, dependency installation, migration rehearsal

**Library Quickstart**:
A bounded learning experience that reduces the learner's time spent finding a path into a library, framework, or developer tool, building on existing language foundations and explaining the concepts and behavior needed for the learner's intended use in depth. Its scope serves that immediate purpose, with documentation-grounded explanations and Guided Demonstrations, rather than expanding into an ongoing curriculum as detail increases.
_Avoid_: Usage-First Audit, exhaustive library course, task-only walkthrough, programming language course, long-term study plan

**Source Preparation**:
The default, bounded study of a target's relevant repository structure, public entrypoints, examples, tests, and implementation after its official documentation, grounding the guide's explanations in source matching the demonstrated version. The learner's intended use determines how much implementation enters the guide: ordinary onboarding explains key mechanisms, while contribution preparation also follows a relevant source path through a minimal change and regression testing, without treating internal interfaces as supported public contracts.
_Avoid_: Whole-repository audit, optional-only source lookup, source-code curriculum

**Guided Demonstration**:
A documentation-grounded example demonstrated by the agent and explained in a Quickstart Guide through the relevant code, choices, behavior, and result. Delivery does not require learner code changes, predictions, exercises, or assessments.
_Avoid_: Guided Experiment, learner exercise, assessment gate

**Quickstart Guide**:
The single primary document delivered as a complete Library Quickstart, explaining the target's core capabilities and their relationships through a representative scenario, with the context, reasoning, code explanations, and supporting variations needed to follow the intended learning path without the originating conversation. Runnable examples accompany the guide, advanced topics have explicit boundaries, and later conversation clarifies or extends the delivered material.
_Avoid_: Execution report, link collection, incremental lesson series

**Quickstart Workspace**:
An independent directory retaining one Quickstart Guide and its accompanying runnable examples. Retaining it does not imply a recurring course or require repeated skill invocation.
_Avoid_: Disposable audit workspace, long-term learning record, production integration

**Teaching Language**:
The learner-selected language for conversational explanations and saved teaching material in a Library Quickstart, with code identifiers and API names retaining their conventional form. An explicit choice in the current request establishes it; otherwise it remains a learner decision before teaching begins.
_Avoid_: Hard-coded tutorial language, inferred language preference, translated API identifiers

**Get Up to Speed**:
The explicit-only skill that delivers a Library Quickstart as one complete Quickstart Guide with accompanying runnable examples in a retained Quickstart Workspace, grounded in official documentation and Source Preparation.
_Avoid_: Usage-First Audit, exercise-driven course, recurring curriculum

**Repository Tool Audit**:
The first stage of Tool Fit for Projects that scans the current repository for Material Tool Opportunities and returns at most five prioritized opportunities for the user to choose from before any full Tool Decision begins.
_Avoid_: Dependency-by-dependency review, batch tool selection, automatic deep dive

**Tool Evidence Hierarchy**:
The ordered evidence basis for Tool Fit: repository facts and existing validation first, authoritative project or vendor sources second, and reproducible independent evidence for material claims those sources cannot establish.
_Avoid_: Popularity ranking, uncited consensus, vendor claims alone

**Frame Expansion**:
The deliberate introduction of project-relevant perspectives the user has not raised, with enough explanation to make informed judgments and trace the implications of their answers. It considers risks, opportunities, and simplification together; newly surfaced directions are explained before the user chooses whether to deepen, defer, or end exploration.
_Avoid_: Question volume, risk-only checklist, automatic scope expansion

**Expand the Frame**:
The standalone Explicit-only Skill that uses Frame Expansion for an existing project or an unrealized idea, improving both project decisions and the user's ability to recognize relevant questions, including questions about the project's goals. Its discussion outcome connects newly introduced perspectives to the decisions they changed or supported and preserves unresolved directions, without treating the agent's broader knowledge as authority over user-owned trade-offs or permission to implement decisions.
_Avoid_: Knowledge quiz, generic brainstorming, decision outsourcing

**Skill Evolution**:
The iterative improvement of a skill through opportunities discovered in how it was used in conversation, assessed against that skill's stated purpose as introduced by its description and clarified by its instructions. It includes successful approaches worth carrying forward and changes that could improve future use, with a detailed history kept separately for each skill.
_Avoid_: Execution compliance audit, failure-only review, change for its own sake

**Skill Evolution Opportunity**:
An evidence-grounded possibility for improving future use of a skill in relation to its particular purpose, discovered in an actual usage conversation. It may concern the method, sequence of work, instruction structure, references, templates, or validation scenarios, including effective approaches worth carrying forward.
_Avoid_: Compliance violation, mandatory new rule, confirmed improvement

**Skill Evolution Hypothesis**:
A concrete proposed change that connects a Skill Evolution Opportunity to an expected benefit and a way to compare behavior before and after the change. A single clear observation can support a hypothesis; evidence from validation determines whether the expected benefit is supported.
_Avoid_: Proven improvement, repeated-failure prerequisite, untested success claim

**Skill Evolution Record**:
A detailed, skill-specific history that lets a later reader understand what changed, why it changed, and what evidence supports it, with enough information to reverse the recorded changes. It preserves the distinction between proposed changes, applied changes, and observed validation results.
_Avoid_: Summary-only changelog, conversation dump, implied rollback support

**Evolve Skills**:
The Explicit-only Skill that performs Skill Evolution from prior skill use, taking user-selected hypotheses through modification, validation, and a Skill Evolution Record. It can operate independently, while co-active grilling skills deepen discussion of the hypotheses and trade-offs.
_Avoid_: Compliance checker, generic skill generator, mandatory grilling dependency
