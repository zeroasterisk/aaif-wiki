---
type: taxonomy
title: Guardrail
description: Universal taxonomy term defining a model-level constraint that prescribes
  intended actions or prevents unwanted actions and disclosures.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/91
tags:
- taxonomy
- safety
- guardrail
- constraints
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:14:48.488964+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-91
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/91
  author: julianna-ciq
  last_modified: '2026-10-15T15:39:46+00:00'
---

# Overview
Guardrail is a universal taxonomy term defining a form of constraint on a model that prescribes intended actions or prevents unwanted actions or disclosures[^evt-ws-taxonomy-landscape-pr-91]. While guardrails apply directly to models, agent harnesses host and provide their runtime execution boundaries and enforcement mechanisms[^evt-ws-taxonomy-landscape-pr-91].

# Architecture / Specification
Within the AAIF taxonomy schema, guardrails represent targeted operational constraints governing model input and output boundaries[^evt-ws-taxonomy-landscape-pr-91]:
- **Target of Evaluation**: Guardrails specifically target models, prescribing intended behavior or restricting unwanted disclosures and tool invocation sequences[^evt-ws-taxonomy-landscape-pr-91].
- **Harness Integration**: The agent harness acts as the hosting environment providing context and executing pre- and post-generation guardrail checks[^evt-ws-taxonomy-landscape-pr-91].
- **Constraint Specialization**: Connects to the broader concept of constraint, formalizing active policy enforcement rules rather than ambient runtime limitations[^evt-ws-taxonomy-landscape-pr-91].

# Lifecycle History
The term was introduced as a universal taxonomy definition in PR #91 within the [Taxonomy and Landscape Working Group](../working-groups/taxonomy-and-landscape.md) (`aaif/ws-taxonomy-landscape`)[^evt-ws-taxonomy-landscape-pr-91]. Category assignments and broader term hierarchies were deferred pending alignment with related governance entries[^evt-ws-taxonomy-landscape-pr-91].

# References
- Taxonomy & Landscape PR #91: https://github.com/aaif/ws-taxonomy-landscape/pull/91

[^evt-ws-taxonomy-landscape-pr-91]: https://github.com/aaif/ws-taxonomy-landscape/pull/91
