---
type: guideline
title: Reference Architecture Use Case Validation Guide
description: Standardized methodology and criteria for evaluating whether a real-world
  use case aligns with an AAIF reference architecture.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
tags:
- aaif
- workflows
- reference-architecture
- validation
- guidelines
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:40:18.524329+00:00'
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
The Reference Architecture Use Case Validation Guide defines a repeatable, lightweight evaluation process for assessing whether an AAIF Reference Architecture (RA) is an architectural fit for a specific real-world use case [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]. Intended for both human contributors and AI coding agents, validation focuses on matching the primary job and defining boundaries rather than verifying implementation-level mechanics [^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30].

# Architecture / Specification
Validation determines whether an RA provides the architectural controls needed to implement a target use case safely [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

## Core Validation Principles
- **Job and Boundary Fit:** A use case is marked `Validated` when the source demonstrates the RA's primary job and key operational boundaries, even if specific runtime mechanics (such as credential storage or exact retry backoff) are not detailed [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
- **Sourced Evidence Requirement:** Evidence must derive from stated facts in the Use Case Inventory or cited external artifacts, rather than illustrative scenario text embedded within RA specifications [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
- **Constrained Check Counts:** Evaluations must establish two or three concise checks derived from the RA's purpose, checklist, boundaries, and guarantees [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

## Evaluation Outcomes
1. **Validated:** The RA's primary job, actor roles (agent, workflow engine, human, external system), and boundaries match the use case [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
2. **Partial:** Some architectural boundaries or capabilities align, but key operational requirements or control paths diverge [^evt-wg-workflows-and-process-integration-pr-35].
3. **No Fit:** The use case core requirements contradict the structural guarantees or authority model of the RA [^evt-wg-workflows-and-process-integration-pr-35].
4. **Candidate:** Initial alignment observed, but essential evidence is missing or requires further investigation [^evt-wg-workflows-and-process-integration-pr-35].

## Contributor and Agent Guidelines
AI and human contributors follow standardized intake workflows, submitting a GitHub Issue when guidance or evidence is lacking, or opening a focused pull request against the RA's validation record when evidence is clear [^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64, ^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30].

# References
- [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md)
- [Workflow Architecture Principles](workflow-architecture-principles.md)

[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
[^evt-wg-workflows-and-process-integration-file-cd94574f9d34-a7acfb30]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/AGENTS.md
[^evt-wg-workflows-and-process-integration-pr-35]: https://github.com/aaif/wg-workflows-and-process-integration/pull/35
