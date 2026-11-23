---
type: guideline
title: Agent Plugin Portability and Authorization Boundaries
description: Standardized manifest architecture, directory resolution rules, capability
  abstractions, and authorization boundaries ensuring agent plugins run portably across
  heterogeneous runtimes.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/PORTABILITY.md
tags:
- agent-plugins
- agent-skills
- portability
- authorization
- packaging
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:14:34.405060+00:00'
sources:
- id: evt-community-events-file-57c4a0921db3-7bd7bd69
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/PORTABILITY.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
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

The Agent Plugin Portability and Authorization Boundaries guideline specifies conventions for packaging modular [Agent Plugins](../standards/agent-plugins.md) and [Agent Skills](../standards/agent-skills.md) so they execute reliably across heterogeneous host environments—such as Claude Code, Codex, and Cursor—without relying on client-specific path semantics or unvalidated write permissions[^evt-community-events-file-57c4a0921db3-7bd7bd69]. It enforces portable directory resolution, capability-driven instruction design, namespaced metadata retention, and strict runtime authorization gates across external mutations[^evt-community-events-pr-54].

# Architecture / Specification

### Manifest Structure
Portable plugins declare a canonical root `plugin.json` conformant with the Agent Plugins specification[^evt-community-events-file-57c4a0921db3-7bd7bd69]. When targeting clients with proprietary configuration schemas (such as Claude Code), client manifests (e.g., `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`) are maintained in tandem, but the root manifest remains canonical for identity, description, and version metadata[^evt-community-events-file-57c4a0921db3-7bd7bd69]. Overlays (such as `.codex-plugin` or `.cursor-plugin`) are omitted unless client-specific configuration is strictly required[^evt-community-events-file-57c4a0921db3-7bd7bd69].

### Directory Resolution and Capability Abstraction
All resource references inside a `SKILL.md` or its companion files must be relative to the directory containing that `SKILL.md`[^evt-community-events-file-57c4a0921db3-7bd7bd69]. Portable skills replace platform-specific environment variables (such as `${CLAUDE_SKILL_DIR}`) with the `<skill-root>` placeholder, which the agent harness resolves at runtime from the skill's loaded location rather than passing it literally to a shell[^evt-community-events-file-57c4a0921db3-7bd7bd69][^evt-community-events-pr-54].

Skills define tool dependencies using vendor-neutral capability descriptions rather than vendor-specific tool names[^evt-community-events-file-57c4a0921db3-7bd7bd69]:
- **Read bundled files**: Access skill-packaged references or templates; missing resources halt execution[^evt-community-events-file-57c4a0921db3-7bd7bd69].
- **Run Python and subprocesses**: Execute deterministic helper scripts rather than generating ad hoc mutating shell code[^evt-community-events-file-57c4a0921db3-7bd7bd69].
- **Read web pages**: Fetch external public state or fallback to manual prompts[^evt-community-events-file-57c4a0921db3-7bd7bd69].
- **Show local files**: Output local paths and instructions for user inspection[^evt-community-events-file-57c4a0921db3-7bd7bd69].
- **Request user approval**: Pause workflow execution before crossing write boundaries[^evt-community-events-file-57c4a0921db3-7bd7bd69].

### Frontmatter and Metadata Compatibility
The portable Agent Skills schema disallows non-standard autocomplete keys in top-level frontmatter; client-specific features (such as `argument-hint`) must be nested under namespaced `metadata` so catalog parsers can extract them without triggering schema validation failures on standard runtimes[^evt-community-events-file-57c4a0921db3-7bd7bd69][^evt-community-events-pr-54].

### Authorization Boundaries and Safety Invariants
Invoking or loading an agent skill does not grant authorization to execute mutations[^evt-community-events-file-57c4a0921db3-7bd7bd69]. Implementations follow the [human approval gate](../patterns/human-approval-gate.md) pattern:
- **Plan-by-default**: Default runs are strictly read-only and print a diff or plan[^evt-community-events-file-57c4a0921db3-7bd7bd69].
- **Explicit mutation flags**: Destructive actions require deliberate command-line flags (`--write`, `--apply`, `--create`)[^evt-community-events-file-57c4a0921db3-7bd7bd69].
- **Attestation flags**: Flags certifying approval (`--i-have-approval`) must reflect actual human sign-off and must never be injected by an agent autonomously[^evt-community-events-file-57c4a0921db3-7bd7bd69].
- **Credential containment**: Secrets must never be supplied via command-line arguments or prompts; credentials reside exclusively in environment variables, `.env` files, or OS keychains[^evt-community-events-file-57c4a0921db3-7bd7bd69][^evt-community-events-file-63a9c44a44ac-37822210].

# Lifecycle History

- **2026-03**: Established through PR #54 in `aaif/community-events`, migrating 23 operational skills from Claude-specific path conventions to the unified Agent Plugins v1 and Agent Skills portable packaging specification[^evt-community-events-pr-54].

[^evt-community-events-file-57c4a0921db3-7bd7bd69]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/PORTABILITY.md
[^evt-community-events-file-63a9c44a44ac-37822210]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/.pre-commit-config.yaml
[^evt-community-events-pr-54]: https://github.com/aaif/community-events/pull/54
