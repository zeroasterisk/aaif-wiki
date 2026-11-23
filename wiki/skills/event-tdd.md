---
type: skill
title: Event Test-Driven Development
description: Procedural agent skill enforcing a red-green-refactor loop to verify
  event functionality across domain, API, MCP, and agent seams.
resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/event-tdd/SKILL.md
tags:
- skill
- testing
- tdd
- aaif-dallas
- software-engineering
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:40:02.549783+00:00'
sources:
- id: evt-aaif-dallas-community-file-fb3c2f0e279b-737452f2
  resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/event-tdd/SKILL.md
  author: Govindaraj Palanisamy
  last_modified: '2026-11-22T22:32:04-06:00'
---

# Overview
The `event-tdd` skill guides agents and engineers through a red-green-refactor workflow to verify community event behaviors across public, observable seams[^evt-aaif-dallas-community-file-fb3c2f0e279b-737452f2]. Rather than coupling tests to internal implementation details, prompts, or database schemas, the skill prioritizes verification at the highest observable abstraction level agreed upon with human operators[^evt-aaif-dallas-community-file-fb3c2f0e279b-737452f2].

# Architecture / Specification
The skill defines testing seams, core operational rules, and glossary-driven naming patterns for test-driven development[^evt-aaif-dallas-community-file-fb3c2f0e279b-737452f2].

## Verification Seams
Before authoring tests, agents confirm public observation seams with operators, selecting from[^evt-aaif-dallas-community-file-fb3c2f0e279b-737452f2]:
- **Domain and Use-Case Logic**: Scenarios validating event domain invariants without transport overhead (complementing `../skills/event-domain-modeling.md`).
- **HTTP API Contracts**: End-to-end HTTP request and typed response validation (aligning with `../skills/event-api-contracts.md`).
- **Frontend User Interactions**: Interface behavior tested against controlled adapters.
- **MCP Tool Invocation**: Tool execution exercised directly through a running Model Context Protocol server.
- **Agent Behavior Graders**: Evaluations measuring observable agent tool calls, argument validity, and terminal outcomes.
- **Production-Like Integration Slices**: Transactional state persistence and schema migration validation.

## Operational Rules
1. Write a single failing behavioral test first[^evt-aaif-dallas-community-file-fb3c2f0e279b-737452f2].
2. Author the minimal production code needed to satisfy the test[^evt-aaif-dallas-community-file-fb3c2f0e279b-737452f2].
3. Iterate to the next independently valuable behavior[^evt-aaif-dallas-community-file-fb3c2f0e279b-737452f2].
4. Refactor only after achieving green tests, never during behavior implementation[^evt-aaif-dallas-community-file-fb3c2f0e279b-737452f2].
5. Compare outputs against independent sources of truth[^evt-aaif-dallas-community-file-fb3c2f0e279b-737452f2].
6. Avoid asserting private function invocations, database table structures, or prompt phrasing when public outcomes can be evaluated[^evt-aaif-dallas-community-file-fb3c2f0e279b-737452f2].
7. Mock external system boundaries only, preserving domain validation rules[^evt-aaif-dallas-community-file-fb3c2f0e279b-737452f2].
8. Cover authorization gates, input boundaries, idempotency/retry handling, and user-facing error modes on external interfaces[^evt-aaif-dallas-community-file-fb3c2f0e279b-737452f2].

## Naming and Execution
Tests use domain glossary phrasing (for example, verifying attendee registration, retry idempotency, or organizer cancellation workflows)[^evt-aaif-dallas-community-file-fb3c2f0e279b-737452f2]. Agents execute the minimal relevant test target after each loop and run the full test suite before handing off for code review (coordinating with `../skills/fullstack-event-delivery.md` and `../skills/event-review.md`)[^evt-aaif-dallas-community-file-fb3c2f0e279b-737452f2].

# Lifecycle History
- Introduced as an authoritative operational skill in `aaif-dallas-community` via `.github/skills/event-tdd/SKILL.md`[^evt-aaif-dallas-community-file-fb3c2f0e279b-737452f2].

[^evt-aaif-dallas-community-file-fb3c2f0e279b-737452f2]: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/event-tdd/SKILL.md
