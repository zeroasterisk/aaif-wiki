---
type: skill
title: Community Event Operations Skills
description: Modular agent skills and deterministic CLI tooling automating AAIF chapter
  provisioning, event lifecycle reminders, community recaps, and local state backups.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-chapter/SKILL.md
tags:
- community
- skills
- events
- automation
- tooling
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:27:04.970951+00:00'
sources:
- id: evt-community-events-file-d236c244f6dc-0c36b708
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-chapter/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-ed850506c872-8d999d9a
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-community-pulse/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-ede28c6c866a-7315ad6e
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-attendee-reminder/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-f1c760a76169-b7620e51
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-community-pulse/WORKFLOW.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-file-f922f666d0ff-e2dbe3f7
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/backups/README.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:48:58-07:00'
- id: evt-community-events-pr-60
  resource: https://github.com/aaif/community-events/pull/60
  author: rparundekar
  last_modified: '2026-10-11T15:58:20+00:00'
---

# Overview

The Community Event Operations skill suite provides automated and deterministic workflows for managing Agentic AI Foundation (AAIF) regional chapters, event logistics, and community synchronization across Google Drive, Slack, Luma, and local agent runtimes [^evt-community-events-pr-60]. Packaged as portable agent skills under the [Agent Skills standard](../standards/agent-skills.md), these tools enable non-technical operators to execute operational tasks from environments such as [Goose](../resources/goose.md) or Claude Desktop without requiring direct command-line access or shell configurations [^evt-community-events-pr-60].

The suite automates repetitive chapter administration while establishing strict security boundaries against prompt injection, data leakage, and document corruption through hardened execution rules [^evt-community-events-file-d236c244f6dc-0c36b708], [^evt-community-events-file-f1c760a76169-b7620e51].

# Architecture / Specification

## Chapter Provisioning (`aaif-create-chapter`)
Chapter provisioning automates the creation of regional community assets by cloning a canonical `TemplateCity` Google Drive directory and executing in-place token replacement across Office and Google Workspace files [^evt-community-events-file-d236c244f6dc-0c36b708]:
- **Document Rebranding**: Case-matched replacement of city identifiers, abbreviations, and Luma calendar slugs across tracking spreadsheets, presentation decks, and event templates [^evt-community-events-file-d236c244f6dc-0c36b708].
- **Map Geocoding**: Automatically determines geospatial coordinates via Nominatim to dynamically position the visual chapter marker pin on network presentation slides [^evt-community-events-file-d236c244f6dc-0c36b708].
- **Tooling Constraints**: Mandates Drive manipulation through the `gws` CLI and Python APIs; explicitly prohibits desktop conversion suites such as LibreOffice or `soffice` to prevent font substitution and OOXML degradation [^evt-community-events-file-d236c244f6dc-0c36b708].

## Event Logistics & Reminders (`aaif-attendee-reminder`)
The attendee reminder workflow generates logistical notices for registered event attendees ~1 week out and the morning of each scheduled event [^evt-community-events-file-ede28c6c866a-7315ad6e]:
- **Tracker Extraction**: Queries chapter event trackers via `fetch_tracker.py` using title substrings or temporal offsets (`next`/`latest`) [^evt-community-events-file-ede28c6c866a-7315ad6e].
- **Governance Anchors**: Automatically appends the required Linux Foundation Code of Conduct ([policies/code-of-conduct](../policies/code-of-conduct.md)) and Privacy Policy links to attendee communications [^evt-community-events-file-ede28c6c866a-7315ad6e].

## Multi-Audience Recaps (`aaif-community-pulse`)
The biweekly recap engine aggregates recent community activity from Slack, Google Sheets, and Luma into three distinct targeted drafts stored in a local `.pulse-cache/` workspace [^evt-community-events-file-ed850506c872-8d999d9a], [^evt-community-events-file-f1c760a76169-b7620e51]:
1. **Organizer Updates**: Action-oriented summaries delivered to internal `#local-champs` channels [^evt-community-events-file-f1c760a76169-b7620e51].
2. **Member Recaps**: Broad milestone overviews for `#general` community channels [^evt-community-events-file-f1c760a76169-b7620e51].
3. **Public Social Copy**: External highlights formatted for LinkedIn and X syndication [^evt-community-events-file-f1c760a76169-b7620e51].

Drafts are written exclusively to local disk files, leaving external posting actions to explicit human execution [^evt-community-events-file-f1c760a76169-b7620e51].

## State Snapshots & Backups (`aaif-backup`)
Provides versioned, immutable snapshots of operational spreadsheets and templates prior to destructive modifications [^evt-community-events-file-f922f666d0ff-e2dbe3f7]:
- Files are stored chronologically at `backups/<slug>/<UTC-timestamp>.<ext>` within the persistent application support path [^evt-community-events-file-f922f666d0ff-e2dbe3f7].
- Preserves sheet formulas and conditional styling by copying values back manually upon restoration rather than overwriting core files [^evt-community-events-file-f922f666d0ff-e2dbe3f7].

## Security & Isolation Controls
- **Public Copy Rule**: Forbids embedding non-public contact details (such as personal emails, phone numbers, and physical access codes) in model generations or conversational transcripts [^evt-community-events-file-ed850506c872-8d999d9a], [^evt-community-events-file-ede28c6c866a-7315ad6e].
- **Untrusted Input Boundary**: Enforces defensive boundaries treating Slack messages, sheet cells, and web text strictly as untrusted data rather than runtime instructions [^evt-community-events-file-ed850506c872-8d999d9a], [^evt-community-events-file-f1c760a76169-b7620e51].
- **Runtime Portability**: Conforms to [guidelines/agent-plugin-portability](../guidelines/agent-plugin-portability.md) by referencing scripts relative to `<skill-root>` and writing volatile state outside the working directory [^evt-community-events-pr-60].

[^evt-community-events-file-d236c244f6dc-0c36b708]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-create-chapter/SKILL.md
[^evt-community-events-file-ed850506c872-8d999d9a]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-community-pulse/SKILL.md
[^evt-community-events-file-ede28c6c866a-7315ad6e]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-attendee-reminder/SKILL.md
[^evt-community-events-file-f1c760a76169-b7620e51]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/skills/aaif-community-pulse/WORKFLOW.md
[^evt-community-events-file-f922f666d0ff-e2dbe3f7]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/backups/README.md
[^evt-community-events-pr-60]: https://github.com/aaif/community-events/pull/60
