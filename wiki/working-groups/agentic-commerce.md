---
type: working-group
title: Agentic Commerce Working Group
description: Technical working group establishing capability maps, gap analyses, and
  protocol architectures for autonomous commerce transactions, cross-boundary evidence
  binding, and post-purchase settlement.
resource: https://github.com/aaif/wg-agentic-commerce/issues/5
tags:
- working-group
- commerce
- protocols
- settlement
- evidence
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:18:09.925582+00:00'
sources:
- id: evt-wg-agentic-commerce-issue-5
  resource: https://github.com/aaif/wg-agentic-commerce/issues/5
  author: narko4u
  last_modified: '2026-10-08T04:12:43+00:00'
---

# Overview
The Agentic Commerce Working Group is an AAIF technical working group establishing standardized capability maps, gap analyses, protocol architectures, and audit mechanisms for autonomous agent commerce[^evt-wg-agentic-commerce-issue-5]. The group evaluates interaction standards spanning product discovery, agent-negotiated purchases, payment authorization, and post-purchase accountability across agent, merchant, payment processor, and risk-system boundaries[^evt-wg-agentic-commerce-issue-5].

The working group coordinates cross-cutting concerns with sibling foundation efforts, delegating telemetry and causal audit structures to the [Observability & Traceability Working Group](../working-groups/observability-and-traceability.md) and identity binding and delegation primitives to the [Identity & Trust Working Group](../working-groups/identity-and-trust.md)[^evt-wg-agentic-commerce-issue-5].

# Architecture / Specification

The working group structures its core deliverables around an overarching Capability Map and Gap Analysis, targeting full lifecycle transaction coverage across pre-purchase, point-of-sale, and post-purchase operational phases[^evt-wg-agentic-commerce-issue-5]:

- **Evidence Binding**: Constructing verifiable receipts and audit records that cryptographically bind execution claims to transaction identifiers, agent identities, shopper identities, and delegation scopes to enable deterministic dispute resolution[^evt-wg-agentic-commerce-issue-5].
- **Signal Provenance**: Establishing explicit markers distinguishing self-reported signals from independently observed signals across platforms, payment providers, and merchants[^evt-wg-agentic-commerce-issue-5].
- **Authorization Strength**: Formulating evidentiary thresholds and renewed approval requirements for state-changing remedies, including cancellations, returns, refunds, and disputes[^evt-wg-agentic-commerce-issue-5].
- **Auditability and Verdict Envelopes**: Defining bounded verification results via machine-readable verdict envelopes containing:
  1. `verdict`: Tri-state classification (`supported`, `contradicted`, or `unresolvable`)[^evt-wg-agentic-commerce-issue-5].
  2. `verifier`: Distinct entity identifier computing the classification[^evt-wg-agentic-commerce-issue-5].
  3. `verifier_signature`: Digital signature computed over verdict and evidence fingerprints[^evt-wg-agentic-commerce-issue-5].
  4. `evidence_refs`: Canonical references to transaction, delegation, and consent claims[^evt-wg-agentic-commerce-issue-5].
  5. `evidence_fingerprints`: RFC 8785 canonical hashes ensuring deterministic replay[^evt-wg-agentic-commerce-issue-5].
  6. `verification_basis`: Specification of evaluated policy checks[^evt-wg-agentic-commerce-issue-5].
  7. `witness_scope`: Scope limitations and boundaries of the verification verdict[^evt-wg-agentic-commerce-issue-5].
  8. `timestamp`: Freshness assertion[^evt-wg-agentic-commerce-issue-5].

# Lifecycle History
- **Issue #5**: Proposed capability row and machine-readable verdict envelope contract for post-purchase cross-boundary evidence, auditability, and dispute reconciliation[^evt-wg-agentic-commerce-issue-5].

[^evt-wg-agentic-commerce-issue-5]: https://github.com/aaif/wg-agentic-commerce/issues/5
