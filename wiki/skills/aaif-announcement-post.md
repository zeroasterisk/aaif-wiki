---
type: skill
title: AAIF Announcement Post Skill
description: An agent skill for generating vendor-neutral LinkedIn announcement posts
  when AAIF event RSVPs open, enforcing legal footers and neighbor skill exclusion.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/skill_fires.md
tags:
- skills
- events
- social-media
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:08:25.774551+00:00'
sources:
- id: evt-community-events-file-95e86f9d14bc-9418ea76
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/skill_fires.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
- id: evt-community-events-file-8570bc08b106-eb1aa55d
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/not_the_neighbours.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
- id: evt-community-events-file-a7c09511caf9-e4bc8987
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/legal_footer.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
---

# Overview

`aaif-announcement-post` is an attendee-facing writing skill within the AAIF Community Events Toolkit that generates concise, vendor-neutral LinkedIn announcement copy upon opening event registrations.[^evt-community-events-file-95e86f9d14bc-9418ea76] It operates under strict neighbor disambiguation boundaries and mandatory legal footer compliance rules.[^evt-community-events-file-8570bc08b106-eb1aa55d][^evt-community-events-file-a7c09511caf9-e4bc8987]

# Architecture / Specification

## Trigger Boundaries and Neighbor Disambiguation
The skill auto-activates when prompted that RSVPs have opened for an event.[^evt-community-events-file-95e86f9d14bc-9418ea76] Evaluation suites enforce negative triggering against semantically adjacent writing skills:[^evt-community-events-file-8570bc08b106-eb1aa55d]
- `aaif-recap-post`: Reserved exclusively for post-event summary reporting.[^evt-community-events-file-8570bc08b106-eb1aa55d]
- `aaif-luma-description`: Reserved for event platform landing page descriptions.[^evt-community-events-file-8570bc08b106-eb1aa55d]
- `aaif-attendee-reminder`: Reserved for logistics reminders dispatched to already registered attendees.[^evt-community-events-file-8570bc08b106-eb1aa55d]

## Legal Footer Compliance
All generated attendee-facing copy must include standing links to both the [AAIF Code of Conduct](../governance/code-of-conduct.md) and the Privacy Policy in the message footer to prevent footer drift.[^evt-community-events-file-a7c09511caf9-e4bc8987]

[^evt-community-events-file-8570bc08b106-eb1aa55d]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/not_the_neighbours.md
[^evt-community-events-file-95e86f9d14bc-9418ea76]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/skill_fires.md
[^evt-community-events-file-a7c09511caf9-e4bc8987]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/legal_footer.md
