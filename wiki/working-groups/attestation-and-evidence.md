---
type: working-group
title: Attestation & Evidence Working Group
description: Cross-cutting AAIF working group defining standards, witness taxonomies,
  and portable bundle formats for independently verifiable AI agent actions and decisions.
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
  at: '2026-10-26T11:08:56.885758+00:00'
sources:
- id: evt-working-group-proposals-issue-6
  resource: https://github.com/aaif/working-group-proposals/issues/6
  author: StevenMih
  last_modified: '2026-10-25T15:10:07+00:00'
---

# Overview
The Attestation & Evidence Working Group (AE-WG) is a proposed cross-cutting technical working group within the Agentic AI Foundation tasked with standardizing how statements about AI agent actions, decisions, authorizations, and outcomes are attested and preserved as independently verifiable evidence.[^evt-working-group-proposals-issue-6]

# Architecture / Specification
The working group focuses on creating evidence formats that survive across organizational boundaries and allow third parties to independently verify historical agent operations without relying on centralized authorities.[^evt-working-group-proposals-issue-6]

### Primary Workstreams
- **Bilateral and Multi-Party Attestation**: Protocols ensuring each participant in an interaction cryptographically seals its own observation, deriving consensus or dispute deterministically.[^evt-working-group-proposals-issue-6]
- **Portable Evidence Bundles**: Self-describing, offline-verifiable data structures declaring their completeness and disclosure boundaries.[^evt-working-group-proposals-issue-6]
- **Witness and Root-of-Trust Taxonomy**: Structural classification mapping verification mechanisms—such as transparency logs, timestamp authorities, Trusted Execution Environments (TEEs), and Hardware Security Modules (HSMs)—to the guarantees they provide.[^evt-working-group-proposals-issue-6]

### Cross-Group Collaboration
The AE-WG operates liaisons with sibling AAIF bodies:
- Sourcing entity identifiers from the [Identity and Trust Working Group](identity-and-trust.md).[^evt-working-group-proposals-issue-6]
- Consuming runtime telemetry models from the [Observability and Traceability Working Group](observability-and-traceability.md).[^evt-working-group-proposals-issue-6]
- Mapping evidence classes to compliance mandates defined by the [Governance, Risk, and Regulatory Working Group](governance-risk-and-regulatory.md).[^evt-working-group-proposals-issue-6]

[^evt-working-group-proposals-issue-6]: https://github.com/aaif/working-group-proposals/issues/6
