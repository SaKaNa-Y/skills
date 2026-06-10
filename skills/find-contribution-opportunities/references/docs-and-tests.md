# Discovery pass: Docs & tests gaps

Documentation and test contributions are often the highest-acceptance, lowest-risk PRs — maintainers welcome them and they rarely break anything. Read-only throughout.

## Docs gaps (`type: docs`)

- **Undocumented public API** — exported functions/components/CLI flags/config options with no doc entry. Compare the public surface (exports, `--help`, schema) against the docs site / README.
- **README drift** — install/usage/example steps that no longer match current commands, options, or output.
- **Broken or missing examples** — code samples that reference removed APIs, dead links, examples that won't run. Check links and sample imports against the current code.
- **Missing essentials** — no documented setup, no troubleshooting, missing migration notes for a recent breaking change (check `CHANGELOG`/recent tags).
- **Typos & clarity** — only worth a candidate if the project accepts such PRs (check disqualifiers; many large projects discourage trivial typo PRs).

For each: `location` = doc file path or the undocumented symbol's `path:line`; `evidence` = the specific gap; `summary` = what to document.

## Tests gaps (`type: test`)

- **Untested code paths** — modules/functions with no corresponding test file, or branches with no coverage. If a coverage report exists (`coverage/`, CI artifacts), use it; otherwise reason from test-file presence vs source-file presence.
- **Failing or flaky CI** — read the latest runs and surface concrete failures:
  ```bash
  gh run list --repo {owner}/{repo} --limit 10
  gh run view <run-id> --repo {owner}/{repo} --log-failed
  ```
  A reproducible failing test or a flaky test that needs stabilizing is a strong candidate (`type: test` or `fix`).
- **Missing regression test** for a recently fixed bug (cross-reference recent fix commits/PRs that landed without a test).

For each: `location` = source file needing tests or the failing test name; `evidence` = the gap or the failure excerpt; `summary` = what to test.

## Guardrails

- Don't propose tests for code that's already well covered — verify the gap is real.
- A failing CI job may be infra/secrets-related, not a code bug; note that uncertainty in `evidence` so the feasibility stage can check.
- De-dupe against issues and the codebase pass.
