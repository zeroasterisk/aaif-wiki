---
type: taxonomy
title: Identity and Trust Terms
description: Standardized taxonomy vocabulary defining Trust, Identifier, Attestation,
  and Delegation across agentic runtimes.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/49
tags:
- taxonomy
- identity
- trust
- attestation
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:11:27.774715+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-49
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/49
  author: narko4u
  last_modified: '2026-09-16T17:48:10+00:00'
---

# Overview

The Identity and Trust taxonomy provides formal definitions for security boundaries, delegation, identity claims, and verifiable assurances in agentic AI architectures[^evt-ws-taxonomy-landscape-pr-49]. It is maintained jointly across the Identity & Trust, Security & Privacy, and Governance, Risk & Regulatory working groups[^evt-ws-taxonomy-landscape-pr-49].

# Architecture / Specification

### Key Terms

- **Trust**: The baseline assurance that an entity or system will behave according to expected operational and security parameters.
- **Identifier**: A unique, persistent label representing a human principal, autonomous agent, tool, or runtime context.
- **Attestation**: Cryptographically verifiable evidence that allows a relying party to verify the state, integrity, or properties of an execution environment without having to trust the system or runtime that produced it[^evt-ws-taxonomy-landscape-pr-49].
  - *Platform Attestation*: Verifies the integrity and security parameters of the underlying hardware or TEE environment[^evt-ws-taxonomy-landscape-pr-49].
  - *Identity Binding*: A distinct signed cryptographic binding connecting a specific agent identity or executable artifact to the attested platform environment[^evt-ws-taxonomy-landscape-pr-49].
- **Delegation**: The structured handoff of authority, scope, and tokenized credentials from an initiator to an executing agent.

# References

- [Attested Isolated Runtime Pattern](../patterns/attested-isolated-runtime.md)
- [Identity and Trust Working Group](../working-groups/identity-and-trust.md)
- [Taxonomy and Landscape Workstream](../working-groups/taxonomy-and-landscape.md)

[^evt-ws-taxonomy-landscape-pr-49]: https://github.com/aaif/ws-taxonomy-landscape/pull/49
