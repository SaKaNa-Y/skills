# Agent Skills

Explicit agent skills for keeping long-running AI work focused, understandable, and under user control. `make-it-land` gives substantive messages enough context to be understood and acted on; `prune-the-tree` reduces decision load without taking user-owned decisions away; `yak-shaving-triage` continuously guards the current problem while preserving valid problems discovered along the way.

## Skills

| Skill | Use it when | What it does |
|---|---|---|
| [`make-it-land`](skills/make-it-land/SKILL.md) | Questions or answers arrive without enough context | Explains the relevant background, terms, examples, evidence, implications, and next action |
| [`prune-the-tree`](skills/prune-the-tree/SKILL.md) | A workflow generates too many low-value questions | Resolves factual, redundant, premature, or safely delegated choices while preserving user-owned decisions |
| [`yak-shaving-triage`](skills/yak-shaving-triage/SKILL.md) | Work risks branching into other valid problems | Checks potential task switches, preserves distinct problems, and returns to the current problem |

## Installation

Install a skill into the current project with the [skills CLI](https://skills.sh):

```bash
npx skills@latest add SaKaNa-Y/skills --skill make-it-land
npx skills@latest add SaKaNa-Y/skills --skill prune-the-tree
npx skills@latest add SaKaNa-Y/skills --skill yak-shaving-triage
```

Append `--agent codex` to install specifically for Codex, and append `--global` when the skill should be available across projects:

```bash
npx skills@latest add SaKaNa-Y/skills --skill prune-the-tree --agent codex --global
```

## Usage

Invoke these skills explicitly.

Use Make It Land after an unclear message or alongside a task whose questions and answers need more context:

```text
$make-it-land Re-pitch your last answer so I can understand its terms, evidence, implications, and next step.
```

```text
$make-it-land Explain this architecture choice and recommend what fits the current project.
```

Use Prune the Tree alone or with a question-heavy workflow:

```text
$prune-the-tree Build this feature and ask only for decisions that affect what I receive.
```

```text
$prune-the-tree $grill-with-docs Stress-test this product idea without offloading routine choices to me.
```

Use Yak Shaving Triage alone or alongside another skill:

```text
$yak-shaving-triage Fix the checkout failure without losing other confirmed problems.
```

```text
$yak-shaving-triage $grilling Stress-test this design and preserve unrelated findings.
```

## Make It Land

Make It Land creates **Context Sufficiency**: each Substantive Message carries the relevant information the user needs to understand, judge, or act without first requesting clarification. It can re-pitch the last unclear message or remain active for the current problem.

For questions, it supplies the current situation, explains why user input is needed, defines terms, makes viable options concrete, states their implications, and gives a recommendation. For answers, it leads with the result, adds checkable evidence and relevant context, explains implications and uncertainty, and closes with the next action.

The information contract is fixed, but its presentation is proportional. Simple messages stay short; abstract concepts, important claims, and risky actions receive the examples, evidence, safeguards, and verification their stakes require. Deliverables keep their requested style unless the user explicitly asks to apply the skill inside them.

For the complete behavior, see [`skills/make-it-land/SKILL.md`](skills/make-it-land/SKILL.md).

## Prune the Tree

Prune the Tree reduces **Decision Load**: the human effort and synchronous interruption required to resolve choices. It does not promise lower model reasoning time, fewer underlying decisions, or a fixed question count.

Before the agent asks a question, the skill routes it in one of five ways:

| Route | Treatment |
|---|---|
| `FIND` | Resolve a fact or an authoritative prior decision from available evidence |
| `DROP` | Remove a duplicate, already-settled, or irrelevant candidate |
| `DEFAULT` | Take an evidence-backed, local, reversible implementation choice |
| `DEFER` | Revisit a real decision when its named prerequisite is resolved |
| `ASK` | Put a user-owned or mandatory decision to the user with a recommendation |

Only `FIND`, `DROP`, and `DEFAULT` permanently reduce synchronous questions. `DEFER` changes when a question is asked; `ASK` preserves it.

The user retains decisions about goals, non-goals, the concrete failure being solved, acceptance criteria, hard constraints, user-visible alternatives, values and taste, domain rules and terminology, public contracts, persistent data, authorization, external or destructive effects, security, and costly or irreversible commitments.

Material defaults appear in a compact **Decision Ledger** at a natural checkpoint or by completion, so the user can veto them without reviewing every routine implementation detail.

For the complete behavior, see [`skills/prune-the-tree/SKILL.md`](skills/prune-the-tree/SKILL.md).

## Yak Shaving Triage

Agents often discover another unfinished problem while working, switch over to solve it, discover yet another problem, and keep going until the original work is lost.

Yak Shaving Triage stays active from explicit invocation through the current User Problem. It silently checks newly discovered problems and contemplated task switches before they become detours. Work needed to resolve the User Problem remains with the active task workflow; distinct confirmed problems are preserved as self-contained tracker issues or drafts, then work returns to the User Problem. A problem is still recorded when it already existed or was not caused by the current change.

### How It Works

- Normal task and workflow skills continue deciding how to solve the user's current problem and how deeply to investigate it.
- When a new problem appears or the next action would change the line of work, Yak Shaving Triage silently checks the potential branch against the User Problem.
- A check that remains within the User Problem produces no user-visible update.
- A distinct observable problem is preserved without following the branch to diagnose or repair it.
- It follows the project's tracker guidance, checks for duplicates, and creates, updates, or reuses an issue at a natural checkpoint.
- Without tracker guidance, it keeps an issue-ready draft and asks once where to record it after the current work.
- Urgent security, data-loss, and destructive risks are reported and preserved immediately without silently expanding the current repair.

For the complete behavior, see [`skills/yak-shaving-triage/SKILL.md`](skills/yak-shaving-triage/SKILL.md).

## Combining Skills

The active task workflow still owns the User Problem.

- Prune the Tree is a Modifier Skill: it specializes ordinary question routing while preserving mandatory safety, authorization, external-effect, and human checkpoints.
- Make It Land is a Modifier Skill: it makes the remaining questions and all substantive answers understandable without changing who owns a decision.
- Yak Shaving Triage is a Co-active Skill: it continuously checks potential detours and preserves distinct discovered problems without invoking, managing, or limiting the workflow used to solve the User Problem.

The shared vocabulary and composition rules live in [`CONTEXT.md`](CONTEXT.md). The Modifier Skill decision is recorded in [`docs/adr/0001-explicit-modifier-skills.md`](docs/adr/0001-explicit-modifier-skills.md).
