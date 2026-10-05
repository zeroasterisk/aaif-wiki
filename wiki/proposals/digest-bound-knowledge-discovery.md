---
type: proposal
title: Digest-Bound Knowledge Link Set Discovery
description: Pre-connection discovery format using RFC 9264 link sets and RFC 9530
  cryptographic digests to verify published agent surfaces.
resource: https://github.com/aaif/wg-identity-and-trust/issues/11
tags:
- discovery
- identity
- trust
- mcp
- verification
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:24:38.036376+00:00'
sources:
- id: evt-wg-identity-and-trust-issue-11
  resource: https://github.com/aaif/wg-identity-and-trust/issues/11
  author: andreibesleaga
  last_modified: '2026-10-01T08:42:42+00:00'
---

# Overview
The digest-bound knowledge link set discovery proposal defines a static, pre-connection discovery mechanism allowing AI agents to discover and cryptographically verify published server capabilities and documents before initiating active interaction [^evt-wg-identity-and-trust-issue-11]. Submitted to the [Identity and Trust Working Group](../working-groups/identity-and-trust.md), the proposal explores extending Model Context Protocol (MCP) server cards with independent, transport-agnostic metadata integrity verification [^evt-wg-identity-and-trust-issue-11].

# Architecture / Specification
## Discovery Endpoint and Format
- **Endpoint**: Hosted at `/.well-known/knowledge-linkset` and served with media type `application/linkset+json` using the RFC 9264 §5 profile parameter [^evt-wg-identity-and-trust-issue-11].
- **Link Context**: Anchored at the publisher's Bundle IRI, exposing an array of linked discovery targets [^evt-wg-identity-and-trust-issue-11].

## Integrity and Federation Boundaries
- **Cryptographic Digest Binding**: Every linked artifact carries a target `digest` attribute formatted as an RFC 9530 SHA-256 value in RFC 9651 Byte Sequence syntax, enabling clients to verify canonical bytes independently of transport delivery [^evt-wg-identity-and-trust-issue-11].
- **Surface Declarations**: Published agent surfaces declare the specific external specification revisions they implement via registered `describedby` relation links [^evt-wg-identity-and-trust-issue-11].
- **Mutual Federation**: Federation between nodes requires explicit mutual naming; any metadata derived from peers is isolated with an untrusted origin boundary [^evt-wg-identity-and-trust-issue-11].

# Lifecycle History
Proposed as an exploratory issue in the Identity and Trust Working Group to evaluate whether verifiable publisher metadata and pre-connection link integrity fall within the working group's scope or should be submitted directly to MCP SEP-2127 [^evt-wg-identity-and-trust-issue-11].

[^evt-wg-identity-and-trust-issue-11]: https://github.com/aaif/wg-identity-and-trust/issues/11
