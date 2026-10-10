---
type: architecture
title: Single-Agent Human Approval Architecture
description: Reference architecture establishing an enforceable human approval gate
  between an agent proposal and downstream execution.
resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/45
tags:
- architecture
- human-in-the-loop
- governance
- workflows
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:19:23.863565+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-issue-45
  resource: https://github.com/aaif/wg-workflows-and-process-integration/issues/45
  author: geemus
  last_modified: '2026-10-03T00:58:32+00:00'
---

# Overview
The Single-Agent Human Approval architecture defines an execution pattern wherein an autonomous agent produces an immutable proposal that must receive verified human authorization prior to triggering side-effecting operations.

# Architecture / Specification

## Boundary Isolation and Executor Decoupling
The architecture enforces authorization boundaries by separating proposal generation from action execution:
- **Proposal-Execution Split**: Decoupling the proposal engine from the execution handler guarantees that sensitive tools cannot execute without passing an explicit approval checkpoint [^evt-wg-workflows-and-process-integration-issue-45].
- **Durable Waits and Context Cache**: When approval involves extended delay ([../patterns/durable-wait.md](../patterns/durable-wait.md)), spawning a clean executor process avoids stale cache states while requiring minimal context reconstruction [^evt-wg-workflows-and-process-integration-issue-45].
- **Critique Separation**: Multi-session separation allows independent verification or critique workflows prior to human sign-off [^evt-wg-workflows-and-process-integration-issue-45].

# Lifecycle History
- Draft reference architecture established within the Workflows and Process Integration Working Group.
- Open issue feedback highlighted execution decoupling tradeoffs and context rebuilding considerations [^evt-wg-workflows-and-process-integration-issue-45].

[^evt-wg-workflows-and-process-integration-issue-45]: https://github.com/aaif/wg-workflows-and-process-integration/issues/45
