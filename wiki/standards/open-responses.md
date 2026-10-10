---
type: standard
title: Open Responses
description: Vendor-neutral specification and conformance suite standardizing language
  model request, response, streaming, and tool-call APIs.
resource: https://github.com/aaif/project-proposals/issues/41
tags:
- standards
- inference
- model-api
- tool-calling
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:12:58.013933+00:00'
sources:
- id: evt-project-proposals-issue-41
  resource: https://github.com/aaif/project-proposals/issues/41
  author: nickcoai
  last_modified: '2026-09-29T22:21:56+00:00'
---

# Overview
Open Responses is a vendor-neutral specification and conformance project that defines standard application programming interfaces for language-model inference, output items, multimodal payloads, tool calls, and streaming events [^evt-project-proposals-issue-41]. Derived from the OpenAI Responses API, it establishes a shared model-inference contract across foundation model providers, inference gateways, client libraries, and agent frameworks [^evt-project-proposals-issue-41].

# Architecture / Specification
Open Responses establishes a common inference layer within the agentic stack, complementing tool-integration protocols such as the [Model Context Protocol](../resources/mcp-gateway-registry.md) and agent runtimes like [Goose](../resources/goose.md) [^evt-project-proposals-issue-41]:
- **Inference Protocol**: Defines structured representations for model requests, output item lifecycles, and streaming events across HTTP and WebSocket transports [^evt-project-proposals-issue-41].
- **Tool Invocations**: Standardizes how tool definitions, execution requests, and tool outputs are represented in model exchanges [^evt-project-proposals-issue-41].
- **Acceptance & Conformance Suites**: Supplies machine-readable OpenAPI schemas, date-versioned snapshots, and browser/CLI conformance test suites to validate provider interoperability [^evt-project-proposals-issue-41].

# Lifecycle History
In July 2026, Open Responses was submitted as an open project proposal to the Agentic AI Foundation [Technical Committee](../governance/technical-committee.md) under Apache-2.0 and CC-BY-4.0 licensing with multi-vendor technical steering committee governance [^evt-project-proposals-issue-41].

# References
- AAIF Project Proposals: [Issue #41](https://github.com/aaif/project-proposals/issues/41) [^evt-project-proposals-issue-41]

[^evt-project-proposals-issue-41]: https://github.com/aaif/project-proposals/issues/41
