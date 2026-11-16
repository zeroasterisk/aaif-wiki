---
type: resource
title: Agent Observability Prior Work Landscape
description: Comparative landscape survey evaluating specifications, platforms, and
  hosted protocols across agent telemetry, identity cards, and runtime mediation.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/31
tags:
- observability
- landscape
- prior-work
- standards
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:13:40.113419+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-31
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/31
  author: narko4u
  last_modified: '2026-09-19T04:53:51+00:00'
---

# Overview
The agent observability prior work landscape evaluates emerging open specifications, commercial platforms, and hosted foundational protocols to identify architectural coverage and unaddressed gaps across agentic telemetry.[^evt-wg-observability-and-traceability-pr-31] Maintained by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), the survey documents how projects handle execution tracing, capability boundaries, identity verification, and runtime governance.[^evt-wg-observability-and-traceability-pr-31]

Recent additions evaluate hosted foundation projects including [A2A](../taxonomy/agent-to-agent.md) and [agentgateway](agentgateway.md), identifying key strengths in runtime traffic control and exposing an unclaimed evidence layer gap across agent communications.[^evt-wg-observability-and-traceability-pr-31]

# Architecture / Specification
The landscape framework categorizes agent runtime tools across scope, maturity, licensing, and key technical capabilities.[^evt-wg-observability-and-traceability-pr-31]

## Hosted Project Additions
- **A2A**: Joined the foundation in August 2026 to serve as the agent-to-agent interoperability layer.[^evt-wg-observability-and-traceability-pr-31] It introduces signed agent cards for discovery and capability declaration, though verifying signed card claims against actual runtime behavior remains an unresolved challenge.[^evt-wg-observability-and-traceability-pr-31]
- **agentgateway**: Joined the foundation in June 2026 to mediate traffic and enforce policies across Model Context Protocol (MCP) and A2A communications, providing deployment options across major cloud marketplaces.[^evt-wg-observability-and-traceability-pr-31]

## Evidence Layer Gap
A critical gap identified across surveyed technologies is the missing evidence layer.[^evt-wg-observability-and-traceability-pr-31] While transport mediation and signed declarations establish perimeter identity, existing frameworks lack verifiable mechanisms linking runtime tool execution, agent identity claims, and non-repudiable audit logs.[^evt-wg-observability-and-traceability-pr-31]

[^evt-wg-observability-and-traceability-pr-31]: https://github.com/aaif/wg-observability-and-traceability/pull/31
