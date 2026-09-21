---
type: methodology
title: AAIF Create Online Series Skill
description: Operational agent skill for provisioning recurring AAIF online event
  series in Google Drive by cloning TemplateSeries and rebranding assets.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-create-online-series/SKILL.md
tags:
- methodology
- community-events
- skills
- automation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:02:45.557539+00:00'
sources:
- id: evt-community-events-file-2e96153bc720-e7b736d6
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-create-online-series/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-08-27T15:52:49-07:00'
- id: evt-community-events-pr-31
  resource: https://github.com/aaif/community-events/pull/31
  author: rparundekar
  last_modified: '2026-08-27T21:52:07+00:00'
---

# Overview

`aaif-create-online-series` is an operational agent skill designed to provision and bootstrap new Agentic AI Foundation online event programs (such as reading groups, paper clubs, webinars, and virtual panel series) in Google Drive [^evt-community-events-file-2e96153bc720-e7b736d6]. It acts as the online counterpart to `aaif-create-chapter`.

Online series reside in the top-level `Online/` Drive workspace and clone the `TemplateSeries` structure, creating dedicated trackers, attendee CRMs, and design asset folders without physical venue fields [^evt-community-events-file-2e96153bc720-e7b736d6].

# Architecture / Specification

## Tooling Rules

- **Drive Interface**: Driven strictly via the `gws` CLI and Python. Native Google Workspace files (`application/vnd.google-apps.*`) are manipulated via Docs/Sheets/Slides APIs.
- **OOXML Byte Manipulation**: Direct zip/XML manipulation is reserved for stored Office files (`.docx`, `.pptx`, `.xlsx`). Desktop suites (e.g., LibreOffice / `soffice`, `unoconv`) are strictly prohibited to prevent font substitution and OOXML degradation [^evt-community-events-file-2e96153bc720-e7b736d6].
- **Slide Previews**: Rendered via `aaif_events.slides_export.render_slide_png` API instead of local conversion [^evt-community-events-file-2e96153bc720-e7b736d6].

## Rebranding Transforms

When instantiating `TemplateSeries`, the skill applies token replacement while preserving template structure:
- Replaces `San Francisco` / `SAN FRANCISCO` tokens with the target series name.
- Expands `SF` abbreviations to the full series name.
- Replaces default Luma slugs (`aaif-sanfrancisco` / `aaif-sf`) with series-specific slugs (`aaif-<slug>`).
- Incorporates standardized AAIF lockup footers into template decks [^evt-community-events-pr-31].

[^evt-community-events-file-2e96153bc720-e7b736d6]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-create-online-series/SKILL.md
[^evt-community-events-pr-31]: https://github.com/aaif/community-events/pull/31
