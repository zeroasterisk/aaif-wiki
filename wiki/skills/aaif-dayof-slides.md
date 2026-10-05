---
type: skill
title: AAIF Day-of Slides Generation Skill
description: Standardized automation skill converting event tracker records into Day
  of Event slide deck copy while preserving brand lockups.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-dayof-slides/SKILL.md
tags:
- skills
- community
- presentation
- ooxml
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:55:38.670960+00:00'
sources:
- id: evt-community-events-file-4676d39ff431-8c8b765e
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-dayof-slides/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
---

# Overview

The `aaif-dayof-slides` skill transforms structured metadata from an event's `Event Tracker.docx` into formatted slide copy for the AAIF "Day of Event" presentation deck (`Event Template/Slides.pptx`) [^evt-community-events-file-4676d39ff431-8c8b765e]. It populates dynamic event agendas and speaker details while protecting fixed global branding slides [^evt-community-events-file-4676d39ff431-8c8b765e].

# Architecture / Specification

## Deck Invariants and Formatting
- **Fixed Brand Assets**: Slides covering AAIF organizational overviews and global network statistics are marked `[FIXED]` and remain unaltered [^evt-community-events-file-4676d39ff431-8c8b765e].
- **Lockup Placeholders**: The `HOSTED BY` lockup on cover slides is preserved; slot markers (`LOGO 1`, `LOGO 2`) are reserved for organizer image placement rather than text replacement [^evt-community-events-file-4676d39ff431-8c8b765e].
- **Sponsor and Venue Attribution**: Venue and member community credits are routed exclusively to the concluding "Thank you" slide in prose [^evt-community-events-file-4676d39ff431-8c8b765e].

## Public-Copy Protection
Adheres to the AAIF public-copy constraint by withholding non-public attendee records, private door codes, and unlisted speaker contact information during deck drafting and transcript generation [^evt-community-events-file-4676d39ff431-8c8b765e].

# References
- [`aaif-announcement-post`](./aaif-announcement-post.md)
- [`aaif-create-chapter`](./aaif-create-chapter.md)
- [`brand-guidelines`](../policies-guidelines/brand-guidelines.md)

[^evt-community-events-file-4676d39ff431-8c8b765e]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-dayof-slides/SKILL.md
