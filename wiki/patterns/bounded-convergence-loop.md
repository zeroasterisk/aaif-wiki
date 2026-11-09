---
type: pattern
title: Bounded Convergence Loop
description: Architectural pattern safely iterating an agent-driven task within explicit
  budget limits until a deterministic gate passes or defined termination triggers.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
tags:
- workflow
- pattern
- orchestration
- remediation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:33:45.576359+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
  author: Mario Zagar
  last_modified: '2026-11-05T08:39:35-08:00'
---

# Overview

The Bounded Convergence Loop governs iterative agent remediation tasks—such as dependency updates, lint corrections, or documentation fixes—where solutions require repeated attempts [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]. The pattern provides the benefits of iterative execution without permitting unbounded retries, open-ended objectives, or self-declared completion [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8].

Every candidate iteration must be assessed by an independent [Deterministic Acceptance Gate](../patterns/deterministic-acceptance-gate.md) [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]. The pattern is used directly within the [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md) reference architecture and interfaces with the [Proposal/Execution Split](../patterns/proposal-execution-split.md) and [Durable Wait](../patterns/durable-wait.md) patterns [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8].

# Architecture / Specification

```mermaid
flowchart TD
    A["Admit bounded business task"] --> B["Agent attempts permitted work"]
    B --> G["Deterministic gate evaluates result"]
    G -->|"accepted"| E["Exit to controlled effect"]
    G -->|"not accepted"| C{"Configured retry criteria permit?"}
    C -->|"yes"| B
    C -->|"no"| S["Escalate, stop, or fail"]
```

The workflow admits an explicitly defined task, restricts agent capabilities to the declared scope, and subjects every output to a deterministic gate [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]. If non-accepted, retries are evaluated against preconfigured constraints including maximum iteration counters, execution deadlines, and cost allocations [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8].

### Invariants

- **Pre-execution constraints:** Task scope, tool access boundaries, and acceptance criteria must be declared before the loop initiates [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8].
- **External evaluation:** The agent cannot certify its own completion; an external deterministic gate evaluates all candidate results [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8].
- **Explicit budgets:** Each retry loop requires an explicit iteration cap and at least one time or token/monetary budget limit [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8].
- **State persistence:** The workflow logs the attempt counter, gate verdicts, and termination reasons, resuming from recorded checkpoints rather than resetting budgets upon restart [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8].
- **Fail-bounded:** Failed gates terminate strictly in bounded retries, escalations, human intervention, or recorded failure [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8].
- **Scope enforcement:** Output passing technical checks but violating scope cannot proceed to side-effect execution [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8].

[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-14b411d8]: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
