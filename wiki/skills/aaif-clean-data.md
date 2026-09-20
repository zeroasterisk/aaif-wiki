---
type: skill
title: AAIF Clean Data Skill
description: An agent skill for scanning, normalizing, and proposing data quality
  fixes on the AAIF Community Intake Ops sheet.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-clean-data/SKILL.md
tags:
- skills
- operations
- data-cleaning
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:55:28.977530+00:00'
sources:
- id: evt-community-events-file-1caae192c2a4-9d319720
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-clean-data/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-08-22T00:44:21-07:00'
---

# Overview
The `aaif-clean-data` skill is an operational workflow designed to normalize and remediate data quality issues in the AAIF Community Intake Ops spreadsheet while preserving data integrity and audit provenance[^evt-community-events-file-1caae192c2a4-9d319720]. It operates under a proposal-first model, surfacing before-and-after diffs for operator review prior to applying modifications[^evt-community-events-file-1caae192c2a4-9d319720].

Built as an [Agent Skill](../specification/agent-skill.md), it provides automated heuristics for casing normalization, LinkedIn URL canonicalization, and free-text city extraction, paired with human oversight gates[^evt-community-events-file-1caae192c2a4-9d319720].

# Architecture / Specification
The skill provides several execution modes driven by `scripts/clean.py`[^evt-community-events-file-1caae192c2a4-9d319720]:
- **Scan Mode**: A read-only analysis detecting mechanical issues (whitespace trimming, name/city casing, LinkedIn URL formatting) and flagging ambiguous cases (e.g., missing emails, non-profile LinkedIn links, duplicate emails) for human review[^evt-community-events-file-1caae192c2a4-9d319720].
- **Apply Mode**: Applies an explicitly approved batch change file (`changes.json`) to the source `Form Responses` sheet[^evt-community-events-file-1caae192c2a4-9d319720]. Writes are performed using raw cell values rather than user-entered formulas to prevent formula injection, and every modification is logged with a timestamp and change descriptor in an `Autofixes` provenance column[^evt-community-events-file-1caae192c2a4-9d319720].
- **City Resolution**: Extracts canonical city names from free-text form inputs into an `Extracted City` column while respecting operator overrides in a `Resolved City` column[^evt-community-events-file-1caae192c2a4-9d319720].

[^evt-community-events-file-1caae192c2a4-9d319720]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-clean-data/SKILL.md
