---
type: taxonomy
title: Agent-to-Agent
description: Universal taxonomy term defining direct communication, task delegation,
  and coordination interactions between autonomous AI agents.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/31
tags:
- taxonomy
- coordination
- delegation
- a2a
- protocols
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:28:12.524255+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-31
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/31
  author: narko4u
  last_modified: '2026-09-19T04:53:51+00:00'
---

# Overview
Agent-to-Agent (A2A) defines direct communication, task delegation, negotiation, and coordination interactions between autonomous AI agents operating across shared or disparate execution environments.[^evt-wg-observability-and-traceability-pr-31] In August 2026, the A2A interoperability layer formally joined the Agentic AI Foundation as a hosted project to standardize multi-agent interaction protocols and identity discovery.[^evt-wg-observability-and-traceability-pr-31]

# Architecture / Specification
Agent-to-agent interactions require standardized mechanisms for discovery, capability advertisement, and execution verification:

- **Protocol Mediation**: Direct communication between agents can be routed through proxies such as [agentgateway](../resources/agentgateway.md) or point-to-point connections.[^evt-wg-observability-and-traceability-pr-31]
- **Signed Agent Cards**: Introduced in A2A v1.0 (March 2026), signed agent cards allow agents to declare capabilities, endpoints, and identity metadata cryptographically.[^evt-wg-observability-and-traceability-pr-31]
- **Runtime Verification Challenge**: Verifying signed card declarations against actual runtime behavior remains an active challenge within the foundation's observability and evidence frameworks.[^evt-wg-observability-and-traceability-pr-31]

# Lifecycle History
- **March 2026**: A2A v1.0 released, introducing signed agent cards for capability and identity declaration.[^evt-wg-observability-and-traceability-pr-31]
- **August 2026**: A2A officially joined the Agentic AI Foundation as a hosted project.[^evt-wg-observability-and-traceability-pr-31]

# References
- [AAIF Observability Prior Work Landscape (PR #31)](https://github.com/aaif/wg-observability-and-traceability/pull/31)

[^evt-wg-observability-and-traceability-pr-31]: https://github.com/aaif/wg-observability-and-traceability/pull/31
