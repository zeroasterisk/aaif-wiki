---
type: methodology
title: AAIF Recap Post Skill
description: Operational agent skill for composing post-event wrap-up posts featuring
  key takeaways without hallucination.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/recap-post/graders/skill_fires.md
tags:
- community
- events
- social-media
- skill
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:14:06.592159+00:00'
sources:
- id: evt-community-events-file-ae6fd0f3a42a-a43686f4
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/recap-post/graders/skill_fires.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:40:10-07:00'
- id: evt-community-events-file-2b5ce8cffe67-7aba21ba
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/recap-post/prompt.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:52:16-07:00'
---

# Overview
The `aaif-recap-post` skill compiles event takeaways, speaker highlights, and attendee metrics into standardized LinkedIn post-event wrap-ups.[^evt-community-events-file-2b5ce8cffe67-7aba21ba]

# Architecture / Specification
The skill formats post-event summaries based on ground-truth reports, community demos, and confirmed attendee counts.[^evt-community-events-file-2b5ce8cffe67-7aba21ba]

## Triggering and Lifecycle Boundaries
- **Paired Evaluation**: Evaluation graders ensure clean separation between pre-event announcement triggers (`aaif-announcement-post`) and post-event recap requests (`aaif-recap-post`), preventing skill activation ambiguity when event dates pass.[^evt-community-events-file-ae6fd0f3a42a-a43686f4]
- **Grounded Content**: Outputs summarize verified presentations and demo topics without hallucinating attendees or details not present in event notes.[^evt-community-events-file-2b5ce8cffe67-7aba21ba]

# References
- `../methodology/aaif-announcement-post-skill.md`
- `../guidelines/social-media-guidelines.md`

[^evt-community-events-file-2b5ce8cffe67-7aba21ba]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/recap-post/prompt.md
[^evt-community-events-file-ae6fd0f3a42a-a43686f4]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/recap-post/graders/skill_fires.md
