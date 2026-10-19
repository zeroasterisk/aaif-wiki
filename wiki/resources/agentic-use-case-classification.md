---
type: resource
title: Agentic Use Case Classification
description: Twelve-column classification schema defining structural dimensions, coordination
  mechanisms, and evidentiary criteria for agent workflows.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/41
tags:
- taxonomy
- classification
- workflows
- governance
- evidence
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:49:23.773344+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-41
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/41
  author: jodeev
  last_modified: '2026-10-01T14:35:56+00:00'
---

# Overview
The Agentic Use Case Classification schema is a standardized taxonomy and structural rubric maintained by the [Workflows & Process Integration Working Group](../working-groups/workflows-and-process-integration.md) to systematically categorize, compare, and validate production agentic implementations [^evt-wg-workflows-and-process-integration-pr-41]. The framework establishes precise metadata definitions across triggers, human-in-the-loop (HITL) gates, multi-agent coordination architectures, and operational constraints [^evt-wg-workflows-and-process-integration-pr-41].

This classification schema serves as the formal foundation for the companion [Agentic Use Case Inventory](../resources/agentic-use-case-inventory.md), ensuring that real-world agent deployments are evaluated against uniform architectural criteria rather than informal marketing claims [^evt-wg-workflows-and-process-integration-pr-41].

# Architecture / Specification

## Structural Dimensions
The schema standardizes twelve core attributes across agentic systems:
1. **Functional Domain**: Horizontal business functions or industry verticals.
2. **Trigger Mechanism**: Event-driven, schedule-based, or manual agent initiation.
3. **Workflow Shape**: Sequence topology, including iterative convergence loops, directed graphs, or parallel swarms.
4. **HITL Pattern**: Enforcement points for human intervention, including patterns like [Human Approval Gate](../patterns/human-approval-gate.md) or [Approval Checkpoint](../patterns/approval-checkpoint.md).
5. **Approval Gate Sub-Type**: Explicit taxonomy for runtime approval requirements and oversight mechanics [^evt-wg-workflows-and-process-integration-pr-41].
6. **Agent Count & Architecture**: Single-agent versus distributed multi-agent systems.
7. **Multi-Agent Rationale**: Mandatory documented justification when classifying workflows as "Better as multi-agent" or "Inherently multi-agent" [^evt-wg-workflows-and-process-integration-pr-41].
8. **Coordination Mechanism**: State machines, message passing, or shared persistent stores.
9. **Failure Modes**: Characteristic vulnerabilities, such as [Context Exhaustion](../taxonomy/context-exhaustion.md) or unconstrained tool recursion.
10. **Preconditions**: Environmental prerequisites, identity assertions, and system dependencies.
11. **Runtime Durations**: Execution envelopes and timeout budgets.
12. **Source Evidence & Citations**: Verifiable references documenting real-world operation [^evt-wg-workflows-and-process-integration-pr-41].

## Evidentiary Standards and Citation Quality
To ensure schema integrity, entries classified under this framework must comply with rigorous verification thresholds [^evt-wg-workflows-and-process-integration-pr-41]:
- **Tier 1 (Preferred)**: Direct vendor product pages or official press releases detailing named, verifiable enterprise customer deployments [^evt-wg-workflows-and-process-integration-pr-41].
- **Tier 2 (Acceptable)**: Vendor product documentation exhibiting documented production-scale features without public customer identification [^evt-wg-workflows-and-process-integration-pr-41].
- **Excluded Sources**: Secondary analyst summaries, academic preprints, unverified third-party blogs, and commercial marketing forecasts are disallowed as primary evidence [^evt-wg-workflows-and-process-integration-pr-41].
- **Citation Health**: Working groups conduct active link-rot mitigation, retiring stale URLs and updating records following corporate rebranding or software acquisitions [^evt-wg-workflows-and-process-integration-pr-41].

[^evt-wg-workflows-and-process-integration-pr-41]: https://github.com/aaif/wg-workflows-and-process-integration/pull/41
