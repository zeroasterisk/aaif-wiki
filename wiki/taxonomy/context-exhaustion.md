---
type: taxonomy
title: Context Exhaustion
description: Universal taxonomy term defining the session failure mode where task-required
  information exceeds model context window capacity.
resource: https://github.com/aaif/ws-taxonomy-landscape/issues/46
tags:
- taxonomy
- context
- failure-modes
- memory
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:17:10.786573+00:00'
sources:
- id: evt-ws-taxonomy-landscape-issue-46
  resource: https://github.com/aaif/ws-taxonomy-landscape/issues/46
  author: asish-singh
  last_modified: '2026-08-22T12:07:57+00:00'
---

# Overview

Context exhaustion is the failure mode in which the information an agent needs for its current task no longer fits within the model's context window at the same time, because accumulated content has reached the window's capacity [^evt-ws-taxonomy-landscape-issue-46].

The primary discriminator of context exhaustion is that required information is displaced specifically by window capacity limits, distinguishing it from adjacent operational conditions [^evt-ws-taxonomy-landscape-issue-46]:
- **Populated context**: A large or heavily populated context window that still accommodates all task-relevant information is not exhausted [^evt-ws-taxonomy-landscape-issue-46].
- **Degraded attention**: Attention degradation across an expansive but non-overflowed context represents an attention quality defect rather than exhaustion [^evt-ws-taxonomy-landscape-issue-46].
- **Retrieval failure**: Failure to retrieve or load relevant information into context represents an upstream retrieval defect rather than exhaustion [^evt-ws-taxonomy-landscape-issue-46].

Context exhaustion specifically identifies the condition where window capacity itself prevents the agent from observing required task information [^evt-ws-taxonomy-landscape-issue-46].

# Architecture / Specification

Context exhaustion is a runtime property of an execution session rather than an intrinsic characteristic of a model [^evt-ws-taxonomy-landscape-issue-46].

Common engineering mitigations—such as context summarization, external vector memory retrieval, and task decomposition across [taxonomy/subagent](../taxonomy/subagent.md) boundaries—do not prevent exhaustion; rather, they trade hard capacity exhaustion for lossy compression, shifting observable operational failures into compression and retrieval artifacts [^evt-ws-taxonomy-landscape-issue-46].

### Taxonomic Relationships
- **Related Terms**: `Session`, `Harness` [^evt-ws-taxonomy-landscape-issue-46]
- **Core Dependencies**: Directly relates to [taxonomy/context](../taxonomy/context.md) and task partitioning under [taxonomy/subagent](../taxonomy/subagent.md)

[^evt-ws-taxonomy-landscape-issue-46]: https://github.com/aaif/ws-taxonomy-landscape/issues/46
