---
type: architecture
title: Bounded Autonomous Remediation
description: Reference architecture governing iterative, autonomous problem resolution
  through declared budgets, deterministic gates, and escalation paths.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/reporting/2026-09-report.md
tags:
- workflow
- architecture
- automation
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:42:23.754300+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/reporting/2026-09-report.md
  author: Yaron Schneider
  last_modified: '2026-11-05T08:38:51-08:00'
- id: evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/architectures/bounded-autonomous-remediation.md
  author: Mario Zagar
  last_modified: '2026-11-05T08:39:35-08:00'
---

# Overview
The Bounded Autonomous Remediation reference architecture governs workflows that resolve a specific, bounded problem autonomously without requiring human authorization for every intermediate step.[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e] Developed by the [Workflows & Process Integration Working Group](../working-groups/workflows-and-process-integration.md), it acts as a counterpart to the [Single-Agent Process with Human Approval](single-agent-human-approval.md) for scenarios where candidate actions have constrained impact, are reversible, and can be evaluated using independent deterministic evidence.[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e]

# Architecture / Specification
The architecture guarantees bounded autonomy, independent acceptance, constrained side effects, and safe non-convergence handling:[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e]
- **Execution Engine**: Governs the lifecycle of the business task, enforces admission criteria, tracks iteration budgets, and triggers safe termination or escalation.[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e]
- **Isolated Work Area**: Limits agent tooling, credentials, and data access to a non-authoritative staging sandbox (such as a branch or draft record).[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e]
- **Deterministic Acceptance Gate**: Evaluates the candidate result against explicit, repeatable validation rules, contracts, or test suites, preventing model self-assessment from certifying output validity.[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e][^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-4c010677]
- **Constrained Effect Executor**: Applies only the accepted, scope-valid change to external systems.[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e]
- **Escalation Surface**: Dispatches unresolvable tasks, exhausted budgets, or scope violations to human operators for review.[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e]

Composed patterns:
- [Bounded Convergence Loop](../patterns/bounded-convergence-loop.md)
- [Deterministic Acceptance Gate](../patterns/deterministic-acceptance-gate.md)
- [Proposal/Execution Split](../patterns/proposal-execution-split.md)

# Lifecycle History
- **2026-08-29**: Core reference architecture merged via PR #26.[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]
- **2026-09-15**: Validation record merged via PR #37 covering maintenance runs and scheduling tasks.[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]
- **2026-09**: PR #43 proposed minimum evidence standards based on action reversibility and blast radius, and PR #49 introduced terminology alignment.[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]

# References
- [Single-Agent Process with Human Approval](single-agent-human-approval.md)
- [Deterministic Acceptance Gate Pattern](../patterns/deterministic-acceptance-gate.md)
- [Proposal/Execution Split Pattern](../patterns/proposal-execution-split.md)

[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e]: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/architectures/bounded-autonomous-remediation.md
[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/reporting/2026-09-report.md
