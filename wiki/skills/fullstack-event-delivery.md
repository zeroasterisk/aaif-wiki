---
type: skill
title: Full-Stack Event Delivery Skill
description: Procedural agent skill implementing AAIF Dallas event-management features
  as narrow, tested vertical slices across frontend, backend, APIs, MCP tools, and
  agents.
resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/fullstack-event-delivery/SKILL.md
tags:
- skills
- event-management
- fullstack
- copilot
- testing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:39:37.899959+00:00'
sources:
- id: evt-aaif-dallas-community-file-6cb8eb7b0e35-372ed90c
  resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/fullstack-event-delivery/SKILL.md
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
`fullstack-event-delivery` is an operational agent skill governing end-to-end implementation of AAIF Dallas event-management capabilities as narrow, tested vertical slices spanning user interfaces, backend logic, APIs, Model Context Protocol (MCP) tools, and autonomous agent workflows[^evt-aaif-dallas-community-file-6cb8eb7b0e35-372ed90c][^evt-aaif-dallas-community-file-b33563055168-618b63aa]. The skill enforces strict architectural boundaries to avoid speculative infrastructure, ensuring that business rules reside in shared application services rather than being duplicated across adapters or presentation layers[^evt-aaif-dallas-community-file-6cb8eb7b0e35-372ed90c][^evt-aaif-dallas-community-file-a54ff182c7e8-97bf5d62].

# Architecture / Specification
The skill operates according to vertical-slice engineering principles adapted from Matt Pocock's workflow, prioritizing complete user capabilities over horizontal layer isolation[^evt-aaif-dallas-community-file-6cb8eb7b0e35-372ed90c][^evt-aaif-dallas-community-file-b33563055168-618b63aa]:

1. **Slice Definition**: Identify the target actor, action, result, and expected failure modes prior to implementation[^evt-aaif-dallas-community-file-6cb8eb7b0e35-372ed90c].
2. **Boundary Testing**: Validate public test seams before authoring logic[^evt-aaif-dallas-community-file-6cb8eb7b0e35-372ed90c].
3. **Domain Centralization**: Encapsulate domain rules once within shared application services, preventing policy drift across frontend or transport interfaces[^evt-aaif-dallas-community-file-6cb8eb7b0e35-372ed90c].
4. **Adapter Exposure**: Surface capabilities via typed HTTP handlers and consume them from presentation components without copying domain invariants[^evt-aaif-dallas-community-file-6cb8eb7b0e35-372ed90c].
5. **Tool and Agent Integration**: Add MCP tools or agent workflows strictly when required by the specification, routing execution through identical service authorization paths[^evt-aaif-dallas-community-file-6cb8eb7b0e35-372ed90c].
6. **Verification and Review**: Run targeted and full test suites, concluding with an independent review via [`./event-review.md`](./event-review.md) against specification acceptance criteria[^evt-aaif-dallas-community-file-6cb8eb7b0e35-372ed90c].

### Architectural Boundaries
The skill defines strict component responsibilities[^evt-aaif-dallas-community-file-6cb8eb7b0e35-372ed90c]:
- **Frontend Components**: Manage presentation and local interaction state without owning lifecycle rules.
- **HTTP Handlers**: Handle protocol serialization, transport parsing, and authentication.
- **Application Services**: Encapsulate use-case orchestration and business flows.
- **Domain Modules**: Guard domain invariants and state transitions.
- **Persistence Adapters**: Execute transactions and queries without deciding product policy.
- **MCP Tools**: Function as thin, typed adapters enforcing explicit authorization and bounded inputs.
- **Agents**: Formulate plans and invoke approved tools without directly mutating underlying storage.

# Lifecycle History
- **Merged Skill Specification**: Authored and integrated into the `aaif/aaif-dallas-community` repository under `.github/skills/fullstack-event-delivery/SKILL.md` to guide engineering workflows for the static-first event platform release[^evt-aaif-dallas-community-file-6cb8eb7b0e35-372ed90c][^evt-aaif-dallas-community-file-a54ff182c7e8-97bf5d62].

[^evt-aaif-dallas-community-file-6cb8eb7b0e35-372ed90c]: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/skills/fullstack-event-delivery/SKILL.md
[^evt-aaif-dallas-community-file-a54ff182c7e8-97bf5d62]: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/AGENTS.md
[^evt-aaif-dallas-community-file-b33563055168-618b63aa]: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/README.md
