---
type: skill
title: AAIF LinkedIn Carousel Copy Skill
description: An agent skill for generating concise 6-slide copy decks for AAIF LinkedIn
  promotional carousels.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-carousel-copy/SKILL.md
tags:
- skills
- community-events
- social-media
- events
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:05:55.779047+00:00'
sources:
- id: evt-community-events-file-52894c310bd9-8aae0fc9
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-carousel-copy/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:34:23-07:00'
---

# Overview
The `aaif-carousel-copy` skill generates structured caption text and headlines for 6-slide LinkedIn carousels announcing AAIF chapter and online events [^evt-community-events-file-52894c310bd9-8aae0fc9]. It translates event tracker details into concise, builder-oriented social narratives designed for PDF carousel exports [^evt-community-events-file-52894c310bd9-8aae0fc9].

# Architecture / Specification
The skill extracts event logistics, speaker topics, and demo lineups from the event tracker (leveraging [`aaif-event-status`](./aaif-event-status.md) or [`aaif-create-event`](./aaif-create-event.md)) to populate the standardized carousel structure [^evt-community-events-file-52894c310bd9-8aae0fc9].

### Slide Structure and Editorial Constraints
- **Slide 1**: Hook establishing the core technical challenge or theme [^evt-community-events-file-52894c310bd9-8aae0fc9].
- **Slides 2–5**: Technical agenda details, featured speaker insights, demo previews, and practitioner-first values [^evt-community-events-file-52894c310bd9-8aae0fc9].
- **Slide 6**: Call-to-action (CTA) with date, location, and RSVP link [^evt-community-events-file-52894c310bd9-8aae0fc9].
- **Copy Limits**: Headlines are capped at a maximum of 7 words paired with one short supporting line per slide [^evt-community-events-file-52894c310bd9-8aae0fc9].

### Tooling and Export Workflow
- **Drive Manipulation**: Updates the chapter's `LinkedIn Carousel.pptx` template via `gws` CLI tooling, preserving brand typography and layout [^evt-community-events-file-52894c310bd9-8aae0fc9].
- **PDF Export Pipeline**: Converts presentation copies via the Google Slides API to PDF or renders individual slide PNGs via `aaif_events.slides_export` to guarantee visual fidelity [^evt-community-events-file-52894c310bd9-8aae0fc9].
- **Privacy Assurance**: Enforces the public-copy rule, forbidding disclosure of private emails, door codes, or attendee intake data [^evt-community-events-file-52894c310bd9-8aae0fc9].

[^evt-community-events-file-52894c310bd9-8aae0fc9]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-carousel-copy/SKILL.md
