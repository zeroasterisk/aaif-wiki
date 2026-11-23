---
type: working-group
title: Accuracy & Reliability Working Group
description: Technical working group defining evaluation frameworks, failure mode
  taxonomies, survey instruments, and test reporting standards for agentic AI systems.
resource: https://github.com/aaif/wg-accuracy-and-reliability/blob/10bc173f00e45d93a8f7038cb0c36a89e3219565/deliverables/arwg-survey.md
tags:
- working-groups
- accuracy
- reliability
- evaluation
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T09:58:38.771813+00:00'
sources:
- id: evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-503ff3e3
  resource: https://github.com/aaif/wg-accuracy-and-reliability/blob/10bc173f00e45d93a8f7038cb0c36a89e3219565/deliverables/arwg-survey.md
  author: Sanjeev Suresh
  last_modified: '2026-09-16T06:33:27-07:00'
- id: evt-wg-accuracy-and-reliability-pr-11
  resource: https://github.com/aaif/wg-accuracy-and-reliability/pull/11
  author: Rul1an
  last_modified: '2026-09-16T08:37:29+00:00'
---

# Overview

The Accuracy & Reliability Working Group establishes standardized evaluation methods, failure mode classifications, and measurement practices to assess the correctness, predictability, and operational resilience of agentic AI systems[^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-503ff3e3]. Represented on the [Taxonomy & Landscape Workstream](taxonomy-and-landscape.md) by Casper Nielsen and Matthew Khouzam, the working group develops empirical surveys, test inventories, and benchmark reporting criteria to support rigorous evaluation across diverse enterprise deployments[^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-503ff3e3][^evt-wg-accuracy-and-reliability-pr-11].

# Architecture / Specification

### Key Deliverables and Activities

- **Empirical Industry Survey**: Authored the platform-neutral [Accuracy & Reliability Survey](../resources/accuracy-and-reliability-survey.md), establishing a 16-question practitioner assessment evaluating deployment maturity, failure consequences, and testing needs across production environments[^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-503ff3e3].
- **D1 Deliverable Framework**: Under active development, the D1 workstream specifies testing vocabulary, benchmark inventories, and execution reporting standards[^evt-wg-accuracy-and-reliability-pr-11].
- **Coverage and Defect-Detection Reporting**: Proposed guidelines for D1 §9.4 mandate clear separation in coverage and mutation testing claims between declared inventories, selected evaluation subsets, fully exercised units, and uncompleted or excluded tests[^evt-wg-accuracy-and-reliability-pr-11]. For mutation analyses, the proposal mandates disaggregating detected, exercised-undetected, and unexercised seeded defects, rather than collapsing errors and timeouts into a single composite metric[^evt-wg-accuracy-and-reliability-pr-11].

# Lifecycle History

The working group operates under the Technical Committee governance, regularly reviewing community feedback on deliverable drafts and coordinating cross-cutting terminology through designated Domain Editors[^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-503ff3e3][^evt-wg-accuracy-and-reliability-pr-11].

[^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-503ff3e3]: https://github.com/aaif/wg-accuracy-and-reliability/blob/10bc173f00e45d93a8f7038cb0c36a89e3219565/deliverables/arwg-survey.md
[^evt-wg-accuracy-and-reliability-pr-11]: https://github.com/aaif/wg-accuracy-and-reliability/pull/11
