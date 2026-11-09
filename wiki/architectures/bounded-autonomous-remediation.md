---
type: architecture
title: Bounded Autonomous Remediation
description: Reference architecture governing iterative, autonomous problem resolution
  within predefined task bounds, deterministic verification gates, and fail-safe escalation
  paths.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/architectures/bounded-autonomous-remediation.md
tags:
- architecture
- autonomous-agents
- remediation
- workflows
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:33:12.467454+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/architectures/bounded-autonomous-remediation.md
  author: Mario Zagar
  last_modified: '2026-11-05T08:39:35-08:00'
- id: evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/reporting/2026-09-report.md
  author: Yaron Schneider
  last_modified: '2026-11-05T08:38:51-08:00'
---

# Overview
Bounded Autonomous Remediation is a reference architecture designed to autonomously resolve discrete, well-bounded problems without requiring per-attempt human intervention[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e]. It serves as a contrasting companion to the [Single-Agent Process with Human Approval](single-agent-human-approval.md): while it permits autonomous model iterations, it prevents unbounded autonomy and uncontrolled effects by enforcing explicit task boundaries, isolated work areas, independent deterministic acceptance gates, and fail-safe escalation paths[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e].

# Architecture / Specification
The architecture applies to business tasks where scope, tools, budgets, and measurable acceptance criteria can be declared in advance, and the resulting external effect is constrained and low-impact or reversible (e.g., opening a remediation pull request or generating reconciliation batches)[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e].

### Composition of Patterns
The architecture composes three core patterns:
- [Bounded Convergence Loop](../patterns/bounded-convergence-loop.md): Limits agent retries and token/time budgets to prevent runaway execution loops[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e].
- [Deterministic Acceptance Gate](../patterns/deterministic-acceptance-gate.md): Employs independent programmatic checks (unit tests, schema validators, lint rules) rather than agent self-evaluation to judge candidate outputs[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e].
- [Proposal/Execution Split](../patterns/proposal-execution-split.md): Isolates the candidate result from the external executor, preventing direct write actions by the agent[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e].

### Qualification Checklist
To determine if an operational problem fits this architecture, five conditions must be satisfied:
1. **Pre-declared Problem Bounds**: The task contract, allowed scope, permitted tools/data, and acceptance conditions must be established prior to execution[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e].
2. **Independent Deterministic Evaluation**: Objective tests, schemas, or reconciliation rules evaluate candidate outputs without relying on model self-judgment[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e].
3. **Constrained External Effect**: Permitted real-world actions are strictly limited and ideally reversible[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e].
4. **Fenced Agent Environment**: The agent operates inside an isolated workspace with least-privilege credentials and strict resource limits[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e].
5. **Safe Non-Convergence Route**: Budget exhaustion, validation errors, or out-of-scope conditions cleanly halt execution and escalate to human operators[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e].

# Lifecycle History
- **2026-08-29**: Architecture PR #26 merged on main[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e].
- **2026-09-15**: Validation record (PR #37) merged on main[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e].
- **2026-09-30**: PR #43 (minimum evidence rules based on blast radius and reversibility) and PR #49 (terminology cleanup) remain in active review prior to plenary vote scheduling[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e].

[^evt-wg-workflows-and-process-integration-file-58dfe42e59bd-d009744e]: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/workstreams/reference-architectures/architectures/bounded-autonomous-remediation.md
[^evt-wg-workflows-and-process-integration-file-60f28464dd94-4c7ddd9e]: https://github.com/aaif/wg-workflows-and-process-integration/blob/774d4e09283835b4b0b5062ad389dc8dc48752b9/reporting/2026-09-report.md
