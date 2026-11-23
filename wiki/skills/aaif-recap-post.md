---
type: skill
title: AAIF Recap Post Skill
description: Social copy generation skill drafting post-event LinkedIn recaps under
  strict metric-hallucination constraints and temporal routing boundaries.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/recap-post/graders/not_the_announcement.md
tags:
- skills
- social
- community
- evals
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:01:29.072428+00:00'
sources:
- id: evt-community-events-file-42c3ab6be70d-2fba308c
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/recap-post/graders/not_the_announcement.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:40:10-07:00'
- id: evt-community-events-file-598739538a73-226e7bf3
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/recap-post/graders/no_invented_numbers.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:40:10-07:00'
- id: evt-community-events-file-ae6fd0f3a42a-a43686f4
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/recap-post/graders/skill_fires.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:40:10-07:00'
---

# Overview
The `aaif-recap-post` skill drafts LinkedIn summary copy for concluded Agentic AI Foundation events while adhering to strict factual grounding policies[^evt-community-events-file-598739538a73-226e7bf3][^evt-community-events-file-ae6fd0f3a42a-a43686f4]. It serves as the post-event complement to [aaif-announcement-post](../skills/aaif-announcement-post.md), gated by a temporal routing boundary that activates only after an event has taken place[^evt-community-events-file-42c3ab6be70d-2fba308c][^evt-community-events-file-ae6fd0f3a42a-a43686f4].

# Architecture / Specification
The skill enforces explicit editorial and factual constraints:

## Temporal Routing Boundary
The skill triggers exclusively for events that have concluded[^evt-community-events-file-ae6fd0f3a42a-a43686f4]. In accordance with [Community Events Evaluation Suite](../resources/community-events-eval-suite.md) routing checks, descriptions that blur past and upcoming timings are separated such that announcement prompts do not fire recap workflows and recap prompts do not trigger launch copy[^evt-community-events-file-42c3ab6be70d-2fba308c][^evt-community-events-file-ae6fd0f3a42a-a43686f4].

## Grounding Rule: Signal, Not Numbers
The skill adheres to the foundation's public copy standard prioritizing qualitative takeaways over vanity metrics[^evt-community-events-file-598739538a73-226e7bf3]:
- **No Invented Metrics**: The agent must not fabricate or estimate attendance figures, participant percentages, or operational counts not provided in the input context[^evt-community-events-file-598739538a73-226e7bf3].
- **Substantive Signal**: Content focuses on delivered technical demonstrations, community insights, and verified attendance facts[^evt-community-events-file-598739538a73-226e7bf3].

# References
- [AAIF Announcement Post](../skills/aaif-announcement-post.md)
- [Community Events Eval Suite](../resources/community-events-eval-suite.md)
- [Social Media Guidelines](../guidelines/social-media-guidelines.md)

[^evt-community-events-file-42c3ab6be70d-2fba308c]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/recap-post/graders/not_the_announcement.md
[^evt-community-events-file-598739538a73-226e7bf3]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/recap-post/graders/no_invented_numbers.md
[^evt-community-events-file-ae6fd0f3a42a-a43686f4]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/recap-post/graders/skill_fires.md
