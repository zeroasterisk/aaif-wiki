---
type: architecture
title: Bounded Autonomous Remediation Reference Architecture
description: Reference architecture for resolving bounded operational problems autonomously
  through isolated execution, deterministic gates, and convergence loops.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/49
tags:
- aaif
- architecture
- remediation
- workflows
- autonomy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:45:25.908535+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-49
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/49
  author: mzagar
  last_modified: '2026-10-09T11:27:17+00:00'
---

# Overview
The *Bounded Autonomous Remediation* reference architecture defines an operational model for an AI agent to diagnose, plan, and remediate bounded operational incidents without requiring continuous synchronous human supervision.[^evt-wg-workflows-and-process-integration-pr-49] The architecture constrains execution within pre-verified blast radii using deterministic safety gates and convergence limits.[^evt-wg-workflows-and-process-integration-pr-49]

Standardized by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md), this reference architecture establishes rigorous separation between internal execution steps and the overarching problem admitted to the system.[^evt-wg-workflows-and-process-integration-pr-49]

# Architecture / Specification
The architecture codifies strict terminology boundaries for operational units:
- **Business Task**: The admitted bounded business problem or work item handled by an end-to-end execution run (such as remediating an alerting service or rolling back a failed deployment).[^evt-wg-workflows-and-process-integration-pr-49]
- **Activity**: A modular workflow subunit or atomic execution step within the run executed by the agent or runtime environment.[^evt-wg-workflows-and-process-integration-pr-49]

The system architecture composes three core patterns:
1. [Proposal-Execution Split](../patterns/proposal-execution-split.md): Isolates the agent's generative reasoning and action proposals from privileged actuators.
2. [Deterministic Acceptance Gate](../patterns/deterministic-acceptance-gate.md): Validates candidate commands against hard invariant checks and blast-radius policies before granting execution permission.
3. [Bounded Convergence Loop](../patterns/bounded-convergence-loop.md): Limits diagnostic and corrective iterations to explicit budget and cycle thresholds, preventing runaway cost or cascading degradation.

# Lifecycle History
Developed under the Workflows and Process Integration Working Group, the reference architecture was refined in PR #49 to clarify the distinction between internal workflow activities and admitted business tasks across all lifecycle stages, diagrams, and recovery flows.[^evt-wg-workflows-and-process-integration-pr-49]

[^evt-wg-workflows-and-process-integration-pr-49]: https://github.com/aaif/wg-workflows-and-process-integration/pull/49
