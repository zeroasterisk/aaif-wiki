---
type: taxonomy
title: Workflow Primitives
description: Core vocabulary and execution primitives standardizing structured multi-activity
  work, coordination flows, and determinism boundaries.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/40
tags:
- taxonomy
- workflow
- orchestration
- primitives
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:18:43.513324+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-40
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/40
  author: chaksaray
  last_modified: '2026-09-08T17:48:26+00:00'
---

# Overview

Workflow Primitives provide foundational definitions for orchestrating agent activities, coordinating control flow, and classifying execution state transitions across multi-step processes [^evt-wg-workflows-and-process-integration-pr-40].

# Architecture / Specification

### Core Primitives
- **Determinism**: Evaluated as a scoped property of a discrete layer—Workflow Execution, Control Flow, or an individual Activity—rather than an invariant across an entire end-to-end workflow [^evt-wg-workflows-and-process-integration-pr-40]. A workflow can retain deterministic control flow logic while orchestrating non-deterministic language model activities [^evt-wg-workflows-and-process-integration-pr-40].
- **Control Flow**: The structural ordering, branching, and joining logic governing execution sequences [^evt-wg-workflows-and-process-integration-pr-40]. Control flow definitions are agnostic to whether transitions are static design-time paths or dynamically determined at runtime by an agent orchestrator [^evt-wg-workflows-and-process-integration-pr-40].
- **Workflow Execution**: An instantiated lifecycle execution that retains continuity across mid-execution replanning, retries, and dynamic plan alterations [^evt-wg-workflows-and-process-integration-pr-40].
- **Handoff**: The transfer of execution responsibility or context across agents, tools, or human boundaries [^evt-wg-workflows-and-process-integration-pr-40]. Handoff captures both the responsibility transition and the observable trace boundary where transfer occurs [^evt-wg-workflows-and-process-integration-pr-40].

# References

- Layered determinism models reference factor classifications from [../resources/agentic-vulnerability-enumeration.md](../resources/agentic-vulnerability-enumeration.md) [^evt-wg-workflows-and-process-integration-pr-40].

[^evt-wg-workflows-and-process-integration-pr-40]: https://github.com/aaif/wg-workflows-and-process-integration/pull/40
