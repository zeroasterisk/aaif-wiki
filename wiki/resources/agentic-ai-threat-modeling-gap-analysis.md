---
type: resource
title: Agentic AI Threat Modeling Gap Analysis
description: Comparative gap analysis evaluating OWASP, MITRE ATLAS, CSA MAESTRO,
  and NIST AI RMF across eight agentic threat domains to establish AAIF framework
  baselines.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/threat-modeling/README.md
tags:
- threat-modeling
- security
- gap-analysis
- owasp
- mitre-atlas
- csa-maestro
- nist-ai-rmf
- wg-security-and-privacy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:10:49.513667+00:00'
sources:
- id: evt-wg-security-and-privacy-file-0e2b23067e13-ece26d85
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/threat-modeling/README.md
  author: Alex Frazer
  last_modified: '2026-09-30T10:38:42-04:00'
- id: evt-wg-security-and-privacy-file-a9e41c531556-11747157
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/deliverables/README.md
  author: Alex Frazer
  last_modified: '2026-09-30T10:38:42-04:00'
- id: evt-wg-security-and-privacy-file-bc22580e2387-ad459308
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/deliverables/DRAFT-agentic-ai-threat-modeling-gap-analysis.md
  author: Alex Frazer
  last_modified: '2026-09-30T10:38:42-04:00'
---

# Overview
The *Agentic AI Threat Modeling: Gap Analysis and Framework Design* (Deliverable 2 of the Security and Privacy Working Group) evaluates existing artificial intelligence threat modeling frameworks to determine whether they adequately address threats unique to autonomous and multi-agent systems[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]. Led by Fernando Lucktemberg (SAP) and co-led by Alon Mazor (Ocean Security), the analysis serves as the architectural foundation for downstream working group deliverables, including the Design Patterns Catalog (D3) and the [Security Best Practices Guide](../guidelines/agentic-ai-security-best-practices.md) (D4)[^evt-wg-security-and-privacy-file-0e2b23067e13-ece26d85][^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].

The study evaluated major baseline frameworks—principally OWASP Top 10 for Agentic Applications (ASI01–ASI10), MITRE ATLAS v4.6.0–v5.4.0, CSA MAESTRO, and NIST AI RMF—across eight threat domains: memory and context poisoning, multi-agent persuasion, agent sabotage/derailment/rogue agents, tool invocation risk, excessive agency and blast radius containment, delegated authorization boundaries, supply chain integrity, and commerce and payment-agent risk[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].

# Architecture / Specification

## Evaluation Methodology
The gap analysis establishes that no single existing security framework comprehensively addresses all three requirements of an agentic security program[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]:
1. **Developer Controls (OWASP):** Categorizing failure modes and developer-actionable controls via the OWASP Top 10 for LLM Applications and OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10)[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].
2. **SOC and Adversary Techniques (MITRE ATLAS):** Modeling concrete adversary actions across a structured attack lifecycle via `AML.T####` techniques, while lacking vocabulary for non-adversarial systemic failures[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].
3. **Architectural Hardening Layers (CSA MAESTRO):** Allocating defense budgets across an L1–L7 stack where L6 (Security and Compliance) spans horizontally across foundation models, data, memory, tool, and ecosystem layers[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].
4. **Governance Scaffolding:** Provided by NIST AI RMF 1.0 (Govern-Map-Measure-Manage), ISO/IEC 42001, and the CSA AI Controls Matrix v1.0[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].

## Core Findings and Recommendations
The report concludes that existing industry frameworks jointly provide adequate vulnerability classification and adversary technique coding, advising the AAIF against building a competing threat taxonomy[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]. However, the report identifies distinct voids requiring specific treatment[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]:
- **Working Group Workstreams:** Five technical and methodological gaps require new AAIF guidance, specifically around multi-agent persuasion dynamics, tool invocation runtime invariants, supply chain verification, memory poisoning defenses, and blast radius containment[^evt-wg-security-and-privacy-file-0e2b23067e13-ece26d85][^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].
- **Cross-WG Delegations:** Architectural gaps in delegated authorization boundaries are handed off to the [Identity and Trust Working Group](../working-groups/identity-and-trust.md), while commerce and payment-agent risks are coordinated with the [Agentic Commerce Working Group](../working-groups/agentic-commerce.md)[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].
- **Jurisdictional Boundaries:** Agent derailment and non-adversarial failure modes surface an unresolved boundary between adversarial security and operational robustness under the [Accuracy and Reliability Working Group](../working-groups/accuracy-and-reliability.md)[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].

# Lifecycle History
The deliverable was chartered as Deliverable 2 of the [Security and Privacy Working Group](../working-groups/security-and-privacy.md)[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]. Draft v0.1 was submitted for working group review under the leadership of Fernando Lucktemberg and Alon Mazor, establishing the baseline framework for the Design Patterns Catalog and Best Practices Guide[^evt-wg-security-and-privacy-file-0e2b23067e13-ece26d85][^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].

[^evt-wg-security-and-privacy-file-0e2b23067e13-ece26d85]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/threat-modeling/README.md
[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/deliverables/DRAFT-agentic-ai-threat-modeling-gap-analysis.md
