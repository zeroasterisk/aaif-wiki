---
type: guideline
title: Reference Architecture Use-Case Validation Guide
description: Methodology and evaluation criteria for validating whether real-world
  use cases architecturally align with reference architectures.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
tags:
- guidelines
- reference-architectures
- validation
- workflows
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:03:36.065347+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
- id: evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/CONTRIBUTING.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
- id: evt-wg-workflows-and-process-integration-pr-35
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
  author: mzagar
  last_modified: '2026-09-15T20:19:55+00:00'
- id: evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/AGENTS.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
---

# Overview
The Reference Architecture Use-Case Validation Guide defines the standardized process for evaluating whether a real-world use case fits a specific Reference Architecture (RA) developed by the Workflows and Process Integration Working Group ([`../working-groups/workflows-and-process-integration.md`](../working-groups/workflows-and-process-integration.md)) [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]. It provides practitioners and automated coding agents with structured criteria to evaluate architectural fit rather than implementation-specific mechanics [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64] [^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30].

# Architecture / Specification
### Validation Principles
- **Architectural Fit vs. Implementation Audit:** Validation determines whether a use case matches the primary job, capability roles, and boundary controls of an RA; it does not require proof that a target implementation already implements every control (e.g., retries, hashing, storage) that the RA provides [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
- **Evidence Grounding:** Validation checks must be grounded strictly in facts from the Use Case Inventory or cited sources, not illustrative examples within an RA [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
- **Concise Evaluation:** Evaluators formulate 2 to 3 targeted checks evaluating job alignment, capability distribution (agent, workflow engine, human, external systems), and boundary constraints [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

### Classification Outcomes
- **`Validated`**: The RA is an architectural fit for the use case's core job and defining boundaries [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64] [^evt-wg-workflows-and-process-integration-pr-35].
- **`Partial`**: The use case matches some structural elements but exhibits conflicting boundaries or missing architectural layers [^evt-wg-workflows-and-process-integration-pr-35].
- **`No fit`**: The fundamental job or authority model contradicts the RA requirements [^evt-wg-workflows-and-process-integration-pr-35].
- **`Candidate`**: Initial intake stage pending sufficient factual evidence to complete validation [^evt-wg-workflows-and-process-integration-pr-35].

# Lifecycle History
Introduced via Reference Architecture Workstream Sync #6 and merged under PR #35 to provide standard intake and validation procedures for contributors and coding agents [^evt-wg-workflows-and-process-integration-pr-35] [^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].

[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/CONTRIBUTING.md
[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
[^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/AGENTS.md
[^evt-wg-workflows-and-process-integration-pr-35]: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
