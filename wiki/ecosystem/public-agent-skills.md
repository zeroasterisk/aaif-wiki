---
type: resource
title: Public Agent Skills and Evaluation Harnesses
description: Standardized skill definitions, prompt triggers, negative regression
  suites, and comparative evaluation harnesses for agentic AI workflows.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/announcement-post/prompt.md
tags:
- skills
- evaluations
- ecosystem
- testing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:42:36.102156+00:00'
sources:
- id: evt-community-events-file-79d927ff6229-9d338aa6
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/announcement-post/prompt.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:52:16-07:00'
- id: evt-community-events-file-995af191aa66-c91cec0e
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/audit-slack/prompt.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:52:16-07:00'
- id: evt-community-events-file-8570bc08b106-eb1aa55d
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/announcement-post/graders/not_the_neighbours.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
- id: evt-community-events-file-95e86f9d14bc-9418ea76
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/announcement-post/graders/skill_fires.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
- id: evt-community-events-file-a1a9eeb43d4d-942740dd
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/README.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
---

# Overview

AAIF public agent skills are portable, standardized execution units and prompt descriptions designed to run safely across AI agent runtimes [^evt-community-events-file-a1a9eeb43d4d-942740dd]. To guarantee that skills fire reliably without triggering neighbouring capabilities or violating safety boundaries, skills are verified through structured, dual-arm evaluation test harnesses [^evt-community-events-file-a1a9eeb43d4d-942740dd].

# Architecture / Specification

## Skill Evaluation Framework

Deterministic checks such as static schema validation and script unit tests verify syntax, but behavioral reliability requires prompt-driven triggering and constraint evaluations [^evt-community-events-file-a1a9eeb43d4d-942740dd].

### Trigger Disambiguation and Negative Gradings
Skills operating in close semantic domains (e.g., event announcements, recaps, and reminders) are susceptible to misclassification [^evt-community-events-file-8570bc08b106-eb1aa55d][^evt-community-events-file-95e86f9d14bc-9418ea76]. Evaluation suites assert two distinct criteria:
1. **Target Activation**: Validates that the intended skill fires given a natural conversational prompt [^evt-community-events-file-79d927ff6229-9d338aa6][^evt-community-events-file-95e86f9d14bc-9418ea76][^evt-community-events-file-995af191aa66-c91cec0e].
2. **Negative Neighbour Exclusion**: Asserts via trace regex matching that adjacent domain skills are not erroneously invoked [^evt-community-events-file-8570bc08b106-eb1aa55d].

### Dual-Arm Delta Evaluation (`arm: with-only`)
Evaluations execute in paired runs: once with the candidate skill enabled and once without [^evt-community-events-file-a1a9eeb43d4d-942740dd]. Gradings designated as `with-only` ensure assertions only pass when the skill documentation actively enforces constraints (such as stripping PII or enforcing authorization gates) that the base model fails by default [^evt-community-events-file-a1a9eeb43d4d-942740dd].

[^evt-community-events-file-79d927ff6229-9d338aa6]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/announcement-post/prompt.md
[^evt-community-events-file-8570bc08b106-eb1aa55d]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/announcement-post/graders/not_the_neighbours.md
[^evt-community-events-file-95e86f9d14bc-9418ea76]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/announcement-post/graders/skill_fires.md
[^evt-community-events-file-995af191aa66-c91cec0e]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/audit-slack/prompt.md
[^evt-community-events-file-a1a9eeb43d4d-942740dd]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/evals/README.md
