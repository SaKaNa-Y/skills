# Tool Fit for Projects Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add an explicit-only, read-only skill that resolves repository-context Tool Decisions or discovers Material Tool Opportunities without assuming that adopting a new tool is the correct result.

**Architecture:** Keep the invariant workflow, decision gates, proportional report contract, and user checkpoint in one `SKILL.md`. Disclose the four category-specific risk profiles through separate references so each run loads only the profiles relevant to its candidates. Add explicit invocation metadata, repository documentation, structural validation, and independent behavioral forward tests.

**Tech Stack:** Markdown, YAML, the bundled Python skill initializer and validator, repository files and primary web sources, independent Codex subagent forward tests

---

### Task 1: Preserve the research and domain model

**Files:**
- Inspect: `docs/research/antfu-progressive-path.md`
- Inspect: `CONTEXT.md`

**Step 1: Verify the source boundary**

Confirm the research distinguishes Antfu's original cost balance and progressive paths from the skill's independent repository-analysis, search, gate, and recommendation extensions.

**Step 2: Verify the shared language**

Confirm `CONTEXT.md` defines Tool Decision, Current Baseline, Tool Fit, Candidate Seed, Candidate Gate, Evidence Saturation, Decision Depth, Tool Candidate Disposition, Repository Tool Audit, Tool Decision Report, and Tool Choice Checkpoint without implementation detail.

**Step 3: Apply the ADR threshold**

Do not create an ADR unless implementation reveals a hard-to-reverse and surprising decision not already covered by `docs/adr/0002-cross-project-discovery-is-explicit-and-bounded.md`.

### Task 2: Scaffold the explicit-only skill

**Files:**
- Create: `skills/tool-fit-for-projects/SKILL.md`
- Create: `skills/tool-fit-for-projects/agents/openai.yaml`
- Create: `skills/tool-fit-for-projects/references/`

**Step 1: Run the initializer**

Run:

```powershell
F:\Anaconda\python.exe -X utf8 C:\Users\86138\.codex\skills\.system\skill-creator\scripts\init_skill.py tool-fit-for-projects --path F:\Github_Project\skills\skills --resources references
```

Expected: a new `skills/tool-fit-for-projects/` directory containing `SKILL.md`, `agents/openai.yaml`, and an empty `references/` directory.

**Step 2: Make invocation user-only**

Keep the `SKILL.md` description human-facing and set `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. The repository validator does not support `disable-model-invocation` frontmatter, so the product metadata is the invocation control.

**Step 3: Remove scaffold residue**

Replace all generated TODO text; do not add assets, scripts, examples, or placeholder files.

### Task 3: Write the invariant decision workflow

**Files:**
- Modify: `skills/tool-fit-for-projects/SKILL.md`

**Step 1: Write discriminating frontmatter**

Use this shape, tightening wording during implementation:

```markdown
---
name: tool-fit-for-projects
description: Evaluate which tools fit a repository need, or audit the repository for material tool opportunities, without implementing a change.
---
```

**Step 2: Route the two modes**

Define:

- **Tool Decision** for a concrete framework, library, infrastructure, platform, or service choice.
- **Repository Tool Audit** for a first-stage scan that returns at most five Material Tool Opportunities and stops at user selection.

Completion criterion: every invocation enters exactly one mode; an audit never silently expands into full candidate research.

**Step 3: Establish decision context and depth**

Require the concrete repository work, affected users, desired outcome, constraints, and success conditions before comparing products. Classify the work as Quick, Standard, or High-stakes from change radius, reversibility, data or external effects, and migration burden.

Completion criterion: generic product comparisons have been reframed into a repository-context decision, and the selected depth is justified by observable risk.

**Step 4: Establish the Current Baseline and early exit**

Compare the present tool, local implementation, manual work, or deliberate absence of a tool. Return a No-change Result early when no material problem exists or the likely research and adoption cost exceeds the plausible benefit.

Completion criterion: the baseline can be evaluated beside external candidates and no-change remains a successful outcome.

**Step 5: Apply the Tool Evidence Hierarchy**

Use repository facts and existing validation first, authoritative project or vendor sources second, and reproducible independent evidence only for claims those sources cannot establish. Ask the user only for a material constraint that cannot be discovered.

Completion criterion: every material claim is traceable and every unresolved gate is explicit.

**Step 6: Discover candidates to Evidence Saturation**

Treat user-named tools as Candidate Seeds rather than an exhaustive set. Search independent solution shapes until additional paths no longer produce a materially different qualified candidate. Keep at most five full finalists; give every user-named candidate a disposition and reason.

Completion criterion: the search boundary, paths checked, stopping condition, and omitted user seeds are all visible.

**Step 7: Gate before comparing**

Read the relevant category profile references. Apply runtime, license, security, compliance, data, operational, and other non-negotiable Candidate Gates before qualitative comparison. Compare benefits with discovery, learning, price, adoption, migration, and maintenance cost without a numeric score.

Completion criterion: no failed gate is offset by popularity or features, and every finalist has a Tool Candidate Disposition.

**Step 8: Design progressive paths without executing them**

For Recommended and Trial candidates, define the cheapest pre-trial verification, isolated trial, coexistence or migration checkpoint, passing and killing observations, and rollback or exit path. Use Read-only Validation only; do not install candidates, modify files, or create prototypes.

Completion criterion: every proposed change can be tested and abandoned before irreversible adoption.

**Step 9: Return the proportional report and checkpoint**

Always include result, Tool Decision Context, Current Baseline, evidence boundary, candidate dispositions, recommendation plus viable choices, and Tool Choice Checkpoint. Compress Quick decisions; fully expand High-stakes risks. Default to conversation-only output.

Completion criterion: the user can select a candidate, keep the baseline, authorize targeted evidence gathering, or stop without implementation being implied.

**Step 10: Attribute the source lens**

Add an `Origin of the Lens` section linking Antfu's official talk and source slides. Attribute cost balance and progressive paths to Antfu while identifying the repository workflow as an independent extension.

### Task 4: Write the category profiles

**Files:**
- Create: `skills/tool-fit-for-projects/references/code-and-developer-tools.md`
- Create: `skills/tool-fit-for-projects/references/data-and-infrastructure.md`
- Create: `skills/tool-fit-for-projects/references/cloud-and-deployment.md`
- Create: `skills/tool-fit-for-projects/references/hosted-and-commercial-services.md`

**Step 1: Write the code and developer tools profile**

Cover language and runtime compatibility, framework and build integration, API and type surface, output or runtime overhead, maintenance and release policy, ecosystem compatibility, migration scope, and supply-chain risk.

**Step 2: Write the data and infrastructure profile**

Cover data model fit, correctness and consistency, durability, backup and restore, migration and rollback, operational ownership, capacity and performance evidence, observability, topology, and failure modes.

**Step 3: Write the cloud and deployment profile**

Cover regions and runtime availability, deployment model, identity and access, networking, scaling, service limits, reliability and support, portability, egress, pricing shape, and exit path.

**Step 4: Write the hosted and commercial services profile**

Cover product fit, pricing and contract constraints, data handling and residency, security and compliance evidence, identity and access, integrations, export and deletion, service continuity, vendor dependency, and exit path.

Completion criterion: each reference contains only category-specific gates and comparison concerns; the shared workflow remains single-sourced in `SKILL.md`.

### Task 5: Write UI metadata and repository documentation

**Files:**
- Modify: `skills/tool-fit-for-projects/agents/openai.yaml`
- Modify: `README.md`

**Step 1: Write explicit invocation metadata**

Use:

```yaml
interface:
  display_name: "Tool Fit for Projects"
  short_description: "Evaluate tool fit against repository evidence"
  default_prompt: "Use $tool-fit-for-projects to evaluate which tools fit this repository need without implementing a change."
policy:
  allow_implicit_invocation: false
```

**Step 2: Update the README inventory**

Add the skill to the opening summary, skills table, installation commands, usage examples, a concise behavior section, and the skill-composition summary. Link the Antfu research note and clarify the skill is independent and unofficial.

Completion criterion: a reader can discover, install, invoke, and distinguish the skill from `set-theory-for-projects` without opening its implementation.

### Task 6: Validate structure and writing

**Files:**
- Inspect: `skills/tool-fit-for-projects/SKILL.md`
- Inspect: `skills/tool-fit-for-projects/agents/openai.yaml`
- Inspect: `skills/tool-fit-for-projects/references/*.md`
- Inspect: `README.md`
- Inspect: `CONTEXT.md`

**Step 1: Run structural validation**

Run:

```powershell
F:\Anaconda\python.exe -X utf8 C:\Users\86138\.codex\skills\.system\skill-creator\scripts\quick_validate.py F:\Github_Project\skills\skills\tool-fit-for-projects
```

Expected: validation succeeds with no naming, frontmatter, or unfinished-placeholder errors.

**Step 2: Run repository checks**

Run `git diff --check`, inspect `git status --short`, and review the full diff. Expected: no unrelated edits, whitespace errors, stale scaffold text, duplicated rules, or uncited attribution claims.

**Step 3: Apply the writing-for-agents review**

Verify every step has a checkable completion criterion, the explicit-only description is human-facing, invariant steps remain visible, category branches are disclosed behind precise pointers, each meaning has one source of truth, and every sentence changes agent behavior.

### Task 7: Forward-test behavior

**Files:**
- Inspect: `skills/tool-fit-for-projects/`
- Use: isolated temporary workspaces only

**Step 1: Test four independent cases**

Give independent evaluators only the skill and realistic prompts for:

- a Quick request where a tiny local implementation should beat adding a dependency;
- a Standard test-tool migration with many user-provided Candidate Seeds;
- a High-stakes data or hosted-service choice with an unresolved compliance constraint;
- a Repository Tool Audit that must stop after opportunity triage.

**Step 2: Evaluate observable invariants**

Pass only when each run establishes repository context, preserves the baseline, searches beyond user seeds when warranted, applies category gates before comparison, avoids numeric scoring, respects Decision Depth, produces the correct dispositions, and stops at the Tool Choice Checkpoint without mutation.

**Step 3: Iterate narrowly**

Change only instructions implicated by observed failures, rerun the failing case and a nearby safe case, then repeat structural and repository validation.
