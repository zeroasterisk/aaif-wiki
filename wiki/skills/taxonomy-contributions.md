---
type: skill
title: Taxonomy Contributions Skill
description: Modular agent skill providing automated routing, pre-drafting validation,
  and schema compliance for AAIF taxonomy and landscape submissions.
resource: https://github.com/aaif/public-agents/pull/3
tags:
- skills
- taxonomy
- landscape
- tooling
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:58:36.377829+00:00'
sources:
- id: evt-public-agents-pr-3
  resource: https://github.com/aaif/public-agents/pull/3
  author: asish-singh
  last_modified: '2026-08-22T12:50:41+00:00'
---

# Overview
The Taxonomy Contributions skill (`aaif-taxonomy-contributions`) guides automated agents in preparing, validating, and routing submissions to the AAIF Common Taxonomy and Landscape workstream [^evt-public-agents-pr-3]. It codifies repository contribution rules, schema constraints, and triage workflows to ensure third-party landscape entries and terminology definitions meet baseline quality standards before submission [^evt-public-agents-pr-3].

# Architecture / Specification
The skill encapsulates contribution logic across several verification stages [^evt-public-agents-pr-3]:
- **Pre-Drafting Checks**: Inspects the target repository for in-flight issues or pull requests proposing identical terms or landscape components to prevent duplicates [^evt-public-agents-pr-3].
- **Routing Rules**: Directs agents to appropriate submission channels (e.g., structured `Define` issue templates versus weekly sync agenda items for deferred definition fields) [^evt-public-agents-pr-3].
- **Schema Conformance**: Strips marketing superlatives from landscape descriptions, validates required fields (including undocumented live fields like `logo`), and verifies term syntax against the data schema [^evt-public-agents-pr-3].
- **Dynamic Documentation Retrieval**: Instructs agents to fetch live repository guidelines prior to drafting, degrading safely when upstream workstream schemas evolve [^evt-public-agents-pr-3].

# Lifecycle History
Proposed in PR #3 within the `public-agents` repository to streamline multi-step agent triage for `aaif/ws-taxonomy-landscape` contributions [^evt-public-agents-pr-3].

# References
- [`resources/public-agent-skills`](../resources/public-agent-skills.md)
- [`working-groups/taxonomy-and-landscape`](../working-groups/taxonomy-and-landscape.md)

[^evt-public-agents-pr-3]: https://github.com/aaif/public-agents/pull/3
