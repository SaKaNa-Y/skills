# Missing Prerequisites

Read this reference when launch or build fails, inputs are missing, artifact correspondence is unknown, or documented use needs an unavailable prerequisite.

## Verify the Requirement

Before proposing an installation:

- identify the exact capability that needs the prerequisite and the documented version constraint, if any;
- check whether a suitable version is already available using the project's documented command;
- check the public documentation for a supported prebuilt binary, package, browser experience, container, devcontainer, or other path that avoids changing the user's machine; and
- inspect only the installation or entrypoint metadata allowed by the source-closed safety check. Do not read behavioral implementation source early to infer how the product works.

Evaluate alternatives against the target established during framing. Build prerequisites matter for a selected checkout, while contributor tooling can be unnecessary for an explicit release or running instance. An available prebuilt artifact completes target coverage only when its correspondence is established; otherwise keep any comparison separately scoped and the requested target's missing coverage explicit.

## Recover the selected target

Classify the observed failure before selecting a fallback: missing source or generated input, unresolved dependency/link, incompatible existing tool, or unavailable runtime/system tool. Inspect the documented preparation path and its effects. Complete authorized, reversible preparation in the disposable environment, then retry the failed operation and establish the resulting artifact identity. A missing file in a temporary copy is a recovery lead, not proof that the target cannot be built.

If an alternative artifact can answer a specific preparation or comparison question, state that question before using it. Keep its observations separate; resume the selected target after recovery. If a proposed recovery requires new authority, external access or material resources beyond the established budget, prepare the concrete action and request only that missing decision. An unavailable measurement alone does not establish resource exhaustion; use another supported bound or present the specific unresolved resource requirement.

## Resolve installation authority

If installation is still required, reuse existing authorization for its exact scope. Complete authorized temporary or project-local setup. For installation beyond that authority, present one prerequisite checkpoint containing:

- the missing dependency, required version, and evidence that it is needed;
- the capabilities that cannot be exercised without it;
- the exact official installation method;
- whether the change is temporary, project-local, user-local, or system-wide;
- the expected download, time, disk use, permissions, and persistent machine changes; and
- the cleanup plan, including anything that would remain installed.

Among supported options that match the selected audit target, offer available choices in this order:

1. use an already installed compatible environment;
2. use an official prebuilt or browser-based path;
3. use a project-provided isolated environment such as a container or devcontainer;
4. install an approved temporary or project-local prerequisite; or
5. install an approved user-local or system-wide prerequisite.

Skill invocation does not authorize persistent machine-level changes. Preserve applicable permission checkpoints and use existing user authorization without asking again. A new installation decision must identify the exact option and its effects.

## Continue or Block

When the user approves an installation, verify the resulting version, record every temporary and persistent resource it creates, and continue from the documented path.

After a failed attempt, inspect its cause and continue the next supported, authorized recovery that can resolve it. Mark affected capabilities `Blocked` only when a specific authority, access, resource or user-decision barrier prevents progress. Record the failed operation, the evidence for that barrier, alternatives investigated and the concrete action needed to resume. Continue unaffected work. A Blocked status preserves unfinished target work; it does not complete the audit.

A missing prerequisite in the user's environment is not by itself an Audit Finding. Create a separate Documentation Finding when the public documentation omits a required prerequisite, states an incompatible version, or promises a setup path that cannot work as described.

Remove approved temporary or project-local prerequisites during cleanup. Do not uninstall a user-local or system-wide prerequisite unless that removal was also explicitly agreed; report it as persistent state instead.

**Complete when:** the prerequisite is satisfied and the selected target can be exercised. If progress requires an unavailable action or decision, return that concrete blocker and retain the target as unfinished.
