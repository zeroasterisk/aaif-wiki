---
type: skill
title: AAIF Working Group Monthly Report Skill
description: Progressively disclosed agent skill synthesizing monthly meeting notes,
  GitHub repository activity, and prior reports into TC status documents.
resource: https://github.com/aaif/working-group-chairs/pull/2
tags:
- governance
- reporting
- working-groups
- skills
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:50:53.998977+00:00'
sources:
- id: evt-working-group-chairs-pr-2
  resource: https://github.com/aaif/working-group-chairs/pull/2
  author: awfrazer
  last_modified: '2026-10-07T07:34:57+00:00'
---

# Overview
The AAIF Working Group Monthly Report skill (`aaif-wg-monthly-report`) is an agent skill that automates drafting monthly progress reports for the [Technical Committee](../governance/technical-committee.md)[^evt-working-group-chairs-pr-2]. Generalized from workflows developed in the [Security & Privacy Working Group](../working-groups/security-and-privacy.md), the skill synthesizes repository event telemetry and meeting records into structured governance deliverables[^evt-working-group-chairs-pr-2].

# Architecture / Specification
## Input Signal Aggregation
The agent ingests three distinct inputs to assemble a monthly progress record[^evt-working-group-chairs-pr-2]:
- **Monthly Meeting Notes**: Parses all meeting notes generated during the target calendar month.
- **Repository Telemetry**: Analyzes GitHub activity across the working group repository, tracking merged pull requests, new issues, and community contributions.
- **Preceding TC Report**: References the prior month's report to track milestone continuity, recurring initiatives, and deliverable status.

## Generation and Review Workflow
- **Target Location**: Outputs the draft directly to `reporting/YYYY-MM-report.md` matching the structure specified by the [Working Group Reporting Template](../guidelines/working-group-reporting-template.md)[^evt-working-group-chairs-pr-2].
- **Human Supervision**: Working group chairs review the generated draft, adapt domain-specific ecosystem highlights, and submit the final document as a pull request[^evt-working-group-chairs-pr-2].
- **Execution Packaging**: Packaged as a discrete folder containing `SKILL.md` and `template.md` that loads into agent environments (such as `~/.cursor/skills/` or `~/.claude/skills/`) only upon explicit naming[^evt-working-group-chairs-pr-2].

# Lifecycle History
Proposed in PR #2 of the `aaif/working-group-chairs` repository to standardize monthly reporting operations across foundation leadership[^evt-working-group-chairs-pr-2].

[^evt-working-group-chairs-pr-2]: https://github.com/aaif/working-group-chairs/pull/2
