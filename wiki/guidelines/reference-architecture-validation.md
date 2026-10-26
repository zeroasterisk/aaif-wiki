---
type: guideline
title: Reference Architecture Use-Case Validation Guide
description: Evaluation criteria and procedures for validating that an AAIF reference
  architecture matches real-world agentic workflow use cases.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
tags:
- guideline
- workflows
- validation
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:20:54.323193+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
- id: evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/CONTRIBUTING.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
---

# Overview
The Reference Architecture Use-Case Validation Guide establishes the standard procedure for evaluating whether an AAIF Reference Architecture (RA) accurately fits a real-world use case documented in the [Agentic Use Case Inventory](../resources/agentic-use-case-inventory.md) [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]. The validation process ensures that reference architectures map directly to recognizable practitioner jobs while clarifying boundaries, capability requirements, and failure modes [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].

# Architecture / Specification
## Purpose of Validation
Validation assesses whether an RA addresses the core job and primary boundary of a given use case [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]. A designation of `Validated` confirms architectural fit; it does not require that an existing production implementation already complies with every secondary technical control (such as specific retry settings, storage backends, or credential hashing) [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

## Validation Procedure
Validating an RA against a real use case proceeds in three steps [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]:
1. **Analyze Purpose and Boundaries**: Review the RA's job statement, boundaries, checklist, guarantees, and terminal exit states.
2. **Evaluate Use Case Evidence**: Compare against documented evidence in the Use Case Inventory:
   - Does the RA solve the primary practitioner job?
   - Are actor roles clearly separated across agent, workflow engine, human reviewer, and external systems?
   - Does the use case possess the defining boundary mandated by the RA?
   - Does the RA address the critical failure, wait, retry, recovery, or escalation paths?
3. **Formulate Verification Checks**: Construct two to three simple evaluation checks focused on the core job and defining boundaries, recording unambiguous `Yes`, `No`, or `Unknown` determinations [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

## Distinction Between Architectural Patterns, Reference Architectures, and Scenarios
Contributors must adhere to the structural boundaries established by the Workflows and Process Integration Working Group [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]:
- **Patterns**: Solve a single, recurring workflow problem independently (e.g., [Durable Wait](../patterns/durable-wait.md), [Human Approval Gate](../patterns/human-approval-gate.md)).
- **Reference Architectures**: Comprehensive blueprints addressing complete practitioner jobs, composing multiple patterns, capability roles, boundaries, and exit states (e.g., [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md)).
- **Scenarios**: Concrete or illustrative domain examples used to validate an architecture; a scenario cannot serve as an architecture name [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].

# Lifecycle History
Authored under the AAIF Workflows and Process Integration Working Group to accompany the reference architecture templates and contributing guidelines [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4, ^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/CONTRIBUTING.md
[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
