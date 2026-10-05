---
type: skill
title: AAIF LinkedIn Carousel Copy Skill
description: Standardized skill generating structured 6-slide LinkedIn carousel copy
  and PDF collateral for AAIF community event promotion.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-carousel-copy/SKILL.md
tags:
- skills
- community
- social
- marketing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:56:09.400706+00:00'
sources:
- id: evt-community-events-file-52894c310bd9-392b08f5
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-carousel-copy/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
---

# Overview
The `aaif-carousel-copy` skill drafts structured promotional copy for a 6-slide LinkedIn carousel deck based on AAIF chapter and online series event tracker data[^evt-community-events-file-52894c310bd9-392b08f5]. It enforces editorial constraints, brand voice rules, and privacy protections when generating slide headlines and supporting copy[^evt-community-events-file-52894c310bd9-392b08f5].

# Architecture / Specification
The skill executes a structured workflow for generating and rendering slide collateral[^evt-community-events-file-52894c310bd9-392b08f5]:

- **Slide Structure**: Produces exactly six slides where each slide includes a headline (maximum 7 words) and one short supporting line, with slide 1 hooking the reader and slide 6 serving as the call to action (CTA)[^evt-community-events-file-52894c310bd9-392b08f5].
- **Data Ingestion**: Queries the chapter or series `Event Tracker.docx` via `skills/aaif-event-status/scripts/fetch_tracker.py` to extract event metadata[^evt-community-events-file-52894c310bd9-392b08f5].
- **Public-Copy Privacy Rule**: Automatically suppresses private personal identifiers (such as attendee emails, personal phone numbers, or door access codes) from both generated drafts and conversational agent responses[^evt-community-events-file-52894c310bd9-392b08f5].
- **Deck Rendering**: Updates the PowerPoint template (`LinkedIn Carousel.pptx`) via `gws` and converts it to PDF or renders individual PNG slides via `aaif_events.slides_export` without local office suite conversions[^evt-community-events-file-52894c310bd9-392b08f5].

[^evt-community-events-file-52894c310bd9-392b08f5]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-carousel-copy/SKILL.md
