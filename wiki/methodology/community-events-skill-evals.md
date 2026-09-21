---
type: methodology
title: Community Events Skill Evaluation Framework
description: Two-arm evaluation methodology for AAIF community event skills measuring
  activation triggers, neighbor disambiguation, and safety compliance.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/README.md
tags:
- methodology
- evals
- community-events
- testing
- skills
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:15:20.020405+00:00'
sources:
- id: evt-community-events-file-a1a9eeb43d4d-942740dd
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/README.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
- id: evt-community-events-file-8570bc08b106-eb1aa55d
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/not_the_neighbours.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
- id: evt-community-events-file-95e86f9d14bc-9418ea76
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/skill_fires.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
- id: evt-community-events-file-a7c09511caf9-e4bc8987
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/legal_footer.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
- id: evt-community-events-file-fa8f546a26bb-2adc4759
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/audit-slack/graders/skill_fires.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
- id: evt-community-events-file-eca12c0a30e2-e4dc57b4
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/CONTRIBUTING.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
---

# Overview
The Community Events Skill Evaluation Framework is a dual-arm behavioral testing methodology designed to verify that AAIF agent skills trigger accurately on natural practitioner prompts and strictly obey instructions without regressing or overlapping neighbouring capabilities [^evt-community-events-file-a1a9eeb43d4d-942740dd]. Unlike deterministic unit tests that validate file syntax, tooling banners, and script calculations, the eval framework measures whether an LLM agent accurately activates a skill's `SKILL.md` instructions and evaluates the differential value contributed over base model execution [^evt-community-events-file-a1a9eeb43d4d-942740dd] [^evt-community-events-file-eca12c0a30e2-e4dc57b4].

# Architecture / Specification
The evaluation framework executes test cases across two evaluation arms: an unassisted baseline model arm and a skill-enabled plugin arm using `claude plugin eval` [^evt-community-events-file-a1a9eeb43d4d-942740dd].

## Core Test Dimensions
- **Differential Baseline Isolation (`arm: with-only`)**: Graders verify behaviors that must only pass when a `SKILL.md` is loaded, isolating the delta ($\Delta$) contributed by the skill instructions from standard base model capabilities [^evt-community-events-file-a1a9eeb43d4d-942740dd].
- **Neighbor Disambiguation**: Explicit negative assertions ensure that skills sitting close in semantic description space (such as [aaif-announcement-post](aaif-announcement-post-skill.md), [aaif-recap-post](aaif-recap-post-skill.md), [aaif-luma-description](aaif-luma-description-skill.md), and [aaif-attendee-reminder](aaif-attendee-reminder-skill.md)) do not cross-trigger [^evt-community-events-file-8570bc08b106-eb1aa55d] [^evt-community-events-file-95e86f9d14bc-9418ea76].
- **Safety and Public-Copy Rules**: Verifies that public-facing outputs redact private information (e.g., telephone numbers and email addresses) and mandatory legal notices like the [Code of Conduct](../governance/code-of-conduct.md) and Privacy Policy footers are present [^evt-community-events-file-a1a9eeb43d4d-942740dd] [^evt-community-events-file-a7c09511caf9-e4bc8987].
- **Prompt-Injection Resilience & Write Gates**: Asserts that untrusted inputs cannot force status overrides in intake forms and that operational skills default to dry-run reporting unless explicit human approval is supplied [^evt-community-events-file-a1a9eeb43d4d-942740dd].

## Operational Constraints
Evaluations run locally with reporting kept off hosted clouds to protect attendee data and credential boundaries [^evt-community-events-file-a1a9eeb43d4d-942740dd]. Evaluation runs are omitted from pull request CI workflows to eliminate credential exposure on public forks [^evt-community-events-file-a1a9eeb43d4d-942740dd].

[^evt-community-events-file-8570bc08b106-eb1aa55d]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/not_the_neighbours.md
[^evt-community-events-file-95e86f9d14bc-9418ea76]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/skill_fires.md
[^evt-community-events-file-a1a9eeb43d4d-942740dd]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/README.md
[^evt-community-events-file-a7c09511caf9-e4bc8987]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/legal_footer.md
[^evt-community-events-file-eca12c0a30e2-e4dc57b4]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/CONTRIBUTING.md
