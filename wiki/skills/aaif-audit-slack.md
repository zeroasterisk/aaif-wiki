---
type: skill
title: AAIF Slack Audit Skill
description: Read-only Slack workspace inspection skill auditing channel topology,
  organizer presence, member demographics, and spam patterns as phase 8 of community
  estate sync.
resource: https://github.com/aaif/community-events/blob/a411604181e6a15dc2278221bc7501c8bb3c49fc/skills/aaif-audit-slack/SKILL.md
tags:
- community
- slack
- audit
- operations
- skills
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:31:50.972026+00:00'
sources:
- id: evt-community-events-file-91886a9e0653-92673e4e
  resource: https://github.com/aaif/community-events/blob/a411604181e6a15dc2278221bc7501c8bb3c49fc/skills/aaif-audit-slack/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-11-01T11:56:54-08:00'
---

# Overview
The `aaif-audit-slack` skill is a read-only community inspection procedure that evaluates an AAIF Slack workspace's health, chapter channel coverage, organizer memberships, subject-matter topic activity, and member roster composition [^evt-community-events-file-91886a9e0653-92673e4e]. It operates as phase 8 of the community estate synchronization pipeline orchestrated by [aaif-sync](../skills/aaif-sync.md), providing an independent validation layer executed through a separate code path from the estate mutation scripts [^evt-community-events-file-91886a9e0653-92673e4e].

# Architecture / Specification
The audit architecture executes three core reporting engines over the workspace alongside a shared activity measurement layer and an on-demand spam detection utility [^evt-community-events-file-91886a9e0653-92673e4e]:

- **Organizers Audit (`audit_organizers.py`):** Verifies that every local chapter has designated public and private `-organizers` channels and confirms that accepted organizers are present in their corresponding chapter channels [^evt-community-events-file-91886a9e0653-92673e4e].
- **Topics Audit (`audit_topics.py`):** Inspects subject-matter discussion rooms to identify stale, quiet, or overlapping channels and verify discoverability for newcomers [^evt-community-events-file-91886a9e0653-92673e4e].
- **Members Audit (`audit_members.py`):** Analyzes the overall workspace structure, user accounts, and newcomer onboarding experience [^evt-community-events-file-91886a9e0653-92673e4e].
- **Activity Measurement (`audit_activity.py`):** Captures operational telemetry including timestamp of the last human message, historical message volume, and distinct active posters per channel to feed topic and member analyses [^evt-community-events-file-91886a9e0653-92673e4e].
- **On-Demand Spam Scanner (`audit_spam.py`):** Scans public channels, message threads, and fixed phrase searches across visible direct messages for promotional pitches, partnership solicitations, or credential rentals, outputting leads strictly to terminal output without automated mutation [^evt-community-events-file-91886a9e0653-92673e4e].
- **Report Aggregation (`summarize_audits.py`):** Compiles findings into a consolidated single-page HTML report indexing the four audit dimensions with a ranked priority list of remediation actions [^evt-community-events-file-91886a9e0653-92673e4e].

Operational invariants enforce read-only execution: all discrepancy findings must be resolved at their primary data sources—such as [aaif-clean-data](../skills/aaif-clean-data.md) or chapter registration sheets—prior to re-running the sync pipeline [^evt-community-events-file-91886a9e0653-92673e4e]. Workspace files and exports must be processed using Python and the Google Workspace CLI (`gws`) interacting with native cloud document APIs, prohibiting desktop office software like LibreOffice from modifying or converting templates [^evt-community-events-file-91886a9e0653-92673e4e].

# References
- [Community Event Operations](../skills/community-event-operations.md)
- [AAIF Estate Synchronization](../skills/aaif-sync.md)
- [AAIF Data Cleaning](../skills/aaif-clean-data.md)

[^evt-community-events-file-91886a9e0653-92673e4e]: https://github.com/aaif/community-events/blob/a411604181e6a15dc2278221bc7501c8bb3c49fc/skills/aaif-audit-slack/SKILL.md
