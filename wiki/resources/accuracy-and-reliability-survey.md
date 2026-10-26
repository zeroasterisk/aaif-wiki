---
type: resource
title: Accuracy & Reliability Working Group Survey
description: Platform-neutral 16-question survey instrument evaluating real-world
  AI system deployments, failure visibility, and shared industry priorities.
resource: https://github.com/aaif/wg-accuracy-and-reliability/blob/36572aec9bd6c78db9b2ce27bf7f1b9b9d4834bd/deliverables/arwg-survey.md
tags:
- survey
- evaluation
- accuracy-and-reliability
- benchmarks
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T11:06:06.176360+00:00'
sources:
- id: evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891
  resource: https://github.com/aaif/wg-accuracy-and-reliability/blob/36572aec9bd6c78db9b2ce27bf7f1b9b9d4834bd/deliverables/arwg-survey.md
  author: Jessie Zhang
  last_modified: '2026-10-15T14:09:14-07:00'
---

# Overview
The Accuracy & Reliability Working Group Survey is a platform-neutral, 16-question evaluation instrument developed by the [Accuracy & Reliability Working Group](../working-groups/accuracy-and-reliability.md) to gather firsthand empirical evidence on AI agent deployments operating in production environments [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891]. Designed to assess operational realities rather than synthetic benchmarks, the survey measures deployment maturity, failure frequency, pre-impact failure recognition, and community priorities across diverse industry workflows [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].

# Architecture / Specification
The survey specifies standardized response formats, strict data governance parameters, eligibility screening, and a single focal-system evaluation structure [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].

## Response Formats and Governance
- **Response Formats:** Employs single-select, multi-select, single-response matrix (Likert scale), and conditional inline text entries [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].
- **Privacy and Data Governance:** Prohibits respondent names, employer identities, and customer confidential information; responses are stored by AAIF and published exclusively in aggregate, with short text answers redacted of identifying context before quotation [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].

## Questionnaire Structure
The survey organizes 16 questions across five operational dimensions centered on a single focal system evaluated over a six-month window [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891]:
1. **Eligibility and Real-World Use (Q1):** Gates participation based on maturity. Respondents working with serious pilots, limited deployments, broad deployments, paused/retired systems, or unspecified real-world use proceed to the survey; respondents with only demos, prototypes, secondhand knowledge, or no experience exit early [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].
2. **About the System (Q2–Q6):** Evaluates direct practitioner roles (design, quality testing, operations, and human oversight), functional work domain, architectural structure, human checking mechanisms, and organizational scale [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].
3. **Benefits and Challenges (Q7–Q8):** Identifies primary operational benefits alongside principal architectural and organizational constraints [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].
4. **Accuracy and Reliability (Q9–Q13):** Measures unacceptable output frequencies, root-cause accuracy factors, failure detection prior to downstream impact, severity of real-world consequences, and primary quality validation evidence [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].
5. **Future Priorities (Q14–Q16):** Surfaces shared-industry technical priorities and preferred cross-organizational resource investments [^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891].

[^evt-wg-accuracy-and-reliability-file-0e87c3ebe88a-a4aae891]: https://github.com/aaif/wg-accuracy-and-reliability/blob/36572aec9bd6c78db9b2ce27bf7f1b9b9d4834bd/deliverables/arwg-survey.md
