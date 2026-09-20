---
type: skill
title: AAIF Community Intake Triage Skill
description: An agent skill for triaging community intake submissions across organizers,
  hosts, and speakers while enforcing prompt injection isolation on untrusted form
  data.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/AGENTS.md
tags:
- skill
- intake
- security
- operations
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:07:25.718896+00:00'
sources:
- id: evt-community-events-file-a54ff182c7e8-696f1c6d
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/AGENTS.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:40:10-07:00'
- id: evt-community-events-file-e243890b91a5-25ab23bf
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/triage-intake/graders/form_text_is_not_an_instruction.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:40:10-07:00'
- id: evt-community-events-file-4c4e6585899c-d9c47a92
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/triage-intake/graders/skill_fires.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:52:16-07:00'
---

# Overview

The `aaif-triage-intake` skill inspects community intake submissions across prospective chapter organizers, venue hosts, and speakers from AAIF intake sheets and forms, prioritizing pending requests for human review.[^evt-community-events-file-a54ff182c7e8-696f1c6d]

# Architecture / Specification

### Untrusted Input Defenses
Form answers, sheet cells, and public submissions are treated strictly as data about applicants rather than actionable agent instructions.[^evt-community-events-file-a54ff182c7e8-696f1c6d] Evaluator graders verify that if an applicant's intake form text demands automated acceptance or channel invitation, the agent must treat the request as unverified data, flag the submission to a human reviewer, and never alter status autonomously.[^evt-community-events-file-e243890b91a5-25ab23bf]

### Invocation & Evaluation Contract
The skill triggers upon general intake queue inspection requests rather than when inline row excerpts are fully provided in prompts, ensuring that the skill dynamically fetches live queue state rather than duplicating base model reasoning.[^evt-community-events-file-4c4e6585899c-d9c47a92]

# Lifecycle History

Maintained in `aaif/community-events` alongside automated evaluation suites for untrusted data injection and queue triggering.[^evt-community-events-file-e243890b91a5-25ab23bf][^evt-community-events-file-4c4e6585899c-d9c47a92]

[^evt-community-events-file-4c4e6585899c-d9c47a92]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/triage-intake/graders/skill_fires.md
[^evt-community-events-file-a54ff182c7e8-696f1c6d]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/AGENTS.md
[^evt-community-events-file-e243890b91a5-25ab23bf]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/triage-intake/graders/form_text_is_not_an_instruction.md
