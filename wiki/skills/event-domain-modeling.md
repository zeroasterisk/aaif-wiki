---
type: skill
title: Event Domain Modeling
description: Procedural agent skill guiding event-management domain modeling, lifecycle
  transitions, registration invariants, and architecture decisions.
resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/event-domain-modeling/SKILL.md
tags:
- skill
- events
- domain-modeling
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:38:13.279200+00:00'
sources:
- id: evt-aaif-dallas-community-file-1fe3ce7fd6b7-ca482786
  resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/event-domain-modeling/SKILL.md
  author: Govindaraj Palanisamy
  last_modified: '2026-11-22T22:32:04-06:00'
- id: evt-aaif-dallas-community-file-1a18650fe092-ea310fad
  resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/docs/adr/0001-static-first-event-site.md
  author: Govindaraj Palanisamy
  last_modified: '2026-11-22T22:32:04-06:00'
---

# Overview
Event Domain Modeling is a procedural agent skill governing technical event domain models, entity glossaries, lifecycle transitions, and architecture trade-offs for AAIF community initiatives [^evt-aaif-dallas-community-file-1fe3ce7fd6b7-ca482786]. Established within the AAIF Dallas community infrastructure, it formalizes domain boundaries, registration constraints, and operational invariants for agent-assisted community event management [^evt-aaif-dallas-community-file-1fe3ce7fd6b7-ca482786] [^evt-aaif-dallas-community-file-1a18650fe092-ea310fad].

# Architecture / Specification
The skill establishes strict procedural gates when reviewing or updating event management software, data schemas, and agent interactions [^evt-aaif-dallas-community-file-1fe3ce7fd6b7-ca482786]:

- **Terminology Harmonization**: Mandates strict disambiguation between conflicting entity concepts (e.g., separating member, user, attendee, and presenter identities) and synchronization with canonical domain glossaries [^evt-aaif-dallas-community-file-1fe3ce7fd6b7-ca482786].
- **Edge Scenario Verification**: Instructs agents to challenge ambiguous requirements against failure modes, including publishing incomplete event records, cancellations with active registrations, capacity exhaustion, overlapping session schedules, and Model Context Protocol (MCP) tool retries [^evt-aaif-dallas-community-file-1fe3ce7fd6b7-ca482786].
- **Architecture Decision Rigor**: Prompts an Architecture Decision Record (ADR) whenever non-obvious operational or architectural trade-offs emerge, such as prioritizing static-first web generation over mutable runtime APIs to minimize operational attack surface and isolate attendee registration data [^evt-aaif-dallas-community-file-1fe3ce7fd6b7-ca482786] [^evt-aaif-dallas-community-file-1a18650fe092-ea310fad].

## Domain Invariants
The skill codifies core invariants that agentic and human workflows cannot violate [^evt-aaif-dallas-community-file-1fe3ce7fd6b7-ca482786]:
1. Public registrations are accepted only for published community events [^evt-aaif-dallas-community-file-1fe3ce7fd6b7-ca482786].
2. An attendee may hold at most one active registration per community event [^evt-aaif-dallas-community-file-1fe3ce7fd6b7-ca482786].
3. Session schedules must remain bounded within the parent community event time window [^evt-aaif-dallas-community-file-1fe3ce7fd6b7-ca482786].
4. Cancellations must preserve immutable audit records [^evt-aaif-dallas-community-file-1fe3ce7fd6b7-ca482786].
5. Organizer modifications require explicit authorization gates [^evt-aaif-dallas-community-file-1fe3ce7fd6b7-ca482786].
6. Agent and MCP actions must never bypass domain validation logic [^evt-aaif-dallas-community-file-1fe3ce7fd6b7-ca482786].

# Lifecycle History
The skill was established in the AAIF Dallas community repository alongside ADR 0001, defining operational boundaries for the Dallas Agentic AI Summit web platform [^evt-aaif-dallas-community-file-1fe3ce7fd6b7-ca482786] [^evt-aaif-dallas-community-file-1a18650fe092-ea310fad].

# References
- [AAIF Dallas Community Repository](https://github.com/aaif/aaif-dallas-community) [^evt-aaif-dallas-community-file-1fe3ce7fd6b7-ca482786]

[^evt-aaif-dallas-community-file-1a18650fe092-ea310fad]: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/docs/adr/0001-static-first-event-site.md
[^evt-aaif-dallas-community-file-1fe3ce7fd6b7-ca482786]: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/event-domain-modeling/SKILL.md
