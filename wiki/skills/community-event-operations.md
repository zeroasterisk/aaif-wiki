---
type: skill
title: Community Event Operations Toolkit
description: Standardized agent skill suite and portable plugin runtime managing AAIF
  chapter provisioning, estate synchronization, event planning, and communications.
resource: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/README.md
tags:
- aaif
- skill
- community
- operations
- events
- goose
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:35:22.654393+00:00'
sources:
- id: evt-community-events-file-b33563055168-23a10754
  resource: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/README.md
  author: Rahul Parundekar
  last_modified: '2026-11-03T22:44:51-08:00'
---

# Overview
The Community Event Operations Toolkit provides packaged agent skills and operational workflows instructing AI assistants—specifically [Goose](../resources/goose.md) or Claude Desktop—how to execute Agentic AI Foundation community operations using AAIF templates, Google Drive folders, Slack workspaces, and Luma calendars [^evt-community-events-file-b33563055168-23a10754]. The toolkit executes administrative, content generation, and chapter lifecycle tasks via plain-English instructions without requiring command-line programming from organizers [^evt-community-events-file-b33563055168-23a10754].

# Architecture / Specification
The toolkit coordinates multiple specialized operational routines across three primary capability domains [^evt-community-events-file-b33563055168-23a10754]:
- **Event Communications and Copywriting**: Drafts launch announcements, Luma descriptions, six-slide LinkedIn carousel narratives, speaker invitations, speaker bios, day-of-event presentation slides, RSVP attendee reminders, and post-event recaps. Attendee-facing communications automatically enforce compliance by embedding AAIF [Code of Conduct](../policies/code-of-conduct.md) and Privacy Policy disclosures [^evt-community-events-file-b33563055168-23a10754].
- **Event Planning and Milestone Tracking**: Schedules chapter events in Google Drive Event Trackers, auto-calculates backward milestone due dates based on the event target date, reschedules cascading tasks upon date revisions, and aggregates RSVP counts and overdue tasks without mutating upstream systems [^evt-community-events-file-b33563055168-23a10754].
- **Chapter Provisioning and Estate Management**: Reviews pending community intake queues, audits data hygiene (normalizing capitalization, LinkedIn profile formats, and city records), executes full estate synchronization (`aaif-sync`) auditing Drive, Slack, and Luma assets, and handles automated chapter or online series provisioning via template cloning [^evt-community-events-file-b33563055168-23a10754].

# Lifecycle and Safeguards
The toolkit operates under a strict [Human-Approval Gate](../patterns/human-approval-gate.md) paradigm to guarantee operational safety [^evt-community-events-file-b33563055168-23a10754]:
- **Approval Checkpoints**: The assistant must explicitly confirm with the operator before executing changes that mutate public state or affect external stakeholders [^evt-community-events-file-b33563055168-23a10754].
- **Intake Triage Boundary**: While the toolkit aggregates applicant summaries and drafts responses, admissions and acceptance decisions remain strictly with authorized human organizers [^evt-community-events-file-b33563055168-23a10754].
- **Read-Only Inspection**: Health auditing routines (such as Slack topology checks and RSVP status reports) execute purely read-only data extraction [^evt-community-events-file-b33563055168-23a10754].

[^evt-community-events-file-b33563055168-23a10754]: https://github.com/aaif/community-events/blob/f46c3425e92d63c336889819e21e8af88cc4abff/README.md
