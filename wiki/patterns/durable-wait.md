---
type: pattern
title: Durable Wait
description: Workflow pattern converting in-memory execution waits into durable state
  records to survive process termination, deploys, and restarts.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/durable-wait.md
tags:
- pattern
- workflow
- persistence
- orchestration
- resilience
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:36:19.816203+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/durable-wait.md
  author: Mario Zagar
  last_modified: '2026-08-25T07:58:21-07:00'
- id: evt-wg-workflows-and-process-integration-pr-33
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/33
  author: mzagar
  last_modified: '2026-08-25T14:58:22+00:00'
---

# Overview

The Durable Wait pattern decouples workflow run persistence from transient host process lifecycles, enabling workflows to pause for hours or days awaiting external events, timer expirations, or human intervention [^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7]. By transforming a physical blocking thread or process wait into a logically recorded parked state, the workflow run survives process restarts, host crashes, and scheduled deploys without consuming active runtime memory [^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].

This pattern is foundational for architectures requiring asynchronous external input, such as the [Human Approval Gate](../patterns/human-approval-gate.md) [^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].

# Architecture / Specification

### Parking and Resume Mechanism

When a workflow enters a wait condition:
1. **State Recording**: The execution engine captures current execution position, intermediate inputs/context, and correlation identity into persistent storage [^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].
2. **Parked State**: The process releases in-memory execution; the persisted record represents the entire run [^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].
3. **Event Correlation & Resume**: When an external event or timeout occurs, the system matches the event to the run identity, loads the context record, and resumes execution at the designated activity [^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7][^evt-wg-workflows-and-process-integration-pr-33].

### Core Invariants

- **Process Survivability**: Parked runs must survive host terminations, restarts, and redeployments [^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].
- **Context and Position Fidelity**: Continuation restores exact position and prior knowledge without recomputing state from scratch [^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].
- **Idempotent Resume**: Duplicate wake-up events trigger execution resumption at most once [^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].
- **Discoverability**: Suspended runs remain queryable and discoverable across restarts [^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7].

[^evt-wg-workflows-and-process-integration-file-7fc9dc05d148-f1943cf7]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/durable-wait.md
[^evt-wg-workflows-and-process-integration-pr-33]: https://github.com/aaif/wg-workflows-and-process-integration/pull/33
