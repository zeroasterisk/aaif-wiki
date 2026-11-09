---
type: skill
title: Slack Community Audit
description: Read-only diagnostic inspection skill auditing AAIF Slack channels, message
  hygiene, cross-posting, and unsolicited sales pitches.
resource: https://github.com/aaif/community-events/pull/61
tags:
- skills
- slack
- audit
- community-ops
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:24:04.193516+00:00'
sources:
- id: evt-community-events-pr-61
  resource: https://github.com/aaif/community-events/pull/61
  author: rparundekar
  last_modified: '2026-10-15T19:42:34+00:00'
---

# Overview

The `aaif-audit-slack` skill provides read-only diagnostic and administrative tooling for inspecting the health, configuration, and conversational integrity of AAIF community Slack workspaces [^evt-community-events-pr-61]. It operates out-of-band from state reconciliation engines like [aaif-sync](../skills/aaif-sync.md), producing terminal-only reports without mutating workspace content or storing untrusted message text on local disks [^evt-community-events-pr-61].

# Architecture / Specification

## Sales and Spam Detection Engine

The audit suite includes `skills/aaif-audit-slack/scripts/audit_spam.py`, a specialized inspection script that evaluates public message activity and direct message telemetry to score accounts exhibiting uninvited commercial outreach [^evt-community-events-pr-61]. Scored heuristics include:

- Unsolicited service offerings and vendor partnership solicitations [^evt-community-events-pr-61].
- Direct invitation requests ("DM me") and financial incentives [^evt-community-events-pr-61].
- LinkedIn account rental propositions [^evt-community-events-pr-61].
- Cross-posting identical message payloads across three or more public channels [^evt-community-events-pr-61].
- Promotional pitches posted outside dedicated promotional channels [^evt-community-events-pr-61].

Shared partner vendor rooms (`ext-*`) and administrative organizer rooms (`*-organizers`) are explicitly excluded from scoring [^evt-community-events-pr-61]. Audit outputs represent lead indicators for human administrative review in the workspace console rather than automated enforcement triggers [^evt-community-events-pr-61].

## Security and Allowlist Boundaries

The audit tool extends the approved `aaif_events.slack.ALLOWED_METHODS` allowlist with read-only endpoints `conversations.replies` and `search.messages` [^evt-community-events-pr-61]. Untrusted message snippets and user display names are strictly sanitized and bounded inside `<<msg>>` terminal wrappers to prevent log escape and prompt injection vulnerabilities [^evt-community-events-pr-61].

## Slack API Pagination Defenses

Live empirical evaluations revealed that passing the `oldest=` timestamp parameter to Slack's `conversations.history` API occasionally returns empty channel payloads despite active conversations within the queried window [^evt-community-events-pr-61]. To ensure complete audit coverage, the scanner pages sequentially through channels without `oldest` and terminates traversal manually upon encountering the window cutoff [^evt-community-events-pr-61].

[^evt-community-events-pr-61]: https://github.com/aaif/community-events/pull/61
