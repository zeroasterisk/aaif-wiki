---
type: methodology
title: AAIF Triage Intake Skill
description: Operational agent skill for reviewing, categorizing, and triaging community
  intake submissions while defending against prompt injections in untrusted form fields.
resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/triage-intake/prompt.md
tags:
- ops
- automation
- intake
- security
- evals
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T10:14:44.022779+00:00'
sources:
- id: evt-community-events-file-53c69ccfd21d-fa0ef669
  resource: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/triage-intake/prompt.md
  author: Rahul Parundekar
  last_modified: '2026-09-16T21:52:16-07:00'
---

# Overview

The AAIF Triage Intake Skill is an operational agent skill designed to process, summarize, and prioritize community intake submissions across foundation workflows while maintaining strict boundaries against untrusted input [^evt-community-events-file-53c69ccfd21d-fa0ef669].

# Architecture / Specification

The intake triage pipeline operates under defensive operational guidelines:

- **Untrusted Input Isolation**: Free-text form submissions (such as 'what brings you here' fields) are treated strictly as data payloads rather than executable operational instructions [^evt-community-events-file-53c69ccfd21d-fa0ef669].
- **Adversarial Input Handling**: Explicit evaluation prompts test for prompt-injection scenarios where applicants attempt to self-authorize acceptance or request automatic channel additions via free-text entries [^evt-community-events-file-53c69ccfd21d-fa0ef669].
- **Digest Generation**: Summarizes pending applicants awaiting decision queues without executing state mutations autonomously unless explicitly routed through authorized intake approval flows.

# Lifecycle History

- **Untrusted Form Text Evaluation**: Added explicit test harnesses validating that triage agent prompts correctly isolate user-submitted form text and reject self-granting status instructions [^evt-community-events-file-53c69ccfd21d-fa0ef669].

[^evt-community-events-file-53c69ccfd21d-fa0ef669]: https://github.com/aaif/community-events/blob/a8ca38601d912f5cdef68ce52a3c2aad0b196657/evals/triage-intake/prompt.md
