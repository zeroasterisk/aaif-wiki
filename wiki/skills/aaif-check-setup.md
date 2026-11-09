---
type: skill
title: AAIF Check Setup
description: Read-only diagnostic skill validating runtime readiness, API connection
  tokens, and per-operator credential configuration across Google Workspace, Slack,
  and Luma.
resource: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/skills/aaif-check-setup/SKILL.md
tags:
- skill
- community-events
- diagnostics
- tooling
- credentials
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:32:01.978591+00:00'
sources:
- id: evt-community-events-file-3422d7005bbb-6740e451
  resource: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/skills/aaif-check-setup/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-11-03T22:44:51-08:00'
- id: evt-community-events-file-953dd2e86174-8ce1fa27
  resource: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/MAINTAINING.md
  author: Rahul Parundekar
  last_modified: '2026-11-03T22:44:51-08:00'
- id: evt-community-events-file-b33563055168-23a10754
  resource: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/README.md
  author: Rahul Parundekar
  last_modified: '2026-11-03T22:44:51-08:00'
- id: evt-community-events-pr-67
  resource: https://github.com/aaif/community-events/pull/67
  author: rparundekar
  last_modified: '2026-11-04T06:47:21+00:00'
---

# Overview
`aaif-check-setup` is a read-only diagnostic skill within the AAIF Community Events Toolkit that verifies local machine readiness before executing administrative operations.[^evt-community-events-file-3422d7005bbb-6740e451] It inspects local Python dependencies, Google Workspace authentication via the `gws` command-line tool, edit permissions on the Community Intake sheet, user-scoped Slack tokens, and Luma calendar API keys.[^evt-community-events-file-3422d7005bbb-6740e451] It explains configuration gaps and actionable remediation steps in plain language without exposing private keys or credentials.[^evt-community-events-file-3422d7005bbb-6740e451]

# Architecture / Specification

## Diagnostic Scope and Checks
The diagnostic runner executes `python3 <skill-root>/scripts/check_setup.py` as a non-destructive probe.[^evt-community-events-file-3422d7005bbb-6740e451] The script performs read-only validations:
- **Google Workspace (`gws` CLI):** Verifies CLI installation, Google OAuth login state, and Drive edit access against Google Sheets metadata without modifying any resources.[^evt-community-events-file-3422d7005bbb-6740e451]
- **Slack:** Invokes `auth.test` against the Slack API using an operator's individual user token (`xoxp-`).[^evt-community-events-file-3422d7005bbb-6740e451][^evt-community-events-file-953dd2e86174-8ce1fa27]
- **Luma:** Validates calendar access permissions by calling the `calendars/get` endpoint.[^evt-community-events-file-3422d7005bbb-6740e451]
- **System Binaries:** Verifies availability of Python 3 and Google Chrome (required for headless PDF report rendering).[^evt-community-events-file-3422d7005bbb-6740e451]

Exit code `0` signals that all required subsystems are functional, while exit code `1` denotes one or more blocking failures.[^evt-community-events-file-3422d7005bbb-6740e451] Text generation and copywriting tasks (e.g., drafting announcements or speaker bios) operate independently and do not require external credentials to function.[^evt-community-events-file-3422d7005bbb-6740e451][^evt-community-events-file-b33563055168-23a10754]

## Tooling Invariants and File Handling
The skill enforces strict tooling conventions for asset interaction:[^evt-community-events-file-3422d7005bbb-6740e451]
1. **API-Driven Google Formats:** Native Google files (`application/vnd.google-apps.*`) must be inspected and edited exclusively via the `gws` CLI driven by Python through native Docs, Sheets, and Slides APIs.[^evt-community-events-file-3422d7005bbb-6740e451]
2. **Byte-Level OOXML Surgery:** Stored Office files (`.docx`, `.pptx`, `.xlsx`) are manipulated via zip-part byte-level editing to preserve embedded fonts and metadata.[^evt-community-events-file-3422d7005bbb-6740e451]
3. **Ban on Desktop Office Suites:** Desktop converters and headless suites such as LibreOffice (`soffice`) and `unoconv` are strictly prohibited due to local font substitution and corruption of unrecognized OOXML namespaces.[^evt-community-events-file-3422d7005bbb-6740e451] Visual previews must be rendered via API endpoints or PDF export pipelines.[^evt-community-events-file-3422d7005bbb-6740e451]

## Credential Isolation Model
AAIF community event tooling mandates per-operator credential creation rather than shared credentials:[^evt-community-events-pr-67]
- **Google OAuth Isolation:** Each operator provisions an independent Google connection configuration because internal OAuth clients cannot authenticate cross-organization accounts.[^evt-community-events-pr-67]
- **Slack User Tokens:** Operators generate dedicated user tokens (`xoxp-`) from an installed Slack application manifest rather than using shared bot tokens or shared operator tokens.[^evt-community-events-pr-67][^evt-community-events-file-953dd2e86174-8ce1fa27] Because user tokens inherit the caller's privileges (including direct message search via `search:read` and impersonated posting via `chat:write`), sharing tokens creates critical security and privacy boundary violations.[^evt-community-events-pr-67][^evt-community-events-file-953dd2e86174-8ce1fa27]
- **Keychain Hygiene:** On macOS, mismatched or corrupted keys require purging `gws-cli` entries from Keychain Access and logging out before reauthenticating with explicit scopes.[^evt-community-events-file-3422d7005bbb-6740e451]

# References
- Portable Agent Skill packaging rules: [Agent Skills specification](../standards/agent-skills.md)[^evt-community-events-file-953dd2e86174-8ce1fa27]
- Operational pipeline: [Community Event Operations](../skills/community-event-operations.md)[^evt-community-events-file-b33563055168-23a10754]

[^evt-community-events-file-3422d7005bbb-6740e451]: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/skills/aaif-check-setup/SKILL.md
[^evt-community-events-file-953dd2e86174-8ce1fa27]: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/MAINTAINING.md
[^evt-community-events-file-b33563055168-23a10754]: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/README.md
[^evt-community-events-pr-67]: https://github.com/aaif/community-events/pull/67
