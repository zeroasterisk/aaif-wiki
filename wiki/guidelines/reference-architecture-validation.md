---
type: guideline
title: Reference Architecture Use Case Validation Guide
description: Standardized criteria, evidence requirements, and issue or pull request
  workflows for evaluating architectural fit between reference architectures and real-world
  use cases.
resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
tags:
- workflows
- reference-architecture
- validation
- methodology
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T09:55:47.183427+00:00'
sources:
- id: evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64
  resource: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
  author: Mario Zagar
  last_modified: '2026-09-15T16:19:55-04:00'
---

# Overview

The Reference Architecture Use Case Validation Guide defines the procedure for evaluating whether an Agentic AI Foundation (AAIF) Reference Architecture (RA) is an architectural fit for a real-world use case from the [Use Case Inventory](../resources/agentic-use-case-inventory.md)[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]. Designed for human contributors and automated coding agents, the process assesses whether a target use case shares the primary job and defining boundaries solved by the architecture.

A `Validated` outcome demonstrates architectural fit rather than operational compliance: it does not require proof that an existing implementation already deploys specific secondary controls such as version hashes, retries, storage layers, or credentials provided by the RA itself[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

# Architecture / Specification

### Validation Principles and Evidence
- **Definition of Fit**: An RA is marked `Validated` when the use-case source exhibits the primary job and key boundary governed by the architecture. Implementation-specific controls provided by the RA are not prerequisites for proving architectural alignment[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
- **Acceptable Evidence**: Evidence is restricted to facts asserted in the [Use Case Inventory](../resources/agentic-use-case-inventory.md) or its primary cited sources. Internal illustrative examples within an RA document do not constitute independent validation[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
- **Classification Field Weight**: Structural inventory fields (such as `Approval gate`, `Exception escalation`, or pattern assignments) constitute valid architectural evidence even if descriptive prose lacks full implementation details. Classification tags marked with undocumented rationale must be treated as `Unknown`[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

### Evaluation Workflow
1. **Check Construction**: Formulate two to three targeted checks derived from the RA's stated purpose, boundary conditions, guarantees, and checklist. Detailed implementation facts should only be evaluated if they alter architectural fit[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
2. **Tri-State Check Accounting**: Record explicit definitions for `Yes`, `No`, and `Unknown` across each check[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
3. **Result Formulation**: Conclude with a concise plain-language summary restricting "What matches" and "What is unknown" to a maximum of two bullet points each[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].
4. **Contribution Output**: Submit a pull request when the evidence is unambiguous, or open a tracking issue if further domain clarification or evidence discovery is required[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64].

# References

- [Bounded Autonomous Remediation](../architectures/bounded-autonomous-remediation.md)
- [Critical Use Case Inventory](../resources/agentic-use-case-inventory.md)
- [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md)

[^evt-wg-workflows-and-process-integration-file-c88ec331f2fd-2adc5f64]: https://github.com/aaif/wg-workflows-and-process-integration/blob/3b4d645499620b10b313297e7f365148fa6d0ee1/workstreams/reference-architectures/docs/ra-use-case-validation-guide.md
