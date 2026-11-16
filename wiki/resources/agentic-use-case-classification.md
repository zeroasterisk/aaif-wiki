---
type: resource
title: Agentic Use Case Classification
description: Multi-dimensional taxonomy and classification schema characterizing agentic
  AI production deployments across operational patterns and human interaction levels.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/62
tags:
- workflows
- classification
- taxonomy
- use-cases
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:44:45.603116+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-62
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/62
  author: jodeev
  last_modified: '2026-11-12T16:32:21+00:00'
---

# Overview
The Agentic Use Case Classification schema is a standardized evaluation matrix created by the [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md) to characterize production agent implementations by operational pattern, automation tier, and risk level[^evt-wg-workflows-and-process-integration-pr-62]. The schema indexes deployed enterprise and community workflows to guide adoption and reference architecture selection[^evt-wg-workflows-and-process-integration-pr-62].

# Architecture / Specification
The schema classifies agentic deployments through several primary axes:
- **Interaction Topology**: Single-agent execution versus orchestrated multi-agent topologies such as parallel research or supervisor patterns.
- **Oversight and Approval**: Presence of deterministic gates, human authorization checkpoints, or unconstrained autonomous iterations.
- **Action Radius**: Read-only analysis, sandboxed state generation, or direct external side-effect execution across production tool interfaces.
- **State and Context Lifecycle**: Ephemeral single-turn tasks versus persistent, recoverable conversational and memory sessions.

# Lifecycle History
Following review, the Workflows and Process Integration Working Group formally approved the use case classification schema and its initial seed list of reference deployments, removing provisional draft markers from the specification while migrating remaining feature feedback into ongoing tracker issues[^evt-wg-workflows-and-process-integration-pr-62].

[^evt-wg-workflows-and-process-integration-pr-62]: https://github.com/aaif/wg-workflows-and-process-integration/pull/62
