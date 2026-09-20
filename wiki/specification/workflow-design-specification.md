---
type: specification
title: Workflow Design Specification
description: A proposed machine-readable specification format and design method capturing
  agentic workflow designs across deterministic, model-assisted, and agent-driven
  systems.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/21
tags:
- specification
- workflows
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:48:49.167309+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-21
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/21
  author: mzagar
  last_modified: '2026-08-08T14:58:27+00:00'
---

# Overview
The Workflow Design Specification (WDS) is a proposed formal, machine-readable artifact within the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md) that captures recommended agentic workflow designs for automated implementation by coding agents or human engineers.[^evt-wg-workflows-and-process-integration-pr-21] It is paired with the Workflow Design Method (WDM), a repeatable procedure for translating business use cases into compliant workflow specifications.[^evt-wg-workflows-and-process-integration-pr-21]

# Architecture / Specification
The specification-driven architecture is structured around three core principles:[^evt-wg-workflows-and-process-integration-pr-21]

- **Spectrum-Wide Coverage**: Unifies deterministic, model-assisted, and agent-driven workflows under a single vocabulary, recommending the least-agentic pattern required for a given task rather than treating agent count as the core organizing factor.[^evt-wg-workflows-and-process-integration-pr-21]
- **Shared Design Artifact (WDS)**: Provides a standardized, machine-interpretable blueprint used as the direct input for downstream workflow synthesis and execution.[^evt-wg-workflows-and-process-integration-pr-21]
- **Workflow Design Method (WDM)**: Defines repeatable analysis steps executed by either human architects or AI agents to generate valid WDS blueprints from domain requirements.[^evt-wg-workflows-and-process-integration-pr-21]

[^evt-wg-workflows-and-process-integration-pr-21]: https://github.com/aaif/wg-workflows-and-process-integration/pull/21
