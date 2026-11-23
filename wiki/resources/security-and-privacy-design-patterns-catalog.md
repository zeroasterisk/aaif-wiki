---
type: resource
title: Security and Privacy Design Patterns Catalog
description: Architectural catalog defining vendor-neutral, reusable design patterns
  addressing recurring security and privacy challenges in agentic AI deployments.
resource: https://github.com/aaif/wg-security-and-privacy/blob/a322f52eea70e3bc7c3a0e7d08007fc309ac4dc8/meeting-notes/README.md
tags:
- security
- privacy
- patterns
- architecture
- catalog
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:27:22.448719+00:00'
sources:
- id: evt-wg-security-and-privacy-file-d7a6875f36a3-a722423c
  resource: https://github.com/aaif/wg-security-and-privacy/blob/a322f52eea70e3bc7c3a0e7d08007fc309ac4dc8/meeting-notes/README.md
  author: Alex Frazer
  last_modified: '2026-10-19T09:09:02-04:00'
- id: evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93
  resource: https://github.com/aaif/wg-security-and-privacy/blob/a322f52eea70e3bc7c3a0e7d08007fc309ac4dc8/meeting-notes/2026-10-13.md
  author: Alex Frazer
  last_modified: '2026-10-19T09:09:02-04:00'
---

# Overview
The Security and Privacy Design Patterns Catalog is an open, vendor-neutral repository of reusable architectural patterns maintained by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) [^evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93]. The catalog equips system designers, platform engineers, and security architects with standardized mitigations for vulnerabilities that emerge when autonomous or semi-autonomous software agents invoke external tools, process untrusted instructions, and delegate execution authority [^evt-wg-security-and-privacy-file-d7a6875f36a3-a722423c].

# Architecture / Specification
Patterns within the catalog are structured around common operational surfaces and threat boundaries in agent harnesses. Each pattern defines concrete invariants, component responsibilities, failure modes, and implementation guidance.

Key design patterns actively developed and merged into the main repository include [^evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93]:
- **[Approval Checkpoint](../patterns/approval-checkpoint.md)**: A runtime authorization checkpoint binding human or policy approval records to exact execution payloads and parameter hashes before privileged actions take place [^evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93].
- **[Attested Isolated Runtime](../patterns/attested-isolated-runtime.md)**: An architectural security pattern isolating policy evaluation and cryptographic evidence generation within a hardware-attested or isolated environment [^evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93].
- **[Kill Switch](../patterns/kill-switch.md)**: An out-of-band operational control plane mechanism capable of immediately revoking agent delegation, terminating execution loops, and isolating impacted systems during containment events [^evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93].

# Lifecycle History
- **2026-07-21**: Design patterns catalog structural framework drafted and submitted for architecture guidance review [^evt-wg-security-and-privacy-file-d7a6875f36a3-a722423c].
- **2026-09-01**: Initial review of kill-switch and containment pattern proposals [^evt-wg-security-and-privacy-file-d7a6875f36a3-a722423c].
- **2026-10-13**: Working group merged initial baseline drafts of the approval checkpoint, attested runtime isolation, and kill switch patterns to the main catalog [^evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93].

[^evt-wg-security-and-privacy-file-d7a6875f36a3-a722423c]: https://github.com/aaif/wg-security-and-privacy/blob/a322f52eea70e3bc7c3a0e7d08007fc309ac4dc8/meeting-notes/README.md
[^evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93]: https://github.com/aaif/wg-security-and-privacy/blob/a322f52eea70e3bc7c3a0e7d08007fc309ac4dc8/meeting-notes/2026-10-13.md
