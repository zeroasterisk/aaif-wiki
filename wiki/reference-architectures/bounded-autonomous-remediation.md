---
type: reference-architecture
title: Bounded Autonomous Remediation Reference Architecture
description: Reference architecture enabling autonomous iteration and bounded remediation
  under independent deterministic acceptance gates and explicit budget controls.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/49
tags:
- workflow
- reference-architecture
- remediation
- orchestration
- safety
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:14:44.022779+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-49
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/49
  author: mzagar
  last_modified: '2026-09-17T04:59:03+00:00'
---

# Overview

The Bounded Autonomous Remediation reference architecture specifies an architectural framework for executing autonomous error remediation and iteration cycles while enforcing strict termination boundaries, deterministic acceptance criteria, and budget controls [^evt-wg-workflows-and-process-integration-pr-49]. It integrates pattern primitives from [bounded-convergence-loop](../patterns/bounded-convergence-loop.md), [proposal-execution-split](../patterns/proposal-execution-split.md), and [deterministic-acceptance-gate](../patterns/deterministic-acceptance-gate.md).

# Architecture / Specification

Under this architecture, a bounded run processes a specific unit of work while preserving a formal separation between execution subunits and business objectives [^evt-wg-workflows-and-process-integration-pr-49]:

- **Business Task**: The bounded business problem or work item admitted to and handled by a run [^evt-wg-workflows-and-process-integration-pr-49].
- **Activity**: The granular workflow subunits executed within the iteration cycle to propose, analyze, or remediate the business task [^evt-wg-workflows-and-process-integration-pr-49].

The loop operates across four sequential phases:

1. **Task Admission & Scope Bounding**: The system admits a business task and establishes immutable budget invariants (such as maximum token budget, iteration limits, and wall-clock timeout) [^evt-wg-workflows-and-process-integration-pr-49].
2. **Remediation Proposal Activities**: Model-driven or rule-based agents generate candidate remediation proposals without mutating target production systems without validation.
3. **Deterministic Acceptance Evaluation**: Independent test harnesses and acceptance checks evaluate proposal outputs against pre-declared criteria [^evt-wg-workflows-and-process-integration-pr-49].
4. **Convergence or Escalation**: If acceptance tests pass, changes are committed; if the budget is exhausted or checks fail irrecoverably, execution halts and escalates to human operators via [human-approval-gate](../patterns/human-approval-gate.md).

# Lifecycle History

- **Terminology Alignment (PR #49)**: Clarified distinction between workflow activities (execution subunits) and business tasks (admitted work items) across lifecycle diagrams, gates, and recovery semantics [^evt-wg-workflows-and-process-integration-pr-49].

[^evt-wg-workflows-and-process-integration-pr-49]: https://github.com/aaif/wg-workflows-and-process-integration/pull/49
