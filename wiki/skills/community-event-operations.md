---
type: skill
title: Community Event Operations Toolkit
description: Procedural operations pipeline and runtime infrastructure managing chapter
  provisioning, credentials resolution, and data directory isolation.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/MAINTAINING.md
tags:
- skills
- operations
- runtime
- plugins
- portability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:22:52.144306+00:00'
sources:
- id: evt-community-events-file-953dd2e86174-aa074a1c
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/MAINTAINING.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-pr-60
  resource: https://github.com/aaif/community-events/pull/60
  author: rparundekar
  last_modified: '2026-10-11T15:58:20+00:00'
---

# Overview

The Community Event Operations Toolkit provides runtime infrastructure, data hygiene, and procedural automation for managing AAIF community chapters, event scheduling, and organizer directories[^evt-community-events-file-953dd2e86174-aa074a1c]. Packaged as a portable [Agent Plugin](../standards/agent-plugins.md) leveraging [Agent Skills](../standards/agent-skills.md), the toolkit operates consistently across [Goose](../resources/goose.md), Claude Desktop, Claude Code, Codex, and Cursor[^evt-community-events-file-953dd2e86174-aa074a1c].

# Architecture / Specification

## Multi-Client Packaging

The toolkit exposes two integration manifests to maximize client portability[^evt-community-events-file-953dd2e86174-aa074a1c]:
- A root `plugin.json` adhering to cross-client Agent Plugin standards[^evt-community-events-file-953dd2e86174-aa074a1c].
- A `.claude-plugin/` directory providing backwards compatibility with Anthropic Claude marketplaces[^evt-community-events-file-953dd2e86174-aa074a1c].

Individual operations are structured as modular skills under `skills/aaif-*`, each loaded through progressive disclosure rules and relative `<skill-root>` path execution to prevent path breakage in isolated cache environments[^evt-community-events-pr-60].

## Data Directory Isolation

To decouple state and audit artifacts from the active working directory or ephemeral plugin cache clones, the engine routes file outputs through `aaif_events.datadir`[^evt-community-events-pr-60]:
- **Repository Checkout Mode:** Writes reports (`sync-reports/`), backups, and JSON outputs directly to the repository root[^evt-community-events-file-953dd2e86174-aa074a1c].
- **Installed Plugin Mode:** Diverts state files and backups to `~/Library/Application Support/AAIF` on macOS (or XDG data homes on Linux), ensuring that automatic plugin version updates do not orphan local backup snapshots or overwrite user files[^evt-community-events-file-953dd2e86174-aa074a1c].
- **Override Control:** Accepts an absolute path via `AAIF_DATA_DIR` while rejecting relative values to safeguard execution integrity[^evt-community-events-file-953dd2e86174-aa074a1c][^evt-community-events-pr-60].

## Operational Pipelines

The operational suite pairs diagnostics ([`aaif-check-setup`](../skills/aaif-check-setup.md)) with chapter estate management ([`aaif-create-chapter`](../skills/aaif-create-chapter.md)), backup snapshots, and CRM synchronization, enforcing strict data normalization and proposal-execution boundaries across all administrative actions[^evt-community-events-file-953dd2e86174-aa074a1c].

# Lifecycle History

- Expanded via PR #60 to support non-technical operator execution inside desktop agent environments without local git checkouts or pre-configured shell environments[^evt-community-events-pr-60].

[^evt-community-events-file-953dd2e86174-aa074a1c]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/MAINTAINING.md
[^evt-community-events-pr-60]: https://github.com/aaif/community-events/pull/60
