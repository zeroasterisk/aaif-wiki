---
type: pattern
title: Proposal/Execution Split
description: Workflow design pattern separating non-deterministic agent proposal generation
  from deterministic, workflow-controlled side-effect execution.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/README.md
tags:
- pattern
- workflows
- architecture
- safety
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:02:45.557539+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/README.md
  author: Mario Zagar
  last_modified: '2026-08-28T22:42:47-04:00'
---

# Overview

The Proposal/Execution Split is a workflow architectural pattern cataloged by the [Workflows and Process Integration WG](../working-groups/workflows-and-process-integration.md) [^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424]. The pattern decouples the reasoning component that generates an action proposal from the execution component that applies state mutations or external side-effects.

By ensuring that language models and autonomous agents only produce structured, immutable proposals, the system can interpose deterministic acceptance gates, policy validation, and [human approval gates](../patterns/human-approval-gate.md) before any irreversible effect occurs [^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424].

# Architecture / Specification

## Composition

Under [job-oriented reference architectures](../methodology/job-oriented-reference-architectures.md), the Proposal/Execution Split serves as a foundation for multiple composite workflows:
- **Single-Agent Process with Human Approval**: An agent proposes changes, a human reviewer authorizes them across a [durable wait](../patterns/durable-wait.md) boundary, and an external deterministic executor carries out the action [^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424].
- **Bounded Autonomous Remediation**: An agent iterates inside a bounded convergence loop until an independent deterministic gate verifies the solution, after which an execution engine applies the constrained remediation [^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424].

## Core Invariants

1. **No Direct Agent Mutation**: The reasoning agent has zero write access to production endpoints or state stores.
2. **Typed Proposals**: Proposals are emitted as strongly validated, schema-compliant data structures containing expected pre-conditions and diffs.
3. **Deterministic Execution**: The downstream executor executes only verified proposals without invoking further model reasoning during execution.

[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424]: https://github.com/aaif/wg-workflows-and-process-integration/blob/c2b245dd9c1c837b0487d58e14ae8dd137b6433b/workstreams/reference-architectures/README.md
