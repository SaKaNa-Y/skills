# Finding Packets

Read this reference as soon as actual use may have revealed a functional, documentation, visual, interaction, operational, availability, or Capability Gap problem.

## Confirm the Observation

Compare observable behavior with a public promise, a usable-path expectation, or a consistent visible state. Preserve a Finding when the result has practical impact and actual use supplies evidence. Keep subjective taste and source-only suspicion as notes rather than Findings.

Re-run the same path once when doing so is safe and cheap. A repeat observation is reproducible. An observation that does not recur consistently is an **Intermittent Finding**, not a discarded flake; record every attempt result and the state that may distinguish them.

A Blocked capability becomes a Finding when the product or its documentation creates the block. A limitation caused only by the available audit environment remains Blocked coverage with its reason.

A source-confirmed public capability missing from user documentation is a documentation-discoverability Finding when the shipped interface and project signals establish public intent. When public intent remains ambiguous, exercise the capability if safe and report the ambiguity without asserting a documentation defect.

A **Capability Gap** is a reproducible limitation found through a concrete user path where shipped capabilities cannot be combined, scoped, or controlled finely enough to reach a practical outcome. Record the blocked outcome and operational impact, and describe it as a gap or limitation. Call it a bug only when it contradicts a public promise or consistent product contract. A preference without an exercised path and concrete impact remains a note rather than a Finding.

Stop after a cheap confirmation. Root cause, repair design, and implementation belong to a later User Problem.

## Build the Packet

Keep one session-scoped Finding Packet for each independently understandable behavior:

- affected capability and user impact;
- environment, version, prerequisites, and initial state;
- exact public action path;
- expected and observed behavior;
- reproduction attempts and whether the result is stable or intermittent;
- available screenshot, output, log, viewport, or documentation location; and
- material unknowns, stated without guessing.

For documentation Findings, identify the exact public instruction or claim. For visual Findings, include the rendered state and viewport. For Capability Gaps, identify the independently useful behaviors that cannot coexist and the smallest missing control or composition boundary, without designing the solution. Keep secrets and unrelated personal data out of the packet.

Describe concrete user impact. Assign severity or priority only when the project supplies the applicable scale and enough evidence supports the classification.

## Hand Off Without Publishing

At the next coherent feature-group boundary, make completed packets available to the user. When `$yak-shaving-triage` is separately active, let it reconcile packets with the repository's Tracker Guidance and request Tracker Write Approval. When it is not active, retain the packets in the final audit report.

Just Use It performs no tracker mutation and immediately returns to the remaining Capability Surface after the checkpoint.

**Complete when:** another agent can reproduce or responsibly retry the observation from the packet, the uncertainty is explicit, and the audit has resumed without diagnosing or repairing it.
