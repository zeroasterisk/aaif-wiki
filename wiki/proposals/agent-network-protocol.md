---
type: proposal
title: Agent Network Protocol
description: Open Internet communication protocol stack defining decentralized W3C
  DID identity, end-to-end encrypted agent messaging, and linked-data service discovery.
resource: https://github.com/aaif/project-proposals/issues/46
tags:
- protocols
- identity
- messaging
- discovery
- interoperability
- did
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:26:10.204199+00:00'
sources:
- id: evt-project-proposals-issue-46
  resource: https://github.com/aaif/project-proposals/issues/46
  author: chgaowei
  last_modified: '2026-10-02T09:05:31+00:00'
---

# Overview

Agent Network Protocol (ANP) is an open communication protocol stack enabling agents across distinct platforms, organizations, and environments to establish cryptographic identity, discover capabilities, and communicate securely over the Internet.[^evt-project-proposals-issue-46] ANP reuses established Web, DNS, and HTTPS standards without requiring blockchain infrastructure.[^evt-project-proposals-issue-46]

# Architecture / Specification

ANP comprises three core modular layers:

- **Agent Identity**: Leverages W3C Decentralized Identifiers (DIDs), introducing `did:wba` (Web-Based Agent) alongside `did:web` to anchor user-controlled identities and cross-platform authentication.[^evt-project-proposals-issue-46]
- **Agent Messaging**: Defines a DID-based messaging protocol supporting peer-to-peer messaging, multi-agent group conversations, attachment transfer, and end-to-end encryption anchored in DID cryptographic keys.[^evt-project-proposals-issue-46]
- **Agent Discovery and Description**: Uses Semantic Web Linked Data and URL hierarchies to expose multi-level interface and service descriptions, integrating standard API formats such as OpenAPI.[^evt-project-proposals-issue-46]

# Lifecycle History

ANP was initiated in early 2024 by Gaowei Chang and transitioned to an open-source community project in April 2025 prior to its formal proposal to the Agentic AI Foundation in ISSUE#46.[^evt-project-proposals-issue-46]

[^evt-project-proposals-issue-46]: https://github.com/aaif/project-proposals/issues/46
