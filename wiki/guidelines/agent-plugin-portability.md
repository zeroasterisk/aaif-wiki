---
type: guideline
title: Agent Plugin Portability and Execution Isolation Guidelines
description: Architectural guidelines and directory resolution rules ensuring agent
  skills run reliably across checkouts and headless plugin host environments.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
tags:
- plugins
- portability
- runtime
- skills
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:33:25.457551+00:00'
sources:
- id: evt-community-events-file-a54ff182c7e8-2d5d5bf6
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview
Agent skills and toolchains must operate reliably across diverse host execution topologies without assuming a full git checkout, a persistent shell environment, or an immutable current working directory [^evt-community-events-file-a54ff182c7e8-2d5d5bf6]. In the Agentic AI Foundation reference implementation, runtime hosts such as Goose perform git checkouts while hosts such as Claude Desktop provision isolated, versioned directory trees devoid of git metadata [^evt-community-events-file-a54ff182c7e8-2d5d5bf6].

# Architecture / Specification
The portability model resolves operational disparities through standardized path variables, tiered credential discovery, and isolated data containment:

- **Root-Relative Path Resolution**: Skill invocation commands in `SKILL.md` must prefix script paths with `<skill-root>` rather than assuming relative workspace roots like `skills/<name>/...` [^evt-community-events-file-a54ff182c7e8-2d5d5bf6]. This invariant prevents path traversal failures when an agent executes commands from arbitrary session directories. Conformance is verified statically by `check_skill_portability.py` [^evt-community-events-file-a54ff182c7e8-2d5d5bf6].
- **Tiered Secret Resolution**: Headless plugin hosts frequently launch subshells without inherited terminal environment variables. Credential lookups systematically fall back from the active process environment to the repo-root `.env` file, and finally to the host operating system keyring (such as macOS Keychain), ensuring installed plugins maintain connectivity without hardcoded tokens [^evt-community-events-file-a54ff182c7e8-2d5d5bf6].
- **Isolated Scratch and Data Directories**: Plugin executions must never emit unmanaged scratch files or persistent state into the caller's working directory, which often coincides with synced user folders [^evt-community-events-file-a54ff182c7e8-2d5d5bf6]. Runtime mutations must route through dedicated data storage routines (such as `aaif_events.datadir`) or ephemeral temporary directories via `mktemp -d` [^evt-community-events-file-a54ff182c7e8-2d5d5bf6].
- **Drift Protection for Decoupled Copies**: Standalone utility scripts that duplicate core storage or secret-lookup logic without shared libraries must be tracked in unit testing (`tests/test_pinned_copies.py`) to prevent behavioral divergence [^evt-community-events-file-a54ff182c7e8-2d5d5bf6].

# Lifecycle History
Portability testing established that eleven skills initially broke when executed outside the repository root [^evt-community-events-file-a54ff182c7e8-2d5d5bf6]. Static validation checks and pinned-copy verification suites were introduced to enforce runtime independence across Claude Desktop and Goose plugin environments [^evt-community-events-file-a54ff182c7e8-2d5d5bf6].

# References
- [Community Event Operations](../skills/community-event-operations.md)
- [AAIF Check Setup](../skills/aaif-check-setup.md)
- [AAIF Backup](../skills/aaif-backup.md)

[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
