---
type: assessment
title: 'Agentic AI Threat Modeling: Gap Analysis and Framework Design'
description: Comparative gap analysis evaluating OWASP, MITRE ATLAS, CSA MAESTRO,
  and NIST AI RMF to establish threat modeling foundations for agentic systems.
resource: https://github.com/aaif/wg-security-and-privacy/blob/e757d350133fea0858dda1deec13dbca923b3cf8/deliverables/DRAFT-agentic-ai-threat-modeling-gap-analysis.md
tags:
- security
- threat-modeling
- owasp
- mitre-atlas
- csa-maestro
- gap-analysis
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:20:29.655867+00:00'
sources:
- id: evt-wg-security-and-privacy-file-bc22580e2387-ad459308
  resource: https://github.com/aaif/wg-security-and-privacy/blob/e757d350133fea0858dda1deec13dbca923b3cf8/deliverables/DRAFT-agentic-ai-threat-modeling-gap-analysis.md
  author: Alex Frazer
  last_modified: '2026-09-30T10:38:42-04:00'
- id: evt-wg-security-and-privacy-file-a9e41c531556-11747157
  resource: https://github.com/aaif/wg-security-and-privacy/blob/e757d350133fea0858dda1deec13dbca923b3cf8/deliverables/README.md
  author: Alex Frazer
  last_modified: '2026-09-30T10:38:42-04:00'
---

# Overview
*Agentic AI Threat Modeling: Gap Analysis and Framework Design* (Deliverable 2 of 5 of the [Security and Privacy Working Group](../working-groups/security-and-privacy.md)) evaluates existing AI threat modeling frameworks to determine whether they adequately address threats unique to autonomous AI agents [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]. Led by Fernando Lucktemberg and Alon Mazor, the report assesses whether existing industry standards provide adequate developer-facing classifications, SOC-facing adversarial technique taxonomies, and architectural layer models [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].

The assessment concludes that existing frameworks provide an adequate baseline classification, recommending that AAIF adopt them rather than author a duplicative taxonomy, while focusing new WG efforts on specific evidenced voids [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].

# Architecture / Specification
The report evaluates framework coverage across eight primary agentic risk categories [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]:

## Evaluated Frameworks
- **OWASP:** LLM Top 10 and OWASP Top 10 for Agentic Applications 2026 (`ASI01`–`ASI10`) providing developer-facing control requirements [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].
- **MITRE ATLAS:** Adversarial threat matrix (v4.6.0 baseline with 14 agentic techniques, plus v5.3/v5.4 refinements) providing SOC detection rules and red-team technique mappings [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].
- **CSA MAESTRO:** Seven-layer reference architecture (L1 Foundation Models through L7 Agent Ecosystem, with L6 Security and Compliance spanning vertically) providing layer-based hardening budget guidance [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].
- **Governance Standards:** NIST AI RMF 1.0, NIST IR 8596 Cyber AI Profile, ISO/IEC 42001:2023, and CSA AI Controls Matrix v1.0 [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].

## Evaluated Threat Domains & Findings
1. **Memory and Context Poisoning:** Evaluating persistent state corruption across session contexts [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].
2. **Multi-Agent Persuasion:** Collusion, deceptive coordination, and cascading manipulation in multi-agent swarms [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].
3. **Agent Sabotage, Derailment, and Rogue Agents:** Unintended goal drift and adversarial goal hijacking [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].
4. **Tool Invocation Risk:** Protocol-level security flaws, prompt injection via tool descriptions, and unauthorized RPC invocation [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].
5. **Excessive Agency and Blast Radius Containment:** Unbounded autonomy without architectural fences or approval checkpoints [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].
6. **Delegated Authorization Boundaries:** Token delegation and identity propagation across downstream tools (coordinated with [Identity and Trust](../working-groups/identity-and-trust.md)) [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].
7. **Supply Chain Integrity:** Model provenance, tool manifest verification, and skill integrity [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].
8. **Commerce and Payment-Agent Risk:** Autonomous financial execution, wallet delegation, and transaction limits [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].

# Lifecycle History
- **2026-09-30:** Merged as Draft v0.1 Deliverable 2 of 5 for the Security & Privacy Working Group [^evt-wg-security-and-privacy-file-a9e41c531556-11747157] [^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].

[^evt-wg-security-and-privacy-file-a9e41c531556-11747157]: https://github.com/aaif/wg-security-and-privacy/blob/e757d350133fea0858dda1deec13dbca923b3cf8/deliverables/README.md
[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]: https://github.com/aaif/wg-security-and-privacy/blob/e757d350133fea0858dda1deec13dbca923b3cf8/deliverables/DRAFT-agentic-ai-threat-modeling-gap-analysis.md
