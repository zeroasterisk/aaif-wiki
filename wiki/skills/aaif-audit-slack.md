---
type: skill
title: AAIF Audit Slack Skill
description: Read-only inspection skill auditing community Slack workspace coverage,
  organizer membership, topic channel vitality, and member spam as phase 8 of the
  estate sync.
resource: https://github.com/aaif/community-events/blob/a411604181e6a15dc2278221bc7501c8bb3c49fc/skills/aaif-audit-slack/SKILL.md
tags:
- community
- slack
- operations
- audit
- pipeline
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:32:51.084396+00:00'
sources:
- id: evt-community-events-file-91886a9e0653-92673e4e
  resource: https://github.com/aaif/community-events/blob/a411604181e6a15dc2278221bc7501c8bb3c49fc/skills/aaif-audit-slack/SKILL.md
  author: Rahul Parundekar
  last_modified: '2026-11-01T11:56:54-08:00'
---

# Overview

The `aaif-audit-slack` skill is a read-only audit engine and independent verification check operating as phase 8 of the AAIF community estate sync pipeline (`../skills/aaif-sync.md`) [^evt-community-events-file-91886a9e0653-92673e4e]. It verifies whether chapters have designated public and organizer channels, confirms that approved organizers occupy appropriate channels, assesses channel clutter and newcomer experience, and generates an integrated HTML diagnostic report [^evt-community-events-file-91886a9e0653-92673e4e].

In accordance with operational hygiene rules, the skill executes from an isolated code path separate from the write engines, adhering to the principle that generation filters cannot validate their own output [^evt-community-events-file-91886a9e0653-92673e4e]. Findings must be remediated at the source (e.g., via `../skills/aaif-clean-data.md`) and verified by re-running the sync pipeline [^evt-community-events-file-91886a9e0653-92673e4e].

# Architecture / Specification

The skill structures workspace auditing across three core reports, a shared measurement layer, an on-demand spam scanner, and a single consolidated HTML deliverable [^evt-community-events-file-91886a9e0653-92673e4e]:

| Report / Component | Script | Function | Execution Model |
|---|---|---|---|
| Organizers Report | `audit_organizers.py` | Verifies channel presence for every chapter and validates accepted organizer memberships | Phase 8 sync pipeline |
| Topics Report | `audit_topics.py` | Evaluates activity, discoverability, and overlap across subject-matter channels | Phase 8 sync pipeline |
| Members Report | `audit_members.py` | Analyzes workspace accessibility, roster composition, and headline counts | Phase 8 sync pipeline |
| Activity Layer | `audit_activity.py` | Measures human message volumes, latest human message timestamps, and distinct posters | Feeds Topics & Members reports |
| Spam Inspection | `audit_spam.py` | Detects solicitations, account rentals, and multi-channel message blasts across public threads and token-visible scopes; exits with code 2 on partial lead lists (`INCOMPLETE:`) | On-demand script (manual triage) |
| Deliverable Engine | `summarize_audits.py` | Compiles an interactive HTML report containing indexed audit sections and a prioritized remediation TL;DR | Pipeline completion output |

### Tooling Invariants

The audit skill strictly enforces Google Workspace environment rules: all Google Drive interactions must pass through the `gws` CLI driven via Python [^evt-community-events-file-91886a9e0653-92673e4e]. Native Docs, Sheets, and Slides APIs are mandatory for editing Google Apps documents, and byte-level OOXML surgery is reserved strictly for non-native files [^evt-community-events-file-91886a9e0653-92673e4e]. Desktop office suites such as LibreOffice, `soffice`, or `unoconv` are strictly prohibited to prevent font substitution, tab stripping, and OOXML schema corruption [^evt-community-events-file-91886a9e0653-92673e4e].

[^evt-community-events-file-91886a9e0653-92673e4e]: https://github.com/aaif/community-events/blob/a411604181e6a15dc2278221bc7501c8bb3c49fc/skills/aaif-audit-slack/SKILL.md
