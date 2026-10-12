---
type: guideline
title: Job-Oriented Architecture Model
description: Architectural decision record organizing workflow reference architectures
  around recognizable practitioner jobs rather than agent topology or agent count.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/decisions/job-oriented-architecture-model.md
tags:
- guidelines
- workflows
- architecture
- adr
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:09:09.431272+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/decisions/job-oriented-architecture-model.md
  author: Zayne Turner
  last_modified: '2026-08-05T23:05:12-04:00'
---

# Overview
The Job-Oriented Architecture Model is an architectural decision adopted by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md) to structure reference architectures around recognizable practitioner jobs rather than structural agent counts [^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]. It formalizes the distinction between reusable [workflow patterns](../guidelines/workflow-pattern-template.md) and complete reference architectures composed of capabilities, boundaries, guarantees, and exit states [^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62].

# Architecture / Specification
The decision establishes explicit criteria for organizing and reviewing workflow architectures [^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]:

- **Practitioner Jobs Over Topology**: Generic single-agent and multi-agent workflow scaffolds are replaced because agent count is a design outcome rather than an operational need [^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]. Single-agent and multi-agent descriptors remain structural characteristics within architectures rather than top-level categorization axes [^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62].
- **Reference Architecture Composition**: Reference architectures provide a complete composition of reusable patterns, required capabilities, boundary controls, guarantees, and exit states for an explicit operational job, such as [Single-Agent Human Approval](../architectures/single-agent-human-approval.md) [^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62].
- **Pattern Separation**: Patterns serve as independently adoptable solutions to individual recurring problems, retaining their own invariants, failure modes, and implementation approaches [^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62].
- **Scenario Validation**: Real-world use cases validate reference architectures; scenarios that fail to fit indicate a missing variant, an uncaptured pattern, or an entirely distinct job [^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62].

# Lifecycle History
The decision was formally proposed as an Architecture Decision Record on 2026-07-20 in the Workflows and Process Integration repository [^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]. It deprecated generic multi-agent templates in favor of job-specific architectures such as [bounded-autonomous-remediation](../architectures/bounded-autonomous-remediation.md) [^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62].

[^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/decisions/job-oriented-architecture-model.md
