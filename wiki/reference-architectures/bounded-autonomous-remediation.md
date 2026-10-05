---
type: reference-architecture
title: Bounded Autonomous Remediation
description: Job-oriented reference architecture enabling constrained agent iteration
  on fenced tasks with deterministic acceptance gates.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
tags:
- architecture
- workflows
- gates
- remediation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:26:32.273472+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-43
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
  author: narko4u
  last_modified: '2026-10-02T15:00:07+00:00'
---

# Overview
The Bounded Autonomous Remediation reference architecture defines a constrained execution model enabling agents to iteratively remediate fenced operational or codebase issues while enforcing strict convergence limits and deterministic verification gates [^evt-wg-workflows-and-process-integration-pr-43].

# Architecture / Specification
This architecture integrates several core workflow patterns:
- [Bounded Convergence Loop](../patterns/bounded-convergence-loop.md): Constrains remediation iterations by time, token count, and retry bounds.
- [Deterministic Acceptance Gate](../patterns/deterministic-acceptance-gate.md): Evaluates proposed remediation output against non-probabilistic checks before committing changes.
- [Proposal-Execution Split](../patterns/proposal-execution-split.md): Separates the agent's exploratory proposal generation from privileged execution.

## Minimum Evidence for Deterministic Gates
The evidence bar required for a deterministic gate to authorize execution scales with two fundamental properties of the candidate effect [^evt-wg-workflows-and-process-integration-pr-43]:
1. **Blast Radius**: The operational, security, or data boundary affected if the candidate action fails or behaves unexpectedly.
2. **Reversal Cost**: The operational complexity and latency required to roll back or undo the applied state transition.

Regardless of gate strength or autonomy tier, three invariants hold for every acceptance record [^evt-wg-workflows-and-process-integration-pr-43]:
- **Determinism of Verdict**: The acceptance check produces identical pass/fail verdicts when evaluated against the same candidate and environment state.
- **Binding of Verdict to Candidate**: The recorded verdict is immutably bound to the exact candidate artifact or diff hash.
- **Preservation as Execution Evidence**: Every gate evaluation and verdict is retained in the execution audit log as non-repudiable proof.

# Lifecycle History
- Proposed in Workflows and Process Integration Working Group to govern automated self-healing and remediation pipelines.
- Minimum evidence criteria formalized to scale gate requirements with blast radius and reversal cost [^evt-wg-workflows-and-process-integration-pr-43].

[^evt-wg-workflows-and-process-integration-pr-43]: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
