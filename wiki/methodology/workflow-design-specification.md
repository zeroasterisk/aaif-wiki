---
type: methodology
title: Workflow Design Specification
description: A formal, machine-readable specification and design methodology for defining
  agentic workflows across deterministic and autonomous execution modes.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/21
tags:
- workflows
- reference-architecture
- specification
- process-integration
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:51:24.993490+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-21
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/21
  author: mzagar
  last_modified: '2026-08-08T14:58:27+00:00'
---

# Overview
The Workflow Design Specification (WDS) is a proposed formal, machine-readable artifact for defining agentic workflows, developed in the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md)[^evt-wg-workflows-and-process-integration-pr-21]. It pairs with a Workflow Design Method (WDM) to transform business use cases into standardized blueprints that can be executed directly by coding agents or human software engineers[^evt-wg-workflows-and-process-integration-pr-21].

# Architecture / Specification
The specification framework is structured around three key design principles[^evt-wg-workflows-and-process-integration-pr-21]:
- **Unified Spectrum Coverage**: Spans deterministic, model-assisted, and agent-driven workflows within a single vocabulary, treating agent count not as an organizing principle but as an outcome of recommending the least-agentic pattern suitable for the task.
- **Shared Artifact (WDS)**: Provides a single structured specification capturing target workflow architecture, execution boundaries, state requirements, and integration points for downstream implementation.
- **Formal Design Method (WDM)**: Outlines repeatable steps to translate business requirements into a valid WDS, designed for interchangeable execution by human architects and AI agents.

[^evt-wg-workflows-and-process-integration-pr-21]: https://github.com/aaif/wg-workflows-and-process-integration/pull/21
