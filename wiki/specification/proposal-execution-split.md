---
type: specification
title: Proposal/Execution Split
description: A workflow pattern enforcing distinct roles and separate recording for
  proposal generation, authorization decisions, and effect execution.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/proposal-execution-split.md
tags:
- workflows
- patterns
- authorization
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:58:02.952470+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/proposal-execution-split.md
  author: Mario Zagar
  last_modified: '2026-08-28T22:42:47-04:00'
---

# Overview

The Proposal/Execution Split pattern separates intent generation, authorization, and effect execution across distinct architectural roles to enforce strict governance boundaries on probabilistic agents [^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]. Under this pattern, an agent outputs immutable proposal data rather than triggering actions directly; an independent authorization authority reviews that exact proposal, and a dedicated workflow executor applies the effect [^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].

This pattern forms the baseline for high-risk, auditable operations and interfaces directly with patterns such as [Human Approval Gate](../specification/human-approval-gate.md) and [Durable Wait](../specification/durable-wait.md) [^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].

# Architecture / Specification

The pattern enforces three decoupled roles and an auditable system of record [^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]:

```text
  proposer (agent)            authorization authority       executor (system)
        │                             │                            │
        ▼                             ▼                            ▼
   proposal ─────────► gate: authorize this exact ─ yes ─► workflow-controlled
   (immutable data,         proposal?                      execution of the
    not an action)            │                            authorized proposal
                              └─ no / invalid ──► terminal or     │
                                 recovery path                    ▼
                                                                effect
  ─────────────────────────────────────────────────────────────────────────
    system of record: proposal · authority + decision evidence · effect
```

## Invariants

1. **Data over action:** The agent produces an immutable, structured proposal rather than invoking side-effecting tools [^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].
2. **Distinct authority:** Authorization is granted by an independent authority (human reviewer or versioned policy engine), never the proposing agent [^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].
3. **Exact authorization binding:** The execution step executes precisely the payload and parameters that were reviewed and authorized [^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].
4. **Inaccessible executor:** The execution mechanism and privileged credentials are inaccessible to the proposing agent [^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].
5. **Separate audit provenance:** Proposal content, authorization decisions, and final effect telemetry are logged as separate, correlated records in the system of record [^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950].

[^evt-wg-workflows-and-process-integration-file-e3cb5264d4e0-5b43d950]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/proposal-execution-split.md
