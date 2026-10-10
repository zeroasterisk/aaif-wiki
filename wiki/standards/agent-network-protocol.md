---
type: standard
title: Agent Network Protocol
description: Open communication protocol stack utilizing Decentralized Identifiers
  (DIDs) for cross-platform agent identity, secure messaging, and semantic discovery.
resource: https://github.com/aaif/project-proposals/issues/46
tags:
- anp
- networking
- identity
- did
- messaging
- discovery
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:18:20.208859+00:00'
sources:
- id: evt-project-proposals-issue-46
  resource: https://github.com/aaif/project-proposals/issues/46
  author: chgaowei
  last_modified: '2026-10-02T09:05:31+00:00'
---

# Overview

The Agent Network Protocol (ANP) is an open communication protocol stack designed to interconnect autonomous agents across heterogeneous platforms, administrative domains, and infrastructure [^evt-project-proposals-issue-46]. ANP defines mechanisms for decentralized agent identity, end-to-end encrypted messaging, and semantic discovery over standard Internet protocols (DNS, HTTPS) without requiring proprietary silos or blockchain dependencies [^evt-project-proposals-issue-46].

# Architecture / Specification

ANP comprises three primary functional layers [^evt-project-proposals-issue-46]:
- **Agent Identity**: Employs W3C Decentralized Identifiers (DIDs), introducing the `did:wba` (Web-Based Agent) method and supporting `did:web` to bind cryptographic key material to web-accessible agent identities (see [../working-groups/identity-and-trust.md](../working-groups/identity-and-trust.md)).
- **Agent Messaging**: A DID-anchored messaging protocol facilitating direct peer-to-peer dialogues, multi-agent group communication, attachment sharing, and end-to-end encrypted interactions with verifiable origin proofs.
- **Agent Discovery and Description**: Semantic Linked Data representations referencing agent capabilities and interfaces (such as OpenAPI schemas), allowing external agents to dynamically discover available service endpoints [^evt-project-proposals-issue-46].

# Lifecycle History

Initiated in 2024 and launched as an open-source community effort in April 2025, ANP was submitted as a project proposal to the Agentic AI Foundation [^evt-project-proposals-issue-46].

[^evt-project-proposals-issue-46]: https://github.com/aaif/project-proposals/issues/46
