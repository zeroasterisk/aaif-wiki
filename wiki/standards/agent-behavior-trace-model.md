---
type: standard
title: Agent Behavior Trace Model
description: Open telemetry and correlation specification standardizing agent execution
  entities, turn boundaries, and evidence-backed OpenTelemetry trace conventions.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/81dc934a316e97895677257cdc0977f5c3498ea2/reporting/2026-09-report.md
tags:
- standard
- observability
- opentelemetry
- tracing
- goose
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:38:09.419537+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/81dc934a316e97895677257cdc0977f5c3498ea2/reporting/2026-09-report.md
  author: Pavan Sudheendra
  last_modified: '2026-10-27T05:12:49+00:00'
---

# Overview

The Agent Behavior Trace Model is an open telemetry and correlation specification stewarded by the [Observability & Traceability Working Group](../working-groups/observability-and-traceability.md).[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869] The specification defines structural representations for agent execution trajectories, turn boundaries, causal call chains, approval gates, and state-change outcomes.[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]

Following an empirical survey of major coding agents and agent SDKs, the working group discovered substantial discrepancies in OpenTelemetry GenAI semantic convention compliance—including divergent span hierarchies, conflicting session identifiers, outdated token usage metrics, and absent human-in-the-loop approval representations.[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869] Consequently, the specification development strategy shifted from theoretical specification authoring to an evidence-driven methodology anchored on real-world runtime emissions from [Goose](../resources/goose.md).[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]

# Architecture / Specification

### Core Behavioral Dimensions

The trace model evaluates agent execution records against four foundational behavioral questions:[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]
1. **Continuity:** How execution identity, session parentage, and trajectory steps persist across multi-turn exchanges and agent interruptions.[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]
2. **Calls and Retries:** How external tool invocations, retried failures, and fallback strategies are recorded across client and server protocol boundaries.[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]
3. **Approvals:** How interactive human-in-the-loop authorization gates and policy checks are represented within trace contexts.[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]
4. **Effects:** How tangible environmental side effects, tool outputs, and downstream state mutations are causally linked to initiating spans.[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]

### Evidence-Driven Reference Architecture (Goose Baseline)

Rather than implementing an isolated greenfield specification, the working group utilizes [Goose](../resources/goose.md)—the AAIF native general-purpose agent runtime—as its reference implementation platform:[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]
- **Baseline Telemetry Ingestion:** Capturing baseline OpenTelemetry spans and logs emitted by Goose during standardized multi-step tasks.[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]
- **Gap Register:** Logging identified telemetry omissions and span structural deficits against the four core behavioral dimensions.[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]
- **Upstream Collaboration:** Proposing targeted semantic extensions directly to upstream OpenTelemetry working groups backed by empirical capture artifacts.[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]

# Lifecycle History

- **2026-07-31:** Initial charter deliverable target scheduled for trace model recommendations.[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]
- **2026-09-29:** Execution plan formally merged under lead Matthew Lee, restructuring follow-on workstreams into an evidence-first order and establishing the Goose reference capture harness.[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]

# References

[^evt-wg-observability-and-traceability-file-60f28464dd94-2a91d869]: Observability & Traceability Working Group September 2026 Report (`reporting/2026-09-report.md`).
