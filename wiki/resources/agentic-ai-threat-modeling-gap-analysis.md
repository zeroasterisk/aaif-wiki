---
type: resource
title: Agentic AI Threat Modeling Gap Analysis
description: Comparative gap analysis evaluating OWASP, MITRE ATLAS, CSA MAESTRO,
  and NIST AI RMF across eight agentic threat dimensions.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/2026-09-report.md
tags:
- security
- threat-modeling
- resource
- gap-analysis
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:19:16.159967+00:00'
sources:
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
The Agentic AI Threat Modeling Gap Analysis is a technical deliverable produced by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) evaluating existing cybersecurity and AI safety frameworks against the specific risks posed by agentic AI.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1] Authored by Alon Mazor and Fernando Lucktemberg, it establishes the empirical justification for targeted threat modeling initiatives across the foundation.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]

# Architecture / Specification
The document evaluates four prominent frameworks—OWASP, MITRE ATLAS, CSA MAESTRO, and the NIST AI Risk Management Framework (AI RMF)—across eight agentic threat categories:
- **Classification Baseline**: Recommends establishing existing industry frameworks as the WG's classification foundation rather than authoring redundant baselines.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]
- **Targeted Gap Coverage**: Directs new analytical work toward gaps unique to agentic architectures, including goal manipulation, memory corruption, unconstrained recursive delegation, and runtime tool abuse.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]
- **Session Operationalization**: Serves as the primary reference document for dedicated threat modeling sessions launched in October 2026, interleaved with the best practices track.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]

# Lifecycle History
The gap analysis was finalized and merged on 2026-09-30 via PR #8 as Draft v0.1 at `deliverables/DRAFT-agentic-ai-threat-modeling-gap-analysis.md`.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1][^evt-wg-security-and-privacy-pr-25]

[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/2026-09-report.md
[^evt-wg-security-and-privacy-pr-25]: https://github.com/aaif/wg-security-and-privacy/pull/25
