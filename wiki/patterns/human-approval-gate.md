---
type: pattern
title: Human Approval Gate
description: Workflow governance pattern requiring explicit, authenticated authorization
  from a uniquely identified human before executing a protected agent action.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/human-approval-gate.md
tags:
- pattern
- workflows
- governance
- human-in-the-loop
- authorization
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T09:43:46.015740+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/human-approval-gate.md
  author: Zayne Turner
  last_modified: '2026-08-05T23:05:12-04:00'
---

# Overview
The Human Approval Gate pattern mandates that an authenticated, uniquely identified human principal reviews and explicitly decides whether an immutable proposal may execute a protected effect.[^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428] Designed for workflows where actions carry high risk, legal exposure, or audit obligations, this pattern parks execution safely in a durable wait state until an explicit authorization decision binds to the exact version of the reviewed proposal.[^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]

The pattern is composed within reference architectures such as [Single-Agent Process with Human Approval](../architectures/single-agent-human-approval.md) and directly coordinates with the [Proposal/Execution Split](../patterns/proposal-execution-split.md) and [Durable Wait](../patterns/durable-wait.md) patterns.[^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]

# Architecture / Specification

## Core Flow
```text
immutable proposal ──► present to authorized human ──► explicit decision
                              │                           │
                              └── durable wait ─────────┘
                                          │
                          decision record: who · what · when
```

An execution engine surfaces an immutable action proposal across a human interaction surface to an authorized approver. While awaiting input, the workflow engine transitions into a durable wait state. When the human approves or rejects, an immutable decision record capturing the who, what, and when is persisted to the audit log under the same workflow run identity.[^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]

## Required Capabilities
Implementations of this pattern require four foundational system capabilities:[^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]
- **Execution engine**: Capable of halting and resuming execution safely based on external asynchronous events.
- **Human interaction surface**: Renders the complete, immutable proposal payload for inspection.
- **State/context store**: Persists workflow execution state, timers, and proposal versions during extended pauses.
- **Audit log**: Captures tamper-evident records of approval credentials, timestamps, and decision outcomes.

## Invariants
Any conformant implementation must satisfy the following invariants:[^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]
- The approver must be a uniquely identified human principal authorized for the decision class; shared approval accounts or generic tokens do not qualify.
- The interaction surface must display the exact, immutable proposal version to which the subsequent decision will bind.
- Approval and rejection must be explicit decisions; silence, timeouts, delivery failures, or system errors must never evaluate to implicit approval.
- The decision record must atomically capture the proposal version, approver identity, explicit decision, and timestamp under the same run identity.
- Any modification or supersession of a pending proposal invalidates previous reviews and mandates a new approval decision.
- Pending approval requests must define an explicit deadline with deterministic expiration or escalation paths.
- Duplicate, late, or conflicting decision events must not cause duplicate resumption or multiple executions of the protected action.

## Failure Modes
Violating pattern invariants introduces distinct operational and security failures:[^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]
- **Shared Approver Accounts**: Masks individual attribution, preventing non-repudiation in audit trails.
- **Mutable Proposals**: Allows an action to change between human review and backend execution, creating time-of-check to time-of-use (TOCTOU) vulnerabilities.
- **Implicit Approval on Timeout**: Degrades security boundaries by treating communication outages or human inaction as authorization.
- **Race Conditions on Late Delivery**: Allows duplicate execution of sensitive side-effects if approval messages arrive concurrently with timeout handlers.

# References
- Workflows and Process Integration WG: [Human Approval Gate Pattern Specification](https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/human-approval-gate.md)[^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]

[^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/human-approval-gate.md
