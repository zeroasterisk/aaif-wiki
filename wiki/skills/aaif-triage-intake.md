---
type: skill
title: AAIF Triage Intake
description: Operational agent skill reviewing pending community intake queues, generating
  applicant digests, and routing multi-role candidates.
resource: https://github.com/aaif/community-events/pull/59
tags:
- skill
- community-events
- intake
- triage
- operations
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:21:12.283283+00:00'
sources:
- id: evt-community-events-pr-59
  resource: https://github.com/aaif/community-events/pull/59
  author: rparundekar
  last_modified: '2026-10-09T18:08:39+00:00'
---

# Overview
AAIF Triage Intake (`skills/aaif-triage-intake`) is an operational automation skill that inspects incoming community intake form submissions, parses role applications, generates structured digests for reviewers, and routes applicants into specialized tracking sheets[^evt-community-events-pr-59]. The skill supports multi-role candidate processing across organizers, hosts, speakers, and collaborators.

The intake pipeline coordinates with underlying estate scripts to maintain state alignment between public Google Forms, central Intake Ops spreadsheets, and chapter-level records[^evt-community-events-pr-59].

# Architecture / Specification
The triage intake process operates through automated scanning, filtering, and summary generation:

- **Per-Role Question Ingestion**: Form inputs evaluate distinct Yes/No gates for each available community role (organizer, speaker, event host, and collaborator), allowing applicants to select multiple involvement avenues simultaneously[^evt-community-events-pr-59].
- **Intake Ops Synchronization**: Submissions are mapped into specific role tabs on the central Intake Ops spreadsheet (`Organizers`, `Hosts`, `Speakers`, and `Collaborators`), protected by column guards that prevent silent filter failures if question headers change[^evt-community-events-pr-59].
- **Digest Generation (`intake.py`)**: Generates periodic markdown digests summarizing pending applicants across all role categories, flagging unreviewed records and collaborator counts for maintainer review[^evt-community-events-pr-59].
- **Migration & Normalization**: Backwards-compatibility logic and migration scripts (`migrations/migrate_intake_role_gates.py`) reconcile historical single-choice entries with the per-role multi-gate schema to preserve candidate status columns without row shifting[^evt-community-events-pr-59].

[^evt-community-events-pr-59]: https://github.com/aaif/community-events/pull/59
