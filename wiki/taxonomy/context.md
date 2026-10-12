---
type: taxonomy
title: Context
description: Universal taxonomy term defining the information assembled and available
  to an agent when making a decision during an execution step.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/82
tags:
- taxonomy
- execution
- agent-architecture
- context
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:09:38.057750+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-82
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/82
  author: julianna-ciq
  last_modified: '2026-09-29T11:33:39+00:00'
---

# Overview
Context is the information available to an agent when making a decision during an execution step [^evt-ws-taxonomy-landscape-pr-82]. Within the Agentic AI Foundation taxonomy schema, context represents the assembled operational view presented to a model, encompassing incoming user messages, execution results from tools, retrieved external documentation, short- or long-term memory records, and system instructions configuring agent boundaries [^evt-ws-taxonomy-landscape-pr-82].

# Architecture / Specification
Context functions as the bounded runtime information payload supplied to an agent at a given turn [^evt-ws-taxonomy-landscape-pr-82]. Under the taxonomy definition, the scope of context covers:
- User messages and direct input directives (see `../taxonomy/prompt.md`).
- System prompts, policies, and behavioral instructions configuring agent governance.
- Tool invocation outputs, API responses, and observation feedback (see `../taxonomy/tool.md`).
- Retrieved knowledge artifacts, database records, and persistent memory segments.

Related terms within the AAIF taxonomy include context assembly, context exhaustion, context propagation across system boundaries, memory access, and information retrieval [^evt-ws-taxonomy-landscape-pr-82].

# Lifecycle History
Proposed as an open universal taxonomy entry in `ws-taxonomy-landscape` PR #82, bringing the taxonomy schema inventory to 38 entries and passing validation test suites [^evt-ws-taxonomy-landscape-pr-82].

[^evt-ws-taxonomy-landscape-pr-82]: https://github.com/aaif/ws-taxonomy-landscape/pull/82
