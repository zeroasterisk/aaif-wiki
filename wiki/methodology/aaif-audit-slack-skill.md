---
type: methodology
title: AAIF Audit Slack Skill
description: Operational agent skill for evaluating Slack workspace coverage, organizer
  channel access, and topic dormancy across AAIF chapters.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/audit-slack/graders/skill_fires.md
tags:
- methodology
- skill
- community-events
- slack
- auditing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:15:20.020405+00:00'
sources:
- id: evt-community-events-file-fa8f546a26bb-2adc4759
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/audit-slack/graders/skill_fires.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
- id: evt-community-events-file-a1a9eeb43d4d-942740dd
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/README.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
---

# Overview
The `aaif-audit-slack` skill is an operational agent skill used by AAIF chapter maintainers to audit workspace channel coverage, organizer access permissions, and topic dormancy across city chapters [^evt-community-events-file-a1a9eeb43d4d-942740dd]. It is subject to behavioral eval testing to ensure its trigger activates reliably on natural user queries without relying on exact phrasing matches [^evt-community-events-file-fa8f546a26bb-2adc4759].

# Architecture / Specification

## Trigger Coverage and Description Design
- **Natural Language Triggering**: Eval grading tests realistic user phrasing rather than self-referential keywords to guarantee the description triggers auto-activation robustly [^evt-community-events-file-fa8f546a26bb-2adc4759] [^evt-community-events-file-a1a9eeb43d4d-942740dd].
- **Conciseness Constraints**: Refactored to eliminate bloated single-line descriptions while preserving disambiguation fidelity against other chapter and communication auditing workflows [^evt-community-events-file-fa8f546a26bb-2adc4759].

## Evaluation Framework Integration
Tested within the [Community Events Skill Evaluation Framework](community-events-skill-evals.md) using dual-arm model testing to confirm that tool invocation occurs when expected [^evt-community-events-file-fa8f546a26bb-2adc4759] [^evt-community-events-file-a1a9eeb43d4d-942740dd].

[^evt-community-events-file-a1a9eeb43d4d-942740dd]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/README.md
[^evt-community-events-file-fa8f546a26bb-2adc4759]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/audit-slack/graders/skill_fires.md
