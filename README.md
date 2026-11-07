# Skills for Deliberate Engineering

Agent skills by sakana for investigating problems, exploring ideas, and delivering agreed engineering changes.

## Installation

You need Node.js with `npx` and an agent supported by the [skills CLI](https://skills.sh).
Run this command from the project where you want to use the skills:

```bash
npx skills@latest add SaKaNa-Y/skills
```

The installer lets you select skills and agents. Installation is project-scoped by default.
Add `--global` to the command for agents that support a user-level skills directory.

Some skills also need shared methods from this collection. Select these dependencies during installation:

| Selected skill | Also install |
| --- | --- |
| `assess-findings`, `expand-the-frame`, `challenge-the-claim`, `review-change` | `investigate-with-evidence` |
| `just-use-it`, `yak-shaving-triage`, `explore-new-capabilities`, `implement-change` | `assess-findings`, `investigate-with-evidence` |
| `setup-sakana-skills`, when configuring working records | `assess-findings`, `investigate-with-evidence` |

Install `review-change` alongside implementation skills to use the shared review method. Without it, Implement Change keeps its proportionate inline review.

The workflows do not install dependencies at runtime.
See the [installation guide](docs/guide.md#quick-start) for individual selection and configuration details.

## Skills

### Communication and task control

| Skill | Purpose |
| --- | --- |
| [make-it-land](skills/make-it-land/SKILL.md) | Make important questions and answers understandable and actionable. |
| [prune-the-tree](skills/prune-the-tree/SKILL.md) | Reduce routine questions while preserving decisions that belong to you. |
| [yak-shaving-triage](skills/yak-shaving-triage/SKILL.md) | Preserve separate findings while keeping the current task on track. |

### Investigation and assessment

| Skill | Purpose |
| --- | --- |
| [investigate-with-evidence](skills/investigate-with-evidence/SKILL.md) | Resolve a specific factual question through sources or controlled execution. |
| [just-use-it](skills/just-use-it/SKILL.md) | Evaluate a developer tool through its user workflows and record evidence. |
| [assess-findings](skills/assess-findings/SKILL.md) | Assess findings and opportunities, then recommend scoped next actions. |
| [challenge-the-claim](skills/challenge-the-claim/SKILL.md) | Test a specific claim against relevant counterevidence. |
| [tool-fit-for-projects](skills/tool-fit-for-projects/SKILL.md) | Evaluate whether a tool fits a repository need. |

### Exploration and learning

| Skill | Purpose |
| --- | --- |
| [explore-new-capabilities](skills/explore-new-capabilities/SKILL.md) | Discover and discuss one grounded capability opportunity at a time. |
| [set-theory-for-projects](skills/set-theory-for-projects/SKILL.md) | Find other contexts where an existing project can provide value. |
| [expand-the-frame](skills/expand-the-frame/SKILL.md) | Explore project perspectives and questions you have not considered. |
| [get-up-to-speed](skills/get-up-to-speed/SKILL.md) | Deliver a complete guide and runnable examples for a developer tool. |

### Implementation and delivery

| Skill | Purpose |
| --- | --- |
| [issue-writing](skills/issue-writing/SKILL.md) | Clarify an idea and prepare an issue draft for you to submit. |
| [review-change](skills/review-change/SKILL.md) | Review a specified change against project standards and intended requirements. |
| [implement-change](skills/implement-change/SKILL.md) | Implement and verify an agreed change, with a Draft PR as the default delivery. |

### Configuration, records, and skill maintenance

| Skill | Purpose |
| --- | --- |
| [setup-sakana-skills](skills/setup-sakana-skills/SKILL.md) | Configure shared defaults, working records, and project conventions. |
| [browse-records](skills/browse-records/SKILL.md) | Browse recorded problems, decisions, and progress without editing them. |
| [evolve-skills](skills/evolve-skills/SKILL.md) | Improve skills through selected changes, evidence, and recoverable history. |

## Examples

The commands below select each task's required skills from this collection.
Use your agent's explicit skill invocation syntax. These examples use `$skill-name`.
Invocation does not expand the task's authority. See the [invocation guide](docs/guide.md#invoke-skills) for selection rules.

### Investigate a specific question

```bash
npx skills@latest add SaKaNa-Y/skills --skill investigate-with-evidence
```

```text
$investigate-with-evidence Determine whether this cache survives repeated activations. Use matching source or a controlled local test, and explain any evidence limits.
```

### Evaluate a developer tool

```bash
npx skills@latest add SaKaNa-Y/skills --skill just-use-it assess-findings investigate-with-evidence
```

```text
$just-use-it Exercise this project's primary user workflows and report observable findings with their evidence. Reuse my records configuration, or ask for a records directory if none is configured. Do not repair the product or publish issues.
```

The [audit guide](docs/guide.md#just-use-it) explains coverage, saved records, and continuation.

### Implement an agreed change

```bash
npx skills@latest add SaKaNa-Y/skills --skill implement-change assess-findings investigate-with-evidence
```

```text
$implement-change Implement the agreed change described below and verify its acceptance conditions. Keep delivery local: do not commit, push or create a PR. [Add the agreed outcome, scope and acceptance conditions, or a reference to them.]
```

This example requests local delivery. The [implementation guide](docs/guide.md#implement-selected-work-through-a-draft-pr) explains the default Draft PR workflow.

## Guides and maintenance

- [Skill guide](docs/guide.md): Detailed use, configuration, dependencies, and boundaries.
- [Workflow overview](docs/guide.md#workflow-overview) for direct repairs, independent reviews, assessment, and delivery.
- [Update installed skills](docs/guide.md#update-installed-skills): CLI update commands.
- [Metadata policy](docs/agents/skill-metadata.md): Author and date-version maintenance rules.
- [Repository validation](docs/agents/validation.md): Checks for the complete candidate tree.
- [Shared vocabulary](CONTEXT.md) and [architecture decisions](docs/adr/): Terms and design rationale.

Each skill's `SKILL.md` defines its complete behavior. The repository installs directly from GitHub through the skills CLI.

## License

Licensed under the [MIT License](LICENSE).
