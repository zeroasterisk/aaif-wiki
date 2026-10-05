---
type: proposal
title: Open Responses
description: Vendor-neutral API specification and conformance test suite standardizing
  language model requests, output items, and tool calls.
resource: https://github.com/aaif/project-proposals/issues/41
tags:
- proposal
- api
- inference
- tool-use
- interoperability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:18:07.441771+00:00'
sources:
- id: evt-project-proposals-issue-41
  resource: https://github.com/aaif/project-proposals/issues/41
  author: nickcoai
  last_modified: '2026-09-29T22:21:56+00:00'
---

# Overview

Open Responses is a vendor-neutral API specification and conformance test suite for language-model inference interfaces, derived from OpenAI's Responses API[^evt-project-proposals-issue-41]. It provides model providers, inference gateways, client libraries, and agent frameworks with a standardized contract representing model requests, output items, multimodal content, tool calls, and streaming events[^evt-project-proposals-issue-41].

Within the broader agentic stack, Open Responses addresses the model-inference layer, complementing protocols like Model Context Protocol (MCP) and agent frameworks such as `../reference-architectures/goose.md`[^evt-project-proposals-issue-41].

# Architecture / Specification

The Open Responses specification defines a standard protocol across several functional layers[^evt-project-proposals-issue-41]:

- **Inference Lifecycle Contract**: Standardizes request envelopes, output items, multimodal payload structures, and tool call invocations.
- **Transport & Streaming**: Supports HTTP streaming interfaces, WebSocket transport, and compaction capabilities across dated specification releases[^evt-project-proposals-issue-41].
- **Conformance & Acceptance Testing**: Provides machine-readable OpenAPI schemas alongside browser-based and CLI test suites to validate provider implementations against semantic standards[^evt-project-proposals-issue-41].

# Lifecycle History

The Open Responses project was launched publicly in January 2026 and submitted to the Agentic AI Foundation as a project proposal under the sponsorship of Nick Cooper (OpenAI)[^evt-project-proposals-issue-41]. The project operates under an Apache-2.0 code license and CC-BY-4.0 specification license managed by a Technical Steering Committee (TSC) ensuring multi-vendor governance[^evt-project-proposals-issue-41].

[^evt-project-proposals-issue-41]: https://github.com/aaif/project-proposals/issues/41
