# ADR-014: Deterministic People Roster (TC Members and WG Chairs)

## Status
**Proposed** (2026-10-19), feature branch `feat/external-sources`.

## Context
Readers keep asking who sits on the Technical Committee and who chairs each working group. The
data is in each group's README, as uniform bullets. Before this ADR, the LLM curator read every
one of those READMEs and kept the roster only on `governance/technical-committee`. All eight WG
pages left the chairs out. A model paraphrasing names is the wrong tool: a missing chair is a gap,
but a hallucinated or misattributed one is a reputational error about a real person.

## Decision
1. **Parse, don't generate.** `aaif_wiki/people.py` extracts rows from `## Members`
   (technical-committee) and `## Chairs` (`wg-*`, `ws-*`) with one regex, the AAIF bullet form:
   `* **[Chair: |Co-Chair: ]Name [TC CHAIR|TC CO-CHAIR] [@handle](url)|(no GitHub)** - Org`.
   Other sections and other roles (secretary, decoys under `## Mission`) are ignored. The term
   line is captured verbatim.
2. **One page, `governance/people`.** It is regenerated on every pipeline run from the newest
   README event per repo. It is written only when the body or the cited events change, so an
   unchanged roster produces no diff.
3. **Cited like everything else.** Every TC/WG block cites the README blob event it came from;
   `sources[]` lists those events. Status stays `draft` (ADR-009).
4. **Owned by code, not the model.** `apply_mutations` refuses any LLM mutation of that slug.
   `uncurated_event_ids` ignores the page's citations, so a README cited by the roster is still
   curated into its WG page.
5. **AAIF only.** Events labelled `external` (ADR-013) never feed the roster.

## Consequences
- The roster can't contain a name that isn't in a README. If a README changes format, the group
  drops out of the table (visible in review) instead of being guessed at.
- Group members beyond chairs are not listed: AAIF does not publish WG membership in git.
- Verified on 2026-10-19: 8 TC members plus 16 chair seats across 8 groups, matching GitHub
  HEAD and https://aaif.io/tc.
