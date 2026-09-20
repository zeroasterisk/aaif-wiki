---
type: skill
title: AAIF Day-of Slides Skill
description: An agent skill for transforming event tracker metadata into slide deck
  copy for AAIF day-of-event presentations.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-dayof-slides/SKILL.md
tags:
- skills
- community-events
- slides
- events
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:05:55.779047+00:00'
sources:
- id: evt-community-events-file-4676d39ff431-fa3b0eaf
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-dayof-slides/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:34:23-07:00'
---

# Overview
The `aaif-dayof-slides` skill converts structured event tracker entries into presentation copy for the AAIF "Day of Event" slide deck template [^evt-community-events-file-4676d39ff431-fa3b0eaf]. It automates slide copy generation while preserving brand-standard fixed slides, strict logo placeholder boundaries, and document formatting invariants [^evt-community-events-file-4676d39ff431-fa3b0eaf].

# Architecture / Specification
The skill consumes event metadata from event tracking sheets (via [`aaif-event-status`](./aaif-event-status.md)) and outputs structured, label-driven text for each slide in the presentation sequence [^evt-community-events-file-4676d39ff431-fa3b0eaf].

### Tooling and Document Manipulation Rules
- **Google Workspace First**: File access and updates are executed via Python through the `gws` CLI interacting with native Google Drive formats (Docs, Sheets, Slides APIs) [^evt-community-events-file-4676d39ff431-fa3b0eaf].
- **OOXML Surgery**: Binary OOXML formats (`.pptx`, `.docx`, `.xlsx`) are manipulated directly at the zip part level to protect embedded brand fonts and metadata [^evt-community-events-file-4676d39ff431-fa3b0eaf].
- **Prohibition of Third-Party Desktop Suites**: Third-party local converters such as LibreOffice, `soffice`, or `unoconv` are strictly prohibited to prevent font substitution and schema corruption [^evt-community-events-file-4676d39ff431-fa3b0eaf]. Previews are generated via the Slides export API or Google Drive export pipelines [^evt-community-events-file-4676d39ff431-fa3b0eaf].

### Content and Layout Invariants
- **Fixed Slides**: Retains fixed organizational brand slides (such as "About AAIF" and global network metrics) unchanged [^evt-community-events-file-4676d39ff431-fa3b0eaf].
- **Logo Footer Boundaries**: Protects the cover and welcome slide lockups (`HOSTED BY AAIF`); sponsor venues and community members are credited in prose on dedicated concluding slides rather than replacing cover brand assets [^evt-community-events-file-4676d39ff431-fa3b0eaf].
- **Public-Copy Rule**: Never exposes private intake or venue logistics details [^evt-community-events-file-4676d39ff431-fa3b0eaf].

[^evt-community-events-file-4676d39ff431-fa3b0eaf]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-dayof-slides/SKILL.md
