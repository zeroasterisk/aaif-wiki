---
type: skill
title: AAIF Clean Data Skill
description: Operational intake data hygiene and normalization skill executing read-only
  scanning, diff-based proposals, and gated writes across community estate spreadsheets.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-clean-data/WORKFLOW.md
tags:
- community
- operations
- intake
- data-hygiene
- skills
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:21:20.246093+00:00'
sources:
- id: evt-community-events-file-f66a78711977-a26d3112
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-clean-data/WORKFLOW.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:56-07:00'
- id: evt-community-events-file-06572a96a58d-9d2d11f7
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/CHANGELOG.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview
`aaif-clean-data` is an automated data normalization and intake hygiene skill for the AAIF community events estate, functioning as Phase 1 of the broader `aaif-sync` pipeline to sanitize incoming chapter and organizer submissions before downstream processing[^evt-community-events-file-f66a78711977-a26d3112]. It operates under an explicit [proposal-execution split](../patterns/proposal-execution-split.md) by running read-only issue detection, generating structured before-and-after diffs, and committing modifications only upon operator approval[^evt-community-events-file-f66a78711977-a26d3112].

# Architecture / Specification
The skill interacts with the central community intake sheet through the `gws` command-line interface driven by Python scripts, adhering to native Google Workspace formats or atomic OOXML manipulation while banning desktop office suites like LibreOffice to prevent font degradation and XML schema stripping[^evt-community-events-file-f66a78711977-a26d3112].

### Operational Modes
1. **Scan (`clean.py scan`)**: Default read-only mode detecting formatting anomalies, canonicalizing LinkedIn URLs, collapsing irregular whitespace, and flagging unresolved records such as `City="Other"`, duplicate emails, or missing names[^evt-community-events-file-f66a78711977-a26d3112].
2. **Apply (`clean.py apply`)**: Gated execution mode consuming an approved `changes.json` payload, applying modifications directly to the source `Form Responses` tab by header name, and logging row-level audit trails in an `Autofixes` column[^evt-community-events-file-f66a78711977-a26d3112].
3. **Chapter Flags (`clean.py chapter-flags`)**: Formats submitted `Other` city cells with red highlights across role tabs to visually surface rows requiring chapter triage without mutating values or granting automated permissions[^evt-community-events-file-06572a96a58d-9d2d11f7].

### Estate Sync Dependency
Because downstream pipeline stages (such as CRM synchronization, Chapters List population, and Google Drive access provisioning) resolve chapters through extracted city records, unresolved cities become invisible omissions rather than explicit errors[^evt-community-events-file-f66a78711977-a26d3112]. `aaif-clean-data` serves as the intake gate guaranteeing all applicants are resolved into their respective roles (`Organizers`, `Hosts`, `Speakers`, `Collaborators`)[^evt-community-events-file-f66a78711977-a26d3112][^evt-community-events-file-06572a96a58d-9d2d11f7].

[^evt-community-events-file-06572a96a58d-9d2d11f7]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/CHANGELOG.md
[^evt-community-events-file-f66a78711977-a26d3112]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-clean-data/WORKFLOW.md
