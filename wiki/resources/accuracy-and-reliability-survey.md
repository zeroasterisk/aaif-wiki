---
type: resource
title: Accuracy & Reliability Survey
description: Vendor-neutral 16-question empirical survey assessing production agent
  system architectures, human verification practices, failure consequences, and industry
  priorities.
resource: https://github.com/aaif/wg-accuracy-and-reliability/blob/36572aec9bd6c78db9b2ce27bf7f1b9b9d4834bd/deliverables/arwg-survey.md
tags:
- resource
- survey
- accuracy
- reliability
- metrics
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:24:04.193516+00:00'
sources:
- id: evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891
  resource: https://github.com/aaif/wg-accuracy-and-reliability/blob/36572aec9bd6c78db9b2ce27bf7f1b9b9d4834bd/deliverables/arwg-survey.md
  author: Jessie Zhang
  last_modified: '2026-10-15T14:09:14-07:00'
---

# Overview

The AAIF Accuracy & Reliability Survey is a 16-question, platform-neutral empirical instrument designed by the [Accuracy & Reliability Working Group](../working-groups/accuracy-and-reliability.md) to gather firsthand operational data from practitioners deploying AI agent systems into real-world workflows [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891]. Designed to be completed in approximately 20 minutes, the survey explicitly disallows identifying or confidential details and aggregates responses to prioritize open foundation engineering initiatives [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].

# Architecture / Specification

## Eligibility Gating and Focal-System Anchoring

The survey utilizes a strict gating mechanism in Question 1 based on personal experience during the preceding six months [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891]:

- **Qualifying Cohorts:** Practitioners with experience in serious pilots (testing in intended work settings), limited deployments (normal work for some users), broad deployments (normal work for most users), paused or retired deployments, or unclassified real-world systems continue to the full survey [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].
- **Early-Exit Cohorts:** Respondents reporting only demo, prototype, or generic research work, secondhand knowledge, or no relevant system experience are routed directly to an early-exit closure [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].
- **Focal System Principle:** Qualified respondents evaluate one focal system throughout questions 2 through 16 to preserve observational consistency across operational metrics [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].

## Survey Inquiry Domains

The instrument assesses agent operations across five distinct analytical areas [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891]:

1. **System Profile (Q2–Q6):** Practitioner roles (design, testing, operation, human review), domain areas, structural composition, human verification checkpoints, and organizational scale [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].
2. **Benefits and Constraints (Q7–Q8):** Measurable productivity gains weighed against deployment bottlenecks [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].
3. **Accuracy and Reliability Failures (Q9–Q13):** Incident frequency, contributing error sources, pre-impact failure detection rates, severity of adverse outcomes, and primary evidentiary validation methods [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].
4. **Industry Priorities (Q14–Q15):** Cross-industry standardization needs and preferred open-source technical resources [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].
5. **Optional Closing Context (Q16):** Unstructured commentary regarding operational reliability hurdles [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].

[^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891]: https://github.com/aaif/wg-accuracy-and-reliability/blob/36572aec9bd6c78db9b2ce27bf7f1b9b9d4834bd/deliverables/arwg-survey.md
