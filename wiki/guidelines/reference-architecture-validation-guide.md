---
type: guideline
title: Reference Architecture Use Case Validation Guide
description: Standardized evaluation guide and criteria for verifying architectural
  fit between AAIF reference architectures and real-world use cases.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
tags:
- guidelines
- reference-architectures
- validation
- workflows
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:08:24.395767+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
- id: evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/AGENTS.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
- id: evt-wg-workflows-and-process-integration-pr-35
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
  author: mzagar
  last_modified: '2026-09-15T20:19:55+00:00'
---

# Overview

The Reference Architecture Use Case Validation Guide provides a structured method for evaluating whether an Agentic AI Foundation (AAIF) Reference Architecture (RA) matches a specific real-world use case[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]. Maintained by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md), this evaluation framework is designed for both human practitioners and coding agents without requiring deep implementation knowledge[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64][^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30].

Validation specifically verifies that a use case aligns with the core practitioner job and defining operational boundaries that an RA addresses, rather than verifying whether an existing codebase already implements every low-level control (such as storage formats, idempotency keys, or credential handling)[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

# Architecture / Specification

## Validation Outcomes

Validation assessments classify the relationship between an RA and a use case into one of four distinct states[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64][^evt-wg-workflows-and-process-integration-pr-35]:

- **Validated**: The use case clearly matches the RA's primary job and defining boundaries, and the RA supplies the necessary controls.
- **Partial**: The use case shares core aspects with the RA but requires additional patterns, split boundaries, or variant considerations not fully encompassed by the single RA.
- **No Fit**: The use case diverges in authority model, boundary requirements, or core task (e.g., open-ended autonomy or unconstrained human-delegated execution).
- **Candidate**: A potential match requiring further discovery or documentation within the Use Case Inventory.

## Evaluation Procedure

Validation follows a lightweight three-step process[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]:

1. **Boundary & Requirement Analysis**: Compare the RA purpose, checklist, guarantees, and exit states against facts sourced from the Use Case Inventory[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
2. **Check Generation**: Formulate two to three targeted checks assessing the primary job, entity roles (agent, workflow, human, external system), and failure/escalation paths[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
3. **Result Recording**: Record findings with concise explanations of matches and unknowns via small pull requests or GitHub issues[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64][^evt-wg-workflows-and-process-integration-pr-35].

# Lifecycle History

- **Workstream Sync #6**: Formulated action item to provide contributors with an unambiguous validation guide[^evt-wg-workflows-and-process-integration-pr-35].
- **PR #35**: Merged the RA use-case validation guide into the Workflows and Process Integration workstream[^evt-wg-workflows-and-process-integration-pr-35].

# References

- [Job-Oriented Architecture Model](../decisions/job-oriented-architecture-model.md)
- [Bounded Autonomous Remediation](../reference-architectures/bounded-autonomous-remediation.md)
- [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md)

[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
[^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/AGENTS.md
[^evt-wg-workflows-and-process-integration-pr-35]: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
