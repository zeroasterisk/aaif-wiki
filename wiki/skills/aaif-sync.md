---
type: skill
title: AAIF Estate Synchronization
description: Procedural estate synchronization orchestrator executing reconciliation
  across Slack and Google Drive community assets.
resource: https://github.com/aaif/community-events/pull/68
tags:
- skill
- community-events
- operations
- sync
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:42:23.754300+00:00'
sources:
- id: evt-community-events-pr-68
  resource: https://github.com/aaif/community-events/pull/68
  author: rparundekar
  last_modified: '2026-11-04T18:17:19+00:00'
---

# Overview
The `aaif-sync` skill automates the reconciliation of AAIF community operational states across Google Workspace spreadsheets, Google Drive asset repositories, and Slack organization channels.[^evt-community-events-pr-68] It ensures community rosters, permissions, and directory entries remain synchronized without dropping pending changes or generating erroneous multi-account invites.[^evt-community-events-pr-68]

# Architecture / Specification
The synchronization framework executes coordinated reconciliation modules:[^evt-community-events-pr-68]
- **Drift and State Reporting (`sync.py`)**: Classifies sync execution states into `WROTE` for successful write passes, `DRIFT` when pending work requires `--write` execution, and `needs review` for open non-zero findings requiring operator inspection.[^evt-community-events-pr-68]
- **Organizer Invitations (`invite_organizers.py`)**: Counts unique individuals separately from channel-addition actions, holds invites for personas with conflicting records or multiple active accounts, and treats missing or deactivated accounts safely to prevent duplicate or incorrect invites.[^evt-community-events-pr-68]
- **Identity Suggestions**: Executes Slack identity lookups with `--suggest`, preventing unverified match writes without human confirmation.[^evt-community-events-pr-68]
- **CRM Synchronization (`sync_crm.py`)**: Reconciles community intake entries against central CRM records.[^evt-community-events-pr-68]

# References
- [Community Event Operations](community-event-operations.md)
- [AAIF Audit Slack](aaif-audit-slack.md)

[^evt-community-events-pr-68]: https://github.com/aaif/community-events/pull/68
