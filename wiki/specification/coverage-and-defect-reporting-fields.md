---
type: specification
title: Coverage and Defect Detection Reporting Fields
description: Defines required reporting fields for coverage and defect-detection claims,
  mandating separation of inventory, selection, exercised items, and specific mutation
  testing outcomes.
resource: https://github.com/aaif/wg-accuracy-and-reliability/pull/11
tags:
- accuracy
- reliability
- reporting
- mutation-testing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-flash-latest
  at: '2026-09-20T18:02:54.231316+00:00'
sources:
- id: evt-wg-accuracy-and-reliability-pr-11
  resource: https://github.com/aaif/wg-accuracy-and-reliability/pull/11
  author: Rul1an
  last_modified: '2026-09-16T08:37:29+00:00'
---

# Overview
This specification defines minimum vocabulary and required reporting fields for coverage and defect-detection claims made on panels or reports, applying the same idea used for benchmark inventories [^evt-wg-accuracy-and-reliability-pr-11].
The goal is to ensure clarity and prevent silent folding of unexercised or ambiguous results into other counts [^evt-wg-accuracy-and-reliability-pr-11].

# Architecture / Specification
When reporting coverage or defect-detection effectiveness, the claim must explicitly report the counting unit, declared inventory, selected subset, what was exercised, and what was excluded or could not complete [^evt-wg-accuracy-and-reliability-pr-11].
For mutation results, the specification requires keeping detected, exercised but undetected, and never exercised defects apart. It also mandates naming timeouts, errors, and equivalent mutants rather than merging them into a single score [^evt-wg-accuracy-and-reliability-pr-11].

[^evt-wg-accuracy-and-reliability-pr-11]: https://github.com/aaif/wg-accuracy-and-reliability/pull/11
