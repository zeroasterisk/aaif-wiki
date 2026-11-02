---
type: guideline
title: Agent Plugin and Skill Portability Guidelines
description: Packaging, capability abstraction, directory resolution, and manifest
  conventions ensuring interoperability between Agent Plugins v1 and agent runtimes.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/.pre-commit-config.yaml
tags:
- standards
- portability
- agent-plugins
- agent-skills
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:13:06.696072+00:00'
sources:
- id: evt-community-events-file-63a9c44a44ac-37822210
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/.pre-commit-config.yaml
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
- id: evt-community-events-pr-54
  resource: https://github.com/aaif/community-events/pull/54
  author: rparundekar
  last_modified: '2026-10-01T02:01:13+00:00'
---

# Overview
The Agent Plugin Portability guidelines define structural conventions, execution path abstractions, and manifest standards that allow AI agent plugins and skills to operate interchangeably across diverse client runtimes [^evt-community-events-pr-54]. These conventions eliminate proprietary path dependencies, standardize client argument hints, and maintain portable declarative contracts [^evt-community-events-pr-54].

# Architecture / Specification
Portable plugin packages adhere to five architectural principles:

- **Dual-Manifest Packaging**: Plugins ship a root Agent Plugins v1 manifest (`plugin.json`) alongside runtime-specific catalogs (such as Anthropic Claude marketplace manifests) [^evt-community-events-pr-54].
- **Standardized Directory and Path Placeholders**: Runtime-specific environment variables (such as `${CLAUDE_SKILL_DIR}`) are replaced with client-neutral `<skill-root>` placeholders within documentation, scripts, and invocation examples [^evt-community-events-file-799e4722911d-3d7dbf62] [^evt-community-events-pr-54].
- **Namespaced Metadata for UI Hints**: Runtime-specific features such as command line argument hints are decoupled from base frontmatter and isolated under namespaced `metadata` blocks, ensuring runtime validation does not fail on unrecognized root properties [^evt-community-events-pr-54].
- **Contract and Workflow Separation**: Operational procedures are decoupled into two distinct documents: a clean `SKILL.md` declaring interface metadata, tools, and constraints, and an auxiliary `WORKFLOW.md` specifying step-by-step execution procedures [^evt-community-events-pr-54].
- **Automated Portability Linting**: Manifest compliance, skill frontmatter compatibility declarations, and the absence of vendor-locked execution syntax are verified programmatically via dedicated CI and pre-commit linting tools (`check_manifests.py`, `check_skill_portability.py`) [^evt-community-events-file-63a9c44a44ac-37822210] [^evt-community-events-pr-54].

# Related Concepts
- [Agent Plugins Standard](../standards/agent-plugins.md)
- [Agent Skills Standard](../standards/agent-skills.md)
- [Community Events Eval Suite](../resources/community-events-eval-suite.md)

[^evt-community-events-file-63a9c44a44ac-37822210]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/.pre-commit-config.yaml
[^evt-community-events-pr-54]: https://github.com/aaif/community-events/pull/54
