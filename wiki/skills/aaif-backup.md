---
type: skill
title: AAIF Operations Backup Skill
description: Standardized automation skill capturing versioned, immutable snapshots
  of critical ops spreadsheets and Drive files prior to risky bulk edits.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-backup/SKILL.md
tags:
- skills
- operations
- backup
- data-integrity
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:56:40.298719+00:00'
sources:
- id: evt-community-events-file-91fd6707275c-30b3ce2e
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-backup/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
---

# Overview
`aaif-backup` is an operational safety skill that captures immutable, timestamped local snapshots of critical AAIF operations data before high-risk mutations such as schema changes, column restructuring, or bulk cleanup scripts [^evt-community-events-file-91fd6707275c-30b3ce2e]. By default, it creates versioned exports of the Community Intake Ops sheet and can snapshot arbitrary Drive files or local paths [^evt-community-events-file-91fd6707275c-30b3ce2e].

# Architecture / Specification
The backup engine executes via `scripts/backup.py` and strictly enforces read/export paths [^evt-community-events-file-91fd6707275c-30b3ce2e].

### Key Features and Guardrails
- **Immutable Versioning**: Snapshots are saved to timestamped paths (e.g., `<dest>/<slug>/<UTC-timestamp>.<ext>`) without overwriting previous runs, preserving an audit trail [^evt-community-events-file-91fd6707275c-30b3ce2e].
- **Native API Integration**: Interacts with Google Drive via the `gws` CLI to export Google Workspace files directly to native Office formats (.xlsx, .docx, .pptx) without intermediary desktop office suite conversions [^evt-community-events-file-91fd6707275c-30b3ce2e].
- **Tooling Constraints**: Prohibits third-party conversion binaries (like LibreOffice/`soffice` or `unoconv`) to prevent font corruption and XML schema stripping [^evt-community-events-file-91fd6707275c-30b3ce2e].

[^evt-community-events-file-91fd6707275c-30b3ce2e]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-backup/SKILL.md
