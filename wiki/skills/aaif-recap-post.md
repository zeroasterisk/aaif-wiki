---
type: skill
title: AAIF Post-Event Recap Skill
description: Standardized automation skill for authoring timely LinkedIn recap posts
  highlighting speaker insights, event turnout, and standard legal notices.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-recap-post/SKILL.md
tags:
- skills
- community
- social
- events
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:56:09.400706+00:00'
sources:
- id: evt-community-events-file-6ceee5c2c51f-0a4ad5f7
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-recap-post/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
---

# Overview
The `aaif-recap-post` skill drafts LinkedIn wrap-up posts for AAIF chapter and online series events to be published within 48 hours following an event[^evt-community-events-file-6ceee5c2c51f-0a4ad5f7]. It synthesizes key technical takeaways, acknowledges venue and speaker contributions, and appends mandatory Linux Foundation governance links[^evt-community-events-file-6ceee5c2c51f-0a4ad5f7].

# Architecture / Specification
The skill applies editorial constraints and tracker ingestion routines[^evt-community-events-file-6ceee5c2c51f-0a4ad5f7]:

- **Editorial Structure**: Produces a concise narrative (~110 words) thanking speakers and host venues by name, summarizing 1–2 practical takeaways, mentioning turnout, and teasing the next event[^evt-community-events-file-6ceee5c2c51f-0a4ad5f7]. Limits emoji usage to a single instance[^evt-community-events-file-6ceee5c2c51f-0a4ad5f7].
- **Standard Governance Footer**: Appends standing links to the Linux Foundation Code of Conduct and Privacy Policy outside the core word count[^evt-community-events-file-6ceee5c2c51f-0a4ad5f7].
- **Tracker Integration**: Retrieves event details via `skills/aaif-event-status/scripts/fetch_tracker.py` without leaking private contact fields into public copy or chat transcripts[^evt-community-events-file-6ceee5c2c51f-0a4ad5f7].

[^evt-community-events-file-6ceee5c2c51f-0a4ad5f7]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-recap-post/SKILL.md
