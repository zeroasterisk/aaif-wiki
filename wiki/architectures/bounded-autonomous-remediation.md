---
type: architecture
title: Bounded Autonomous Remediation
description: Reference architecture for autonomously resolving bounded business tasks
  using deterministic acceptance gates and structured activity workflows.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/49
tags:
- workflows
- remediation
- acceptance-gates
- deterministic-execution
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:23:01.422207+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-49
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/49
  author: mzagar
  last_modified: '2026-10-09T11:27:17+00:00'
---

# Overview

Bounded Autonomous Remediation is a reference architecture developed within the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md) for resolving well-defined operational incidents and workflow errors within strict autonomy bounds without requiring human intervention for routine steps [^evt-wg-workflows-and-process-integration-pr-49]. It relies on deterministic acceptance gates and bounded convergence loops to verify outcomes before state changes are committed.

# Architecture / Specification

The architecture explicitly distinguishes between workflow subunits and target operational problems [^evt-wg-workflows-and-process-integration-pr-49]:

- **Business Task**: The bounded business problem or work item admitted to and resolved by an execution run.
- **Activity**: Individual workflow subunits and operational steps executed by the agent to fulfill the business task.

Key architectural components include:

- **Admission Boundary**: Ingests and validates the scope of incoming business tasks.
- **Activity Execution Engine**: Dispatches individual activities bounded by resource limits and policy gates.
- **Acceptance Evaluation**: Employs [deterministic acceptance gates](../patterns/deterministic-acceptance-gate.md) to inspect activity artifacts against explicit success criteria before closing the business task [^evt-wg-workflows-and-process-integration-pr-49].

[^evt-wg-workflows-and-process-integration-pr-49]: https://github.com/aaif/wg-workflows-and-process-integration/pull/49
