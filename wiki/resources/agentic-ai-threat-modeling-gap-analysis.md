---
type: resource
title: 'Agentic AI Threat Modeling: Gap Analysis and Framework Design'
description: Working group deliverable evaluating OWASP, MITRE ATLAS, CSA MAESTRO,
  and NIST AI RMF against eight agentic threat areas to guide new security framework
  development.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/deliverables/DRAFT-agentic-ai-threat-modeling-gap-analysis.md
tags:
- security
- threat-modeling
- owasp
- mitre-atlas
- maestro
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:13:12.203172+00:00'
sources:
- id: evt-wg-security-and-privacy-file-bc22580e2387-ad459308
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/deliverables/DRAFT-agentic-ai-threat-modeling-gap-analysis.md
  author: Alex Frazer
  last_modified: '2026-09-30T10:38:42-04:00'
- id: evt-wg-security-and-privacy-file-0e2b23067e13-ece26d85
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/threat-modeling/README.md
  author: Alex Frazer
  last_modified: '2026-09-30T10:38:42-04:00'
- id: evt-wg-security-and-privacy-file-a9e41c531556-11747157
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/deliverables/README.md
  author: Alex Frazer
  last_modified: '2026-09-30T10:38:42-04:00'
---

# Overview

The Agentic AI Threat Modeling Gap Analysis and Framework Design is an authoritative technical report (Deliverable 2) produced by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md).[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308] Led by Fernando Lucktemberg (SAP) and Alon Mazor (Ocean Security), the report evaluates whether existing AI security frameworks—specifically OWASP, MITRE ATLAS, Cloud Security Alliance (CSA) MAESTRO, and NIST AI RMF—adequately cover threats unique to agentic AI systems.[^evt-wg-security-and-privacy-file-0e2b23067e13-ece26d85] [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]

The report concludes that while existing frameworks jointly provide adequate threat classification and adversarial technique coding, critical architectural and operational voids persist across five technical areas, requiring dedicated AAIF guidance rather than redundant baseline taxonomy work.[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]

# Architecture / Specification

The gap analysis combines three complementary framework perspectives to evaluate coverage across the system lifecycle:[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]

- **OWASP (Developer Controls):** Combines the OWASP Top 10 for LLM Applications with the OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10) to assess developer-facing risk categories.[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]
- **MITRE ATLAS (SOC Detection):** Employs the ATLAS matrix (v4.6.0 through v5.4.0) to evaluate security operations center detection rules and adversary attack techniques (AML.T codes).[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]
- **CSA MAESTRO (Architectural Hardening):** Evaluates threat placement across MAESTRO's seven-layer reference stack (L1 Foundation Models through L7 Agent Ecosystem, with L6 Security and Compliance as a cross-cutting vertical).[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]
- **Supplementary Governance:** References NIST AI RMF 1.0, NIST IR 8596 Cyber AI Profile, ISO/IEC 42001:2023, and the CSA AI Controls Matrix v1.0 for risk management framing.[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]

The analysis evaluates eight distinct agentic threat categories:[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]
1. Memory and context poisoning
2. Multi-agent persuasion and collusion
3. Agent sabotage, derailment, and rogue agent behavior
4. Tool invocation risks and protocol-level vulnerabilities
5. Excessive agency and blast radius containment
6. Delegated authorization boundaries (jurisdiction formally designated to the [Identity and Trust Working Group](../working-groups/identity-and-trust.md))
7. Supply chain integrity (prompts, tool manifests, and models)
8. Commerce and payment-agent risks

# Lifecycle History

The deliverable mandate was established during initial working group sessions in spring 2026.[^evt-wg-security-and-privacy-file-d7a6875f36a3-5484c59b] Workstream leads published draft revisions during July and August 2026, culminating in Draft v0.1 submitted for formal working group review in late September 2026.[^evt-wg-security-and-privacy-file-d7a6875f36a3-5484c59b] [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308] Its findings directly inform the scope of the [Security and Privacy Design Patterns Catalog](./security-and-privacy-design-patterns-catalog.md) and the [Agentic AI Security Best Practices Guide](../guidelines/agentic-ai-security-best-practices.md).[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]

# References

- Report Source: [DRAFT-agentic-ai-threat-modeling-gap-analysis.md](https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/deliverables/DRAFT-agentic-ai-threat-modeling-gap-analysis.md)
- Threat Modeling Workstream: [aaif/wg-security-and-privacy workstreams/threat-modeling](https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/threat-modeling/README.md)

[^evt-wg-security-and-privacy-file-0e2b23067e13-ece26d85]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/threat-modeling/README.md
[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/deliverables/DRAFT-agentic-ai-threat-modeling-gap-analysis.md
