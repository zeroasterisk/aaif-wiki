---
type: skill
title: AAIF Setup Diagnostics Skill
description: Read-only pre-flight diagnostics skill verifying Python runtime, Google
  Workspace authentication, credentials, and external service access for community
  operations.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/README.md
tags:
- aaif
- skills
- diagnostics
- google-workspace
- slack
- luma
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:55:55.482485+00:00'
sources:
- id: evt-community-events-file-b33563055168-f722dd04
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/README.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:20:05-07:00'
- id: evt-community-events-file-06572a96a58d-9d2d11f7
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/CHANGELOG.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-3422d7005bbb-fcddfd77
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-check-setup/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview
The `aaif-check-setup` skill provides automated, read-only environment and dependency verification for operators running the AAIF Community Events Toolkit[^evt-community-events-file-3422d7005bbb-fcddfd77]. It validates that an operator's local environment possesses required runtimes, command-line interfaces, service authentication tokens, and API credentials across Google Workspace, Slack, and Luma without modifying system state or exposing secret tokens[^evt-community-events-file-3422d7005bbb-fcddfd77].

# Architecture / Specification
The skill executes a deterministic verification script (`scripts/check_setup.py`) designed to return clear status indicators and remediation guidance for non-technical users[^evt-community-events-file-3422d7005bbb-fcddfd77]:
- **Runtime and Package Structure:** Asserts the presence of Python 3 and identifies whether execution occurs within an unpacked standalone skill archive or a complete repository checkout[^evt-community-events-file-3422d7005bbb-fcddfd77].
- **Google Workspace CLI (`gws`):** Evaluates `gws` command availability, active OAuth credentials, and Google Drive API scopes, preventing failures caused by default scopes omitting Drive permissions[^evt-community-events-file-3422d7005bbb-fcddfd77].
- **Spreadsheet Access:** Validates edit permissions on the AAIF Community Intake sheet by inspecting sheet metadata[^evt-community-events-file-3422d7005bbb-fcddfd77].
- **Credential Resolution Hierarchy:** Verifies access tokens via an established resolution chain: process environment variables, repository `.env` files, and the macOS system keychain (`aaif-slack-read-token`, `aaif-slack-write-token`, and `luma-api-key`)[^evt-community-events-file-06572a96a58d-9d2d11f7].
- **Headless Document Rendering:** Confirms the availability of Google Chrome to support automated HTML-to-PDF export pipelines[^evt-community-events-file-3422d7005bbb-fcddfd77].
- **Decoupled Operation:** Adheres to a fault-tolerant design where offline drafting skills (such as announcement posts or speaker biographies) remain functional even if external API connectivity checks fail[^evt-community-events-file-b33563055168-f722dd04][^evt-community-events-file-3422d7005bbb-fcddfd77].

# Lifecycle History
Introduced in the AAIF Community Events Toolkit to provide self-service setup validation and plain-English troubleshooting for non-technical community volunteers running agent assistants such as Goose and Claude Desktop[^evt-community-events-file-b33563055168-f722dd04][^evt-community-events-file-06572a96a58d-9d2d11f7].

[^evt-community-events-file-06572a96a58d-9d2d11f7]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/CHANGELOG.md
[^evt-community-events-file-3422d7005bbb-fcddfd77]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-check-setup/SKILL.md
[^evt-community-events-file-b33563055168-f722dd04]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/README.md
