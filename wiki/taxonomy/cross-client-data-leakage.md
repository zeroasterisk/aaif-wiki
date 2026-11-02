---
type: taxonomy
title: Cross-Client Data Leakage
description: Security vulnerability where confidential session state, prompt data,
  or tool responses cross isolation boundaries on a shared agent tool server.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/88
tags:
- taxonomy
- security
- privacy
- isolation
- tools
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:20:48.792446+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-88
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/88
  author: GeeksikhSecurity
  last_modified: '2026-10-09T12:40:04+00:00'
---

# Overview
Cross-client data leakage is an isolation vulnerability occurring on shared tool servers (such as multi-tenant Model Context Protocol servers) where session state, credentials, prompts, or execution outputs belonging to one client are inadvertently exposed to another client session.[^evt-ws-taxonomy-landscape-pr-88] The flaw occurs when tool server implementations maintain unsegmented global variables, shared cache buffers, or connection multiplexing without strict per-session boundaries.[^evt-ws-taxonomy-landscape-pr-88]

# Architecture / Specification
When multiple agent clients interact with a shared tool server, context contamination can propagate through:
- In-memory conversation state or tool execution history retained across distinct client invocations.[^evt-ws-taxonomy-landscape-pr-88]
- Shared credential caches exposing elevated access tokens across multi-user environments.[^evt-ws-taxonomy-landscape-pr-88]
- Error logs and telemetry payloads returning raw context from previous sessions.[^evt-ws-taxonomy-landscape-pr-88]

Countermeasures include enforcing [branch isolation](../patterns/branch-isolation.md), requiring ephemeral sandboxing for tool execution, and strictly partitioning session state in tool runtime protocols.[^evt-ws-taxonomy-landscape-pr-88]

# Lifecycle History
Proposed in PR #88 of the [Taxonomy and Landscape Workstream](../working-groups/taxonomy-and-landscape.md) in coordination with the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) and [Identity and Trust Working Group](../working-groups/identity-and-trust.md).[^evt-ws-taxonomy-landscape-pr-88]

[^evt-ws-taxonomy-landscape-pr-88]: https://github.com/aaif/ws-taxonomy-landscape/pull/88
