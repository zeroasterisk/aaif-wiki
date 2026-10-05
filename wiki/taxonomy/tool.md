---
type: taxonomy
title: Tool
description: Universal taxonomy term defining an external function, API, or service
  an agent may call to retrieve data or perform an action.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/87
tags:
- taxonomy
- tools
- runtime
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:26:32.273472+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-87
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/87
  author: julianna-ciq
  last_modified: '2026-10-02T10:00:02+00:00'
---

# Overview
In AAIF terminology, a **Tool** is an external function, API, or service that an AI agent may call to retrieve data or perform an action within an execution environment [^evt-ws-taxonomy-landscape-pr-87].

# Architecture / Specification
Within the Agentic AI Foundation taxonomy schema, a Tool is classified as an external capability interface [^evt-ws-taxonomy-landscape-pr-87]:
- **Interface Contract**: Exposes deterministic schemas detailing input parameters and return types (such as OpenAPI schemas or Model Context Protocol tool declarations).
- **Contrasts with Skill**: While a Tool is an external execution mechanism or invocation endpoint, a Skill (such as packaging standardized under [Agent Skills](../proposals/agent-skills.md)) encapsulates procedural instructions, context, execution scripts, and metadata enabling an agent to achieve a high-level objective [^evt-ws-taxonomy-landscape-pr-87].
- **Supply Chain Security**: Tool definitions and external dependencies fall under the governance and verification practices outlined in [Agent Tool Supply Chain Terms](../taxonomy/agent-tool-supply-chain-terms.md).

# Lifecycle History
- Introduced in the Taxonomy and Landscape workstream via PR #87 to establish universal terminology across AAIF specifications [^evt-ws-taxonomy-landscape-pr-87].

[^evt-ws-taxonomy-landscape-pr-87]: https://github.com/aaif/ws-taxonomy-landscape/pull/87
