---
type: skill
title: AAIF WG Monthly Report Skill
description: Modular operational skill generating evidence-based monthly working group
  status reports for Technical Committee review.
resource: https://github.com/aaif/working-group-chairs/blob/64a22a2d76dbf349c074cbba3e22d4a509a85e6e/skills/aaif-wg-monthly-report/SKILL.md
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:37:01.936664+00:00'
sources:
- id: evt-working-group-chairs-file-b41d2241e043-0366462a
  resource: https://github.com/aaif/working-group-chairs/blob/64a22a2d76dbf349c074cbba3e22d4a509a85e6e/skills/aaif-wg-monthly-report/SKILL.md
  author: Alex Frazer
  last_modified: '2026-10-26T11:07:46-04:00'
- id: evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2
  resource: https://github.com/aaif/working-group-chairs/blob/64a22a2d76dbf349c074cbba3e22d4a509a85e6e/skills/aaif-wg-monthly-report/template.md
  author: Alex Frazer
  last_modified: '2026-10-26T11:07:46-04:00'
---

# Overview
The `aaif-wg-monthly-report` skill automates the compilation and authoring of standardized monthly reports submitted by working group chairs to the [Technical Committee](../governance/technical-committee.md)[^evt-working-group-chairs-file-b41d2241e043-0366462a]. The workflow consolidates progress, blockers, risks, and requested committee decisions into `reporting/YYYY-MM-report.md`, ensuring every assertion maps to verifiable repository artifacts and commit history[^evt-working-group-chairs-file-b41d2241e043-0366462a][^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2].

# Architecture / Specification
The skill explicitly disables autonomous model invocation (`disable-model-invocation: true`) to enforce human-in-the-loop validation by working group chairs prior to pull request submission[^evt-working-group-chairs-file-b41d2241e043-0366462a].

## Input Configuration
Execution requires or queries for:
- Working group name as used in official reports.
- Chair names and member organizational affiliations.
- Reporting month (defaulting to the most recently completed calendar month).
- Target GitHub repository path.
- Working group meeting notes for the active reporting period.
- GitHub team handle for TC reviewer assignment[^evt-working-group-chairs-file-b41d2241e043-0366462a].

## Operating Workflow
1. **Contract Validation**: Resolves repository reporting rules against [guidelines/working-group-reporting-template](../guidelines/working-group-reporting-template.md) and verifies local template paths[^evt-working-group-chairs-file-b41d2241e043-0366462a].
2. **Evidence Ledger Compilation**: Queries merged pull requests, closed issues, and published releases using the GitHub CLI within the month's calendar boundaries[^evt-working-group-chairs-file-b41d2241e043-0366462a].
3. **Report Generation**: Populates standard template sections: Summary, Progress Against Objectives, Ecosystem Highlights, Blockers and Risks, Decisions Needed from the TC, Next Month's Focus, and Metrics/Links[^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2].
4. **Hand-Off and Pull Request Submission**: Validates that external statements cite durable artifacts, requires the pull request title `[Report] YYYY-MM`, attaches the `monthly-report` label, and assigns TC reviewers for asynchronous sign-off[^evt-working-group-chairs-file-b41d2241e043-0366462a][^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2].

[^evt-working-group-chairs-file-b41d2241e043-0366462a]: https://github.com/aaif/working-group-chairs/blob/64a22a2d76dbf349c074cbba3e22d4a509a85e6e/skills/aaif-wg-monthly-report/SKILL.md
[^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2]: https://github.com/aaif/working-group-chairs/blob/64a22a2d76dbf349c074cbba3e22d4a509a85e6e/skills/aaif-wg-monthly-report/template.md
