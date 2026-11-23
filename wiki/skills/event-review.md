---
type: skill
title: Event Change Review Skill
description: Procedural agent skill independently reviewing event-management code
  changes against engineering standards and originating issue specifications.
resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/event-review/SKILL.md
tags:
- skills
- event-management
- review
- code-quality
- copilot
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:39:37.899959+00:00'
sources:
- id: evt-aaif-dallas-community-file-cfb0e91cc971-992f230f
  resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/event-review/SKILL.md
  author: Govindaraj Palanisamy
  last_modified: '2026-11-22T22:32:04-06:00'
- id: evt-aaif-dallas-community-file-a54ff182c7e8-97bf5d62
  resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/AGENTS.md
  author: Govindaraj Palanisamy
  last_modified: '2026-11-22T22:32:04-06:00'
- id: evt-aaif-dallas-community-file-b33563055168-618b63aa
  resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/README.md
  author: Govindaraj Palanisamy
  last_modified: '2026-11-22T22:32:04-06:00'
---

# Overview
`event-review` is a maintainer and verification agent skill that evaluates AAIF Dallas pull requests and commits against documented engineering standards and originating feature specifications[^evt-aaif-dallas-community-file-cfb0e91cc971-992f230f][^evt-aaif-dallas-community-file-a54ff182c7e8-97bf5d62]. It separates findings into two distinct evaluation axes—the Standards axis and the Specification axis—to detect security vulnerabilities, logic bypasses, and scope discrepancies before changes are integrated[^evt-aaif-dallas-community-file-cfb0e91cc971-992f230f].

# Architecture / Specification
The skill operates as a verification gate executed prior to declaring full-stack delivery complete[^evt-aaif-dallas-community-file-a54ff182c7e8-97bf5d62][^evt-aaif-dallas-community-file-cfb0e91cc971-992f230f]:

### Review Axes
1. **Standards Axis**: Audits code for architectural hygiene, operational safety, and defensive engineering practices[^evt-aaif-dallas-community-file-cfb0e91cc971-992f230f]:
   - Detection of duplicated lifecycle logic across interface adapters.
   - Prevention of unauthorized access or validation bypasses across UI, API, MCP, and agent boundaries.
   - Protection against leaking secrets or sensitive attendee data into logs, traces, prompts, or serialized responses.
   - Identification of schema drift between transport layers and domain behaviors.
   - Mitigation of implementation-coupled test patterns, speculative abstractions, missing idempotency, or lost registration histories.
2. **Specification Axis**: Evaluates the change against the originating GitHub issue or specification[^evt-aaif-dallas-community-file-cfb0e91cc971-992f230f]:
   - Missing or partially implemented requirements.
   - Unrequested behavior or out-of-scope implementations.
   - Semantically incorrect behavior despite passing syntactical tests.
   - Acceptance criteria lacking test coverage.

### Operational Workflow
- The reviewer requires a fixed commit, branch, or merge-base reference and confirms the diff is non-empty[^evt-aaif-dallas-community-file-cfb0e91cc971-992f230f].
- Mechanical issues enforced by the existing compiler and linting toolchain are explicitly bypassed[^evt-aaif-dallas-community-file-cfb0e91cc971-992f230f].
- Output reports cite specific file paths and line numbers alongside violated requirements, summarizing the total finding count and highest-severity risk for each axis[^evt-aaif-dallas-community-file-cfb0e91cc971-992f230f].

# Lifecycle History
- **Merged Skill Specification**: Standardized in `aaif/aaif-dallas-community` at `.github/skills/event-review/SKILL.md` as the final quality gate in the agentic development workflow[^evt-aaif-dallas-community-file-cfb0e91cc971-992f230f][^evt-aaif-dallas-community-file-b33563055168-618b63aa].

[^evt-aaif-dallas-community-file-a54ff182c7e8-97bf5d62]: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/AGENTS.md
[^evt-aaif-dallas-community-file-b33563055168-618b63aa]: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/README.md
[^evt-aaif-dallas-community-file-cfb0e91cc971-992f230f]: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/event-review/SKILL.md
