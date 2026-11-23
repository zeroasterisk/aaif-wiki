---
type: pattern
title: Kill Switch
description: Architectural control plane pattern establishing an independent out-of-band
  containment loop to halt agent operations, revoke credentials, and prevent cascading
  harm.
resource: https://github.com/aaif/wg-security-and-privacy/blob/9fdce8acf3b6640e31a08498bcfaa66f53c9c53b/meeting-notes/README.md
tags:
- security
- containment
- revocation
- governance
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
The Kill Switch pattern defines an independent out-of-band containment mechanism that interrupts autonomous agent execution, revokes identity credentials, and halts delegated authority across systems to contain anomalous or malicious behavior [^evt-wg-security-and-privacy-file-faf61688d774-40179adf]. Formulated as a core deliverable within the [Security and Privacy Working Group](../working-groups/security-and-privacy.md), the pattern addresses operational containment across both enterprise trust boundaries and open-internet interactions [^evt-wg-security-and-privacy-file-d7a6875f36a3-8b0afa11][^evt-wg-security-and-privacy-file-e3f78aaae09b-1f9fb425].

# Architecture / Specification
The pattern formalizes containment and revocation across several layers of the agent stack:
- **Runtime Interception**: Direct execution halts commanded by local runtime watchdogs, policy decision points, or administrative control surfaces [^evt-wg-security-and-privacy-file-faf61688d774-40179adf].
- **Credential Revocation and Identity Invalidation**: Rapid invalidation of active bearer tokens, delegated session keys, and authority grants [^evt-wg-security-and-privacy-file-faf61688d774-40179adf]. In enterprise contexts, containment relies on centralized Identity Providers (IdPs) and protocols like OpenID Continuous Access Evaluation Profile (CAEP), whereas open-internet and cross-domain architectures explore decentralized ledger state or broadcast status registers to avoid single points of failure and ensure revocation checks remain verifiable during network partitions [^evt-wg-security-and-privacy-file-faf61688d774-40179adf].
- **Cascading Revocation**: Hierarchical revocation mechanisms ensuring that pulling a principal kill switch transitively invalidates subagents, ephemeral execution keys, and delegated subtask mandates spawned during the session [^evt-wg-security-and-privacy-file-faf61688d774-40179adf].
- **Propagation Bounds**: Enforces deterministic upper bounds between revocation publication and universal verifier rejection (e.g., verifying refusal within bounded propagation windows) [^evt-wg-security-and-privacy-file-faf61688d774-40179adf].

# Lifecycle History
Initial draft specifications for the kill switch pattern merged into the [Security and Privacy Design Patterns Catalog](../resources/security-and-privacy-design-patterns-catalog.md) in October 2026 [^evt-wg-security-and-privacy-file-e3f78aaae09b-1f9fb425]. Working group reviews subsequently expanded the pattern to reconcile enterprise CAEP models with open-internet zero-knowledge and distributed credential architectures [^evt-wg-security-and-privacy-file-faf61688d774-40179adf].

[^evt-wg-security-and-privacy-file-d7a6875f36a3-8b0afa11]: https://github.com/aaif/wg-security-and-privacy/blob/9fdce8acf3b6640e31a08498bcfaa66f53c9c53b/meeting-notes/README.md
[^evt-wg-security-and-privacy-file-e3f78aaae09b-1f9fb425]: https://github.com/aaif/wg-security-and-privacy/blob/9fdce8acf3b6640e31a08498bcfaa66f53c9c53b/meeting-notes/2026-10-13.md
[^evt-wg-security-and-privacy-file-faf61688d774-40179adf]: https://github.com/aaif/wg-security-and-privacy/blob/9fdce8acf3b6640e31a08498bcfaa66f53c9c53b/meeting-notes/2026-10-27.md
