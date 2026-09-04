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
The act of checking whether an Issue-ready Problem is already tracked before proposing a new record. Reuse a complete existing record without mutation; prepare only materially useful missing evidence when an update is needed, and never propose a duplicate merely to preserve the current conversation's version.
_Avoid_: Duplicate issue, unconditional comment

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
A natural boundary between active steps where accumulated Issue-ready Problems can be reconciled, proposed tracker mutations can receive Tracker Write Approval, and approved records can be written without abandoning the current work. At the checkpoint, tell the user what was written, reused, or retained as a draft, then resume the current work.
_Avoid_: Immediate context switch, end-only backlog

**Urgent Discovered Problem**:
A Discovered Problem with credible security, data-loss, or destructive risk that warrants immediate notice and sanitized draft preparation without silently expanding the current repair scope or bypassing Tracker Write Approval.
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

**Repository Tool Audit**:
The first stage of Tool Fit for Projects that scans the current repository for Material Tool Opportunities and returns at most five prioritized opportunities for the user to choose from before any full Tool Decision begins.
_Avoid_: Dependency-by-dependency review, batch tool selection, automatic deep dive

**Tool Evidence Hierarchy**:
The ordered evidence basis for Tool Fit: repository facts and existing validation first, authoritative project or vendor sources second, and reproducible independent evidence for material claims those sources cannot establish.
_Avoid_: Popularity ranking, uncited consensus, vendor claims alone
