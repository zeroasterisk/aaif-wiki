---
type: project
title: Agent Skills
description: An open format and specification for packaging procedural knowledge,
  workflows, and tool instructions into portable on-demand agent capability bundles.
resource: https://github.com/aaif/project-proposals/issues/47
tags:
- capability
- packaging
- skills
- specification
- progressive-disclosure
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T06:00:39.547716+00:00'
sources:
- id: evt-project-proposals-issue-47
  resource: https://github.com/aaif/project-proposals/issues/47
  author: claim-ant
  last_modified: '2026-10-02T03:46:40+00:00'
---

# Overview

Agent Skills is an open specification and folder-based format for extending AI agent capabilities with specialized procedural knowledge, multi-step workflows, and contextual instructions[^evt-project-proposals-issue-47]. Originally developed by Anthropic and released as an open standard in December 2025, Agent Skills packages domain context and tool usage rules into version-controlled folders centered around a `SKILL.md` file[^evt-project-proposals-issue-47].

# Architecture / Specification

Agent Skills standardizes the capability layer, sitting complementarily alongside runtime tool protocols like the Model Context Protocol (MCP) and repository-scoped instructions like AGENTS.md[^evt-project-proposals-issue-47].

### Progressive Disclosure Model
Skills are loaded by compatible agent runtimes (such as [Goose](../projects/goose.md)) using a three-stage progressive disclosure pipeline that optimizes agent context window utilization[^evt-project-proposals-issue-47]:
1. **Discovery**: At startup, runtimes ingest only high-level skill metadata (the `name` and `description` defined in frontmatter)[^evt-project-proposals-issue-47].
2. **Activation**: When a user task or agent sub-goal matches a skill's description, the agent reads the full `SKILL.md` instructions into active context[^evt-project-proposals-issue-47].
3. **Execution**: The agent executes the specified procedural steps, loading bundled reference documents, templates, or executing local scripts as required[^evt-project-proposals-issue-47].

# Lifecycle History

Anthropic first introduced the capability format on October 16, 2025, and published it as an open standard on December 18, 2025[^evt-project-proposals-issue-47]. In 2026, a proposal was submitted to the AAIF [Technical Committee](../governance/technical-committee.md) to transfer the specification repository, reference validator, and domain assets into neutral foundation governance[^evt-project-proposals-issue-47].

[^evt-project-proposals-issue-47]: https://github.com/aaif/project-proposals/issues/47
