---
type: skill
title: AAIF Slack Community Audit Skill
description: Standardized automation skill auditing Slack channels, organizer memberships,
  workspace activity, and generating composite health reports.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-audit-slack/references/caches-and-composition.md
tags:
- skills
- community
- slack
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:56:40.298719+00:00'
sources:
- id: evt-community-events-file-8b30d97e0275-93d6c214
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-audit-slack/references/caches-and-composition.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
- id: evt-community-events-file-91886a9e0653-1a4c1c65
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-audit-slack/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
---

# Overview
`aaif-audit-slack` provides a comprehensive, read-only operational audit of the AAIF Slack community workspace [^evt-community-events-file-91886a9e0653-1a4c1c65]. It serves as phase 8 of the estate synchronization pipeline (`../skills/aaif-sync.md`), acting as an independent verification layer to ensure chapter coverage, organizer inclusion, and topic channel activity without modifying Slack state directly [^evt-community-events-file-91886a9e0653-1a4c1c65].

# Architecture / Specification
The audit system is split into three report engines, a shared measurement layer, and a unified HTML summary generator [^evt-community-events-file-91886a9e0653-1a4c1c65][^evt-community-events-file-8b30d97e0275-93d6c214]:

### Report Engines and Scripts
- **Organizers Audit (`audit_organizers.py`)**: Confirms every chapter has active public and organizer channels and verifies that accepted community organizers are present [^evt-community-events-file-91886a9e0653-1a4c1c65].
- **Topics Audit (`audit_topics.py`)**: Evaluates subject-matter channels for message recency, overlap, and newcomer discoverability [^evt-community-events-file-91886a9e0653-1a4c1c65].
- **Members Audit (`audit_members.py`)**: Analyzes workspace composition and user experience from the perspective of standard members [^evt-community-events-file-91886a9e0653-1a4c1c65].
- **Activity Measurement (`audit_activity.py`)**: Supplies message metrics, distinct poster counts, and timestamp of the last human interaction [^evt-community-events-file-91886a9e0653-1a4c1c65].
- **Summary Engine (`summarize_audits.py`)**: Compiles engine outputs into `slack-full-audit.html`, combining chapter, organizer, topic, and member metrics into an actionable priority index [^evt-community-events-file-8b30d97e0275-93d6c214].

### Caching and Security Guardrails
- **Atomic Caching**: Cache files are written with 0600 permissions in a 0700 cache directory (`.slack-audit-cache`) stamped with workspace metadata to prevent cross-workspace contamination [^evt-community-events-file-8b30d97e0275-93d6c214].
- **Git Safety Check**: Scripts refuse to execute if cache or output directories risk inclusion via `git add -A`, safeguarding private member identities and emails from accidental commit to public repositories [^evt-community-events-file-8b30d97e0275-93d6c214].
- **Prompt Injection Defense**: Member profiles, channel topics, and CRM cells are strictly treated as untrusted data and cannot trigger administrative mutations or authorization grants [^evt-community-events-file-91886a9e0653-1a4c1c65].

[^evt-community-events-file-8b30d97e0275-93d6c214]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-audit-slack/references/caches-and-composition.md
[^evt-community-events-file-91886a9e0653-1a4c1c65]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-audit-slack/SKILL.md
