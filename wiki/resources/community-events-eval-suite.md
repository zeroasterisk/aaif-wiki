---
type: resource
title: Community Events Eval Suite
description: Empirical evaluation suite using two-arm comparative execution and automated
  graders to benchmark agent skill routing and execution.
resource: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/evals/sync-front-door/graders/not_a_phase_skill.md
tags:
- evals
- benchmarking
- skills
- testing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:08:29.494725+00:00'
sources:
- id: evt-community-events-file-cc0e90fa8ff2-c75eeab5
  resource: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/evals/sync-front-door/graders/not_a_phase_skill.md
  author: Rahul Parundekar
  last_modified: '2026-09-19T15:40:28-07:00'
- id: evt-community-events-file-d8b637bc00e2-5c63f836
  resource: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/evals/sync-front-door/graders/skill_fires.md
  author: Rahul Parundekar
  last_modified: '2026-09-19T15:40:28-07:00'
---

# Overview
The Community Events Eval Suite provides automated benchmarking and behavioral grading for operational agent skills and orchestrator front doors within the Agentic AI Foundation[^evt-community-events-file-cc0e90fa8ff2-c75eeab5][^evt-community-events-file-d8b637bc00e2-5c63f836]. It verifies skill dispatch accuracy, gate adherence, and execution safety using trace assertions and comparative testing.

# Architecture / Specification
The evaluation framework executes test cases across comparative trials and evaluates trace logs against declarative rule graders[^evt-community-events-file-cc0e90fa8ff2-c75eeab5][^evt-community-events-file-d8b637bc00e2-5c63f836]:

- **Front-Door Dispatch Grader (`skill_fires.md`)**: Asserts that generalized whole-estate drift requests invoke the primary orchestrator (`aaif-sync`) rather than prematurely executing an isolated phase engine[^evt-community-events-file-d8b637bc00e2-5c63f836].
- **Isolation Grader (`not_a_phase_skill.md`)**: Verifies that individual phase skills (such as `aaif-sync-chapters`, `aaif-sync-organizers`, or `aaif-sync-slack`) do not trigger independently when given broad multi-phase prompts, preventing partial, uncoordinated pipeline executions[^evt-community-events-file-cc0e90fa8ff2-c75eeab5].
- **Trace Matching**: Employs regex and tool invocation pattern matching against execution traces to grade routing decisions deterministically[^evt-community-events-file-cc0e90fa8ff2-c75eeab5][^evt-community-events-file-d8b637bc00e2-5c63f836].

[^evt-community-events-file-cc0e90fa8ff2-c75eeab5]: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/evals/sync-front-door/graders/not_a_phase_skill.md
[^evt-community-events-file-d8b637bc00e2-5c63f836]: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/evals/sync-front-door/graders/skill_fires.md
