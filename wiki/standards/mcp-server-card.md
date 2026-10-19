---
type: standard
title: MCP Server Cards
description: Static metadata document format and discovery protocol enabling clients
  to discover and connect to remote MCP servers.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/mcp-server-card.yaml
tags:
- external
- standard
- discovery
- mcp
- http
- specification
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:45:26.365731+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-51c16b7e68a7-0a9465af
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/mcp-server-card.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:46:06+02:00'
---

# Overview
MCP Server Cards (SEP-2127, ext-server-card) is an experimental extension specification for the Model Context Protocol (MCP), a project of the Agentic AI Foundation (AAIF), a Linux Foundation directed fund[^evt-ext-frmoretto-agentic-standards-map-85d122-file-51c16b7e68a7-0a9465af]. Cataloged by independent researcher Francesco Marinoni Moretto in the agentic standards landscape, a Server Card is a static metadata document providing remote connectivity details sufficient for clients to discover and connect to a remote MCP server without enumerating dynamic runtime primitives[^evt-ext-frmoretto-agentic-standards-map-85d122-file-51c16b7e68a7-0a9465af].

# Architecture / Specification
A Server Card describes remote connectivity only, intentionally omitting listings of primitives such as tools, resources, and prompts[^evt-ext-frmoretto-agentic-standards-map-85d122-file-51c16b7e68a7-0a9465af]. Local package installation metadata remains scoped to `server.json` in the MCP Registry rather than the card[^evt-ext-frmoretto-agentic-standards-map-85d122-file-51c16b7e68a7-0a9465af].

Clients performing domain-level discovery retrieve `/.well-known/ai-catalog.json`, whose entries of MIME type `application/mcp-server-card+json` direct clients to individual server cards[^evt-ext-frmoretto-agentic-standards-map-85d122-file-51c16b7e68a7-0a9465af]. Commerce and payment metadata were explicitly kept out of the Server Card format: proposals to introduce metadata patterns such as `_meta` riders (Issue #27) and payment extensions (SEP-2007) were closed or marked dormant[^evt-ext-frmoretto-agentic-standards-map-85d122-file-51c16b7e68a7-0a9465af]. Discovery and catalog boundaries cross-reference [AI Catalog](../standards/ai-catalog.md), [Agentic Resource Discovery](../standards/agentic-resource-discovery.md), and [A2A](../standards/a2a.md)[^evt-ext-frmoretto-agentic-standards-map-85d122-file-51c16b7e68a7-0a9465af].

# Lifecycle History
- **2026-06-13**: Maintainers close issue #27, confirming MCP-specific metadata patterns will not be added to the catalog format[^evt-ext-frmoretto-agentic-standards-map-85d122-file-51c16b7e68a7-0a9465af].
- **2026-06-24**: Specification Enhancement Proposal SEP-2007 (payment support) closed as dormant[^evt-ext-frmoretto-agentic-standards-map-85d122-file-51c16b7e68a7-0a9465af].
- **2026-08-12**: Extension repository PR #47 merged, establishing roadmap toward official MCP extension graduation[^evt-ext-frmoretto-agentic-standards-map-85d122-file-51c16b7e68a7-0a9465af].
- **2026-10-06**: Specification Enhancement Proposal SEP-2127 merged into the main MCP repository on the Extensions Track with status Final[^evt-ext-frmoretto-agentic-standards-map-85d122-file-51c16b7e68a7-0a9465af].

# References
- [Francesco Marinoni Moretto: MCP Server Card Entry](https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/mcp-server-card.yaml)
- [Model Context Protocol PR #2127](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2127)
- [ext-server-card PR #47](https://github.com/modelcontextprotocol/ext-server-card/pull/47)

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-51c16b7e68a7-0a9465af]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/mcp-server-card.yaml
