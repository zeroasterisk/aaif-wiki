---
type: guideline
title: Community Event Operations
description: Operational standards, privacy controls, deterministic tooling rules,
  and credential isolation governing AAIF community events.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-clean-data/SKILL.md
tags:
- community
- operations
- events
- data-hygiene
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:26:44.766525+00:00'
sources:
- id: evt-community-events-file-1caae192c2a4-183bf153
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-clean-data/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-02T11:26:22-07:00'
- id: evt-community-events-file-06572a96a58d-e7b73b4b
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/CHANGELOG.md
  author: Rahul Parundekar
  last_modified: '2026-10-02T11:47:27-07:00'
- id: evt-community-events-file-f66a78711977-144b4f32
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-clean-data/WORKFLOW.md
  author: Rahul Parundekar
  last_modified: '2026-10-02T11:47:27-07:00'
---

# Overview
Operational guidelines governing community intake workflows, chapter synchronization, and Drive estate maintenance across the Agentic AI Foundation [^evt-community-events-file-1caae192c2a4-183bf153].

# Architecture / Specification

## Intake Data Cleaning and Proposals
- **Proposal-First Clean Workflow**: Automation must scan and propose normalization diffs (`clean.py scan`) and require explicit operator approval prior to mutating intake sheets (`clean.py apply`) [^evt-community-events-file-1caae192c2a4-183bf153].
- **Format & Value Rules**: Writes must use `RAW` cell values rather than `USER_ENTERED` to prevent formula injection. Values are matched strictly by header name [^evt-community-events-file-1caae192c2a4-183bf153].
- **PII Containment**: Local intermediate files like `changes.json` containing PII must remain gitignored and be deleted post-run [^evt-community-events-file-1caae192c2a4-183bf153, ^evt-community-events-file-f66a78711977-144b4f32].
- **Review Flags**: Unresolved or `Other` city inputs trigger formatting review flags (`chapter-flags`) rather than silent creation or deletion of chapters [^evt-community-events-file-06572a96a58d-e7b73b4b].

## Non-Idempotent Drive Operations
- Non-idempotent operations (such as folder creation or file copying via `gws`) must disable blind multi-try loops (`NO_RETRY`) to avoid duplicate directory trees and stranding template clones [^evt-community-events-file-06572a96a58d-e7b73b4b].
- Native Google Workspace formats (`application/vnd.google-apps.*`) must be processed via native APIs rather than desktop conversion tools like LibreOffice to preserve typography and layout integrity [^evt-community-events-file-1caae192c2a4-183bf153].

[^evt-community-events-file-06572a96a58d-e7b73b4b]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/CHANGELOG.md
[^evt-community-events-file-1caae192c2a4-183bf153]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-clean-data/SKILL.md
