---
type: methodology
title: AAIF Sync Badges Skill
description: Operational agent skill for generating, restyling, and synchronizing
  AAIF chapter organizer badge assets in per-chapter Google Drive folders.
resource: https://github.com/aaif/community-events/pull/39
tags:
- community-operations
- automation
- badges
- design-system
- google-drive
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:11:27.774715+00:00'
sources:
- id: evt-community-events-pr-39
  resource: https://github.com/aaif/community-events/pull/39
  author: rparundekar
  last_modified: '2026-09-16T17:47:06+00:00'
---

# Overview

The `aaif-sync-badges` skill automates the generation, validation, and synchronization of official organizer badge assets across AAIF local chapter workspaces in Google Drive[^evt-community-events-pr-39]. It provisions both classic orange badges and design-system mascot badges directly into each chapter's dedicated `Badges/` subfolder[^evt-community-events-pr-39].

# Architecture / Specification

### Asset Generation & Storage
- **Target Folder Structure**: Badges are stored in a dedicated `Badges/` subfolder within each chapter's root Drive directory, alongside existing folders like `Icons/` and `Event Templates`[^evt-community-events-pr-39].
- **Badge Styles**:
  - **Classic Badge** (`make_badges.py`): The original hand-tuned orange badge format[^evt-community-events-pr-39].
  - **Design-System Badge** (`make_agent_badge.py`): Renders chapter-specific agent art using embedded Instrument Sans, live palette tokens from `design/aaif-tokens.css`, and deterministic per-chapter color assignments via headless Chrome[^evt-community-events-pr-39].
- **Output Payload**: Generates a standardized suite of 6 badge files per chapter across SVG and high-resolution PNG variants[^evt-community-events-pr-39].

### Security & Operational Guardrails
- **XML Sanitization**: Chapter display names are strictly XML-escaped prior to SVG injection to prevent malformed files or injection attacks from modified folder titles[^evt-community-events-pr-39].
- **Idempotency & Migration**: Driven by `sync_badges.py` with modular builders that generate only missing files. Legacy badges are reparented into chapter subfolders using `migrate_legacy_badges.py` with parent-verification checks and circuit breakers[^evt-community-events-pr-39].

# Lifecycle History

Originally stored in a centralized shared directory, badge management was refactored in PR #39 to colocate badges inside individual chapter Drive directories and introduce design-system mascot badges[^evt-community-events-pr-39].

[^evt-community-events-pr-39]: https://github.com/aaif/community-events/pull/39
