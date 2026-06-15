#!/usr/bin/env python3
"""
Backfills a `date:` field in YAML frontmatter for articles that only have
a "Last Updated" line in the body and no date in frontmatter.
"""

import re
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

FILES = [
    "content/Articles/coordination/Three features I would pay for in a sufficiently decentralized social network.md",
    "content/Articles/coordination/Predicting Public Goods Funding Using Reward Distribution Curves - An Exploratory Approach.md",
    "content/Articles/living-well/Retrospective from Surviving A 300 km Cycling Ride.md",
    "content/Articles/living-well/The Era of Digital Distraction - A Co-Production by All of Us.md",
    "content/Articles/living-well/My Experiments to Crack the Code of Deep Sleep.md",
    "content/Articles/living-well/The Physics of Desire.md",
    "content/Articles/living-well/Consistency Compounds - Insights from 6 Years of Cycling Data.md",
    "content/Articles/living-well/AI Can Solve Your Problems. It Can’t Build You..md",
    "content/Articles/living-well/Decoding Quality of Life.md",
    "content/Articles/living-well/The Mind's Terms of Service.md",
    "content/Articles/living-well/The Utility of Marriage.md",
    "content/Articles/living-well/The Life You Live Is Shaped by the Words You Use.md",
    "content/Articles/living-well/You Can’t Outrun a Misaligned Life.md",
    "content/Articles/living-well/Don't Ignore the Fascists, They Won't Ignore You.md",
    "content/Articles/living-well/Why 99% of the Self-Help Industry Is Slop - Gust Against Gravity.md",
    "content/Articles/living-well/Purpose.exe - Not Found.md",
    "content/Articles/living-well/Why Gada Training Became My Secret Weapon for Long-Distance Cycling.md",
    "content/Articles/living-well/The Anomalies of Attraction.md",
    "content/Articles/living-well/The Quiet Epidemic of Checking Out at Home.md",
    "content/Articles/art-of-work/The Clock We Didn't Watch - India's Demographic Dividend.md",
    "content/Articles/art-of-work/AI as Amplifier - Three Shifts That Change How You Work.md",
    "content/Articles/art-of-work/The Infrastructure for Insight - Cultivating Personal Judgement in the Age of Generation.md",
    "content/Articles/building-better-orgs/The Hidden Economics Behind Enterprise Software Choices.md",
    "content/Articles/building-better-orgs/The Next Frontier for Indian Startups - Sequoias and Meadows.md",
]

DATE_FORMATS = [
    "%B, %Y",   # January, 2026
    "%B %Y",    # January 2026
    "%b, %Y",   # Jan, 2026
    "%b %Y",    # Jan 2026
]

BODY_PATTERN = re.compile(
    r'^[*_]?Last [Uu]pdated:\s*(.+?)[*_]?\s*$',
    re.MULTILINE,
)


def parse_date(raw: str) -> str:
    raw = raw.strip().strip("*_")
    for fmt in DATE_FORMATS:
        try:
            dt = datetime.strptime(raw.strip(), fmt)
            return dt.strftime("%Y-%m-01")
        except ValueError:
            continue
    raise ValueError(f"Cannot parse date: {raw!r}")


def process(path: Path) -> None:
    text = path.read_text(encoding="utf-8")

    m = BODY_PATTERN.search(text)
    if not m:
        print(f"  SKIP (no Last Updated line found): {path.name}")
        return

    date_str = parse_date(m.group(1))

    # Find the closing --- of frontmatter
    if not text.startswith("---"):
        print(f"  SKIP (no frontmatter): {path.name}")
        return

    end_fm = text.index("\n---", 3)  # find closing ---
    insert_pos = end_fm  # insert just before closing ---

    new_text = text[:insert_pos] + f"\ndate: {date_str}" + text[insert_pos:]
    path.write_text(new_text, encoding="utf-8")
    print(f"  OK  date: {date_str}  ← {m.group(1).strip()}  [{path.name}]")


def main():
    errors = []
    for rel in FILES:
        path = REPO_ROOT / rel
        if not path.exists():
            print(f"  MISSING: {rel}")
            errors.append(rel)
            continue
        try:
            process(path)
        except Exception as e:
            print(f"  ERROR {path.name}: {e}")
            errors.append(rel)

    if errors:
        print(f"\n{len(errors)} error(s). Fix before Phase 2.")
        sys.exit(1)
    else:
        print(f"\nAll {len(FILES)} files processed successfully.")


if __name__ == "__main__":
    main()
