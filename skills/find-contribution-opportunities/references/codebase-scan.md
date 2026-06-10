# Discovery pass: Codebase scan

Find contribution opportunities the maintainers left *in the code itself*. Requires a local clone (or fetched sources). All actions are read-only — `Grep`/`Read` only, no edits.

## 1. Explicit markers

Authors leave breadcrumbs. Search for them:

```
TODO  FIXME  HACK  XXX  BUG  WORKAROUND  @deprecated  "for now"  "temporary"
```

Use `Grep` (ripgrep) across source, excluding vendored/build dirs:

```
rg -n --no-heading -i "\b(TODO|FIXME|HACK|XXX|BUG)\b" -g '!**/node_modules/**' -g '!**/dist/**' -g '!**/vendor/**'
```

For each hit, read enough surrounding context to judge whether it's a real, self-contained task. Many TODOs are aspirational or stale — keep only ones a contributor could actually close.

- A marker that describes a concrete missing behavior → `fix` or `feat`.
- "clean this up / simplify" → `refactor`.
- "this is slow" → `perf`.

## 2. Smells worth a small PR

Look for low-risk, self-contained issues (these read well to maintainers and merge easily):

- **Missing error handling** — unchecked returns, swallowed exceptions, `catch {}` with no handling, unawaited promises.
- **Obvious type gaps** — `any`/`unknown` that could be narrowed, missing return types in typed codebases, `// @ts-ignore` / `# type: ignore` left in.
- **Dead or unreachable code** — unused exports/functions (cross-check call sites with `Grep` before claiming), commented-out blocks.
- **Inconsistent patterns** — one module does X the documented way, a sibling doesn't.
- **Copy-paste duplication** that an extraction would de-risk.

## 3. Map to candidates

For each kept finding:

- `type`: per the mapping above.
- `location`: `path:line`.
- `evidence`: the exact marker text or a 1-line code excerpt.
- `summary`: what's wrong and the conceptual fix.

## Guardrails

- **Verify before claiming dead code** — "unused" is easy to get wrong; confirm there are no dynamic/string references.
- **Keep candidates small.** A sprawling "refactor the whole module" is not a good first PR; split or skip it.
- **Cross-check against issues** — if a TODO is already tracked, it's the same candidate (de-dupe; prefer the issue location).
- Respect Project Profile disqualifiers (e.g. some projects reject pure style/refactor PRs).
