# Agent Skill Workflows

This context defines the language used to design skills that keep agent work aligned with the problem the user asked the current conversation to solve.

## Language

**Yak Triage**:
The discipline of continuing work on the User Problem while preserving each distinct Discovered Problem instead of silently ignoring it or switching over to repair it. It does not judge necessary work within the User Problem, limit investigation depth, or display a separate problem anchor.
_Avoid_: Task switching, silent dismissal

**User Problem**:
The problem the user has authorized the current conversation to solve, together with the conditions that show it is resolved and the agreed boundaries. It changes when the user explicitly revises the request.
_Avoid_: User Goal, original prompt, immutable task

**Discovered Problem**:
Another observable problem encountered while working on the User Problem. Yak Triage handles it only when it is distinct from the problem currently being solved.
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
