---
type: taxonomy
title: Meta-harness
description: Taxonomy definition and scope note for meta-harnesses orchestrating and
  composing lower-level agent execution harnesses.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/48
tags:
- taxonomy
- execution
- orchestration
- runtime
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:08:25.399504+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-48
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/48
  author: jmaionchi
  last_modified: '2026-09-14T15:58:16+00:00'
---

# Overview
A meta-harness is an architectural construct and execution framework that composes, coordinates, or manages multiple specialized agent harnesses across workflow stages [^evt-ws-taxonomy-landscape-pr-48]. Standardized by the [Taxonomy and Landscape Workstream](../working-groups/taxonomy-and-landscape.md), the term distinguishes higher-level coordination layers from individual, low-level execution harnesses [^evt-ws-taxonomy-landscape-pr-48].

# Architecture / Specification
In the AAIF SKOS Lite taxonomy model, `Meta-harness` is linked to `Harness` through bidirectional `relatedTerms` relationships rather than strict hierarchy or contrast, reflecting their compositional nature [^evt-ws-taxonomy-landscape-pr-48]:
- **Compositional Relationship**: A meta-harness acts above single-agent harnesses, orchestrating multiple runtimes or tool-boundary environments rather than replacing individual runtime harnesses [^evt-ws-taxonomy-landscape-pr-48].
- **Taxonomy Placement**: Categorized alongside agent execution models and runtime architectures to unify vocabulary across AAIF working groups [^evt-ws-taxonomy-landscape-pr-48].

# References
- AAIF Taxonomy and Landscape Workstream [^evt-ws-taxonomy-landscape-pr-48]

[^evt-ws-taxonomy-landscape-pr-48]: https://github.com/aaif/ws-taxonomy-landscape/pull/48
