---
type: skill
title: AAIF Estate Sync Pipeline
description: Procedural pipeline orchestrator coordinating AAIF community estate reconciliation,
  organizer verification, report site navigation, and directory synchronization.
resource: https://github.com/aaif/community-events/pull/62
tags:
- skills
- sync
- crm
- community
- reporting
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:34:12.987397+00:00'
sources:
- id: evt-community-events-pr-62
  resource: https://github.com/aaif/community-events/pull/62
  author: rparundekar
  last_modified: '2026-11-02T07:31:04+00:00'
- id: evt-community-events-pr-63
  resource: https://github.com/aaif/community-events/pull/63
  author: rparundekar
  last_modified: '2026-11-02T07:03:54+00:00'
---

# Overview
The `aaif-sync` skill orchestrates automated synchronization across AAIF community touchpoints, Google Drive chapter folders, CRM trackers, and Slack workspaces [^evt-community-events-pr-62][^evt-community-events-pr-63]. It cross-checks public intake records against active chapter rosters, enforces human authorization before altering public organizer listings, and produces connected multi-page HTML audit reports following the AAIF design system [^evt-community-events-pr-62][^evt-community-events-pr-63].

# Architecture / Specification

## Cross-Report Navigation Bar
- **Page Manifest Generation**: `sync.py` computes the list of active report pages (`run_pages`), recording the sequence in `run.json` and exposing it to rendering engines via `AAIF_REPORT_NAV` [^evt-community-events-pr-63].
- **Sticky Header Component**: `report_style.page()` renders a persistent top navigation bar across sibling HTML reports, resolving relative links and marking the active view while automatically suppressing the bar during print operations [^evt-community-events-pr-63].
- **Broken Link Prevention**: `render_report.py` filters links against actually written outputs so that failed sub-steps do not introduce dead links [^evt-community-events-pr-63].

## Organizer Qualification and Removal Gating
- **Accepted Organizer Requirement**: In `sync_crm`, folderless cities are only surfaced for chapter creation via `aaif-create-chapter` if they have an accepted organizer; general pipeline applicants, speakers, and operations staff are aggregated into counts without naming [^evt-community-events-pr-62].
- **Human-in-the-Loop Roster Pruning**: Implementing the [proposal-execution split](../patterns/proposal-execution-split.md), `sync_chapters` flags non-qualifying organizers for removal but restricts execution to an explicit manual flag (`--apply-removals`) to protect public rosters against malicious or mistaken intake submissions [^evt-community-events-pr-62].
- **Roster Invariants**: Untracked hand entries and historical organizers are preserved, and any removal proposal that would completely empty a chapter's organizer cell is halted as an operational retirement question that halts execution with exit code 2 [^evt-community-events-pr-62].

# Lifecycle History
- Extended in PR#62 to enforce organizer acceptance requirements for chapter provisioning and human-gated roster pruning [^evt-community-events-pr-62].
- Enhanced in PR#63 with unified multi-page top navigation across sync report suites [^evt-community-events-pr-63].

[^evt-community-events-pr-62]: https://github.com/aaif/community-events/pull/62
[^evt-community-events-pr-63]: https://github.com/aaif/community-events/pull/63
