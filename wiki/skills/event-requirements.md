---
type: skill
title: Event Requirements
description: Interactive agent skill eliciting and validating AAIF Dallas event-management
  specifications, actor permissions, and architectural trade-offs prior to implementation.
resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/event-requirements/SKILL.md
tags:
- skills
- requirements
- events
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:38:49.354262+00:00'
sources:
- id: evt-aaif-dallas-community-file-47d3099d5d03-c0922d27
  resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/event-requirements/SKILL.md
  author: Govindaraj Palanisamy
  last_modified: '2026-11-22T22:32:04-06:00'
- id: evt-aaif-dallas-community-file-3f6ddafc4eae-6a744dcf
  resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/docs/agents/domain.md
  author: Govindaraj Palanisamy
  last_modified: '2026-11-22T22:32:04-06:00'
---

# Overview

`event-requirements` is an interactive agent skill used to clarify technical event-management requests, eliminate unstated assumptions, and capture canonical domain terminology and architectural decisions for the AAIF Dallas community.[^evt-aaif-dallas-community-file-47d3099d5d03-c0922d27] Executed with model invocation disabled, it guides practitioners through a structured design-tree interview to resolve decision frontiers before any code implementation begins.[^evt-aaif-dallas-community-file-47d3099d5d03-c0922d27]

# Architecture / Specification

The skill organizes requirements intake across systematic procedural phases:[^evt-aaif-dallas-community-file-47d3099d5d03-c0922d27]

- **Design Tree Interviewing**: Groups inquiries into dependent rounds, queries the active decision frontier simultaneously, and provides recommended defaults to accelerate human confirmation.[^evt-aaif-dallas-community-file-47d3099d5d03-c0922d27]
- **Core Domain Dimensions**: Evaluates primary actors (attendee, presenter, organizer, volunteer, administrator), lifecycle state transition permissions, registration and waitlist rules, check-in constraints, privacy and authorization boundaries, and target workflows governed by [Event API Contracts](../skills/event-api-contracts.md).[^evt-aaif-dallas-community-file-47d3099d5d03-c0922d27]
- **Artifact Synchronization**: Resolves ambiguous terminology using [Event Domain Modeling](../skills/event-domain-modeling.md), records canonical terms in repository glossaries, captures irreversible trade-offs in architecture decision records (ADRs), and formats final requirements into structured issue tracker entries.[^evt-aaif-dallas-community-file-47d3099d5d03-c0922d27][^evt-aaif-dallas-community-file-3f6ddafc4eae-6a744dcf]

# Lifecycle History

Established in the AAIF Dallas community repository to enforce disciplined requirements gathering and terminology alignment before changes to event automation systems.[^evt-aaif-dallas-community-file-47d3099d5d03-c0922d27]

[^evt-aaif-dallas-community-file-3f6ddafc4eae-6a744dcf]: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/docs/agents/domain.md
[^evt-aaif-dallas-community-file-47d3099d5d03-c0922d27]: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/event-requirements/SKILL.md
