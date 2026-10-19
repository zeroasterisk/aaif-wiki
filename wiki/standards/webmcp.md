---
type: standard
title: WebMCP
description: Draft Community Group Report of the W3C Web Machine Learning Community
  Group enabling web applications to expose structured client-side tools directly to
  AI browsing agents.
resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/browsers-webmcp.yaml
tags:
- external
- standards
- w3c
- browser
- tools
- agent-web
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T01:54:14.852213+00:00'
sources:
- id: evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9
  resource: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/browsers-webmcp.yaml
  author: frmoretto
  last_modified: '2026-10-14T04:52:24+02:00'
---

# Overview
WebMCP is a Draft Community Group Report of the W3C Web Machine Learning Community Group (not a W3C standards-track specification) that defines a browser API allowing web applications to expose structured client-side tools directly to AI browsing agents [^evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9]. The draft provides an explicit tool-calling channel within web pages, aiming to replace heuristic DOM parsing with typed actions [^evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9].

WebMCP addresses in-browser tool invocation and intersects with the Model Context Protocol (`../standards/model-context-protocol.md`), an AAIF project stewarded under the Agentic AI Foundation, though browser reviewers emphasize that WebMCP operates as an independent browser API rather than the core client-server protocol [^evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9]. It relates to the W3C Agentic Web initiative (`../standards/w3c-agentic-web.md`) and Shopify MCP implementations (`../resources/shopify-mcp.md`).

# Architecture / Specification
WebMCP defines client-side tool registry and invocation conventions in web browsers [^evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9]:
- **Structured Page Tools**: Sites expose typed interfaces directly to user agents, enabling operations such as product search, cart manipulation, and appointment bookings [^evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9].
- **Browser Vendor Positions**:
  - **Google Chrome**: Provided an early preview describing WebMCP as a standard format for exposing structured tools to AI agents [^evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9].
  - **Microsoft Edge**: Announced implementation readiness for developer testing [^evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9].
  - **Mozilla**: Adopted a neutral position, raising concerns that adversarial websites might expose tool capabilities divergent from the visual experience presented to users [^evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9].
  - **Apple WebKit**: Closed its position as opposed, citing lack of explicit consent and reversibility models for consequential actions [^evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9].
- **Merchant Integrations**:
  - **PayPal**: Deployed WebMCP in its JavaScript SDK for Store Sync merchants, enabling agents to search items and build carts while enforcing human sign-in and approval for payments [^evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9].
  - **Shopify**: Released Checkout WebMCP tools (`get_checkout`, `update_checkout`, `complete_checkout`), requiring explicit buyer permission before order submission [^evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9].

# Lifecycle History
- 2026-02-10: Google Chrome announces developer preview of WebMCP [^evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9].
- 2026-06-11: WebKit standards position issue closed as opposed [^evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9].
- 2026-08-05: Mozilla standards position issue closed as neutral [^evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9].
- 2026-09-21: Microsoft Edge announces implementation ready for testing [^evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9].
- 2026-10-08: PR #338 removed the declarative API from the draft [^evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9].

# References
- WebKit Standards Position #670: https://github.com/WebKit/standards-positions/issues/670
- Mozilla Standards Position #1412: https://github.com/mozilla/standards-positions/issues/1412
- Agentic Standards Map WebMCP Entry: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/browsers-webmcp.yaml

[^evt-ext-frmoretto-agentic-standards-map-85d122-file-faeec7da37c7-0cb706f9]: https://github.com/frmoretto/agentic-standards-map/blob/b7ea348f961457df551928597041fc428e37e169/entries/browsers-webmcp.yaml
