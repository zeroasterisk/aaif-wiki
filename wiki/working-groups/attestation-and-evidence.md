---
type: working-group
title: Attestation and Evidence Working Group
description: Cross-cutting AAIF technical working group defining vendor-neutral standards,
  verification taxonomies, and portable evidence bundles for independently checkable
  agent actions.
resource: https://github.com/aaif/working-group-proposals/issues/6
tags:
- working-group
- attestation
- evidence
- verification
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:26:49.475987+00:00'
sources:
- id: evt-working-group-proposals-issue-6
  resource: https://github.com/aaif/working-group-proposals/issues/6
  author: StevenMih
  last_modified: '2026-10-25T15:10:07+00:00'
---

# Overview
The Attestation & Evidence Working Group (AE-WG) is a cross-cutting technical body proposed within the Agentic AI Foundation to make AI agent actions, decisions, authorizations, and outcomes independently verifiable across organizational boundaries [^evt-working-group-proposals-issue-6]. While sibling working groups address specific aspects of agent behavior—such as identity in [Identity & Trust](../working-groups/identity-and-trust.md), telemetry in [Observability & Traceability](../working-groups/observability-and-traceability.md), and execution history in [Workflows & Process Integration](../working-groups/workflows-and-process-integration.md)—AE-WG focuses on the second-party and third-party verifiability of durable evidence records without requiring reliance on a central authority [^evt-working-group-proposals-issue-6].

# Architecture / Specification
The proposed working group operates across four core focus areas [^evt-working-group-proposals-issue-6]:
- **Bilateral and Multi-Party Attestation**: Establishing protocols where each party to an interaction seals its own observations, deriving agreement or divergence through verifiable comparison rather than assertion.
- **Portable Evidence Bundles**: Designing self-describing, offline-verifiable bundles that declare their completeness and disclosure boundaries, returning artifacts, signed refusals, or cryptographic proofs of absence.
- **Witness and Root-of-Trust Taxonomies**: Categorizing and standardizing verification primitives across transparency logs, cosigners, timestamp authorities, Trusted Execution Environments (TEEs), Hardware Security Modules (HSMs), and secure elements.
- **Cross-WG Coordination**: Maintaining liaison seats with sibling working groups such as [Governance, Risk & Regulatory](../working-groups/governance-risk-and-regulatory.md) for regulatory mapping and [Security & Privacy](../working-groups/security-and-privacy.md) for privacy-preserving disclosures.

## Scope Boundaries
- **In-Scope**: Evidence vocabularies and class hierarchies, action attestation, commitment prior to observation, boundary evidence interchange, and verifiable disclosure mechanisms [^evt-working-group-proposals-issue-6].
- **Out-of-Scope**: Direct identity credentialing, telemetry wire formats, evaluation scoring or benchmark verdicts, threat modeling, payment operations, hardware attestation mechanisms themselves, and foundation-operated ledgers [^evt-working-group-proposals-issue-6].

# Lifecycle History
- **Proposed Charter**: Submitted as an initial cross-working-group charter proposal by Steven Mih (Action State) with a 90-day ramp plan targeting an initial Evidence Vocabulary v0, sibling evidence requirement matrices, and a gap analysis for [Technical Committee](../governance/technical-committee.md) review [^evt-working-group-proposals-issue-6].

[^evt-working-group-proposals-issue-6]: https://github.com/aaif/working-group-proposals/issues/6
