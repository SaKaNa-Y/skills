# Yak Triage

An explicit, composable agent skill for finishing the problem in front of you without losing valid problems discovered along the way.

## Why It Exists

Agents often discover another unfinished problem while working, switch over to solve it, discover yet another problem, and keep going until the original work is lost.

Yak Triage keeps one problem in progress. It preserves other confirmed problems as self-contained tracker issues or drafts, then returns to the current work. A problem is still recorded when it already existed or was not caused by the current change.

## Installation

Install `yak-triage` into the current project with the [skills CLI](https://skills.sh):

```bash
npx skills@latest add SaKaNa-Y/skills --skill yak-triage
```

Install it specifically for Codex:

```bash
npx skills@latest add SaKaNa-Y/skills --skill yak-triage --agent codex
```

Add `--global` to make it available across projects:

```bash
npx skills@latest add SaKaNa-Y/skills --skill yak-triage --agent codex --global
```

## Usage

Invoke the skill explicitly, either alone or alongside other skills:

```text
$yak-triage Fix the checkout failure without losing other confirmed problems.
```

```text
$yak-triage $grilling Stress-test this design and preserve unrelated findings.
```

Yak Triage does not invoke, manage, or limit other skills. Each active skill keeps its own responsibility.

## How It Works

- Normal task and workflow skills continue solving the user's current problem.
- When another observable problem appears, Yak Triage captures enough context for a future agent to understand and verify it.
- It follows the project's tracker guidance, checks for duplicates, and creates, updates, or reuses an issue at a natural checkpoint.
- Without tracker guidance, it keeps an issue-ready draft and asks once where to record it after the current work.
- Urgent security, data-loss, and destructive risks are reported and preserved immediately without silently expanding the current repair.

For the complete behavior, see [`skills/yak-triage/SKILL.md`](skills/yak-triage/SKILL.md).
