---
type: specification
title: Bounded Convergence Loop
description: A workflow pattern safely iterating an agent-assisted task until a deterministic
  acceptance condition passes or ending in a defined non-success outcome.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
tags:
- workflows
- patterns
- iteration
- remediation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:58:02.952470+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
  author: Mario Zagar
  last_modified: '2026-08-28T22:42:47-04:00'
- id: evt-wg-workflows-and-process-integration-pr-26
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/26
  author: mzagar
  last_modified: '2026-08-29T02:42:47+00:00'
---

# Overview

The Bounded Convergence Loop pattern governs iterative agent execution on a bounded task by pairing agent work with independent deterministic evaluation and strictly enforced retry budgets [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0]. It prevents open-ended execution, cost overruns, and self-certified completion by requiring an external gate and finite iteration, time, or cost limits [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].

This pattern is utilized in autonomous workflows such as bounded autonomous remediation and connects with [Deterministic Acceptance Gate](../specification/deterministic-acceptance-gate.md) and [Proposal/Execution Split](../specification/proposal-execution-split.md) [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0, ^evt-wg-workflows-and-process-integration-pr-26].

# Architecture / Specification

The workflow engine admits a single bounded task, exposes only the tools required for that scope, and evaluates candidate results through a deterministic gate [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0]. If the gate does not accept the result, retries are permitted only if declared retry budgets remain unexhausted [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].

```text
Admit bounded task ──► Agent attempts permitted work
                             │
                             ▼
                   Deterministic gate evaluates result
                             ├── [accepted]     ──► Exit to controlled effect
                             └── [not accepted] ──► Configured retry criteria permit?
                                                      ├── [yes] ──► Agent retries
                                                      └── [no]  ──► Escalate, stop, or fail
```

## Invariants

1. **Pre-defined task boundary:** Scope, permitted tool capabilities, and acceptance criteria are set before the loop starts [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].
2. **Independent convergence decision:** An external deterministic gate evaluates all candidate results; the agent cannot declare its own success [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].
3. **Mandatory budget bounds:** Every loop defines an iteration ceiling and at least one time or cost limit [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].
4. **Audit and state durability:** The workflow records the attempt counter, evaluation outcomes, and exit reasons; restarts resume from recorded state without resetting budget limits [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].
5. **Scope enforcement:** Results that pass gate checks but breach declared scope are prohibited from executing protected effects [^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0].

[^evt-wg-workflows-and-process-integration-file-dc0b08806fbd-19da1bf0]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/bounded-convergence-loop.md
