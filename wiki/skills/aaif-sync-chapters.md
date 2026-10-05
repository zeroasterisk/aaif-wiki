---
type: skill
title: AAIF Sync Chapters Skill
description: Standardized automation skill managing chapter lifecycle states, estate
  capacity caps, health metrics, and non-destructive retirement reporting.
resource: https://github.com/aaif/community-events/pull/55
tags:
- skill
- community
- operations
- chapters
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T06:00:17.540946+00:00'
sources:
- id: evt-community-events-pr-55
  resource: https://github.com/aaif/community-events/pull/55
  author: rparundekar
  last_modified: '2026-10-01T23:11:19+00:00'
---

# Overview
The `aaif-sync-chapters` skill automates the lifecycle tracking, capacity caps, and health audits of AAIF city chapters across operational spreadsheets and public registries[^evt-community-events-pr-55]. It ensures synchronization between organizer rosters, community activity metrics, and chapter directory records while enforcing strict non-destructive update guarantees[^evt-community-events-pr-55].

# Architecture / Specification
The chapter synchronization workflow operates under deterministic state rules:
- **Non-Destructive Retention**: Chapter records are never deleted or cleared automatically from the primary Chapters List, preserving handwritten historical summaries, images, and operational notes[^evt-community-events-pr-55].
- **Retirement Candidate Reporting**: Cities without qualifying active organizers are flagged as retirement candidates on the execution Drift tab rather than pruned during `--write` passes[^evt-community-events-pr-55].
- **Manual State Transitions**: Candidate chapters require explicit human intervention to transition into `Deprecated` or `Merged` (referencing a `Merged Into` target) states[^evt-community-events-pr-55].
- **Ambiguity Holds**: Ambiguous city inputs, malformed records, or unresolved organizers hold chapter mutation until verified[^evt-community-events-pr-55].

# Lifecycle History
Governed under community automation workflows, the chapter sync engine was updated in PR #55 to deprecate destructive row clearing in favor of soft deprecation and drift candidate reporting[^evt-community-events-pr-55].

[^evt-community-events-pr-55]: https://github.com/aaif/community-events/pull/55
