---
type: skill
title: AAIF Audit Slack Skill
description: Configuration-driven Slack inspection skill auditing chapter channels,
  organizer rooms, message integrity, and unsolicited commercial spam.
resource: https://github.com/aaif/community-events/pull/61
tags:
- skills
- slack
- community-events
- operations
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:35:51.444864+00:00'
sources:
- id: evt-community-events-pr-61
  resource: https://github.com/aaif/community-events/pull/61
  author: rparundekar
  last_modified: '2026-10-15T19:42:34+00:00'
---

# Overview

The `aaif-audit-slack` skill provides automated, read-only inspection and hygiene auditing across the AAIF Slack workspace, validating regional chapter channels, organizer coordination spaces, and channel configurations[^evt-community-events-pr-61]. It operates alongside [community-event-operations](../skills/community-event-operations.md) to detect operational drift and commercial abuse while preventing untrusted message text from persisting to disk[^evt-community-events-pr-61].

# Architecture / Specification

## Spam and Commercial Outreach Detection

An on-demand inspection tool (`audit_spam.py`) scans public channels, reply threads, and token-owner direct message searches using heuristics designed to detect unsolicited commercial pitches[^evt-community-events-pr-61]:

- **Signal Ranking**: Ranks members based on detected services pitches, "DM me" conversion attempts, LinkedIn-account rental offers, financial solicitations, and identical messages cross-posted across three or more channels outside designated promotion areas[^evt-community-events-pr-61].
- **Scope Isolation**: Excludes shared external vendor rooms (`ext-*`) and organizer channels (`*-organizers`) from behavioral scoring[^evt-community-events-pr-61].
- **Untrusted Input Protection**: Message snippets print to terminal output within sanitized `<<msg>>` delimiters; no message text is written to persistent disk storage[^evt-community-events-pr-61].
- **Pagination Handling**: Because Slack's `conversations.history` API intermittently yields empty results when queried with timestamp boundaries (`oldest=`), the audit script pages without `oldest` and enforces evaluation boundaries locally with thread-reply lookback tracking[^evt-community-events-pr-61].
- **Human-in-the-Loop Governance**: Audit findings serve solely as administrative leads; deactivations and enforcement actions remain manual human decisions in the Slack admin console[^evt-community-events-pr-61].

# Lifecycle History

Expanded in PR #61 within `aaif/community-events` to add dedicated spam detection heuristics and register `conversations.replies` and `search.messages` in the Slack client allowlist[^evt-community-events-pr-61].

[^evt-community-events-pr-61]: https://github.com/aaif/community-events/pull/61
