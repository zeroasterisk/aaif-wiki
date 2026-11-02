---
type: skill
title: AAIF Working Group Monthly Report Generation Skill
description: Reusable agent skill synthesizing monthly working group activity, charter
  objectives, KPIs, and governance variance for Technical Committee review.
resource: https://github.com/aaif/working-group-chairs/pull/1
tags:
- skills
- governance
- reporting
- working-groups
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:23:45.459230+00:00'
sources:
- id: evt-working-group-chairs-pr-1
  resource: https://github.com/aaif/working-group-chairs/pull/1
  author: 91pavan
  last_modified: '2026-10-12T09:43:40+00:00'
---

# Overview
The AAIF Working Group Monthly Report Generation Skill (`aaif-wg-monthly-report`) is an operational agent skill designed to produce structured, evidence-based monthly progress reports across Agentic AI Foundation working groups [^evt-working-group-chairs-pr-1]. It synthesizes monthly meeting notes, repository activity, and governance decisions to support asynchronous review by the [Technical Committee](../governance/technical-committee.md) and governing body [^evt-working-group-chairs-pr-1].

# Architecture / Specification
The skill operates in alignment with the [Working Group Reporting Template](../guidelines/working-group-reporting-template.md) while preserving each working group repository's specific reporting conventions [^evt-working-group-chairs-pr-1].

Key capabilities and evaluation criteria include [^evt-working-group-chairs-pr-1]:
- **Charter Alignment**: Mapping monthly milestones and deliverables directly against charter objectives, key performance indicators (KPIs), and prior commitments.
- **Variance and Risk Tracking**: Highlighting material variances in timelines, scope, or resource availability, and flagging open risks requiring Technical Committee intervention.
- **Governance Tracking**: Documenting formal decisions, votes, and consensus calls taken during working group sessions.
- **Asynchronous Review Enablement**: Formatting summaries to facilitate rapid evaluation by Technical Committee members and cross-working-group stakeholders.

# References
- [Technical Committee](../governance/technical-committee.md)
- [Working Group Reporting Template](../guidelines/working-group-reporting-template.md)

[^evt-working-group-chairs-pr-1]: https://github.com/aaif/working-group-chairs/pull/1
