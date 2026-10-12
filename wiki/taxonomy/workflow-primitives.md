---
type: taxonomy
title: Workflow Primitives
description: Standardized vocabulary of modular workflow building blocks, execution
  states, and boundary contracts for agentic AI orchestration.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/taxonomy/terms.md
tags:
- taxonomy
- workflow
- vocabulary
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T02:54:39.529684+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-612fd92abd3a-7d19866f
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/taxonomy/terms.md
  author: Mario Zagar
  last_modified: '2026-08-28T22:43:08-04:00'
- id: evt-wg-workflows-and-process-integration-pr-31
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/31
  author: mzagar
  last_modified: '2026-08-29T02:43:08+00:00'
---

# Overview

Workflow Primitives define the foundational vocabulary and execution building blocks for structured agentic AI workflows and orchestration systems.[^evt-wg-workflows-and-process-integration-file-612fd92abd3a-7d19866f]

# Architecture / Specification

### Foundational Concepts

- **Activity**: A single, bounded task with defined inputs and outputs that can be tracked to completion.[^evt-wg-workflows-and-process-integration-file-612fd92abd3a-7d19866f] This term replaces earlier usages of "Workflow Step" and "Workflow Task" to prevent circularity with the Workflow definition.[^evt-wg-workflows-and-process-integration-pr-31]
- **Workflow**: The primary unit of structured, multi-activity work with a defined goal and outcome, composed of one or more activities, their relationships, and execution logic.[^evt-wg-workflows-and-process-integration-file-612fd92abd3a-7d19866f]
- **Workflow Execution**: A runtime instance of a workflow definition, maintaining its own execution state and lifecycle independently of concurrent instances.[^evt-wg-workflows-and-process-integration-file-612fd92abd3a-7d19866f]
- **Workflow State**: The information representing the current condition and execution progress of a workflow execution at a specific point in time.[^evt-wg-workflows-and-process-integration-file-612fd92abd3a-7d19866f]
- **Workflow Context**: The shared information available to workflow participants during execution, including inputs, shared metadata, history, and external references.[^evt-wg-workflows-and-process-integration-file-612fd92abd3a-7d19866f]

### Execution and Control

- **Control Flow**: The logic determining execution order, branching, parallelism, and synchronization of activities.[^evt-wg-workflows-and-process-integration-file-612fd92abd3a-7d19866f]
- **Trigger**: An event, condition, schedule, or signal initiating or advancing workflow execution.[^evt-wg-workflows-and-process-integration-file-612fd92abd3a-7d19866f]
- **Durability**: The capability of preserving execution state across system failures or interruptions without loss of progress.[^evt-wg-workflows-and-process-integration-file-612fd92abd3a-7d19866f]
- **Determinism**: The property whereby identical inputs, execution state, and history produce consistent execution behavior.[^evt-wg-workflows-and-process-integration-file-612fd92abd3a-7d19866f]

[^evt-wg-workflows-and-process-integration-file-612fd92abd3a-7d19866f]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/taxonomy/terms.md
[^evt-wg-workflows-and-process-integration-pr-31]: https://github.com/aaif/wg-workflows-and-process-integration/pull/31
