---
type: standard
title: Control Surfaces for Agentic Harnesses
description: Standardized profile defining administrative harness lifecycle events,
  external authorization checkpoints, and delegated execution boundaries.
resource: https://github.com/aaif/wg-security-and-privacy/pull/45
tags:
- standard
- security
- harness
- control-plane
- authorization
- policy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:31:15.104701+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-45
  resource: https://github.com/aaif/wg-security-and-privacy/pull/45
  author: awfrazer
  last_modified: '2026-10-29T19:54:21+00:00'
---

# Overview

The Control Surfaces for Agentic Harnesses profile (v0.3) defines the administrative control plane an agentic harness exposes to system operators: the lifecycle events it records and the checkpoints where an external authorization decision gates agent execution.[^evt-wg-security-and-privacy-pr-45] Rather than defining an abstract security model, the specification functions as an interoperable contract realized by client harnesses and policy services, bridging the implementation-independent patterns catalog and operational guides maintained by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md).[^evt-wg-security-and-privacy-pr-45]

# Architecture / Specification

## Protocol Composition

The profile composes four external standards to govern runtime interactions:[^evt-wg-security-and-privacy-pr-45]

- **OpenID AuthZEN**: Implements runtime authorization checkpoint decisions and decision record binding.
- **Agent Plugins Portable Hooks**: Provides canonical lifecycle event naming across tool execution, step transitions, and subagent spawning (see [Agent Plugins](../standards/agent-plugins.md)).
- **Open Cybersecurity Schema Framework (OCSF)**: Structures structured audit trail records and telemetry payloads.
- **OAuth Token Exchange**: Enforces monotonic scope narrowing, principal assertion, and delegation lineage across subagent chains.

## Concrete Pattern Realization

The specification provides normative implementations for core catalog design patterns:[^evt-wg-security-and-privacy-pr-45]

- **Approval Checkpoint (Section 8.3 & 8.4)**: Realizes decision binding and decision records (see [Approval Checkpoint](../patterns/approval-checkpoint.md)).
- **Runtime Policy Enforcement (Section 8)**: Standardizes external Policy Decision Point (PDP) checkpoint queries and timeout/failure semantics (`fail_closed_deny`).
- **Delegation Constraint & Permission Downgrade (Section 6.2)**: Mandates monotonic narrowing and per-sub-agent scope issuance.
- **Capability-Based Tool Invocation (Sections 5.3 & 6.2)**: Associates canonical tool identifiers with scope tokens.
- **Memory Provenance (Section 7)**: Establishes context sources and integrity labels (`untrusted`, `sensitive`), implementing the Rule of Two per session defined in [Agentic AI Security Best Practices](../guidelines/agentic-ai-security-best-practices.md).
- **Audit Trail (Section 5)**: Defines normative lifecycle event capture.

## Pattern Reconciliation Points

The draft highlights specific reconciliation requirements against existing patterns:[^evt-wg-security-and-privacy-pr-45]

- **Approval Checkpoint Alignment**: Reconciles clock skew tolerance, recomputed digests under argument minimization, and error outcome classifications.
- **Attested Isolated Runtime Alignment**: Evaluates single-use action identifier consumption across persistent restart state versus stateless PDP verification (see [Attested Isolated Runtime](../patterns/attested-isolated-runtime.md)).
- **Kill Switch Alignment**: Clarifies session binding revocation and cascade lineage mechanics, distinguishing the session authority PDP from downstream identity providers (see [Kill Switch](../patterns/kill-switch.md)).

## Cross-Working-Group Dependencies

Delegation chain architecture and principal assertion link directly to the [Identity and Trust Working Group](../working-groups/identity-and-trust.md), while lifecycle telemetry coordinates with the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md).[^evt-wg-security-and-privacy-pr-45]

[^evt-wg-security-and-privacy-pr-45]: https://github.com/aaif/wg-security-and-privacy/pull/45
