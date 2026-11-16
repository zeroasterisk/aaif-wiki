---
type: skill
title: AAIF Backup Skill
description: Operational backup skill generating immutable, timestamped snapshots
  of community estate sheets and local operational files.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/backups/README.md
tags:
- skills
- operations
- backup
- data-protection
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:33:25.457551+00:00'
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
The `aaif-backup` skill creates automated, immutable, timestamped snapshots of critical operational artifacts across Google Drive and local file systems [^evt-community-events-file-f922f666d0ff-e2dbe3f7]. It protects primary estate registers—such as the Community Intake Ops sheet—against accidental corruption or unrecoverable agent edits while strictly keeping sensitive binary exports out of public version control [^evt-community-events-file-f922f666d0ff-e2dbe3f7][^evt-community-events-file-a54ff182c7e8-2d5d5bf6].

# Architecture / Specification
The backup skill enforces strict storage segregation, naming conventions, and non-destructive recovery workflows:

- **Snapshot Directory Layout**: Snapshots follow a standardized path structure: `backups/<slug>/<UTC-timestamp>.<ext>` (for example, `backups/aaif-community-intake-ops/2026-07-03T142530Z.xlsx`) [^evt-community-events-file-f922f666d0ff-e2dbe3f7]. Each execution appends a new file without overwriting prior captures, establishing an audit-ready chronological version history [^evt-community-events-file-f922f666d0ff-e2dbe3f7].
- **Environment-Aware Storage Routing**: When run in a git checkout, snapshots are written to the repository's `backups/` directory, which is completely git-ignored except for documentation [^evt-community-events-file-f922f666d0ff-e2dbe3f7]. When executed from an installed plugin harness (such as Goose or Claude Desktop), snapshots automatically route to `~/Library/Application Support/AAIF/backups/` on macOS to persist across plugin version upgrades [^evt-community-events-file-f922f666d0ff-e2dbe3f7].
- **Execution Interfaces**: The underlying runner `backup.py` supports defaulting to the central Intake Ops spreadsheet or accepting arbitrary target file parameters:
  ```bash
  # Default: AAIF Community Intake Ops sheet
  python3 <toolkit>/skills/aaif-backup/scripts/backup.py

  # Arbitrary Drive file ID or local file path
  python3 <toolkit>/skills/aaif-backup/scripts/backup.py <driveFileId>
  python3 <toolkit>/skills/aaif-backup/scripts/backup.py ./path/to/file.xlsx
  ```
  [^evt-community-events-file-f922f666d0ff-e2dbe3f7]
- **Safe Restore Protocol**: Restoration is intentionally manual and non-destructive. Operators copy raw cell values back from exported snapshots rather than overwriting sheets entirely, preventing the destruction of operational formulas and conditional formatting [^evt-community-events-file-f922f666d0ff-e2dbe3f7].

# Lifecycle History
To safeguard privacy across public repositories, binary snapshot files (`.xlsx`, `.docx`, `.pptx`) are banned from source tracking via gitignore filters, and data directory isolation was introduced to prevent accidental mutations inside user workspaces [^evt-community-events-file-a54ff182c7e8-2d5d5bf6][^evt-community-events-file-f922f666d0ff-e2dbe3f7].

# References
- [Agent Plugin Portability Guidelines](../guidelines/agent-plugin-portability.md)
- [Community Event Operations](../skills/community-event-operations.md)

[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
[^evt-community-events-file-f922f666d0ff-e2dbe3f7]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/backups/README.md
