---
type: guideline
title: Reference Architecture Use Case Validation Guide
description: Evaluation procedure and boundary checklist for validating reference
  architectures against real-world use cases from the inventory.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
tags:
- workflows
- reference-architectures
- validation
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:09:19.961520+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
---

# Overview
The Reference Architecture Use Case Validation Guide defines the standardized process for determining whether an Agentic AI Foundation (AAIF) reference architecture fits a specific real-world use case[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]. Validation establishes architectural alignment with the use case's core operational job and defining boundaries, rather than certifying that an existing implementation adheres to every specific implementation control[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

The framework serves both human contributors and automated coding agents, allowing evaluations to be submitted directly as GitHub issues or pull requests to the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md)[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

# Architecture / Specification

## Scope of Architectural Validation
Validation asks whether a real use case exhibits the job and boundary conditions that a reference architecture is designed to govern[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]:
- **Fit vs. Implementation:** A `Validated` classification indicates that the reference architecture provides the architectural controls required to safely implement the use case. It does not require proof that an existing system already deploys specific controls such as cryptographic version hashes, credentials, retry limits, or idempotency keys[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
- **Permissible Assumptions:** When the primary use case source demonstrates the core job and primary boundary, it is classified as `Validated` without demanding exhaustive documentation of low-level implementation details[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

## Evidentiary Standards
- **Inventory Sourcing:** Evidence must be grounded in facts stated in the [Agentic Use Case Inventory](../resources/agentic-use-case-inventory.md) or its cited sources[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]. Illustrative examples embedded within reference architectures do not constitute independent validation[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
- **Classification Fields:** Metadata tags such as approval gates, exception escalations, and workflow pattern designations serve as valid architectural evidence unless marked with an undocumented-rationale indicator, in which case the rationale is treated as `Unknown`[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

## Validation Procedure
1. **Analyze Reference Architecture:** Review purpose, "Is this your architecture?" checklist criteria, boundary constraints, guarantees, and exit states[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
2. **Comparative Mapping:** Evaluate actor allocations (agent, workflow engine, human participant, external system), boundary enforcement, and failure/wait/recovery handoff paths against the target use case[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
3. **Formulate Checks:** Construct two to three concise checks focused strictly on the defining job and boundary. Each check must declare the explicit architectural consequence of a `Yes`, `No`, or `Unknown` result[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
4. **Draft Findings:** Summarize matches and unknowns in plain language, limiting each section to a maximum of two bullet points[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

# Lifecycle History
The guide was established by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md) under the Reference Architectures workstream to lower contributor friction while maintaining rigorous boundaries between architectural fit and implementation compliance[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
