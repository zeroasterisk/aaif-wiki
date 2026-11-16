---
type: pattern
title: Deterministic Acceptance Gate
description: Architectural pattern evaluating candidate agent outputs against explicit,
  repeatable checks and scope rules rather than model self-assessment.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/patterns/deterministic-acceptance-gate.md
tags:
- workflow
- pattern
- verification
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:42:23.754300+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-970f1ea4eefc-4c010677
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/patterns/deterministic-acceptance-gate.md
  author: Mario Zagar
  last_modified: '2026-11-05T08:39:35-08:00'
---

# Overview
The Deterministic Acceptance Gate is an architectural pattern that evaluates candidate agent outputs against explicit, repeatable criteria and declared scope constraints before allowing workflow advancement.[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-4c010677] Formulated by the [Workflows & Process Integration Working Group](../working-groups/workflows-and-process-integration.md), this pattern eliminates reliance on probabilistic model self-assessment, which can produce unwarranted confidence in invalid results.[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-4c010677]

# Architecture / Specification
The gate validates outputs using independent, automated mechanisms:[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-4c010677]
- **Deterministic Evaluation**: Tests, schemas, contracts, and policy engines assess the candidate output reproducibly.[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-4c010677]
- **Scope & Policy Constraints**: Validates that changes remain within authorized targets, permitted modification classes, tool boundaries, and blast-radius limits.[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-4c010677]
- **Evidence Association**: Binds verification records to the exact version, artifact digest, or candidate identity evaluated.[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-4c010677]

Key invariants:[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-4c010677]
- Acceptance criteria are declared before candidate evaluation occurs.
- Evaluators operate independently of the generating model context.
- Acceptance evidence binds to the specific evaluated candidate digest.
- Passing technical checks is insufficient if scope or policy bounds are breached.
- Ambiguous, failed, or unavailable verification never defaults to permission.

# References
- [Bounded Convergence Loop](bounded-convergence-loop.md)
- [Proposal/Execution Split](proposal-execution-split.md)
- [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md)

[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-4c010677]: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/patterns/deterministic-acceptance-gate.md
