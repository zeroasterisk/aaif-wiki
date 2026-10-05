---
type: resource
title: Agentic Workflow Patterns Comparison
description: Comparative taxonomy and evaluation matrix of industry agentic AI workflow
  orchestration patterns from major cloud providers and research labs.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/agentic-workflow-patterns-comparison.md
tags:
- resource
- workflow
- patterns
- orchestration
- taxonomy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:36:19.816203+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/agentic-workflow-patterns-comparison.md
  author: Mario Zagar
  last_modified: '2026-08-25T07:58:21-07:00'
- id: evt-wg-workflows-and-process-integration-pr-33
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/33
  author: mzagar
  last_modified: '2026-08-25T14:58:22+00:00'
---

# Overview

The Agentic AI Workflow Orchestration Patterns Comparison is a reference document cataloging, categorizing, and comparing architectural workflow patterns across major industry frameworks, including AWS, Azure, Google Cloud, and Anthropic [^evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab]. The document maps pattern complexity, agency levels, concrete use cases, and selection criteria to guide practitioners in choosing between deterministic orchestration, single-agent loops, and complex multi-agent architectures [^evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab].

# Architecture / Specification

### Pattern Spectrum

- **Minimal / Low Agency**: Includes *LLM-Augmented Workflows*, *Routing / Triage*, and *Prompt Chaining*, prioritizing deterministic control, low cost, and step-level validation [^evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab][^evt-wg-workflows-and-process-integration-pr-33].
- **Moderate Agency**: Encompasses *Single-Agent (ReAct)*, *Sequential Multi-Agent*, *Parallel Multi-Agent*, *Iterative Loop*, and *Review & Critique (Maker-Checker)* patterns balancing tool use with structured execution bounds [^evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab].
- **High / Complex Agency**: Covers *Coordinator (Orchestrator-Workers)*, *Hierarchical Task Decomposition*, *Swarm (Roundtable)*, and *Hybrid (Plan & Solve)* patterns designed for dynamic task decomposition and autonomous problem-solving [^evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab].
- **Control Boundaries**: Integrates *Human-in-the-Loop* approval points and *Custom Logic* for governance, compliance, and deterministic fail-safes [^evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab].

[^evt-wg-workflows-and-process-integration-file-d47ac6a6752f-a44a75ab]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/agentic-workflow-patterns-comparison.md
[^evt-wg-workflows-and-process-integration-pr-33]: https://github.com/aaif/wg-workflows-and-process-integration/pull/33
