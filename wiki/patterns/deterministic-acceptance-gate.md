---
type: pattern
title: Deterministic Acceptance Gate
description: Workflow pattern evaluating candidate results against explicit, repeatable
  checks and scope rules rather than model self-assessment.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/deterministic-acceptance-gate.md
tags:
- workflows
- patterns
- acceptance-gate
- verification
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:36:52.018344+00:00'
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
The Deterministic Acceptance Gate pattern provides an objective, repeatable verification mechanism that evaluates candidate results produced by an agent against explicit acceptance criteria and scope boundaries rather than relying on model self-assessment [^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658]. It ensures that candidate changes are backed by verifiable evidence before being permitted to advance within an agentic workflow [^evt-wg-workflows-and-process-integration-pr-26].

# Architecture / Specification
The pattern evaluates an exact candidate artifact against declared policy rules and deterministic checks such as unit test suites, schema validation, and linting rules [^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].

Key invariants include [^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658]:
- Acceptance criteria are declared before candidate evaluation occurs.
- The gate operates independently of the model or agent that produced the candidate result.
- Acceptance evidence is strictly bound to the exact candidate artifact version or digest.
- Passing verification checks is insufficient if task scope or authorization policies are violated.
- A failed, unavailable, or ambiguous check result fails closed and never counts as acceptance.

# References
- [Bounded Autonomous Remediation](../reference-architectures/bounded-autonomous-remediation.md)
- [Bounded Convergence Loop](bounded-convergence-loop.md)
- [Proposal/Execution Split](proposal-execution-split.md)

[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/deterministic-acceptance-gate.md
[^evt-wg-workflows-and-process-integration-pr-26]: https://github.com/aaif/wg-workflows-and-process-integration/pull/26
