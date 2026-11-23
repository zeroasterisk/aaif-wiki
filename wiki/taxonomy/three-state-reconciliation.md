---
type: taxonomy
title: Three-State Reconciliation
description: Evaluation model comparing an agent claim against independent observation
  across agreement, contradiction, and the explicit absence of independent evidence.
resource: https://github.com/aaif/wg-observability-and-traceability/issues/36
tags:
- observability
- telemetry
- evidence
- control-plane
- taxonomy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:03:41.939015+00:00'
sources:
- id: evt-wg-observability-and-traceability-issue-36
  resource: https://github.com/aaif/wg-observability-and-traceability/issues/36
  author: narko4u
  last_modified: '2026-09-19T04:54:01+00:00'
---

# Overview
Three-State Reconciliation is an architectural evaluation model for agentic telemetry that assesses an agent's self-reported actions against independent control-plane or boundary observations [^evt-wg-observability-and-traceability-issue-36]. Rather than treating telemetry reconciliation as a binary match or mismatch, the model explicitly distinguishes three outcomes: agreement, contradiction, and the absence of independent evidence [^evt-wg-observability-and-traceability-issue-36].

By treating the lack of independent corroboration as an explicit state rather than a silent pass or fail, the model establishes a rigorous basis for evaluating agent claims across untrusted runtime boundaries [^evt-wg-observability-and-traceability-issue-36].

# Architecture / Specification
The reconciliation framework evaluates telemetry along two distinct candidate dimensions before validating claims [^evt-wg-observability-and-traceability-issue-36]:

1. **Observation Source:** Identifies where the telemetry originated, distinguishing agent-emitted runtime traces from tool self-reports, API gateway and proxy logs, runtime-boundary monitors, and external service receipts [^evt-wg-observability-and-traceability-issue-36].
2. **Observation Relationship:** Categorizes what the telemetry asserts relative to the target action, classifying signals as direct observation, corroborating evidence, contradictory evidence, or derived telemetry [^evt-wg-observability-and-traceability-issue-36].

### Reconciliation Triad
When an agent submits an execution claim (e.g., claiming a tool was invoked with specific parameters), the observation layer reconciles the claim into one of three explicit states [^evt-wg-observability-and-traceability-issue-36]:
- **Agreement:** An independent boundary or gateway observer confirms the call occurred as claimed [^evt-wg-observability-and-traceability-issue-36].
- **Contradiction:** An independent boundary observer directly refutes the claim (e.g., observing a failed request, differing parameters, or an unexecuted endpoint) [^evt-wg-observability-and-traceability-issue-36].
- **No Independent Evidence:** No external gateway, proxy, or service observed the interaction, denoting an uncorroborated claim rather than assumed agreement or failure [^evt-wg-observability-and-traceability-issue-36].

# Lifecycle History
- **Issue #36:** Proposed formalizing control-plane telemetry as an independent evidence source and establishing the two-dimension evidence model (Observation Source and Observation Relationship) alongside the three-state reconciliation case [^evt-wg-observability-and-traceability-issue-36].

# References
- Related standard: [Agent Behavior Trace Model](../standards/agent-behavior-trace-model.md)
- Related pattern: [Attested Isolated Runtime](../patterns/attested-isolated-runtime.md)
- Related taxonomy: [Action Record](../taxonomy/action-record.md)

[^evt-wg-observability-and-traceability-issue-36]: https://github.com/aaif/wg-observability-and-traceability/issues/36
