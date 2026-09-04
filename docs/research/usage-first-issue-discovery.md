# Usage-First Issue Discovery Patterns from Developer Tools

> Research date: 2026-09-04
>
> Scope: first-party documentation and issue reports from pnpm, Vite+, Oxc, Rolldown, Bun, Playwright, and VS Code. The issue sample is used to recover discovery conditions, not implementation causes. This note evaluates the pre-change `just-use-it` workflow and records the evidence used by the subsequent skill update.

## Conclusion

At the start of this research, `just-use-it` **could surface the behavior behind pnpm #14507, but it would not do so reliably**.

The report was produced by ordinary use: a user who already had another runtime manager noticed that enabling pnpm runtime management materialized another `node`, consumed storage twice, and could select a version different from the user's other manager. The requested capability is not “make runtime management work”; it is “disable one managed runtime while retaining the others.” pnpm currently labels this an open feature request, not a confirmed bug. [pnpm #14507](https://github.com/pnpm/pnpm/issues/14507)

Following the documentation would exercise the underlying feature: `devEngines.runtime` may declare one or multiple runtimes, `pnpm install` resolves them, records exact versions in the lockfile, and runs scripts with the local runtime. The documented `runtimeOnFail` control overrides `onFail` uniformly; it is not a per-runtime control. [pnpm `devEngines.runtime` documentation](https://pnpm.io/package_json#devenginesruntime) [pnpm `runtimeOnFail` documentation](https://pnpm.io/settings/cli#runtimeonfail)

However, a documented install can succeed while still creating the unwanted condition. The pre-change workflow asked for state transitions, repetition, persistence, invalid input, and related-feature interactions, but it did not explicitly require an inventory of files, executables, caches, downloads, selected versions, and command resolution before and after each material operation. Nor did it require a selective-disable test for each member of a multi-item capability. An auditor could therefore mark runtime installation `Verified` without noticing duplicated ownership or the all-or-nothing control. [updated `just-use-it` workflow](../../skills/just-use-it/SKILL.md) [programmatic branch](../../skills/just-use-it/references/programmatic-experience.md)

A strengthened audit would discover the #14507 class by combining four observations:

1. capture which relevant executables and versions resolve before the install;
2. inspect the created executables, lockfile entries, caches, and materialized storage afterward;
3. compare tool-managed state with pre-existing managers or installations; and
4. for a multi-member feature, try to disable one member while keeping another enabled at each documented configuration scope.

The result should be reported as an **operational or usability limitation** unless it contradicts a public promise. A missing fine-grained option is not automatically a functional bug.

## How Real Usage Exposed the Sampled Issues

| Project and issue | User workflow and necessary combination | Why a happy path or source-first review can miss it | Reusable exploration move |
| --- | --- | --- | --- |
| [pnpm #14507](https://github.com/pnpm/pnpm/issues/14507) | Existing external runtime manager + a project declaring multiple managed runtimes + `pnpm install`; the user inspected the additional runtime and wanted to disable only one member. | Installation behaves as designed, so exit status and the primary promise both pass. The problem is ownership, storage, version selection, and control granularity. | Diff the operational footprint; compare with pre-existing tools; test selective enable/disable for members of a composite feature. |
| [Vite+ #2254](https://github.com/voidzero-dev/vite-plus/issues/2254) | Scaffold a library into a non-empty Git worktree with `--directory . --no-git`; compare interactive and non-interactive modes and compare the library and monorepo templates. | A fresh empty directory succeeds. One mode showed only a generic failure, another exited `0` without scaffolding, and a sibling template worked in the same directory. | Vary initial directory state; compare sibling implementations; verify promised artifacts as well as message and exit code; compare interactive and unattended operation. |
| [Vite+ #2250](https://github.com/voidzero-dev/vite-plus/issues/2250) | Invoke a wrapped build command with an argument separator and inspect what reaches the underlying config; the global and project-local wrappers consumed different numbers of separators. | Normal flags work and the build wrapper starts. The failure sits at a boundary between command layers and appears only with passthrough arguments. | At every wrapper or adapter boundary, send sentinel arguments, environment values, stdin, stdout/stderr, signals, and exit status through the full stack and compare with the direct tool. |
| [Vite+ #2234](https://github.com/voidzero-dev/vite-plus/issues/2234) | Run a normally fast command in a real TTY while the configured registry responds slowly; repeat five times and inspect whether the update-check cache appears. | Fast networks and non-interactive test runners skip the condition. A single timed run does not reveal that the missing cache repeats the cost. | Exercise healthy, slow, failed, and offline dependencies where safe; measure cold, warm, and repeated runs; inspect the state intended to amortize the work. |
| [Oxc #20067](https://github.com/oxc-project/oxc/issues/20067) | Extend a shared Oxlint config, override one inherited rule locally, and lint a file to which the inherited override applies. | A single config and a non-conflicting rule both pass. The failure requires precedence, inheritance, and file-selection behavior to interact, despite documentation saying later configurations override earlier ones. [Oxc configuration reference](https://oxc.rs/docs/guide/usage/linter/config-file-reference.html#extends) | For layered configuration, construct conflicting values and verify precedence across global, project, nested, override, environment, and CLI scopes using observable behavior. |
| [Oxc VS Code #185](https://github.com/oxc-project/oxc-vscode/issues/185) | Compare working CLI formatting with the editor extension, then vary single-folder versus multi-root workspaces and restart the editor repeatedly. The reporter retained an intermittent observation even without a stable reproduction. | CLI success does not verify the editor surface; startup logs can look healthy while the command remains unavailable; a one-session check can pass by chance. | Test every shipped interface separately; exercise restart and workspace-topology transitions; record attempt-by-attempt intermittent results instead of discarding them. |
| [Rolldown #10675](https://github.com/rolldown/rolldown/issues/10675) | Build a medium-to-large lazy-loaded SPA, change only the Rolldown version, and inspect the initial static import closure in the manifest or browser network panel. | Small fixtures and total byte size can remain acceptable while request count and cold-start behavior regress. Source review does not supply the user's real graph or scale. | Include a realistic-scale specimen; compare structural artifacts and runtime delivery, not only success and total size; use one-variable A/B version comparisons. |
| [Rolldown #10403](https://github.com/rolldown/rolldown/issues/10403) | Call an experimental resolver hook programmatically for a dual-format package, varying the per-call import kind and comparing it with the equivalent static option. | Ordinary CLI bundling and one export condition succeed. The fault appears only through a public library hook and an option crossing the JavaScript/native boundary. | Exercise equivalent capabilities through every public entrypoint; use discriminating inputs whose expected outputs differ so silently dropped options are visible. |
| [Bun #40077](https://github.com/oven-sh/bun/issues/40077) | Migrate roughly 1,600 tests across 15 applications from Vitest to `bun:test`; the real corpus exercised live DOM snapshots, builtin-module test doubles, monorepo watch boundaries, and native-binding promise rejections. | Small examples of each API work, but the migration supplied object shapes, filesystem topology, long-running behavior, and native integrations that isolated smoke tests did not. | Use an existing workload or conformance suite as an incremental migration oracle; preserve each divergence, then minimize it without replacing the original evidence. |
| [Playwright #30319](https://github.com/microsoft/playwright/issues/30319) | Run all tests in UI mode, wait after completion, and observe results disappear about a second later. | Inspection at the moment the operation completes passes. The broken state occurs only after the transition settles. | Observe after completion, idle, navigation, reload, and restart; define how long results and selections should persist. |
| [Playwright #42263](https://github.com/microsoft/playwright/issues/42263) | Open trace-viewer detail sections and try to focus and toggle controls with Tab, Enter, and Space. | Mouse use succeeds and the controls are announced as buttons, so a visual or click-only tour appears correct. | Exercise keyboard traversal, focus visibility, activation, and recovery for every interactive control family. |
| [VS Code #327048](https://github.com/microsoft/vscode/issues/327048) | Populate a chat working set, open several editor groups, then drag a sash and compare populated/unpopulated state and stable/insiders builds. | A clean window and a simple layout remain smooth. The regression requires accumulated UI state plus a high-frequency interaction. | Build representative accumulated state; exercise continuous interactions; compare empty and populated states and one-variable version baselines. |

## Sample Boundary and Saturation

The sample is purposive and bounded at twelve public reports across seven developer-tool project families. It starts with the user-provided pnpm report, covers the requested Vite+, Oxc, and Rolldown repositories, adds Bun for runtime and test-runner migration behavior, and uses Playwright and VS Code only to cover interactive UI, accessibility, post-completion state, and accumulated-state performance.

Included reports had a concrete user action path and an observable outcome. The sample excludes source-only suspicions, implementation proposals without usage evidence, private reports that cannot be inspected, and additional reports whose encounter mechanism merely repeats one already represented. Issue-body root-cause claims were not treated as established facts.

Sampling stopped when adding Bun supplied the last materially new mechanism: using a real compatibility migration as an oracle. Further candidates inspected during the search reduced to already represented families: configuration composition, lifecycle repetition and invalidation, mode parity, boundary fidelity, artifact inspection, degraded dependencies, realistic scale, or alternative interaction. This is qualitative mechanism saturation, not evidence that all bug classes are covered.

## Reusable Check Families

These are generic behavioral heuristics. An audit should select the families that fit the capability rather than exhaustively multiplying every combination.

### 1. Observable footprint and ownership

Before and after a material action, inspect applicable files, generated executables, lockfiles, caches, processes, listeners, network fetches, persistent configuration, command resolution, selected versions, disk usage, and externally created resources. Ask whether the tool duplicates, shadows, mutates, or takes ownership from something already present.

This is the main missing family for pnpm #14507. It also turns cleanup from a final chore into evidence about the product's behavior.

### 2. Configuration composition and control granularity

Do not test settings only in isolation. Use conflicting sentinel values to establish precedence and scope, and exercise combinations such as base + local override, root + nested config, config + environment + CLI, and two independently configurable members. For a feature that accepts a list or map, try enabling or disabling one member without changing the rest.

Use pairwise, behavior-informed combinations rather than a Cartesian product. The purpose is to test seams and user decisions, not generate an arbitrary option matrix.

### 3. Lifecycle and temporal states

Observe first use, second use, repeated use, completion, post-completion idle, restart, reload, recovery, and cleanup. Record both cold and warm timing when a feature claims or visibly uses caching. A successful instantaneous snapshot does not verify persistence or eventual behavior.

### 4. Interface and mode parity

Treat CLI, library API, editor extension, browser UI, non-interactive mode, watch mode, development mode, and production build as separate user surfaces. When two surfaces claim the same capability, feed them the same discriminating input and compare observable results; success in one surface cannot verify another.

### 5. Boundary fidelity

For wrappers, plugins, adapters, subprocesses, and native bindings, verify that arguments, option discriminants, environment, input streams, output streams, exit status, signals, and cancellation semantics survive the boundary. Choose sentinels that produce observably different outputs when preserved versus dropped.

### 6. Artifact and outcome integrity

Never equate exit `0` with success. Check that expected files exist, unwanted files do not, generated content is executable or consumable, dependency graphs and manifests have the intended shape, and a real downstream consumer can use the result. For UI work, inspect the settled rendered state rather than only structure or logs.

### 7. Realistic scale and degraded surroundings

After a minimal example, add one representative specimen with realistic file count, graph depth, workspace topology, accumulated UI state, or task count. Where safe, vary external conditions such as latency, offline behavior, unavailable services, and constrained resources. Keep one variable fixed at a time so the observation remains reproducible.

### 8. Alternative interaction and accessibility

For interactive products, use keyboard-only navigation in addition to pointing input, inspect focus and disabled states, resize relevant viewports, and verify that error and recovery paths remain operable. Accessibility exposes behavioral failures that a click-only visual tour cannot.

### 9. Counterfactual comparison

When behavior feels wrong but no explicit promise exists, compare a single changed dimension: previous/current version, direct/wrapped invocation, empty/populated state, first/repeat run, one template/another, or one interface/another. This turns vague friction into a reproducible observation without requiring root-cause analysis.

### 10. Compatibility migration

When a tool replaces or claims compatibility with another tool, run a representative existing workload incrementally under both and preserve behavior differences before minimizing them. The original workload remains evidence even after a smaller reproduction is available.

## What Should Not Become a Skill Checklist

The following are product-specific symptoms, not reusable rules:

- looking specifically for `node_modules/.bin/node`;
- always trying three `--` separators;
- always delaying an npm registry by two seconds;
- hard-coding CJS/ESM condition names; or
- expecting every build to minimize chunk count.

The reusable layer is instead: inspect created executables and ownership, verify wrapper passthrough, degrade optional network work, vary a discriminating option across a boundary, and compare artifact structure at realistic scale. Product-specific issue symptoms should remain examples or post-audit leads, not required actions for unrelated tools.

## Gaps Found in the Pre-change `just-use-it` Skill

The existing workflow already covers documentation-first use, free exploration, source-last reconciliation, repetition, persistence, invalid-input recovery, related-capability interactions, visual states, and intermittent findings. The issue sample identifies five material gaps:

1. **No operation-level footprint ledger.** The target-checkout integrity baseline protects the repository, but it does not require auditing what the product intentionally creates elsewhere.
2. **No explicit configuration-seam method.** “Meaningful variations” is too broad to guarantee precedence, scope, selective-disable, and wrapper-boundary checks.
3. **No outcome triangle.** A capability could look successful from messages or exit code without explicit verification of artifacts and downstream consumption.
4. **No realistic-scale or degraded-environment pass.** Minimal consumers are useful for isolation but miss graph-, latency-, topology-, and accumulated-state failures.
5. **No explicit usability or operational-friction finding class.** #14507 can be important without violating a documented contract; forcing it into “bug” or discarding it both misrepresent the evidence.

A conditional exploration reference would be a better fit than expanding the core workflow with repository-specific examples. It should build a small, capability-shaped check plan from the generic families above and record why each selected variation is relevant.

The follow-up update implements that recommendation in [`exploration-lenses.md`](../../skills/just-use-it/references/exploration-lenses.md) and adds the evidence-bounded Capability Gap category in [`finding-packets.md`](../../skills/just-use-it/references/finding-packets.md).

## How Issue Archaeology Should Interact with Usage-First Order

Cross-project issue research is useful for distilling generic exploration families before an audit. Reading the **target project's** known issues before hands-on use is different: it biases the auditor toward known symptoms and can make issue reproduction look like independent discovery.

To preserve the intended order:

1. use generic cross-project heuristics during documentation-first and free exploration;
2. keep the target implementation and target issue tracker closed during those passes;
3. reconcile public source entrypoints afterward; and
4. optionally consult the target issue tracker only as a final coverage calibration or duplicate check, clearly labeling known-issue reproduction separately from independently observed findings.

This preserves the value of human-like use while still allowing the repository's issue history to improve future audits.

## Limitations

- This is a purposive sample, not a statistical survey of issue trackers.
- The twelve-report boundary reflects discovery-mechanism saturation for this design question, not repository or feature coverage.
- Issue bodies document reporter observations; they do not by themselves prove the reporter's proposed cause or remedy. This note intentionally relies only on the action paths and observable results.
- Several reports concern evolving or experimental releases. Their value here is the discovery pattern, not a claim that the current release still contains the behavior.
- pnpm #14507 is a feature request. The note treats its user friction as discoverable evidence without relabeling it as a bug.
