---
type: methodology
title: Reference Architecture Use-Case Validation Methodology
description: Evaluation framework and review workflow for assessing the architectural
  fit of reference architectures against documented use cases.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
tags:
- methodology
- reference-architectures
- workflows
- validation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:09:35.963034+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
- id: evt-wg-workflows-and-process-integration-pr-35
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
  author: mzagar
  last_modified: '2026-09-15T20:19:55+00:00'
- id: evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/CONTRIBUTING.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
- id: evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/AGENTS.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
---

# Overview

The Reference Architecture (RA) Use-Case Validation Methodology provides a standardized procedure for evaluating whether a proposed or existing Reference Architecture fits a verified production agentic use case[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]. Established by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md), this methodology allows human contributors and autonomous coding agents to test architectural alignment without requiring an existing codebase to fully implement every technical control upfront[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64][^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30].

# Architecture / Specification

## Validation Scope and Core Principle

Validation assesses whether a target use case shares the primary operational job and defining boundaries addressed by the reference architecture[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

- **Architectural Fit vs. Implementation Conformance**: A `Validated` classification indicates that the reference architecture provides the appropriate structural roles, boundaries, and failure controls for the job[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]. It does not certify that a specific running deployment already complies with all reference architecture mechanisms (such as retry parameters, token storage, or credential handling)[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
- **Evidentiary Standard**: Evaluations must rely strictly on documented facts in the Use Case Inventory or cited primary sources, rather than synthetic examples or illustrative scenarios within pattern templates[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64][^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30].

## Evaluation Workflow

1. **Boundary and Responsibility Mapping**: Inspect who executes each task across agent, orchestrator/workflow engine, human operator, and external systems[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
2. **Check Definition**: Construct two or three targeted validation checks addressing the core job and required boundaries; do not mandate evidence for omitted low-level implementation details unless they alter architectural fit[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
3. **Result Classification**: Assign one of four standardized status values[^evt-wg-workflows-and-process-integration-pr-35]:
   - `Validated`: Strong architectural alignment with the main job and boundaries[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
   - `Partial`: Fits core elements but exhibits significant boundary mismatches or missing failure handling[^evt-wg-workflows-and-process-integration-pr-35].
   - `No fit`: The use case requires a fundamentally different coordination pattern or job structure[^evt-wg-workflows-and-process-integration-pr-35].
   - `Candidate`: Insufficient factual evidence available to determine architectural fit[^evt-wg-workflows-and-process-integration-pr-35].

## Contribution Output

Findings are submitted as either a lightweight GitHub Issue (when seeking consensus on ambiguous boundaries) or a direct pull request appending the validation record to the Reference Architecture document[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64][^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4].

# Lifecycle History

Introduced in PR #35 following Reference Architecture Workstream Sync #6 to provide consistent guidelines for validating architectural models across practitioner use cases[^evt-wg-workflows-and-process-integration-pr-35].

[^evt-wg-workflows-and-process-integration-file-54e7ca1fd5c5-e33239f4]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/CONTRIBUTING.md
[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
[^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/AGENTS.md
[^evt-wg-workflows-and-process-integration-pr-35]: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
