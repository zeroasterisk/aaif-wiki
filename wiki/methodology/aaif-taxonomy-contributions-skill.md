---
type: methodology
title: AAIF Taxonomy Contributions Skill
description: Agent skill guiding automated and manual routing, validation, schema
  conformity, and issue drafting for ws-taxonomy-landscape contributions.
resource: https://github.com/aaif/public-agents/pull/3
tags:
- methodology
- skills
- taxonomy
- landscape
- public-agents
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:00:54.879118+00:00'
sources:
- id: evt-public-agents-pr-3
  resource: https://github.com/aaif/public-agents/pull/3
  author: asish-singh
  last_modified: '2026-08-22T12:50:41+00:00'
---

# Overview
The `aaif-taxonomy-contributions` skill is an agent operational workflow designed to streamline contributions to the AAIF Common Taxonomy and Landscape workstream (`aaif/ws-taxonomy-landscape`) [^evt-public-agents-pr-3]. Proposed within [public-agents](../project/public-agents.md), the skill assists agents and contributors in routing taxonomy changes, performing pre-drafting deduplication checks, stripping non-neutral marketing superlatives, and adhering to strict schema requirements [^evt-public-agents-pr-3].

# Architecture / Specification
The skill addresses dispersed contribution rules across data schemas, contributing guides, and codebase definitions [^evt-public-agents-pr-3]:
- **Routing and Pre-Drafting Checks**: Identifies whether a proposed addition requires an issue, sync discussion, or pull request, and performs search checks to prevent duplicate submissions [^evt-public-agents-pr-3].
- **Schema and Quality Bar Enforcement**: Normalizes entry descriptions to objective, pre-competitive language per [Landscape Inclusion Criteria](../guidelines/landscape-inclusion-criteria.md), ensuring required fields (`name`, `homepage_url`, `description`, `project`, `logo`) meet schema validation [^evt-public-agents-pr-3].
- **Self-Updating Fallback**: Directs agents to fetch live workstream documentation before generating submissions to adapt dynamically to governance updates [^evt-public-agents-pr-3].

[^evt-public-agents-pr-3]: https://github.com/aaif/public-agents/pull/3
