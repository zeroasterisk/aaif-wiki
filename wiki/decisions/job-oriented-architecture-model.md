---
type: decision
title: Job-Oriented Architecture Model
description: Architectural framework organizing AAIF reference architectures around
  practitioner jobs, reusable patterns, and prospective machine-readable Workflow
  Design Specifications.
resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/28
tags:
- workflows
- architecture
- patterns
- methodology
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:13:54.117507+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-issue-28
  resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/28
  author: mzagar
  last_modified: '2026-09-24T00:09:43+00:00'
---

# Overview

The Job-Oriented Architecture Model establishes a structural paradigm organizing AAIF reference architectures around recognizable practitioner operational jobs rather than abstract capabilities [^evt-wg-workflows-and-process-integration-issue-28]. It composes modular workflow design patterns with concrete validation scenarios to produce consistent and verifiable agentic system architectures.

# Architecture / Specification

The foundational architecture model operates across three complementary tiers [^evt-wg-workflows-and-process-integration-issue-28]:

1. **Reusable Patterns**: Atomic building blocks that resolve recurring workflow challenges, such as [Durable Wait](../patterns/durable-wait.md) and [Human Approval Gate](../patterns/human-approval-gate.md).
2. **Job-Oriented Reference Architectures**: Compositions combining patterns, capability roles, trust boundaries, guarantees, and exit states to execute defined practitioner jobs (e.g., [Bounded Autonomous Remediation](../reference-architectures/bounded-autonomous-remediation.md)).
3. **Real-World Scenarios**: Empirical use cases providing validation evidence and boundary testing for reference compositions.

### North-Star Evolution: Workflow Design Specification

The [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md) is evaluating the long-term delivery artifact of the reference architecture [^evt-wg-workflows-and-process-integration-issue-28]:

- **Option A (Reusable Guidance)**: Reference architectures remain a knowledge base of patterns, compositions, and scenario validation rules, leaving concrete implementation formatting to practitioners.
- **Option B (Machine-Readable Workflow Design Specification)**: Reference architectures produce a versioned, schema-valid, machine-readable specification (WDS in YAML/JSON) from which diagrams, audit views, and implementation handoffs are derived.

# Lifecycle History

Originally formulated by the Reference Architectures Workstream, with expanded scope debated in issue #28 regarding the transition toward executable, schema-backed workflow specifications [^evt-wg-workflows-and-process-integration-issue-28].

[^evt-wg-workflows-and-process-integration-issue-28]: https://github.com/aaif/wg-workflows-and-process-integration/issues/28
