---
type: resource
title: AAIF Dallas Community Web Platform
description: Static web architecture, typed JSON content domain schema, and OIDC deployment
  pipeline powering the AAIF Dallas community summit portal.
resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/workflows/deploy.yml
tags:
- community
- deployment
- content-management
- static-site
- aaif-dallas
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:40:40.299520+00:00'
sources:
- id: evt-aaif-dallas-community-file-28802fbf11c8-a0805ead
  resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/workflows/deploy.yml
  author: Govindaraj Palanisamy
  last_modified: '2026-11-23T01:10:11-06:00'
- id: evt-aaif-dallas-community-file-2ac4893aa049-e1fe43a4
  resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/docs/content-management.md
  author: Govindaraj Palanisamy
  last_modified: '2026-11-23T01:10:11-06:00'
- id: evt-aaif-dallas-community-file-509a7fef8a34-033bfcc9
  resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/public/images/core-team/README.md
  author: Govindaraj Palanisamy
  last_modified: '2026-11-23T01:10:11-06:00'
- id: evt-aaif-dallas-community-file-7f6254f34e12-91809500
  resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/docs/deployment.md
  author: Govindaraj Palanisamy
  last_modified: '2026-11-23T01:10:11-06:00'
- id: evt-aaif-dallas-community-file-f6d36ab592c3-3152c916
  resource: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/public/images/committee-team/README.md
  author: Govindaraj Palanisamy
  last_modified: '2026-11-23T01:10:11-06:00'
- id: evt-aaif-dallas-community-pr-4
  resource: https://github.com/aaif/aaif-dallas-community/pull/4
  author: npgovintarajan
  last_modified: '2026-11-23T07:13:52+00:00'
---

# Overview
The AAIF Dallas Community Web Platform is the official static web portal and operational content estate powering the AAIF Dallas community summit [^evt-aaif-dallas-community-file-2ac4893aa049-e1fe43a4]. Implemented in Vite, TypeScript, and React, the site decouples public summit presentation from content management through a typed JSON content architecture, automated GitHub Actions change workflows, and a keyless OpenID Connect (OIDC) deployment pipeline targeting Amazon S3 and CloudFront [^evt-aaif-dallas-community-file-28802fbf11c8-a0805ead] [^evt-aaif-dallas-community-file-7f6254f34e12-91809500]. It directly serves event tracks, speaker rosters, committee assignments, and registration checkout while enforcing strict privacy boundaries against publishing attendee data or credentials [^evt-aaif-dallas-community-file-2ac4893aa049-e1fe43a4] [^evt-aaif-dallas-community-pr-4].

# Architecture / Specification

## Content Domain Architecture
The site reads static domain data from structured JSON documents located under `src/content/` [^evt-aaif-dallas-community-file-2ac4893aa049-e1fe43a4]:
- `event.json`: Summit metadata, event dates, registration references, and external student poster submission URLs [^evt-aaif-dallas-community-file-2ac4893aa049-e1fe43a4].
- `schedule.json`: Conference tracks, individual sessions, scheduled time slots, assigned rooms, speakers, and topical tags [^evt-aaif-dallas-community-file-2ac4893aa049-e1fe43a4] [^evt-aaif-dallas-community-pr-4].
- `speakers.json`: Presenter biographies, social profiles, and session associations [^evt-aaif-dallas-community-file-2ac4893aa049-e1fe43a4].
- `partners.json`: Organizing communities, community partners, and sponsoring organizations [^evt-aaif-dallas-community-file-2ac4893aa049-e1fe43a4].
- `organizers.json`: Core team and committee membership records with affiliations and headshots [^evt-aaif-dallas-community-file-2ac4893aa049-e1fe43a4] [^evt-aaif-dallas-community-pr-4].
- `committees.json`: Operational workstreams and organizational responsibilities [^evt-aaif-dallas-community-file-2ac4893aa049-e1fe43a4].
- `resources.json`: Public attendee lab preparation materials and prerequisites [^evt-aaif-dallas-community-file-2ac4893aa049-e1fe43a4].
- `news.json`: Editorial updates and summit announcements [^evt-aaif-dallas-community-file-2ac4893aa049-e1fe43a4].

Static image assets are segregated into typed directories under `public/images/`, including dedicated directories for CORE team portraits (`public/images/core-team/`) and committee member headshots (`public/images/committee-team/`) with initials fallbacks for missing assets [^evt-aaif-dallas-community-file-2ac4893aa049-e1fe43a4] [^evt-aaif-dallas-community-file-509a7fef8a34-033bfcc9] [^evt-aaif-dallas-community-file-f6d36ab592c3-3152c916].

## Data Validation and Privacy Rules
Data integrity and privacy constraints are strictly enforced before deployment:
- **Privacy Boundary**: Committing attendee exports, participant CSV files, private contact information, Luma API keys, or organizer secrets into the repository is prohibited [^evt-aaif-dallas-community-file-2ac4893aa049-e1fe43a4].
- **Schema & Relational Integrity**: Local and continuous integration checks (`npm run validate:content`) execute Zod schemas from `src/content/schema.ts`, verifying field types, date formats, and cross-reference links between speakers and sessions [^evt-aaif-dallas-community-file-28802fbf11c8-a0805ead] [^evt-aaif-dallas-community-file-2ac4893aa049-e1fe43a4].
- **Content Mutation Flow**: Non-developer maintainers submit content via a GitHub Actions workflow ("Prepare content change") which validates full object replacement payloads and opens a structured pull request [^evt-aaif-dallas-community-file-2ac4893aa049-e1fe43a4].

## Deployment Pipeline and Infrastructure
Production deployment is fully automated through GitHub Actions upon merge to `main` [^evt-aaif-dallas-community-file-28802fbf11c8-a0805ead] [^evt-aaif-dallas-community-file-7f6254f34e12-91809500]:
- **Runtime Environment**: Built using Node.js 22 within an `ubuntu-latest` runner governed by the `production` environment and single-concurrency lock `production-static-site` [^evt-aaif-dallas-community-file-28802fbf11c8-a0805ead].
- **Keyless Authentication**: The workflow exchanges GitHub OIDC tokens (`token.actions.githubusercontent.com`) for an AWS IAM role (`AAIFDallasStaticSiteDeployment`) scoped strictly to the repository and environment [^evt-aaif-dallas-community-file-28802fbf11c8-a0805ead] [^evt-aaif-dallas-community-file-7f6254f34e12-91809500].
- **Hosting Topology**: Static assets sync to an Amazon S3 bucket, followed by a CloudFront cache invalidation, with DNS managed via Cloudflare and TLS certificates hosted in ACM `us-east-1` [^evt-aaif-dallas-community-file-7f6254f34e12-91809500].

# References
- Related agent skills: [skills/community-event-operations](../skills/community-event-operations.md), [skills/fullstack-event-delivery](../skills/fullstack-event-delivery.md), [skills/event-requirements](../skills/event-requirements.md).

[^evt-aaif-dallas-community-file-28802fbf11c8-a0805ead]: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/.github/workflows/deploy.yml
[^evt-aaif-dallas-community-file-2ac4893aa049-e1fe43a4]: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/docs/content-management.md
[^evt-aaif-dallas-community-file-509a7fef8a34-033bfcc9]: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/public/images/core-team/README.md
[^evt-aaif-dallas-community-file-7f6254f34e12-91809500]: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/docs/deployment.md
[^evt-aaif-dallas-community-file-f6d36ab592c3-3152c916]: https://github.com/aaif/aaif-dallas-community/blob/9ee767202ead7d87455fcc04e6638836501625f3/public/images/committee-team/README.md
[^evt-aaif-dallas-community-pr-4]: https://github.com/aaif/aaif-dallas-community/pull/4
