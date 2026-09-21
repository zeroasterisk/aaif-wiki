---
type: reference-architecture
title: Agent to MCP Server Boundary
description: Cross-boundary telemetry model and gap analysis for agent client interactions
  with Model Context Protocol (MCP) servers.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/32
tags:
- mcp
- observability
- reference-architecture
- traceability
- cross-boundary
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:16:08.415721+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-32
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/32
  author: narko4u
  last_modified: '2026-09-19T04:56:36+00:00'
---

# Overview

The Agent to MCP Server boundary reference architecture details observability, tracing semantics, and telemetry correlation for agent clients invoking Model Context Protocol (MCP) servers [^evt-wg-observability-and-traceability-pr-32]. It maps protocol interactions across eight cross-boundary matrix dimensions: Identity, Context, Relationship, Lifecycle, Outcome, Provenance, Security, and Timing.

# Architecture / Specification

### Core Telemetry Dimensions
- **Declared vs. Observed Divergence:** Identifies critical telemetry gaps where declared server capabilities differ from actual observed runtime execution [^evt-wg-observability-and-traceability-pr-32].
- **Evidence Integrity and Provenance:** Proposes cryptographic verification of tool execution manifests and server responses [^evt-wg-observability-and-traceability-pr-32].
- **Side-Effect Manifests and Consent:** Tracks consent-chain observability across downstream mutations invoked by MCP servers [^evt-wg-observability-and-traceability-pr-32].
- **Reference Implementations:** Demonstrates verification patterns using tools such as mcp-evidence-validator alongside Agent Contract Interfaces [^evt-wg-observability-and-traceability-pr-32].

# References

- [Agent to Tool CLI Boundary](../reference-architectures/agent-tool-cli-boundary.md)
- [Observability and Traceability WG](../working-groups/observability-and-traceability.md)

[^evt-wg-observability-and-traceability-pr-32]: https://github.com/aaif/wg-observability-and-traceability/pull/32
