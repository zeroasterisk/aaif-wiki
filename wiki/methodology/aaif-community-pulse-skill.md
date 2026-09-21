---
type: methodology
title: AAIF Community Pulse Skill
description: Operational agent skill for synthesizing biweekly community updates across
  Slack, Google Drive, and Luma with privacy-safe redaction and synthetic fixtures.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/CHANGELOG.md
tags:
- community
- agent-skill
- automation
- privacy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:15:40.175389+00:00'
sources:
- id: evt-community-events-file-06572a96a58d-3b18db49
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/CHANGELOG.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:12:15-07:00'
- id: evt-community-events-pr-47
  resource: https://github.com/aaif/community-events/pull/47
  author: rparundekar
  last_modified: '2026-09-17T05:27:45+00:00'
---

# Overview

The `aaif-community-pulse` skill is an automated operational capability within the AAIF Community Events Toolkit that aggregates and summarizes biweekly community metrics, events, and chapter activities across Slack channels, Google Drive documents, and Luma trackers [^evt-community-events-file-06572a96a58d-3b18db49].

# Architecture / Specification

## Privacy and Data Redaction

To prevent personal identifiable information (PII) leakage into public repositories and logs, the skill enforces strict redaction standards:
- **Synthetic Test Casts**: All worked examples and skill documentation utilize synthetic organizer profiles and fixtures rather than real organizer identities [^evt-community-events-file-06572a96a58d-3b18db49] [^evt-community-events-pr-47].
- **Centralized Redaction Surface**: Shared redaction logic (`lib/aaif_events/redact.py`) uniformly scrubs email addresses and contact information, validated by automated drift checks (`check_no_local_redaction.py`) [^evt-community-events-file-06572a96a58d-3b18db49] [^evt-community-events-pr-47].
- **Resilient Sheet Ingestion**: Spreadsheet ingestion uses header-name resolution with duplicate-header guards and unified error handling across transient API failures [^evt-community-events-file-06572a96a58d-3b18db49] [^evt-community-events-pr-47].

# Lifecycle History

- Refactored in v0.6.0 to eliminate local script redaction drift, sanitize historical worked examples to synthetic fixtures, and adopt centralized Google Workspace API client handling [^evt-community-events-file-06572a96a58d-3b18db49] [^evt-community-events-pr-47].

[^evt-community-events-file-06572a96a58d-3b18db49]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/CHANGELOG.md
[^evt-community-events-pr-47]: https://github.com/aaif/community-events/pull/47
