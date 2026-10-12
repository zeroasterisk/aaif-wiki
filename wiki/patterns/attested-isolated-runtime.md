---
type: pattern
title: Attested Isolated Runtime
description: Architectural pattern isolating policy enforcement, secret handling,
  and execution within hardware-attested confidential environments.
resource: https://github.com/aaif/wg-security-and-privacy/issues/37
tags:
- pattern
- confidential-computing
- attestation
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:16:55.654115+00:00'
sources:
- id: evt-wg-security-and-privacy-issue-37
  resource: https://github.com/aaif/wg-security-and-privacy/issues/37
  author: imran-siddique
  last_modified: '2026-10-05T15:26:00+00:00'
---

# Overview
The Attested Isolated Runtime pattern executes agent reasoning, policy enforcement, or sensitive tool invocations inside a hardware-isolated confidential computing environment (such as a confidential virtual machine or enclave). By generating cryptographic attestation reports verifying guest software integrity, the pattern protects execution state against untrusted host operators and co-located workloads.

# Architecture / Specification

## Host vs. Guest Threat Boundaries
Hardware attestation guarantees memory encryption and guest execution integrity against host-level hypervisors, firmware, and physical access [^evt-wg-security-and-privacy-issue-37]. However, guest software operating within the isolated environment remains part of the trusted computing base [^evt-wg-security-and-privacy-issue-37]. If guest software exposes a bearer token, hardware isolation does not constrain the resulting blast radius or shorten the token's validity window [^evt-wg-security-and-privacy-issue-37]. Confidential runtime architectures must enforce:
- **Short-Lived Token Lifecycles**: Provisioning short-lived, narrowly scoped credentials whose maximum exposure window is governed by token validity and revocation mechanisms rather than hardware boundaries [^evt-wg-security-and-privacy-issue-37].
- **Internal Guest Restrictions**: Partitioning guest processes to restrict which software components can read, process, or release credentials [^evt-wg-security-and-privacy-issue-37].
- **Attestation Claims Binding**: Cryptographically binding attestation payloads (such as REPORT_DATA) to hashes of runtime claims, including vTPM keys, virtual machine configurations, and user data [^evt-wg-security-and-privacy-issue-37].

## Integration with Governance Patterns
Attested isolated runtimes frequently pair with [proposal-execution splits](./proposal-execution-split.md) and [human-approval gates](./human-approval-gate.md) to ensure high-risk agent operations cannot execute without verified attestation boundaries. Guidelines for credential exposure within confidential boundaries are maintained in the [Agentic AI Security Best Practices Guide](../guidelines/agentic-ai-security-best-practices.md) [^evt-wg-security-and-privacy-issue-37].

# Lifecycle History
Established as an architectural pattern under the Security and Privacy Working Group. Refined in issue #37 to clarify the platform threat model regarding guest-level token exposures and report payload claim bindings.

[^evt-wg-security-and-privacy-issue-37]: https://github.com/aaif/wg-security-and-privacy/issues/37
