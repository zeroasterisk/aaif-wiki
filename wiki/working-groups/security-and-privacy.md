---
type: working-group
title: Security and Privacy Working Group
description: Technical working group establishing threat modeling frameworks, security
  design patterns, cross-working-group review checklists, and actionable security
  best practices for agentic AI.
resource: https://github.com/aaif/wg-security-and-privacy/pull/43
tags:
- governance
- security
- privacy
- working-group
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:39:42.950330+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-43
  resource: https://github.com/aaif/wg-security-and-privacy/pull/43
  author: awfrazer
  last_modified: '2026-10-30T16:49:49+00:00'
---

# Overview

The Security and Privacy Working Group (WG) defines threat models, defensive architecture patterns, runtime isolation baselines, and cross-cutting security evaluation checklists across the Agentic AI Foundation ecosystem [^evt-wg-security-and-privacy-pr-43]. Its scope covers vulnerabilities unique to agentic autonomous execution, context boundaries, dynamic tool discovery, and multi-agent delegation.

# Architecture / Specification

The working group manages several primary workstreams and shared deliverables:

- **Security Best Practices Guide**: Concrete builder guidance maintained in `guidelines/agentic-ai-security-best-practices.md`, covering context sanitization, credential containment, and sandbox parameters [^evt-wg-security-and-privacy-pr-43].
- **Threat Modeling Framework**: Following initial gap analysis work in `resources/agentic-ai-threat-modeling-gap-analysis.md`, the WG's threat modeling methodology extends STRIDE and PASTA methodologies with agent-specific matrices from MITRE ATLAS and OWASP ASI [^evt-wg-security-and-privacy-pr-43].
- **Security Design Patterns Catalog**: Reusable implementation blueprints documented in `resources/security-and-privacy-design-patterns-catalog.md`, including containment and revocation mechanisms such as `../patterns/kill-switch.md` [^evt-wg-security-and-privacy-pr-43].
- **Cross-WG Review Checklist**: Operational review criteria in `guidelines/cross-wg-security-review-checklist.md` applied across foundation working groups, with designated liaisons spanning Observability, Agentic Commerce, and Governance [^evt-wg-security-and-privacy-pr-43].
- **Taxonomy Harmonization**: Security and privacy definitions maintained in cooperation with `../working-groups/taxonomy-and-landscape.md`, formally integrated into the cross-WG taxonomy [^evt-wg-security-and-privacy-pr-43].

# Lifecycle History

Following initial foundation chartering, the WG shipped its initial baseline deliverables in late 2026 and opened external contribution streams for best practices and pattern submissions [^evt-wg-security-and-privacy-pr-43]. The group operates regular global working sessions alongside dedicated APAC timezone meetings [^evt-wg-security-and-privacy-pr-43].

[^evt-wg-security-and-privacy-pr-43]: https://github.com/aaif/wg-security-and-privacy/pull/43
