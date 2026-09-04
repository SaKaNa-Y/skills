# UI Experience

Read this reference when the target exposes any official interactive UI: a web application, local administration surface, playground, Storybook or component browser, interactive documentation, web demo, native developer application, IDE surface, or terminal UI. Static screenshots and marketing pages are not interactive UI.

## Use the Rendered Product

For a browser-reachable UI, use browser control. When the user explicitly opened and requested a browser or tab, use that existing session first; otherwise open the documented UI with an available browser-control capability. For a native, IDE, or terminal UI, use an available control surface that performs real user actions. Mark the affected UI capabilities Blocked when the environment provides no such control, and continue every unaffected branch.

Treat a user-provided browser session as user-owned state. Leave it open and preserve its cookies, storage, and unrelated tabs; close only disposable tabs or contexts created for the audit when cleanup requires it.

Operate through controls visible to a user: navigate, click, type, select, scroll, drag, move backward and forward, reload, and resize when those actions are relevant. Accessibility or document structure may locate visible controls, while the rendered view supplies the visual result. Console and network observations may support evidence.

Keep the UI path real. Count a capability as UI-verified only when the visible interface exercised it; script injection, hidden endpoint calls, and direct internal-state changes do not substitute for UI use.

## Inspect Meaningful States

After each meaningful transition, inspect the rendered result rather than relying only on text or structure. Check the states the feature actually exposes, including:

- initial, active, completed, empty, loading, error, disabled, and recovery states when present;
- clipping, overlap, overflow, alignment, visibility, and incorrect status presentation;
- return, reload, or restart persistence for stateful behavior;
- interactions with related features; and
- materially different viewport sizes when the UI claims or visibly attempts responsive behavior.

Preserve the viewport, visible state, action path, and screenshot or equivalent visual evidence for a visual Finding. A purely aesthetic preference is not a Finding unless it causes practical readability, discoverability, consistency, or operability harm, or violates an explicit contract.

## Preserve Coverage Boundaries

When the UI exposes only part of the Capability Surface, finish that part through its real user-control surface and use the programmatic branch for the remainder. An API result cannot verify its corresponding UI behavior.

Treat an unavailable required control surface, an unlaunchable UI, or missing safe test state as Blocked coverage. A documented UI launch that fails may also be a documentation or product Finding. Continue through every unaffected capability.

**Complete when:** every UI-exposed capability has a terminal state, every meaningful rendered state has been visually inspected, and no non-UI path has been counted as UI verification.
