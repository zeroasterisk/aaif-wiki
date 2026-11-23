---
type: pattern
title: Deterministic Acceptance Gate
description: Architectural pattern evaluating candidate agent outputs against explicit,
  repeatable checks and scope rules rather than model self-assessment.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/deterministic-acceptance-gate.md
tags:
- pattern
- verification
- workflows
- governance
- safety
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T09:52:14.257124+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/deterministic-acceptance-gate.md
  author: Mario Zagar
  last_modified: '2026-08-28T22:42:47-04:00'
---

# Overview
The Deterministic Acceptance Gate is an architectural pattern that decides whether a candidate agent output or state change may advance using explicit, repeatable checks rather than model self-assessment[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658]. In autonomous or bounded workflows, allowing a generating model to evaluate its own result leaves the system vulnerable to confident yet ungrounded self-assessment[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].

The pattern decouples evaluation from generation by testing candidates against predefined criteria such as automated test suites, JSON Schema validations, contracts, or explicit policy rules[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658]. It forms a core verification component of [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md) alongside [Bounded Convergence Loop](bounded-convergence-loop.md) and [Proposal/Execution Split](proposal-execution-split.md)[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].

# Architecture / Specification

## Mechanism
When an agent produces a candidate result with a declared operational scope, the deterministic gate performs two-factor verification[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658]:
1. **Technical Criteria & Scope Validation**: Checks evaluate whether technical conditions are satisfied and ensure the action remains within task-level boundaries—including affected systems, allowed change classes, accessed data, and permitted tools[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
2. **Evidence Recording**: If acceptance criteria and scope validations pass, tamper-evident verification records are persisted and bound to the candidate's exact version or content digest[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
3. **Workflow Control**: If evaluation fails or evidence is insufficient, the gate returns the result to workflow orchestration. The enclosing workflow decides whether to iterate within budget limits, escalate, or halt[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].

## Required Capabilities
- **Deterministic Evaluator**: Repeatable test runner, contract verifier, or schema validator independent of model reasoning[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
- **Policy/Scope Validator**: Boundary checking component verifying that candidate outputs comply with permitted operational targets and action limits[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
- **Evidence Store**: Storage repository retaining signed or verifiable evaluation records bound directly to candidate artifact digests[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].

## Invariants
Implementations must uphold seven invariant guarantees[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658]:
- Acceptance criteria are declared before evaluating candidate results[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
- The gate operates independently of the model or agent producing the candidate output[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
- Acceptance evidence is cryptographically or structurally bound to the evaluated candidate version or digest[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
- Passing functional checks is insufficient if policy or scope verification fails[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
- Failed, ambiguous, or unavailable gate evaluations never default to an accepted state[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
- Workflows record all evaluation inputs, outcomes, and resulting decisions in an audit log[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
- Gate authority is strictly limited to its declared contract; broader downstream modifications require independent authorization[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].

## Failure Modes
- **Agent Self-Evaluation**: Allowing generating agents to assess output correctness converts hallucinated confidence into workflow truth[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
- **Detached Evidence**: Failing to bind acceptance evidence to candidate digests permits stale evidence to authorize altered payloads[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
- **Permissive Failure Defaults**: Treating gate evaluation outages or missing checks as acceptable advances unvalidated changes[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].
- **Omitted Scope Boundary Validation**: Validating technical correctness without enforcing target constraints allows actions to exceed granted organizational authority[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658].

[^evt-wg-workflows-and-process-integration-file-970f1ea4eefc-f3be8658]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/patterns/deterministic-acceptance-gate.md
