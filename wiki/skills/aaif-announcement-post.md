---
type: skill
title: AAIF Announcement Post Skill
description: LinkedIn launch copy generation skill enforcing privacy protection, attendee
  disclosure controls, and event RSVP announcement triggering boundaries.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/announcement-post/prompt.md
tags:
- skill
- community
- social-media
- content
- evals
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:00:12.294357+00:00'
sources:
- id: evt-community-events-file-79d927ff6229-9d338aa6
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/announcement-post/prompt.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:52:16-07:00'
- id: evt-community-events-file-8570bc08b106-eb1aa55d
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/announcement-post/graders/not_the_neighbours.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
- id: evt-community-events-file-95e86f9d14bc-9418ea76
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/announcement-post/graders/skill_fires.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
---

# Overview
The `aaif-announcement-post` skill is a modular agent skill that drafts LinkedIn announcement copy when chapter event RSVPs open, incorporating logistics, speaker topics, and registration links under AAIF privacy and editorial guidelines[^evt-community-events-file-79d927ff6229-9d338aa6][^evt-community-events-file-95e86f9d14bc-9418ea76].

# Architecture / Specification
The skill is triggered specifically when registration opens for an upcoming event and prospective attendees must be directed to an RSVP page[^evt-community-events-file-79d927ff6229-9d338aa6].

### Neighboring Skill Boundaries
Because multiple attendee-facing writing skills share similar description keywords (such as "post" and "AAIF event"), the [community-events-eval-suite](../resources/community-events-eval-suite.md) actively evaluates skill routing discrimination to prevent adjacent skills from firing on announcement requests[^evt-community-events-file-8570bc08b106-eb1aa55d][^evt-community-events-file-95e86f9d14bc-9418ea76]:
- **`aaif-announcement-post`**: Fires exclusively for the "RSVPs are open" milestone to drive initial registration[^evt-community-events-file-79d927ff6229-9d338aa6][^evt-community-events-file-95e86f9d14bc-9418ea76].
- **`aaif-luma-description`**: Limited to staging the primary event landing page prior to or alongside public launch[^evt-community-events-file-8570bc08b106-eb1aa55d].
- **[aaif-attendee-reminder](aaif-attendee-reminder.md)**: Reserved for logistical updates sent to individuals who have already registered[^evt-community-events-file-8570bc08b106-eb1aa55d].
- **`aaif-recap-post`**: Reserved for retrospective summary copy written after an event has taken place[^evt-community-events-file-8570bc08b106-eb1aa55d].

Negative trace match evaluation (`not_the_neighbours`) prevents producing the wrong document type in the correct organization voice, which represents a critical failure mode in automated content workflows[^evt-community-events-file-8570bc08b106-eb1aa55d].

[^evt-community-events-file-79d927ff6229-9d338aa6]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/announcement-post/prompt.md
[^evt-community-events-file-8570bc08b106-eb1aa55d]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/announcement-post/graders/not_the_neighbours.md
[^evt-community-events-file-95e86f9d14bc-9418ea76]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/announcement-post/graders/skill_fires.md
