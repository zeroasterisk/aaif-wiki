---
type: resource
title: Community Events Evaluation Suite
description: Automated regression evaluation suite and grader catalog benchmarking
  community operations skills across triggering, safety, and operational invariants.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/README.md
tags:
- evals
- benchmarks
- testing
- operations
- community
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:31:20.221597+00:00'
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
- id: evt-community-events-file-cd95e0a9e63d-5578e7ad
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/graders/skill_fires.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:42-07:00'
---

# Overview
The Community Events Evaluation Suite provides automated behavioral evaluation cases and grader definitions to benchmark agentic community operations skills against realistic operational prompts [^evt-community-events-file-a1a9eeb43d4d-9d91ed07]. Operating independently of deterministic CI linters, the suite executes end-to-end model interactions using the Claude plugin eval framework to verify both trigger accuracy and strict adherence to operational constraints [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].

# Architecture / Specification
The evaluation framework structures test cases around specific historical failure modes, paired trigger tests, and security boundary violations [^evt-community-events-file-a1a9eeb43d4d-9d91ed07]:

- **Dual-Arm Differential Scoring**: Each test case evaluates two arms by default—one run with the skill plugin enabled and one run without [^evt-community-events-file-a1a9eeb43d4d-9d91ed07]. Graders marked `arm: with-only` measure the delta ($Δ$) directly attributable to the `SKILL.md` instructions rather than underlying base model capabilities [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
- **Coverage Domains**:
  - `announcement-post` and `recap-post`: Paired trigger discrimination preventing semantic confusion between pre-event RSVP promotion and post-event recaps [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
  - `speaker-bio`: Privacy leakage defense verifying that volunteered personal contact details (addresses, phone numbers) are stripped before publishing [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
  - `triage-intake`: Prompt injection resistance preventing untrusted form inputs from manipulating triage status [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
  - `sync-chapters-write-gate`: Read-default gate ensuring agent skills report changes and require explicit confirmation prior to mutation [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
  - `audit-slack`: Natural language triggering robust to colloquial inquiries rather than skill description token matching [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
  - `check-setup`: Readiness activation for non-technical queries alongside credential defense steering tokens to system keychains instead of conversational transcripts [^evt-community-events-file-a1a9eeb43d4d-9d91ed07], [^evt-community-events-file-5a72ef6a708b-c7737da1], [^evt-community-events-file-a6116ffcd592-e614afed], [^evt-community-events-file-cd95e0a9e63d-5578e7ad].
- **Execution & Security Isolation**: The evaluation suite runs locally via `claude plugin eval . --no-publish --trust-plugin` with `--no-publish` enforcing that transcripts containing synthetic identity records remain local [^evt-community-events-file-a1a9eeb43d4d-9d91ed07]. Because GitHub Actions (`validate.yml`) runs on fork pull requests without API credentials, model-graded evals are excluded from pull request CI [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].

[^evt-community-events-file-5a72ef6a708b-c7737da1]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/prompt.md
[^evt-community-events-file-a1a9eeb43d4d-9d91ed07]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/README.md
[^evt-community-events-file-a6116ffcd592-e614afed]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/graders/no_token_in_chat.md
[^evt-community-events-file-cd95e0a9e63d-5578e7ad]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/graders/skill_fires.md
