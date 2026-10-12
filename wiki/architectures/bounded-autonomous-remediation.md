---
type: architecture
title: Bounded Autonomous Remediation
description: Reference architecture for resolving bounded operational problems autonomously
  through isolated execution, deterministic acceptance gates, and convergence loops.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
tags:
- architecture
- remediation
- autonomous
- safety
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:15:53.446387+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-43
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
  author: narko4u
  last_modified: '2026-10-02T15:00:07+00:00'
---

# Overview

Bounded Autonomous Remediation provides a reference framework for allowing software agents to remediate operational failures and execute constrained system mutations without synchronous human approval [^evt-wg-workflows-and-process-integration-pr-43]. Remediation workflows operate strictly within bounded execution sandboxes, iterating across convergence loops and submitting proposed changes against strict deterministic acceptance criteria before effects are merged or promoted into production.

To balance operational autonomy with safety, the architecture scales verification intensity against the blast radius and reversal cost of the permitted effect [^evt-wg-workflows-and-process-integration-pr-43].

# Architecture / Specification

### Minimum Evidence for Deterministic Gates

While deterministic gates scale their verification hurdles according to the risk of the action, the evidence model preserving gate verdicts enforces three universal invariants across all tiers [^evt-wg-workflows-and-process-integration-pr-43]:

1. **Determinism of the Verdict**: The acceptance check must evaluate repeatable, deterministic criteria (such as test suites, linters, schema validators, or static analysis runs) where identical candidates and test inputs yield identical verdicts [^evt-wg-workflows-and-process-integration-pr-43].
2. **Binding of Verdict to Candidate**: The emitted acceptance record is cryptographically bound to the specific immutable candidate artifact (via content digests), ensuring verification cannot be forged or transferred to unvetted revisions [^evt-wg-workflows-and-process-integration-pr-43].
3. **Preservation as Execution Evidence**: Gate verdicts, captured logs, and evaluation metrics persist permanently within the execution ledger to provide auditability and post-mortem transparency [^evt-wg-workflows-and-process-integration-pr-43].

### Scaling Gate Strength

Gate validation criteria scale dynamically based on two structural properties of the target effect [^evt-wg-workflows-and-process-integration-pr-43]:
- **Blast Radius**: The potential scope of operational impact (e.g., local process restart versus cross-region routing updates).
- **Reversal Cost**: The complexity, financial impact, or latency required to roll back the applied change if unexpected degradation occurs.

# References

- Composed patterns: `../patterns/deterministic-acceptance-gate.md`, `../patterns/bounded-convergence-loop.md`
- Boundary guidance: `../guidelines/workflow-architecture-principles.md`

[^evt-wg-workflows-and-process-integration-pr-43]: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
