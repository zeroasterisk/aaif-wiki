---
type: skill
title: Community Event Operations Skill Suite
description: Operational agent skill suite and execution engines automating AAIF chapter
  intake, diagnostic setup verification, event synchronization, and reporting across
  local checkouts and installed agent runtimes.
resource: https://github.com/aaif/community-events/pull/60
tags:
- community
- operations
- skills
- automation
- tooling
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
The Community Event Operations skill suite provides automated execution engines and procedural workflows for managing Agentic AI Foundation (AAIF) local chapters, community events, and ecosystem communications.[^evt-community-events-pr-60] Packaged as modular agent skills adhering to the `agent-skills` format, the suite automates chapter provisioning, attendee and intake triage, event synchronization across Google Workspace and Luma, and monthly chapter updates.[^evt-community-events-pr-60]

The suite is engineered to execute both from source repository checkouts and as an installed plugin within agent runtimes like [Goose](../resources/goose.md) and Claude Desktop without requiring a shell environment or local git repository.[^evt-community-events-pr-60]

# Architecture / Specification

## Installed Plugin Runtime Architecture
The operational suite isolates execution paths to support running inside containerized, cached, or `.git`-less agent plugin installations:[^evt-community-events-pr-60]
- **Isolated Data Storage**: Runtime writes, synchronizations, caches, and backups are routed away from the current working directory (`cwd`) to a dedicated user application directory (e.g., `~/Library/Application Support/AAIF`), preventing workspace contamination during operator execution.[^evt-community-events-pr-60]
- **Credential Resolution Chain**: Secret resolution follows a deterministic hierarchy across execution contexts: process environment variables first, local `.env` files within the repository root second, and OS-native secret storage (such as the macOS keychain) third, with per-run caching.[^evt-community-events-pr-60]
- **Portability Guards**: Engine instructions address dependencies using relative `<skill-root>` conventions instead of fixed repository paths or shell variable overrides like `PYTHONPATH`.[^evt-community-events-pr-60]

## Setup and Readiness Engine (`aaif-check-setup`)
The suite includes the `aaif-check-setup` diagnostic engine, providing plain-language readiness evaluations for operators.[^evt-community-events-pr-60] The tool verifies:
1. Availability and accessibility of required credentials (e.g., Slack, Google Workspace, Luma tokens).
2. Distinction between missing credentials and OS keychain access refusals.
3. Guided remediation providing scoped sign-in commands for missing or misconfigured integrations.[^evt-community-events-pr-60]

## Execution Engines and Synchronization
Core scripts include `sync.py`, digest engines, and tracker fetch tools designed to gracefully handle partial network failures, ensure restrictive folder permissions (`0700` for backups), and clean up partial downloads during failure modes.[^evt-community-events-pr-60]

# Lifecycle History
Originally developed as repository-bound automation scripts, the community event operations suite underwent extensive refactoring in PR #60 to support non-technical operators executing through desktop agent harnesses like Goose and Claude Desktop, eliminating assumptions about shell paths, git presence, and working directory ownership.[^evt-community-events-pr-60]

# References
- Goose Agent Framework: [../resources/goose.md](../resources/goose.md)
- Agent Plugin Portability Guidelines: [../guidelines/agent-plugin-portability.md](../guidelines/agent-plugin-portability.md)
- Community Events Evaluation Suite: [../resources/community-events-eval-suite.md](../resources/community-events-eval-suite.md)

[^evt-community-events-pr-60]: https://github.com/aaif/community-events/pull/60
