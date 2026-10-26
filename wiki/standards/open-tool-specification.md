---
type: standard
title: Open Tool Specification
description: Declarative, contract-first specification defining schemas, security
  scopes, field masking, and governance policies for capabilities consumed over the
  Model Context Protocol.
resource: https://github.com/aaif/project-proposals/issues/63
tags:
- standard
- mcp
- governance
- api-contract
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T11:08:56.885758+00:00'
sources:
- id: evt-project-proposals-issue-63
  resource: https://github.com/aaif/project-proposals/issues/63
  author: psagarna
  last_modified: '2026-10-22T17:02:08+00:00'
---

# Overview
The Open Tool Specification (OTS) is a declarative, language-agnostic, contract-first specification for defining tools, resources, and prompts consumed by AI agents over the Model Context Protocol (MCP).[^evt-project-proposals-issue-63] Analogous to OpenAPI for REST endpoints, OTS defines a machine-readable document describing capability schemas, backend implementations, security boundaries, and runtime constraints.[^evt-project-proposals-issue-63]

# Architecture / Specification
OTS decouples capability definition into three architectural layers: the semantic interface presented to the agent, an aggregated discovery catalog, and backend runtime execution mapping.[^evt-project-proposals-issue-63]

### Core Project Components
1. **Specification (OTS 1.0.0)**: Schema definitions covering capability metadata, server configurations, component reuse, per-tool scopes, cache TTL, idempotency, agent error semantics, and field-level output masking via `x-ots-mask`.[^evt-project-proposals-issue-63]
2. **OTS Gateway**: A Go-based reference proxy positioned between agents and MCP servers that returns identity-filtered catalogs, validates inputs and outputs, enforces quotas and token budgets, masks sensitive fields, and routes requests across backend servers.[^evt-project-proposals-issue-63]
3. **OTS Visual Designer**: An IDE visual extension for VS Code supporting specification authoring, embedded gateway execution, and test scenario debugging.[^evt-project-proposals-issue-63]

### Integration with MCP
OTS acts as a governance and contract layer on top of standard MCP wire protocols rather than replacing them.[^evt-project-proposals-issue-63] Client agents such as [Goose](../resources/goose.md) can connect directly to the OTS Gateway as a consolidated MCP endpoint without client-side modifications.[^evt-project-proposals-issue-63]

[^evt-project-proposals-issue-63]: https://github.com/aaif/project-proposals/issues/63
