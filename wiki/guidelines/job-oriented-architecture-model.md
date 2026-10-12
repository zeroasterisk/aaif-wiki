---
type: guideline
title: Job-Oriented Architecture Model
description: Architectural guideline organizing workflow reference architectures around
  recognizable practitioner jobs while evaluating machine-readable workflow design
  specifications.
resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/28
tags:
- workflows
- reference-architectures
- patterns
- specification
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:05:41.968863+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-issue-28
  resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/28
  author: mzagar
  last_modified: '2026-09-24T00:09:43+00:00'
---

# Overview
The Job-Oriented Architecture Model structures workflow reference architectures around recognizable, practitioner-centric jobs rather than abstract orchestration mechanics. It establishes a multi-tiered hierarchy linking reusable workflow patterns, such as [durable wait](../patterns/durable-wait.md) and [human approval gates](../patterns/human-approval-gate.md), into composed job-oriented reference architectures evaluated against real-world use case scenarios [^evt-wg-workflows-and-process-integration-issue-28].

# Architecture / Specification
Under the job-oriented model, architectural artifacts are organized across three primary strata:
- **Reusable Patterns:** Granular solutions solving recurring workflow challenges, such as the [approval checkpoint](../patterns/approval-checkpoint.md) or [bounded convergence loop](../patterns/bounded-convergence-loop.md) [^evt-wg-workflows-and-process-integration-issue-28].
- **Job-Oriented Reference Architectures:** Compositions of patterns, capability roles, boundary controls, guarantees, and exit states tailored to a defined operational task [^evt-wg-workflows-and-process-integration-issue-28].
- **Real-World Scenarios:** Empirical use cases that validate whether a reference architecture satisfies concrete operational requirements [^evt-wg-workflows-and-process-integration-issue-28].

## Evolution and Workflow Design Specifications
The workstream is evaluating two north-star trajectories regarding the long-term artifact model [^evt-wg-workflows-and-process-integration-issue-28]:
- **Option A (Reusable Guidance Only):** The reference architecture repository remains a human-readable knowledgebase of patterns, architectures, and validations, leaving implementation-specific documentation formats to adopting organizations [^evt-wg-workflows-and-process-integration-issue-28].
- **Option B (Workflow Design Specification - WDS):** The reference architecture also produces a formal, versioned, schema-validated, machine-readable specification (such as YAML) serving as the canonical source of truth from which diagrams, architectural reviews, and execution handoffs can be derived [^evt-wg-workflows-and-process-integration-issue-28].

[^evt-wg-workflows-and-process-integration-issue-28]: https://github.com/aaif/wg-workflows-and-process-integration/issues/28
