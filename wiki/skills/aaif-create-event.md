---
type: skill
title: AAIF Create Event Skill
description: Standardized automation skill cloning event task templates into chapter
  or online series trackers and provisioning live Luma event listings upon approval.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-create-event/SKILL.md
tags:
- skills
- community
- events
- luma
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:56:09.400706+00:00'
sources:
- id: evt-community-events-file-4c2672b57ca1-cb10dc93
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-create-event/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
---

# Overview
The `aaif-create-event` skill automates the scheduling and task setup for AAIF in-person chapter and online series events by cloning task template sections in `Event Tracker.docx` files and computing milestone due dates[^evt-community-events-file-4c2672b57ca1-cb10dc93]. Once scheduled, the skill can draft and publish live Luma calendar listings subject to explicit human confirmation[^evt-community-events-file-4c2672b57ca1-cb10dc93].

# Architecture / Specification
The skill interacts with Google Drive via the `gws` CLI tool and local Python OOXML modification scripts[^evt-community-events-file-4c2672b57ca1-cb10dc93]:

- **Tracker Customization**: Differentiates between in-person chapters (requiring `VENUE` and `LOCATION / CITY` fields) and online series (requiring `PLATFORM` and `STREAM / JOIN LINK` fields)[^evt-community-events-file-4c2672b57ca1-cb10dc93].
- **Date Arithmetic**: Computes milestone task due dates backward from the target event date, preserving the schedule cadence defined in tracker templates[^evt-community-events-file-4c2672b57ca1-cb10dc93].
- **Luma Integration**: Formulates markdown event descriptions and connects to Luma's calendar API using API keys stored securely in system keychains or environment variables (`LUMA_API_KEY`)[^evt-community-events-file-4c2672b57ca1-cb10dc93].
- **Approval Checkpoints**: External API creation is gated behind explicit human approval, aligning with [patterns/approval-checkpoint](../patterns/approval-checkpoint.md)[^evt-community-events-file-4c2672b57ca1-cb10dc93].
- **Tooling Constraints**: Forbids third-party office conversions such as LibreOffice/`soffice` or `unoconv` to preserve brand typography and embedded OOXML metadata[^evt-community-events-file-4c2672b57ca1-cb10dc93].

[^evt-community-events-file-4c2672b57ca1-cb10dc93]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-create-event/SKILL.md
