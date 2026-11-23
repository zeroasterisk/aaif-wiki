---
type: working-group
title: Identity and Trust Working Group
description: Technical working group establishing vendor-neutral specifications, attestation
  models, and delegated authorization frameworks for AI agents across internal, B2B,
  and B2C interactions.
resource: https://github.com/aaif/wg-identity-and-trust/blob/03635504ad1c4ab99631967b15705bf947f64f1e/reporting/2026-08-report.md
tags:
- identity
- trust
- delegation
- attestation
- working-group
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:31:50.972026+00:00'
sources:
- id: evt-wg-identity-and-trust-file-922f59c26329-928a222f
  resource: https://github.com/aaif/wg-identity-and-trust/blob/03635504ad1c4ab99631967b15705bf947f64f1e/reporting/2026-08-report.md
  author: Dedeoglu
  last_modified: '2026-11-01T20:45:38+01:00'
---

# Overview
The Identity and Trust Working Group is an AAIF technical body defining vendor-neutral frameworks, attestation models, identity primitives, and authorization boundaries for autonomous agents [^evt-wg-identity-and-trust-file-922f59c26329-928a222f]. Co-chaired by Grant Miller (IBM) and Alper Dedeoğlu (SAP SE), the working group focuses on core concepts including agent identity, delegation, action records, and consent receipts across enterprise and open-network boundaries [^evt-wg-identity-and-trust-file-922f59c26329-928a222f].

# Architecture / Specification
The working group organizes its technical deliverables across three dedicated sub-working groups [^evt-wg-identity-and-trust-file-922f59c26329-928a222f]:

- **Taxonomy Sub-WG:** Coordinates with the cross-cutting [Taxonomy and Landscape](../working-groups/taxonomy-and-landscape.md) workstream to formalize definitions for trust, attestation, delegation, and identifiers [^evt-wg-identity-and-trust-file-922f59c26329-928a222f].
- **Reference Architecture Sub-WG:** Adopts a bottom-up, primitive-first strategy that authors foundational primitives—commencing with the agent [identity](../taxonomy/identity.md) primitive—before assembling them into composite reference architectures and runtime profiles [^evt-wg-identity-and-trust-file-922f59c26329-928a222f].
- **Critical Use Cases Sub-WG:** Formulates illustrative agent lifecycle models spanning internal, business-to-business (B2B), and business-to-consumer (B2C) topologies across six lifecycle stages: naming, deployment, delegation, access control, audit/compliance, and retirement/revocation [^evt-wg-identity-and-trust-file-922f59c26329-928a222f].

Core functional requirements established by the working group include verifiable delegation chains, dynamic per-request authorization gates, content-private [action records](../taxonomy/action-record.md) with selective disclosure, and principal-attested credential revocation [^evt-wg-identity-and-trust-file-922f59c26329-928a222f]. The group integrates external industrial architectural patterns into its evaluation pipeline, including NVIDIA's Secure Agent Workspace reference design and Uber's agentic identity model [^evt-wg-identity-and-trust-file-922f59c26329-928a222f].

# References
- [Agent Identity Primitives](../standards/agent-identity-primitives.md)
- [Action Record](../taxonomy/action-record.md)
- [Working Group Lifecycle Policy](../policies/working-group-lifecycle-policy.md)

[^evt-wg-identity-and-trust-file-922f59c26329-928a222f]: https://github.com/aaif/wg-identity-and-trust/blob/03635504ad1c4ab99631967b15705bf947f64f1e/reporting/2026-08-report.md
