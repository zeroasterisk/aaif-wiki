---
type: working-group
title: Identity and Trust Working Group
description: Technical working group defining vendor-neutral standards, reference
  architectures, delegation frameworks, and action verification protocols for agentic
  systems.
resource: https://github.com/aaif/wg-identity-and-trust/blob/03635504ad1c4ab99631967b15705bf947f64f1e/reporting/2026-08-report.md
tags:
- governance
- working-group
- identity
- trust
- delegation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:32:51.084396+00:00'
sources:
- id: evt-wg-identity-and-trust-file-922f59c26329-928a222f
  resource: https://github.com/aaif/wg-identity-and-trust/blob/03635504ad1c4ab99631967b15705bf947f64f1e/reporting/2026-08-report.md
  author: Dedeoglu
  last_modified: '2026-11-01T20:45:38+01:00'
---

# Overview

The Identity and Trust Working Group is an Agentic AI Foundation technical body responsible for defining open standards, architectures, and taxonomies for agent identity, delegation, consent receipts, and verifiable action records [^evt-wg-identity-and-trust-file-922f59c26329-928a222f]. Co-chaired by Grant Miller (IBM) and Alper Dedeoğlu (SAP SE), the working group focuses on establishing verifiable boundaries between principals, agent runtimes, and downstream services [^evt-wg-identity-and-trust-file-922f59c26329-928a222f].

# Architecture / Specification

The working group organizes its technical agenda into three specialized sub-working groups [^evt-wg-identity-and-trust-file-922f59c26329-928a222f]:

- **Taxonomy Sub-WG:** Coordinates with the cross-cutting `../working-groups/taxonomy-and-landscape.md` workstream to standardize formal definitions for trust, attestation, delegation, and identifiers [^evt-wg-identity-and-trust-file-922f59c26329-928a222f].
- **Reference Architecture Sub-WG:** Employs a primitive-first methodology, developing modular core primitives (beginning with the identity primitive draft) that aggregate into concrete use cases and full reference architectures [^evt-wg-identity-and-trust-file-922f59c26329-928a222f].
- **Critical Use Cases Sub-WG:** Formulates end-to-end lifecycle models across Internal, B2B, and B2C operational scopes, spanning agent naming, deployment, delegation, per-request authorization, audit/compliance, and principal-attested revocation [^evt-wg-identity-and-trust-file-922f59c26329-928a222f].

### Functional Requirements & External Inputs

The group evaluates external industry implementations to refine its technical deliverables, including NVIDIA's Secure Agent Workspace reference design and Uber's agentic identity architecture [^evt-wg-identity-and-trust-file-922f59c26329-928a222f]. Key technical requirements under active specification include verifiable delegation hierarchies, dynamic per-request authorization gates, selective disclosure for content-private action records, and tamper-evident revocation mechanics [^evt-wg-identity-and-trust-file-922f59c26329-928a222f].

[^evt-wg-identity-and-trust-file-922f59c26329-928a222f]: https://github.com/aaif/wg-identity-and-trust/blob/03635504ad1c4ab99631967b15705bf947f64f1e/reporting/2026-08-report.md
