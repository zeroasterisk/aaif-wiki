---
type: architecture
title: Bounded Autonomous Remediation
description: Reference architecture governing iterative, autonomous problem resolution
  within predefined task boundaries, safety convergence loops, and deterministic acceptance
  gates.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
tags:
- architecture
- autonomous-remediation
- deterministic-gate
- convergence-loop
- safety
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:50:37.814965+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-43
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
  author: narko4u
  last_modified: '2026-10-02T15:00:07+00:00'
---

# Overview
Bounded Autonomous Remediation is a reference architecture governing agentic systems that autonomously diagnose, synthesize solutions for, and remediate technical or operational issues within constrained execution boundaries. The architecture relies on bounded iteration cycles, constrained effect scopes, and strict deterministic evaluation criteria to resolve failures without human intervention while guarding against diverging loops or collateral system damage.

To maintain safety without requiring manual human approval for every action, the architecture pairs autonomous exploration with a [deterministic acceptance gate](../patterns/deterministic-acceptance-gate.md) and [bounded convergence loop](../patterns/bounded-convergence-loop.md). Proposed remediation candidates are evaluated against objective verification suites before deployment, ensuring that autonomous action remains bounded by policy and predictable exit criteria.

# Architecture / Specification

## Deterministic Gate Minimum Evidence Bar
Working group proposals establish that the required rigor of a deterministic acceptance gate scales directly with two fundamental properties of the permitted remediation effect[^evt-wg-workflows-and-process-integration-pr-43]:
1. **Blast Radius**: The maximum scope, infrastructure surface area, or customer population affected if the remediation candidate fails or behaves incorrectly[^evt-wg-workflows-and-process-integration-pr-43].
2. **Reversal Cost**: The operational, financial, or temporal difficulty required to roll back or undo the applied change[^evt-wg-workflows-and-process-integration-pr-43].

As blast radius and reversal cost expand, gate validation must escalate from local functional assertions to comprehensive pre-flight verification, canary evaluations, or cross-system integration checks[^evt-wg-workflows-and-process-integration-pr-43].

## Universal Acceptance Record Invariants
Independent of the specific gate strength required for a given remediation effect, every generated acceptance record must satisfy three invariant properties[^evt-wg-workflows-and-process-integration-pr-43]:
- **Verdict Determinism**: The evaluation verdict must be strictly reproducible given the identical candidate artifact and evaluation inputs[^evt-wg-workflows-and-process-integration-pr-43].
- **Candidate Binding**: The verdict record must cryptographically or structurally bind to the exact hash or immutable specification of the evaluated candidate, preventing post-evaluation tampering or payload substitution[^evt-wg-workflows-and-process-integration-pr-43].
- **Execution Evidence Preservation**: The acceptance record, evaluation telemetry, and test outputs must be preserved as non-ephemeral execution evidence within the audit trail[^evt-wg-workflows-and-process-integration-pr-43].

# Lifecycle History
- **Draft Architecture Intake**: Initial formulation establishing bounded iteration loops, resource ceilings, and acceptance gate checks.
- **Evidence Bar Calibration (PR #43)**: Open proposal resolving criteria for deterministic gate strength by mapping evidence requirements to blast radius and reversal cost while defining universal acceptance record invariants[^evt-wg-workflows-and-process-integration-pr-43].

[^evt-wg-workflows-and-process-integration-pr-43]: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
