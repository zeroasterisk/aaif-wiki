---
type: decision
title: Job-Oriented Reference Architecture Model
description: Architectural model organizing AAIF reference architectures around recognizable
  practitioner jobs and composable workflow patterns.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/decisions/job-oriented-architecture-model.md
tags:
- workflows
- reference-architectures
- decisions
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:29:28.001865+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/decisions/job-oriented-architecture-model.md
  author: Zayne Turner
  last_modified: '2026-08-05T23:05:12-04:00'
---

# Overview
The Job-Oriented Reference Architecture Model is an architectural decision proposed within the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md) to structure reference architectures around concrete practitioner jobs rather than structural agent counts[^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]. This approach separates end-to-end operational compositions from reusable sub-patterns.

# Architecture / Specification
The decision establishes explicit definitions and separation of concerns across workstream artifacts[^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]:
- **Reference Architectures**: Complete compositions of reusable patterns, capabilities, boundaries, operational guarantees, and exit states solving a named practitioner job.
- **Patterns**: Independently adoptable solutions to recurring workflow sub-problems (such as the [Human Approval Gate](../patterns/human-approval-gate.md)) that define their own invariants and failure modes.
- **Structural Roles**: Classifications like single-agent or multi-agent topologies are treated as internal implementation characteristics rather than top-level architectural taxonomy categories.
- **Validation**: Scenarios and use cases serve to validate architectures, identifying missing variants or distinct practitioner jobs.

[^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/decisions/job-oriented-architecture-model.md
