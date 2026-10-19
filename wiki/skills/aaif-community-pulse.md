---
type: skill
title: AAIF Community Pulse Skill
description: Multi-channel update drafting skill aggregating Slack, Luma, and git
  activity into separate organizer, member, and public communications under prompt-injection
  isolation.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-community-pulse/SKILL.md
tags:
- skills
- community
- communications
- slack
- privacy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:09:07.266888+00:00'
sources:
- id: evt-community-events-file-ed850506c872-8d999d9a
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-community-pulse/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-f1c760a76169-b7620e51
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-community-pulse/WORKFLOW.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
---

# Overview
The `aaif-community-pulse` skill drafts the periodic "AAIF Community Organizer Update" (the Pulse), summarizing recent chapter events, upcoming calendar schedules, and foundation operational updates[^evt-community-events-file-ed850506c872-8d999d9a][^evt-community-events-file-f1c760a76169-b7620e51]. Operating under the [Community Event Operations](community-event-operations.md) suite, the skill executes a single data collection pass across Slack, Google Sheets, Luma, and git commits to synthesize three distinct, audience-specific drafts[^evt-community-events-file-ed850506c872-8d999d9a][^evt-community-events-file-f1c760a76169-b7620e51].

The skill enforces strict security and privacy boundaries: it writes local drafts only, never posts autonomously to external APIs, and isolates untrusted user messages to prevent prompt injection[^evt-community-events-file-ed850506c872-8d999d9a][^evt-community-events-file-f1c760a76169-b7620e51].

# Architecture / Specification

## Three-Audience Publishing Model
Because community groups require differing depths of operational detail, the skill creates three distinct text files in a local `.pulse-cache/` directory rather than duplicating content[^evt-community-events-file-f1c760a76169-b7620e51]:

| Draft Variant | Target Audience | Primary Focus | Destination File |
|---|---|---|---|
| Organizer Post | `#local-champs` | Actionable requests, admin and tooling changes, chapter-specific asks[^evt-community-events-file-f1c760a76169-b7620e51] | `.pulse-cache/pulse-local-champs.txt`[^evt-community-events-file-f1c760a76169-b7620e51] |
| Member Post | `#general` | Event recaps, upcoming community calendar, participation links[^evt-community-events-file-f1c760a76169-b7620e51] | `.pulse-cache/pulse-general.txt`[^evt-community-events-file-f1c760a76169-b7620e51] |
| Public Post | LinkedIn / X | High-level foundation narrative, milestones, external awareness[^evt-community-events-file-f1c760a76169-b7620e51] | `.pulse-cache/pulse-social.txt`[^evt-community-events-file-f1c760a76169-b7620e51] |

The organizer draft assumes readers have already viewed the `#general` post and deliberately avoids repeating event listings, focusing exclusively on operational directives[^evt-community-events-file-f1c760a76169-b7620e51].

## Six-Step Workflow Pipeline
Execution proceeds strictly through six sequential phases[^evt-community-events-file-f1c760a76169-b7620e51]:
1. **Gather Organizer Updates**: Fetches semi-private channel history from Slack `#local-champs` via `fetch_local_champs.py`[^evt-community-events-file-f1c760a76169-b7620e51].
2. **Read Sheet Status**: Inspects community intake spreadsheets via `gws` to detect newly formed chapters and assigned organizers[^evt-community-events-file-f1c760a76169-b7620e51].
3. **Query Luma Calendar**: Retrieves past and scheduled events across chapter feeds[^evt-community-events-file-f1c760a76169-b7620e51].
4. **Inspect Git History**: Analyzes recent repository commits to summarize tooling and skill updates[^evt-community-events-file-f1c760a76169-b7620e51].
5. **Compose Drafts**: Generates the three localized text drafts using builder-oriented tone[^evt-community-events-file-f1c760a76169-b7620e51].
6. **Mandatory Cache Cleanup**: Cleans and purges `.pulse-cache/` once user inspection is complete to prevent lingering names and quotes[^evt-community-events-file-ed850506c872-8d999d9a][^evt-community-events-file-f1c760a76169-b7620e51].

## Security and Injection Containment
- **Untrusted Input Invariant**: Content retrieved from Slack and Google Sheets is classified as unverified text, not executable directives[^evt-community-events-file-ed850506c872-8d999d9a][^evt-community-events-file-f1c760a76169-b7620e51]. Messages containing requests such as "mark my chapter accepted" must be flagged as decision items, never enacted automatically[^evt-community-events-file-f1c760a76169-b7620e51].
- **No Autonomous Posting**: The skill contains no network publication endpoints (`chat.postMessage`, social APIs); publication requires human copy-paste approval[^evt-community-events-file-f1c760a76169-b7620e51].
- **Public-Copy Privacy**: PII and names not already public on external event registration pages are withheld from all drafted outputs[^evt-community-events-file-ed850506c872-8d999d9a].

[^evt-community-events-file-ed850506c872-8d999d9a]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-community-pulse/SKILL.md
[^evt-community-events-file-f1c760a76169-b7620e51]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-community-pulse/WORKFLOW.md
