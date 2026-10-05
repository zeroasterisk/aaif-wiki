---
type: project
title: Agent-to-Agent Protocol (A2A)
description: Hosted open interoperability protocol standardizing communication, discovery,
  and signed agent cards between autonomous AI agents.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/31
tags:
- projects
- protocols
- interoperability
- agent-to-agent
- identity
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:43:33.394704+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-31
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/31
  author: narko4u
  last_modified: '2026-09-19T04:53:51+00:00'
---

# Overview

The Agent-to-Agent Protocol (A2A) is an AAIF hosted project establishing a vendor-neutral interoperability layer for direct communication, capability discovery, and task delegation between autonomous AI agents [^evt-wg-observability-and-traceability-pr-31]. A2A introduced signed agent cards to declare capabilities and trust metadata, providing a foundation for multi-agent coordination and mediation [^evt-wg-observability-and-traceability-pr-31].

# Architecture / Specification

## Core Capabilities

- **Signed Agent Cards**: Self-describing cryptographically signed metadata documents detailing agent capabilities, authentication endpoints, and operational constraints [^evt-wg-observability-and-traceability-pr-31].
- **Interoperability & Mediation**: Compatible with runtime traffic mediation gateways such as `agentgateway` for policy enforcement and routing across MCP and A2A networks [^evt-wg-observability-and-traceability-pr-31].
- **Verification & Telemetry**: Integrates with observability standards to enable runtime verification of signed card claims against observed agent behavior and execution telemetry [^evt-wg-observability-and-traceability-pr-31].

# Lifecycle History

- **March 2026**: A2A v1.0 specification released introducing signed agent cards [^evt-wg-observability-and-traceability-pr-31].
- **August 2026**: Formally joined the Agentic AI Foundation as a hosted project [^evt-wg-observability-and-traceability-pr-31].

# References

- [Identity and Trust Working Group](../working-groups/identity-and-trust.md)
- [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md)

[^evt-wg-observability-and-traceability-pr-31]: https://github.com/aaif/wg-observability-and-traceability/pull/31
