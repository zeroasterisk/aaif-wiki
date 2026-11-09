---
type: guideline
title: Agent Plugin Portability Guidelines
description: Packaging conventions, capability abstractions, and authorization boundaries
  ensuring portable agent plugin execution across diverse host harnesses.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/PORTABILITY.md
tags:
- plugins
- portability
- standards
- manifest
- authorization
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:11:44.946840+00:00'
sources:
- id: evt-community-events-file-57c4a0921db3-7bd7bd69
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/PORTABILITY.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
---

# Overview
The Agent Plugin Portability Guidelines establish packaging conventions, capability abstractions, and runtime authorization boundaries ensuring agent plugins operate consistently across diverse client environments such as Codex, Cursor, and Claude Code.[^evt-community-events-file-57c4a0921db3-7bd7bd69] The guidelines ensure skill authors maintain vendor-neutral interoperability while respecting human-in-the-loop governance.[^evt-community-events-file-57c4a0921db3-7bd7bd69]

# Architecture / Specification
Portable plugins comply with standard manifest declarations, relative path resolutions, and capability-oriented instructions:[^evt-community-events-file-57c4a0921db3-7bd7bd69]
- **Unified Manifest Structure**: The root `plugin.json` acts as the canonical manifest for shared identity and version metadata across compliant clients, avoiding redundant client-specific config directories when no specialized overlays are required.[^evt-community-events-file-57c4a0921db3-7bd7bd69]
- **Relative Skill Resolution**: Skill paths within `SKILL.md` files must be relative to the containing skill directory, utilizing `<skill-root>` as a dynamically resolved runtime placeholder rather than an environment variable.[^evt-community-events-file-57c4a0921db3-7bd7bd69]
- **Capability Abstractions**: Skill instructions must specify functional capabilities (e.g., read bundled files, run subprocesses, inspect web pages, display local files, request human approval) rather than hardcoded client tool primitives.[^evt-community-events-file-57c4a0921db3-7bd7bd69]
- **Authorization Boundaries**: Loading or invoking a skill does not authorize state mutations. Mutating actions require explicit command-line gates (e.g., `--write`, `--apply`, `--create`) preceded by human review.[^evt-community-events-file-57c4a0921db3-7bd7bd69] Gating flags such as `--i-have-approval` must represent genuine human consent and must never be supplied by an agent autonomously.[^evt-community-events-file-57c4a0921db3-7bd7bd69]
- **Credential Handling**: Secrets must be injected via runtime environment variables or platform keychains, never passed within prompts, arguments, or tracked files.[^evt-community-events-file-57c4a0921db3-7bd7bd69]

# Lifecycle History
Maintained in alignment with the Agent Plugins standard ([`../standards/agent-plugins.md`](../standards/agent-plugins.md)) and refined through reference implementations in AAIF operational repositories.[^evt-community-events-file-57c4a0921db3-7bd7bd69]

[^evt-community-events-file-57c4a0921db3-7bd7bd69]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/PORTABILITY.md
