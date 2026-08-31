# Agent Skill Workflows

This context defines the language used to design skills that keep agent work aligned with the problem the user asked the current conversation to solve.

## Language

**Yak Shaving Triage**:
The continuous, silent discipline of checking newly discovered problems and contemplated task switches against the User Problem, preserving each distinct Discovered Problem instead of silently ignoring it or switching over to repair it. It stays active from explicit invocation through the current User Problem without judging investigation depth, displaying a separate problem anchor, or managing another skill.
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
The act of checking whether an Issue-ready Problem is already tracked before creating a new issue. Reuse the existing issue and add only materially useful missing evidence; never create a duplicate merely to preserve the current conversation's version.
_Avoid_: Duplicate issue, unconditional comment

**Evidence Capture**:
A bounded act of preserving evidence already encountered or cheaply reconfirmed, without diagnosing or solving the Discovered Problem.
_Avoid_: Root-cause analysis, issue investigation

**Tracker Guidance**:
Project-provided instructions that identify where and how Issue-ready Problems are recorded.
_Avoid_: Assumed tracker, default GitHub

**Capture Checkpoint**:
A natural boundary between active steps where accumulated Issue-ready Problems can be reconciled and recorded without abandoning the current work. At the checkpoint, tell the user what was created, updated, or reused, then resume the current work.
_Avoid_: Immediate context switch, end-only backlog

**Urgent Discovered Problem**:
A Discovered Problem with credible security, data-loss, or destructive risk that warrants immediate notice and recording without silently expanding the current repair scope.
_Avoid_: Silent deferral, unauthorized repair

**Co-active Skill**:
A skill used alongside one or more other skills in the same conversation. Co-active skills remain independent; co-use does not mean one skill invokes, routes, orders, limits, monitors, or manages another. Each skill keeps its own responsibility, and genuine instruction conflicts require user direction.
_Avoid_: Caller skill, router skill

**Explicit-only Skill**:
A skill activated only by direct user selection when the client supports that invocation policy.
_Avoid_: Always-on skill, implicit skill

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
