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
- exact public action path and the material input or state needed to replay it;
- expected and observed behavior;
- reproduction attempts and whether the result is stable or intermittent;
- available screenshot, output, log, viewport, or documentation location; and
- material unknowns, stated without guessing.

For documentation Findings, identify the exact public instruction or claim. For visual Findings, include the rendered state and viewport. For Capability Gaps, identify the independently useful behaviors that cannot coexist and the smallest missing control or composition boundary, without designing the solution. Keep secrets and unrelated personal data out of the packet.

Preserve the failing specimen or an exact creation command when retyping a sample could change the observation. Keep material whitespace, encoding, argument boundaries, and pre-existing state explicit when relevant; a displayed code block or a path to soon-deleted temporary data may not preserve them. Retain the necessary input with the packet before cleanup. Ordinary findings need only the representation sufficient to replay their behavior.

Describe the condition actually observed, distinguishing it from an inferred trigger. Record which dimensions changed in a comparison and leave untested conditions unknown.

Describe concrete user impact. Assign severity or priority only when the project supplies the applicable scale and enough evidence supports the classification.

## Hand Off Without Publishing

At the next coherent feature-group boundary, make completed packets available to the user. When `$yak-shaving-triage` is separately active, hand them off as pending while the hands-on and source-reconciliation work keeps target tracker history closed. Receiving a packet does not open the Audit Reconciliation Gate.

After the source-confirmed public surface is accounted for and the independently observed packets are frozen, declare the gate open so Yak Shaving Triage can reconcile the batch. An explicitly concluded Partial Audit also freezes its completed packets and opens the gate. Opening the gate without reading the tracker preserves behavioral blindness; once tracker history is read, label the remaining current audit work and any later resume tracker-informed. When Yak Shaving Triage is not active, retain the packets in the final audit report.

Just Use It performs no Issue Reconciliation or tracker mutation. It immediately returns to the remaining Capability Surface after an ordinary packet handoff and may include Reused record links or identifiers returned by the recording workflow in its final report.

**Complete when:** another agent can reproduce or responsibly retry the observation from the packet, the uncertainty is explicit, and the packet is retained in the audit or handed off with an explicit pending or gate-open state.
