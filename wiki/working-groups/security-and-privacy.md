---
type: working-group
title: Security and Privacy Working Group
description: Technical working group establishing open threat models, defensive architecture
  patterns, builder best practices, and runtime security standards for agentic systems.
resource: https://github.com/aaif/wg-security-and-privacy/blob/9fdce8acf3b6640e31a08498bcfaa66f53c9c53b/meeting-notes/README.md
tags:
- security
- privacy
- governance
- working-group
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:37:17.639051+00:00'
sources:
- id: evt-wg-security-and-privacy-file-d7a6875f36a3-8b0afa11
  resource: https://github.com/aaif/wg-security-and-privacy/blob/9fdce8acf3b6640e31a08498bcfaa66f53c9c53b/meeting-notes/README.md
  author: Alex Frazer
  last_modified: '2026-11-16T11:50:26-05:00'
- id: evt-wg-security-and-privacy-file-e3f78aaae09b-1f9fb425
  resource: https://github.com/aaif/wg-security-and-privacy/blob/9fdce8acf3b6640e31a08498bcfaa66f53c9c53b/meeting-notes/2026-10-13.md
  author: Alex Frazer
  last_modified: '2026-11-16T11:50:26-05:00'
- id: evt-wg-security-and-privacy-file-faf61688d774-40179adf
  resource: https://github.com/aaif/wg-security-and-privacy/blob/9fdce8acf3b6640e31a08498bcfaa66f53c9c53b/meeting-notes/2026-10-27.md
  author: Alex Frazer
  last_modified: '2026-11-16T11:50:26-05:00'
---

# Overview
The Security and Privacy Working Group is a charter-approved AAIF body focused on establishing vendor-neutral threat modeling methodologies, defensive design patterns, security guidelines, and runtime containment specifications for agentic artificial intelligence [^evt-wg-security-and-privacy-file-d7a6875f36a3-8b0afa11]. The group coordinates cross-cutting security reviews with other working groups and aligns vocabulary with the Foundation's taxonomy workstream [^evt-wg-security-and-privacy-file-d7a6875f36a3-8b0afa11][^evt-wg-security-and-privacy-file-e3f78aaae09b-1f9fb425].

# Architecture / Specification
The working group drives five primary workstreams and deliverables:
- **Threat Modeling**: Completed the [Agentic AI Threat Modeling Gap Analysis](../resources/agentic-ai-threat-modeling-gap-analysis-and-framework-design.md) assessing traditional frameworks against non-deterministic systems, and conducts active modeling incorporating MITRE ATLAS and OWASP standards [^evt-wg-security-and-privacy-file-e3f78aaae09b-1f9fb425].
- **Design Patterns Catalog**: Authors repeatable defensive patterns in the [Security and Privacy Design Patterns Catalog](../resources/security-and-privacy-design-patterns-catalog.md), including [Approval Checkpoints](../patterns/approval-checkpoint.md), [Attested Isolated Runtime](../patterns/attested-isolated-runtime.md), and [Kill Switches](../patterns/kill-switch.md) [^evt-wg-security-and-privacy-file-e3f78aaae09b-1f9fb425].
- **Security Best Practices Guide**: Publishes the [Agentic AI Security Best Practices](../guidelines/agentic-ai-security-best-practices.md) guide, open to external contributions and covering pre-execution hooks, gateway mediation, and sandboxing [^evt-wg-security-and-privacy-file-e3f78aaae09b-1f9fb425].
- **Cross-WG Review Checklist**: Operates the [Cross-WG Security Review Checklist](../guidelines/cross-wg-security-review-checklist.md) with delegates across Commerce, Observability, and Governance workstreams [^evt-wg-security-and-privacy-file-e3f78aaae09b-1f9fb425][^evt-wg-security-and-privacy-file-faf61688d774-40179adf].
- **Attestation & Verification Collaboration**: Coordinates with the [Identity and Trust](../working-groups/identity-and-trust.md) and [Observability and Traceability](../working-groups/observability-and-traceability.md) groups on Merkle tree execution traces and an experimental 90-day attestation pilot [^evt-wg-security-and-privacy-file-faf61688d774-40179adf].

# Lifecycle History
Formed in early 2026 under chair Alex Frazer, the group's charter received formal Technical Committee approval in May 2026 [^evt-wg-security-and-privacy-file-d7a6875f36a3-8b0afa11]. In late 2026, the group delivered its threat modeling gap analysis, published the first release of the security best practices guide, established APAC meeting cadences, and integrated draft control plane specifications [^evt-wg-security-and-privacy-file-d7a6875f36a3-8b0afa11][^evt-wg-security-and-privacy-file-e3f78aaae09b-1f9fb425].

[^evt-wg-security-and-privacy-file-d7a6875f36a3-8b0afa11]: https://github.com/aaif/wg-security-and-privacy/blob/9fdce8acf3b6640e31a08498bcfaa66f53c9c53b/meeting-notes/README.md
[^evt-wg-security-and-privacy-file-e3f78aaae09b-1f9fb425]: https://github.com/aaif/wg-security-and-privacy/blob/9fdce8acf3b6640e31a08498bcfaa66f53c9c53b/meeting-notes/2026-10-13.md
[^evt-wg-security-and-privacy-file-faf61688d774-40179adf]: https://github.com/aaif/wg-security-and-privacy/blob/9fdce8acf3b6640e31a08498bcfaa66f53c9c53b/meeting-notes/2026-10-27.md
