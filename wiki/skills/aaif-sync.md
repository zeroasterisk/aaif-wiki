---
type: skill
title: AAIF Sync
description: Procedural operations pipeline orchestrating community estate reconciliation,
  safe chapter retirement, drift reporting, and organizer invitation workflows.
resource: https://github.com/aaif/community-events/pull/68
tags:
- skill
- operations
- automation
- community
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:33:12.467454+00:00'
sources:
- id: evt-community-events-pr-68
  resource: https://github.com/aaif/community-events/pull/68
  author: rparundekar
  last_modified: '2026-11-04T18:17:19+00:00'
---

# Overview
The `aaif-sync` skill automates the reconciliation of community operational assets across GitHub, Google Drive, Luma, Slack, and CRM systems[^evt-community-events-pr-68]. It checks intake records against active infrastructure, generates deterministic drift reports, flags inconsistencies, and selectively writes back verified state updates to maintain synchronized community operations[^evt-community-events-pr-68].

# Architecture / Specification
The pipeline is orchestrated primarily via `sync.py` along with specialized submodules including `invite_organizers.py`, `sync_crm.py`, and `resolve_slack_ids.py`[^evt-community-events-pr-68].

### Reconciliation and Drift Classification
To prevent reporting pending changes as fully synchronized, the sync workflow evaluates run findings into distinct operational statuses:
- **DRIFT**: Assigned when clean execution (exit code 0) yields actionable findings prefixed with `apply with --write` or `re-run --write`, denoting unapplied pending changes[^evt-community-events-pr-68].
- **NEEDS REVIEW**: Assigned when open findings require manual human intervention or adjudication, leaving exit codes intact[^evt-community-events-pr-68].
- **WROTE**: Denotes successful application of updates during a write-enabled execution[^evt-community-events-pr-68].
- **PARTIAL**: Dominant terminal state assigned if any sub-operation fails or halts mid-run[^evt-community-events-pr-68].

### Identity Resolution and Invite Safety
The invitation workflow (`invite_organizers.py`) applies strict safeguards to prevent duplicate or invalid invitations:
- **Account Disambiguation and Holds**: Individuals associated with multiple active Slack accounts or conflicting reviewed intake rows are automatically held; held organizers are recorded in the execution log and excluded from automated invitations[^evt-community-events-pr-68].
- **Stale Identifier Pruning**: Column IDs corresponding to deactivated accounts yield to confirmed live accounts[^evt-community-events-pr-68].
- **Identity Suggestions**: Identity resolution runs with `--suggest` by default, ensuring candidate name and email matches are proposed for review and never written automatically[^evt-community-events-pr-68].

[^evt-community-events-pr-68]: https://github.com/aaif/community-events/pull/68
