---
type: resource
title: Agentic Use Case Classification Framework
description: Classification taxonomy defining core architectural dimensions and boundary
  scopes to categorize real-world agent deployments.
resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/60
tags:
- taxonomy
- classification
- workflows
- use-cases
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:32:01.605413+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-issue-60
  resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/60
  author: mluciano-sbai
  last_modified: '2026-10-30T20:12:06+00:00'
---

# Overview
The Agentic Use Case Classification Framework structures real-world agent deployments across standardized architectural dimensions to evaluate workflow orchestration, human oversight, and operational complexity.

# Architecture / Specification
The classification framework categorizes production workflows defined in the inventory ([resources/agentic-use-case-inventory](../resources/agentic-use-case-inventory.md)):
- **Core Dimensions**: Analyzes trigger mechanism, human intervention gates, agent cardinality (single-agent vs. multi-agent), execution determinism (fixed/scripted vs. adaptive), and orchestration topology (sequential pipeline, fan-out/join, or iterative loop).
- **Boundary Scope (Proposed)**: Evaluates the output destination perimeter across three discrete values: `Same team`, `Across teams`, and `Across companies`.[^evt-wg-workflows-and-process-integration-issue-60]
- **Architectural Implications**: Workflows crossing team or enterprise boundaries mandate differentiated approval routing, audit logging, and payload validation even when sharing identical triggering and topology primitives.[^evt-wg-workflows-and-process-integration-issue-60]

# Lifecycle History
- **2026-10**: Issue #60 proposed extending the schema with the `Boundary` dimension to disambiguate routing and handoff requirements across inventory use cases.[^evt-wg-workflows-and-process-integration-issue-60]

[^evt-wg-workflows-and-process-integration-issue-60]: https://github.com/aaif/wg-workflows-and-process-integration/issues/60
