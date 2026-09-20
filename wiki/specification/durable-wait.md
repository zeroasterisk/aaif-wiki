---
type: specification
title: Durable Wait Pattern
description: A workflow pattern enabling execution runs to logically park state and
  survive process restarts while awaiting external signals, timers, or human approvals.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/durable-wait.md
tags:
- workflow
- pattern
- resilience
- state-management
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:56:41.343367+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/durable-wait.md
  author: Mario Zagar
  last_modified: '2026-08-25T07:58:21-07:00'
- id: evt-wg-workflows-and-process-integration-pr-33
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/33
  author: mzagar
  last_modified: '2026-08-25T14:58:22+00:00'
---

# Overview

The durable wait pattern enables workflow runs to pause and wait for external events, timers, or human decisions over extended durations (hours to days) without relying on process or thread liveness[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7]. By converting an in-memory physical wait into a persisted logical state record, the pattern ensures that workflow executions survive hosting process termination, scheduled restarts, and infrastructure deployments[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].

# Architecture / Specification

When a workflow enters a wait state, it transitions from active execution to a parked state where no compute process holds the run in memory[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].

```text
run ──► record state + position ──► PARKED ⏸      (no process holds the run)
                                       │
     external event / timeout ────────┘──► load the record ──► resume
```

### Invariants

Implementations of the durable wait pattern must enforce four core invariants[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7]:

1. **Survivability**: A parked run survives process termination, restarts, and redeployments.
2. **Context and Position Restoration**: Resuming a run restores its exact activity position and contextual intermediate results rather than re-executing from scratch[^evt-wg-workflows-and-process-integration-pr-33].
3. **Idempotent Resume**: Wake-up signals delivered multiple times must only resume the run once.
4. **Discoverability and Bounded Wait**: Parked runs must remain discoverable and maintain explicit timeouts to prevent indefinitely orphaned executions.

### Relationships and Composition

Durable wait is commonly composed alongside human approval gates (`../specification/human-approval-gate.md`) and proposal/execution splits across single-agent and multi-agent reference architectures (`../specification/workflow-pattern.md`)[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].

[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/durable-wait.md
[^evt-wg-workflows-and-process-integration-pr-33]: https://github.com/aaif/wg-workflows-and-process-integration/pull/33
