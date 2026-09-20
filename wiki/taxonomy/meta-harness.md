---
type: taxonomy-term
title: Meta-Harness
description: An execution harness or orchestration framework that manages, coordinates,
  or composes multiple underlying agent harnesses.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/48
tags:
- taxonomy
- runtime
- orchestration
- harness
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T18:01:17.701184+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-48
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/48
  author: jmaionchi
  last_modified: '2026-09-14T15:58:16+00:00'
---

# Overview
A meta-harness is an architectural layer and execution framework that coordinates, configures, or composes multiple distinct agent harnesses[^evt-ws-taxonomy-landscape-pr-48]. While an individual harness wraps and manages the execution lifecycle of a single agent instance, a meta-harness operates at a higher tier of abstraction across multi-agent or multi-runtime topologies[^evt-ws-taxonomy-landscape-pr-48].

# Architecture / Specification
Within the AAIF taxonomy schema, meta-harness relates directly to `taxonomy/harness` via compositional relationships rather than mutual exclusion[^evt-ws-taxonomy-landscape-pr-48]:
- **Compositional Relationship**: A meta-harness encapsulates or supervises multiple child harnesses, managing context handoffs, credential boundaries, and joint task lifecycles[^evt-ws-taxonomy-landscape-pr-48].
- **Taxonomy Placement**: Linked bidirectionally with [Harness](../taxonomy/harness.md) through `relatedTerms`[^evt-ws-taxonomy-landscape-pr-48].

# Lifecycle History
- Defined and approved by the Taxonomy and Landscape workstream via PR #48, expanding upon foundational runtime terms[^evt-ws-taxonomy-landscape-pr-48].

[^evt-ws-taxonomy-landscape-pr-48]: https://github.com/aaif/ws-taxonomy-landscape/pull/48
