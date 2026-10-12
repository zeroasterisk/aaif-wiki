---
type: resource
title: legacy2mcp
description: Open-source adapter framework and CLI generating typed, read-only Model
  Context Protocol servers from legacy enterprise SOAP, database, and REST interfaces.
resource: https://github.com/aaif/project-proposals/issues/54
tags:
- mcp
- adapters
- enterprise
- integration
- tools
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:20:12.498367+00:00'
sources:
- id: evt-project-proposals-issue-54
  resource: https://github.com/aaif/project-proposals/issues/54
  author: bvenkata
  last_modified: '2026-10-11T15:02:12+00:00'
---

# Overview
legacy2mcp is an open-source integration framework and command-line tool designed to expose legacy enterprise architectures—such as SOAP/WSDL web services, relational databases, and older REST APIs—as typed Model Context Protocol (MCP) servers [^evt-project-proposals-issue-54]. Proposed as an Agentic AI Foundation Sandbox project, legacy2mcp enables AI agents to query enterprise data safely without requiring developers to write custom glue code or grant broad backend privileges [^evt-project-proposals-issue-54].

# Architecture / Specification

## Dynamic Tool Generation and Schema Validation
legacy2mcp inspects backend systems directly (parsing WSDL service definitions or querying live relational database schemas) to generate typed MCP tool definitions with structured JSON Schemas [^evt-project-proposals-issue-54]:
- **Schema Validation**: Every incoming tool invocation from an MCP client is validated against the generated schema before any backend payload dispatch occurs.
- **Read-Only Defaults**: The framework enforces read-only access by default; write operations must be explicitly configured, and relational database adapters restrict queries to configured allowlists of tables and named parameterized queries, preventing arbitrary agent SQL execution [^evt-project-proposals-issue-54].
- **Audit Logging**: Every tool call and dispatched request is logged for traceability.

## Extensible Adapter Architecture
The framework core manages tool validation, dispatch, and logging while exposing a lightweight `BaseAdapter` interface requiring two methods [^evt-project-proposals-issue-54]:
- `discover_tools()`: Discovers backend endpoints and generates MCP tool schemas.
- `invoke()`: Executes validated calls against the upstream service.

Initial adapters support SOAP/WSDL endpoints, SQL relational databases (PostgreSQL, Microsoft SQL Server, Oracle), and REST APIs, alongside a scaffolding command (`legacy2mcp init`) to bootstrap configurations from existing codebases [^evt-project-proposals-issue-54].

## Ecosystem Integration
The generated servers run over stdio and are compatible with MCP-compliant agents, such as [goose](../resources/goose.md) and IDE client protocols [^evt-project-proposals-issue-54].

# Lifecycle History
Created by Venkata Bhupalam under the Apache-2.0 license, reaching version 0.2.1 and indexed on the MCP Registry prior to submission for AAIF Sandbox project intake in October 2026 [^evt-project-proposals-issue-54].

[^evt-project-proposals-issue-54]: https://github.com/aaif/project-proposals/issues/54
