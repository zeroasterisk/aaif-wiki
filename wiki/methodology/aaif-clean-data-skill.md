---
type: methodology
title: AAIF Clean Data Skill
description: Operational agent skill for scanning, validating, and normalizing intake
  data with diff proposals and provenance logging.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-clean-data/SKILL.md
tags:
- automation
- skill
- operations
- data-quality
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:58:05.942337+00:00'
sources:
- id: evt-community-events-file-1caae192c2a4-9d319720
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-clean-data/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-08-22T00:44:21-07:00'
---

# Overview
The AAIF Clean Data Skill (`aaif-clean-data`) is an operational workflow and automated agent skill for auditing and normalizing community intake data without silent modifications [^evt-community-events-file-1caae192c2a4-9d319720].

# Architecture / Specification
The skill operates via distinct operational modes aligned with the [Human Approval Gate](../patterns/human-approval-gate.md) pattern:
- **Scan Mode**: Evaluates inputs in read-only mode to generate structured diffs for mechanical issues (such as whitespace collapsing, casing corrections, and LinkedIn URL canonicalization) while flagging anomalies like missing names, duplicate emails, or generic city responses [^evt-community-events-file-1caae192c2a4-9d319720].
- **Apply Mode**: Requires explicit human approval before writing validated change sets (`changes.json`) to the source form data [^evt-community-events-file-1caae192c2a4-9d319720]. All cell writes use `RAW` value encoding to prevent formula injection, and every update logs an entry to a dedicated `Autofixes` column for audit provenance [^evt-community-events-file-1caae192c2a4-9d319720].
- **City Normalization**: Extracts structured city and country metadata into an `Extracted City` column while preserving human-verified overrides in `Resolved City` [^evt-community-events-file-1caae192c2a4-9d319720].

[^evt-community-events-file-1caae192c2a4-9d319720]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-clean-data/SKILL.md
