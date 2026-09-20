---
type: taxonomy-term
title: Attestation
description: Verifiable evidence establishing the integrity, identity, or state of
  a runtime platform or agent artifact without requiring trust in the producing system.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/49
tags:
- security
- identity
- trust
- attestation
- cryptography
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:04:33.485834+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-49
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/49
  author: narko4u
  last_modified: '2026-09-16T17:48:10+00:00'
---

# Overview
Attestation is verifiable evidence that establishes the integrity, identity, or operational state of an execution environment or agent artifact such that a relying party can verify claims without trusting the system that generated them[^evt-ws-taxonomy-landscape-pr-49]. It serves as a foundational security primitive across identity, security, and governance frameworks[^evt-ws-taxonomy-landscape-pr-49].

# Architecture / Specification

## Core Discriminator
The essential discriminator of attestation is independent verifiability: distinguishing declared, self-asserted claims from cryptographically provable evidence that does not rely on implicit trust in the producing host or harness[^evt-ws-taxonomy-landscape-pr-49].

## The Two-Binding Model
Attestation relies on two distinct, decoupled bindings to avoid deceptive identity claims[^evt-ws-taxonomy-landscape-pr-49]:
1. **Platform Attestation**: Cryptographic proof establishing that the underlying execution platform and hardware (e.g., confidential computing enclaves, kernel environments) conform to expected security postures[^evt-ws-taxonomy-landscape-pr-49].
2. **Artifact / Identity Binding**: A separate signed binding linking a specific agent identity, code manifest, or artifact to the verified platform state[^evt-ws-taxonomy-landscape-pr-49].

Collapsing these two layers risks creating superficial "attested identity" without true isolation guarantees[^evt-ws-taxonomy-landscape-pr-49].

# References
- [Attested Isolated Runtime](../deliverable/attested-isolated-runtime.md)
- [Working Group: Identity and Trust](../working-groups/identity-and-trust.md)
- [Working Group: Security and Privacy](../working-groups/security-and-privacy.md)
- [Working Group: Governance, Risk, and Regulatory Alignment](../working-groups/governance-risk-and-regulatory.md)

[^evt-ws-taxonomy-landscape-pr-49]: https://github.com/aaif/ws-taxonomy-landscape/pull/49
