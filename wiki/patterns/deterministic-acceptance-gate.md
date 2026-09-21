---
type: pattern
title: Deterministic Acceptance Gate
description: Workflow design pattern evaluating candidate results against explicit,
  repeatable checks and declared scope constraints rather than model self-assessment.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/deterministic-acceptance-gate.md
tags:
- pattern
- workflow
- verification
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:03:22.515811+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/deterministic-acceptance-gate.md
  author: Mario Zagar
  last_modified: '2026-08-28T22:42:47-04:00'
- id: evt-wg-workflows-and-process-integration-pr-26
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/26
  author: mzagar
  last_modified: '2026-08-29T02:42:47+00:00'
---

# Overview
The Deterministic Acceptance Gate pattern establishes an independent verification barrier in agentic workflows to decide whether a candidate result may advance using explicit, repeatable criteria rather than model self-assessment [^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658]. In bounded autonomous tasks, relying on the generating model to judge its own output risks confident but erroneous self-validation. The gate decouples candidate evaluation into reproducible technical checks, schema validation, contract tests, and task scope enforcement [^evt-wg-workflows-and-process-integration-pr-26].

# Architecture / Specification
The gate operates at the boundary between candidate artifact production and workflow state progression [^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].

Key architectural components include:
- **Deterministic Evaluator**: Executes explicit checks (such as unit test suites, JSON Schema validators, or status checks) against the candidate artifact [^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
- **Policy/Scope Validator**: Confirms that candidate outputs do not exceed declared boundaries, including permitted target systems, allowed tool actions, data access boundaries, and maximum permissible impact [^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
- **Evidence Store**: Persists cryptographic digests, check inputs, validation logs, and acceptance timestamps bound to the exact candidate version evaluated [^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].

### Core Invariants
Implementations must preserve several fundamental invariants [^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658]:
1. Acceptance criteria must be declared prior to candidate evaluation.
2. The gate evaluation mechanism must remain completely independent of the model or agent that produced the candidate result.
3. Acceptance evidence must be bound to the exact candidate artifact digest or version.
4. Passing technical checks is insufficient if task policy or scope validation fails.
5. Missing, failed, or ambiguous gate evaluations must default to fail-closed behavior (non-acceptance).
6. The gate's authority is constrained to its declared scope; downstream actions with higher blast radius require separate authorization controls.

### Interaction with Other Patterns
The Deterministic Acceptance Gate is commonly used in conjunction with the [Bounded Convergence Loop](bounded-convergence-loop.md) to govern iteration exit conditions, and the [Proposal/Execution Split](proposal-execution-split.md) to separate proposal verification from workflow execution [^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].

[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/deterministic-acceptance-gate.md
[^evt-wg-workflows-and-process-integration-pr-26]: https://github.com/aaif/wg-workflows-and-process-integration/pull/26
