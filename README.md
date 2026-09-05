# Skills for Deliberate Engineering

Seven explicit, opt-in agent skills for engineering work that benefits from clearer decisions, bounded exploration, guided learning, and user control.

Use them to make a conversation actionable, reduce low-value interruptions, protect the current task from scope drift, experience a developer tool before judging its implementation, discover evidence-backed ways to reuse a project's value, decide whether an external tool fits a repository, or get familiar with a tool through guided demonstrations.

Each skill has a narrow responsibility. Invoking one does not silently expand the task, transfer a user-owned decision, or bypass an existing safety, authorization, or external-effect checkpoint.

## Quick Start

You need Node.js with `npx` and an agent supported by the [skills CLI](https://skills.sh).

Install from this GitHub repository:

```bash
npx skills@latest add SaKaNa-Y/skills
```

The interactive installer discovers the available skills and lets you choose which ones and which detected agents to use. Installation is project-scoped by default.

Preview the available skills without installing anything:

```bash
npx skills@latest add SaKaNa-Y/skills --list
```

Install one skill directly:

```bash
npx skills@latest add SaKaNa-Y/skills --skill prune-the-tree
```

For agents that support a user-level skills directory, add `--global` to make a skill available across projects:

```bash
npx skills@latest add SaKaNa-Y/skills --skill prune-the-tree --global
```

Omit `--yes` when you want the installer to prompt for skills and agents.

This repository does not publish its own npm package. `npx` runs the general-purpose `skills` CLI, which installs the skill folders directly from GitHub.

## Choose a Skill

| When you need to... | Use | What you receive |
|---|---|---|
| Make an important question or answer understandable and actionable | [`make-it-land`](skills/make-it-land/SKILL.md) | The missing context, terms, evidence, implications, and next action |
| Stop a workflow from asking you to decide routine details | [`prune-the-tree`](skills/prune-the-tree/SKILL.md) | Fewer low-value interruptions without losing user-owned decisions |
| Keep a valid side problem from replacing the current task | [`yak-shaving-triage`](skills/yak-shaving-triage/SKILL.md) | A preserved, issue-ready finding and a return to the original problem |
| Evaluate a source-accessible library, framework, CLI, or developer tool as a user | [`just-use-it`](skills/just-use-it/SKILL.md) | Hands-on coverage evidence and reproducible Finding Packets |
| Find where an existing project's value could serve more real contexts | [`set-theory-for-projects`](skills/set-theory-for-projects/SKILL.md) | Evidence-backed candidates, rejection reasons, and experiment ladders |
| Decide whether a tool fits a repository need | [`tool-fit-for-projects`](skills/tool-fit-for-projects/SKILL.md) | A comparison against the current baseline and a progressive adoption path |
| Learn the common capabilities of a library, framework, or developer tool | [`get-up-to-speed`](skills/get-up-to-speed/SKILL.md) | Documentation-grounded demonstrations and a retained teaching workspace |

## Invoke Skills Explicitly

Every skill in this repository runs only when you select it. The examples use the `$skill-name` convention; use the equivalent explicit-invocation syntax supported by your agent.

```text
$prune-the-tree Help me implement this feature. Resolve routine choices yourself and ask me only about decisions that change the outcome.
```

You can invoke compatible skills together. Each remains responsible for its own behavior; one skill does not silently activate or control another.

## Keep the Current Work Clear and Controlled

These skills modify how the current task is communicated or protected. They do not take ownership of the task itself.

### Make It Land

**Use it when:** An important question or answer is technically correct but lacks enough context to understand, evaluate, or act on. Invoke it after a message that did not land, or alongside a task to keep substantive messages clear throughout the work.

**You get:** A proportionate explanation of the situation, necessary terms, evidence, trade-offs, implications, and next action. Questions include viable options and a recommendation when the evidence supports one.

**Boundary:** It improves communication without changing the task's scope, decision ownership, safety rules, or authorization requirements.

```text
$make-it-land Re-pitch your last answer. Explain the unfamiliar terms, the evidence behind the recommendation, what it changes, and what I should do next.
```

### Prune the Tree

**Use it when:** A workflow is generating too many questions, especially questions the repository, documentation, environment, or a reversible local default can answer.

**You get:** Each candidate question is found, dropped, defaulted, deferred, or asked. Only decisions that belong to you remain synchronous, and material defaults are summarized in a compact Decision Ledger.

**Boundary:** It reduces Decision Load, not reasoning effort or decision quality. Goals, acceptance criteria, user-visible behavior, domain rules, authorization, security, persistent data, and costly or irreversible choices remain yours.

```text
$prune-the-tree Build this feature. Investigate factual questions, use safe local defaults for routine implementation details, and ask me about choices that affect what users receive.
```

### Yak Shaving Triage

**Use it when:** Work on one problem is likely to reveal other valid problems, and you want to preserve those findings without abandoning the current task.

**You get:** Silent scope checks during the task. A distinct, observable problem is preserved as an issue-ready draft, reconciled against existing open and closed records in the project's canonical tracker at an eligible checkpoint, and recorded only after approval.

**Boundary:** It does not diagnose or repair the side problem, take over the active workflow, invent a tracker, or mutate a tracker without explicit approval. Urgent security or data-loss risks are surfaced immediately but still do not bypass reconciliation or write approval.

```text
$yak-shaving-triage Fix the checkout failure. Preserve any independently actionable problems we encounter, but keep this task focused on checkout.
```

## Investigate Before Changing

These skills create evidence and decision checkpoints. They stop before implementation, adoption, migration, or publication unless you explicitly start a separate task for that work.

### Just Use It

**Use it when:** You need to evaluate a source-accessible library, framework, CLI, or developer tool through the experience its users actually receive.

**You get:** A slice-first Usage-First Audit that completes one user outcome and its discriminating variation before moving to another, then reads source to find shipped public capabilities the hands-on work missed. The result includes honest partial-coverage boundaries, Verification Traces, and reproducible Finding Packets.

**Boundary:** It does not diagnose or repair findings, publish issues, or count source inspection as successful usage. Disposable audit resources are cleaned up or reported if cleanup fails.

```text
$just-use-it Exercise this CLI through every documented public capability, explore it as a new user, then inspect source for public behavior the hands-on passes missed.
```

### Set Theory for Projects

**Use it when:** An existing project may contain value that could serve additional real contexts, but you do not yet know whether the right move is a reusable core, a bounded adapter, a platform seam, or no expansion at all.

**You get:** Bounded cross-project research, bilateral evidence from the current project and real adjacent contexts, up to five candidate cards, meaningful rejections, and falsifiable experiment ladders.

**Boundary:** Discovery is read-only and stops at an Exploration Checkpoint. It does not prototype, integrate, or change another project. Preserving the current scope is a valid result.

```text
$set-theory-for-projects Find evidence-backed ways this project's existing value could serve more real contexts while preserving what makes the project specific.
```

### Tool Fit for Projects

**Use it when:** You need either a concrete tool decision or a bounded audit of the repository for material tool opportunities.

**You get:** A comparison against the Current Baseline, evidence-based candidate dispositions, relevant compatibility gates, and progressive paths for testing or adopting the strongest choices. A repository-wide audit returns at most five opportunities and waits for you to select one before researching candidates.

**Boundary:** It does not install, purchase, prototype, migrate, or change services. Keeping the current approach is a valid result, and selecting a recommendation does not authorize implementation.

```text
$tool-fit-for-projects Compare this repository's current test setup with suitable alternatives and stop at a recommendation before making changes.
```

```text
$tool-fit-for-projects Audit this repository for material tool opportunities, then let me choose one before you research products.
```

## Learn Through Demonstrations

### Get Up to Speed

**Use it when:** You want a practical introduction to a library, framework, or developer tool, with the agent demonstrating and explaining its common capabilities.

**You get:** Official-documentation preparation, explanations in a language you select, and one coherent topic at a time. The agent connects purpose and effects to necessary concepts, code, and observable results, then waits for your questions or direction to continue. An independent teaching folder retains the examples, explanations, run instructions, and source links.

**Boundary:** Progress does not depend on you changing code or completing exercises. One invocation supports the full conversation; retained material does not imply a recurring course. Examples belong to the teaching workspace, and execution limits are stated explicitly.

```text
$get-up-to-speed Introduce me to Rolldown's common bundling capabilities. Explain in English, demonstrate each topic yourself, and keep the examples and notes in a new teaching folder. Pause between topics so I can ask questions.
```

The teaching structure draws on sampled sections of [HDAlex_John's Shadcn quickstart](https://www.bilibili.com/video/BV1ye411v7Q2/), connecting official documentation, code, and visible results, and on the short, purposeful lessons in [Matt Pocock's teach skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md). These are design references; the installed skill is self-contained and does not fetch those courses during teaching.

## Combine Skills

Use combinations when two independent responsibilities are both useful:

- `make-it-land` + `prune-the-tree`: ask fewer questions, and make every remaining question easy to understand and answer.
- `just-use-it` + `yak-shaving-triage`: exercise a tool independently, freeze confirmed findings, reconcile each against existing tracker records, and request approval before writing.
- `make-it-land` + another task skill: keep explanations actionable while the task skill owns the work.

For example:

```text
$make-it-land $prune-the-tree Help me design this change. Ask only user-owned questions, and give each question enough context for me to make the decision.
```

Some useful combinations require skills that are not included in this repository. Install those skills separately before invoking them:

```text
$prune-the-tree $grill-with-docs Stress-test this product idea without offloading routine implementation choices to me.
```

```text
$yak-shaving-triage $grilling Stress-test this design, preserve unrelated confirmed problems, and keep the interview focused on the design.
```

## Design Principles

- **Explicit activation:** A skill runs because you selected it, not because the model silently opted into a broader workflow.
- **Narrow ownership:** Each skill changes one responsibility and leaves the current task, other skills, and mandatory checkpoints in place.
- **Evidence before expansion:** Facts come from the repository, real use, current documentation, and traceable sources rather than plausible guesses.
- **Bounded exploration:** Broad research has an explicit stopping condition and returns control at a named checkpoint.
- **No change is valid:** An audit may conclude that the current scope, tool, or approach is stronger than the alternatives.
- **Approval remains explicit:** Installing, purchasing, publishing, mutating external systems, or performing irreversible work requires the authority already expected by the active task.

## Update Installed Skills

Use the skills CLI to update installed skills:

```bash
npx skills update
```

Or update one skill by name:

```bash
npx skills update prune-the-tree
```

## Repository Layout

Each installable skill lives in its own directory:

```text
skills/
└── skill-name/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
```

`SKILL.md` is required and contains the skill's name, description, and instructions. Agent metadata and reference files are optional. Once a valid skill directory is committed and pushed to GitHub, the skills CLI can discover it from this repository; no repository-specific npm package is required.

## Reference

- [`CONTEXT.md`](CONTEXT.md) defines the shared vocabulary used across the skills.
- [`docs/adr/`](docs/adr/) records the architectural decisions that keep composition, discovery, and finding publication bounded.
- [`docs/evals/`](docs/evals/) contains maintainer-only Reference Audit Suites that validate general contracts without entering installed skill runtime paths.
- Each linked `SKILL.md` is the authoritative contract for that skill's complete behavior and stopping conditions.

## License

Licensed under the [MIT License](LICENSE).
