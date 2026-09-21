---
type: methodology
title: AAIF Carousel Copy Skill
description: Operational agent skill for generating 6-slide LinkedIn carousel copy
  and managing export workflows for AAIF event promotion.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-carousel-copy/SKILL.md
tags:
- skills
- community
- events
- design
- social-media
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:12:53.653858+00:00'
sources:
- id: evt-community-events-file-52894c310bd9-8aae0fc9
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-carousel-copy/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:34:23-07:00'
- id: evt-community-events-file-a5c0f08bc43f-e22bd242
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/.github/workflows/validate.yml
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:32:24-07:00'
- id: evt-community-events-file-63a9c44a44ac-a1b4ea70
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/.pre-commit-config.yaml
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:34:23-07:00'
---

# Overview
The `aaif-carousel-copy` skill generates structured headline and caption text for 6-slide LinkedIn carousel decks announcing AAIF events[^evt-community-events-file-52894c310bd9-8aae0fc9]. It ingests event details from the chapter tracker (via [aaif-event-status](../methodology/aaif-event-status-skill.md)) and formats succinct slide copy aligned with [brand guidelines](../guidelines/brand-guidelines.md) and automated export workflows[^evt-community-events-file-52894c310bd9-8aae0fc9].

# Architecture / Specification
The skill guides carousel narrative structure and Google Drive conversion mechanics[^evt-community-events-file-52894c310bd9-8aae0fc9]:
- **6-Slide Narrative Flow**: Slide 1 serves as the opening hook; Slides 2 through 5 showcase technical topics, speakers, and live demos (limited to a headline of at most 7 words and one supporting line); Slide 6 provides the RSVP call-to-action[^evt-community-events-file-52894c310bd9-8aae0fc9].
- **Drive Tooling Workflow**: Interacts with Google Drive files using the `gws` CLI driven by Python scripts[^evt-community-events-file-52894c310bd9-8aae0fc9]. It updates `Event Template/LinkedIn Carousel.pptx`, converts the `.pptx` to a temporary Google Slides presentation via `gws drive files copy`, exports the deck to PDF via `gws drive files export`, and purges the temporary copy[^evt-community-events-file-52894c310bd9-8aae0fc9].
- **Rendering and Font Integrity**: Forbids headless tools like LibreOffice (`soffice`) and `unoconv` due to font substitution and OOXML corruption, mandating native API conversions or `aaif_events.slides_export` PNG rendering for high-fidelity needs[^evt-community-events-file-52894c310bd9-8aae0fc9].
- **Public-Copy Safety**: Strictly enforces privacy restrictions prohibiting the inclusion of unpublished email addresses, phone numbers, or private attendee names[^evt-community-events-file-52894c310bd9-8aae0fc9].

# Lifecycle History
The skill is maintained in `skills/aaif-carousel-copy/SKILL.md` within the `aaif/community-events` repository, subjected to pre-commit checks preventing banner drift and unredacted PII leaks[^evt-community-events-file-a5c0f08bc43f-e22bd242][^evt-community-events-file-63a9c44a44ac-a1b4ea70].

[^evt-community-events-file-52894c310bd9-8aae0fc9]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-carousel-copy/SKILL.md
[^evt-community-events-file-63a9c44a44ac-a1b4ea70]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/.pre-commit-config.yaml
[^evt-community-events-file-a5c0f08bc43f-e22bd242]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/.github/workflows/validate.yml
