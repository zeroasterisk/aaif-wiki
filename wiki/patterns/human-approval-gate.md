---
type: pattern
title: Human Approval Gate
description: Workflow pattern requiring an authorized, uniquely identified human to
  explicitly approve an immutable proposal before a workflow executes a protected
  effect.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/human-approval-gate.md
tags:
- pattern
- governance
- approval
- workflows
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T02:47:31.904164+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/human-approval-gate.md
  author: Zayne Turner
  last_modified: '2026-08-05T23:05:12-04:00'
---

# Overview

The Human Approval Gate pattern halts execution before a protected effect until a uniquely identified, authorized human principal makes an explicit decision on an immutable proposal [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]. It ensures that human judgment is captured within a durable, tamper-evident record linking who reviewed, what version was reviewed, and the exact decision rendered before downstream execution proceeds [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].

# Architecture / Specification

The pattern mediates between proposal generation and executor action:
```text
immutable proposal ──► present to authorized human ──► explicit decision
                              │                           │
                              └── durable wait ─────────┘
                                          │
                          decision record: who · what · when
```

### Invariants
- **Unique Human Principal**: The approver must be an individually authenticated human holding authorization for the specific decision class; shared role accounts are disallowed [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].
- **Proposal Immutability**: The interaction surface must display the exact proposal payload that binds to execution. Any mutation or superseding proposal invalidates pending reviews and requires a fresh decision [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].
- **Explicit Affirmation**: Approval and rejection must be explicit; timeouts, queue silence, delivery failures, or system crashes must never default to approval [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].
- **Deterministic Decision Binding**: The resulting decision record couples run identifier, proposal version, approver identity, decision status, and timestamps [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].
- **Idempotency & Race Safety**: Out-of-order, late, or duplicated decisions cannot trigger duplicate resumes or executions [^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428].

### Related Patterns
- [Proposal-Execution Split](../patterns/proposal-execution-split.md)
- [Durable Wait](../patterns/durable-wait.md)
- [Approval Checkpoint](../patterns/approval-checkpoint.md)

[^evt-wg-workflows-and-process-integration-file-3e360b3d4277-1647d428]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/human-approval-gate.md
