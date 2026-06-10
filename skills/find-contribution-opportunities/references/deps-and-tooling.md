# Discovery pass: Deps & tooling

Find maintenance opportunities in dependencies, build config, and CI. These are easy to scope but **acceptance varies a lot** — some projects automate dep bumps (Renovate/Dependabot) and reject manual ones. Always check the Project Profile disqualifiers first. Read-only throughout.

## 1. Check for existing automation (do this first)

If the repo has `renovate.json`, `.github/dependabot.yml`, or a bot opening dep PRs, **do not** surface manual dependency bumps — they'll be closed. Note the automation and skip that sub-pass.

## 2. Outdated / vulnerable dependencies (`type: build` or `chore`)

Only if not automated. Inspect the manifest/lockfile and report what's actionable:

```bash
# Node
npm outdated || pnpm outdated || yarn outdated
npm audit --omit=dev
# Rust / Python / Go (use what applies)
cargo outdated ; pip list --outdated ; go list -m -u all
```

Favor candidates with a clear motivation (security advisory, a dep that unblocks a feature, EOL runtime) over cosmetic "newer exists" bumps.

## 3. Deprecation warnings (`type: refactor` / `fix`)

Run the build/test once and read warnings (deprecated APIs, peer-dep mismatches, engine warnings). Each distinct deprecation that has a documented replacement is a candidate.

## 4. Lint / format violations (`type: chore` / `style`)

```bash
# Use the project's own config — don't impose your own
npm run lint 2>&1 | tail -40
npx prettier --check . ; ruff check . ; cargo clippy
```

Surface only if the project's lint/format isn't already clean in CI and accepts such PRs. A repo-wide reformat is usually unwelcome — prefer a scoped, already-failing target.

## 5. Config / CI drift (`type: ci` / `build`)

- CI using a deprecated action version or EOL runtime image.
- Missing/obsolete config (e.g. references a removed file, stale Node/Python version matrix).
- Build scripts referencing tools no longer used.

Read `.github/workflows/*`, `package.json` engines, `tsconfig`/`pyproject`/`Cargo.toml`.

## Map to candidates

`location` = the manifest/config file (`package.json`, `.github/workflows/ci.yml`, ...); `evidence` = the specific outdated version / warning / failing check; `summary` = the proposed bump or fix and its motivation.

## Guardrails

- **Automation check gates this whole pass** — respect it.
- Prefer motivated, scoped changes over churn. Maintainers dislike noisy dependency/style PRs.
- Major-version bumps often carry breaking changes → flag as larger effort for the feasibility stage.
