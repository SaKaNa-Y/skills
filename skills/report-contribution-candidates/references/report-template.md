# Report template

Render the final report in exactly this shape. Replace `<...>` placeholders. Omit a type section if it has no candidates.

---

```markdown
# Contribution Scouting Report — <owner>/<repo>

**Scanned:** <date/commit or "remote">  ·  **Access:** <gh CLI | REST API>
**Conventions:** <commit convention> · <PR requirements in brief> · **Legal:** <CLA/DCO/none>
**Disqualifiers:** <types the project won't accept, or "none stated">
**Candidates found:** <N total> — feat <n> · fix <n> · docs <n> · test <n> · refactor <n> · perf <n> · build <n> · ci <n> · chore <n>
<if any stage capped/dropped candidates, note it here>

## Top picks

| # | Type | Title | Loc | Effort | Merge | Why |
|---|------|-------|-----|--------|-------|-----|
| 1 | fix  | <title> | <#12 / path:line> | S | 🟢 High | <dominant factor> |
| 2 | docs | <title> | <path>  | S | 🟢 High | <dominant factor> |
| 3 | test | <title> | <path>  | M | 🟡 Med  | <dominant factor> |

*(Merge: 🟢 High · 🟡 Medium · 🔴 Low)*

## All candidates by type

### fix
- **C3 · <title>** — <#12 / path:line>
  - Feasibility: feasible · Effort: S · Merge: 🟢 High (<dominant factor>)
  - Rationale: <1-2 lines of evidence>
  - Suggested approach: <1-3 sentences, conceptual — what/where would change. No code.>

### docs
- **C7 · <title>** — <path>
  - Feasibility: feasible · Effort: S · Merge: 🟡 Medium (<dominant factor>)
  - Rationale: <...>
  - Suggested approach: <...>

### test
- ...

<... remaining type sections ...>

### Not actionable now
- **C9 · <title>** — blocked (already has open PR #44)
- **C5 · <title>** — needs-discussion (feature requires an RFC first per CONTRIBUTING)

---

⚠️ **Nothing has been changed.** This is a scouting report only — no code was modified, no branch created, no PR opened. Picking what (if anything) to work on is entirely your call. Tell me which candidate you'd like to pursue and I'll hand it back to you / the main session to implement.
```
