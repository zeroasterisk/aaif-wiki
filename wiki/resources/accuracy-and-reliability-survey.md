---
type: resource
title: Accuracy and Reliability Survey
description: Platform-neutral 16-question survey instrument evaluating real-world
  AI system deployments, failure modes, error recovery, and accuracy constraints.
resource: https://github.com/aaif/wg-accuracy-and-reliability/pull/14
tags:
- survey
- evaluation
- reliability
- accuracy
- benchmarks
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:26:35.776719+00:00'
sources:
- id: evt-wg-accuracy-and-reliability-pr-14
  resource: https://github.com/aaif/wg-accuracy-and-reliability/pull/14
  author: Jessie1989
  last_modified: '2026-10-15T21:09:55+00:00'
---

# Overview
The Accuracy and Reliability Survey is an empirical, platform-neutral instrument developed by the [Accuracy and Reliability Working Group](../working-groups/accuracy-and-reliability.md) to gather cross-industry data on operational AI failures, testing methodologies, and reliability blockers[^evt-wg-accuracy-and-reliability-pr-14]. The survey captures quantitative and qualitative metrics across real-world agent deployments without harvesting proprietary or identifying information[^evt-wg-accuracy-and-reliability-pr-14].

# Architecture / Specification

## Instrument Structure and Question Ordering
The 16-question survey assesses production AI systems across distinct evaluation domains[^evt-wg-accuracy-and-reliability-pr-14]:
- **Demographics and Architecture (Q1–Q4)**: System maturity, organizational footprint, and foundational architecture.
- **Operational Oversight and Benefits (Q5–Q8)**: Human checking touchpoints, organizational scale, realized benefits, and core operational constraints[^evt-wg-accuracy-and-reliability-pr-14].
- **Failure Taxonomy and Reliability Factors (Q9–Q16)**: Specific failure rates, quality degradations, error recovery limitations, and cross-industry remediation priorities[^evt-wg-accuracy-and-reliability-pr-14].

## Accuracy and Reliability Factors (Q10)
Question 10 evaluates observed deployment degradation factors, incorporating failure dimensions addressing system evolution and operational resilience[^evt-wg-accuracy-and-reliability-pr-14]:
- **Post-Change Quality Decline**: Degradation triggered by modifications to underlying models, prompts, tool definitions, or harness software versions[^evt-wg-accuracy-and-reliability-pr-14].
- **Unsafe Error Recovery**: Failures where the agent fails to recover cleanly after runtime errors, leaving behind partial tool mutations, corrupted state, or uncommitted execution fragments[^evt-wg-accuracy-and-reliability-pr-14].

## Consent and Data Governance Protocol
The intake protocol enforces strict data hygiene[^evt-wg-accuracy-and-reliability-pr-14]:
- **Anonymity**: No personal names or contact details are collected.
- **Reporting**: Responses are synthesized and published solely in aggregated benchmarking reports.
- **Administration**: Stored and governed by AAIF with administrative oversight coordinated via Foundation support channels[^evt-wg-accuracy-and-reliability-pr-14].

[^evt-wg-accuracy-and-reliability-pr-14]: https://github.com/aaif/wg-accuracy-and-reliability/pull/14
