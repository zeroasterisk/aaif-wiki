---
type: guideline
title: Reference Architecture Template
description: Standardized structure, metadata headers, and section requirements for
  authoring AAIF workflow reference architectures.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/architectures/TEMPLATE.md
tags:
- reference-architecture
- template
- workflows
- guidelines
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T02:53:46.880870+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-c1c1cdc015db-05940fd8
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/architectures/TEMPLATE.md
  author: Mario Zagar
  last_modified: '2026-08-25T07:58:21-07:00'
---

# Overview
The Reference Architecture Template defines the canonical authoring structure and documentation standards for reference architectures published by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md)[^evt-wg-workflows-and-process-integration-file-c1c1cdc015db-05940fd8]. It ensures that architectural guidance across the foundation is structured around clear practitioner jobs, explicit boundary contracts, and verifiable design invariants[^evt-wg-workflows-and-process-integration-file-c1c1cdc015db-05940fd8].

The template enforces a user-centric documentation philosophy where practitioners can immediately evaluate whether an architecture answers their specific operational problem before diving into implementation mechanics[^evt-wg-workflows-and-process-integration-file-c1c1cdc015db-05940fd8].

# Architecture / Specification

## Required Metadata Headers
Every reference architecture document begins with a standardized metadata header defining its high-level scope[^evt-wg-workflows-and-process-integration-file-c1c1cdc015db-05940fd8]:
- **The job it serves**: The recurring practitioner need answered plainly.
- **Built from patterns**: Composed patterns referenced from the foundation pattern catalog.
- **Requires capabilities**: Distinct capability roles necessary to implement the architecture.
- **Audience**: Builders, reviewers, and stakeholders benefiting from the architecture.

## Canonical Structural Sections
Architectures adhering to the template must provide the following sections[^evt-wg-workflows-and-process-integration-file-c1c1cdc015db-05940fd8]:
1. **Status**: Lifecycle status (Draft, Proposed, Approved) and decision record links.
2. **Purpose**: Plain-language description of the job and reading paths routing technical versus executive readers.
3. **Is this your architecture? (Checklist)**: Use-case routing questions answerable without prior implementation knowledge or model assumptions.
4. **Variants**: Allowable additions or subtractions of components that preserve underlying architectural invariants.
5. **Structure**: Capability-level block diagram and required-capabilities table focusing on data contracts crossing interface boundaries.
6. **Pattern Composition**: How component design patterns combine to enforce end-to-end guarantees.
7. **The Agent and Workflow-Control Boundary**: Clear delineation separating orchestrator control logic from autonomous agent loops.
8. **Choosing Deterministic and Model-Driven Activities**: Decision criteria partitioning deterministic policy gates from nondeterministic model inference.
9. **Exit States**: Complete taxonomy of terminal and intermediate execution states.
10. **Worked Scenario**: Concrete walk-through illustrating boundary crossings and failure handling.
11. **Composition Considerations & Out of Scope**: Architectural constraints, non-goals, and boundary limitations.
12. **Validation Record & Open Questions**: Empirical verification status and unresolved design items.

[^evt-wg-workflows-and-process-integration-file-c1c1cdc015db-05940fd8]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/architectures/TEMPLATE.md
