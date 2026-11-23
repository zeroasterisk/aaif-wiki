---
type: guideline
title: Job-Oriented Architecture Model
description: Architectural framework organizing agent reference architectures around
  recognizable practitioner jobs rather than agent topology.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/README.md
tags:
- guidelines
- workflows
- architecture
- patterns
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T09:52:14.257124+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/README.md
  author: Mario Zagar
  last_modified: '2026-08-28T22:42:47-04:00'
---

# Overview
The Job-Oriented Architecture Model is an architectural structuring principle defined by the Workflows & Process Integration Working Group that organizes reference architectures around the job a practitioner needs an agentic system to perform[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424]. While topological metrics such as agent count ("single-agent" versus "multi-agent") provide structural context, they do not communicate the operational objective, behavioral guarantees, or failure boundaries of a workflow[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424].

Under this framework, reference architectures function as practitioner routing checklists: builders evaluate whether an architecture fits their target use case, whether an adjacent variant applies, or whether individual reusable patterns provide sufficient control[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424].

# Architecture / Specification

## Structural Taxonomy
The framework establishes explicit definitions distinguishing architectures, patterns, and scenarios[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424]:
- **Reference Architecture**: A complete composition defining reusable patterns, required capabilities, system boundaries, component relationships, guarantees, and exit states for a recognizable practitioner job[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424]. The architecture's name completes the sentence: *"We're building a ___"*[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424].
- **Pattern**: A self-contained solution addressing a single recurring sub-problem that can be adopted independently or composed into multiple reference architectures[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424]. Each pattern owns its own invariants and failure modes[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424].
- **Scenario**: Validation material demonstrating how an architecture behaves under a concrete, real-world use case[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424]. Scenarios serve strictly as test harnesses and validation benchmarks, not separate architectures[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424].

## Baseline Reference Architectures
The catalog establishes contrasting reference architectures addressing distinct practitioner jobs[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424]:
- [Single-Agent Process with Human Approval](../architectures/single-agent-human-approval.md): An agent drafts a proposal, an authorized human reviews and approves, and an isolated execution engine performs the protected modification[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424]. Composes [Proposal/Execution Split](../patterns/proposal-execution-split.md), [Human Approval Gate](../patterns/human-approval-gate.md), and [Durable Wait](../patterns/durable-wait.md)[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424].
- [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md): An agent iterates within a fenced problem boundary, an independent deterministic acceptance gate checks convergence, and bounded effects are committed[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424]. Composes [Bounded Convergence Loop](../patterns/bounded-convergence-loop.md), [Deterministic Acceptance Gate](../patterns/deterministic-acceptance-gate.md), and [Proposal/Execution Split](../patterns/proposal-execution-split.md)[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424].

## Architectural Boundary Rules
Reference architectures must delineate deterministic and model-driven activities, identifying where conventional workflow logic provides repeatable, testable execution versus where open-ended reasoning requires generative models[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424]. Inside agent boundaries, deterministic code and ReAct-style iterative reasoning loops are treated as equivalent implementation choices[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424].

[^evt-wg-workflows-and-process-integration-file-7443f6b14b82-702c4424]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/README.md
