"""Compact definitions for catalogue departments.

Each department lists its roles one per line::

    name | Title | Mission sentence(s). | deliverable_a, deliverable_b [| tiers]

``tiers`` is optional and overrides the department default. It is one of
``r``, ``rw``, ``rx``, ``rwx``, optionally followed by ``+web`` for agents
that may research on the internet (when the run allows it).
"""

from __future__ import annotations

from dataclasses import dataclass

TIER_CODES = {
    "r": {"read"},
    "rw": {"read", "write"},
    "rx": {"read", "exec"},
    "rwx": {"read", "write", "exec"},
}


@dataclass(frozen=True)
class Role:
    name: str
    title: str
    mission: str
    deliverables: tuple[str, ...]
    tiers: frozenset[str]


@dataclass(frozen=True)
class Department:
    name: str
    label: str
    description: str
    roles: str
    tiers: str = "rw"
    light: bool = False
    # Regulated domains: outputs are drafts for qualified professionals.
    regulated: bool = False

    def parse(self) -> list[Role]:
        out: list[Role] = []
        for lineno, raw in enumerate(self.roles.strip().splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split("|")]
            if len(parts) not in (4, 5):
                raise ValueError(f"{self.name} line {lineno}: expected 4 or 5 fields, got {len(parts)}: {line!r}")
            name, title, mission, deliverables = parts[:4]
            code = parts[4] if len(parts) == 5 else self.tiers
            out.append(Role(
                name=name,
                title=title,
                mission=mission,
                deliverables=tuple(d.strip() for d in deliverables.split(",") if d.strip()),
                tiers=frozenset(parse_tiers(code)),
            ))
        return out


def parse_tiers(code: str) -> set[str]:
    base, _, extra = code.partition("+")
    if base not in TIER_CODES:
        raise ValueError(f"Unknown tier code '{code}'")
    tiers = set(TIER_CODES[base])
    if extra:
        if extra != "web":
            raise ValueError(f"Unknown tier extra '+{extra}'")
        tiers.add("web")
    return tiers
