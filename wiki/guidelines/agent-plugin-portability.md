---
type: guideline
title: Agent Plugin Portability
description: Standards for packaging portable agent plugins, resolving skill root
  paths, and structuring progressive disclosure between SKILL.md and WORKFLOW.md.
resource: https://github.com/aaif/community-events/pull/54
tags:
- standards
- agent-plugins
- skills
- portability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:17:07.477767+00:00'
sources:
- id: evt-community-events-pr-54
  resource: https://github.com/aaif/community-events/pull/54
  author: rparundekar
  last_modified: '2026-10-01T02:01:13+00:00'
- id: evt-community-events-file-eca12c0a30e2-fd49cca9
  resource: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/CONTRIBUTING.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
- id: evt-community-events-file-ed850506c872-63272570
  resource: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/skills/aaif-community-pulse/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
---

# Overview
Agent Plugin Portability defines architectural standards for authoring, packaging, and distributing vendor-neutral AI agent skills across client runtimes such as Claude Code, Codex, and Cursor [^evt-community-events-pr-54]. The standard mandates portable directory placeholders, explicit execution compatibility manifests, and token-bounded procedural documents to maximize runtime reliability and cross-client compatibility [^evt-community-events-file-eca12c0a30e2-fd49cca9].

# Architecture / Specification

## Plugin and Skill Directory Layout
A portable agent plugin encapsulates skills, manifests, and validation tools within a standardized repository structure [^evt-community-events-pr-54][^evt-community-events-file-eca12c0a30e2-fd49cca9]:
- `plugin.json`: Shared root manifest declaring the plugin identifier, version, and exposed skills.
- `.claude-plugin/`: Client-specific manifests (`plugin.json`, `marketplace.json`) retained for backwards compatibility.
- `skills/<skill-name>/`: Individual capability directories containing:
  - `SKILL.md`: Core procedural spine bounded strictly under 500 lines (~5,000 tokens).
  - `WORKFLOW.md`: Extended procedural sequences linked progressively for complex workflows.
  - `scripts/`: Executable helper tools, each paired with unit tests (`test_*.py`).
  - `references/`: Detailed reference documentation loaded on demand with explicit trigger conditions.

## Path Resolution and Metadata Standards
- **Placeholder Resolution**: File references within skills must avoid client-specific environment variables (such as `${CLAUDE_SKILL_DIR}`) and use client-agnostic `<skill-root>` placeholders resolved dynamically from `SKILL.md` [^evt-community-events-pr-54][^evt-community-events-file-ed850506c872-63272570].
- **Frontmatter Declarations**: Every `SKILL.md` must declare a descriptive `name`, activation criteria in `description` ("Use when asked to..."), and an explicit `compatibility` string listing runtime prerequisites [^evt-community-events-file-eca12c0a30e2-fd49cca9]. Client-specific extensions must be scoped under the `metadata` namespace [^evt-community-events-pr-54].

## References
- Operational reference skills are documented in [Community Event Operations](../skills/community-event-operations.md).

[^evt-community-events-file-eca12c0a30e2-fd49cca9]: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/CONTRIBUTING.md
[^evt-community-events-file-ed850506c872-63272570]: https://github.com/aaif/community-events/blob/7812e00cb0da0153a9a93f3e19040b1f608a4901/skills/aaif-community-pulse/SKILL.md
[^evt-community-events-pr-54]: https://github.com/aaif/community-events/pull/54
