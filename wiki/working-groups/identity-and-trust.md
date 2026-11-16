---
type: working-group
title: Identity and Trust Working Group
description: Technical working group establishing vendor-neutral standards, delegation
  models, cryptographic trust roots, and multi-hop operational viewpoints for AI agents.
resource: https://github.com/aaif/wg-identity-and-trust/issues/25
tags:
- identity
- trust
- delegation
- architecture
- cryptography
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:45:37.921247+00:00'
sources:
- id: evt-wg-identity-and-trust-issue-25
  resource: https://github.com/aaif/wg-identity-and-trust/issues/25
  author: kevinhammond
  last_modified: '2026-11-15T10:54:44+00:00'
- id: evt-wg-identity-and-trust-issue-30
  resource: https://github.com/aaif/wg-identity-and-trust/issues/30
  author: MarcMolas
  last_modified: '2026-11-12T20:51:03+00:00'
---

# Overview

The Identity and Trust Working Group establishes vendor-neutral identity primitives, cryptographic attestation mechanisms, and authority delegation frameworks for agentic AI deployments [^evt-wg-identity-and-trust-issue-25]. It defines how agents assert identity, inherit permissions from principals, verify counterparties across institutional trust boundaries, and maintain delegation continuity [^evt-wg-identity-and-trust-issue-25, ^evt-wg-identity-and-trust-issue-30].

# Architecture / Specification

The working group models agent authority, verifiable identity assertions, and multi-party trust topologies.

## Reference Architecture Operational Viewpoint

The working group develops an operational viewpoint based on ISO/IEC/IEEE 42010 to define authority and accountability flow across agent systems [^evt-wg-identity-and-trust-issue-25]:
- **Actor Model**: Formulates explicit operational roles for interacting entities, evaluating extensions for specialized roles such as Approver and Auditor [^evt-wg-identity-and-trust-issue-25].
- **Delegation Models**: Governs authority attenuation, shared execution limits, multi-parent delegation graphs, cross-organizational hops, and delegation finalisation [^evt-wg-identity-and-trust-issue-25].
- **Operational Rules and Scenarios**: Establishes candidate conformance scenarios (S1–S12) and normative rules (R1–R13) to validate authority handling during dispatch, timeout, and delegation replacement [^evt-wg-identity-and-trust-issue-25].

## Multi-Hop Delegation Evidence

In coordination with the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), the group explores delegation evidence across hops where telemetry cannot carry full proof artifacts [^evt-wg-identity-and-trust-issue-30]:
- **Verifiable Delegation Roots**: Specifying verification requirements for each intermediary hop back to an accountable root principal [^evt-wg-identity-and-trust-issue-30].
- **Trust Boundary Translation**: Recording identity mappings where identifiers are translated across distinct organizational or cryptographic boundaries [^evt-wg-identity-and-trust-issue-30].

# Lifecycle History

Discussions in Issue #25 and Issue #30 expanded the working group's scope to formal architectural viewpoints and cross-boundary delegation evidence continuity [^evt-wg-identity-and-trust-issue-25, ^evt-wg-identity-and-trust-issue-30].

[^evt-wg-identity-and-trust-issue-25]: https://github.com/aaif/wg-identity-and-trust/issues/25
[^evt-wg-identity-and-trust-issue-30]: https://github.com/aaif/wg-identity-and-trust/issues/30
