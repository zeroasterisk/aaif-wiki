---
type: resource
title: Platform-Neutral Accuracy and Reliability Survey
description: Platform-neutral 16-question survey instrument evaluating real-world
  AI system deployments, failure modes, accuracy challenges, and operational priorities.
resource: https://github.com/aaif/wg-accuracy-and-reliability/pull/9
tags:
- resources
- survey
- accuracy
- reliability
- evaluation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:19:58.462595+00:00'
sources:
- id: evt-wg-accuracy-and-reliability-pr-9
  resource: https://github.com/aaif/wg-accuracy-and-reliability/pull/9
  author: Sanjeev-S
  last_modified: '2026-09-28T06:27:12+00:00'
---

# Overview

The Platform-Neutral Accuracy and Reliability Survey is an empirical research instrument authored by the [Accuracy and Reliability Working Group](../working-groups/accuracy-and-reliability.md) to gather structured data on production agentic AI deployments, operational failure modes, and industry mitigation strategies [^evt-wg-accuracy-and-reliability-pr-9]. Designed to remain independent of any proprietary framework or model vendor, the survey collects standardized responses across engineering teams, operators, and researchers to inform AAIF benchmark profiles and reliability taxonomies.

# Architecture / Specification

## Survey Structure and Sections

The survey contains 16 questions organized into five structured sections [^evt-wg-accuracy-and-reliability-pr-9]:

- **Section 1: Eligibility (Q1)**: Filters respondent organizations based on deployment lifecycle stage. Includes an early-exit branch directing ineligible participants to an informative exit page [^evt-wg-accuracy-and-reliability-pr-9].
- **Section 2: About the System (Q2–Q5)**: Captures architecture topologies, agent autonomy levels, runtime integration patterns, and domain contexts. Q2 supports extensible write-ins via a required free-text field on selection of "Something else", while Q5 is optional [^evt-wg-accuracy-and-reliability-pr-9].
- **Section 3: Benefits and Challenges (Q6–Q8)**: Assesses observed business benefits versus operational hurdles using 5-point choice matrices that include explicit "Not sure" response anchors [^evt-wg-accuracy-and-reliability-pr-9].
- **Section 4: Accuracy and Reliability (Q9–Q13)**: Probes specific failure modes, hallucination frequency, deterministic verification approaches, human approval gates, and regression testing practices [^evt-wg-accuracy-and-reliability-pr-9].
- **Section 5: Future Priorities (Q14–Q16)**: Evaluates organizational roadmap requirements for benchmarking, standardized evaluations, and guardrail architectures. Q16 provides optional qualitative feedback [^evt-wg-accuracy-and-reliability-pr-9].

## Response Mechanics and Validation

All questions are mandatory with the exception of Q5 and Q16 [^evt-wg-accuracy-and-reliability-pr-9]. The instrument incorporates deterministic branching logic for early screen-outs at Q1, matrix constraint validation, and inline text collection for open-ended category expansions to ensure analytical consistency across deployments [^evt-wg-accuracy-and-reliability-pr-9].

# Lifecycle History

- **August 2026**: Merged complete platform-neutral 16-question specification, response mechanics, and validation flows into the Accuracy and Reliability Working Group repository under PR #9 [^evt-wg-accuracy-and-reliability-pr-9].

[^evt-wg-accuracy-and-reliability-pr-9]: https://github.com/aaif/wg-accuracy-and-reliability/pull/9
