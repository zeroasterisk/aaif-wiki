---
type: skill
title: AAIF Working Group Monthly Report Skill
description: Procedural agent skill automating the generation, evidence ledger compilation,
  and submission validation of AAIF working group monthly reports to the Technical
  Committee.
resource: https://github.com/aaif/working-group-chairs/blob/64a22a2d76dbf349c074cbba3e22d4a509a85e6e/skills/aaif-wg-monthly-report/SKILL.md
tags:
- skill
- governance
- reporting
- automation
- technical-committee
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:26:49.475987+00:00'
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
The `aaif-wg-monthly-report` skill automates the compilation of evidence-backed monthly progress reports submitted by working group chairs to the [Technical Committee](../governance/technical-committee.md) [^evt-working-group-chairs-file-b41d2241e043-0366462a]. The skill executes locally within working group repositories, assembling an audit ledger from GitHub pull requests, issues, releases, and meeting notes, and formats the output to `reporting/YYYY-MM-report.md` adhering to [working-group-reporting-template](../guidelines/working-group-reporting-template.md) [^evt-working-group-chairs-file-b41d2241e043-0366462a].

# Architecture / Specification
The skill enforces a five-stage operational workflow [^evt-working-group-chairs-file-b41d2241e043-0366462a]:
1. **Contract Establishment**: Resolves the working group identity, reporting period, local templates (`reporting/TEMPLATE.md`), and authoritative Technical Committee reporting constraints.
2. **Evidence Ledger Compilation**: Queries GitHub via CLI (`gh pr list`, `gh issue list`, `gh release list`) and reads meeting notes to extract verified achievements, dates, outcomes, and objective alignments [^evt-working-group-chairs-file-b41d2241e043-0366462a].
3. **Report Drafting**: Generates standard sections including Summary, Progress Against Objectives, Ecosystem Highlights, Blockers and Risks, Decisions Needed from the TC, Next Month's Focus, and Metrics / Links [^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2].
4. **Validation**: Verifies that every assertion links to durable evidence, confirms calendar date boundaries, ensures TC decisions carry actionable recommendations, and checks PR title and file path conventions [^evt-working-group-chairs-file-b41d2241e043-0366462a].
5. **Handoff**: Delivers the completed report draft and pull request instructions to the working group chair for review and submission [^evt-working-group-chairs-file-b41d2241e043-0366462a].

# Lifecycle History
- **Authoritative Definition**: Consolidated in `aaif/working-group-chairs` under `skills/aaif-wg-monthly-report/SKILL.md` alongside the canonical `template.md` [^evt-working-group-chairs-file-b41d2241e043-0366462a] [^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2].

[^evt-working-group-chairs-file-b41d2241e043-0366462a]: https://github.com/aaif/working-group-chairs/blob/64a22a2d76dbf349c074cbba3e22d4a509a85e6e/skills/aaif-wg-monthly-report/SKILL.md
[^evt-working-group-chairs-file-f863c50ea9a7-ebe3d9f2]: https://github.com/aaif/working-group-chairs/blob/64a22a2d76dbf349c074cbba3e22d4a509a85e6e/skills/aaif-wg-monthly-report/template.md
