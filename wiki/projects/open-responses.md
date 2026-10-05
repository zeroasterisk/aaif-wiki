---
type: project
title: Open Responses
description: Vendor-neutral specification and conformance test suite for model APIs
  standardizing requests, output items, tool calls, and streaming events.
resource: https://github.com/aaif/project-proposals/issues/41
tags:
- specification
- api
- inference
- conformance
- project-proposal
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:50:17.658922+00:00'
sources:
- id: evt-project-proposals-issue-41
  resource: https://github.com/aaif/project-proposals/issues/41
  author: nickcoai
  last_modified: '2026-09-29T22:21:56+00:00'
---

# Overview
Open Responses is a vendor-neutral specification and conformance project for language-model inference APIs, derived from the OpenAI Responses API design[^evt-project-proposals-issue-41]. It provides model providers, inference gateways, client SDKs, and agent frameworks with a standardized representation for prompt requests, multimodal output items, tool calls, and streaming lifecycle events[^evt-project-proposals-issue-41].

Within the Agentic AI Foundation stack, Open Responses operates at the model-inference layer, complementing runtime agent frameworks like [Goose](../reference-architectures/goose.md) and communication protocols such as [A2A](../projects/a2a.md)[^evt-project-proposals-issue-41].

# Architecture / Specification
The specification and its accompanying test suite establish consistent semantics across model backends while maintaining explicit extension points[^evt-project-proposals-issue-41]:
- **Standardized Payloads**: Common schemas for model requests, responses, tool calls, and structured streaming events[^evt-project-proposals-issue-41].
- **Transport and Lifecycle**: Support for HTTP/REST and WebSocket transports, along with context compaction capabilities[^evt-project-proposals-issue-41].
- **Acceptance and Conformance**: Browser-based and command-line test suites validating provider compliance against date-versioned OpenAPI definitions[^evt-project-proposals-issue-41].
- **Ecosystem Integration**: Designed to integrate with routing gateways and client SDKs without proprietary vendor lock-in[^evt-project-proposals-issue-41].

# Lifecycle History
The proposal was submitted to the [Technical Committee](../governance/technical-committee.md) under the [Project Proposal Process](../governance/project-proposal-process.md) sponsored by OpenAI[^evt-project-proposals-issue-41]. The project operates under an Apache-2.0 license for code and CC-BY-4.0 for specifications with an open Technical Steering Committee (TSC) governance model[^evt-project-proposals-issue-41].

[^evt-project-proposals-issue-41]: https://github.com/aaif/project-proposals/issues/41
