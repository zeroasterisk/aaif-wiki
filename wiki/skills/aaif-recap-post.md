---
type: skill
title: AAIF Event Recap Post Skill
description: An agent skill for drafting post-event LinkedIn recaps highlighting key
  technical takeaways, demos, and attendee discussions.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/recap-post/graders/skill_fires.md
tags:
- skill
- marketing
- recap
- events
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:07:25.718896+00:00'
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

The `aaif-recap-post` skill transforms event outcomes, speaker talk points, attendee metrics, and demo recaps into structured, vendor-neutral post-event LinkedIn posts for AAIF community channels.[^evt-community-events-file-2b5ce8cffe67-7aba21ba]

# Architecture / Specification

### Trigger Boundary vs Announcements
The skill's invocation surface is evaluated strictly in pair with `aaif-announcement-post`:[^evt-community-events-file-ae6fd0f3a42a-a43686f4]
- `aaif-announcement-post` triggers for upcoming event promotion and registration drives.
- `aaif-recap-post` triggers exclusively for after-the-event summaries, speaker talk wrap-ups, and post-event photo sharing.[^evt-community-events-file-ae6fd0f3a42a-a43686f4][^evt-community-events-file-2b5ce8cffe67-7aba21ba]

# Lifecycle History

Maintained in `aaif/community-events` with automated evaluation testing temporal trigger discrimination.[^evt-community-events-file-ae6fd0f3a42a-a43686f4]

[^evt-community-events-file-2b5ce8cffe67-7aba21ba]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/recap-post/prompt.md
[^evt-community-events-file-ae6fd0f3a42a-a43686f4]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/recap-post/graders/skill_fires.md
