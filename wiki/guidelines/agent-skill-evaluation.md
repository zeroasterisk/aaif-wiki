---
type: guideline
title: Agent Skill Evaluation Framework
description: Empirical evaluation framework and trigger verification methodology for
  agent skills, portable tools, and multi-skill orchestration pipelines.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/sync-front-door/prompt.md
tags:
- evals
- skills
- testing
- benchmarks
- verification
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:12:12.687642+00:00'
sources:
- id: evt-community-events-file-60baba93c961-5853f27a
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/sync-front-door/prompt.md
  author: Rahul Parundekar
  last_modified: '2026-09-19T15:40:28-07:00'
- id: evt-community-events-file-a7c09511caf9-8abab7d5
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/announcement-post/graders/legal_footer.md
  author: Rahul Parundekar
  last_modified: '2026-09-19T15:40:28-07:00'
- id: evt-community-events-file-ba08ba8ec7d9-cd762fcd
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/sync-front-door/graders/order_is_respected.md
  author: Rahul Parundekar
  last_modified: '2026-09-19T15:40:28-07:00'
- id: evt-community-events-file-cc0e90fa8ff2-c75eeab5
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/sync-front-door/graders/not_a_phase_skill.md
  author: Rahul Parundekar
  last_modified: '2026-09-19T15:40:28-07:00'
- id: evt-community-events-file-d8b637bc00e2-5c63f836
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/sync-front-door/graders/skill_fires.md
  author: Rahul Parundekar
  last_modified: '2026-09-19T15:40:28-07:00'
---

# Overview

The Agent Skill Evaluation Framework defines empirical verification patterns, trigger fidelity tests, and multi-grader evaluation criteria for portable tools and agent skills within the Agentic AI Foundation (AAIF) ecosystem. It establishes testing standards to verify that agents correctly route high-level user requests to root orchestration skills rather than premature phase-specific skills, execute multi-stage operational pipelines in strict dependency order, separate reporting from destructive state writes, and comply with mandatory output requirements such as legal footers[^evt-community-events-file-60baba93c961-5853f27a][^evt-community-events-file-a7c09511caf9-8abab7d5][^evt-community-events-file-cc0e90fa8ff2-c75eeab5][^evt-community-events-file-d8b637bc00e2-5c63f836].

# Architecture / Specification

### Trigger Disambiguation and Namespace Isolation

When multiple specialized phase skills (for example, `aaif-sync-chapters`, `aaif-sync-organizers`, and `aaif-sync-slack`) share semantic overlap with a general front-door orchestrator (`aaif-sync`), evaluations must enforce strict routing boundaries[^evt-community-events-file-cc0e90fa8ff2-c75eeab5][^evt-community-events-file-d8b637bc00e2-5c63f836]:

1. **Positive Tool Triggering (`tool_used`)**: High-level or estate-wide operational prompts must invoke the top-level orchestrator skill that manages end-to-end pipeline execution and sequencing[^evt-community-events-file-60baba93c961-5853f27a][^evt-community-events-file-d8b637bc00e2-5c63f836].
2. **Negative Trace Assertions (`not_contains`)**: The evaluation harness asserts via trace inspection regexes that no individual phase skill fires independently for an estate-level prompt, preventing partial or incomplete pipeline runs[^evt-community-events-file-cc0e90fa8ff2-c75eeab5].

### Grader Typology

The evaluation harness employs three complementary grader types:

- **Regex Graders**: Perform deterministic matching over final outputs or traces. Used to verify structural compliance, such as ensuring attendee-facing announcements carry both mandatory links (`../policies/code-of-conduct.md` and Privacy Policy) to prevent legal footer drift[^evt-community-events-file-a7c09511caf9-8abab7d5].
- **Tool Invocations Graders**: Assert minimum tool usage counts and match tool parameters or skill names within execution traces[^evt-community-events-file-d8b637bc00e2-5c63f836].
- **Model-Based Evaluators (LLM Graders)**: Evaluate behavioral ordering, ensuring the agent proposes multi-stage actions as ordered dependency sequences, generates review reports prior to mutations, and adheres to `../patterns/proposal-execution-split.md` by confirming candidate matches before mutating downstream state[^evt-community-events-file-ba08ba8ec7d9-cd762fcd].

# References

- Deterministic Acceptance Gates: `../patterns/deterministic-acceptance-gate.md`
- Proposal-Execution Split: `../patterns/proposal-execution-split.md`
- Code of Conduct: `../policies/code-of-conduct.md`
- Community Chapter Lifecycle: `../policies/community-chapter-lifecycle.md`

[^evt-community-events-file-60baba93c961-5853f27a]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/sync-front-door/prompt.md
[^evt-community-events-file-a7c09511caf9-8abab7d5]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/announcement-post/graders/legal_footer.md
[^evt-community-events-file-ba08ba8ec7d9-cd762fcd]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/sync-front-door/graders/order_is_respected.md
[^evt-community-events-file-cc0e90fa8ff2-c75eeab5]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/sync-front-door/graders/not_a_phase_skill.md
[^evt-community-events-file-d8b637bc00e2-5c63f836]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/sync-front-door/graders/skill_fires.md
