---
type: proposal
title: Agent Skills Specification
description: Open packaging format structuring procedural knowledge, metadata, scripts,
  and resources into version-controlled folders loaded via progressive disclosure.
resource: https://github.com/aaif/project-proposals/issues/47
tags:
- packaging
- capabilities
- skills
- specifications
- context-engineering
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:26:10.204199+00:00'
sources:
- id: evt-project-proposals-issue-47
  resource: https://github.com/aaif/project-proposals/issues/47
  author: claim-ant
  last_modified: '2026-10-02T03:46:40+00:00'
---

# Overview

Agent Skills is an open packaging format and specification designed to extend AI agent capabilities with domain expertise, repeatable procedures, and contextual instructions.[^evt-project-proposals-issue-47] A skill is packaged as a directory containing a `SKILL.md` file detailing name and description metadata alongside procedural instructions, optional executable scripts, templates, and reference materials.[^evt-project-proposals-issue-47]

To conserve agent context, skills utilize a three-stage progressive disclosure lifecycle: discovery (loading only names and descriptions at startup), activation (loading full `SKILL.md` instructions when a task matches the description), and execution (carrying out instructions, executing bundled code, or referencing assets as needed).[^evt-project-proposals-issue-47]

# Architecture / Specification

The Agent Skills format standardizes capability packaging adjacent to runtime integration protocols like the Model Context Protocol (MCP) and repository configuration conventions such as `AGENTS.md`.[^evt-project-proposals-issue-47] While MCP provides tool connectivity and execution primitives, Agent Skills defines procedural guidance on how and when to invoke tools.[^evt-project-proposals-issue-47] Conforming skills are portable across multiple client implementations and runtimes such as [Goose](../reference-architectures/goose.md).[^evt-project-proposals-issue-47]

# Lifecycle History

Agent Skills was originally developed by Anthropic as a product feature in October 2025 and published as an open standard in December 2025.[^evt-project-proposals-issue-47] Proposal ISSUE#47 submitted the specification, reference validator, documentation, and assets to the Agentic AI Foundation for neutral ecosystem governance.[^evt-project-proposals-issue-47]

[^evt-project-proposals-issue-47]: https://github.com/aaif/project-proposals/issues/47
