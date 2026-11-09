---
type: guideline
title: Working Group Reporting Template Guideline
description: Standardized reporting template, filing conventions, and required evidence
  sections for AAIF working groups reporting monthly to the Technical Committee.
resource: https://github.com/aaif/working-group-chairs/blob/64a22a2d76dbf349c074cbba3e22d4a509a85e6e/skills/aaif-wg-monthly-report/template.md
tags:
- guideline
- governance
- reporting
- technical-committee
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:26:49.475987+00:00'
sources:
- id: evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2
  resource: https://github.com/aaif/working-group-chairs/blob/64a22a2d76dbf349c074cbba3e22d4a509a85e6e/skills/aaif-wg-monthly-report/template.md
  author: Alex Frazer
  last_modified: '2026-10-26T11:07:46-04:00'
- id: evt-working-group-chairs-file-b41d2241e043-0366462a
  resource: https://github.com/aaif/working-group-chairs/blob/64a22a2d76dbf349c074cbba3e22d4a509a85e6e/skills/aaif-wg-monthly-report/SKILL.md
  author: Alex Frazer
  last_modified: '2026-10-26T11:07:46-04:00'
---

# Overview
The Working Group Reporting Template defines the canonical document structure and submission protocol for monthly status reports submitted by AAIF working groups to the [Technical Committee](../governance/technical-committee.md) [^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2]. Maintained in the `aaif/working-group-chairs` repository and executed via [aaif-wg-monthly-report](../skills/aaif-wg-monthly-report.md), this format ensures asynchronous scannability and verifiable progress tracking across foundation workstreams [^evt-working-group-chairs-file-b41d2241e043-0366462a].

# Architecture / Specification
Reports must be saved to `reporting/YYYY-MM-report.md` (e.g., `reporting/2026-06-report.md`) and submitted via pull request titled `[Report] <YYYY-MM>` with the `monthly-report` label [^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2]. Reports are due on the final business day of the reporting month, initiating a 7-calendar-day TC review window [^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2].

## Required Schema Sections
- **Frontmatter Metadata**: Captures working group name, reporting period, chair names with affiliations, and submission date [^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2].
- **Summary**: A concise 2–3 sentence executive synopsis [^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2].
- **Progress Against Objectives**: Concrete deliverables tied to charter goals, prior month commitments, or tracked KPIs [^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2].
- **Ecosystem Highlights**: External cross-group engagements such as OWASP, AARM, or MCP [^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2].
- **Blockers and Risks**: Identified impediments with associated impact, dependencies, and owners [^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2].
- **Decisions Needed from the TC**: Explicit, actionable requests with deadlines and recommended motions [^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2].
- **Next Month's Focus**: Top 2–3 prioritized objectives [^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2].
- **Metrics / Links**: Verified URLs to merged PRs, releases, issues, and dashboard milestones [^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2].

# Lifecycle History
- **Standardized**: Merged into `aaif/working-group-chairs` as the authoritative template under `skills/aaif-wg-monthly-report/template.md` [^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2].

[^evt-working-group-chairs-file-b41d2241e043-0366462a]: https://github.com/aaif/working-group-chairs/blob/64a22a2d76dbf349c074cbba3e22d4a509a85e6e/skills/aaif-wg-monthly-report/SKILL.md
[^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2]: https://github.com/aaif/working-group-chairs/blob/64a22a2d76dbf349c074cbba3e22d4a509a85e6e/skills/aaif-wg-monthly-report/template.md
