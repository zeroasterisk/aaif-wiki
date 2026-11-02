---
type: taxonomy
title: Three-State Reconciliation
description: Evaluation model comparing an agent claim against independent observation
  across agreement, contradiction, and absence of independent evidence.
resource: https://github.com/aaif/wg-observability-and-traceability/issues/36
tags:
- taxonomy
- reconciliation
- evidence
- telemetry
- assurance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:01:23.012889+00:00'
sources:
- id: evt-wg-observability-and-traceability-issue-36
  resource: https://github.com/aaif/wg-observability-and-traceability/issues/36
  author: narko4u
  last_modified: '2026-09-19T04:54:01+00:00'
---

# Overview
Three-State Reconciliation is an evaluation taxonomy and verification model defining the evidential relationship between an agent's self-reported claim and independent boundary observations [^evt-wg-observability-and-traceability-issue-36]. Departing from binary confirmation defaults, the model explicitly distinguishes between agreement, contradiction, and the complete absence of independent corroborating evidence [^evt-wg-observability-and-traceability-issue-36].

# Architecture / Specification

## Evidence Evaluation Dimensions
To measure signal trustworthiness across agent runtimes and network gateways, evidence is categorized across two operational dimensions [^evt-wg-observability-and-traceability-issue-36]:

1. **Observation Source**: Identifies the origin of the boundary signal, distinguishing:
   - Agent or runtime self-reports
   - Tool execution receipts
   - Gateway or proxy telemetry
   - External enterprise systems of record [^evt-wg-observability-and-traceability-issue-36].
2. **Observation Relationship**: Characterizes what the telemetry asserts regarding the target action:
   - Direct observation of the action
   - Corroborating evidence
   - Contradictory evidence
   - Derived telemetry generated from secondary signals [^evt-wg-observability-and-traceability-issue-36].

## Reconciliation States
Comparing an agent's claimed execution against boundary telemetry produces one of three distinct states [^evt-wg-observability-and-traceability-issue-36]:
- **Agreement**: Independent boundary telemetry corroborates or directly witnesses the action reported by the agent.
- **Contradiction**: Independent boundary observations directly conflict with the agent's claim, parameters, or reported outcome.
- **No Independent Evidence**: No gateway, proxy, or boundary telemetry captured the interaction; this absence is treated as an explicit, measurable state rather than defaulting to presumed compliance.

# References
- [Agent Observability Prior Work Landscape](../resources/agent-observability-prior-work.md)
- [Agent Behavior Trace Model](../standards/agent-behavior-trace-model.md)
- [agentgateway](../resources/agentgateway.md)
- [Evidence Record Specification](../standards/evidence-record-spec.md)

[^evt-wg-observability-and-traceability-issue-36]: https://github.com/aaif/wg-observability-and-traceability/issues/36
