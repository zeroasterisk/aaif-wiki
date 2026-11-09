---
type: architecture
title: Single-Agent Process with Human Approval
description: Reference architecture enforcing an immutable human approval gate between
  an agent proposal and external execution to ensure non-probabilistic authorization
  at the point of effect.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/architectures/single-agent-human-approval.md
tags:
- architecture
- human-in-the-loop
- workflows
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:33:12.467454+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/architectures/single-agent-human-approval.md
  author: Zayne Turner
  last_modified: '2026-11-05T08:39:07-08:00'
- id: evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/reporting/2026-09-report.md
  author: Yaron Schneider
  last_modified: '2026-11-05T08:38:51-08:00'
---

# Overview
The Single-Agent Process with Human Approval reference architecture establishes an enforceable structural break between a probabilistic agent's proposal and a protected external effect[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7]. In this architecture, an agent investigates, calculates, and constructs an action proposal, but lacks the credentials and capabilities to invoke the protected effect directly. A named human reviewer evaluates the immutable proposal, and a dedicated, workflow-controlled executor executes the action only after recording explicit human authorization[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7].

This architecture was unanimously approved as the Workflows & Process Integration Working Group's second voted deliverable at its September 17, 2026 plenary session[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e].

# Architecture / Specification
The reference architecture addresses jobs where an agent's output can alter real systems (such as issuing refunds, executing configuration changes, or sending outbound communications) and requires strict attribution of authority, risk bounding, or auditability[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7].

### Composition of Patterns
The architecture is composed from three core workflow patterns:
- [Proposal/Execution Split](../patterns/proposal-execution-split.md): Enforces that intent generation, approval, and execution belong to separate roles[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7].
- [Human Approval Gate](../patterns/human-approval-gate.md): Intercepts the workflow, requiring explicit authentication and approval from an authorized human before proceeding[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7].
- [Durable Wait](../patterns/durable-wait.md): Ensures the workflow state is durably persisted so that multi-hour or multi-day waits for human authorization survive process restarts, deployments, and crashes without losing state or repeating completed steps[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7].

### Core Invariants
Implementations of this architecture guarantee:
1. **Strict Authority Separation**: The executor capability and credentials that cause the protected effect are inaccessible to the agent. Separation of authority is mandatory even if the executor shares a host process with the agent[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7].
2. **Immutable Authorization**: The executor executes precisely what the human authorized without revisions, re-evaluations, or model-driven modifications[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7].
3. **Complete Attribution Chain**: Every workflow run terminates in an explicit, known terminal state, recording the complete intent-to-decision-to-effect chain (proposer, approver, and executor) in an immutable system of record[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7].

# Lifecycle History
- **2026-09-17**: Voted unanimously and merged on main by the Workflows & Process Integration Working Group plenary[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e].
- **2026-10-02**: Terminology follow-up (PR #50) merged, adopting "activity" for workflow subunits and "business task" for business-level work requests[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e].

[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/reporting/2026-09-report.md
[^evt-wg-workflows-and-process-integration-file-a4fea1b2d544-2fb150b7]: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/architectures/single-agent-human-approval.md
