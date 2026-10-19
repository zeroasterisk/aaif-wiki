---
type: resource
title: 'Agentic AI Threat Modeling: Gap Analysis and Framework Design'
description: Comparative threat modeling report evaluating OWASP, MITRE ATLAS, and
  CSA MAESTRO frameworks across eight agentic risk areas to establish foundational
  security baselines.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/deliverables/DRAFT-agentic-ai-threat-modeling-gap-analysis.md
tags:
- security
- threat-modeling
- owasp
- mitre-atlas
- csa-maestro
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:46:05.272520+00:00'
sources:
- id: evt-wg-security-and-privacy-file-bc22580e2387-ad459308
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/deliverables/DRAFT-agentic-ai-threat-modeling-gap-analysis.md
  author: Alex Frazer
  last_modified: '2026-09-30T10:38:42-04:00'
---

# Overview
The Agentic AI Threat Modeling: Gap Analysis and Framework Design report is an authoritative technical analysis produced by the [Security & Privacy Working Group](../working-groups/security-and-privacy.md) to determine whether existing security frameworks adequately address agentic AI threats[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]. Led by Fernando Lucktemberg with co-lead Alon Mazor, the deliverable evaluates established frameworks against agent-specific behaviors to establish where existing taxonomies suffice and where new foundation-led engineering work is required[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].

The report concludes that existing industry frameworks provide adequate classification and technique taxonomies for standard vulnerabilities, recommending that the Foundation adopt them as a baseline rather than inventing a competing taxonomy, while targeting new WG efforts exclusively at verified architectural gaps[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].

# Architecture / Specification

## Tri-Framework Evaluation Methodology
The analysis evaluates security frameworks in combination across three complementary operational perspectives[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]:
1. **Developer Controls (OWASP):** Combines the OWASP Top 10 for LLM Applications with the OWASP Top 10 for Agentic Applications (ASI01–ASI10) to define application-level vulnerability requirements.
2. **SOC and Detection (MITRE ATLAS):** Leverages the adversarial technique taxonomy (`AML.T####` codes, baseline v4.6.0 through v5.4.0) to model multi-stage adversary tactics, red-team techniques, and SIEM detection rules.
3. **Architectural Hardening (CSA MAESTRO):** Uses the seven-layer reference stack (L1 Foundation Models through L7 Agent Ecosystem, intersected by vertical L6 Security and Compliance) to identify layer-specific hardening targets.
4. **Governance Scaffolding:** Evaluates NIST AI RMF 1.0, NIST IR 8596, ISO/IEC 42001:2023, and the CSA AI Controls Matrix v1.0 (243 controls across 18 domains) to provide compliance and governance frameworks.

## Evaluated Threat Domains
The deliverable expands the working group's initial mandate from four to eight distinct agentic risk domains[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]:
- **Memory and context poisoning:** Tampering with persistent agent memory stores or conversational context windows.
- **Multi-agent persuasion:** Adversarial subversion, manipulation, or consensus corruption across autonomous agent networks.
- **Agent sabotage, derailment, and rogue agents:** Behavioral deviation, infinite execution cycles, and unconstrained action execution.
- **Tool invocation risk:** Exploitation of protocol boundaries, command injection, and untrusted execution via tool calling.
- **Excessive agency and blast radius containment:** Inadequate boundary enforcement resulting in disproportionate privilege and unconfined damage.
- **Delegated authorization boundaries:** Vulnerabilities in cross-boundary credential exchange, deferred to the [Identity and Trust Working Group](../working-groups/identity-and-trust.md).
- **Supply chain integrity:** Compromised models, malicious agent skills, and unverified tool package registries.
- **Commerce and payment-agent risk:** Financial transaction manipulation and autonomous authorization risks, interfacing with the [Agentic Commerce Working Group](../working-groups/agentic-commerce.md).

# Lifecycle History
The report forms Deliverable 2 of the [Security & Privacy Working Group](../working-groups/security-and-privacy.md) five-part roadmap[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]. Its findings serve as a mandatory precondition and baseline for Deliverable 3 (Design Patterns Catalog) and Deliverable 4 ([Agentic AI Security Best Practices Guide](../guidelines/agentic-ai-security-best-practices.md))[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308].

[^evt-wg-security-and-privacy-file-bc22580e2387-ad459308]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/deliverables/DRAFT-agentic-ai-threat-modeling-gap-analysis.md
