---
type: standard
title: Model Context Protocol
description: Open protocol standardizing integration between LLM applications and
  external data sources, tools, and prompts.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/mcp-core.yaml
tags:
- external
- standard
- context
- tooling
- mcp
- interoperability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:45:26.365731+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-5b65614e420d-8b4a9451
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/mcp-core.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:28:09+02:00'
---

# Overview
The Model Context Protocol (MCP) is an open protocol and a project of the Agentic AI Foundation (AAIF), a Linux Foundation directed fund, that enables seamless integration between LLM applications and external data sources and tools[^evt-ext-frmoretto-agentic-standards-map-85d122-file-5b65614e420d-8b4a9451]. Donated by Anthropic to the Agentic AI Foundation on December 9, 2025, MCP provides a standardized client-server protocol enabling language model harnesses to discover, read, and invoke contextual capabilities[^evt-ext-frmoretto-agentic-standards-map-85d122-file-5b65614e420d-8b4a9451].

# Architecture / Specification
The core MCP specification standardizes three primary capability primitives exposed by servers: tools, resources, and prompts[^evt-ext-frmoretto-agentic-standards-map-85d122-file-5b65614e420d-8b4a9451]. Protocol interactions occur over structured transports, governing request-response lifecycles and runtime capability negotiation between hosts, clients, and servers[^evt-ext-frmoretto-agentic-standards-map-85d122-file-5b65614e420d-8b4a9451].

Discovery mechanisms for remote MCP endpoints are defined in companion specifications, including [MCP Server Cards](../standards/mcp-server-card.md) for static connection metadata and [AI Catalog](../standards/ai-catalog.md) for domain-level registry indexing[^evt-ext-frmoretto-agentic-standards-map-85d122-file-5b65614e420d-8b4a9451]. The specification also overlaps and coordinates with the [A2A](../standards/a2a.md) protocol for direct agent-to-agent task delegation[^evt-ext-frmoretto-agentic-standards-map-85d122-file-5b65614e420d-8b4a9451].

# Lifecycle History
- **2025-03-26**: Core specification version 2025-03-26 released[^evt-ext-frmoretto-agentic-standards-map-85d122-file-5b65614e420d-8b4a9451].
- **2025-06-18**: Core specification version 2025-06-18 released[^evt-ext-frmoretto-agentic-standards-map-85d122-file-5b65614e420d-8b4a9451].
- **2025-11-25**: Core specification version 2025-11-25 released[^evt-ext-frmoretto-agentic-standards-map-85d122-file-5b65614e420d-8b4a9451].
- **2025-12-09**: Anthropic announces donation of MCP to the Agentic AI Foundation[^evt-ext-frmoretto-agentic-standards-map-85d122-file-5b65614e420d-8b4a9451].
- **2026-07-28**: Core specification version 2026-07-28 released[^evt-ext-frmoretto-agentic-standards-map-85d122-file-5b65614e420d-8b4a9451].

# References
- [Francesco Marinoni Moretto: MCP Core Entry](https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/mcp-core.yaml)

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-5b65614e420d-8b4a9451]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/mcp-core.yaml
