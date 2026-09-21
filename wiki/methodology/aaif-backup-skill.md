---
type: methodology
title: AAIF Backup Skill
description: Operational agent skill for creating timestamped, immutable local backups
  of AAIF community operations data prior to mutations.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-backup/SKILL.md
tags:
- automation
- skill
- operations
- backup
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:58:05.942337+00:00'
sources:
- id: evt-community-events-file-91fd6707275c-7f3a8d13
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-backup/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-08-21T14:07:26-07:00'
---

# Overview
The AAIF Backup Skill (`aaif-backup`) is a standardized agent skill for taking versioned, immutable local snapshots of critical Agentic AI Foundation operational datasets, such as the Community Intake Ops sheet, before executing risky or bulk edits [^evt-community-events-file-91fd6707275c-7f3a8d13].

# Architecture / Specification
The skill enforces operational and data integrity rules:
- **API-First Automation**: All Google Drive document modifications are executed via the `gws` CLI driven by Python scripts (`scripts/backup.py`) [^evt-community-events-file-91fd6707275c-7f3a8d13]. Third-party desktop conversion suites such as LibreOffice are explicitly prohibited to prevent font substitutions and OOXML corruption.
- **Immutable Snapshots**: Snapshots are saved to timestamped paths formatted as `<dest>/<slug>/<UTC-timestamp>.<ext>` [^evt-community-events-file-91fd6707275c-7f3a8d13].
- **Repository Safety**: The destination folder (defaulting to `./backups`) is git-ignored, and execution is refused if the destination directory contains tracked files inside a repository [^evt-community-events-file-91fd6707275c-7f3a8d13].

[^evt-community-events-file-91fd6707275c-7f3a8d13]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-backup/SKILL.md
