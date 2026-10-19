---
type: resource
title: Shopify Agent MCP Surfaces
description: Architectural reference analyzing Shopify Model Context Protocol surfaces
  spanning Checkout WebMCP, developer tooling, merchant administration, and Shop CLI.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/shopify.yaml
tags:
- external
- mcp
- commerce
- shopify
- tools
- webmcp
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:43:52.637607+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-4851ae5b081d-cc7ee8a9
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/shopify.yaml
  author: frmoretto
  last_modified: '2026-10-14T06:46:06+02:00'
---

# Overview
Shopify Agent MCP Surfaces are a suite of Model Context Protocol (MCP) interfaces and client tools stewarded by Shopify.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4851ae5b081d-cc7ee8a9] The architecture exposes four distinct integration surfaces tailored to buyer agents, software developers, merchants, and consumer shoppers.

# Architecture / Specification
- Buyer Agent Surfaces:
  - Server-Side Checkout MCP: Provides programmatic checkout sessions for autonomous agents executing in server-side environments.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4851ae5b081d-cc7ee8a9]
  - Checkout WebMCP: Browser-based client API exposing checkout capabilities directly to agents operating in the buyer's browser, implementing the Universal Commerce Protocol (UCP) capability `dev.ucp.shopping.checkout`.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4851ae5b081d-cc7ee8a9]
- Merchant Management Surface: Remote MCP hosted at `setup.shopify.com/mcp` utilized by developer plugins and store-creation assistants to configure merchant inventory and store settings.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4851ae5b081d-cc7ee8a9]
- Developer Tooling:
  - Local developer utility package `@shopify/dev-mcp` enabling local environment testing.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4851ae5b081d-cc7ee8a9]
  - Packaged skills within the `Shopify-AI-Toolkit`, including standalone `ucp` skills executing the UCP command-line binary.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4851ae5b081d-cc7ee8a9]
- Shopper Agent CLI (`@shopify/shop`):
  - Command-line agent interfacing with Shop's MCP endpoint at `mcp.shop.com` to search catalogs, construct carts, and execute payments.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4851ae5b081d-cc7ee8a9]
  - Bridges automated checkout across non-UCP storefronts through human-in-the-loop spend requests: shoppers approve spending caps in the Shop app, releasing temporary one-time credentials for form autofill execution.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4851ae5b081d-cc7ee8a9]

# Lifecycle History
- 2026-09-25: `@shopify/dev-mcp` version 1.16.0 published.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4851ae5b081d-cc7ee8a9]
- 2026-09-28: Checkout WebMCP documentation published specifying browser-based checkout integration.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4851ae5b081d-cc7ee8a9]
- 2026-10-01: `Shopify-AI-Toolkit` v2.1.0 released connecting Cursor plugins to remote merchant MCP endpoints.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4851ae5b081d-cc7ee8a9]
- 2026-10-08: Command-line client `@shopify/shop` version 1.0.3 published.[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4851ae5b081d-cc7ee8a9]

# References
- [Universal Commerce Protocol](../standards/universal-commerce-protocol.md)
- [WebMCP Draft Specification](../standards/webmcp.md)
- [Agentic Commerce Working Group](../working-groups/agentic-commerce.md)

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-4851ae5b081d-cc7ee8a9]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/shopify.yaml
