---
type: skill
title: AAIF Backup Skill
description: Immutable snapshot and local backup skill protecting operational Google
  Workspace files and local data artifacts across agent execution environments.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/backups/README.md
tags:
- skills
- backup
- data-protection
- google-workspace
- operations
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T11:01:50.430523+00:00'
sources:
- id: evt-community-events-file-f922f666d0ff-e2dbe3f7
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/backups/README.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview

The AAIF Backup skill (`aaif-backup`) provides automated, immutable point-in-time snapshotting of mission-critical Google Workspace sheets and local operational files across chapter workflows.[^evt-community-events-file-f922f666d0ff-e2dbe3f7] Designed to prevent irreversible data loss during programmatic mutations, the skill preserves version histories in dedicated local storage while keeping binary artifacts excluded from version control systems.[^evt-community-events-file-f922f666d0ff-e2dbe3f7]

# Architecture / Specification

## Snapshot Layout and Storage Locations

Snapshots are generated as append-only, timestamped files formatted as `backups/<slug>/<UTC-timestamp>.<ext>` (for example, `backups/aaif-community-intake-ops/2026-07-03T142530Z.xlsx`).[^evt-community-events-file-f922f666d0ff-e2dbe3f7] Storage location adapts to the runtime context:[^evt-community-events-file-f922f666d0ff-e2dbe3f7]
- **Local Checkouts**: Preserved in the repository's git-ignored `backups/` directory.
- **Installed Plugins**: When executed inside host clients such as Goose or Claude Desktop, snapshots are routed to `~/Library/Application Support/AAIF/backups/` on macOS, ensuring snapshots survive plugin upgrades without cluttering operator working directories.

## Execution and Ingestion

Backups are executed via CLI invocation targeting either default community sheets (such as the Community Intake Ops sheet) or arbitrary Google Drive file identifiers and local spreadsheets.[^evt-community-events-file-f922f666d0ff-e2dbe3f7]

## Restoration Protocol

Restoration operations are strictly manual and deliberate.[^evt-community-events-file-f922f666d0ff-e2dbe3f7] Rather than overwriting whole files—which risks breaking embedded formulas and conditional formatting on role tabs—operators copy data values back from historical snapshots into live sheets.[^evt-community-events-file-f922f666d0ff-e2dbe3f7]

# References

- [Agent Plugin Portability Guidelines](../guidelines/agent-plugin-portability.md)
- [AAIF Attendee Reminder Skill](./aaif-attendee-reminder.md)
- [Proposal Execution Split Pattern](../patterns/proposal-execution-split.md)

[^evt-community-events-file-f922f666d0ff-e2dbe3f7]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/backups/README.md
