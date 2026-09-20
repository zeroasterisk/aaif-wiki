---
type: specification
title: Workflow Pattern
description: An independently adoptable solution to a recurring workflow sub-problem,
  defined by its invariants, failure modes, and implementation approaches.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/TEMPLATE.md
tags:
- pattern
- workflow
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-flash-latest
  at: '2026-09-20T17:48:22.618496+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/TEMPLATE.md
  author: Zayne Turner
  last_modified: '2026-08-05T23:05:12-04:00'
- id: evt-wg-workflows-and-process-integration-pr-20
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/20
  author: zaynelt
  last_modified: '2026-08-06T03:05:13+00:00'
---

# Overview

A Workflow Pattern is an independently adoptable solution addressing a recurring sub-problem within agentic workflows [^evt-wg-workflows-and-process-integration-file-f035520d0488-6fefbf62]. Patterns are context-free, focusing on the shape of the solution rather than specific deployment stories, product names, or use-case specifics [^evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054]. Reference architectures compose multiple patterns.

# Specification

A pattern document must define the problem it solves, why that problem is difficult, and the abstract solution shape (ideally 2–4 boxes). Key components of a pattern specification include:

1.  **Invariants**: Properties that any implementation must guarantee, written such that they hold regardless of the specific product or mechanism used.
2.  **Failure Modes**: Concrete descriptions of what breaks if the invariants are violated.
3.  **Implementation Approaches**: Illustrative examples of documented mechanisms, distinguishing what the runtime provides versus what the implementation must add to satisfy the invariants [^evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054].

Patterns may also document known uses outside of agentic AI to demonstrate that the shape is discovered, not invented, and to highlight the delta introduced by agentic workflows [^evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054].

[^evt-wg-workflows-and-process-integration-file-0f939e51d343-befb4054]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/patterns/TEMPLATE.md
