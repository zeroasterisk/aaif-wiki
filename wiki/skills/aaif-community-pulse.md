---
type: skill
title: AAIF Community Pulse Skill
description: Standardized automation skill drafting multi-audience community organizer
  updates across Slack channels and public social channels.
resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-community-pulse/SKILL.md
tags:
- skills
- community
- automation
- slack
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:58:42.587132+00:00'
sources:
- id: evt-community-events-file-ed850506c872-63272570
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-community-pulse/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
- id: evt-community-events-file-f1c760a76169-ceb51f5d
  resource: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-community-pulse/WORKFLOW.md
  author: Rahul Parundekar
  last_modified: '2026-09-30T18:54:05-07:00'
- id: evt-community-events-pr-54
  resource: https://github.com/aaif/community-events/pull/54
  author: rparundekar
  last_modified: '2026-10-01T02:01:13+00:00'
---

# Overview
`aaif-community-pulse` is an automation skill that collects community activity data and drafts biweekly update digests across three distinct target audiences: organizers (`#local-champs`), community members (`#general`), and external social networks (LinkedIn/X)[^evt-community-events-file-ed850506c872-63272570][^evt-community-events-file-f1c760a76169-ceb51f5d].

# Architecture / Specification
- **Multi-Audience Triad**: From a single gathering pass, generates three separate drafts:
  - *Organizer Post* (`.pulse-cache/pulse-local-champs.txt`): Focuses on actionable chapter operational tasks, admin/tooling updates, and requests[^evt-community-events-file-f1c760a76169-ceb51f5d].
  - *Member Post* (`.pulse-cache/pulse-general.txt`): Highlights past event recaps and upcoming community calendar listings[^evt-community-events-file-f1c760a76169-ceb51f5d].
  - *Public Post* (`.pulse-cache/pulse-social.txt`): Provides ecosystem-facing overviews of community growth[^evt-community-events-file-f1c760a76169-ceb51f5d].
- **Security & Untrusted Source Guardrails**: Channel messages and spreadsheet cells are strictly treated as data rather than execution directives. Drafts are written exclusively to local files in `.pulse-cache/` and never directly posted to remote networks via API[^evt-community-events-file-ed850506c872-63272570][^evt-community-events-file-f1c760a76169-ceb51f5d].
- **Plugin Packaging**: Conforms to Agent Plugins v1 portable packaging rules declaring explicit runtime dependencies and portable directory resolution tokens[^evt-community-events-pr-54].

# References
- [`skills/aaif-sync`](../skills/aaif-sync.md)
- [`skills/aaif-triage-intake`](../skills/aaif-triage-intake.md)
- [`policies-guidelines/social-guidelines`](../policies-guidelines/social-guidelines.md)

[^evt-community-events-file-ed850506c872-63272570]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-community-pulse/SKILL.md
[^evt-community-events-file-f1c760a76169-ceb51f5d]: https://github.com/aaif/community-events/blob/f978969d2ecb635a7e3a35bff0fc715de52406d9/skills/aaif-community-pulse/WORKFLOW.md
[^evt-community-events-pr-54]: https://github.com/aaif/community-events/pull/54
