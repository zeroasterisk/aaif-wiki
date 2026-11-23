---
type: skill
title: AAIF Check Setup Skill
description: Diagnostic agent skill validating local dependencies, Google Workspace
  connection files, Slack user tokens, and Luma credentials across CLI and plugin
  environments.
resource: https://github.com/aaif/community-events/pull/66
tags:
- skill
- community
- operations
- diagnostics
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:34:28.287156+00:00'
sources:
- id: evt-community-events-pr-66
  resource: https://github.com/aaif/community-events/pull/66
  author: rparundekar
  last_modified: '2026-11-04T06:24:30+00:00'
- id: evt-community-events-file-06572a96a58d-8cb799a7
  resource: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/CHANGELOG.md
  author: Rahul Parundekar
  last_modified: '2026-11-03T22:34:13-08:00'
- id: evt-community-events-file-a54ff182c7e8-b01e6de9
  resource: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/AGENTS.md
  author: Rahul Parundekar
  last_modified: '2026-11-03T22:34:13-08:00'
- id: evt-community-events-file-953dd2e86174-8ce1fa27
  resource: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/MAINTAINING.md
  author: Rahul Parundekar
  last_modified: '2026-11-03T22:44:51-08:00'
---

# Overview
The `aaif-check-setup` skill is a standalone diagnostic utility within the AAIF Community Events Toolkit that executes read-only preflight verification across local software runtimes, API access keys, and cloud service credentials[^evt-community-events-file-06572a96a58d-8cb799a7]. It provides actionable remediation advice when prerequisites are absent, guiding non-technical operators through setup without relying on an external administrative helper[^evt-community-events-pr-66].

# Architecture / Specification
The skill executes strictly using Python standard library modules to ensure portability when packaged as a standalone archive or deployed inside containerized and desktop agent harnesses like Goose and Claude Desktop[^evt-community-events-file-06572a96a58d-8cb799a7].

## Verification Scope
The diagnostic workflow evaluates prerequisites sequentially, surfacing binary pass/fail indicators and plain-text remediation instructions[^evt-community-events-file-06572a96a58d-8cb799a7]:
- **Runtime Environment:** Confirms Python availability, required packaging structure, and headless Google Chrome installation for browser automation tasks[^evt-community-events-file-06572a96a58d-8cb799a7].
- **Google Workspace (`gws`):** Validates the presence of the operator's Google connection configuration file and verifies active edit permissions on the central Community Intake Ops spreadsheet, surfacing missing configuration files rather than prompting invalid interactive logins[^evt-community-events-pr-66][^evt-community-events-file-06572a96a58d-8cb799a7].
- **Slack User Credentials:** Confirms availability of an authorized Slack user token (`xoxp-`) possessing directory read and channel provisioning permissions[^evt-community-events-file-953dd2e86174-8ce1fa27].
- **Luma API Access:** Checks connectivity and authorization against the community event calendar API[^evt-community-events-file-06572a96a58d-8cb799a7].

## Credential Resolution Precedence
To support unprivileged installed plugin runtimes that lack inherited shell environments, credential resolution follows a pinned fallback order[^evt-community-events-file-a54ff182c7e8-b01e6de9]:
1. Explicit process environment variables.
2. Repository root `.env` configuration files.
3. macOS Keychain entries (`aaif-slack-read-token`, `aaif-slack-write-token`, and `luma-api-key`), with per-run caching to mitigate interactive operating system authorization prompts[^evt-community-events-file-06572a96a58d-8cb799a7].

# Lifecycle History
Originally conceived as an administrative helper-assisted check, `aaif-check-setup` was updated to support independent operator self-service, eliminating references to an external setup assistant and adapting error reporting to account for distinct first-time administrator versus subsequent operator provisioning pathways[^evt-community-events-pr-66][^evt-community-events-file-953dd2e86174-8ce1fa27].

# References
- [Community Event Operations](community-event-operations.md)
- [Agent Plugins Standard](../standards/agent-plugins.md)

[^evt-community-events-file-06572a96a58d-8cb799a7]: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/CHANGELOG.md
[^evt-community-events-file-953dd2e86174-8ce1fa27]: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/MAINTAINING.md
[^evt-community-events-file-a54ff182c7e8-b01e6de9]: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/AGENTS.md
[^evt-community-events-pr-66]: https://github.com/aaif/community-events/pull/66
