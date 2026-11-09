---
type: skill
title: Community Event Operations Skill
description: Procedural operations pipeline managing chapter estate provisioning,
  lifecycle statuses, organizer onboarding, and country chapter resolution.
resource: https://github.com/aaif/community-events/pull/57
tags:
- skills
- community
- operations
- automation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:16:27.684579+00:00'
sources:
- id: evt-community-events-pr-57
  resource: https://github.com/aaif/community-events/pull/57
  author: rparundekar
  last_modified: '2026-10-07T03:29:07+00:00'
---

# Overview
The `community-event-operations` skill governs the administrative lifecycle, estate reconciliation, and identity routing across all Agentic AI Foundation community chapters[^evt-community-events-pr-57]. It coordinates automated provisioning across Google Drive, Luma calendars, CRM databases, and communication channels under deterministic safety and naming invariants[^evt-community-events-pr-57].

# Architecture / Specification
The pipeline handles intake normalization, chapter resolution, access provisioning, and Slack roster synchronization across disparate platforms[^evt-community-events-pr-57].

### Country Chapter Resolution
To support broader regional participation, metropolitan chapters may be consolidated into broader country chapters (e.g., Tokyo into AAIF Japan, or Wellington and Auckland into AAIF New Zealand)[^evt-community-events-pr-57].
- **Deterministic Resolution (`chapter_for`)**: A central intake resolver maps historical or metropolitan city submissions to their parent country chapter, ensuring applicants cannot be accidentally fragmented across multiple chapters[^evt-community-events-pr-57].
- **Fold Precedence (`COUNTRY_CHAPTER_FOLDS`)**: Intake hygiene engines enforce fold rules ahead of raw chapter records to prevent retired municipal records from reclaiming regional events[^evt-community-events-pr-57].
- **Ordered Migration Invariant**: When transitioning metropolitan chapters to country chapters, underlying Google Drive folders, About documents, CRM records, and tracking sheets must be renamed prior to merging automation updates to avoid orphan record duplication[^evt-community-events-pr-57].

# Lifecycle History
- **PR #57 (community-events)**: Consolidated Tokyo into AAIF Japan and Wellington into AAIF New Zealand, introducing runtime city folding across sync and clean engines[^evt-community-events-pr-57].

[^evt-community-events-pr-57]: https://github.com/aaif/community-events/pull/57
