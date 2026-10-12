---
type: guideline
title: Agent Plugin Portability Guidelines
description: Architectural specifications for packaging multi-client agent plugins,
  path token resolutions, external persistent data directories, and out-of-band secret
  management.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-event/SKILL.md
tags:
- guidelines
- plugins
- portability
- standards
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:50:35.583468+00:00'
sources:
- id: evt-community-events-file-4c2672b57ca1-5e9465e1
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-event/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-8b30d97e0275-3e6d8b8d
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-audit-slack/references/caches-and-composition.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-953dd2e86174-aa074a1c
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/MAINTAINING.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-a54ff182c7e8-2d5d5bf6
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview

Agent Plugin Portability guidelines establish architectural conventions allowing AI agent plugins and skills to execute predictably across diverse host applications, including [Goose](../resources/goose.md), Claude Desktop, Claude Code, Cursor, and Codex[^evt-community-events-file-953dd2e86174-aa074a1c][^evt-community-events-file-a54ff182c7e8-2d5d5bf6]. By decoupling script execution from working directory assumptions, standardizing path resolution tokens, isolating persistent state, and externalizing credentials, plugins achieve runtime compatibility regardless of whether they are run from a local git repository checkout or installed into version-isolated application containers[^evt-community-events-file-953dd2e86174-aa074a1c][^evt-community-events-file-a54ff182c7e8-2d5d5bf6].

# Architecture / Specification

## Path Token Resolution

Installed plugins operate in environments where host clients manage execution contexts differently—Goose clones git repositories directly, whereas tools like Claude Desktop unpack repository archives into version-specific directories stripped of `.git` metadata[^evt-community-events-file-953dd2e86174-aa074a1c][^evt-community-events-file-a54ff182c7e8-2d5d5bf6]. Consequently:

- Skill instructions in `SKILL.md` must resolve script locations via a dynamic `<skill-root>` token resolved from the loaded skill directory rather than relative paths from an assumed repository root (e.g. `skills/<name>/...`)[^evt-community-events-file-4c2672b57ca1-5e9465e1][^evt-community-events-file-a54ff182c7e8-2d5d5bf6].
- CI validation harnesses must enforce that all referenced script paths use `<skill-root>` to prevent silent failures when executed by desktop runtimes[^evt-community-events-file-a54ff182c7e8-2d5d5bf6].

## Persistent State and Data Directories

Plugins must never store persistent state, caches, backups, or generated reports in the plugin installation directory or the user's current working directory (`cwd`)[^evt-community-events-file-953dd2e86174-aa074a1c][^evt-community-events-file-a54ff182c7e8-2d5d5bf6]:

- **Ephemeral Install Trees**: Automatic updates replace the plugin install directory entirely, orphaning any state or backups stored within it[^evt-community-events-file-953dd2e86174-aa074a1c].
- **Host Working Directories**: Desktop clients frequently run from personal or synchronized user directories that must not be polluted with scratch files[^evt-community-events-file-a54ff182c7e8-2d5d5bf6].
- **Central Data Directory**: Persistent state must route through a dedicated datadir utility (such as `aaif_events.datadir`), resolving to standard operating system application support folders (e.g., `~/Library/Application Support/AAIF` on macOS, or `$XDG_DATA_HOME` on Linux), overridable by an absolute `AAIF_DATA_DIR` environment variable[^evt-community-events-file-953dd2e86174-aa074a1c]. Temporary files must use system scratch directories (`mktemp -d`)[^evt-community-events-file-a54ff182c7e8-2d5d5bf6].

## Dual Manifest Structure

To bridge diverging client packaging specifications:

- The root directory hosts standard `plugin.json` adhering to the open Agent Plugin standard[^evt-community-events-file-953dd2e86174-aa074a1c].
- Client-specific manifests, such as Claude Desktop and Claude Code configurations, reside in dedicated subdirectories (e.g., `.claude-plugin/`), allowing multi-client support from a single upstream codebase[^evt-community-events-file-953dd2e86174-aa074a1c].
- Individual capabilities are encapsulated in [Agent Skills](../standards/agent-skills.md) subdirectories with standard YAML frontmatter[^evt-community-events-file-4c2672b57ca1-5e9465e1][^evt-community-events-file-953dd2e86174-aa074a1c].

## Out-of-Band Secret Sourcing

Desktop assistant applications do not propagate interactive shell environments to plugin subprocesses[^evt-community-events-file-953dd2e86174-aa074a1c]. To maintain credential hygiene without requiring users to expose API keys inside conversational transcripts:

- Sensitive secrets (such as Slack tokens and calendar API keys) must be resolved hierarchically: first from process environment variables, second from a repository-level `.env` file, and third from the OS keychain (e.g. macOS Keychain Access under named items)[^evt-community-events-file-4c2672b57ca1-5e9465e1][^evt-community-events-file-953dd2e86174-aa074a1c][^evt-community-events-file-a54ff182c7e8-2d5d5bf6].
- Setup verification skills (`aaif-check-setup`) confirm keychain accessibility prior to executing operations[^evt-community-events-file-4c2672b57ca1-5e9465e1][^evt-community-events-file-953dd2e86174-aa074a1c].

[^evt-community-events-file-4c2672b57ca1-5e9465e1]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-event/SKILL.md
[^evt-community-events-file-953dd2e86174-aa074a1c]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/MAINTAINING.md
[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
