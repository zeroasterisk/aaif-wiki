---
type: standard
title: AGENTS.md Repository Convention
description: Standardized repository configuration format providing operational constraints,
  runtime execution contexts, and security boundaries to coding agents.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
tags:
- standards
- agent-configuration
- coding-agents
- repository-conventions
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:22:15.933437+00:00'
sources:
- id: evt-community-events-file-a54ff182c7e8-2d5d5bf6
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-ws-taxonomy-landscape-pr-30
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/30
  author: asish-singh
  last_modified: '2026-10-11T18:18:09+00:00'
---

# Overview
The `AGENTS.md` file convention is a standardized repository-level specification that instructs autonomous and interactive coding agents (such as Claude Code) on operational guidelines, security constraints, and execution boundaries[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]. Within the AAIF ecosystem, `AGENTS.md` is tracked under the Conventions & File Formats taxonomy as a member-maintained project convention distinct from wire protocols[^evt-ws-taxonomy-landscape-pr-30].

Coding assistants frequently require clear environmental demarcation between human documentation (`README.md`), skill authoring (`CONTRIBUTING.md`), visual design systems (`DESIGN.md`), and engine maintenance routines (`MAINTAINING.md`)[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]. The convention establishes symlinks (such as `CLAUDE.md`) to maintain backwards compatibility while unifying behavioral policies in a single declarative root artifact[^evt-community-events-file-a54ff182c7e8-2d5d5bf6].

# Architecture / Specification
An `AGENTS.md` configuration enforces several fundamental operational and architectural boundaries[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]:

- **Installed Plugin vs. Checkout Boundary**: Agents must distinguish between local Git checkouts and distributed plugin runtime environments (e.g., [Goose](../resources/goose.md) or Claude Desktop)[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]. Command invocations must target `<skill-root>` variables rather than repository-relative paths (`skills/<name>/...`), ensuring script portability[^evt-community-events-file-a54ff182c7e8-2d5d5bf6].
- **Credential Resolution Precedence**: Operational secrets required by executing scripts follow strict resolution chains: process environment variables, repository-root `.env` files, and platform-native credential storage (such as the macOS Keychain), ensuring installed plugins without shell environments authenticate safely[^evt-community-events-file-a54ff182c7e8-2d5d5bf6].
- **Working Directory and Scratch Data Isolation**: Agents are restricted from writing scratch or runtime outputs directly to the current working directory (`cwd`), which often maps to synced user folders[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]. Outputs must be directed through designated data directories (e.g., `aaif_events.datadir`) or ephemeral scratch spaces generated via `mktemp -d`[^evt-community-events-file-a54ff182c7e8-2d5d5bf6].
- **Personally Identifiable Information (PII) Guardrails**: Because public commits and force-pushes cannot guarantee full eradication on upstream repository hosts, `AGENTS.md` mandates that all test fixtures, logs, and docstrings utilize synthetic data, supported by automated linting scripts like `check_no_real_pii.py`[^evt-community-events-file-a54ff182c7e8-2d5d5bf6].

# Lifecycle History
The convention originated in operational AAIF repositories such as `community-events` to mitigate common agent execution failures, including broken path assumptions and accidental credential or PII disclosure[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]. In the Taxonomy and Landscape workstream, proposals were introduced to formally catalog `AGENTS.md` as an AAIF Member convention alongside runtime control planes and communication protocols[^evt-ws-taxonomy-landscape-pr-30].

[^evt-community-events-file-a54ff182c7e8-2d5d5bf6]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/AGENTS.md
[^evt-ws-taxonomy-landscape-pr-30]: https://github.com/aaif/ws-taxonomy-landscape/pull/30
