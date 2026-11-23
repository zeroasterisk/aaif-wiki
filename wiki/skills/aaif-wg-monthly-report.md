---
type: skill
title: AAIF Working Group Monthly Report Generation Skill
description: Modular operational skill generating evidence-based monthly working group
  status reports aligned with charter milestones, KPIs, risks, and Technical Committee
  review requirements.
resource: https://github.com/aaif/working-group-chairs/pull/1
tags:
- skills
- operations
- reporting
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:23:39.129324+00:00'
sources:
- id: evt-working-group-chairs-pr-1
  resource: https://github.com/aaif/working-group-chairs/pull/1
  author: 91pavan
  last_modified: '2026-10-12T09:43:40+00:00'
---

# Overview
The AAIF Working Group Monthly Report Generation Skill is a reusable operational agent skill that automates the generation of evidence-based monthly progress reports across Agentic AI Foundation working groups [^evt-working-group-chairs-pr-1]. It synthesizes project activity and milestone deliveries into standardized reporting records for evaluation by the Technical Committee [^evt-working-group-chairs-pr-1].

# Architecture / Specification
The reporting skill standardizes monthly operational reporting across multiple dimensions [^evt-working-group-chairs-pr-1]:
- **Charter Alignment**: Validates activities against declared working group charter objectives, scheduled delivery milestones, key performance indicators (KPIs), and historical commitments [^evt-working-group-chairs-pr-1].
- **Variance and Risk Detection**: Systematically identifies and documents material variances from roadmaps, emerging blockers, and items requiring explicit governance intervention [^evt-working-group-chairs-pr-1].
- **Asynchronous Governance Review**: Structures outputs to facilitate asynchronous reviews, voting requests, and decision tracking by the [Technical Committee](../governance/technical-committee.md) [^evt-working-group-chairs-pr-1].
- **Format Preservation**: Respects each repository's local file conventions and the [working group reporting template](../guidelines/working-group-reporting-template.md) structure without breaking existing publication pipelines [^evt-working-group-chairs-pr-1].

[^evt-working-group-chairs-pr-1]: https://github.com/aaif/working-group-chairs/pull/1
