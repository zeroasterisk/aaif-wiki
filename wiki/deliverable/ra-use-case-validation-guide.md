---
type: deliverable
title: Reference Architecture Use-Case Validation Guide
description: A methodology and evaluation framework for assessing whether a reference
  architecture architecturally fits a concrete use case.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
tags:
- workflows
- reference-architecture
- validation
- methodology
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:02:22.540545+00:00'
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
---

# Overview

The Reference Architecture Use-Case Validation Guide is an evaluation framework and operating guide used to assess whether a given reference architecture (RA) is an appropriate architectural fit for a concrete real-world use case [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]. Maintained under the [Reference Architectures Workstream](../working-groups/workflows-and-process-integration/reference-architectures-workstream.md), the guide provides standardized evaluation criteria for both human contributors and automated coding agents to test and document architectural alignment without requiring premature implementation audits [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64], [^evt-wg-workflows-and-process-integration-pr-35].

# Architecture / Specification

### Validation Scope and Guarantees

Validation evaluates whether a target use case shares the primary practitioner job and critical system boundaries that the reference architecture is designed to address [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]:

- **Architectural Fit vs. Implementation Audit**: A `Validated` classification indicates that the RA's structure, boundaries, and capability roles fit the use case. It does not certify that an existing system already implements every technical control specified by the RA (such as specific retry policies, credential management, hash checking, or storage mechanisms), as these controls represent architectural requirements provided by the RA for safe operation rather than prerequisites for validation [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
- **Evidence Grounding**: Validation assessments must rely strictly on documented evidence from the [Use Case Inventory](../working-groups/workflows-and-process-integration/critical-use-cases-workstream.md) or primary source references. Illustrative examples embedded within an RA document do not qualify as independent validation [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

### Evaluation Process

Validation proceeds through a structured review against the RA's specification:

1. **Checklist & Boundary Comparison**: Compare the RA's checklist, boundaries, guarantees, and exit states against the use case to verify if the RA addresses the core practitioner job [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
2. **Role Allocation**: Map entity responsibilities across the agent, workflow orchestrator, human reviewer, and external integrated systems [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
3. **Failure and Recovery Paths**: Confirm that the RA accounts for relevant failure handling, waiting, retry loops, human escalation, and handoff boundaries [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
4. **Outcome Classification**: Output one of four standardized assessment outcomes [^evt-wg-workflows-and-process-integration-pr-35]:
   - `Validated`: The RA provides a complete architectural fit for the job and boundaries.
   - `Partial`: The RA covers substantial portions of the job but leaves critical boundaries unaddressed.
   - `No fit`: The structural requirements or primary job fundamentally diverge from the RA.
   - `Candidate`: Insufficient evidence exists to establish fit, flagging the use case for deeper intake.

[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
[^evt-wg-workflows-and-process-integration-pr-35]: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
