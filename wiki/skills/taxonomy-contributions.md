---
type: skill
title: Taxonomy Contributions Skill
description: Progressively disclosed agent skill guiding automated routing, schema
  validation, and superlative removal for AAIF Common Taxonomy and Landscape contributions.
resource: https://github.com/aaif/public-agents/pull/3
tags:
- skills
- taxonomy
- landscape
- contributions
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T11:01:50.430523+00:00'
sources:
- id: evt-public-agents-pr-3
  resource: https://github.com/aaif/public-agents/pull/3
  author: asish-singh
  last_modified: '2026-10-11T18:18:20+00:00'
---

# Overview

The Taxonomy Contributions skill (`aaif-taxonomy-contributions`) provides structured protocols for AI agents preparing contributions to the AAIF Common Taxonomy and Landscape workstream.[^evt-public-agents-pr-3] The skill unifies contribution requirements across schema specifications, issue templates, and runtime data files, preventing common workflow failures such as opening pull requests for terms that require working group discussion issues.[^evt-public-agents-pr-3]

# Architecture / Specification

## Contribution Routing and Pre-Drafting Checks

Before generating pull requests or taxonomy entries, the skill guides agents through a standardized decision flow:[^evt-public-agents-pr-3]
- **In-Flight Proposal Deduplication**: Inspects open pull requests and issues to prevent duplicate or conflicting submissions.
- **Routing Validation**: Directs contributors to use the appropriate channel (Define issue template vs. Landscape PR) based on definition maturity.
- **Objective Tone Enforcement**: Enforces pre-competitive neutrality by detecting and stripping marketing superlatives prior to submission.

## Operational Performance and Efficiency

Empirical testing demonstrated that agents equipped with the skill reduced exploratory repository tool calls from 15 calls down to 6 targeted operations, successfully validating schema compliance against live landscape schema rules.[^evt-public-agents-pr-3]

# References

- [Taxonomy & Landscape Working Group](../working-groups/taxonomy-and-landscape.md)
- [Agentic AI Landscape Resource](../resources/agentic-ai-landscape.md)
- [Working Group Submission Guidelines](../guidelines/working-group-submission-guidelines.md)

[^evt-public-agents-pr-3]: https://github.com/aaif/public-agents/pull/3
