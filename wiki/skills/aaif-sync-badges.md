---
type: skill
title: AAIF Sync Badges Skill
description: An agent skill for generating, rendering, and synchronizing dual-style
  chapter organizer badges into per-chapter Google Drive Badges folders.
resource: https://github.com/aaif/community-events/pull/39
tags:
- community
- badges
- automation
- drive
- design-system
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:04:33.485834+00:00'
sources:
- id: evt-community-events-pr-39
  resource: https://github.com/aaif/community-events/pull/39
  author: rparundekar
  last_modified: '2026-09-16T17:47:06+00:00'
---

# Overview
The `aaif-sync-badges` skill generates, synchronizes, and migrates community organizer badges for AAIF chapters across Google Drive storage[^evt-community-events-pr-39]. It produces both classic orange badges and design-system agent mascot badges, placing generated assets directly inside dedicated `Badges/` subfolders for each chapter[^evt-community-events-pr-39].

# Architecture / Specification

## Badge Generation Styles
The badge generation pipeline supports two concurrent styles per chapter (six badge files total)[^evt-community-events-pr-39]:
- **Classic Orange Badge (`make_badges.py`)**: The original hand-tuned chapter badge asset[^evt-community-events-pr-39].
- **Design-System Agent Mascot Badge (`make_agent_badge.py`)**: A badge drawing live palette tokens (ink, paper, hairline) from `design/aaif-tokens.css`, embedded Instrument Sans typography via `report_style.font_css()`, and chapter-specific agent mascot scenes (`agent_art.chapter_scene()`), rendered through headless Chrome[^evt-community-events-pr-39].

## Per-Chapter Storage and Migration
Badges are colocated with chapter assets inside chapter-specific `Badges/` subfolders rather than a centralized shared repository[^evt-community-events-pr-39]:
- **Target Resolution**: `canonical_chapters()` resolves chapter Drive folder IDs and dynamically creates missing `Badges/` subdirectories[^evt-community-events-pr-39].
- **Drive Reparenting (`migrate_legacy_badges.py`)**: Migrates existing legacy badge files by adjusting Drive parent pointers (`addParents`/`removeParents`), verifying dual-half completion and handling folder trashing resilience[^evt-community-events-pr-39].
- **Security & XML Escaping**: Chapter display names are XML-escaped prior to SVG injection to prevent formatting corruption and script injection[^evt-community-events-pr-39].

# References
- [AAIF Brand Foundation](../governance/brand-foundation.md)

[^evt-community-events-pr-39]: https://github.com/aaif/community-events/pull/39
