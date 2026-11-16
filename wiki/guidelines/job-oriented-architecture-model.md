---
type: guideline
title: Job-Oriented Architecture Model
description: Architectural decision framework structuring agent reference architectures
  around recognizable practitioner jobs rather than raw agent counts.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/decisions/job-oriented-architecture-model.md
tags:
- guideline
- architecture
- workflows
- decision-record
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T09:56:55.475973+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/decisions/job-oriented-architecture-model.md
  author: Zayne Turner
  last_modified: '2026-08-05T23:05:12-04:00'
---

# Overview
The Job-Oriented Architecture Model is an architectural decision framework established by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md) that organizes reference architectures around recognizable practitioner jobs rather than structural agent topologies [^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]. It decouples the operational need—such as bounded remediation or approval gating—from the agent count, which is treated as an implementation outcome.

Under this model, reference architectures represent complete compositions of reusable patterns, operational boundaries, required capabilities, and explicit exit guarantees, while patterns capture independent solutions to recurring workflow problems [^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62].

# Architecture / Specification
The framework defines distinct roles and relationships between architectural artifacts [^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]:
- **Reference Architectures**: Comprehensive specifications matching named practitioner jobs (e.g., [Single-Agent Process with Human Approval](../architectures/single-agent-human-approval.md)). They compose reusable patterns, declare runtime boundaries, and enforce outcome guarantees.
- **Patterns**: Independently adoptable solutions addressing specific, recurring workflow challenges (e.g., [Human Approval Gate](../patterns/human-approval-gate.md), [Proposal/Execution Split](../patterns/proposal-execution-split.md), [Durable Wait](../patterns/durable-wait.md)). Patterns maintain self-contained invariants and failure modes across multiple architectures.
- **Structural Typologies**: Classifications such as single-agent and multi-agent serve as internal design characteristics rather than top-level architectural taxonomies.
- **Scenario Validation**: Use cases and test scenarios validate architectures; mismatches signal missing patterns, variant gaps, or entirely distinct practitioner jobs.

### Rationale and Trade-offs
Practitioners approach workflow integration from operational needs rather than predetermined agent counts [^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]. Focusing on recognized practitioner jobs provides clearer operational boundaries and prevents redundant definitions across workflows. This replaces earlier scaffolding that categorized architectures strictly by single-agent versus multi-agent boundaries [^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62].

[^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/decisions/job-oriented-architecture-model.md
