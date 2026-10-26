---
type: skill
title: AAIF LinkedIn Carousel Copy
description: Social copy drafting skill generating structured six-slide LinkedIn carousel
  narratives promoting AAIF events.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-carousel-copy/SKILL.md
tags:
- skills
- social-media
- linkedin
- content
- brand
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:57:07.430992+00:00'
sources:
- id: evt-community-events-file-52894c310bd9-02d85f04
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-carousel-copy/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview
`aaif-carousel-copy` is a specialized agent skill designed to extract event metadata from an AAIF chapter event tracker and draft concise copy for a six-slide LinkedIn carousel presentation [^evt-community-events-file-52894c310bd9-02d85f04]. The skill aligns community promotion with the foundation's architectural voice, structuring slides to lead with practitioner value rather than marketing hyperbole [^evt-community-events-file-52894c310bd9-02d85f04].

# Architecture / Specification
The skill enforces specific constraints regarding structural layout, tone, and privacy [^evt-community-events-file-52894c310bd9-02d85f04]:

- **Six-Slide Structure**: The carousel adheres to a strict six-slide framework where slide 1 provides an engaging hook, intermediate slides detail topic substance and speakers, and slide 6 provides the call to action (CTA) [^evt-community-events-file-52894c310bd9-02d85f04]. Every slide consists of a headline constrained to a maximum of seven words followed by a single short supporting line [^evt-community-events-file-52894c310bd9-02d85f04].
- **Editorial Voice**: Follows the foundation's "builder-to-builder" voice: focusing on concrete engineering practice over product promotion, technical specificity over grand claims, and informative signal over metric vanity [^evt-community-events-file-52894c310bd9-02d85f04].
- **Privacy Protections**: Applies the public-copy rule common to all community event skills: attendee PII, unpublished venue entry instructions, and contact information must never appear in copy, responses, or agent transcripts [^evt-community-events-file-52894c310bd9-02d85f04].
- **Rendering & Asset Pipeline**: Populates the chapter's `Event Template/LinkedIn Carousel.pptx` via `gws`, converting to Google Slides for PDF export or utilizing `aaif_events.slides_export` for high-fidelity PNG rendering [^evt-community-events-file-52894c310bd9-02d85f04].

# Lifecycle History
Integrates with AAIF communication standards defined in [social-media-guidelines](../guidelines/social-media-guidelines.md) and [brand-guidelines](../guidelines/brand-guidelines.md) [^evt-community-events-file-52894c310bd9-02d85f04].

# References
- Reference implementation: `skills/aaif-carousel-copy/SKILL.md` [^evt-community-events-file-52894c310bd9-02d85f04]

[^evt-community-events-file-52894c310bd9-02d85f04]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-carousel-copy/SKILL.md
