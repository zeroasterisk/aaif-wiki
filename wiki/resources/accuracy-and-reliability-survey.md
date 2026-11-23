---
type: resource
title: Accuracy and Reliability Survey
description: Platform-neutral 16-question empirical survey measuring real-world agentic
  failure modes, accuracy challenges, and operational constraints.
resource: https://github.com/aaif/wg-accuracy-and-reliability/blob/36572aec9bd6c78db9b2ce27bf7f1b9b9d4834bd/deliverables/arwg-survey.md
tags:
- working-group
- survey
- evaluation
- reliability
- metrics
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:26:12.484877+00:00'
sources:
- id: evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891
  resource: https://github.com/aaif/wg-accuracy-and-reliability/blob/36572aec9bd6c78db9b2ce27bf7f1b9b9d4834bd/deliverables/arwg-survey.md
  author: Jessie Zhang
  last_modified: '2026-10-15T14:09:14-07:00'
- id: evt-wg-accuracy-and-reliability-pr-14
  resource: https://github.com/aaif/wg-accuracy-and-reliability/pull/14
  author: Jessie1989
  last_modified: '2026-10-15T21:09:55+00:00'
---

# Overview
The AAIF Accuracy and Reliability Survey is a platform-neutral 16-question survey specification developed by the [Accuracy & Reliability Working Group](../working-groups/accuracy-and-reliability.md) to gather firsthand operational data from practitioners deploying AI agent systems into real-world production environments [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891]. The instrument measures the operational stability, error recovery capabilities, organizational constraints, and failure consequences observed across enterprise AI deployments over six-month observation windows [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].

# Architecture / Specification
## Response Structure and Routing Logic
The instrument utilizes four distinct question interaction formats: single-select, multi-select, single-response Likert matrix, and conditional inline text fields [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891]. Participation requires approximately 20 minutes and adheres to strict privacy constraints: respondent identity and contact credentials are intentionally omitted, responses are aggregated, and raw text entries are stripped of identifying corporate information prior to storage by AAIF [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891][^evt-wg-accuracy-and-reliability-pr-14].

Eligibility is governed by Question 1 (Experience during the past six months):
- **Continuing Paths:** Serious pilot, limited deployment, broad deployment, paused or retired, and unspecified real-world use allow the participant to advance into the core survey [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].
- **Early Exit:** Prototypes/demos, secondhand knowledge, or absence of relevant experience route respondents directly to an early-exit closure section [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].

## Survey Sections and Catalog
The remaining 15 questions target a single focal system identified during eligibility screening [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891]:
- **About the System (Q2–Q6):** Assesses direct engineering or supervisory roles (Q2), primary domain/work area (Q3), structural architecture (Q4), human verification mechanisms (Q5), and organization headcount (Q6) [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891][^evt-wg-accuracy-and-reliability-pr-14].
- **Benefits and Challenges (Q7–Q8):** Evaluates the primary realized benefit (Q7) paired against deployment constraints such as latency, cost, and safety boundaries (Q8) [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891][^evt-wg-accuracy-and-reliability-pr-14].
- **Accuracy and Reliability (Q9–Q13):** Analyzes the recurrence of unacceptable results (Q9), underlying technical factors triggering failures (Q10), detection latency prior to real-world impact (Q11), severity of worst-case consequences (Q12), and reliance on quality evidence types (Q13) [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891]. Failure factors in Q10 explicitly capture quality degradation post-system update (models, prompts, versions) and safe recovery failures resulting in dangling or partial actions [^evt-wg-accuracy-and-reliability-pr-14].
- **Future Priorities (Q14–Q16):** Identifies industry-wide technical priorities (Q14), preferred shared delivery resources (Q15), and open-ended commentary (Q16) [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].

[^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891]: https://github.com/aaif/wg-accuracy-and-reliability/blob/36572aec9bd6c78db9b2ce27bf7f1b9b9d4834bd/deliverables/arwg-survey.md
[^evt-wg-accuracy-and-reliability-pr-14]: https://github.com/aaif/wg-accuracy-and-reliability/pull/14
