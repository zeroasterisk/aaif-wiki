---
type: standard
title: Agent Skills
description: Open file-based packaging format and progressive disclosure standard
  for extending AI agents with procedural knowledge, scripts, and domain workflows.
resource: https://github.com/aaif/project-proposals/issues/47
tags:
- agent-skills
- packaging
- extensibility
- progressive-disclosure
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:18:20.208859+00:00'
sources:
- id: evt-project-proposals-issue-47
  resource: https://github.com/aaif/project-proposals/issues/47
  author: claim-ant
  last_modified: '2026-10-02T03:46:40+00:00'
---

# Overview

Agent Skills is an open specification and folder structure format for packaging specialized procedural knowledge, scripts, and workflows for AI agents [^evt-project-proposals-issue-47]. Rooted in a self-contained directory with a `SKILL.md` file containing metadata and operational instructions, skills allow portable contextual capabilities to be authored once and executed across conforming agent runtimes [^evt-project-proposals-issue-47].

# Architecture / Specification

Agent Skills standardizes execution through progressive disclosure to minimize context consumption [^evt-project-proposals-issue-47]:
1. **Discovery**: At runtime startup, an agent inspects only top-level metadata (`name` and `description`) across configured skill repositories.
2. **Activation**: When an incoming prompt matches a skill description, the agent loads the complete `SKILL.md` instructions into active context.
3. **Execution**: The agent follows procedural instructions, invoking bundled scripts, referenced templates, or external Model Context Protocol tools as necessary [^evt-project-proposals-issue-47].

It complements repository-level instruction files such as AGENTS.md by isolating portable, on-demand domain tasks from project-specific workspace guidelines (see [../guidelines/agent-plugin-portability.md](../guidelines/agent-plugin-portability.md)) [^evt-project-proposals-issue-47].

# Lifecycle History

Originally developed by Anthropic and published as an open standard in December 2025, the format was proposed for neutral ownership under the Agentic AI Foundation in September 2026 [^evt-project-proposals-issue-47].

[^evt-project-proposals-issue-47]: https://github.com/aaif/project-proposals/issues/47
