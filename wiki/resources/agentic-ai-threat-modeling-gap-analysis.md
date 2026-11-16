---
type: resource
title: Agentic AI Threat Modeling Gap Analysis
description: Comparative gap analysis evaluating traditional cybersecurity methodologies,
  CSA MAESTRO, OWASP, and NIST AI RMF against agentic AI threat vectors.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/2026-09-report.md
tags:
- security
- threat-modeling
- risk-assessment
- resource
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:29:55.745427+00:00'
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
The Agentic AI Threat Modeling Gap Analysis is an evaluative study produced by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) assessing standard cybersecurity frameworks against unique agentic AI threat surfaces.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]

Led by Alon Mazor and Fernando Lucktemberg, the resource evaluates OWASP, MITRE ATLAS, CSA MAESTRO, and the NIST AI Risk Management Framework across eight agentic threat domains to establish baseline taxonomy and focus areas for new threat models.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]

# Architecture / Specification
The gap analysis structures threat modeling around eight agentic threat areas, recommending that AAIF adopt established industry frameworks as classification baselines while focusing novel working group efforts on agent-specific failure points:
- Autonomous goal divergence and intent drift
- Non-deterministic tool use and chaining vulnerabilities
- Multi-agent coordination and identity spoofing
- Environment feedback manipulation and unobserved side-effects

# Lifecycle History
The deliverable merged into `main` on 2026-09-30 as Draft v0.1 at `deliverables/DRAFT-agentic-ai-threat-modeling-gap-analysis.md` via PR #8.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1] Dedicated threat modeling working sessions were established starting in October 2026 to expand upon identified framework gaps.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]

[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/2026-09-report.md
