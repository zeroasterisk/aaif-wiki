---
type: working-group
title: Identity and Trust Working Group
description: AAIF technical working group establishing vendor-neutral standards, verification
  test suites, and trust models for agent identity, delegation trees, and key recovery.
resource: https://github.com/aaif/wg-identity-and-trust/issues/18
tags:
- working-groups
- identity
- trust
- attestation
- delegation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:15:47.474225+00:00'
sources:
- id: evt-wg-identity-and-trust-issue-18
  resource: https://github.com/aaif/wg-identity-and-trust/issues/18
  author: astrogilda
  last_modified: '2026-10-17T22:12:36+00:00'
- id: evt-wg-identity-and-trust-pr-20
  resource: https://github.com/aaif/wg-identity-and-trust/pull/20
  author: astrogilda
  last_modified: '2026-10-18T23:48:58+00:00'
---

# Overview
The Identity and Trust Working Group is an AAIF technical body developing vendor-neutral identity primitives, cryptographic attestation frameworks, delegation protocols, and lifecycle verification test cases for autonomous agent systems [^evt-wg-identity-and-trust-issue-18]. The group defines how agents, their human principals, and mediating infrastructure establish provenance, enforce least privilege, propagate delegated authority, and recover from key compromise [^evt-wg-identity-and-trust-issue-18, ^evt-wg-identity-and-trust-pr-20].

# Architecture / Specification
Key focus areas and technical workstreams within the working group include:

- **Agent Identity & DIDs:** Specifying decentralized identifiers, key bindings, and machine-verifiable credentials under standards such as the [Agent Network Protocol](../standards/agent-network-protocol.md).
- **Delegation Trees & Disputed Revocations:** Modeling hierarchical subagent delegation lifecycles, including test vectors where a parent identity is revoked while child delegations remain presented, or where revocation signals are delayed or unenforced [^evt-wg-identity-and-trust-issue-18, ^evt-wg-identity-and-trust-pr-20].
- **Re-Registration & Artifact Binding:** Defining test suites that tie signed action records and requests across identifier rotations and re-registrations [^evt-wg-identity-and-trust-issue-18, ^evt-wg-identity-and-trust-pr-20].
- **Key Recovery Semantics:** Developing recovery record rules signed jointly by registries and responsible entities under software attestation matching; recovery records carry forward history, revocations, and disputes while preventing unauthorized re-grants following compromise [^evt-wg-identity-and-trust-pr-20].
- **Evidence Verification:** Coordinating with external test vector suites such as `agent-evidence-vectors` to ensure deterministic validation across verifiers [^evt-wg-identity-and-trust-issue-18, ^evt-wg-identity-and-trust-pr-20].

# Lifecycle History
The working group actively evaluates identity and delegation lifecycle use cases. In late 2026, test suites covering disputed delegation revocation, identifier re-registration, and lost-key recovery workflows were integrated into the group's test harness [^evt-wg-identity-and-trust-issue-18, ^evt-wg-identity-and-trust-pr-20].

# References
- Working Group Repository: https://github.com/aaif/wg-identity-and-trust
- Delegation Lifecycle Test Cases: https://github.com/aaif/wg-identity-and-trust/pull/20

[^evt-wg-identity-and-trust-issue-18]: https://github.com/aaif/wg-identity-and-trust/issues/18
[^evt-wg-identity-and-trust-pr-20]: https://github.com/aaif/wg-identity-and-trust/pull/20
