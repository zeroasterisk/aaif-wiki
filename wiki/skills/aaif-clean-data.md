---
type: skill
title: AAIF Clean Data Skill
description: Operational data normalization and intake hygiene skill enforcing proposal-execution
  splits, multi-tab verdict filtering, and submission validation.
resource: https://github.com/aaif/community-events/pull/58
tags:
- skill
- community
- operations
- data-hygiene
- aaif
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:19:47.613466+00:00'
sources:
- id: evt-community-events-pr-58
  resource: https://github.com/aaif/community-events/pull/58
  author: rparundekar
  last_modified: '2026-10-08T18:30:02+00:00'
---

# Overview

The `aaif-clean-data` skill is an automated operational pipeline and data hygiene utility used across AAIF community intake trackers and event estates.[^evt-community-events-pr-58] It normalizes contributor and applicant submissions, enforces proposal-execution splits across operational spreadsheets, verifies contact identifiers, and manages hygiene flags across multi-role applicant records.[^evt-community-events-pr-58]

# Architecture / Specification

## Multi-Tab Verdict Filtering
Applicant records frequently span multiple role tabs (such as organizer and speaker) with distinct evaluation verdicts.[^evt-community-events-pr-58] To prevent unactionable issue alerts on rejected applicants, the data scanning engine implements unanimous negative verdict suppression:[^evt-community-events-pr-58]
- **Decided-No Suppression:** The `scan` command skips flagging a submission if and only if every role tab containing the applicant evaluates to a terminal negative status (`Denied`, `Inactive`, or `Duplicate`).[^evt-community-events-pr-58]
- **Mixed-Verdict Retention:** If an applicant is rejected on one role tab (e.g., organizer Denied) but remains active or prospective on another (e.g., speaker Prospect), issues continue to be flagged for review.[^evt-community-events-pr-58]
- **Missing Metadata Fallback:** If a role tab lacks standard `Status`, `Timestamp`, or `Email` columns, verdict suppression is disabled for that tab to prevent silent suppression.[^evt-community-events-pr-58]
- **Live Spreadsheet Formula Synchronization:** The `issues_formula()` helper generated via `install_flags` renders decided-no rows as blank rather than error-flagged, maintaining clean operational views for community organizers.[^evt-community-events-pr-58]

# References

- Repository: `aaif/community-events` (PR #58)[^evt-community-events-pr-58]
- Related skills: `../skills/aaif-audit-slack.md`, `../skills/community-event-operations.md`

[^evt-community-events-pr-58]: https://github.com/aaif/community-events/pull/58
