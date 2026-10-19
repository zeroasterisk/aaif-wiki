---
type: working-group
title: Agentic Commerce Working Group
description: Technical working group defining commerce capabilities, payment protocol
  boundaries, dispute accountability, and transaction evidence architecture across
  autonomous agents.
resource: https://github.com/aaif/wg-agentic-commerce/issues/5
tags:
- working-group
- commerce
- payments
- evidence
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:00:39.514262+00:00'
sources:
- id: evt-wg-agentic-commerce-issue-5
  resource: https://github.com/aaif/wg-agentic-commerce/issues/5
  author: narko4u
  last_modified: '2026-10-08T04:12:43+00:00'
- id: evt-ws-taxonomy-landscape-pr-75
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/75
  author: galesky-a
  last_modified: '2026-10-07T15:58:53+00:00'
---

# Overview
The Agentic Commerce Working Group establishes vendor-neutral standards, capability maps, and protocol boundaries governing autonomous financial transactions, checkout handoffs, and post-purchase accountability. The group defines how agent identity, user delegation, and transaction execution are bound and audited across merchant and payment domains [^evt-wg-agentic-commerce-issue-5].

# Architecture / Specification

## Capability Map and Post-Purchase Accountability
The working group organizes agentic commerce workflows across lifecycle phases, standardizing cross-boundary evidence requirements for dispute resolution and auditability [^evt-wg-agentic-commerce-issue-5]:
- **Evidence Binding**: Tamper-evident receipts and audit trails binding delegation identifiers, transaction IDs, agent credentials, shopper identities, and signed claims [^evt-wg-agentic-commerce-issue-5].
- **Signal Provenance**: Clear attribution distinguishing self-reported agent assertions from independently observed markers across platforms, merchants, and payment providers [^evt-wg-agentic-commerce-issue-5].
- **Authorization Strength for State Changes**: Verified evidence requirements separating order observation from state-changing post-purchase remedies such as returns, cancellations, or refunds [^evt-wg-agentic-commerce-issue-5].
- **Auditability**: Post-purchase retention bundles enabling relying parties to independently verify authorizations and replay dispute trails [^evt-wg-agentic-commerce-issue-5].

## Bounded Verification Verdict Envelope
To standardize verification results across merchant and payment platforms without renegotiating transaction state, the group evaluates an eight-field machine-readable contract [^evt-wg-agentic-commerce-issue-5]:
1. `verdict`: Three-state classification (`supported`, `contradicted`, or `unresolvable`) [^evt-wg-agentic-commerce-issue-5].
2. `verifier`: Identity of the computing verification entity, distinct from the claim producer [^evt-wg-agentic-commerce-issue-5].
3. `verifier_signature`: Cryptographic signature over the verdict and canonical hashes [^evt-wg-agentic-commerce-issue-5].
4. `evidence_refs`: Explicit delegation, transaction, and consent identifiers [^evt-wg-agentic-commerce-issue-5].
5. `evidence_fingerprints`: Canonical hashes (RFC 8785) supporting deterministic verification replay [^evt-wg-agentic-commerce-issue-5].
6. `verification_basis`: Specification of rule sets and checks evaluated [^evt-wg-agentic-commerce-issue-5].
7. `witness_scope`: Explicit boundary coverage of what the verdict attests [^evt-wg-agentic-commerce-issue-5].
8. `timestamp`: Freshness timestamp of verdict evaluation [^evt-wg-agentic-commerce-issue-5].

## Terminology Alignment
The group collaborates with the taxonomy workstream to standardize terms including Agentic commerce protocols across payment layers [^evt-ws-taxonomy-landscape-pr-75].

# References
- Reconciliation model: [../taxonomy/three-state-reconciliation.md](../taxonomy/three-state-reconciliation.md)
- Observability and trace coordination: [../working-groups/observability-and-traceability.md](../working-groups/observability-and-traceability.md)
- Identity delegation: [../working-groups/identity-and-trust.md](../working-groups/identity-and-trust.md)

[^evt-wg-agentic-commerce-issue-5]: https://github.com/aaif/wg-agentic-commerce/issues/5
[^evt-ws-taxonomy-landscape-pr-75]: https://github.com/aaif/ws-taxonomy-landscape/pull/75
