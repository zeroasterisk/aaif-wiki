---
type: skill
title: AAIF Audit Slack Skill
description: An agent skill for auditing the AAIF community Slack workspace across
  organizer coverage, topic health, and channel configurations.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/audit-slack/graders/skill_fires.md
tags:
- skills
- slack
- operations
- audit
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:08:25.774551+00:00'
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

`aaif-audit-slack` is an operational agent skill for auditing AAIF Slack workspaces, evaluating organizer channel coverage, discussion topic health, and channel configuration integrity.[^evt-community-events-file-fa8f546a26bb-2adc4759]

# Architecture / Specification

## Auto-Activation and Prompt Robustness
The skill's metadata is designed to match realistic natural user requests without requiring callers to verbatim mirror the skill's internal terminology.[^evt-community-events-file-fa8f546a26bb-2adc4759] Automated behavioral evaluation verifies that general inquiries regarding workspace health reliably trigger `aaif-audit-slack` while conforming to the [agent skill specification](../specification/agent-skill.md).[^evt-community-events-file-a1a9eeb43d4d-942740dd][^evt-community-events-file-fa8f546a26bb-2adc4759]

[^evt-community-events-file-a1a9eeb43d4d-942740dd]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/README.md
[^evt-community-events-file-fa8f546a26bb-2adc4759]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/audit-slack/graders/skill_fires.md
