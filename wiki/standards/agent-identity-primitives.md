---
type: standard
title: Agent Identity Primitives
description: Draft foundational specification defining attestation models, accountability
  structures, revocability, and identity standards for autonomous agents.
resource: https://github.com/aaif/wg-identity-and-trust/issues/26
tags:
- identity
- attestation
- revocation
- standards
- trust
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:44:14.647197+00:00'
sources:
- id: evt-wg-identity-and-trust-issue-26
  resource: https://github.com/aaif/wg-identity-and-trust/issues/26
  author: tejaduggaraju
  last_modified: '2026-11-12T00:46:14+00:00'
- id: evt-wg-identity-and-trust-issue-27
  resource: https://github.com/aaif/wg-identity-and-trust/issues/27
  author: tejaduggaraju
  last_modified: '2026-11-12T00:36:49+00:00'
- id: evt-wg-identity-and-trust-issue-28
  resource: https://github.com/aaif/wg-identity-and-trust/issues/28
  author: tejaduggaraju
  last_modified: '2026-11-12T00:42:56+00:00'
---

# Overview
The Agent Identity Primitives draft specification (v0.1) defines foundational identity, attestation, accountability, and revocation requirements tailored specifically to autonomous AI agents [^evt-wg-identity-and-trust-issue-26] [^evt-wg-identity-and-trust-issue-27]. Developed under the [Identity and Trust Working Group](../working-groups/identity-and-trust.md), the standard addresses structural shortcomings in legacy workload and human identity standards that fail under long, dynamic, and autonomous agent delegation chains [^evt-wg-identity-and-trust-issue-28].

# Architecture / Specification
The draft specification establishes four core structural domains:
- **Agent Differentiation and Risk Amplification**: Section 1.1 highlights why agents exacerbate traditional identity gaps, citing longer delegation chains, dynamic runtime path selection, high operational autonomy without human-in-the-loop oversight, and unpredictable resource access [^evt-wg-identity-and-trust-issue-28].
- **Accountability and Delegation**: Section 3.2 structures accountability chains across principals, responsible parties, upstream authorities, and intermediate subagents [^evt-wg-identity-and-trust-issue-27].
- **Attestation Framework**: Section 3.4 outlines six core attestation types: identity, provenance, software, environment/hardware, approval, and intervention [^evt-wg-identity-and-trust-issue-26]. Identity attestation serves as the minimum requirement for authentication, while working group discussions evaluate how provenance, software, and hardware measurements should compose pre-issuance evidence [^evt-wg-identity-and-trust-issue-26].
- **Revocability and Cross-Domain Gaps**: Section 3.6 defines revocation triggers by principals, providers, and upstream accountable parties [^evt-wg-identity-and-trust-issue-27]. Section 4 documents nine standards interoperability gaps, including cross-domain revocation propagation and RFC 8693 nested token limitations [^evt-wg-identity-and-trust-issue-27] [^evt-wg-identity-and-trust-issue-28].

# References
- WG Identity and Trust Issue #26 [^evt-wg-identity-and-trust-issue-26]
- WG Identity and Trust Issue #27 [^evt-wg-identity-and-trust-issue-27]
- WG Identity and Trust Issue #28 [^evt-wg-identity-and-trust-issue-28]

[^evt-wg-identity-and-trust-issue-26]: https://github.com/aaif/wg-identity-and-trust/issues/26
[^evt-wg-identity-and-trust-issue-27]: https://github.com/aaif/wg-identity-and-trust/issues/27
[^evt-wg-identity-and-trust-issue-28]: https://github.com/aaif/wg-identity-and-trust/issues/28
