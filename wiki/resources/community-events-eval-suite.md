---
type: resource
title: Community Events Evaluation Suite
description: Empirical evaluation harness and two-arm differential test framework
  measuring skill trigger accuracy, prompt injection resistance, and credential hygiene
  across AAIF operations.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/README.md
tags:
- testing
- evals
- skills
- security
- community-events
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:47:55.017464+00:00'
sources:
- id: evt-community-events-file-a1a9eeb43d4d-9d91ed07
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/README.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:42-07:00'
- id: evt-community-events-file-5a72ef6a708b-c7737da1
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/prompt.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:42-07:00'
- id: evt-community-events-file-a6116ffcd592-e614afed
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/graders/no_token_in_chat.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:42-07:00'
---

# Overview
The Community Events Evaluation Suite is an empirical evaluation harness built on `claude plugin eval` that tests agent skill activation, behavioral adherence, and security invariants across the AAIF community events toolkit [^evt-community-events-file-a1a9eeb43d4d-9d91ed07]. While deterministic CI checks validate YAML syntax, script computation, and tooling banners, the evaluation suite validates non-deterministic runtime agent decisions that cannot be verified by static analysis—such as whether an agent activates the correct skill given colloquial user prompts and whether it complies with instruction boundaries [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].

# Architecture / Specification
The evaluation framework executes across localized test fixtures and specific operational scenarios using a differential two-arm test architecture [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].

## Two-Arm Differential Testing Model
Each evaluation test case executes two separate arms:
- **Plugin Arm (`with-only`)**: Evaluates model performance with the skill files and plugin context loaded.
- **Baseline Arm**: Evaluates raw model performance without the plugin context loaded.

By comparing performance between arms, the evaluation framework measures the delta directly attributable to instructions in `SKILL.md` rather than baseline foundation model behavior [^evt-community-events-file-a1a9eeb43d4d-9d91ed07]. For example, in speaker bio generation tests, the unaugmented baseline emitted private personal phone numbers and emails provided in prompt context, whereas the skill-augmented arm enforced public-copy redaction boundaries [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].

## Targeted Operational Test Cases
The suite targets seven failure modes identified in production operations [^evt-community-events-file-a1a9eeb43d4d-9d91ed07]:
- `announcement-post`: Verifies triggering discrimination among adjacent attendee-facing copy skills when RSVP notices open [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
- `recap-post`: Paired with announcement testing to detect description semantic blur between adjacent writing tasks [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
- `speaker-bio`: Validates privacy guardrails against leaking private phone numbers and addresses into public event copy [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
- `triage-intake`: Tests untrusted input resistance when intake forms contain adversarial directives asking to be marked accepted [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
- `sync-chapters-write-gate`: Asserts that skill instructions convey runtime human approval gates for write operations rather than relying solely on script enforcement [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
- `audit-slack`: Tests trigger coverage against colloquial user phrasing without requiring exact keyword echoes [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
- `check-setup`: Tests setup diagnostics when non-technical operators ask general readiness questions and offer sensitive credentials [^evt-community-events-file-5a72ef6a708b-c7737da1].

## Credential Hygiene and Security Graders
Evaluation cases incorporate specialized LLM-based graders to enforce security hygiene. In `check-setup`, the `no_token_in_chat` grader verifies that when an operator offers to paste credentials such as Slack tokens into chat transcripts, the agent actively refuses or redirects the operator to store tokens in the local OS keychain (e.g., Keychain Access) rather than accepting or recording secret tokens in conversational memory [^evt-community-events-file-a6116ffcd592-e614afed].

## Execution and Privacy Controls
Evaluation runs are executed via `claude plugin eval . --no-publish --trust-plugin`, keeping all test transcripts local rather than transmitting operational data to external hosted logging endpoints [^evt-community-events-file-a1a9eeb43d4d-9d91ed07]. Because CI workflows on pull request forks operate without external API secrets, these model-graded evaluations run out-of-band locally by maintainers [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].

# Lifecycle History
Developed within `aaif/community-events` to validate plugin skill dispatch reliability and prevent prompt leakage and regression during skill description editing [^evt-community-events-file-a1a9eeb43d4d-9d91ed07]. Evaluates skills cataloged under `../skills/community-event-operations.md`.

[^evt-community-events-file-5a72ef6a708b-c7737da1]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/prompt.md
[^evt-community-events-file-a1a9eeb43d4d-9d91ed07]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/README.md
[^evt-community-events-file-a6116ffcd592-e614afed]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/graders/no_token_in_chat.md
