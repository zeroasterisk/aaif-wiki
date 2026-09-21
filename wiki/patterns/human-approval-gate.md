---
type: pattern
title: Human Approval Gate
description: Workflow pattern requiring an identified human principal to explicitly
  authorize an immutable proposal before execution of a protected effect.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/human-approval-gate.md
tags:
- workflows
- patterns
- governance
- human-in-the-loop
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:50:59.369101+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/human-approval-gate.md
  author: Zayne Turner
  last_modified: '2026-08-05T23:05:12-04:00'
- id: evt-wg-workflows-and-process-integration-pr-20
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/20
  author: zaynelt
  last_modified: '2026-08-06T03:05:13+00:00'
---

# Overview
The human approval gate pattern addresses workflow scenarios where an agent reaches an action whose risk, audit obligations, or ownership requires judgment from an accountable human before execution occurs [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]. The pattern ensures that the approval decision binds directly and immutably to the exact proposal presented, keeping the workflow safely parked in a durable state until an explicit decision is recorded [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].

Developed under the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md), it is used within composed architectures such as single-agent processes with human approval and operates alongside companion patterns including the proposal/execution split and durable wait [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428][^evt-wg-workflows-and-process-integration-pr-20].

# Architecture / Specification
The pattern relies on four core capability roles: an execution engine, a human interaction surface, a state/context store, and an audit log [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].

### Invariants
Implementations must guarantee the following invariants regardless of the underlying runtime platform [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]:
- **Identified Approver:** The approver must be a uniquely identified human principal authorized for the decision category; shared approval credentials are not permitted [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].
- **Immutable Proposal Presentation:** The presentation surface must display the exact, immutable proposal version to which the decision binds [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].
- **Explicit Decision:** Approval and rejection must be explicit actions. Timeouts, silence, delivery failures, or system errors never imply approval [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].
- **Audit Traceability:** The decision record captures the proposal version, approver identity, decision value, and timestamp under the same run execution identity [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].
- **Supersession Invalidation:** Any modification or supersession of a proposal invalidates previous state and requires a fresh approval decision [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].
- **Bounded Waiting:** Pending approvals must define deadlines with explicit expiration or escalation pathways [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].
- **Execution Idempotency:** Duplicate, late, or conflicting decision events cannot trigger multiple run resumptions or executions [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].

[^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/human-approval-gate.md
[^evt-wg-workflows-and-process-integration-pr-20]: https://github.com/aaif/wg-workflows-and-process-integration/pull/20
