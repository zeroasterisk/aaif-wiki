---
type: guideline
title: Agent Plugin Portability Guidelines
description: Packaging, runtime abstraction, credential resolution, and execution
  boundary guidelines ensuring agent skills run consistently across git checkouts
  and installed plugins.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
tags:
- guidelines
- plugins
- portability
- runtime
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T11:01:50.430523+00:00'
sources:
- id: evt-community-events-file-a54ff182c7e8-2d5d5bf6
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview

The Agent Plugin Portability Guidelines specify structural and runtime isolation contracts required for agent skills to operate reliably across varied execution environments, including developer git checkouts and packaged host installations.[^evt-community-events-file-a54ff182c7e8-2d5d5bf6] AI agent runners such as Goose and Claude Desktop install and invoke plugins under disparate filesystem topologies and stripped shell environments, necessitating strict path resolution conventions, credential fallback chains, and scratch directory boundaries.[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]

# Architecture / Specification

## Checkout vs. Installed Plugin Runtimes

Plugin architectures must account for divergence in installation semantics:[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]
- **Host Installations**: Host applications like Claude Desktop install decoupled, versioned directory snapshots lacking `.git` metadata, invoking scripts from the operator's active working directory with an empty shell profile.
- **Relative Path Resolution**: Commands defined in `SKILL.md` files must resolve paths using an explicit `<skill-root>` variable rather than static paths relative to repository roots (e.g., avoiding `skills/<name>/...`).

## Secret and Credential Resolution Chain

Because host applications cannot pass environment variables through user shells into plugin child processes, engines resolve operational secrets via a prioritized three-tier fallback hierarchy:[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]
1. Active process environment variables.
2. Root-level `.env` configuration files.
3. Native operating system secure storage (such as the macOS Keychain), ensuring installed plugins retain access without hardcoded credentials.

## Filesystem and Scratch Isolation

Plugins must never default writes to the process's current working directory (CWD), which often maps to synced personal user folders.[^evt-community-events-file-a54ff182c7e8-2d5d5bf6] Operational state, caches, and backups must target centralized application data directories (e.g. `aaif_events.datadir`) or isolated temporary directories created via `mktemp -d` and cleaned up after execution.[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]

## Public Repository PII Safeguards

Publicly distributed agent plugins operating on real organizational rosters must treat commits as immutable.[^evt-community-events-file-a54ff182c7e8-2d5d5bf6] Automated linting hooks (such as `check_no_real_pii.py`) and synthetic fixture constraints prevent live personal data from entering version control or agent transcripts.[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]

# References

- [AAIF Check Setup Skill](../skills/aaif-check-setup.md)
- [AAIF Backup Skill](../skills/aaif-backup.md)
- [Public Agent Skills Resource](../resources/public-agent-skills.md)

[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
