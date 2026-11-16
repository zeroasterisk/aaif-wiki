---
type: skill
title: aaif-check-setup
description: Diagnostic agent skill validating local runtime dependencies, Google
  Workspace credentials, Slack and Luma authentication, and guiding credential remediation
  without leaking secrets.
resource: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/skills/aaif-check-setup/SKILL.md
tags:
- aaif
- skills
- diagnostics
- environment
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:41:21.780611+00:00'
sources:
- id: evt-community-events-file-3422d7005bbb-6740e451
  resource: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/skills/aaif-check-setup/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-11-03T22:44:51-08:00'
- id: evt-community-events-pr-67
  resource: https://github.com/aaif/community-events/pull/67
  author: rparundekar
  last_modified: '2026-11-04T06:47:21+00:00'
---

# Overview

The `aaif-check-setup` skill is a read-only diagnostic capability within the AAIF community events toolkit that verifies whether a host computer is properly configured to execute operational automations [^evt-community-events-file-3422d7005bbb-6740e451]. It assesses Python 3 availability, plugin installations, Google Workspace (`gws`) CLI tokens and permission scopes, Community Intake sheet access, Slack authorization, Luma calendar keys, and headless Chrome [^evt-community-events-file-3422d7005bbb-6740e451].

# Architecture / Specification

The diagnostic engine runs via `python3 <skill-root>/scripts/check_setup.py` under clear boundary invariants [^evt-community-events-file-3422d7005bbb-6740e451]:

- **Non-Destructive Read-Only Operation**: Reads single sheet metadata, calls Slack `auth.test`, and Luma `calendars/get` without performing mutations or leaking raw keys/tokens into execution logs [^evt-community-events-file-3422d7005bbb-6740e451].
- **Remediation Guidance**: Translates diagnostic failures into non-technical step-by-step resolution paths [^evt-community-events-file-3422d7005bbb-6740e451]. For credential failures, it directs operators to authenticate their personal OAuth configuration and generate individual tokens, avoiding shared administrative token lookups [^evt-community-events-file-3422d7005bbb-6740e451] [^evt-community-events-pr-67].
- **Workspace Manipulation Isolation**: Verifies `gws` integration, reinforcing policy restrictions that ban third-party rendering suites like LibreOffice (`soffice`) in favor of direct API operations and temporary PDF previews [^evt-community-events-file-3422d7005bbb-6740e451].

# Lifecycle History

Updated in Pull Request #67 to adjust diagnostic resolution steps away from centralized credential distribution toward individual operator credential provisioning [^evt-community-events-pr-67].

[^evt-community-events-file-3422d7005bbb-6740e451]: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/skills/aaif-check-setup/SKILL.md
[^evt-community-events-pr-67]: https://github.com/aaif/community-events/pull/67
