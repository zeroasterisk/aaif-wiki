---
type: taxonomy
title: Reliability
description: Stability of correct results across repeated agent runs and changing
  environmental conditions within a declared operational scope.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/102
tags:
- taxonomy
- evaluation
- reliability
- metrics
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:44:45.603116+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-102
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/102
  author: jordanauge
  last_modified: '2026-11-12T09:20:37+00:00'
---

# Overview
Reliability in agentic AI is the stability of correct results across repeated runs and changing conditions within a declared operational scope[^evt-ws-taxonomy-landscape-pr-102]. Authored as part of the Accuracy and Reliability Working Group (ARWG) Deliverable 1 canonical glossary, the definition explicitly separates behavioral dependability from lower-level infrastructure and platform availability[^evt-ws-taxonomy-landscape-pr-102].

# Architecture / Specification
Reliability is evaluated across four core dimensions within the agent's declared scope note[^evt-ws-taxonomy-landscape-pr-102]:
- **Consistency**: Generating equivalent and reproducible outputs when presented with identical or functionally equivalent inputs across distinct sessions.
- **Robustness**: Retaining valid operational capabilities and bounded degradation in the presence of noisy, incomplete, or shifting external environment inputs.
- **Predictability**: Maintaining execution paths that conform strictly to stated behavioral parameters rather than exhibiting high-variance emergent actions.
- **Safety**: Preserving operational boundaries and avoiding harmful side effects even under boundary failures or partial service outages.

The concept stands in contrast to accuracy, which gauges the degree of correctness for an individual output against ground truth, and platform availability, which tracks raw uptime of compute, tool endpoints, and [infrastructure](../taxonomy/infrastructure.md)[^evt-ws-taxonomy-landscape-pr-102].

# Lifecycle History
The term was voted KEEP in the Taxonomy Workstream consensus review and submitted for formal inclusion via pull request in the taxonomy registry[^evt-ws-taxonomy-landscape-pr-102].

[^evt-ws-taxonomy-landscape-pr-102]: https://github.com/aaif/ws-taxonomy-landscape/pull/102
