---
type: methodology
title: Operational agent skill for resolving and tracking community member identities
  across platforms
description: Methodology for accurately mapping community member identities between
  intake forms, Slack accounts, and Drive access lists, accounting for email normalization
  issues.
resource: https://github.com/aaif/community-events/pull/44
tags:
- methodology
- operations
- identity
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-flash-latest
  at: '2026-09-21T10:11:02.862187+00:00'
sources:
- id: evt-community-events-pr-44
  resource: https://github.com/aaif/community-events/pull/44
  author: rparundekar
  last_modified: '2026-09-16T17:46:50+00:00'
---

# Overview
The AAIF Identity Resolution Skill addresses the complexity of mapping a single community member's identity across multiple platforms (intake forms, Slack, Google Drive). It resolves identity discrepancies caused by platform-specific behaviors, such as how email addresses are handled [^evt-community-events-pr-44].

# Architecture / Specification
Identity resolution relies on robust lookup logic, particularly for Slack accounts:
1.  **Email Normalization:** The skill handles consumer Gmail's dot and `+tag` folding (e.g., `first.last@gmail.com` vs. `firstlast@gmail.com`) when performing `users.lookupByEmail` retries, as Slack treats these variants as distinct accounts [^evt-community-events-pr-44].
2.  **Identity Tracking:** Three distinct identity columns are maintained in the community tracking sheet to capture the full identity state:
    *   `Slack ID`: The immutable Slack user ID.
    *   `Slack Email`: The email address associated with the Slack account.
    *   `Drive Email`: The email address actually granted access to the chapter folder ACL [^evt-community-events-pr-44].
3.  **Error Handling and Safety:** The skill includes safeguards against critical errors, such as preventing parsing failures (e.g., non-breaking spaces in cells) from causing one person's account ID to be silently inherited by the next person's row. It also ensures that automated name matching is treated only as a suggestion requiring manual review (`--apply`) to prevent misidentification [^evt-community-events-pr-44].

[^evt-community-events-pr-44]: https://github.com/aaif/community-events/pull/44
