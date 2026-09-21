---
type: taxonomy
title: Core Workflow Terms
description: Standardized vocabulary and foundational concepts defining activities,
  workflow execution, control flow, business tasks, and state transitions.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/49
tags:
- taxonomy
- workflows
- terminology
- orchestration
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

The Core Workflow Terms taxonomy establishes unambiguous definitions for agentic workflow orchestration, execution units, and control boundaries across AAIF working groups [^evt-wg-workflows-and-process-integration-pr-49]. It aligns terminology across the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md) and related reference architectures.

# Architecture / Specification

The taxonomy standardizes definitions across workflow composition and runtime lifecycles:

- **Activity**: A workflow subunit representing an individual execution step, tool call, or task component within an orchestration graph [^evt-wg-workflows-and-process-integration-pr-49].
- **Business Task**: The bounded business problem or work item admitted to, tracked by, and resolved through a workflow execution run [^evt-wg-workflows-and-process-integration-pr-49].
- **Convergence Loop**: An iterative control structure that repeatedly executes activities until exit conditions or budget thresholds are met.
- **Acceptance Gate**: An evaluation checkpoint that validates intermediate or final activity outputs against deterministic rules or human approval prior to state transition.
- **Durable Wait**: An execution state where physical runtime resources are released while waiting for an external event or approval, preserving logical progress in persistent storage.

# Lifecycle History

- **Task vs Activity Refinement**: Standardized `activity` as the workflow subunit and `business task` as the admitted business problem across reference architectures and design patterns [^evt-wg-workflows-and-process-integration-pr-49].

[^evt-wg-workflows-and-process-integration-pr-49]: https://github.com/aaif/wg-workflows-and-process-integration/pull/49
