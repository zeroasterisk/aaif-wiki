---
type: pattern
title: Human Approval Gate
description: Workflow governance pattern requiring an explicit, authorized human decision
  bound to an immutable proposal before causing a protected effect.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/human-approval-gate.md
tags:
- pattern
- workflows
- governance
- approval
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T09:56:55.475973+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/human-approval-gate.md
  author: Zayne Turner
  last_modified: '2026-08-05T23:05:12-04:00'
---

# Overview
The Human Approval Gate pattern ensures that a workflow reaching an action with elevated risk, audit obligations, or ownership requirements pauses until an accountable, uniquely identified human principal authorizes the exact proposal [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]. The pattern binds decisions directly to specific immutable proposal versions and enforces that execution remains safely suspended until approval is explicitly granted.

It is paired with the [Proposal/Execution Split](../patterns/proposal-execution-split.md) and [Durable Wait](../patterns/durable-wait.md) patterns, and serves as a core building block for reference architectures such as the [Single-Agent Process with Human Approval](../architectures/single-agent-human-approval.md) [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].

# Architecture / Specification
The pattern addresses common failure modes in asynchronous human reviews, including proposal drift, process lifetime limits exceeding human response delays, non-attributable shared accounts, and race conditions between late approvals and timeout escalations [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].

```text
immutable proposal ──► present to authorized human ──► explicit decision
                              │                           │
                              └── durable wait ─────────┘
                                          │
                          decision record: who · what · when
```

### Invariants
To maintain system safety and auditability, implementations must satisfy the following invariants [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]:
- **Principal Attribution**: Approvers must be uniquely identified human principals authorized for the specific decision class; shared approval accounts are invalid.
- **Immutable Proposal Binding**: The interaction surface must present the exact, immutable proposal version to which the decision binds.
- **Explicit Decisions**: Approval and rejection must be active, explicit decisions; silence, timeouts, delivery errors, or system failures never imply approval.
- **Unified Decision Record**: Decision records must capture proposal version, approver identity, explicit outcome, and timestamp within the same workflow run identity.
- **Proposal Invalidation**: Any mutation or supersession of the proposal invalidates pending reviews and requires a fresh decision.
- **Bounded Duration**: Pending approval requests require explicit deadlines, expiration parameters, or escalation pathways.
- **Idempotent Execution**: Duplicate, conflicting, or delayed decision events must not trigger redundant workflow resumptions or double executions.

[^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/human-approval-gate.md
