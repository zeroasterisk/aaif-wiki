---
type: skill
title: AAIF Taxonomy Contributions Skill
description: An agent skill guiding contributors and agents in preparing schema-conformant
  proposals for the AAIF taxonomy and landscape.
resource: https://github.com/aaif/public-agents/pull/3
tags:
- skill
- taxonomy
- landscape
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:55:54.344066+00:00'
sources:
- id: evt-public-agents-pr-3
  resource: https://github.com/aaif/public-agents/pull/3
  author: asish-singh
  last_modified: '2026-08-22T12:50:41+00:00'
---

# Overview
The `aaif-taxonomy-contributions` skill guides agents and contributors through the routing, schema verification, and drafting workflow required for contributions to the AAIF Common Taxonomy and Landscape workstream [^evt-public-agents-pr-3].

# Architecture / Specification
- **Contribution Routing**: Directs contributions toward the appropriate entry points (e.g., Define issues, weekly sync discussions, or landscape PRs) based on workstream governance [^evt-public-agents-pr-3].
- **Pre-drafting Checks**: Performs automated deduplication by querying in-flight term definitions and open landscape pull requests before drafting [^evt-public-agents-pr-3].
- **Schema & Quality Bar Enforcement**: Strips non-neutral superlatives and marketing language in accordance with pre-competitive landscape rules, validating YAML formatting, entry fields (`name`, `homepage_url`, `description`, `project`, `logo`), and definition structures [^evt-public-agents-pr-3].
- **Dynamic Guideline Fetching**: Instructs agents to fetch live repository guidelines prior to drafting to accommodate evolving workstream processes [^evt-public-agents-pr-3].

Related initiatives and working groups include [../initiatives/agentic-ai-landscape.md](../initiatives/agentic-ai-landscape.md) and [../working-groups/taxonomy-and-landscape.md](../working-groups/taxonomy-and-landscape.md).

[^evt-public-agents-pr-3]: https://github.com/aaif/public-agents/pull/3
