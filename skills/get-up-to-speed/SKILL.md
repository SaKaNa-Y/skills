---
name: get-up-to-speed
description: Get familiar with a library, framework, or developer tool through official-documentation preparation, topic-by-topic demonstrations, and a retained teaching workspace.
disable-model-invocation: true
---

# Get Up to Speed

Teach the purpose, core concepts, and common capabilities of one library, framework, or developer tool. Prepare from official documentation, then connect explanations to examples the agent demonstrates. The learner follows along and may ask questions; learner code changes, predictions, exercises, and assessments are never prerequisites for progress.

One invocation supports a conversation with multiple **Teaching Segments**, each covering a coherent topic. Retain the examples and explanations in an independent **Quickstart Workspace** for later use. Keep the scope to a practical introduction rather than exhaustive API coverage or a recurring curriculum.

## 1. Establish the Learning Context

Identify the target and the learner's intended use from the request and available context. Use a brief official overview to distinguish materially different paths when the target is a suite or offers several roles. If the intended path remains ambiguous, explain the relevant choices and let the learner select one before preparing detailed lessons. Use any stated experience to calibrate explanations; avoid an intake questionnaire or prerequisite quiz.

Establish the **Teaching Language** before teaching. Honor a language explicitly selected for this quickstart; otherwise ask the learner to choose. Use that choice for conversational explanations and saved teaching material, keeping code identifiers, commands, and API names in their conventional form. The conversation's language alone is not a selection.

**Complete when:** the target, intended usage path, and learner-selected Teaching Language are known.

## 2. Prepare from Official Documentation

Read the official overview, getting-started guide, and guides for the selected path before composing the teaching outline. Consult API references for the examples being prepared. Align the documentation with the requested or installed version; for a fresh workspace, identify a current documented release and record the version actually used.

Build a compact outline around useful outcomes and the concepts needed to understand them. Give a brief map of the target's purpose and main capabilities, then select common usage for demonstration. Explain where the chosen path fits and which advanced or alternate paths sit outside this introduction. Read enough to support this outline, then deepen the relevant documentation as each segment is prepared; do not turn preparation into a whole-project audit.

Organize for understanding rather than copying the documentation's table of contents. Introduce concepts beside the example that needs them. Keep version-sensitive claims traceable to the corresponding official pages. If required documentation is unavailable or contradictory, state the specific gap and narrow the claims; a remembered API is not verified documentation.

**Complete when:** a bounded topic outline, its official sources, and the version basis are ready, and the first segment has enough documentation to support its explanation and example.

## 3. Create the Quickstart Workspace

Use the learner's requested destination, or create a fresh, clearly named directory such as `get-up-to-speed-<target>` under the current workspace. Preserve existing contents by choosing an unused directory when needed. Keep demonstrations and dependencies inside this teaching project rather than modifying the library checkout or integrating into an existing application.

Use a small structure that suits the target:

- `README.md`: target and version basis, usage path, topic outline, links to delivered segments, and commands for running the examples.
- `lessons/`: explanations for delivered Teaching Segments in the selected language, with corresponding source links and example paths.
- `examples/`: demonstration code and any local fixtures; place package manifests and configuration where the target's tooling expects them.

Prepare the outline up front and add segment material as it is taught. Preserve earlier examples in a runnable form or record a reproducible command for each stage, so later edits do not invalidate earlier explanations. Record the resolved dependencies using the ecosystem's normal manifest and lockfile conventions.

**Complete when:** the independent directory and first example's prerequisites are ready, and its README identifies what is being taught and how the material is organized.

## 4. Demonstrate One Segment at a Time

Use this rhythm for each Teaching Segment:

1. **Purpose and effect.** Introduce the practical use and show or describe the result the example will produce. Connect it to the previous topic when useful.
2. **Necessary concept.** Explain the idea needed to understand this example and point to the relevant official documentation. Avoid front-loading concepts the learner has no use for yet.
3. **Demonstration.** Write and run the example yourself, explaining each material command, configuration choice, or code change. Adapt setup details to the selected usage path instead of presenting unexplained boilerplate.
4. **Result and reason.** Show the observable output, generated artifact, or rendered UI, and connect it back to the code. When a small agent-performed variation clarifies behavior, demonstrate it and explain what changed. Distinguish observed results from expected behavior; if execution is unavailable, label the example as a documentation-based walkthrough and explain the limitation.
5. **Takeaway and pause.** Summarize what this capability is useful for and one material caveat when relevant. Save the explanation and example references, preview the next topic, and wait for the learner's questions or direction to continue.

Use the actual rendered interface for UI demonstrations when available, and command output or generated artifacts for programmatic tools. Keep operational work within the teaching workspace; service provisioning or changes to the learner's existing projects require their own authorization.

Answer follow-up questions in the current segment, revisiting its example when helpful. A request for clarification does not advance the topic. Continue after the learner directs it; do not deliver the remaining course merely because the examples are already prepared.

**Complete when:** the current topic's explanation and example are saved, its actual or expected result is honestly identified, and the learner has directed the next step. After the final topic, proceed to the wrap-up without requiring a ceremonial extra confirmation.

## 5. Wrap Up and Retain

Once the scoped topics have been delivered or explicitly skipped by the learner, add a compact recap and common-command or API quick reference to the README. Include the official pages to consult next, example run instructions, and any skipped topics or unexecuted examples. Describe what was covered without claiming the learner has demonstrated mastery.

Return links to the workspace and its entry document. Retain the teaching files and stop only temporary processes created for this quickstart, noting any process intentionally left running for the learner. If the learner ends early, preserve the delivered material and identify the next topic without generating a long-term learning record or scheduling another session.

**Complete when:** the learner can revisit the delivered explanations and examples, the coverage and execution limits are clear, and temporary process ownership is accounted for.
