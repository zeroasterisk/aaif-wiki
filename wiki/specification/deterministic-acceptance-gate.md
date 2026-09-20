---
type: specification
title: Deterministic Acceptance Gate
description: A workflow pattern deciding whether a candidate result may advance using
  explicit, repeatable checks.
resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
tags:
- workflow-pattern
- security
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-flash-latest
  at: '2026-09-20T18:00:39.797762+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-pr-43
  resource: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
  author: narko4u
  last_modified: '2026-09-09T23:46:39+00:00'
---

# Overview
A workflow pattern deciding whether a candidate result may advance using explicit, repeatable checks.

The gate requires three properties to hold for every acceptance record, independent of the gate's required strength:
1. **Determinism of the verdict:** The decision (accept/reject) must be repeatable given the inputs.
2. **Binding of verdict to candidate:** The acceptance record must immutably link to the specific proposal or candidate result being evaluated.
3. **Preservation as execution evidence:** The acceptance record must be retained as part of the execution trace. [^evt-wg-workflows-and-process-integration-pr-43]

# Architecture / Specification
The minimum evidence required for a deterministic gate to be considered strong enough scales with the potential impact of the permitted effect. This strength is tied to two properties of the effect: the *blast radius* (the scope of potential damage or unintended consequences) and the *reversal cost* (the effort or resources required to undo the effect). [^evt-wg-workflows-and-process-integration-pr-43]

# References
- Related pattern: [Bounded Convergence Loop](../specification/bounded-convergence-loop.md)

[^evt-wg-workflows-and-process-integration-pr-43]: https://github.com/aaif/wg-workflows-and-process-integration/pull/43
