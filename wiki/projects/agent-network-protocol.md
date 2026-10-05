---
type: project
title: Agent Network Protocol (ANP)
description: An open communication protocol stack providing decentralized DID-based
  identity, encrypted messaging, and linked data service discovery for cross-platform
  agent collaboration.
resource: https://github.com/aaif/project-proposals/issues/46
tags:
- protocol
- did
- identity
- messaging
- discovery
- interoperability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T06:00:39.547716+00:00'
sources:
- id: evt-project-proposals-issue-46
  resource: https://github.com/aaif/project-proposals/issues/46
  author: chgaowei
  last_modified: '2026-10-02T09:05:31+00:00'
---

# Overview

Agent Network Protocol (ANP) is an open communication protocol stack designed to interconnect autonomous AI agents across disparate platforms, administrative domains, and hosting environments[^evt-project-proposals-issue-46]. Initiated as an open-source project in 2024–2025, ANP provides standard mechanisms for decentralized agent identity, secure messaging, and service discovery over standard Web and Internet infrastructure[^evt-project-proposals-issue-46].

# Architecture / Specification

ANP structures cross-agent interoperability into three primary architectural modules[^evt-project-proposals-issue-46]:

- **Agent Identity**: Reuses W3C Decentralized Identifiers (DIDs) without requiring blockchain dependencies. ANP specifies the `did:wba` (Web-Based Agent) method alongside support for `did:web`, establishing cryptographic identity anchors, key publication, and mutual DID authentication over standard DNS and HTTPS[^evt-project-proposals-issue-46].
- **Agent Messaging**: A DID-based peer-to-peer and multi-agent group messaging protocol supporting end-to-end encryption (E2EE), payload attachments, and cryptographically signed message-origin proofs tied directly to verifiable DID key material[^evt-project-proposals-issue-46].
- **Agent Discovery and Description**: Employs Semantic Web Linked Data principles and OpenAPI specifications to structure agent interfaces into multi-level discoverable graphs addressable via URLs[^evt-project-proposals-issue-46].

# Lifecycle History

ANP was originated in early 2024 by Gaowei Chang and transitioned to a community-driven open-source project in April 2025[^evt-project-proposals-issue-46]. In 2026, the project was proposed for hosting within the AAIF to establish vendor-neutral governance alongside protocols such as [A2A](../projects/a2a.md)[^evt-project-proposals-issue-46].

[^evt-project-proposals-issue-46]: https://github.com/aaif/project-proposals/issues/46
