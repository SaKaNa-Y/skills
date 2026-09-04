# Missing Prerequisites

Read this reference when documented use requires a runtime, compiler toolchain, SDK, system package, container runtime, or similar prerequisite that is not available.

## Verify the Requirement

Before proposing an installation:

- identify the exact capability that needs the prerequisite and the documented version constraint, if any;
- check whether a suitable version is already available using the project's documented command;
- check the public documentation for a supported prebuilt binary, package, browser experience, container, devcontainer, or other path that avoids changing the user's machine; and
- inspect only the installation or entrypoint metadata allowed by the source-closed safety check. Do not read behavioral implementation source early to infer how the product works.

Do not treat an optional toolchain as mandatory merely because maintainers use it for development. Prefer supported user-facing paths over contributor setup.

## Request Approval Before Installation

If installation is still required, pause that capability and present one prerequisite checkpoint containing:

- the missing dependency, required version, and evidence that it is needed;
- the capabilities that cannot be exercised without it;
- the exact official installation method;
- whether the change is temporary, project-local, user-local, or system-wide;
- the expected download, time, disk use, permissions, and persistent machine changes; and
- the cleanup plan, including anything that would remain installed.

Offer supported choices in this order when available:

1. use an already installed compatible environment;
2. use an official prebuilt or browser-based path;
3. use a project-provided isolated environment such as a container or devcontainer;
4. install an approved temporary or project-local prerequisite; or
5. install an approved user-local or system-wide prerequisite.

Invoking this skill does not authorize installation. Install only the exact option the user approves, and preserve every normal permission or authorization checkpoint. Do not silently choose a machine-level installation for convenience.

## Continue or Block

When the user approves an installation, verify the resulting version, record every temporary and persistent resource it creates, and continue from the documented path.

When the user declines, no supported installation path is available, or installation fails, mark only the affected capabilities `Blocked` and continue exercising unaffected capabilities. Record the missing prerequisite and the attempted or declined path in the Blocked reason.

A missing prerequisite in the user's environment is not by itself an Audit Finding. Create a separate Documentation Finding when the public documentation omits a required prerequisite, states an incompatible version, or promises a setup path that cannot work as described.

Remove approved temporary or project-local prerequisites during cleanup. Do not uninstall a user-local or system-wide prerequisite unless that removal was also explicitly agreed; report it as persistent state instead.

**Complete when:** the prerequisite is satisfied through a supported, approved path, or every affected capability has an explicit Blocked reason and unaffected coverage continues.
