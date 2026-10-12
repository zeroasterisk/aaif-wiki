---
type: resource
title: Agent Accuracy and Reliability Survey
description: Platform-neutral 16-question survey evaluating production agent adoption,
  failure modes, consequence severity, and reliability requirements.
resource: https://github.com/aaif/wg-accuracy-and-reliability/pull/9
tags:
- survey
- accuracy
- reliability
- metrics
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:33:54.765261+00:00'
sources:
- id: evt-wg-accuracy-and-reliability-pr-9
  resource: https://github.com/aaif/wg-accuracy-and-reliability/pull/9
  author: Sanjeev-S
  last_modified: '2026-09-28T06:27:12+00:00'
---

# Overview

The Agent Accuracy and Reliability Survey is an empirical, platform-neutral instrument developed by the [Accuracy & Reliability Working Group](../working-groups/accuracy-and-reliability.md) to gather quantitative data on agent failures, verification practices, and operational consequences in production.[^evt-wg-accuracy-and-reliability-pr-9] Comprising 16 structured questions, the survey defines explicit respondent response behavior, validation rules, and early-exit screen-out mechanics.[^evt-wg-accuracy-and-reliability-pr-9]

# Architecture / Specification

The survey instrument is structured across five sequential sections:[^evt-wg-accuracy-and-reliability-pr-9]

1. **Eligibility (Q1)**: Establishes respondent eligibility based on active development or deployment of agentic systems, routing non-qualifying respondents through a dedicated early-exit termination path.[^evt-wg-accuracy-and-reliability-pr-9]
2. **About the System (Q2–Q5)**: Captures agent architectures, deployment environments, autonomy levels, and functional domains. Q2 incorporates structured options with required write-in fields for unspecified architectures; Q5 is optional.[^evt-wg-accuracy-and-reliability-pr-9]
3. **Benefits and Challenges (Q6–Q8)**: Assesses realized capabilities, operational impediments, and security concerns using standardized five-choice response matrices (including "Not sure").[^evt-wg-accuracy-and-reliability-pr-9]
4. **Accuracy and Reliability (Q9–Q13)**: Evaluates observed failure types, hallucination rates, error propagation, verification barriers, and impact severity.[^evt-wg-accuracy-and-reliability-pr-9]
5. **Future Priorities (Q14–Q16)**: Surveys organizational tooling roadmaps, benchmark utility, and desired open standards; Q16 is optional.[^evt-wg-accuracy-and-reliability-pr-9]

# Lifecycle History

In August 2026, the complete survey specification and question framework was authored and merged into the working group repository under PR #9, accompanied by a Google Forms prototype for internal working group review prior to public dissemination.[^evt-wg-accuracy-and-reliability-pr-9]

[^evt-wg-accuracy-and-reliability-pr-9]: https://github.com/aaif/wg-accuracy-and-reliability/pull/9
