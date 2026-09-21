---
type: methodology
title: AAIF Day-of Slides Skill
description: Operational agent skill for compiling event tracker metadata into standardized
  slide decks for AAIF day-of-event presentations.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-dayof-slides/SKILL.md
tags:
- skills
- community
- events
- design
- slides
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:12:53.653858+00:00'
sources:
- id: evt-community-events-file-4676d39ff431-fa3b0eaf
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-dayof-slides/SKILL.md
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
The `aaif-dayof-slides` skill transforms event tracker entries into structured slide deck text for chapter "Day of Event" presentations (`Event Template/Slides.pptx`)[^evt-community-events-file-4676d39ff431-fa3b0eaf]. It automates the generation of event-specific agenda items, speaker introductions, and venue instructions while preserving core brand slides[^evt-community-events-file-4676d39ff431-fa3b0eaf].

# Architecture / Specification
The skill enforces formatting, layout protection, and file manipulation protocols[^evt-community-events-file-4676d39ff431-fa3b0eaf]:
- **Slide Generation Protocol**: Emits slide copy in a terse, label-driven format (`Slide N — <name>:`) for dynamic event slides while leaving fixed global brand slides (such as About AAIF and network statistics) untouched[^evt-community-events-file-4676d39ff431-fa3b0eaf].
- **Attribution and Lockup Rules**: Preserves the fixed AAIF lockup on cover and welcome slides alongside placeholder logo slots (`LOGO 1`, `LOGO 2`), restricting host venue and member company credits strictly to Slide 12 (Thank you) prose[^evt-community-events-file-4676d39ff431-fa3b0eaf].
- **Tooling Constraints**: Mandates that Drive operations execute via the `gws` CLI and Python APIs[^evt-community-events-file-4676d39ff431-fa3b0eaf]. It prohibits local conversions via LibreOffice or `soffice` to avoid font substitution and OOXML corruption[^evt-community-events-file-4676d39ff431-fa3b0eaf].
- **Public-Copy Safety**: Restricts the generated slide text from disclosing unvetted attendee identities, private emails, or venue access codes[^evt-community-events-file-4676d39ff431-fa3b0eaf].

# Lifecycle History
Defined in `skills/aaif-dayof-slides/SKILL.md` within `aaif/community-events` and validated in CI using pre-commit hooks and Claude plugin manifest validation[^evt-community-events-file-a5c0f08bc43f-e22bd242][^evt-community-events-file-63a9c44a44ac-a1b4ea70].

[^evt-community-events-file-4676d39ff431-fa3b0eaf]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-dayof-slides/SKILL.md
[^evt-community-events-file-63a9c44a44ac-a1b4ea70]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/.pre-commit-config.yaml
[^evt-community-events-file-a5c0f08bc43f-e22bd242]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/.github/workflows/validate.yml
