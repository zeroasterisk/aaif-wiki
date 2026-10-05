---
type: skill
title: AAIF Clean Data Automation Skill
description: Standardized automation skill normalizing and verifying data quality
  in the AAIF Community Intake Operations spreadsheet.
resource: https://github.com/aaif/community-events/pull/56
tags:
- community
- operations
- automation
- sheets
- validation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T06:02:04.084757+00:00'
sources:
- id: evt-community-events-pr-56
  resource: https://github.com/aaif/community-events/pull/56
  author: rparundekar
  last_modified: '2026-10-03T00:54:08+00:00'
---

# Overview

The `aaif-clean-data` skill normalizes, validates, and audits data submitted across community intake forms into the AAIF Community Intake Operations spreadsheet [^evt-community-events-pr-56]. It ensures consistent schema conformance, verifies chapter associations, and handles automated formatting checks.

# Architecture / Specification

### Subcommands and Execution Flow
- `clean.py chapter-flags`: Adds conditional formatting rules highlighting cells in red when a submitted city value begins with `Other` (case-insensitive) on `Form Responses` and `City (Existing)` columns in role tabs (`Organizers`, `Hosts`, `Speakers`) [^evt-community-events-pr-56].
- `install-colors`: Installs provenance formatting rules while preserving chapter review flags and distinguishing them from error rules [^evt-community-events-pr-56].
- Preview mode operates in a read-only state by default, identifying whether `--write` would alter sheet state or formula ranges [^evt-community-events-pr-56].

### Invariants
- Formatting rules do not mutate underlying cell values, role formulas, or established chapter assignments [^evt-community-events-pr-56].
- Stored conditional ranges are validated against dynamic sheet row counts to prevent newly appended form submissions from bypassing inspection [^evt-community-events-pr-56].

# References
- [`../skills/aaif-triage-intake.md`](../skills/aaif-triage-intake.md)
- [`../skills/aaif-sync-chapters.md`](../skills/aaif-sync-chapters.md)

[^evt-community-events-pr-56]: https://github.com/aaif/community-events/pull/56
