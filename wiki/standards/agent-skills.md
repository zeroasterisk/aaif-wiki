---
type: standard
title: Agent Skills Specification
description: Open file-based packaging format and progressive disclosure standard
  for extending AI agents with procedural knowledge, executable scripts, and resources.
resource: https://github.com/aaif/project-proposals/issues/47
tags:
- standard
- packaging
- skills
- interoperability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:39:03.028504+00:00'
sources:
- id: evt-project-proposals-issue-47
  resource: https://github.com/aaif/project-proposals/issues/47
  author: claim-ant
  last_modified: '2026-10-02T03:46:40+00:00'
---

# Overview
The Agent Skills specification defines an open, file-based packaging format for extending AI agent capabilities with specialized domain knowledge, repeatable multi-step workflows, and operational resources [^evt-project-proposals-issue-47]. Structurally composed of a directory containing a `SKILL.md` file alongside optional scripts, templates, and reference documentation, the standard establishes a portable capability layer across heterogeneous agent runtimes and development environments [^evt-project-proposals-issue-47].

Originally developed by Anthropic and published as an open standard, Agent Skills was formally submitted for project intake under the [Technical Committee](../governance/technical-committee.md) to transition canonical stewardship, specifications, and reference tooling to neutral governance under the Agentic AI Foundation [^evt-project-proposals-issue-47].

# Architecture / Specification

## Three-Stage Progressive Disclosure
To manage context window utilization effectively, agents load skills via progressive disclosure across three operational phases [^evt-project-proposals-issue-47]:
1. **Discovery**: At runtime startup, an agent inspects only the lightweight metadata (such as skill name and descriptive summary) of all installed skills, maintaining an intentionally small baseline context footprint [^evt-project-proposals-issue-47].
2. **Activation**: When an incoming prompt or operational objective matches a skill's activation description, the agent ingests the complete procedural instructions of `SKILL.md` into active context [^evt-project-proposals-issue-47].
3. **Execution**: The agent executes the prescribed instructions, optionally running bundled code scripts, querying referenced datasets, or invoking client tools as needed [^evt-project-proposals-issue-47].

## Interoperability and Complementary Protocols
Agent Skills addresses capability packaging alongside adjacent foundational standards [^evt-project-proposals-issue-47]:
- **Model Context Protocol (MCP)**: Operates at the connectivity and tool execution layer; Agent Skills provides procedural guidance defining when, how, and in what order to invoke specific MCP tools [^evt-project-proposals-issue-47].
- **AGENTS.md**: Operates as a persistent, repository-level instruction file describing project-specific setup, whereas skills provide modular, portable capabilities reusable across repositories [^evt-project-proposals-issue-47].
- **Agent Client Protocol (ACP)**: Defines IDE-to-agent communication channels over which skill execution and file modification requests are mediated [^evt-project-proposals-issue-47].

# Lifecycle History
Anthropic originally introduced Agent Skills on October 16, 2025, and published the open specification on December 18, 2025 [^evt-project-proposals-issue-47]. In 2026, an official proposal was submitted to the AAIF to transfer the specification repository, reference implementations, and associated domains to foundation ownership [^evt-project-proposals-issue-47].

[^evt-project-proposals-issue-47]: https://github.com/aaif/project-proposals/issues/47
