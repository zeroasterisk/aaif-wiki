"""Deterministic people roster: TC members and working-group chairs (ADR-014).

Names are facts, not prose. The LLM curator summarises WG READMEs but routinely
drops or paraphrases the roster, and a hallucinated name is worse than a missing
one. So the roster is parsed straight from the committed README bullets that AAIF
uses for this, with every row cited to the event (blob) it came from:

    * **Chair: Alex Frazer [@awfrazer](https://github.com/awfrazer)** - Runlayer
    * **Caitie McCaffrey [TC CO-CHAIR] [@CaitieM20](https://github.com/CaitieM20)** - Microsoft
    * **Chair: Ryan Hagemann (no GitHub)** - IBM

Only AAIF repos are read (never ADR-013 external sources).
"""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime

from .models import Actor, Concept, ConceptSource, ConceptStatus, RawEvent, SourceType

SLUG = "governance/people"
ACTOR = "agent:aaif-wiki-people/deterministic"

# "* **[Role: ]Name [TAG] [@handle](url)|(no GitHub)** - Org"
ROW_RE = re.compile(
    r"^\s*[*-]\s+\*\*\s*"
    r"(?:(?P<role>Co-Chair|Chair)\s*:\s*)?"
    r"(?P<name>[^\[\]()*@]+?)\s*"
    r"(?:\[(?P<tag>TC (?:CO-)?CHAIR)\]\s*)?"
    r"(?:\[@(?P<handle>[A-Za-z0-9-]+)\]\([^)]*\)|\(no GitHub\))?\s*"
    r"\*\*\s*[-–—]\s*(?P<org>.+?)\s*$"
)
TERM_RE = re.compile(r"Current term for (?:the )?[\w ]+? is \*\*(?P<term>[^*]+)\*\*")
TITLE_RE = re.compile(r"^#\s+(?P<title>.+?)\s*$", re.MULTILINE)
SECTION_RE = re.compile(r"^##\s+(?P<h>.+?)\s*$", re.MULTILINE)


@dataclass(frozen=True)
class Person:
    name: str
    org: str
    role: str  # "TC Chair" | "TC Co-Chair" | "TC Member" | "Chair" | "Co-Chair"
    handle: str | None = None


@dataclass
class Group:
    repo: str  # bare repo name, e.g. wg-security-and-privacy
    title: str
    people: list[Person]
    term: str | None
    event: RawEvent


def _section(text: str, heading: str) -> str | None:
    """Body of the first `## <heading>` section (case-insensitive)."""
    matches = list(SECTION_RE.finditer(text))
    for i, m in enumerate(matches):
        if m.group("h").strip().lower() == heading.lower():
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            return text[m.end() : end]
    return None


def parse_rows(block: str, *, tc: bool) -> list[Person]:
    out: list[Person] = []
    for line in block.splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        name = " ".join(m.group("name").split())
        if tc:
            tag = (m.group("tag") or "").upper()
            role = {"TC CHAIR": "TC Chair", "TC CO-CHAIR": "TC Co-Chair"}.get(tag, "TC Member")
        else:
            if not m.group("role"):
                continue  # a WG README bullet that is not a chair row
            role = m.group("role")
        out.append(Person(name=name, org=m.group("org").strip(), role=role, handle=m.group("handle")))
    return out


def parse_readme(repo: str, text: str, event: RawEvent) -> Group | None:
    tc = repo == "technical-committee"
    block = _section(text, "Members" if tc else "Chairs")
    if block is None:
        return None
    people = parse_rows(block, tc=tc)
    if not people:
        return None
    title = TITLE_RE.search(text)
    term = TERM_RE.search(text)
    return Group(
        repo=repo,
        title=(title.group("title") if title else repo),
        people=people,
        term=term.group("term").strip() if term else None,
        event=event,
    )


def _bare(repository: str) -> str:
    return repository.split("/", 1)[1] if "/" in repository else repository


def is_roster_repo(name: str) -> bool:
    return name == "technical-committee" or name.startswith(("wg-", "ws-"))


def latest_readmes(events: list[RawEvent]) -> dict[str, RawEvent]:
    """Newest README.md file event per AAIF governance repo."""
    latest: dict[str, RawEvent] = {}
    for e in events:
        if e.source_type is not SourceType.REPO_FILE or e.reference_id != "README.md":
            continue
        if "external" in e.labels:
            continue
        name = _bare(e.repository)
        if not is_roster_repo(name):
            continue
        if name not in latest or e.timestamp >= latest[name].timestamp:
            latest[name] = e
    return latest


def collect(events: list[RawEvent], rehydrate: Callable[[RawEvent], str | None]) -> list[Group]:
    groups: list[Group] = []
    for name, event in sorted(latest_readmes(events).items()):
        text = rehydrate(event)
        if not text:
            continue
        g = parse_readme(name, text, event)
        if g:
            groups.append(g)
    return groups


def _wg_slug(repo: str) -> str:
    """wg-security-and-privacy -> working-groups/security-and-privacy."""
    base = repo.split("-", 1)[1] if repo.startswith(("wg-", "ws-")) else repo
    if repo == "ws-taxonomy-landscape":
        base = "taxonomy-and-landscape"
    return f"working-groups/{base}"


def _gh(p: Person) -> str:
    return f"[@{p.handle}](https://github.com/{p.handle})" if p.handle else "—"


def build_concept(groups: list[Group], known_slugs: set[str], now: datetime | None = None) -> Concept | None:
    tc = next((g for g in groups if g.repo == "technical-committee"), None)
    wgs = [g for g in groups if g.repo != "technical-committee"]
    if not tc and not wgs:
        return None

    def cite(g: Group) -> str:
        return f"[^{g.event.event_id}]"

    lines = [
        "# Overview",
        "",
        "Who leads the Agentic AI Foundation's technical work: the members of the Technical",
        "Committee (TC) and the chairs of each working group and workstream, parsed",
        "verbatim from each group's README. This page is generated deterministically (no",
        "language model); every row cites the README revision it came from.",
        "",
    ]
    if tc:
        lines += ["# Technical Committee", ""]
        if tc.term:
            lines += [f"Term: {tc.term}. {cite(tc)}", ""]
        lines += ["| Name | Role | Organization | GitHub |", "|---|---|---|---|"]
        order = {"TC Chair": 0, "TC Co-Chair": 1, "TC Member": 2}
        for p in sorted(tc.people, key=lambda p: (order[p.role], p.name)):
            lines.append(f"| {p.name} | {p.role} | {p.org} | {_gh(p)} |")
        lines += ["", f"Source: technical-committee README. {cite(tc)}", ""]
    if wgs:
        lines += [
            "# Working Group and Workstream Chairs",
            "",
            "| Group | Chair | Co-Chair | Term |",
            "|---|---|---|---|",
        ]
        for g in sorted(wgs, key=lambda g: g.title):
            slug = _wg_slug(g.repo)
            label = f"[{g.title}](../{slug}.md)" if slug in known_slugs else g.title
            def fmt(role: str, g: Group = g) -> str:
                return "; ".join(
                    f"{p.name} ({p.org}) {_gh(p)}" for p in g.people if p.role == role
                ) or "—"

            lines.append(f"| {label} | {fmt('Chair')} | {fmt('Co-Chair')} | {g.term or '—'} {cite(g)} |")
        lines.append("")
    lines += [
        "# References",
        "",
        "- AAIF Technical Committee page: https://aaif.io/tc",
        "- [Technical Committee](technical-committee.md)",
        "",
    ]

    sources = [
        ConceptSource(
            id=g.event.event_id,
            resource=g.event.url or "",
            author=g.event.author,
            last_modified=g.event.timestamp,
        )
        for g in ([tc] if tc else []) + sorted(wgs, key=lambda g: g.repo)
    ]
    return Concept(
        type="governance",
        title="People: Technical Committee and Working Group Chairs",
        description=(
            f"Roster of the AAIF Technical Committee ({len(tc.people) if tc else 0} members) and the "
            f"chairs of {len(wgs)} working groups and workstreams, parsed from their READMEs."
        ),
        resource="https://aaif.io/tc",
        tags=["governance", "people", "technical-committee", "working-groups", "chairs"],
        status=ConceptStatus.DRAFT,
        generated=Actor(by=ACTOR, at=now or datetime.now(UTC)),
        sources=sources,
        slug=SLUG,
        body="\n".join(lines),
    )
