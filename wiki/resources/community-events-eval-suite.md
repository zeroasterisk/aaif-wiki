---
type: resource
title: Community Events Evaluation Suite
description: Automated regression evaluation suite and grader catalog benchmarking
  community operations skills across routing, pipeline sequence invariants, and legal
  compliance.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/announcement-post/graders/legal_footer.md
tags:
- evals
- community
- graders
- testing
- benchmarks
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:04:45.527198+00:00'
sources:
- id: evt-community-events-file-a7c09511caf9-8abab7d5
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/announcement-post/graders/legal_footer.md
  author: Rahul Parundekar
  last_modified: '2026-09-19T15:40:28-07:00'
- id: evt-community-events-file-ba08ba8ec7d9-cd762fcd
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/sync-front-door/graders/order_is_respected.md
  author: Rahul Parundekar
  last_modified: '2026-09-19T15:40:28-07:00'
- id: evt-community-events-file-cc0e90fa8ff2-c75eeab5
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/sync-front-door/graders/not_a_phase_skill.md
  author: Rahul Parundekar
  last_modified: '2026-09-19T15:40:28-07:00'
- id: evt-community-events-file-d8b637bc00e2-5c63f836
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/sync-front-door/graders/skill_fires.md
  author: Rahul Parundekar
  last_modified: '2026-09-19T15:40:28-07:00'
---

# Overview
The Community Events Evaluation Suite is an automated grading and regression test harness developed for the `aaif/community-events` repository to evaluate agent skills on operational tasks.[^evt-community-events-file-a7c09511caf9-8abab7d5][^evt-community-events-file-d8b637bc00e2-5c63f836] It ensures that autonomous and semi-autonomous skills conform to operational boundaries, safety invariants, and procedural pipelines.

The suite utilizes a combination of LLM-as-a-judge criteria, regular expression pattern guards, and tool invocation assertions to validate agent execution traces before and after operational deployments.[^evt-community-events-file-a7c09511caf9-8abab7d5][^evt-community-events-file-ba08ba8ec7d9-cd762fcd]

# Architecture / Specification
The evaluation suite contains specialized grader packages targeting discrete failure modes across community skills.

## Sync Front-Door Graders
Evaluations under `evals/sync-front-door` safeguard multi-phase estate synchronization in [AAIF Sync](../skills/aaif-sync.md):[^evt-community-events-file-d8b637bc00e2-5c63f836]
- `skill_fires.md`: Validates that whole-estate drift prompts activate the primary `aaif-sync` orchestrator rather than bypassing it.[^evt-community-events-file-d8b637bc00e2-5c63f836]
- `not_a_phase_skill.md`: Enforces that specialized phase skills (`aaif-sync-chapters`, `aaif-sync-organizers`, `aaif-sync-slack`) do not fire independently for high-level estate requests.[^evt-community-events-file-cc0e90fa8ff2-c75eeab5]
- `order_is_respected.md`: Assesses that pipeline proposals execute sequentially, enforcing reporting before writing and gating Drive and Slack access on established chapter records.[^evt-community-events-file-ba08ba8ec7d9-cd762fcd]

## Announcement Post Graders
Evaluations under `evals/announcement-post` enforce outbound communication governance in [AAIF Announcement Post](../skills/aaif-announcement-post.md):[^evt-community-events-file-a7c09511caf9-8abab7d5]
- `legal_footer.md`: A regex-based target check asserting that attendee-facing copy includes both the Code of Conduct and Privacy Policy links to prevent footer drift.[^evt-community-events-file-a7c09511caf9-8abab7d5]

# Lifecycle History
Continuous evaluation graders were merged into the `aaif/community-events` repository to lock in architectural invariants for community event operations and synchronization workflows.[^evt-community-events-file-a7c09511caf9-8abab7d5][^evt-community-events-file-d8b637bc00e2-5c63f836]

[^evt-community-events-file-a7c09511caf9-8abab7d5]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/announcement-post/graders/legal_footer.md
[^evt-community-events-file-ba08ba8ec7d9-cd762fcd]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/sync-front-door/graders/order_is_respected.md
[^evt-community-events-file-cc0e90fa8ff2-c75eeab5]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/sync-front-door/graders/not_a_phase_skill.md
[^evt-community-events-file-d8b637bc00e2-5c63f836]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/sync-front-door/graders/skill_fires.md
