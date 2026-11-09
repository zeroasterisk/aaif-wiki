---
type: skill
title: AAIF Community Pulse Skill
description: Multi-channel update drafting skill aggregating Slack, Luma, and git
  activity into separate organizer and public digests under synthetic persona privacy
  constraints.
resource: https://github.com/aaif/community-events/pull/47
tags:
- skills
- pulse
- community-events
- privacy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:00:04.606780+00:00'
sources:
- id: evt-community-events-pr-47
  resource: https://github.com/aaif/community-events/pull/47
  author: rparundekar
  last_modified: '2026-09-17T05:27:45+00:00'
---

# Overview
`aaif-community-pulse` is an editorial and operational summarization skill that synthesizes multi-channel activity across Slack, Luma event registrations, and GitHub repositories into structured community digest updates [^evt-community-events-pr-47]. It produces targeted updates distinguishing private operational organizer digests from public community announcements while enforcing contributor privacy rules [^evt-community-events-pr-47].

# Architecture / Specification
The skill parses raw event and chat streams, grouping highlights by chapter, working group, and governance milestones.

## Privacy and Identity Protections
To prevent accidental personal data disclosure in public repositories and open CI pipelines, documentation and in-skill worked examples must adhere to privacy baselines [^evt-community-events-pr-47]:
- **Synthetic Personas**: Worked examples and template outputs must use synthetic organizer personas rather than referencing real community participants [^evt-community-events-pr-47].
- **Public URL Separation**: Verified public resources (such as public Luma event registration pages) may be cited, whereas personal identities and internal contact information are anonymized or masked [^evt-community-events-pr-47].
- **Centralized Redaction**: Relies on unified community-events redaction plumbing to strip email addresses and sensitive identifiers before rendering public drafts [^evt-community-events-pr-47].

# Lifecycle History
In PR #47, real organizer names previously embedded in public worked examples were replaced with synthetic personas to align with AAIF community privacy and PII protection policies [^evt-community-events-pr-47].

[^evt-community-events-pr-47]: https://github.com/aaif/community-events/pull/47
