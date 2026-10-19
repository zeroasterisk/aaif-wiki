---
type: working-group
title: Security and Privacy Working Group
description: AAIF technical working group establishing threat models, runtime security
  design patterns, and cross-cutting security best practices for agentic AI systems.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/README.md
tags:
- working-group
- security
- privacy
- threat-modeling
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:02:42.782882+00:00'
sources:
- id: evt-wg-security-and-privacy-file-440eb159591a-c575359e
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/README.md
  author: Alex Frazer
  last_modified: '2026-10-09T08:54:25-06:00'
- id: evt-wg-security-and-privacy-pr-36
  resource: https://github.com/aaif/wg-security-and-privacy/pull/36
  author: MatthewKhouzam
  last_modified: '2026-10-09T14:32:29+00:00'
---

# Overview

The Security and Privacy Working Group is an Agentic AI Foundation (AAIF) technical body chartered to establish comprehensive threat models, runtime security design patterns, and cross-cutting defense guidelines for autonomous agent deployments [^evt-wg-security-and-privacy-file-440eb159591a-c575359e]. Operating under the oversight of the [Technical Committee](../governance/technical-committee.md), the group produces foundational baseline guidance, design pattern catalogs, and threat landscape gap analyses.

# Architecture / Specification

The working group operates across five active workstreams stood up in June 2026 [^evt-wg-security-and-privacy-file-440eb159591a-c575359e]:
- **Threat Modeling**: Produced the [Threat Modeling Gap Analysis](../resources/agentic-ai-threat-modeling-gap-analysis.md), evaluating existing industry frameworks against agentic vulnerabilities and merged as a draft deliverable [^evt-wg-security-and-privacy-file-440eb159591a-c575359e].
- **Best Practices**: Authoring the [Agentic AI Security Best Practices](../guidelines/agentic-ai-security-best-practices.md) guide and the Security Best Practices Feature Matrix [^evt-wg-security-and-privacy-file-440eb159591a-c575359e] [^evt-wg-security-and-privacy-pr-36].
- **Design Patterns Catalog**: Establishing structured architecture patterns including [Attested Isolated Runtime](../patterns/attested-isolated-runtime.md) and [Kill Switch](../patterns/kill-switch.md), landing its initial pattern drafts in late 2026 [^evt-wg-security-and-privacy-file-440eb159591a-c575359e].
- **Taxonomy Alignment**: Coordinating domain-specific security and privacy terms for review and integration into the [Taxonomy and Landscape](../working-groups/taxonomy-and-landscape.md) unified taxonomy [^evt-wg-security-and-privacy-file-440eb159591a-c575359e].
- **Review and Protocols**: Driving review checklists and cross-working group protocol coordination [^evt-wg-security-and-privacy-file-440eb159591a-c575359e].

# Lifecycle History

- **2026-06**: Stood up five workstreams with confirmed leads; transitioned initial taxonomy work into the cross-WG effort [^evt-wg-security-and-privacy-file-440eb159591a-c575359e].
- **2026-07**: Published initial pull requests for the Threat Modeling Gap Analysis and Best Practices Guide; finalized the structural outline of the Design Patterns Catalog [^evt-wg-security-and-privacy-file-440eb159591a-c575359e].
- **2026-08**: Released past meeting recordings publicly, established internal review and PR merge policies, and expanded cross-WG collaboration on shared review checklists [^evt-wg-security-and-privacy-file-440eb159591a-c575359e].
- **2026-09**: Formally merged the Best Practices Guide and Threat Modeling Gap Analysis into `deliverables/`, landed initial four design pattern drafts, merged the Feature Matrix, and introduced alternate-week APAC meetings [^evt-wg-security-and-privacy-file-440eb159591a-c575359e].

[^evt-wg-security-and-privacy-file-440eb159591a-c575359e]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/README.md
[^evt-wg-security-and-privacy-pr-36]: https://github.com/aaif/wg-security-and-privacy/pull/36
