---
type: taxonomy
title: Three-State Reconciliation
description: Classification framework evaluating agent self-reported claims against
  independent boundary observations into agreement, contradiction, or no independent
  evidence.
resource: https://github.com/aaif/wg-observability-and-traceability/issues/36
tags:
- observability
- telemetry
- verification
- reconciliation
- evidence
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:28:12.524255+00:00'
sources:
- id: evt-wg-observability-and-traceability-issue-36
  resource: https://github.com/aaif/wg-observability-and-traceability/issues/36
  author: narko4u
  last_modified: '2026-09-19T04:54:01+00:00'
---

# Overview
Three-State Reconciliation is a telemetry evaluation model that compares an agent's self-reported execution claims against independent boundary observations, producing one of three explicit reconciliation states: agreement, contradiction, or no independent evidence.[^evt-wg-observability-and-traceability-issue-36] By treating the absence of independent evidence as an explicit third state rather than a silent default or assumption of agreement, it establishes clear semantics for runtime trust.[^evt-wg-observability-and-traceability-issue-36]

# Architecture / Specification
Three-State Reconciliation addresses the measurement gap between agent self-reports and independently observed control-plane telemetry (such as gateway, proxy, or runtime boundary telemetry).[^evt-wg-observability-and-traceability-issue-36] Evidence trustworthiness is modeled across two distinct dimensions:

1. **Observation Source**: Identifies where the telemetry originated:
   - Agent / runtime self-reports
   - Tool-level instrumentation
   - Gateway / proxy control planes
   - External systems[^evt-wg-observability-and-traceability-issue-36]
2. **Observation Relationship**: Characterizes what the signal asserts about the claimed action:
   - Direct observation
   - Corroborating
   - Contradictory
   - Derived from secondary telemetry[^evt-wg-observability-and-traceability-issue-36]

### Reconciliation Outcomes
Comparing agent claims against independent observations yields three formal states:
- **Agreement (Corroboration)**: Independent boundary observations confirm that the action took place as claimed.[^evt-wg-observability-and-traceability-issue-36]
- **Contradiction**: Independent boundary observations conflict with or refute the agent's claim.[^evt-wg-observability-and-traceability-issue-36]
- **No Independent Evidence**: The boundary lacks telemetry to confirm or refute the claim, avoiding silent assumptions of validity.[^evt-wg-observability-and-traceability-issue-36]

This framework operates in conjunction with boundary models such as [Cross-Boundary Observability Model](../resources/cross-boundary-observability-model.md) and [Agent-MCP Server Boundary](../resources/agent-mcp-server-boundary.md).

# Lifecycle History
- **2026**: Proposed in the Observability and Traceability Working Group as a candidate evidence model (Theme 10 / Open Question 9).[^evt-wg-observability-and-traceability-issue-36]

# References
- [Issue #36: Control-plane telemetry as an evidence source](https://github.com/aaif/wg-observability-and-traceability/issues/36)

[^evt-wg-observability-and-traceability-issue-36]: https://github.com/aaif/wg-observability-and-traceability/issues/36
