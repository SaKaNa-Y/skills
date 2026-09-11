# Programmatic Experience

Read this reference when the target has no interactive UI or when its UI leaves part of the Capability Surface accessible only through a CLI or public API. Programmatic use cannot verify an interactive UI; that branch requires its own real user-control surface or a Blocked state.

## Create a Disposable Consumer

Create a uniquely named temporary workspace outside the target checkout, using the platform's safe temporary-directory mechanism. Record its exact resolved path before adding files. Install, link, or invoke the target as its public documentation instructs.

Use the smallest real consumer that can exercise the public contract:

- invoke a CLI through its documented executable and help surface;
- import a library from a minimal program using its supported package entrypoint; or
- use an official example only when it represents a supported user path.

For a checkout audit, follow its documented build and consumer setup in a disposable copy or worktree when practical. Inspect build and launch metadata without reading behavioral implementation.

Confirm where the consumer resolves the tool or package; a global launcher, link, or stale build can select a different artifact despite a matching version label. Use the minimum evidence sufficient to establish which artifact actually runs and its correspondence to the selected target.

Keep the original checkout's tracked files unchanged and preserve existing authorization boundaries for dependency installation, network access, credentials, or external state.

Before the first launch, capture a cheap integrity baseline for the target: repository status and diff for a Git checkout, or a file inventory and content hashes for a small non-Git target. Compare the same scope after cleanup. Keep the baseline proportional; do not hash dependency caches or large generated trees merely for ceremony.

## Experience Before Inspecting

During the documentation and free-exploration passes, use public commands, types, runtime feedback, and help output without reading behavioral implementation source. Create disposable programs and data freely inside the recorded workspace. Capture commands, inputs, outputs, versions, and relevant environment facts needed to understand a result.

Exercise the documented path first. Then vary inputs, repeat operations, combine related public capabilities, inspect persistence, and attempt recovery according to the behavior the tool exposes. Keep generated harnesses as audit state, not as changes to the target project.

The main workflow owns source reconciliation and cleanup. Preserve required evidence before it removes the temporary consumer.

**Complete when:** every non-UI public capability in the current surface has a terminal state and the target checkout's tracked files remain unchanged.
