---
type: working-group
title: Identity and Trust Working Group
description: Technical working group defining vendor-neutral standards, delegation
  frameworks, and verification taxonomies for agent identity and authorization.
resource: https://github.com/aaif/wg-identity-and-trust/issues/22
tags:
- working-group
- identity
- trust
- delegation
- aaif
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:29:37.606945+00:00'
sources:
- id: evt-wg-identity-and-trust-issue-22
  resource: https://github.com/aaif/wg-identity-and-trust/issues/22
  author: MarcMolas
  last_modified: '2026-10-31T22:24:55+00:00'
---

# Overview

The Identity and Trust Working Group is an AAIF technical body establishing vendor-neutral standards, delegation architectures, and verification criteria for autonomous agents, human principals, and interacting services.[^evt-wg-identity-and-trust-issue-22] Its work addresses foundational security primitives, including cryptographic agent identity, multi-hop delegation chains, time-of-use verification, and cascading credential revocation across organizational trust boundaries.[^evt-wg-identity-and-trust-issue-22]

# Architecture / Specification

The working group's Reference Architecture v1 standardizes core operational rules governing agentic authority:[^evt-wg-identity-and-trust-issue-22]

- **Time-of-Use Verification**: Mandatory validation of five essential grant elements at the moment of execution rather than relying on self-reported agent assertions.[^evt-wg-identity-and-trust-issue-22]
- **Separation of Chains**: Structural separation between delegation chains (authorizing specific capabilities) and accountability chains (resolving liability to a verifiable [principal](../taxonomy/principal.md)).[^evt-wg-identity-and-trust-issue-22]
- **Hop Attenuation**: Monotonic narrowing of permissions across multi-hop delegation paths, preventing authority amplification.[^evt-wg-identity-and-trust-issue-22]
- **Cascading Revocation**: Time-bounded propagation of revocation events from root authorities through all derived downstream grants.[^evt-wg-identity-and-trust-issue-22]
- **Privacy-Preserving Accountability**: Relying-party verification that an accountable principal exists at a designated assurance level without exposing the intermediate delegation topology.[^evt-wg-identity-and-trust-issue-22]

To validate implementations against these invariants, the working group is developing [Delegated-Authority Conformance Cases](../guidelines/delegated-authority-conformance-cases.md) mandating explicit residual disclosure for unaddressed edge cases.[^evt-wg-identity-and-trust-issue-22]

# Lifecycle History

- **2026-10-21**: Published Identity and Trust Reference Architecture v1 establishing normative delegation and revocation invariants.[^evt-wg-identity-and-trust-issue-22]
- **2026-10-31**: Advanced eight delegated-authority conformance evaluation cases with residual disclosure requirements for addition as an architectural appendix.[^evt-wg-identity-and-trust-issue-22]

[^evt-wg-identity-and-trust-issue-22]: https://github.com/aaif/wg-identity-and-trust/issues/22
