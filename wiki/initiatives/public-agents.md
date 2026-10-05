---
type: initiative
title: Public Agents
description: Standardized repository of portable agent resources providing reusable
  skills, contribution helpers, and operational capabilities for AAIF tasks.
resource: https://github.com/aaif/public-agents/pull/3
tags:
- agents
- public-agents
- skills
- automation
- initiative
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:01:57.903883+00:00'
sources:
- id: evt-public-agents-pr-3
  resource: https://github.com/aaif/public-agents/pull/3
  author: asish-singh
  last_modified: '2026-08-22T12:50:41+00:00'
---

# Overview
The Public Agents initiative provides a curated, open repository of portable agent resource definitions, reusable skills, and automated workflows designed to assist developers and maintainers across the Agentic AI Foundation.

# Architecture / Specification
Public agent capabilities are modularized into reusable skills and configurations that execute against standardized contributor interfaces:
- **Taxonomy Contribution Skills**: Includes specialized agent skills such as `aaif-taxonomy-contributions` that automate routing decisions, pre-drafting validation checks, definition quality enforcement, and schema conformance for contributions to the [Taxonomy and Landscape Initiative](taxonomy-and-landscape.md)[^evt-public-agents-pr-3].
- **Autonomous Review and Triage**: Integrates with foundation workflows like the [Submission Analyser](submission-analyser.md) to inspect pull requests, strip non-neutral marketing superlatives, and verify landscape dataset schemas[^evt-public-agents-pr-3].

# Lifecycle History
- **Draft Status**: Maintained as an open initiative repository under AAIF governance.
- **Skill Expansion**: Added specialized automation skills to assist external contributors with taxonomy and landscape submissions[^evt-public-agents-pr-3].

[^evt-public-agents-pr-3]: https://github.com/aaif/public-agents/pull/3
