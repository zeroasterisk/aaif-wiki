---
type: skill
title: AAIF Check Setup Skill
description: Read-only pre-flight diagnostic skill auditing Google Workspace authentication,
  credential resolution order, and runtime dependencies.
resource: https://github.com/aaif/community-events/pull/60
tags:
- skills
- operations
- diagnostics
- authentication
- tooling
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:22:52.144306+00:00'
sources:
- id: evt-community-events-pr-60
  resource: https://github.com/aaif/community-events/pull/60
  author: rparundekar
  last_modified: '2026-10-11T15:58:20+00:00'
- id: evt-community-events-file-953dd2e86174-aa074a1c
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/MAINTAINING.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview

The `aaif-check-setup` skill provides a plain-language diagnostic readiness check for operators running the AAIF Community Events Toolkit across client environments such as [Goose](../resources/goose.md), Claude Desktop, Claude Code, and standalone checkouts[^evt-community-events-pr-60]. It inspects runtime dependencies, validates binary accessibility, tests Google Workspace authentication, and verifies credential availability across multiple storage backends[^evt-community-events-pr-60][^evt-community-events-file-953dd2e86174-aa074a1c].

# Architecture / Specification

## Diagnostic Verification Engine

When invoked by the operator ("check my setup"), the skill audits each component required for operational workflows and outputs actionable remediation instructions rather than silent failures[^evt-community-events-pr-60]:
- **CLI Visibility:** Verifies that the Google Workspace CLI (`gws`) binary is installed and executable in the assistant application's shell context[^evt-community-events-file-953dd2e86174-aa074a1c].
- **OAuth Scopes and Sign-in:** Validates `gws` OAuth authorization; if expired or unauthenticated, it generates the exact scoped login command rather than permitting an unconstrained `gws auth login`[^evt-community-events-file-953dd2e86174-aa074a1c].
- **Credential Chain Verification:** Verifies read and write permissions for external services using the standardized credential resolution hierarchy[^evt-community-events-pr-60].

## Secret Lookup Resolution

The skill and underlying toolkit engines inspect secrets using a strict priority order cached per execution run[^evt-community-events-pr-60]:
1. Process environment variables[^evt-community-events-pr-60].
2. Repository-root `.env` file (when operating inside a git checkout)[^evt-community-events-pr-60].
3. Local operating system secure store (macOS Keychain entries `aaif-slack-write-token`, `aaif-slack-read-token`, and `luma-api-key` under account `aaif`)[^evt-community-events-file-953dd2e86174-aa074a1c].

This multi-tier discovery enables non-technical users to retain secrets across automated agent plugin updates where shell environments are not propagated by the client host[^evt-community-events-file-953dd2e86174-aa074a1c].

# Lifecycle History

- Introduced in PR #60 to support non-technical operators and standalone plugin installations in desktop agent clients[^evt-community-events-pr-60].

[^evt-community-events-file-953dd2e86174-aa074a1c]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/MAINTAINING.md
[^evt-community-events-pr-60]: https://github.com/aaif/community-events/pull/60
