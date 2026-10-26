---
type: skill
title: AAIF Slack Audit Skill
description: Read-only Slack workspace inspection skill providing channel health auditing,
  member activity tracking, and on-demand spam detection.
resource: https://github.com/aaif/community-events/pull/61
tags:
- slack
- community-events
- security
- auditing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T11:06:06.176360+00:00'
sources:
- id: evt-community-events-pr-61
  resource: https://github.com/aaif/community-events/pull/61
  author: rparundekar
  last_modified: '2026-10-15T19:42:34+00:00'
---

# Overview
The AAIF Slack Audit Skill provides read-only inspection tools for community administrators to audit channel health, verify permissions, and detect commercial spam across Agentic AI Foundation Slack workspaces [^evt-community-events-pr-61]. Operating on demand, the skill inspects public channels, conversation threads, and token-owner direct messages to identify vendor solicitation and account rental schemes without persisting sensitive conversation records [^evt-community-events-pr-61].

# Architecture / Specification
The skill enforces read-only access boundaries and strictly treats community message text as untrusted data [^evt-community-events-pr-61].

## Spam Detection Engine (`audit_spam.py`)
The on-demand spam audit module flags member activity using composite behavioral signals [^evt-community-events-pr-61]:
- **Detection Heuristics:** Identifies service and partnership pitches, "DM me" conversion attempts, LinkedIn account rental offers, commercial money bait, duplicate message cross-posting across three or more channels, and promotional messages posted outside dedicated promotion rooms [^evt-community-events-pr-61].
- **Scan Boundaries:** Inspects public channels, parent-thread replies within an extended lookback window (controlled via `--thread-lookback`, default 365 days), and direct messages accessible via `search.messages`. Shared vendor rooms (`ext-*`) and organizer channels (`*-organizers`) are excluded from scoring [^evt-community-events-pr-61].
- **Untrusted Input Sanitization:** Prints output strictly to the terminal with zero disk persistence. Message snippets are rendered within `<<msg>>` boundary markers, with internal delimiter characters in message bodies and display names systematically neutralized [^evt-community-events-pr-61].
- **Human Verification Gate:** Outputs diagnostic leads rather than automated penalties; account deactivation remains an administrative human action executed via the console [^evt-community-events-pr-61].

## API Integration and Resilience
- **Method Allowlist:** Explicitly permits `conversations.replies` and `search.messages` within `aaif_events.slack.ALLOWED_METHODS` for read-only audit callers [^evt-community-events-pr-61].
- **Paging Robustness:** Avoids Slack API `conversations.history` filtering anomalies where `oldest=` arguments fail to return active messages by fetching pages chronologically and terminating manually at the window boundary, flagging incomplete or skipped channel queries [^evt-community-events-pr-61].

[^evt-community-events-pr-61]: https://github.com/aaif/community-events/pull/61
