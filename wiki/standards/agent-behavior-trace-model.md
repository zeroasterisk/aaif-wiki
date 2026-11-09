---
type: standard
title: Agent Behavior Trace Model
description: Vendor-neutral telemetry and correlation specification standardizing
  OpenTelemetry semantic conventions and execution trace models across agent lifecycles.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/81dc934a316e97895677257cdc0977f5c3498ea2/reporting/2026-09-report.md
tags:
- standard
- opentelemetry
- trace
- observability
- telemetry
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:28:02.902619+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/81dc934a316e97895677257cdc0977f5c3498ea2/reporting/2026-09-report.md
  author: Pavan Sudheendra
  last_modified: '2026-10-27T05:12:49+00:00'
---

# Overview
The Agent Behavior Trace Model is a vendor-neutral observability specification developed by the [Observability & Traceability Working Group](../working-groups/observability-and-traceability.md)[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]. It defines shared telemetry data contracts, OpenTelemetry semantic conventions, and correlation identifiers capturing autonomous agent trajectories, multi-turn tool loops, and human-in-the-loop decisions[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869].

# Architecture / Specification
### Evidence-Driven Reference Methodology
Following an analysis of production coding agents and agent SDKs that revealed severe OpenTelemetry GenAI implementation inconsistencies—including conflicting span hierarchies, incompatible session attributes, outdated token usage schemas, and nonexistent approval event structures—the working group adopted an evidence-first empirical approach[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869].

The specification uses the open-source [Goose](../resources/goose.md) agent runtime as its baseline reference implementation to evaluate four foundational operational questions[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]:
1. **Continuity:** Maintaining session identity, thread persistence, and agent identity across long-running, multi-turn executions[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869].
2. **Calls and Retries:** Capturing deterministic tool invocations, retries, contextual failovers, and internal model recovery loops[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869].
3. **Approvals:** Formally instrumenting human-in-the-loop checkpoints, policy gate evaluations, and credential release events[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869].
4. **Effects:** Tracing observable external state changes, tool outputs, and downstream environment mutations[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869].

### Implementation & Gap Analysis
Observed discrepancies between real-world agent telemetry emissions and existing OpenTelemetry conventions are cataloged in an active gap register to formulate concrete upstream extension proposals for OpenTelemetry GenAI working groups[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869].

# Lifecycle History
- 2026-09-29: Merged execution plan and shifted deliverable strategy to an empirical evidence-first approach led by Matthew Lee, establishing the Goose baseline capture setup and opening follow-on issues for shared contracts and cross-agent comparison[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869].

[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]: https://github.com/aaif/wg-observability-and-traceability/blob/81dc934a316e97895677257cdc0977f5c3498ea2/reporting/2026-09-report.md
