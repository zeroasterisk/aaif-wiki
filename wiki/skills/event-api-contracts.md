---
type: skill
title: Event API Contracts
description: Procedural agent skill defining design standards, boundary validation,
  authorization enforcement, and testing rules for AAIF Dallas HTTP APIs and MCP tools.
resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/event-api-contracts/SKILL.md
tags:
- skills
- api
- mcp
- contracts
- events
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:38:49.354262+00:00'
sources:
- id: evt-aaif-dallas-community-file-333926b09e66-2184428a
  resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/event-api-contracts/SKILL.md
  author: Govindaraj Palanisamy
  last_modified: '2026-11-22T22:32:04-06:00'
---

# Overview

`event-api-contracts` is an operational agent skill governing the design, evolution, and contract testing of HTTP APIs, Model Context Protocol (MCP) tools, and agent workflows across AAIF Dallas event services.[^evt-aaif-dallas-community-file-333926b09e66-2184428a] It enforces strict architectural boundaries across process and transport layers, requiring that validation, authorization, and domain invariants reside in service code rather than relying on agent prompts or client-side controls.[^evt-aaif-dallas-community-file-333926b09e66-2184428a]

# Architecture / Specification

The skill specifies contractual requirements across shared service layers and protocol-specific interfaces:[^evt-aaif-dallas-community-file-333926b09e66-2184428a]

- **Shared Contract Rules**: Request and response schemas must derive from a single canonical type definition; endpoint paths, schemas, and tool definitions must align with domain vocabulary established in [Event Domain Modeling](../skills/event-domain-modeling.md); untrusted input must be validated prior to invoking application logic; and mutations or retries must preserve idempotency.[^evt-aaif-dallas-community-file-333926b09e66-2184428a]
- **HTTP API Checklist**: Every endpoint specification must explicitly define the requesting actor, authentication scheme, authorization rules, request/response payload schemas, domain-specific error codes, rate and abuse constraints, and idempotency guarantees.[^evt-aaif-dallas-community-file-333926b09e66-2184428a]
- **MCP Tool Standards**: Each MCP tool must perform a single bounded operation with a strictly typed JSON schema, declare all preconditions and side effects within its description, reject unauthorized invocations, return stable structured payloads, and maintain automated contract and failure-path tests.[^evt-aaif-dallas-community-file-333926b09e66-2184428a]
- **Agent Operational Boundaries**: Agents are restricted to invoking approved tools and prohibited from direct database persistence; prompts guide context and task objectives but cannot substitute for server-side validation or authorization gates; and agent execution traces must avoid persisting secrets or unnecessary attendee personal data.[^evt-aaif-dallas-community-file-333926b09e66-2184428a]

# Lifecycle History

Introduced in the AAIF Dallas community repository to standardize service integrations between event management agents and external HTTP/MCP endpoints.[^evt-aaif-dallas-community-file-333926b09e66-2184428a]

[^evt-aaif-dallas-community-file-333926b09e66-2184428a]: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/event-api-contracts/SKILL.md
