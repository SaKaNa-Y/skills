---
name: explore-new-capabilities
description: Discover and discuss new capabilities for a project, one evidence-grounded idea at a time, with persistent exploration history.
disable-model-invocation: true
---

# Explore New Capabilities

Find capabilities that could create value for a project's users, then refine one idea at a time through discussion. A Feature Opportunity can be a small convenience or a substantial direction. It needs a concrete scenario and a plausible implementation path, while demand, scope, and feasibility may remain unsettled.

This explicitly invoked workflow serves contributors, maintainers, and product developers. It works without a supplied feature idea. Discovery is the agent's responsibility; the user owns priorities, trade-offs, and whether to pursue an opportunity. Work ends at discussion, bounded evidence gathering, and exploration records. Product implementation and external publication require a further instruction.

## 1. Establish the project and history

Read the project's guidance, purpose, public capabilities, and relevant source. Use the user's direction, role, and available effort when supplied; ask only for missing context that would change the exploration. Establish enough grounding to identify concrete user outcomes without requiring a whole-project audit.

Use a records directory the user has already created and supplied. Reuse an established path; if it is missing, inaccessible, or not a directory, ask for a valid existing directory. Leave its creation to the user. Project reading can continue while the path is pending, but presenting a new opportunity waits until its history can be read and its record saved. Keep records at this location without changing repository ignore rules or publishing them.

Identify the project in the history using its repository identity or another unambiguous identifier. Reuse its existing record layout. For a new history, use a project-specific index linking one Markdown file per presented opportunity, with short summaries and current outcomes. Create these files inside the supplied directory. Read the index and relevant earlier records before discovery, including deferred and dismissed ideas.

**Ready when:** the project, relevant constraints, and existing exploration history are understood, and the record location is usable.

## 2. Find and ground an opportunity

Look for outcomes users cannot yet achieve conveniently, useful combinations of existing capabilities, and ideas from other tools or domains. Follow relevant clues into comparable projects, complementary tools, and user-assembled workflows. Explain which part of an outside idea transfers and what must change for this project. Another product having a feature is inspiration, not evidence that this project's users need it.

Favor opportunities that fit the project's purpose, while allowing a compelling broader direction if its changed assumptions and maintenance burden are explicit. Consider small and large ideas on their merits rather than favoring novelty or size. The agent may compare several leads internally; choose one for discussion instead of presenting a candidate list.

Before presenting that opportunity, establish:

- **Value:** a concrete user situation and the additional outcome the capability could enable. Separate observed needs from hypothesized benefits.
- **Feasibility:** traceable evidence in the target project's interfaces, data, architecture, or demonstrated behavior supporting a plausible implementation path. Check the assumptions required to transfer an outside example.
- **Prior work:** whether existing capabilities already satisfy the scenario, and whether exploration records or relevant project issues, PRs, and discussions already cover it. Include closed or rejected work when relevant, and retain its reasoning.

Judge repeated ideas by the user problem and intended capability, not their titles. A scenario already satisfied by shipped capabilities, or an unchanged idea already covered by prior work, sends discovery to another lead. Reopen an earlier idea when the user asks or material evidence or conditions have changed; link the earlier work and explain the change. If a source cannot be checked, state the resulting uncertainty and avoid claims of novelty.

Investigate facts that could change the opportunity's viability. Start with documentation, source, and actual usage; use a small disposable check when it can resolve a consequential uncertainty. Keep checks isolated from product changes and clean up resources created for them. Distinguish source inference from observed execution, and record failed checks as well as successful ones. Costly prototypes can remain proposed next steps.

**Ready when:** one opportunity has a concrete scenario, a supported plausible path, and an account of prior work and remaining uncertainty. If relevant leads yield no such opportunity, report the examined scope and evidence limits instead of filling the gap with an unsupported idea. Do not keep widening the search merely to produce a result.

## 3. Present one idea and discuss it

Save the initial record when first presenting the idea. Explain what users could do, why it is worth discussing now, why it appears feasible, and what remains uncertain. Cite the supporting sources and explain why this opportunity was selected. Keep the initial proposal understandable without treating it as a settled specification.

Invite the user's reaction, then follow the questions it opens. Investigate factual uncertainties yourself; ask the user about goals and trade-offs with concrete alternatives and a recommendation when warranted. Use answers to revise the current idea, narrow or broaden its scope, or discard it. Ask dependent questions after their prerequisites are answered. Respect settled choices unless new evidence changes their basis.

Keep discussion on this opportunity. Related alternatives that solve the same user problem can clarify it; a distinct capability waits until the user chooses to explore another opportunity. Size does not determine identity: a large direction can still be one coherent idea.

The skill works independently. When the user also invokes a grilling skill, let it deepen the current opportunity's questions while this workflow owns discovery, evidence, and history. With `grill-with-docs`, resolved vocabulary and qualifying decisions follow that skill's documentation rules; exploration history still retains the idea's evidence and outcome. These are optional companions, installed separately.

**Complete when:** the user chooses to pursue, defer, or dismiss the idea, or ends the discussion. Retain unresolved questions without forcing a complete design.

## 4. Preserve the outcome and return control

Update the opportunity record at meaningful discussion boundaries and before closing. Keep a concise current account plus dated material changes, preserving why earlier judgments changed. Each record should let a later conversation recover:

- The project identity, idea, user scenario, and intended capability.
- Inspiration and evidence, with source links or code references, checked revisions or dates where useful, and what each source actually establishes.
- Prior related work and the scope or limitations of duplicate checks.
- Open assumptions, feasibility limits, and results of any disposable checks.
- The discussion's current state, decisions and reasons, and conditions for reconsideration.

Keep the index consistent with the record. An unfinished discussion remains unfinished; silence does not select a disposition. If saving fails, retain the update in the conversation, report the failure, and resolve persistence before presenting another idea. These records preserve exploration, not formal feature specifications or tracker items; follow the project's conventions when the user later requests those artifacts.

Close with the current conclusion, unresolved evidence, and record location. Let the user decide whether to continue this idea, explore another, or stop. Choosing to pursue an idea does not itself start implementation.
