---
type: standard
title: Agent Identity and Trust Primitives
description: Draft foundational specification defining attestation models, accountability
  structures, revocability semantics, and authority-at-dispatch verification for autonomous
  agents.
resource: https://github.com/aaif/wg-identity-and-trust/pull/17
tags:
- identity
- trust
- attestation
- authorization
- credentials
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:21:46.728232+00:00'
sources:
- id: evt-wg-identity-and-trust-pr-17
  resource: https://github.com/aaif/wg-identity-and-trust/pull/17
  author: astrogilda
  last_modified: '2026-10-10T23:53:46+00:00'
---

# Overview

The Agent Identity and Trust Primitives specification defines foundational mechanisms for asserting, verifying, and scoping the identity and authority of autonomous AI agents. It addresses identity provenance across multiple principals, dynamic privilege delegation, and the cryptographic validation of agent authority at point-of-action dispatch.

# Architecture / Specification

### Authority-at-Dispatch Verification

To prevent privilege drift and replay attacks during delegated agent tasks, the specification incorporates an authority-at-dispatch evaluation model [^evt-wg-identity-and-trust-pr-17]:

- **Versioned Contract Identifiers**: Every verifiable execution trace must emit a distinct, versioned delegation contract identifier. Interception and verification engines are configured to refuse trace payloads that omit this binding [^evt-wg-identity-and-trust-pr-17].
- **Authority Evidence Age and Freshness**: Authority evidence records must encode their generation timestamp and declare operational freshness limits, ensuring stale delegation grants cannot be replayed past their deployed time-to-live [^evt-wg-identity-and-trust-pr-17].
- **Benchmarked Execution Cases**: The standard references test cases evaluating delegated authority models across heterogeneous implementations to guarantee interoperable verification [^evt-wg-identity-and-trust-pr-17].

# Lifecycle History

- PR #17 introduced reference cases and workflow automation for the authority-at-dispatch comparative catalogue, enforcing contract identifiers and credential age boundaries [^evt-wg-identity-and-trust-pr-17].

[^evt-wg-identity-and-trust-pr-17]: https://github.com/aaif/wg-identity-and-trust/pull/17
