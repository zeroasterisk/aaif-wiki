---
type: skill
title: aaif-sync
description: Procedural estate synchronization orchestrator reconciling community
  sheets, gating chapter listings to accepted organizers, and rendering unified navigation
  across run report pages.
resource: https://github.com/aaif/community-events/pull/62
tags:
- community
- operations
- sync
- reporting
- skills
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:33:44.152648+00:00'
sources:
- id: evt-community-events-pr-62
  resource: https://github.com/aaif/community-events/pull/62
  author: rparundekar
  last_modified: '2026-11-02T07:31:04+00:00'
- id: evt-community-events-pr-63
  resource: https://github.com/aaif/community-events/pull/63
  author: rparundekar
  last_modified: '2026-11-02T07:03:54+00:00'
---

# Overview

The `aaif-sync` operational skill synchronizes AAIF community records, Google Drive folders, and chapter listings, enforcing strict organizer validation rules and generating interconnected HTML operational reports [^evt-community-events-pr-62] [^evt-community-events-pr-63].

# Architecture / Specification

### Accepted Organizer Gating and Removal Safeguards

Chapter folder creation triggers and public chapter listings are restricted exclusively to locations with accepted organizers [^evt-community-events-pr-62]:
- **CRM Sync Validation**: The `sync_crm` module lists only cities with an accepted organizer for chapter provisioning, suppressing unverified applicants, pipeline hosts, and AAIF operations staff into anonymous counts [^evt-community-events-pr-62].
- **Human-Gated Removal**: The `sync_chapters` module flags organizer names listed under non-qualifying status records and proposes their removal [^evt-community-events-pr-62]. To prevent public form submissions from evicting legitimate organizers, standard `--write` runs cannot delete entries; removals require explicit human inspection and the `--apply-removals` flag [^evt-community-events-pr-62].
- **Stale Cell Protection**: Cells targeted for update are re-read immediately prior to execution, aborting if concurrent external edits are detected [^evt-community-events-pr-62].

### Unified Multi-Page Report Navigation

A full synchronization run generates a six-page report suite consisting of `report.html`, coverage, activity, topics, members, and Slack audit views [^evt-community-events-pr-63]:
- **Cross-Page Top Bar**: The execution runner (`sync.py`) passes the ordered list of rendered pages via `AAIF_REPORT_NAV` to `report_style.page()`, which renders a sticky, flat, hairline top navigation bar [^evt-community-events-pr-63].
- **Dead-Link Prevention**: The reporting renderer (`render_report.py`) prunes failed or unwritten pipeline stages to ensure the navigation bar references only valid sibling HTML files [^evt-community-events-pr-63].
- **Print Isolation**: Top navigation bars are automatically hidden during print styling to preserve standalone PDF exports [^evt-community-events-pr-63].

# References

- [`../skills/community-event-operations.md`](../skills/community-event-operations.md)
- [`../skills/aaif-create-chapter.md`](../skills/aaif-create-chapter.md)
- [`../guidelines/brand-guidelines.md`](../guidelines/brand-guidelines.md)

[^evt-community-events-pr-62]: https://github.com/aaif/community-events/pull/62
[^evt-community-events-pr-63]: https://github.com/aaif/community-events/pull/63
