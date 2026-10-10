---
type: working-group
title: Security and Privacy Working Group
description: AAIF technical working group establishing open threat models, security
  best practice guides, and runtime security design patterns for AI agents.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/README.md
tags:
- governance
- working-group
- security
- privacy
- threat-modeling
- patterns
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:23:50.420062+00:00'
sources:
- id: evt-wg-security-and-privacy-file-440eb159591a-c575359e
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/README.md
  author: Alex Frazer
  last_modified: '2026-10-09T08:54:25-06:00'
- id: evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/2026-09-report.md
  author: Alex Frazer
  last_modified: '2026-10-09T08:54:25-06:00'
- id: evt-wg-security-and-privacy-pr-25
  resource: https://github.com/aaif/wg-security-and-privacy/pull/25
  author: awfrazer
  last_modified: '2026-10-09T14:54:26+00:00'
---

# Overview
The Security and Privacy Working Group (WG Security & Privacy) is an Agentic AI Foundation technical body dedicated to establishing comprehensive threat modeling baselines, actionable security best practice guides, and reusable architectural design patterns for autonomous and tool-augmented AI agents[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]. Chaired by Alexander Frazer and Junjie Bu, the group coordinates technical deliverables across threat analysis, developer guidance, static analysis rules, and cross-working-group review checklists[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1][^evt-wg-security-and-privacy-pr-25].

The working group collaborates with other AAIF initiatives, including the [Taxonomy and Landscape Working Group](../working-groups/taxonomy-and-landscape.md) and the [Identity and Trust Working Group](../working-groups/identity-and-trust.md), deferring identity and trust topics while maintaining core threat modeling and security pattern catalogs[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1].

# Architecture / Specification

## Active Workstreams and Deliverables
The working group organizes its technical production into several primary workstreams[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]:

1. **Agentic AI Security Best Practices Guide**: Maintains the foundational [Security Best Practices Guide](../guidelines/agentic-ai-security-best-practices.md) and the companion Security Best Practices Feature Matrix mapping practices to people, process, and technology controls[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1].
2. **Threat Modeling Gap Analysis and Framework Design**: Benchmarks existing frameworks—including OWASP Top 10 for LLMs, MITRE ATLAS, CSA MAESTRO, and NIST AI RMF—across eight agentic threat categories to identify AI-agent-specific risk vectors[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1].
3. **Design Patterns Catalog**: Standardizes reusable security and privacy patterns, including [Approval Checkpoint](../patterns/approval-checkpoint.md), [Kill Switch](../patterns/kill-switch.md), and [Attested Isolated Runtime](../patterns/attested-isolated-runtime.md)[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1].
4. **Cross-WG Review and Taxonomy**: Formulates security and privacy terminology for the unified taxonomy and tracks scope boundaries against other technical working groups[^evt-wg-security-and-privacy-pr-25].

## Governance and Merge Policies
Deliverables within the working group repository undergo formal peer review prior to merging into the `deliverables/` catalog[^evt-wg-security-and-privacy-file-440eb159591a-c575359e]. PR authors do not merge their own pull requests into official deliverables paths, and deliverables operate as living specifications maintained via tracked issues and mandatory designated reviewers[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1][^evt-wg-security-and-privacy-pr-25].

# Lifecycle History
- **2026-06**: Formed workstreams with appointed leads and migrated taxonomy definitions to cross-WG coordination[^evt-wg-security-and-privacy-file-440eb159591a-c575359e].
- **2026-07**: Published initial public PRs for the Threat Modeling Gap Analysis and Best Practices Guide[^evt-wg-security-and-privacy-file-440eb159591a-c575359e].
- **2026-08**: Established open meeting archives and advanced pattern reviews[^evt-wg-security-and-privacy-file-440eb159591a-c575359e].
- **2026-09**: Merged Draft v0.1 of the Threat Modeling Gap Analysis, registered the Security Best Practices Guide and Feature Matrix, landed initial Design Pattern drafts, and instituted deliverables governance rules[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1][^evt-wg-security-and-privacy-pr-25].

[^evt-wg-security-and-privacy-file-440eb159591a-c575359e]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/README.md
[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/2026-09-report.md
[^evt-wg-security-and-privacy-pr-25]: https://github.com/aaif/wg-security-and-privacy/pull/25
