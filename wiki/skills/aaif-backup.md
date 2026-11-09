---
type: skill
title: AAIF Backup Skill
description: Operational agent skill creating timestamped, immutable local and cloud
  snapshots of community Google Drive assets and local spreadsheets.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/backups/README.md
tags:
- skills
- operations
- data-hygiene
- backup
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:22:15.933437+00:00'
sources:
- id: evt-community-events-file-f922f666d0ff-e2dbe3f7
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/backups/README.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-a54ff182c7e8-2d5d5bf6
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview
`aaif-backup` is an operational agent skill designed to generate immutable, timestamped local snapshots of Google Drive files and community operational spreadsheets, such as chapter intake and tracker sheets[^evt-community-events-file-f922f666d0ff-e2dbe3f7]. The skill ensures data integrity and operational resilience by preventing in-place overwrites and segregating backup state from public repository trees[^evt-community-events-file-f922f666d0ff-e2dbe3f7][^evt-community-events-file-a54ff182c7e8-2d5d5bf6].

The skill functions across both developer Git checkouts and installed agent harnesses, adapting storage targets according to runtime environment capabilities to ensure backups survive plugin updates[^evt-community-events-file-f922f666d0ff-e2dbe3f7].

# Architecture / Specification
The backup execution pipeline adheres to strict directory structures and isolation policies[^evt-community-events-file-f922f666d0ff-e2dbe3f7]:

- **Snapshot File Layout**: Backups are persisted chronologically using an immutable folder structure:
  ```
  backups/<slug>/<UTC-timestamp>.<ext>
  ```
  Every execution writes a new timestamped file (e.g., `backups/aaif-community-intake-ops/2026-07-03T142530Z.xlsx`), ensuring that a directory listing reflects a complete, unmodifiable version history[^evt-community-events-file-f922f666d0ff-e2dbe3f7].
- **Environment Storage Routing**: In local development checkouts, snapshots are written to the local `backups/` directory, which is git-ignored to prevent inadvertent committing of organizer or attendee data[^evt-community-events-file-f922f666d0ff-e2dbe3f7][^evt-community-events-file-a54ff182c7e8-2d5d5bf6]. In installed plugin environments (such as [Goose](../resources/goose.md) or Claude Desktop), files are written to system-level application storage (e.g., `~/Library/Application Support/AAIF/backups/` on macOS) to guarantee persistence across plugin updates[^evt-community-events-file-f922f666d0ff-e2dbe3f7].
- **Invocation & CLI Interface**: The backup routine is invoked via Python scripts targeting either the default intake sheet, a specific Google Drive file ID, or a local file path:
  ```bash
  python3 <toolkit>/skills/aaif-backup/scripts/backup.py [target]
  ```
- **Manual Restoration Protocol**: Restoration is strictly manual and non-destructive. Operators copy specific row values or cell data back from snapshots into live sheets rather than overwriting target files, preserving complex formulas, role tabs, and conditional formatting[^evt-community-events-file-f922f666d0ff-e2dbe3f7].

# Lifecycle History
Authored as part of the `aaif/community-events` operational tooling, `aaif-backup` implements library-independent data directory helpers to maintain compatibility with standalone zip distributions and pinned tests[^evt-community-events-file-a54ff182c7e8-2d5d5bf6][^evt-community-events-file-f922f666d0ff-e2dbe3f7].

[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
[^evt-community-events-file-f922f666d0ff-e2dbe3f7]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/backups/README.md
