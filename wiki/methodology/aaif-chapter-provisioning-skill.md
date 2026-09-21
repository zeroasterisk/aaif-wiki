---
type: methodology
title: AAIF Chapter Provisioning Skill
description: Automated methodology for provisioning chapters, synchronizing intake
  decisions, and enforcing report-first write gates across community records.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-sync-chapters/references/completed-migrations.md
tags:
- ops
- automation
- chapters
- migrations
- write-gates
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:14:44.022779+00:00'
sources:
- id: evt-community-events-file-3fa41791e6fd-adb85036
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-sync-chapters/references/completed-migrations.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T22:07:16-07:00'
- id: evt-community-events-file-729b1652037d-3b77c603
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/sync-chapters-write-gate/prompt.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:52:16-07:00'
---

# Overview

The AAIF Chapter Provisioning Skill defines the operational methodology and automation tooling used to provision regional chapters, synchronize approved organizers from intake queues to the Chapters List, and manage estate migrations under report-first write gates [^evt-community-events-file-729b1652037d-3b77c603][^evt-community-events-file-3fa41791e6fd-adb85036].

# Architecture / Specification

The skill and associated synchronization scripts enforce deterministic execution and data hygiene through explicit architectural constraints:

- **Report-First Write Gate**: Scripts and skill executions default to non-mutating reporting mode, generating diffs and verification summaries before applying changes only when explicitly passed the `--write` flag [^evt-community-events-file-729b1652037d-3b77c603][^evt-community-events-file-3fa41791e6fd-adb85036].
- **Resource Column Schema**: Resource identifiers (such as public, organizer, and regional channel handles) are synchronized and maintained directly within dedicated spreadsheet columns rather than detached local JSON maps [^evt-community-events-file-3fa41791e6fd-adb85036].
- **Status Progression**: Standardized intake status transitions (such as retiring legacy `New` status values in favor of `Prospect` and explicit intake decisions) ensure schema consistency across all chapter records [^evt-community-events-file-3fa41791e6fd-adb85036].

# Lifecycle History

- **Resource Column Migration**: Executed `migrate_resource_columns.py` moving channel mappings and Slack configuration directly onto the spreadsheet estate and deprecating standalone `channel_map.json` [^evt-community-events-file-3fa41791e6fd-adb85036].
- **Status Lifecycle Refinement**: Deployed `migrate_status_prospect.py` to migrate legacy `New` intake statuses to `Prospect` [^evt-community-events-file-3fa41791e6fd-adb85036].
- **Write-Gate Evaluation**: Added automated evaluation cases verifying that synchronization tasks generate reports before executing write operations [^evt-community-events-file-729b1652037d-3b77c603].

[^evt-community-events-file-3fa41791e6fd-adb85036]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/skills/aaif-sync-chapters/references/completed-migrations.md
[^evt-community-events-file-729b1652037d-3b77c603]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/sync-chapters-write-gate/prompt.md
