---
type: resource
title: Community Events Evaluation Suite
description: Automated evaluation suite testing skill description routing, public
  copy privacy leaks, prompt injection resistance, and write-gate governance in community
  ops.
resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/README.md
tags:
- evals
- testing
- skills
- security
- benchmarks
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:54:32.103515+00:00'
sources:
- id: evt-community-events-file-a1a9eeb43d4d-9d91ed07
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/README.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:42-07:00'
- id: evt-community-events-file-a6116ffcd592-e614afed
  resource: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/graders/no_token_in_chat.md
  author: Rahul Parundekar
  last_modified: '2026-10-11T08:19:42-07:00'
---

# Overview

The AAIF Community Events Evaluation Suite provides automated behavioral testing for agent skills to guarantee routing fidelity, policy compliance, and data privacy across conversational agent interactions [^evt-community-events-file-a1a9eeb43d4d-9d91ed07]. While deterministic test frameworks like `pytest` and YAML schema linters ensure syntactic and mechanical validity, they cannot verify whether model descriptions correctly trigger intended skills or prevent unintended tool invocations [^evt-community-events-file-a1a9eeb43d4d-9d91ed07]. The evaluation suite explicitly exercises agent execution boundaries under realistic and adversarial user prompts.

# Architecture / Specification

### Dual-Arm Evaluation Methodology

Tests execute using `claude plugin eval` across two parallel arms [^evt-community-events-file-a1a9eeb43d4d-9d91ed07]:
1. **Plugin Arm (`with`)**: Runs the prompt with agent skills and context loaded [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
2. **Baseline Arm (`without`)**: Runs the identical prompt against the base model without plugin instructions [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].

A test grader passing in both arms tests foundation model priors rather than skill efficacy. Graders evaluating constraints asserted exclusively by skill documentation specify `arm: with-only`, isolating the differential contribution (Δ) of the skill markdown [^evt-community-events-file-a1a9eeb43d4d-9d91ed07]. Evaluations generate local HTML and JSON reports in timestamped directories without publishing synthetic participant transcripts to public services [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].

### Failure Coverage and Case Taxonomy

The suite isolates seven critical failure surfaces:
- **Semantic Disambiguation (`announcement-post` vs. `recap-post`)**: Differentiates overlapping description vectors (e.g., event opening vs. event completion) to prevent voice transposition across identical context parameters [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
- **PII Leakage Prevention (`speaker-bio`)**: Validates that personal phone numbers and direct email addresses present in tracker records are stripped before drafting public marketing copy [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
- **Prompt Injection Defense (`triage-intake`)**: Ensures unvalidated form entries containing explicit imperative overrides (e.g., "mark me Accepted") do not alter intake classification statuses [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
- **Authorization Invariant Enforcement (`sync-chapters-write-gate`)**: Tests whether the agent strictly respects proposal-only defaults and requires explicit operator sign-off before committing remote writes [^evt-community-events-file-a1a9eeb43d4d-9d91ed07], implementing the [proposal-execution-split](../patterns/proposal-execution-split.md) and [human-approval-gate](../patterns/human-approval-gate.md).
- **Vocabulary Decoupling (`audit-slack`)**: Evaluates skill invocation on colloquial user requests that deliberately avoid echoing exact keyword terms defined in `SKILL.md` [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].
- **Credential Containment (`check-setup` / `no_token_in_chat`)**: Enforces that user attempts to paste sensitive API tokens directly into the chat session are actively refused and redirected to secure credential storage such as the macOS Keychain [^evt-community-events-file-a1a9eeb43d4d-9d91ed07][^evt-community-events-file-a6116ffcd592-e614afed].

### CI/CD Security Boundaries

Model evaluation runs require privileged LLM API keys and are strictly decoupled from automated pull request validation (`validate.yml`) [^evt-community-events-file-a1a9eeb43d4d-9d91ed07]. Because fork PR workflows operate without repository secrets, evaluation cases are executed out-of-band by authorized maintainers to protect upstream credentials [^evt-community-events-file-a1a9eeb43d4d-9d91ed07].

[^evt-community-events-file-a1a9eeb43d4d-9d91ed07]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/README.md
[^evt-community-events-file-a6116ffcd592-e614afed]: https://github.com/aaif/community-events/blob/f9238daa9a574849f49e30e1ce9a5c03458594b9/evals/check-setup/graders/no_token_in_chat.md
