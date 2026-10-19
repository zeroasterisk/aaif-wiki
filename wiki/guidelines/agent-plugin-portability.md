---
type: guideline
title: Agent Plugin Portability Guidelines
description: Packaging, runtime isolation, and execution guidelines ensuring agent
  skills and tool plugins run predictably across checkout-free runtimes, desktop harnesses,
  and varied operating environments.
resource: https://github.com/aaif/community-events/pull/60
tags:
- guidelines
- packaging
- skills
- portability
- standards
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:09:50.927503+00:00'
sources:
- id: evt-community-events-pr-60
  resource: https://github.com/aaif/community-events/pull/60
  author: rparundekar
  last_modified: '2026-10-11T15:58:20+00:00'
---

# Overview
The Agent Plugin Portability Guidelines specify architectural and procedural standards for authoring agent skills and tool plugins that operate reliably across diverse host environments, including local development checkouts, packaged plugin caches, and desktop agent runtimes such as [Goose](../resources/goose.md) and Claude Desktop.[^evt-community-events-pr-60]

When agents install plugins into runtime-managed caches, operational environments diverge significantly from conventional developer checkouts: shell environments may be absent, `.git` metadata is stripped, and the active working directory belongs to the operator rather than the plugin.[^evt-community-events-pr-60] These guidelines define constraints to prevent path breakage, workspace pollution, and credential discovery failures.[^evt-community-events-pr-60]

# Architecture / Specification

## Directory Isolation and Output Handling
Portable agent plugins must strictly separate runtime data generation from the operator's current working directory (`cwd`):[^evt-community-events-pr-60]
- **Target Data Directories**: Plugins must resolve data output, local cache files, reports, and state backups to standard OS application support directories (such as `~/Library/Application Support/<ORGANIZATION>` on macOS or `$XDG_DATA_HOME` on Linux) rather than `cwd` or assumptions of a repository root.[^evt-community-events-pr-60]
- **File System Cleanliness**: Workspaces must remain untouched unless an action explicitly instructs the agent to create user-facing files in `cwd`.[^evt-community-events-pr-60]
- **Defensive Cleanup**: Intermediate failed syncs and partial downloads must be purged immediately to avoid corrupting subsequent executions.[^evt-community-events-pr-60]

## Credential Resolution Hierarchy
To accommodate desktop and headless agents lacking interactive shells, secret retrieval must follow a deterministic, layered fallback order:[^evt-community-events-pr-60]
1. Host process environment variables.
2. Plugin or repository-level `.env` files.
3. Platform-native credential stores (e.g., macOS Keychain, secret service APIs).

Implementations must distinguish between missing keys and system authorization refusals, guiding the user with scoped remediation instructions rather than failing silently.[^evt-community-events-pr-60]

## Path Resolution and Script Invocations
Skill definitions (`SKILL.md`) and operational wrappers must not assume shell environment configuration:
- Prohibit hardcoded repository root paths, fixed `/tmp` mounts, or dependencies on `PYTHONPATH` manipulation.[^evt-community-events-pr-60]
- Reference intra-plugin resources using relative `<skill-root>` tokens that resolve dynamically regardless of whether the skill resides in a git repository or a flat directory cache.[^evt-community-events-pr-60]
- Ensure underlying execution scripts do not fail when `.git` directories or git binary tools are absent from the runtime host.[^evt-community-events-pr-60]

## Readiness and Verification Diagnostics
Portable plugins should expose self-contained setup verification commands (such as a plain-language diagnostic check) that assess prerequisite credentials, tool access, and network reachability before executing multi-step autonomous tasks.[^evt-community-events-pr-60]

# References
- Community Event Operations Suite: [../skills/community-event-operations.md](../skills/community-event-operations.md)
- Agent Skills Packaging Specification: [../standards/agent-skills.md](../standards/agent-skills.md)
- Goose Framework: [../resources/goose.md](../resources/goose.md)

[^evt-community-events-pr-60]: https://github.com/aaif/community-events/pull/60
