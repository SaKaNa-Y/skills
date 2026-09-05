---
name: get-up-to-speed
description: Get familiar with a library, framework, or developer tool through documentation-first preparation, targeted source reading, and topic-by-topic demonstrations in a retained teaching workspace.
disable-model-invocation: true
---

# Get Up to Speed

Teach the purpose, core concepts, and common capabilities of one library, framework, or developer tool. Prepare from official documentation and relevant source, then connect explanations to examples the agent demonstrates. The learner follows along and may ask questions; learner code changes, predictions, exercises, and assessments are never prerequisites for progress.

One invocation supports a conversation with multiple **Teaching Segments**, each covering a coherent topic. Retain the examples and explanations in an independent **Quickstart Workspace** for later use. Keep the scope to a practical introduction rather than exhaustive API coverage or a recurring curriculum.

## 1. Establish the Learning Context

Identify the target and the learner's intended use from the request and available context. Use a brief official overview to distinguish materially different paths when the target is a suite or offers several roles. If the intended path remains ambiguous, explain the relevant choices and let the learner select one before preparing detailed lessons. Use any stated experience to calibrate explanations; avoid an intake questionnaire or prerequisite quiz.

Establish the **Teaching Language** before teaching. Honor a language explicitly selected for this quickstart; otherwise ask the learner to choose. Use that choice for conversational explanations and saved teaching material, keeping code identifiers, commands, and API names in their conventional form. The conversation's language alone is not a selection.

**Complete when:** the target, intended usage path, and learner-selected Teaching Language are known.

## 2. Prepare from Documentation and Source

Read the official overview, getting-started guide, and guides for the selected path before composing the teaching outline. Consult API references for the examples being prepared. Select the version to teach from the request or relevant installation; for a fresh workspace, choose a current documented release. Match the documentation to that version and verify the actual installation in step 3.

Build a compact outline around useful outcomes and the concepts needed to understand them. Give a brief map of the target's purpose and main capabilities, then select common usage for demonstration. Explain where the chosen path fits and which advanced or alternate paths sit outside this introduction.

Follow the documentation with **Source Preparation** in every quickstart, even when the docs appear sufficient:

- Locate source matching the selected release through a tag, commit, or corresponding published source, and record the version relationship. Unmatched source can guide investigation but cannot substantiate claims about the selected version.
- Orient within the relevant repository packages, public entrypoints, type definitions, official examples, and tests. Select the parts serving the teaching outline rather than surveying every package or file.
- Identify the concrete behaviors each segment needs to explain. Trace the relevant implementation to answer questions about configuration defaults and precedence, key calls, or restrictions affecting the example. Keep the supporting documentation and versioned code locations with the answers for use in the lesson.
- Distinguish supported public usage from implementation behavior at the inspected revision. Use tests to clarify cases the project covers and actual runs to check observable results; neither makes an internal interface a supported API.

Orient in the repository and prepare the first segment before teaching begins; prepare later segments as the conversation reaches them. Stop reading once the behaviors needed for the segment have supported explanations and material usage limits are accounted for. Leave unrelated subsystems outside this scope.

If evidence is missing or contradictory, withhold the affected claim and explain the limit. Missing matching source permits a clearly labeled documentation-only preparation for claims the official documentation supports. If a gap prevents the topic's stated outcome, pause that topic and let the learner choose a supported alternative or defer it. Merely recording an unresolved question does not make its answer ready to teach.

**Complete when:** the outline and version basis are known, repository orientation and the first segment's targeted reading are complete or have explicit source-access limits, and every planned behavioral explanation has supporting evidence. Later segments remain planned rather than implicitly prepared.

## 3. Create the Quickstart Workspace

Use the learner's requested destination, or create a fresh, clearly named directory such as `get-up-to-speed-<target>` under the current workspace. Preserve existing contents by choosing an unused directory when needed. Keep demonstrations and dependencies inside this teaching project rather than modifying the library checkout or integrating into an existing application.

Use a small structure that suits the target:

- `README.md`: target and version basis, including the inspected source revision or its availability limit, usage path, topic outline, links to delivered segments, and commands for running the examples.
- `lessons/`: explanations for delivered Teaching Segments in the selected language, with official documentation links, relevant code references for implementation-derived explanations, and example paths.
- `examples/`: demonstration code and any local fixtures; place package manifests and configuration where the target's tooling expects them.

Add segment material as it is taught. Preserve the code and dependencies needed to reproduce earlier examples, using separate examples or reproducible snapshots when later changes would invalidate them; retaining only an old command is insufficient. Record resolved dependencies using the ecosystem's normal manifest and lockfile conventions. Verify that the installed version matches the preparation; if it differs, align the installation or revisit the affected documentation and source before teaching.

When the environment cannot run an example, record the missing prerequisite and prepare an unexecuted walkthrough with expected output. Keep this execution limit separate from source access: an unexecuted example may still have been checked against matching source. If the walkthrough cannot serve the topic's outcome, use the topic pause described in step 2.

**Complete when:** the directory and README are ready, and the first example either has a version-matched runnable environment or an explicitly limited walkthrough that can support the topic.

## 4. Demonstrate One Segment at a Time

Repeat this section for the next planned topic after the learner directs continuation. Complete that topic's Source Preparation using step 2. When a run disagrees with the preparation, check the version and relevant behavior, then correct the explanation or use the topic pause; preserve the target project itself.

Use this rhythm for each Teaching Segment:

1. **Purpose and effect.** Introduce the practical use and show or describe the result the example will produce. Connect it to the previous topic when useful.
2. **Necessary concept.** Explain the idea needed to understand this example and point to the relevant official documentation. Introduce implementation detail only when it helps the learner understand or use this capability.
3. **Demonstration.** Demonstrate the code and run it yourself when execution is available, explaining each material command, configuration choice, or code change. Connect setup details to the selected usage path.
4. **Result and reason.** Show the observable output, generated artifact, or rendered UI, and connect it back to the code. When a small agent-performed variation clarifies behavior, demonstrate it and explain what changed. Label results from an unexecuted walkthrough as expected rather than observed.
5. **Takeaway.** Summarize what this capability is useful for and one material caveat when relevant. Save and link the explanation and example. If topics remain, preview the next one and wait for the learner's direction; otherwise proceed to the wrap-up.

Use the actual rendered interface for UI demonstrations when available, and command output or generated artifacts for programmatic tools. Keep operational work within the teaching workspace; service provisioning or changes to the learner's existing projects require their own authorization.

Answer clarification questions within the current segment, revisiting its example as needed. Advance only when the learner directs continuation; prepared material alone is not a reason to move on.

**Complete when:** every scoped topic has been delivered with saved explanations and examples or explicitly skipped by the learner, or the learner ends the quickstart early. Between topics, remain in this section; a completed segment alone does not start the wrap-up.

## 5. Wrap Up and Retain

On completion or a learner-requested early finish, add a compact recap and common-command or API quick reference for the delivered material to the README. Include the official pages to consult next, example run instructions, and any remaining or skipped topics and unexecuted examples. Describe what was covered without claiming the learner has demonstrated mastery.

Return links to the workspace and its entry document. Retain the teaching files and stop only temporary processes created for this quickstart, noting any process intentionally left running for the learner. For an early finish, identify the next topic; the retained material is sufficient without a long-term learning record or scheduled session.

**Complete when:** the learner can revisit the delivered explanations and examples, the coverage and execution limits are clear, and temporary process ownership is accounted for.
