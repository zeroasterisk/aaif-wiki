---
type: working-group
title: Identity and Trust Working Group
description: Technical working group defining agent identity, credential delegation,
  decentralized trust, and verifiable authority at dispatch.
resource: https://github.com/aaif/wg-identity-and-trust/pull/17
tags:
- working-group
- identity
- trust
- delegation
- verification
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:20:12.498367+00:00'
sources:
- id: evt-wg-identity-and-trust-pr-17
  resource: https://github.com/aaif/wg-identity-and-trust/pull/17
  author: astrogilda
  last_modified: '2026-10-10T23:53:46+00:00'
---

# Overview
The Identity and Trust Working Group is an Agentic AI Foundation technical body established to standardize agent identity mechanisms, cryptographic delegation frameworks, decentralized trust models, and verifiable authority specifications across multi-agent systems [^evt-wg-identity-and-trust-pr-17]. The working group evaluates decentralized identifiers, delegation chains, and verification harnesses that govern how autonomous agents establish, prove, and constrain authority during execution [^evt-wg-identity-and-trust-pr-17].

# Architecture / Specification

## Core Focus Areas
The working group coordinates technical specifications and empirical evaluation across several domains:
- **Decentralized Agent Identity**: Standardizing verifiable credential profiles and decentralized identifiers (DIDs) interoperable across platforms, complementing efforts such as [agent-network-protocol](../standards/agent-network-protocol.md).
- **Delegated Authority and Consent**: Defining schemas for bounded delegation, subagent credential scopes, and user consent verification.
- **Authority-at-Dispatch Verification**: Benchmarking and cataloguing mechanisms that verify agent authority at the moment of tool or task dispatch [^evt-wg-identity-and-trust-pr-17].

## Authority-at-Dispatch Catalogue and Testing
The working group maintains a reference catalogue and verification workflow evaluating authority-at-dispatch implementations [^evt-wg-identity-and-trust-pr-17]:
- **Contract Identifier Enforcement**: Execution traces must include a versioned contract identifier; trace readers reject submissions lacking this explicit identifier [^evt-wg-identity-and-trust-pr-17].
- **Freshness Limits**: Authority evidence structures must record assertion age against deployed freshness thresholds to prevent replay of stale delegation authorizations [^evt-wg-identity-and-trust-pr-17].
- **Reference Comparative Benchmarks**: Standardized reference cases map authority assertion runs across distinct systems, integrating readers from tooling such as `agent-evidence-observer` [^evt-wg-identity-and-trust-pr-17].

# Lifecycle History
Active within the AAIF governance structure, collaborating with related efforts such as [evidence-record-spec](../standards/evidence-record-spec.md) and [governance-risk-and-regulatory](../working-groups/governance-risk-and-regulatory.md) [^evt-wg-identity-and-trust-pr-17].

[^evt-wg-identity-and-trust-pr-17]: https://github.com/aaif/wg-identity-and-trust/pull/17
