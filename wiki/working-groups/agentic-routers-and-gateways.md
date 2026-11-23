---
type: working-group
title: Agentic Routers and Gateways Working Group
description: Proposed AAIF working group defining shared architecture, intermediary
  protocols, and conformance tests for agent routers and gateways.
resource: https://github.com/aaif/working-group-proposals/issues/7
tags:
- working-group
- gateway
- router
- governance
- interoperability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:37:33.064753+00:00'
sources:
- id: evt-working-group-proposals-issue-7
  resource: https://github.com/aaif/working-group-proposals/issues/7
  author: CharnaParkey
  last_modified: '2026-11-20T16:46:33+00:00'
---

# Overview

The Agentic Routers and Gateways Working Group is a proposed technical working group within the Agentic AI Foundation (AAIF) tasked with standardizing the intermediary layer connecting AI agents to models, tools, and peer agents[^evt-working-group-proposals-issue-7]. In production deployments, routers and gateways mediate communication flows across protocols including Model Context Protocol (MCP), Agent-to-Agent (A2A), and model provider APIs.

The proposal addresses architectural fragmentation where implementations partition data planes, control planes, policy enforcement, and credential brokering incompatibly, while protocols lack prescriptive specifications for proxy behavior regarding streaming, tool lists, and error propagation[^evt-working-group-proposals-issue-7].

# Architecture / Specification

The working group's proposed scope includes:
- Developing a layered reference architecture distinguishing the data plane, control plane, registry or catalog integration, policy decision/enforcement points, credential brokering, usage accounting, and telemetry export across central, sidecar, mesh, and embedded deployment topologies[^evt-working-group-proposals-issue-7].
- Defining intermediary behavior profiles specifying mandatory and prohibited proxy actions when handling MCP, A2A, and LLM requests[^evt-working-group-proposals-issue-7].
- Establishing vendor-neutral interfaces between gateways and surrounding policy engines, identity providers, and registries[^evt-working-group-proposals-issue-7].
- Implementing an open, implementation-agnostic conformance test suite and coordinating interoperability validation[^evt-working-group-proposals-issue-7].

Explicit boundaries place threat modeling under the [Security & Privacy Working Group](../working-groups/security-and-privacy.md), telemetry data models under the [Observability & Traceability Working Group](../working-groups/observability-and-traceability.md), identity protocols under the [Identity & Trust Working Group](../working-groups/identity-and-trust.md), and Kubernetes Gateway APIs under upstream working groups[^evt-working-group-proposals-issue-7].

# Lifecycle History

- Proposed in November 2026 by Charna Parkey (IBM) via AAIF working-group-proposals issue #7[^evt-working-group-proposals-issue-7].

[^evt-working-group-proposals-issue-7]: https://github.com/aaif/working-group-proposals/issues/7
