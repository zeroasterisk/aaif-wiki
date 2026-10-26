---
type: working-group
title: Security and Privacy Working Group
description: AAIF technical working group establishing threat models, defensive architecture
  patterns, runtime safety controls, and security best practices.
resource: https://github.com/aaif/wg-security-and-privacy/blob/a322f52eea70e3bc7c3a0e7d08007fc309ac4dc8/README.md
tags:
- working-group
- security
- privacy
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T11:06:49.409332+00:00'
sources:
- id: evt-wg-security-and-privacy-file-b33563055168-b90dcbe6
  resource: https://github.com/aaif/wg-security-and-privacy/blob/a322f52eea70e3bc7c3a0e7d08007fc309ac4dc8/README.md
  author: Alex Frazer
  last_modified: '2026-10-19T09:14:44-04:00'
- id: evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93
  resource: https://github.com/aaif/wg-security-and-privacy/blob/a322f52eea70e3bc7c3a0e7d08007fc309ac4dc8/meeting-notes/2026-10-13.md
  author: Alex Frazer
  last_modified: '2026-10-19T09:09:02-04:00'
- id: evt-wg-security-and-privacy-file-d7a6875f36a3-a722423c
  resource: https://github.com/aaif/wg-security-and-privacy/blob/a322f52eea70e3bc7c3a0e7d08007fc309ac4dc8/meeting-notes/README.md
  author: Alex Frazer
  last_modified: '2026-10-19T09:09:02-04:00'
---

# Overview
The Security and Privacy Working Group advances the Agentic AI Foundation's mission by establishing security and privacy as a shared discipline across agentic architectures [^evt-wg-security-and-privacy-file-b33563055168-b90dcbe6]. The group develops vendor-neutral threat models, defensive design patterns, and baseline security guidelines that agent developers, system deployers, and peer working groups can adopt to secure autonomous systems [^evt-wg-security-and-privacy-file-b33563055168-b90dcbe6].

# Organization and Governance
The working group is chaired by Alex Frazer (Runlayer) and co-chaired by Junjie Bu (Google), appointed by Platinum and Gold members for the inaugural term spanning March 1, 2026 through January 31, 2027 [^evt-wg-security-and-privacy-file-b33563055168-b90dcbe6]. Subsequent chair terms align with the anniversary of charter approval per Technical Committee governance [^evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93].

The working group conducts two alternating meetings to support global participation [^evt-wg-security-and-privacy-file-b33563055168-b90dcbe6]:
- **Primary Meeting**: Biweekly on Tuesdays at 10:00 AM PT [^evt-wg-security-and-privacy-file-b33563055168-b90dcbe6].
- **APAC Meeting**: Biweekly on Mondays at 9:00 PM ET on alternating weeks to provide working-hours access for contributors across Asia-Pacific time zones [^evt-wg-security-and-privacy-file-b33563055168-b90dcbe6], [^evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93].

# Deliverables and Workstreams
The working group directs several key technical deliverables [^evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93]:
- **Threat Modeling**: Completed an initial comparative gap analysis evaluating traditional methodologies against autonomous agent architectures, followed by threat modeling extensions using MITRE ATLAS and OWASP ASI frameworks [^evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93].
- **Security Best Practices**: Authored the [Agentic AI Security Best Practices](../guidelines/agentic-ai-security-best-practices.md) guide, with the initial draft published and open to community contributions [^evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93].
- **Design Patterns Catalog**: Developed and merged initial architectural patterns including [Approval Checkpoint](../patterns/approval-checkpoint.md), [Attested Isolated Runtime](../patterns/attested-isolated-runtime.md), and [Kill Switch](../patterns/kill-switch.md) into the core patterns catalog [^evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93].
- **Cross-Working Group Alignment**: Collaborates with the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) on telemetry seams and with the [Identity and Trust Working Group](../working-groups/identity-and-trust.md) on hardware and runtime attestation [^evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93].
- **Taxonomy and Landscape**: Contributes security terms into the cross-WG effort coordinated by the [Taxonomy and Landscape Working Group](../working-groups/taxonomy-and-landscape.md) [^evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93].

[^evt-wg-security-and-privacy-file-b33563055168-b90dcbe6]: https://github.com/aaif/wg-security-and-privacy/blob/a322f52eea70e3bc7c3a0e7d08007fc309ac4dc8/README.md
[^evt-wg-security-and-privacy-file-e3f78aaae09b-daf59b93]: https://github.com/aaif/wg-security-and-privacy/blob/a322f52eea70e3bc7c3a0e7d08007fc309ac4dc8/meeting-notes/2026-10-13.md
