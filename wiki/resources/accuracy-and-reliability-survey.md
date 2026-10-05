---
type: resource
title: Accuracy and Reliability Survey
description: Platform-neutral 16-question survey instrument gathering empirical data
  on real-world AI agent deployments and reliability priorities.
resource: https://github.com/aaif/wg-accuracy-and-reliability/pull/9
tags:
- survey
- accuracy
- reliability
- benchmarks
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:48:18.218698+00:00'
sources:
- id: evt-wg-accuracy-and-reliability-pr-9
  resource: https://github.com/aaif/wg-accuracy-and-reliability/pull/9
  author: Sanjeev-S
  last_modified: '2026-09-28T06:27:12+00:00'
---

# Overview
The Accuracy and Reliability Working Group (ARWG) survey is a platform-neutral 16-question instrument designed to collect empirical data on production AI agent deployments, operational hurdles, failure modes, and recovery priorities[^evt-wg-accuracy-and-reliability-pr-9].

# Architecture / Specification
The survey is organized into five structured sections with explicit branching and validation rules[^evt-wg-accuracy-and-reliability-pr-9]:
- **Eligibility (Q1)**: Screens respondents based on active deployment or evaluation of agentic AI systems, directing non-qualifying respondents to a dedicated exit page[^evt-wg-accuracy-and-reliability-pr-9].
- **About the System (Q2–Q5)**: Gathers information on agent system architecture, frameworks, and operational domains (Q5 is optional; Q2 includes structured write-in fields)[^evt-wg-accuracy-and-reliability-pr-9].
- **Benefits and Challenges (Q6–Q8)**: Measures observed operational advantages and integration barriers using standardized five-choice response matrices[^evt-wg-accuracy-and-reliability-pr-9].
- **Accuracy and Reliability (Q9–Q13)**: Identifies verification patterns, failure categories, automated recovery behavior, and evaluation tooling[^evt-wg-accuracy-and-reliability-pr-9].
- **Future Priorities (Q14–Q16)**: Surveys community demand for benchmark standards, reference architectures, and open feedback (Q16 is optional)[^evt-wg-accuracy-and-reliability-pr-9].

Related concepts: `../working-groups/accuracy-and-reliability.md`, `../policies-guidelines/ra-use-case-validation-guide.md`.

[^evt-wg-accuracy-and-reliability-pr-9]: https://github.com/aaif/wg-accuracy-and-reliability/pull/9
