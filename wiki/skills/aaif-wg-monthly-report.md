---
type: skill
title: AAIF Working Group Monthly Report Generator
description: Modular agent skill aggregating monthly working group notes, GitHub activity,
  and previous reports into evidence-based governance updates for Technical Committee
  review.
resource: https://github.com/aaif/working-group-chairs/pull/1
tags:
- skill
- reporting
- governance
- working-groups
- technical-committee
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:10:42.748405+00:00'
sources:
- id: evt-working-group-chairs-pr-1
  resource: https://github.com/aaif/working-group-chairs/pull/1
  author: 91pavan
  last_modified: '2026-10-12T09:43:40+00:00'
---

# Overview
The AAIF Working Group Monthly Report Generator is an operational agent skill designed to compile monthly activity, meeting notes, git contributions, and milestone progression into standardized, evidence-based status reports.[^evt-working-group-chairs-pr-1] These reports maintain cross-workstream accountability and enable asynchronous evaluation by the [Technical Committee](../governance/technical-committee.md) and governing board.[^evt-working-group-chairs-pr-1]

# Architecture / Specification
The reporting skill standardizes monthly compilation while adhering to repository-specific frontmatter and formatting templates:[^evt-working-group-chairs-pr-1]
- **Charter and KPI Alignment**: Correlates month-over-month deliverables against charter mandates, official milestones, and explicit performance indicators.
- **Variance and Risk Tracking**: Identifies material schedule slips, unresolved design disagreements, and governance escalations requiring committee resolution.
- **Asynchronous Governance Integration**: Formats updates into an auditable ledger optimized for non-blocking Technical Committee inspection.
- **Template Preservation**: Retains each repository's localized documentation layout, markdown headers, and publication directory paths.

# References
- Working Group Chairs repository skill contribution: https://github.com/aaif/working-group-chairs/pull/1 [^evt-working-group-chairs-pr-1]

[^evt-working-group-chairs-pr-1]: https://github.com/aaif/working-group-chairs/pull/1
