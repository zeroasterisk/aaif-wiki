---
type: skill
title: aaif-backup
description: Operational backup skill generating immutable, timestamped snapshots
  of AAIF Google Drive and local files prior to state mutations.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-backup/SKILL.md
tags:
- skills
- operations
- backups
- community-events
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:22:46.900652+00:00'
sources:
- id: evt-community-events-file-91fd6707275c-36b98c09
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-backup/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:56-07:00'
---

# Overview
`aaif-backup` is an operational agent skill designed to capture versioned, immutable snapshots of critical AAIF operational data prior to high-risk administrative mutations.[^evt-community-events-file-91fd6707275c-36b98c09] By default, it targets the AAIF Community Intake Ops spreadsheet, writing point-in-time archives to local storage without overwriting past backups.[^evt-community-events-file-91fd6707275c-36b98c09]

# Architecture / Specification
- **Immutable Versioning**: Every snapshot is saved under `<dest>/<slug>/<UTC-timestamp>.<ext>`, ensuring a non-destructive audit history for diffing or rolling back records.[^evt-community-events-file-91fd6707275c-36b98c09] Existing backups are never overwritten.
- **Drive and Local Target Support**: The skill accepts local files directly or Google Drive file IDs. Google Drive native files are exported to standardized Office formats (`application/vnd.google-apps.spreadsheet` to `.xlsx`, Docs to `.docx`, Slides to `.pptx`).[^evt-community-events-file-91fd6707275c-36b98c09]
- **Tooling Constraints**: Drive file operations must strictly utilize the `gws` CLI driven by Python; headless document converters like LibreOffice or `soffice` are banned to preserve native OOXML parts and brand typography.[^evt-community-events-file-91fd6707275c-36b98c09]
- **Pre-execution Verification**: Remote backups require authenticated Google Workspace sessions validated via `gws`, verified before execution alongside [AAIF Check Setup](../skills/aaif-check-setup.md).[^evt-community-events-file-91fd6707275c-36b98c09]

Related operational patterns include [Clean Data](../skills/aaif-clean-data.md) and [Community Event Operations](../skills/community-event-operations.md).

[^evt-community-events-file-91fd6707275c-36b98c09]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-backup/SKILL.md
