---
type: skill
title: AAIF Backup Skill
description: An agent skill for creating immutable, timestamped local backups of AAIF
  operational datasets and Google Drive documents.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-backup/SKILL.md
tags:
- skills
- operations
- backup
- data-management
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:55:28.977530+00:00'
sources:
- id: evt-community-events-file-91fd6707275c-7f3a8d13
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-backup/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-08-21T14:07:26-07:00'
---

# Overview
The `aaif-backup` skill defines an operational workflow for taking versioned, immutable local snapshots of critical Agentic AI Foundation (AAIF) operational data prior to schema changes or bulk edits[^evt-community-events-file-91fd6707275c-7f3a8d13]. By default, it targets the Community Intake Ops sheet but supports snapshotting arbitrary Google Drive files or local paths[^evt-community-events-file-91fd6707275c-7f3a8d13].

Conforming to the [Agent Skill Specification](../specification/agent-skill.md), this skill couples declarative guidance with an execution script (`scripts/backup.py`) driven via the `gws` command-line interface[^evt-community-events-file-91fd6707275c-7f3a8d13].

# Architecture / Specification
The skill enforces strict tooling and immutability invariants:
- **Tooling Constraints**: Operations on Google Drive files strictly execute via Python and the `gws` CLI interacting directly with Docs, Sheets, or Slides APIs[^evt-community-events-file-91fd6707275c-7f3a8d13]. Conversion or editing via desktop office suites such as LibreOffice is disallowed to prevent font substitution and OOXML degradation[^evt-community-events-file-91fd6707275c-7f3a8d13].
- **Storage Safety**: Snapshots land in a structured directory format (`<dest>/<slug>/<UTC-timestamp>.<ext>`), defaulting to `./backups`[^evt-community-events-file-91fd6707275c-7f3a8d13]. The execution script validates that the destination directory is git-ignored and contains no tracked files before proceeding, preventing accidental commits of binary exports to public repositories[^evt-community-events-file-91fd6707275c-7f3a8d13].
- **Immutability**: Every run generates a distinct timestamped file without overwriting existing snapshots, maintaining an auditable local history for diffing and manual restoration[^evt-community-events-file-91fd6707275c-7f3a8d13].

[^evt-community-events-file-91fd6707275c-7f3a8d13]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-backup/SKILL.md
