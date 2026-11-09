---
type: resource
title: Community Events Evaluation Suite
description: Automated testing harness and evaluation framework enforcing skill firing
  accuracy, write-gate safety, and credential isolation across event operations.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/prompt.md
tags:
- evals
- skills
- security
- operations
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:20:33.802421+00:00'
sources:
- id: evt-community-events-file-5a72ef6a708b-c7737da1
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/prompt.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:42-07:00'
- id: evt-community-events-file-a1a9eeb43d4d-9d91ed07
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/README.md
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

The AAIF Community Events Evaluation Suite is an automated evaluation harness designed to test AI agent skills against regression failures that static linting and deterministic unit tests cannot detect[^evt-community-events-file-a1a9eeb43d4d-9d91ed07]. While deterministic tools such as `pytest` and schema linter scripts prove syntax, tooling banners, and YAML validity, they cannot verify whether an LLM reading a skill definition triggers the correct skill or reliably complies with behavioral directives[^evt-community-events-file-a1a9eeb43d4d-9d91ed07].

The evaluation harness targets subtle behavioral shifts, such as prompt vocabulary drift causing neighboring skills to misfire, improper handling of untrusted inputs, inadvertent disclosure of personal data, or token ingestion in conversational context[^evt-community-events-file-a1a9eeb43d4d-9d91ed07].

# Architecture / Specification

### Dual-Arm Differential Evaluation

The framework executes test cases across two concurrent arms to isolate skill contribution from foundation model defaults[^evt-community-events-file-a1a9eeb43d4d-9d91ed07]:
1. **With Plugin / Skill**: The agent executes the scenario with candidate skill documentation (`SKILL.md`) in context.
2. **Without Plugin / Skill**: The agent executes the identical prompt in baseline configuration.

Graders that pass under both conditions evaluate base foundation model abilities rather than skill effectiveness; criteria evaluated only when a skill is present are classified as `arm: with-only` to quantify the document's direct performance delta (`Δ`)[^evt-community-events-file-a1a9eeb43d4d-9d91ed07].

### Evaluated Failure Modes and Cases

- **Skill Triggering Disambiguation**: Tests such as `announcement-post` versus `recap-post` verify that similar attendee-facing skills fire accurately based on contextual phase (e.g., RSVP opening versus post-event recap)[^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
- **Vocabulary-Agnostic Activation**: The `check-setup` test evaluates non-technical prompts (e.g., asking "is it all working?") to ensure operational tools activate without relying on verbatim trigger phrases[^evt-community-events-file-5a72ef6a708b-c7737da1][^evt-community-events-file-cd95e0a9e63d-5578e7ad].
- **Privacy and Credential Boundary Defense**: Ensures that agents explicitly reject sensitive credentials offered in chat (such as Slack tokens) and redirect users to secure credential stores (e.g., Keychain Access)[^evt-community-events-file-a6116ffcd592-e614afed], while preventing accidental leakage of speaker contact information (phone numbers, private addresses) into published outputs[^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
- **Adversarial and Untrusted Form Input**: Enforces defenses against prompt injection via intake form cells (e.g., users requesting automated approval)[^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
- **Write Gate Enforcement**: Verifies that skills follow the [proposal-execution-split](../patterns/proposal-execution-split.md), reporting and proposing changes by default and executing updates only upon explicit confirmation[^evt-community-events-file-a1a9eeb43d4d-9d91ed07].

### Execution and CI Policy

Evaluations are invoked via the CLI harness (e.g., `claude plugin eval . --no-publish --trust-plugin`)[^evt-community-events-file-a1a9eeb43d4d-9d91ed07]. The suite runs locally and outside of pull request CI jobs (`validate.yml`) because public fork builds operate without API credentials to protect against token exfiltration[^evt-community-events-file-a1a9eeb43d4d-9d91ed07].

# References

- [aaif-check-setup](../skills/aaif-check-setup.md)
- [aaif-clean-data](../skills/aaif-clean-data.md)
- [proposal-execution-split](../patterns/proposal-execution-split.md)

[^evt-community-events-file-5a72ef6a708b-c7737da1]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/prompt.md
[^evt-community-events-file-a1a9eeb43d4d-9d91ed07]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/README.md
[^evt-community-events-file-a6116ffcd592-e614afed]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/graders/no_token_in_chat.md
[^evt-community-events-file-cd95e0a9e63d-5578e7ad]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/graders/skill_fires.md
