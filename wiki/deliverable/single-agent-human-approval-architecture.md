---
type: deliverable
title: Single Agent Human Approval Architecture
description: A reference architecture for workflows where an agent prepares an action,
  a named human approves or rejects it, and the agent executes the approved action.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/50
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-flash-latest
  at: '2026-09-20T18:08:49.080313+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-50
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/50
  author: mzagar
  last_modified: '2026-09-17T06:34:37+00:00'
---

# Overview
The Single Agent Human Approval Architecture defines a workflow pattern where an agent prepares a proposal for action, a named human must explicitly approve or reject the proposal, and the agent executes the approved action. This pattern is a realization of the [human-approval-gate](../specification/human-approval-gate.md) and [proposal-execution-split](../specification/proposal-execution-split.md) specifications.

The overall end-to-end request admitted to the agent execution run is defined as the [business-task](../taxonomy/business-task.md). The steps the agent takes to fulfill this request are defined as [activities](../taxonomy/activity.md) [^evt-wg-workflows-and-process-integration-pr-50].

# Architecture / Specification
(Content omitted for brevity)

# Lifecycle History
(Content omitted for brevity)

[^evt-wg-workflows-and-process-integration-pr-50]: https://github.com/aaif/wg-workflows-and-process-integration/pull/50
