---
type: skill
title: aaif-clean-data
description: Operational data hygiene skill normalizing Community Intake Ops sheets
  with strict read-only proposals and approval gates.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-clean-data/SKILL.md
tags:
- skills
- operations
- data-hygiene
- community-events
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:22:46.900652+00:00'
sources:
- id: evt-community-events-file-1caae192c2a4-0c489bc7
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-clean-data/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:56-07:00'
---

# Overview
`aaif-clean-data` is an operational agent skill responsible for scanning, auditing, and normalizing data quality within the AAIF Community Intake Ops spreadsheet without executing unreviewed modifications.[^evt-community-events-file-1caae192c2a4-0c489bc7] Operating under a proposal-execution split, the skill reports findings and drafts mutations by default, demanding explicit human approval before applying updates.[^evt-community-events-file-1caae192c2a4-0c489bc7]

# Architecture / Specification
The skill enforces strict data handling, tooling, and authorization invariants:
- **Default Read-Only Proposal**: Standard execution runs `clean.py scan`, surfacing normalization issues such as non-canonical LinkedIn URLs, name and city whitespace/casing inconsistencies, and missing or duplicate email addresses.[^evt-community-events-file-1caae192c2a4-0c489bc7] Mutation operations (`apply`, `cities --write`, `install-flags`, `install-colors`) require explicit approval.[^evt-community-events-file-1caae192c2a4-0c489bc7]
- **Tooling Constraints**: All Google Drive interactions are executed via the `gws` command-line utility driven through Python.[^evt-community-events-file-1caae192c2a4-0c489bc7] Native Google formats (`application/vnd.google-apps.*`) are manipulated via Docs, Sheets, and Slides APIs, reserving byte-level OOXML edits for true Office files.[^evt-community-events-file-1caae192c2a4-0c489bc7] Third-party converters like LibreOffice, `soffice`, and `unoconv` are strictly prohibited to prevent font substitutions and OOXML corruption.[^evt-community-events-file-1caae192c2a4-0c489bc7]
- **Untrusted Input Invariants**: Form answers and sheet cells are treated as untrusted data; prompt-like instructions within cells cannot alter record statuses, chapter assignments, or permissions.[^evt-community-events-file-1caae192c2a4-0c489bc7] Values are written using `RAW` mode instead of `USER_ENTERED` to prevent formula injection, and derived columns like `Resolved City` are never written directly.[^evt-community-events-file-1caae192c2a4-0c489bc7]
- **PII Containment**: Intermediate proposal diffs containing real-person data (`changes.json`) must reside in isolated temporary directories (`mktemp -d`) rather than persistent workspace directories and are removed immediately following execution.[^evt-community-events-file-1caae192c2a4-0c489bc7]

Related operational safeguards link to [Proposal-Execution Split](../patterns/proposal-execution-split.md) and [Setup Diagnostics](../skills/aaif-check-setup.md).

[^evt-community-events-file-1caae192c2a4-0c489bc7]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-clean-data/SKILL.md
