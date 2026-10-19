---
type: standard
title: Agent Plugins Specification
description: Open packaging format and client configuration standard combining Agent
  Skills and Model Context Protocol servers into distributable plugins.
resource: https://github.com/aaif/project-proposals/issues/56
tags:
- standards
- plugins
- skills
- mcp
- packaging
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:14:48.488964+00:00'
sources:
- id: evt-project-proposals-issue-56
  resource: https://github.com/aaif/project-proposals/issues/56
  author: jonathanhefner
  last_modified: '2026-10-16T00:18:37+00:00'
---

# Overview
Agent Plugins is an open, vendor-neutral packaging standard that bundles reusable components—specifically [Agent Skills](../standards/agent-skills.md) and Model Context Protocol (MCP) server configurations—into distributable plugins across compatible agent clients[^evt-project-proposals-issue-56]. Governed by a cross-vendor Technical Steering Committee, the standard establishes a client configuration contract and conformance test suite while reserving client-specific extension namespaces[^evt-project-proposals-issue-56].

# Architecture / Specification
The specification defines a vendor-neutral package directory structure and manifest format[^evt-project-proposals-issue-56]:
- **Component Composition**: Combines instructions packaged under the [Agent Skills](../standards/agent-skills.md) format with configuration blocks for discovering and connecting to local or remote MCP servers[^evt-project-proposals-issue-56].
- **Protocol Separation**: Retains MCP as the authoritative wire and lifecycle standard, and Agent Skills as the authoritative skill format, standardizing only client packaging and discovery configuration[^evt-project-proposals-issue-56].
- **Extension Namespaces**: Provides reserved, client-owned namespaces to support proprietary host features and custom policies without compromising the portable core[^evt-project-proposals-issue-56].
- **Conformance Suite**: Maintains JSON schemas, client test suites, and migration tools to validate cross-client compatibility[^evt-project-proposals-issue-56].

# Lifecycle History
Originating from the Open Plugin initiative, version 1.0.0 of the specification was published under Apache-2.0 and CC-BY-4.0 licenses before being submitted to the [Technical Committee](../governance/technical-committee.md) in Issue #56 for consideration as an official AAIF standard[^evt-project-proposals-issue-56].

# References
- Agent Plugins Project Proposal: https://github.com/aaif/project-proposals/issues/56
- Agent Plugins Specification Repository: https://github.com/agentplugins/agent-plugins-spec

[^evt-project-proposals-issue-56]: https://github.com/aaif/project-proposals/issues/56
