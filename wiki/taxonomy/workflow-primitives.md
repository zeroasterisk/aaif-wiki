---
type: taxonomy
title: Workflow Execution Primitives
description: Foundational vocabulary and structural execution primitives defined by
  the Workflows and Process Integration Working Group.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/40
tags:
- taxonomy
- workflows
- control-flow
- determinism
- primitives
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T09:54:13.451569+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-40
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/40
  author: chaksaray
  last_modified: '2026-09-08T17:48:26+00:00'
---

# Overview
Workflow Execution Primitives define the core taxonomy terms and execution concepts standardized by the Workflows and Process Integration Working Group to model deterministic, probabilistic, and hybrid AI agent orchestrations[^evt-wg-workflows-and-process-integration-pr-40]. The vocabulary separates design-time intent from runtime execution dynamics, establishing clear boundaries across control flow sequencing, execution lifecycle states, layer-specific determinism, and responsibility handoffs[^evt-wg-workflows-and-process-integration-pr-40].

# Architecture / Specification

## Core Execution Terms
The working group categorizes workflow components into distinct operational layers[^evt-wg-workflows-and-process-integration-pr-40]:
- **Determinism:** Defined as a property of a specific execution layer—such as Workflow Execution, Control Flow, or an individual Activity—rather than an all-or-nothing property of an entire workflow[^evt-wg-workflows-and-process-integration-pr-40]. This decoupling allows a workflow to enforce strictly deterministic control flow and governance policies while orchestrating non-deterministic, probabilistic model activities[^evt-wg-workflows-and-process-integration-pr-40].
- **Control Flow:** The logical specification determining execution order, branching conditions, iterations, and concurrency joins[^evt-wg-workflows-and-process-integration-pr-40]. The definition remains neutral regarding whether sequencing logic is fixed at design time or evaluated dynamically by an autonomous agent runtime[^evt-wg-workflows-and-process-integration-pr-40].
- **Workflow Execution:** An instantiated runtime invocation possessing a continuous lifecycle identity extending from initiation through completion[^evt-wg-workflows-and-process-integration-pr-40]. Dynamic replanning, step retries, and compensation transitions occur within the lifecycle of a single workflow execution without breaking runtime identity[^evt-wg-workflows-and-process-integration-pr-40].
- **Handoff:** The transfer of operational responsibility, state context, and execution authority between distinct actors or agent sub-processes[^evt-wg-workflows-and-process-integration-pr-40]. The concept bridges workflow orchestration (transfer of responsibility) and observability trace modeling (the observable boundary where delegation occurs)[^evt-wg-workflows-and-process-integration-pr-40].

[^evt-wg-workflows-and-process-integration-pr-40]: https://github.com/aaif/wg-workflows-and-process-integration/pull/40
