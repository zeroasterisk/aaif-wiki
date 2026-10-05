---
type: skill
title: AAIF Chapter Badges Synchronization Skill
description: Standardized automation skill generating SVG/PNG community organizer
  badges and synchronizing them idempotently to chapter Drive folders.
resource: https://github.com/aaif/community-events/pull/39
tags:
- skills
- automation
- community
- design-system
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:41:19.744401+00:00'
sources:
- id: evt-community-events-pr-39
  resource: https://github.com/aaif/community-events/pull/39
  author: rparundekar
  last_modified: '2026-09-16T17:47:06+00:00'
---

# Overview
The `aaif-sync-badges` skill automates the generation, styling, and idempotent distribution of official AAIF community organizer badge assets across regional chapter workspaces[^evt-community-events-pr-39]. It produces vector and raster badges using foundation design tokens and synchronizes them directly into Google Drive folder hierarchies[^evt-community-events-pr-39].

# Architecture / Specification
## Badge Styles and Generation
The generation pipeline supports two parallel badge variants, yielding six files per chapter[^evt-community-events-pr-39]:
- **Classic Badge:** Hand-tuned orange badge layout generated via `make_badges.py`[^evt-community-events-pr-39].
- **Agent Design-System Badge:** Generated via `make_agent_badge.py` consuming live tokens from `design/aaif-tokens.css`, embedded Instrument Sans typography, and per-chapter agent mascot artwork (`agent_art.chapter_scene()`), rendered through headless Chrome[^evt-community-events-pr-39].

## Storage Hierarchy and Synchronization
- **Per-Chapter Destination:** Badges are stored in a designated `Badges/` subfolder inside each chapter's root Google Drive folder rather than a flat global bucket[^evt-community-events-pr-39].
- **Drive Migration:** Includes `migrate_legacy_badges.py` for atomic Drive reparenting (`addParents`/`removeParents`) and non-destructive trash cleanup[^evt-community-events-pr-39].
- **Security and Escaping:** Untrusted chapter display names are XML-escaped prior to SVG injection to prevent template injection vulnerabilities[^evt-community-events-pr-39].

# References
- `../policies-guidelines/brand-guidelines.md`
- `../skills/aaif-community-pulse.md`

[^evt-community-events-pr-39]: https://github.com/aaif/community-events/pull/39
