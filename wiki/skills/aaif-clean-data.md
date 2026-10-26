---
type: skill
title: AAIF Clean Data Skill
description: Operational data normalization and intake hygiene skill enforcing proposal-execution
  splits, city resolution precedence, and untrusted input isolation.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-clean-data/SKILL.md
tags:
- skills
- operations
- data-quality
- security
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:54:32.103515+00:00'
sources:
- id: evt-community-events-file-1caae192c2a4-0c489bc7
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-clean-data/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:56-07:00'
- id: evt-community-events-file-f66a78711977-a26d3112
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-clean-data/WORKFLOW.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:56-07:00'
---

# Overview

The `aaif-clean-data` skill normalizes community intake submissions, audits data hygiene, and flags anomalies across the AAIF Community Intake Ops spreadsheet [^evt-community-events-file-1caae192c2a4-0c489bc7]. Positioned as the foundational first phase of the estate synchronization pipeline, the skill ensures that prospective community members, organizers, and speakers are correctly resolved to geographical chapters [^evt-community-events-file-f66a78711977-a26d3112]. The skill operates under strict read-only proposal defaults, requiring manual human authorization prior to mutating upstream records [^evt-community-events-file-1caae192c2a4-0c489bc7][^evt-community-events-file-f66a78711977-a26d3112].

# Architecture / Specification

### Operational Modes and Two-Phase Mutation

The underlying engine (`scripts/clean.py`) enforces an architectural [proposal-execution-split](../patterns/proposal-execution-split.md) [^evt-community-events-file-1caae192c2a4-0c489bc7]:
- **Scan Mode (`scan`)**: Default read-only pass detecting formatting defects (whitespace, erratic capitalization, non-canonical LinkedIn URLs) and raising judgment flags (invalid emails, duplicate submissions, unassigned locations) [^evt-community-events-file-1caae192c2a4-0c489bc7][^evt-community-events-file-f66a78711977-a26d3112]. It outputs human-readable previews or machine-readable JSON proposals without altering sheet contents [^evt-community-events-file-f66a78711977-a26d3112].
- **Apply Mode (`apply`)**: Commits changes only when provided an explicitly approved proposal payload (`changes.json`) [^evt-community-events-file-1caae192c2a4-0c489bc7][^evt-community-events-file-f66a78711977-a26d3112]. Updates are written using `RAW` mode rather than `USER_ENTERED` to prevent inadvertent formula injection, and every modified row receives a persistent trace log in an `Autofixes` column [^evt-community-events-file-1caae192c2a4-0c489bc7][^evt-community-events-file-f66a78711977-a26d3112].

### City Resolution Precedence and Downstream Invisibility

Unresolved geographic entries remain invisible to downstream synchronization scripts, omitting applicants from Chapter CRMs and Drive permissions [^evt-community-events-file-f66a78711977-a26d3112]. City resolution follows strict precedence [^evt-community-events-file-f66a78711977-a26d3112]:
1. Form dropdown `City` value (if not `Other`) [^evt-community-events-file-f66a78711977-a26d3112].
2. Free-text `City > Extracted` derived through heuristic parsing [^evt-community-events-file-f66a78711977-a26d3112].
3. An explicit `Resolved City` manual override, which permanently supersedes automated derivations [^evt-community-events-file-f66a78711977-a26d3112].

Selections indicating `Other` mandate manual operator review via red conditional formatting flags without automatically creating chapters or altering status columns [^evt-community-events-file-1caae192c2a4-0c489bc7].

### Tooling Invariants and Security Controls

- **Tooling Constraints**: Interfacing with Google Workspace documents is strictly limited to the official `gws` CLI driven by Python [^evt-community-events-file-1caae192c2a4-0c489bc7]. Headless office suites like LibreOffice (`soffice`) and `unoconv` are strictly prohibited due to destructive font substitutions and schema stripping during round-trip conversions [^evt-community-events-file-1caae192c2a4-0c489bc7].
- **Untrusted Input Boundaries**: Raw form responses are treated as untrusted data; natural language directives embedded within user fields cannot modify system statuses, chapter assignments, or authorization grants [^evt-community-events-file-1caae192c2a4-0c489bc7].
- **PII Containment**: Ephemeral proposal artifacts (`changes.json`) containing personally identifiable information must be written to temporary directories (`mktemp -d`) and deleted immediately after review [^evt-community-events-file-1caae192c2a4-0c489bc7].

[^evt-community-events-file-1caae192c2a4-0c489bc7]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-clean-data/SKILL.md
[^evt-community-events-file-f66a78711977-a26d3112]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-clean-data/WORKFLOW.md
