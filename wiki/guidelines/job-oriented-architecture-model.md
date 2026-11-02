---
type: guideline
title: Job-Oriented Architecture Model
description: Architectural framework structuring agent workflows around recognizable
  practitioner jobs rather than abstract capabilities, evaluating machine-readable
  Workflow Design Specifications.
resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/28
tags:
- workflows
- reference-architecture
- design-patterns
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:05:17.279542+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-issue-28
  resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/28
  author: mzagar
  last_modified: '2026-09-24T00:09:43+00:00'
---

# Overview

The Job-Oriented Architecture Model organizes agentic reference architectures around concrete, recognizable practitioner tasks—such as invoice processing or human-approved operational changes—rather than generic model reasoning capabilities[^evt-wg-workflows-and-process-integration-issue-28]. It establishes a layered composition linking reusable workflow patterns into complete reference architectures validated against real-world scenario evidence[^evt-wg-workflows-and-process-integration-issue-28].

# Architecture / Specification

The architectural model operates as a three-tier hierarchy[^evt-wg-workflows-and-process-integration-issue-28]:
1. **Reusable Patterns**: Atomic building blocks that resolve one recurring workflow challenge (such as [approval-checkpoint](../patterns/approval-checkpoint.md) or [durable-wait](../patterns/durable-wait.md)).
2. **Job-Oriented Reference Architectures**: Compositions combining patterns, capability roles, operational boundaries, guarantees, and exit criteria tailored for a defined practitioner role.
3. **Real-World Scenarios / Use Cases**: Empirical scenarios providing operational evidence to test whether a composed architecture fits the problem space.

The Workflows and Process Integration Working Group is evaluating two long-term north-star directions for this model: maintaining the reference architectures strictly as human-readable knowledgebase guidance (Option A), or standardizing a canonical, schema-valid, machine-readable Workflow Design Specification (WDS) serialized in YAML that renders multiple downstream architectural, diagrammatic, and review views (Option B)[^evt-wg-workflows-and-process-integration-issue-28].

# References

- Workflows and Process Integration Working Group [Issue #28](https://github.com/aaif/wg-workflows-and-process-integration/issues/28)[^evt-wg-workflows-and-process-integration-issue-28]

[^evt-wg-workflows-and-process-integration-issue-28]: https://github.com/aaif/wg-workflows-and-process-integration/issues/28
