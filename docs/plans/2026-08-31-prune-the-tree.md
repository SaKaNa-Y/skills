# Prune the Tree Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add an explicit-only Modifier Skill that reduces Decision Load by pruning low-value questions while preserving user-owned decisions and mandatory checkpoints.

**Architecture:** Keep the behavior in one short `SKILL.md`: every candidate question is routed through a five-way pruning decision, guarded by a conservative Decision Boundary, and material delegated choices are disclosed in a Decision Ledger. Add Codex UI metadata with implicit invocation disabled, and record the new Modifier Skill composition contract in one ADR.

**Tech Stack:** Markdown, YAML, the bundled Python skill initializer and validator, independent Codex subagent forward tests

---

### Task 1: Record the composition decision

**Files:**
- Modify: `CONTEXT.md`
- Create: `docs/adr/0001-explicit-modifier-skills.md`

**Step 1: Verify the glossary**

Confirm `CONTEXT.md` defines Decision Load, Modifier Skill, Decision Boundary, Decision Ledger, and Decision Pruning without implementation details.

**Step 2: Write the ADR**

Create `docs/adr/0001-explicit-modifier-skills.md`:

```markdown
# Explicit Modifier Skills May Specialize Task Workflows

Explicit-only Modifier Skills may specialize named ordinary process rules of another active skill without taking ownership of its work. We keep Co-active Skills independent, use modifiers only through direct user selection, and preserve mandatory safety, authorization, external-effect, and human checkpoints; this permits deliberate question pruning without silently broadening agent authority.
```

**Step 3: Check the decision against the ADR threshold**

Confirm it remains hard to reverse after other modifiers depend on it, surprising beside the existing Co-active Skill rule, and the result of a real composability-versus-independence trade-off.

### Task 2: Scaffold the explicit-only skill

**Files:**
- Create: `skills/prune-the-tree/SKILL.md`
- Create: `skills/prune-the-tree/agents/openai.yaml`

**Step 1: Run the initializer**

Run:

```powershell
python C:\Users\86138\.codex\skills\.system\skill-creator\scripts\init_skill.py prune-the-tree --path F:\Github_Project\skills\skills
```

Expected: a new `skills/prune-the-tree/` directory with `SKILL.md` and `agents/openai.yaml`.

**Step 2: Make invocation explicit-only**

State the direct-invocation boundary in the `SKILL.md` description and set `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. Keep frontmatter within the repository validator's supported Agent Skills fields.

### Task 3: Write the pruning behavior

**Files:**
- Modify: `skills/prune-the-tree/SKILL.md`
- Modify: `skills/prune-the-tree/agents/openai.yaml`

**Step 1: Write the skill entrypoint**

Use this behavioral shape, tightening wording during implementation:

```markdown
---
name: prune-the-tree
description: Prune low-value questions while preserving decisions that belong to the user. Use only when the user explicitly invokes $prune-the-tree.
---

# Prune the Tree

Keep the trunk. Prune the branches.

Act as a Modifier Skill for the current User Problem. Stay active across turns until the problem is resolved or the user asks to return to normal questioning. Optimize Decision Load, not question count or model reasoning time.

Before asking, route every candidate question as FIND, DROP, DEFAULT, DEFER, or ASK. Apply the conservative Decision Boundary to DEFAULT, preserve mandatory checkpoints, and report material delegated choices in a compact Decision Ledger.
```

Expand the routing and completion criteria in the same file, keeping the whole entrypoint under 100 lines and each meaning in one place.

**Step 2: Write UI metadata**

Use:

```yaml
interface:
  display_name: "Prune the Tree"
  short_description: "Prune low-value questions while preserving user decisions"
  default_prompt: "Use $prune-the-tree to reduce decision load while keeping important choices with me."
policy:
  allow_implicit_invocation: false
```

### Task 4: Validate structure and prose

**Files:**
- Inspect: `skills/prune-the-tree/SKILL.md`
- Inspect: `skills/prune-the-tree/agents/openai.yaml`
- Inspect: `CONTEXT.md`
- Inspect: `docs/adr/0001-explicit-modifier-skills.md`

**Step 1: Run structural validation**

Run:

```powershell
F:\Anaconda\python.exe -X utf8 C:\Users\86138\.codex\skills\.system\skill-creator\scripts\quick_validate.py F:\Github_Project\skills\skills\prune-the-tree
```

Expected: validation succeeds with no frontmatter, naming, or scaffold-placeholder errors.

**Step 2: Run repository checks**

Run `git diff --check` and inspect the full diff. Expected: no whitespace errors, unrelated edits, duplicated rules, or stale scaffold text.

**Step 3: Apply `@writing-for-agents` review**

Verify the description is human-facing because invocation is explicit-only; every line changes behavior; the five routes, Decision Boundary, Decision Ledger, composition, persistence, and completion criteria are co-located and non-duplicative.

### Task 5: Forward-test behavior

**Files:**
- Inspect: `skills/prune-the-tree/SKILL.md`
- Use: isolated temporary test workspaces only

**Step 1: Run independent paired cases**

Give independent subagents realistic small reversible implementation, preference-heavy UI, public API, domain-conflict, external-effect, and open-ended planning requests. Give evaluators only the request and skill under test, not the intended classification.

**Step 2: Compare outcomes**

Measure mandatory-question retention, low-value-question reduction, correction count, goal drift, unauthorized assumptions, and rework. Do not treat shorter prose or lower token count as proof.

**Step 3: Enforce the acceptance gate**

Pass only when user-owned questions are retained, low-value questions fall by at least 30%, and no new material drift, authorization failure, or irreversible rework appears.

**Step 4: Iterate narrowly**

Change only rules implicated by observed failures, rerun the failing case and a nearby safe case, then repeat structural validation.
