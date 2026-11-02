---
type: pattern
title: Kill Switch
description: Architectural control plane pattern establishing out-of-band credential
  revocation and containment mechanisms to immediately halt autonomous agent execution.
resource: https://github.com/aaif/wg-security-and-privacy/blob/dae0a06fe4da39524d05fdc6cd7a63acf60f3c64/meeting-notes/2026-10-27.md
tags:
- security
- governance
- runtime-controls
- revocation
- pattern
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:32:51.084396+00:00'
sources:
- id: evt-wg-security-and-privacy-file-faf61688d774-51e9e85a
  resource: https://github.com/aaif/wg-security-and-privacy/blob/dae0a06fe4da39524d05fdc6cd7a63acf60f3c64/meeting-notes/2026-10-27.md
  author: Marc Molas Carol
  last_modified: '2026-11-01T19:18:57-05:00'
- id: evt-wg-security-and-privacy-pr-46
  resource: https://github.com/aaif/wg-security-and-privacy/pull/46
  author: MarcMolas
  last_modified: '2026-11-02T00:18:58+00:00'
---

# Overview

The Kill Switch pattern defines an authoritative, out-of-band operational mechanism to instantly revoke credentials, terminate runtime access, or halt execution loops across autonomous agent systems [^evt-wg-security-and-privacy-file-faf61688d774-51e9e85a]. As autonomous agents interact across heterogeneous environments, relying solely on cooperative in-band halting is insufficient; a robust kill switch enforces containment at identity, network, and harness boundaries [^evt-wg-security-and-privacy-file-faf61688d774-51e9e85a].

The pattern addresses containment across both enterprise boundaries—where standards like SPIFFE, RFC 7009, and OpenID Continuous Access Evaluation Profile (CAEP) apply—and open internet environments where identity attestation, decentralized verification, and third-party credential revocation are required [^evt-wg-security-and-privacy-file-faf61688d774-51e9e85a].

# Architecture / Specification

The pattern encompasses three primary revocation pathways and enforcement surfaces [^evt-wg-security-and-privacy-file-faf61688d774-51e9e85a]:

1. **Direct Agent or User Revocation:** An agent runtime can self-revoke, or an authenticated principal holding a hardware- or credential-backed token can trigger termination directly through an out-of-band control interface [^evt-wg-security-and-privacy-file-faf61688d774-51e9e85a].
2. **Cascade Revocation:** Revoking a root principal credential automatically invalidates all derived subagent keys, active sessions, and delegated authorization proofs across downstream services [^evt-wg-security-and-privacy-file-faf61688d774-51e9e85a].
3. **Issuer Emergency Revocation:** The authoritative issuer or validator publishes an emergency status root update, forcing verifiers to refuse incoming requests signed by the compromised agent or harness [^evt-wg-security-and-privacy-file-faf61688d774-51e9e85a].

### Open Internet and Ledger Distribution

While enterprise systems rely on reachable central identity providers and Continuous Access Evaluation Profile (CAEP) endpoints, open internet deployments face availability risks such as DNS failures or hyperscaler outages [^evt-wg-security-and-privacy-file-faf61688d774-51e9e85a]. In decentralized architectures, such as the open-source MintID protocol and ZadQ validator ecosystem, agents present short-lived zero-knowledge proofs (e.g., valid for 10 seconds) bound to requests, verified against public ledger status [^evt-wg-security-and-privacy-file-faf61688d774-51e9e85a].

In evaluated benchmarks, ledger-recorded kill switches achieved strict propagation bounds where verifiers systematically refused revoked agents within 245 seconds, with empirical network tests recording revocation refusal between 27.5 and 33.8 seconds [^evt-wg-security-and-privacy-file-faf61688d774-51e9e85a]. Additionally, kill switch events can integrate directly into Model Context Protocol (MCP) server transports and task loops, barring flagged agents at tool authentication time [^evt-wg-security-and-privacy-file-faf61688d774-51e9e85a].

# Lifecycle History

Evaluated within the Security and Privacy Working Group design patterns catalog, with clarification ongoing regarding central identity provider assumptions versus decentralized ledger mechanisms for open internet scenarios [^evt-wg-security-and-privacy-file-faf61688d774-51e9e85a] [^evt-wg-security-and-privacy-pr-46].

[^evt-wg-security-and-privacy-file-faf61688d774-51e9e85a]: https://github.com/aaif/wg-security-and-privacy/blob/dae0a06fe4da39524d05fdc6cd7a63acf60f3c64/meeting-notes/2026-10-27.md
[^evt-wg-security-and-privacy-pr-46]: https://github.com/aaif/wg-security-and-privacy/pull/46
