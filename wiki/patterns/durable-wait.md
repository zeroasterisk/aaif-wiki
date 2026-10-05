---
type: pattern
title: Durable Wait Pattern
description: Workflow design pattern decoupling execution wait states from hosting
  process lifetimes by persisting run position, context, and identity until an external
  event or timeout occurs.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/durable-wait.md
tags:
- workflows
- patterns
- persistence
- orchestration
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:02:30.239461+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/durable-wait.md
  author: Mario Zagar
  last_modified: '2026-08-25T07:58:21-07:00'
---

# Overview

The Durable Wait pattern decouples a workflow run's execution wait state from the transient lifetime of the underlying host process[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7]. In long-running agentic workflows where runs must pause for hours or days awaiting human approval, timers, or external system events, hosting processes frequently terminate, restart, or redeploy. This pattern transforms a physical wait (a blocked thread or process) into a logical wait stored as a persistent record in an execution state store.

The pattern is a core dependency of architectures featuring asynchronous intervention, such as the [Human Approval Gate](../patterns/human-approval-gate.md) and proposal/execution split workflows, ensuring runs survive infrastructure lifecycle changes without compute waste or state loss[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].

# Architecture / Specification

When a workflow encounters a wait condition, the runtime engine records the execution state and position before transitioning the run to a `PARKED` state[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7]. While parked, no compute process holds the run in memory.

```text
run ──► record state + position ──► PARKED ⏸      (no process holds the run)
                                       │
     external event / timeout ────────┘──► load the record ──► resume
```

### Restoration Invariants

Resuming a parked run is triggered by an external event or timeout and restores three mandatory runtime properties[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7]:
- **Position**: Identifies the exact activity where execution was paused.
- **Context**: Re-establishes the inputs, intermediate outputs, and execution memory necessary for continuation without re-executing previous activities.
- **Identity**: Correlates external wake-up signals with the correct run instance.

### Core Invariants

Implementations of durable wait must satisfy the following architectural invariants[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7]:
- **Process Independence**: Parked runs remain preserved across process crashes, restarts, and service redeployments.
- **Idempotent Resume**: Duplicate wake-up event deliveries result in a single workflow resumption.
- **Discoverability**: Parked runs are queryable and observable by operations tooling rather than becoming untracked dormant state.
- **Bounded Duration**: Waits must support explicit timeouts to prevent indefinitely orphaned executions.

[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/durable-wait.md
