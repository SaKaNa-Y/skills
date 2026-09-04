# Vite DevTools Reference Audit Suite

This maintainer-only Reference Audit Suite validates the general `just-use-it` contract through a real Vite DevTools experience. It is not part of the installed skill's runtime path: product names, controls, and fixtures stay here, while only rules that pass the Generalization Gate belong in the skill.

## Generalization Gate

Translate a suite failure into shared user outcomes, Capability Journeys, states, modes, or interaction boundaries before changing the skill. Keep a behavior in this suite when that translation would require Vite DevTools detection, Dock-specific traversal, integration names, or another target-specific branch. A second product may strengthen later evidence but is not required for a rule that is already target-independent.

## Target and Isolation

Use a source-accessible Vite DevTools checkout and its packaged-artifact production playground. Public starting material is in the target checkout at:

- `playgrounds/production/README.md` for `pnpm run setup`, `pnpm dev`, and `pnpm build`;
- `docs/oxc/index.md` for Config Inspector behavior;
- `docs/rolldown/index.md` for module analysis; and
- `docs/kit/commands.md` for Command Palette and theme commands.

Use an existing user-requested browser session first. Otherwise use disposable browser and playground state, record every created resource, and preserve the target checkout's tracked files. Keep behavioral implementation source closed until both hands-on slices and the parity probe finish.

This suite is bounded acceptance evidence, not a complete Vite DevTools audit. Capabilities outside the two slices remain `Not Exercised`, and the product-level result remains a Partial Audit.

## Slice 1: Inspect Oxc Configuration

User outcome: narrow the resolved rule set with meaningful criteria and inspect the configuration applied by an override.

1. Open Oxc Config Inspector and start a Verification Trace for the Rules capability.
2. Search for a rule fragment that produces a non-empty result, then use a rendered category, plugin, usage, or state filter to produce an observably different rule count or result set.
3. Combine two applicable filters and record their result. When the fixture exposes multiple configuration files, switch configuration and record the changed resolved summary. Visually inspect the configuration selector at rest, focused, expanded, and after selecting an option; use full-window evidence for its browser-native option menu and compare it with adjacent controls rather than inferring visual quality from a successful value change.
4. Perform a Surface Discovery Pass through the rule surface and Overrides. Scroll relevant containers, reveal nested content, and inspect one override's pattern, plugins, and rules.
5. Record the main journey, one-variable Discriminating Variation, observable results, and any fixture-dependent exclusion in the Verification Trace.

### Mode Parity Probe

Use the documented Command Palette keyboard path to select Light, then replay the search, filter, nested override, and result states. Select Dark and replay the same fixed inputs and states. Compare business results and the operability of the Dock, panel, inputs, selections, focus, expanded content, scrolled content, and overlays. Switching themes without replaying the journey does not complete this probe.

## Slice 2: Trace a Rolldown Module Dependency

User outcome: find modules through multiple representations and show the dependency path between two related modules.

1. Produce real build data through the packaged production playground, then open Rolldown Modules and start its Verification Trace.
2. Use fuzzy search and one file-type filter that produce observably different module sets.
3. Switch to Folder view, expand nested project directories, scroll beyond the initial viewport when the fixture provides enough modules, and select a concrete module.
4. Switch to Graph view and use the path selector with two modules that have a known dependency relationship. Inspect the candidate menu's semantic exposure and select an endpoint once by pointing input and once by keyboard input.
5. Record the dependency path as the user result and use a one-variable input change as the Discriminating Variation.

## Fixture Sufficiency

Create the smallest missing data through a documented public workflow in an isolated test project when doing so is safe. Mark the affected suite step `Blocked: fixture insufficient` when the fixture cannot provide multiple meaningful configurations, distinguishable filter results, nested or off-screen content, or two related modules without disproportionate mutation. An empty or equivalent result cannot substitute for a Discriminating Variation, and a Blocked suite step does not pass acceptance.

## Acceptance

The suite passes when:

- both Vertical Capability Slices have terminal capability states and complete Verification Traces;
- the Oxc journey has completed Light and Dark Mode Parity Probes;
- every material control used by a journey has rendered-state evidence for the states actually entered, including the Oxc configuration selector at rest, focused, expanded, and selected in both themes;
- every opened entry point, panel, selector, disclosure, and view is credited only for the outcome actually exercised;
- the Coverage Ledger names remaining Vite DevTools capabilities as `Not Exercised` and labels the product result a Partial Audit;
- observation is scoped to meaningful state changes and the changed rendered region, with full-surface checks at slice and mode boundaries; and
- tracked target files and disposable resources pass cleanup checks.

An agent traversal or coverage-claim failure fails this suite and must be corrected through a rule that passes the Generalization Gate before both slices are rerun. A Vite DevTools product problem instead becomes a Finding Packet; when Yak Shaving Triage is separately active, it may reconcile that packet without taking ownership of the audit or turning the product finding into a skill-contract failure.
