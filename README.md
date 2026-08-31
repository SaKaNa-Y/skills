# Agent Skills

Explicit agent skills for keeping long-running AI work focused while preserving user control. `prune-the-tree` reduces decision load without taking user-owned decisions away; `yak-triage` preserves valid problems discovered along the way without derailing the current task.

## Skills

| Skill | Use it when | What it does |
|---|---|---|
| [`prune-the-tree`](skills/prune-the-tree/SKILL.md) | A workflow generates too many low-value questions | Resolves factual, redundant, premature, or safely delegated choices while preserving user-owned decisions |
| [`yak-triage`](skills/yak-triage/SKILL.md) | Work reveals other valid problems | Preserves them as reconciled issues or issue-ready drafts, then returns to the current problem |

## Installation

Install either skill into the current project with the [skills CLI](https://skills.sh):

```bash
npx skills@latest add SaKaNa-Y/skills --skill prune-the-tree
npx skills@latest add SaKaNa-Y/skills --skill yak-triage
```

Append `--agent codex` to install specifically for Codex, and append `--global` when the skill should be available across projects:

```bash
npx skills@latest add SaKaNa-Y/skills --skill prune-the-tree --agent codex --global
```

## Usage

Invoke both skills explicitly.

Use Prune the Tree alone or with a question-heavy workflow:

```text
$prune-the-tree Build this feature and ask only for decisions that affect what I receive.
```

```text
$prune-the-tree $grill-with-docs Stress-test this product idea without offloading routine choices to me.
```

Use Yak Triage alone or alongside another skill:

```text
$yak-triage Fix the checkout failure without losing other confirmed problems.
```

```text
$yak-triage $grilling Stress-test this design and preserve unrelated findings.
```

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

## Yak Triage

Agents often discover another unfinished problem while working, switch over to solve it, discover yet another problem, and keep going until the original work is lost.

Yak Triage keeps one problem in progress. It preserves other confirmed problems as self-contained tracker issues or drafts, then returns to the current work. A problem is still recorded when it already existed or was not caused by the current change.

### How It Works

- Normal task and workflow skills continue solving the user's current problem.
- When another observable problem appears, Yak Triage captures enough context for a future agent to understand and verify it.
- It follows the project's tracker guidance, checks for duplicates, and creates, updates, or reuses an issue at a natural checkpoint.
- Without tracker guidance, it keeps an issue-ready draft and asks once where to record it after the current work.
- Urgent security, data-loss, and destructive risks are reported and preserved immediately without silently expanding the current repair.

For the complete behavior, see [`skills/yak-triage/SKILL.md`](skills/yak-triage/SKILL.md).

## Combining Skills

The active task workflow still owns the User Problem.

- Prune the Tree is a Modifier Skill: it specializes ordinary question routing while preserving mandatory safety, authorization, external-effect, and human checkpoints.
- Yak Triage is a Co-active Skill: it independently preserves distinct discovered problems without invoking, managing, or limiting the active workflow.

The shared vocabulary and composition rules live in [`CONTEXT.md`](CONTEXT.md). The Modifier Skill decision is recorded in [`docs/adr/0001-explicit-modifier-skills.md`](docs/adr/0001-explicit-modifier-skills.md).
