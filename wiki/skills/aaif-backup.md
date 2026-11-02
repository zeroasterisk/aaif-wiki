---
type: skill
title: AAIF Backup Skill
description: Operational backup skill generating immutable, timestamped local snapshots
  of Google Drive and local files prior to mutating edits.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-backup/SKILL.md
tags:
- operations
- community-events
- backup
- google-workspace
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:21:58.155291+00:00'
sources:
- id: evt-community-events-file-91fd6707275c-36b98c09
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-backup/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:56-07:00'
---

# Overview

The `aaif-backup` skill is an operational utility within the AAIF community events toolkit that generates immutable, timestamped local snapshots of critical operations data—such as the Community Intake Ops sheet or arbitrary Google Drive and local files—prior to executing destructive or risky mutations.[^evt-community-events-file-91fd6707275c-36b98c09]

# Architecture / Specification

## Execution and Engine
The skill is powered by the `scripts/backup.py` engine and accepts an optional Google Drive file ID or local file path as an argument.[^evt-community-events-file-91fd6707275c-36b98c09] By default, it exports the AAIF Community Intake Ops sheet into `.xlsx` format.[^evt-community-events-file-91fd6707275c-36b98c09]

## Storage Conventions
Every invocation creates a new immutable file without overwriting prior snapshots, establishing a verifiable version history for differential auditing or manual rollback.[^evt-community-events-file-91fd6707275c-36b98c09] Snapshots land using the structured layout:

```
<dest>/<slug>/<UTC-timestamp>.<ext>
```

The destination defaults to the `backups/` directory within the toolkit's data path, configurable via `--dest`.[^evt-community-events-file-91fd6707275c-36b98c09]

## Tooling Rules and Prohibitions
All interactions with Google Drive files are strictly governed by the Google Workspace (`gws`) CLI driven by Python.[^evt-community-events-file-91fd6707275c-36b98c09] Native Google formats (`application/vnd.google-apps.*`) must be modified directly through Google APIs rather than round-tripping through converted Office documents.[^evt-community-events-file-91fd6707275c-36b98c09] Headless desktop office converters like LibreOffice (`soffice`) and `unoconv` are strictly prohibited due to font substitutions and lossy OOXML rendering.[^evt-community-events-file-91fd6707275c-36b98c09]

Prerequisite authentication for `gws` is validated using [aaif-check-setup](aaif-check-setup.md).[^evt-community-events-file-91fd6707275c-36b98c09]

[^evt-community-events-file-91fd6707275c-36b98c09]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-backup/SKILL.md
