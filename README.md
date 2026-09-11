# Skills for Deliberate Engineering

Nine explicit, opt-in agent skills for engineering work that benefits from clearer decisions, bounded exploration, guided learning, and user control.

Use them to make a conversation actionable, reduce low-value interruptions, protect the current task from scope drift, experience a developer tool before judging its implementation, discover evidence-backed ways to reuse a project's value, decide whether an external tool fits a repository, get started with a tool through a complete guide and runnable examples, explore project perspectives you have not considered, or improve skills from their actual use.

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
| Get started with a library, framework, or developer tool | [`get-up-to-speed`](skills/get-up-to-speed/SKILL.md) | One complete guide with runnable examples and depth matched to your goal |
| Discover project questions you did not know to ask | [`expand-the-frame`](skills/expand-the-frame/SKILL.md) | Explained perspectives, informed trade-offs, and follow-up questions derived from your answers |
| Improve skills based on how they were used | [`evolve-skills`](skills/evolve-skills/SKILL.md) | Purpose-led, user-selected improvements with behavioral evidence and per-skill recovery history |

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

## Expand Your Project Perspective

### Expand the Frame

**Use it when:** You want to think beyond your initial framing of a project or idea and understand the questions you have not considered, including questions about the project's goals.

**You get:** Targeted investigation of relevant project facts, explanations of unfamiliar concepts, and rounds of questions with recommendations and viable alternatives. The agent considers risks, opportunities, and simplification, traces your answers into further questions, and connects new perspectives to the decisions they change or support.

**Boundary:** The agent explains why a new direction matters before you choose whether to deepen, defer, or end exploration. Deferred directions return only at your request or when new information materially changes their relevance. The skill is standalone and explicitly invoked; it keeps a conversational record by default, follows project conventions for requested persistence, and leaves implementation to a separate instruction.

```text
$expand-the-frame Help me think through sharing in this notes project. Surface perspectives I have not considered, explain the concepts before asking me to judge, and present each round with recommendations and alternatives. Let me choose which new directions to explore.
```

## Get Started with a Complete Guide

### Get Up to Speed

**Use it when:** You have the relevant language foundations and want to understand a library, framework, or developer tool well enough to use it or begin contributing, without finding and assembling the learning path yourself.

**Not for:** Learning a programming language from scratch, systematic foundational courses, or long-term study planning. The skill identifies this mismatch before preparing material or creating a teaching workspace.

**You get:** One complete, self-contained guide in a language you select, with runnable examples in an independent workspace. The guide explains core capabilities and their relationships, then uses a representative scenario to connect concepts, code choices, mechanisms, results, and useful variations. Official documentation and matching source ground the explanations. A contribution goal adds a related source walkthrough, minimal change, and regression test to the same path.

**Boundary:** The agent delivers the agreed scope in one pass; later conversation clarifies or extends it. Detail serves the intended outcome, with advanced topics explicitly bounded. You do not need to complete exercises or maintain a learning record. Examples and any contribution rehearsal stay in the teaching workspace. Source-access and execution limits are stated explicitly; a gap that prevents the intended outcome requires a decision about scope before the guide can be called complete.

```text
$get-up-to-speed Help me get started with Rolldown so I can contribute. Write one complete guide in English explaining the core capabilities through a representative example, including a related source walkthrough, minimal change, and regression test. Keep runnable examples alongside the guide in a new workspace.
```

The original design drew on the purposeful lessons in [Matt Pocock's teach skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md). Get Up to Speed delivers a bounded guide and examples as one artifact; it does not manage an ongoing teaching program. The reference is attribution only and is not fetched during use.

## Evolve Skills from Experience

**Use it when:** You have used one or more skills in a conversation and want to improve their future use. Named targets limit the review to those skills; otherwise it identifies the skills actually used. It reads each target's description and instructions before analyzing the available conversation, including successful adaptations and opportunities for better methods.

**You get:** Concrete hypotheses discussed before modification, before/after behavioral comparisons with relevant transfer probes, and detailed private per-skill history explaining the evidence, choices, exact changes, validation, and recovery method. Each run reconciles external edits with the last recorded active state and preserves known history gaps. History follows the source repository under the Git-ignored `docs/skill-evolution/<skill-name>/`; standalone installations use an agreed persistent location. Private records require separate backup or handoff.

**Boundary:** Actual skill use is required. A catalog entry or mention alone is insufficient. Personal preferences remain usage context; shared changes must serve the target's domain, and each iteration examines the whole method for cumulative drift. Candidates remain separate during validation, then supported selected changes are applied in the same run using existing approval. A concrete validation blocker leaves a retained candidate and Pending Validation record; merely unperformed checks remain work to complete.

```text
$evolve-skills Review the skills used in this conversation against their purposes. Discuss concrete improvements with me, then validate and record the changes I select, preserving what is needed to reverse them.
```

It works independently and pairs well with Matt Pocock's grilling series for deeper discussion of the proposed changes. Those skills are optional and installed separately.

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

```text
$evolve-skills $grill-with-docs Find opportunities to improve the skills used here. Stress-test the hypotheses and trade-offs before applying the changes I select, and preserve detailed evolution history.
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
