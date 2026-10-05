---
type: pattern
title: Deterministic Acceptance Gate
description: Workflow design pattern evaluating candidate results against explicit,
  repeatable checks and scope rules rather than model self-assessment.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/deterministic-acceptance-gate.md
tags:
- pattern
- workflows
- validation
- verification
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:03:10.474790+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/deterministic-acceptance-gate.md
  author: Mario Zagar
  last_modified: '2026-08-28T22:42:47-04:00'
- id: evt-wg-workflows-and-process-integration-pr-26
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/26
  author: mzagar
  last_modified: '2026-08-29T02:42:47+00:00'
---

# Overview
The deterministic acceptance gate pattern evaluates a candidate output against explicit, repeatable verification checks (such as tests, linters, schemas, or contract checkers) and scope boundaries before allowing workflow advancement[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658]. It prevents confident but erroneous agent self-assessment from driving downstream state transitions or protected effects[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].

# Architecture / Specification
The gate evaluates a candidate result and its declared execution scope against deterministic acceptance criteria, records digest-bound acceptance evidence, and returns an explicit verification outcome to workflow control[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].

Key invariants include:
- Acceptance criteria and scope constraints must be declared before candidate evaluation occurs[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
- The gate operates independently of the model or agent generating the candidate output[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
- Acceptance evidence is immutably bound to the evaluated candidate version or digest[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
- Passing verification checks is insufficient if policy or scope validation fails[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
- Gate failure, unreachability, or ambiguity must fail closed and never default to acceptance[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].

# References
- Composed in [Bounded Autonomous Remediation](../reference-architectures/bounded-autonomous-remediation.md)[^evt-wg-workflows-and-process-integration-pr-26].
- Related to [Bounded Convergence Loop](bounded-convergence-loop.md) and [Proposal/Execution Split](proposal-execution-split.md)[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].

[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/deterministic-acceptance-gate.md
[^evt-wg-workflows-and-process-integration-pr-26]: https://github.com/aaif/wg-workflows-and-process-integration/pull/26
