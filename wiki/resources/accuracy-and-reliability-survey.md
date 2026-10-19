---
type: resource
title: Accuracy and Reliability Production Survey
description: Platform-neutral 16-question evaluation instrument measuring production
  deployment stages, failure frequencies, and governance priorities across agentic
  AI systems.
resource: https://github.com/aaif/wg-accuracy-and-reliability/pull/14
tags:
- survey
- accuracy
- reliability
- metrics
- evaluation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:14:48.488964+00:00'
sources:
- id: evt-wg-accuracy-and-reliability-pr-14
  resource: https://github.com/aaif/wg-accuracy-and-reliability/pull/14
  author: Jessie1989
  last_modified: '2026-10-15T21:09:55+00:00'
---

# Overview
The Accuracy and Reliability Production Survey is a platform-neutral 16-question evaluation instrument produced by the [Accuracy and Reliability Working Group](../working-groups/accuracy-and-reliability.md) to quantify deployment maturities, failure distributions, and operational pain points across production agentic AI workloads[^evt-wg-accuracy-and-reliability-pr-14]. The survey provides benchmark data on human oversight topologies, failure factors, and safety trade-offs[^evt-wg-accuracy-and-reliability-pr-14].

# Architecture / Specification
The instrument organizes evaluation metrics across four structured sections[^evt-wg-accuracy-and-reliability-pr-14]:
- **System Topology and Oversight**: Assesses single-agent and multi-agent coordination architectures alongside human verification patterns and organization scales[^evt-wg-accuracy-and-reliability-pr-14].
- **Reliability Degradation Factors**: Evaluates common failure modes in Question 10, specifically capturing quality decline caused by underlying system updates (such as model, prompt, or version changes) and failures to recover safely after an error (such as leaving partial, uncompensated actions behind)[^evt-wg-accuracy-and-reliability-pr-14].
- **Benefits and Constraints**: Collects comparative data on production business benefits against engineering, regulatory, and latency constraints[^evt-wg-accuracy-and-reliability-pr-14].
- **Data Custody and Consent**: Incorporates aggregate reporting commitments, AAIF storage policies, and formal respondent consent terms governing anonymous survey collection[^evt-wg-accuracy-and-reliability-pr-14].

# Lifecycle History
Maintained under deliverable D2 (`deliverables/arwg-survey.md`) within `aaif/wg-accuracy-and-reliability`, the survey was revised in PR #14 to refine failure factor granularity for post-error recovery and regression tracking, reorder organizational questions, and add participant consent terms[^evt-wg-accuracy-and-reliability-pr-14].

# References
- Accuracy and Reliability Survey PR #14: https://github.com/aaif/wg-accuracy-and-reliability/pull/14

[^evt-wg-accuracy-and-reliability-pr-14]: https://github.com/aaif/wg-accuracy-and-reliability/pull/14
