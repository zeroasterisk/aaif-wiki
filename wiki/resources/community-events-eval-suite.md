---
type: resource
title: Community Events Evaluation Suite
description: Empirical evaluation suite and grading harness benchmarking skill triggering,
  prompt comprehension, and operational guardrails for community event agent skills.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/graders/skill_fires.md
tags:
- evals
- benchmarks
- community-events
- agent-skills
- testing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:21:20.723735+00:00'
sources:
- id: evt-community-events-file-cd95e0a9e63d-5578e7ad
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/graders/skill_fires.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:42-07:00'
- id: evt-community-events-file-b33563055168-f722dd04
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/README.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:20:05-07:00'
---

# Overview
The Community Events Evaluation Suite is an empirical benchmarking harness within the Agentic AI Foundation (AAIF) repository designed to test tool selection, invocation fidelity, and parameter safety across community management agent skills [^evt-community-events-file-cd95e0a9e63d-5578e7ad][^evt-community-events-file-b33563055168-f722dd04]. The suite verifies that agent runners correctly bind natural language user requests to underlying skills—such as [community event operations](../skills/community-event-operations.md)—without requiring rigid technical phrasing [^evt-community-events-file-cd95e0a9e63d-5578e7ad].

# Architecture and Grading Methodology
The harness evaluates agent behavior across operational tasks ranging from environment configuration checks to complex data migrations and event lifecycle administration [^evt-community-events-file-cd95e0a9e63d-5578e7ad][^evt-community-events-file-b33563055168-f722dd04].

## Tool Invocation and Trigger Evaluation
Evaluations use targeted test cases and automated assertion graders to verify proper activation of skills formatted according to the [Agent Skills standard](../standards/agent-skills.md) [^evt-community-events-file-cd95e0a9e63d-5578e7ad]. For instance, setup verification grading (`evals/check-setup/graders/skill_fires.md`) benchmarks whether the agent accurately triggers `aaif-check-setup` when presented with natural, colloquial queries such as "is it all working" [^evt-community-events-file-cd95e0a9e63d-5578e7ad]:
- **Input Matching**: Evaluates structured agent output against regular expressions detecting target skill invocations (e.g., matching `"skill"\s*:\s*"(?:[\w-]+:)?aaif-check-setup"`) [^evt-community-events-file-cd95e0a9e63d-5578e7ad].
- **Non-Technical Trigger Robustness**: Enforces that the skill triggers reliably on non-expert phrasing without requiring explicit keywords such as "setup" or "check" [^evt-community-events-file-cd95e0a9e63d-5578e7ad].

## Operational Safety and Protocol Conformance
Beyond skill triggering, the evaluation framework assesses adherence to critical operational boundaries [^evt-community-events-file-b33563055168-f722dd04]:
- **Proposal Separation**: Verifies that agents do not trigger mutative write operations during diagnostic or scanning prompts [^evt-community-events-file-b33563055168-f722dd04].
- **Environment Verification**: Benchmarks proper detection of required system dependencies, including authenticated `gws` Google Workspace CLI access and Python runtimes before execution [^evt-community-events-file-cd95e0a9e63d-5578e7ad][^evt-community-events-file-b33563055168-f722dd04].

# Lifecycle History
Developed within the `aaif/community-events` repository, the evaluation suite serves as an automated regression test gate within Foundation CI workflows, standardizing skill routing quality across compatible agent harnesses like [Goose](../resources/goose.md) [^evt-community-events-file-cd95e0a9e63d-5578e7ad][^evt-community-events-file-b33563055168-f722dd04].

[^evt-community-events-file-b33563055168-f722dd04]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/README.md
[^evt-community-events-file-cd95e0a9e63d-5578e7ad]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/graders/skill_fires.md
