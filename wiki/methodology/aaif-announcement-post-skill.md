---
type: methodology
title: AAIF Announcement Post Skill
description: Operational agent skill for drafting concise LinkedIn launch and RSVP
  announcement posts for AAIF events with mandatory legal footers.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/not_the_neighbours.md
tags:
- methodology
- skill
- community-events
- social-media
- evals
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:15:20.020405+00:00'
sources:
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
- id: evt-community-events-file-a1a9eeb43d4d-942740dd
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/README.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
---

# Overview
The `aaif-announcement-post` skill is an operational agent skill designed to generate concise, practitioner-focused LinkedIn announcement posts when event RSVPs open [^evt-community-events-file-95e86f9d14bc-9418ea76]. It is disambiguated from neighboring event content skills through dedicated evaluation suites and enforces mandatory inclusion of foundation governance links [^evt-community-events-file-8570bc08b106-eb1aa55d] [^evt-community-events-file-a7c09511caf9-e4bc8987].

# Architecture / Specification

## Disambiguation and Neighbor Boundaries
The skill operates within a closely clustered semantic description space alongside other attendee-facing writing skills [^evt-community-events-file-a1a9eeb43d4d-942740dd]:
- **`aaif-announcement-post`**: Triggers specifically when event RSVPs open [^evt-community-events-file-95e86f9d14bc-9418ea76].
- **[aaif-recap-post](aaif-recap-post-skill.md)**: Reserved for post-event summaries after the event has concluded [^evt-community-events-file-8570bc08b106-eb1aa55d].
- **[aaif-luma-description](aaif-luma-description-skill.md)**: Dedicated to the static event registration page copy [^evt-community-events-file-8570bc08b106-eb1aa55d].
- **[aaif-attendee-reminder](aaif-attendee-reminder-skill.md)**: Targeted at already-registered attendees for pre-event logistics [^evt-community-events-file-8570bc08b106-eb1aa55d].

## Mandatory Content Requirements
- **Legal Footer Policy**: Attendee-facing announcement copy must carry standing links to both the [Code of Conduct](../governance/code-of-conduct.md) and the Privacy Policy to prevent footer drift [^evt-community-events-file-a7c09511caf9-e4bc8987].
- **Evaluation Verification**: Verified under the [Community Events Skill Evaluation Framework](community-events-skill-evals.md) via `arm: with-only` graders checking for prompt-specific activation and neighbor suppression [^evt-community-events-file-8570bc08b106-eb1aa55d] [^evt-community-events-file-95e86f9d14bc-9418ea76].

[^evt-community-events-file-8570bc08b106-eb1aa55d]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/not_the_neighbours.md
[^evt-community-events-file-95e86f9d14bc-9418ea76]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/skill_fires.md
[^evt-community-events-file-a1a9eeb43d4d-942740dd]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/README.md
[^evt-community-events-file-a7c09511caf9-e4bc8987]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/announcement-post/graders/legal_footer.md
