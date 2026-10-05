---
type: policy
title: Community Chapter Lifecycle Policy
description: Governance policy and operational procedure for provisioning, rebranding,
  renaming, and maintaining community chapters.
resource: https://github.com/aaif/community-events/pull/55
tags:
- policies
- governance
- community
- chapters
- operations
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:25:43.661013+00:00'
sources:
- id: evt-community-events-pr-55
  resource: https://github.com/aaif/community-events/pull/55
  author: rparundekar
  last_modified: '2026-10-01T23:11:19+00:00'
---

# Overview
The Community Chapter Lifecycle Policy governs the establishment, maintenance, renaming, deprecation, and merger of regional AAIF community chapters.[^evt-community-events-pr-55] Chapter rosters and metadata are managed via deterministic synchronization tooling that enforces strict retention guarantees.[^evt-community-events-pr-55]

# Architecture / Specification
### Synchronization & Row Retention Rules
Automated chapter synchronization tooling operates under a non-destructive lifecycle contract:[^evt-community-events-pr-55]
- **Zero Automated Deletion:** Synchronization scripts must never automatically clear or delete a chapter row from the active registry.[^evt-community-events-pr-55]
- **Retirement Candidates:** When a chapter lacks a qualifying active organizer, automated sync flags the entry as a retirement candidate on the operational Drift reporting tab without altering exit codes or executing automated writes.[^evt-community-events-pr-55]
- **Human Lifecycle Transitions:** Chapter retirement requires explicit operator action to set `Status=Deprecated` or `Status=Merged` along with specifying the target `Merged Into` chapter.[^evt-community-events-pr-55]
- **Metadata Preservation:** Hand-written historical documentation, operational notes, and summaries are preserved across renames and organizer changes.[^evt-community-events-pr-55]

# References
- Governed by [community-event-operations](../guidelines/community-event-operations.md).
- Implemented within the community automation toolchain.

[^evt-community-events-pr-55]: https://github.com/aaif/community-events/pull/55
