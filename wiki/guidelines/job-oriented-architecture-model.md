---
type: guideline
title: Job-Oriented Architecture Model
description: Architectural framework structuring agent workflows across reusable patterns,
  job-oriented reference architectures, and scenario evaluations.
resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/28
tags:
- workflows
- architecture
- patterns
- reference-architectures
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:34:55.588168+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-issue-28
  resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/28
  author: mzagar
  last_modified: '2026-09-24T00:09:43+00:00'
---

# Overview
The Job-Oriented Architecture Model establishes a three-tier framework structuring agentic workflow knowledge into reusable patterns, practitioner job-oriented reference architectures, and empirical scenario validations [^evt-wg-workflows-and-process-integration-issue-28]. It provides an architectural foundation for composing granular workflow primitives into reviewable, verifiable operational designs.

# Architecture / Specification
The framework coordinates workflow system design across three structural levels [^evt-wg-workflows-and-process-integration-issue-28]:
- **Reusable Patterns**: Modular building blocks addressing isolated workflow execution problems, such as [durable wait](../patterns/durable-wait.md) and [human approval gate](../patterns/human-approval-gate.md).
- **Job-Oriented Reference Architectures**: Composite frameworks uniting patterns, capability roles, boundary controls, guarantees, and exit states to execute recognizable practitioner jobs.
- **Real-World Scenarios**: Concrete operational use cases (such as invoice processing or autonomous remediation) used to test and validate reference architecture suitability.

Under active workstream consideration, the model evaluates expanding beyond human-readable guidance to produce a formal, machine-readable Workflow Design Specification (WDS) serialized in schema-valid YAML [^evt-wg-workflows-and-process-integration-issue-28]. If adopted, this model treats the specification as an authoritative design artifact from which architecture diagrams, human review materials, and implementation handoffs are automatically derived [^evt-wg-workflows-and-process-integration-issue-28].

# References
- Reference Architectures Workstream Issue #28 [^evt-wg-workflows-and-process-integration-issue-28]
- [Workflow Architecture Principles](../guidelines/workflow-architecture-principles.md)
- [Reference Architecture Template](../guidelines/reference-architecture-template.md)

[^evt-wg-workflows-and-process-integration-issue-28]: https://github.com/aaif/wg-workflows-and-process-integration/issues/28
