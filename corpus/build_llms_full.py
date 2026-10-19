#!/usr/bin/env python3
"""
Build content/llms-full.txt: one file an LLM can fetch to assess Rohit's work
without following links.

  - Full text: About, Work With Me, CV, Portfolio case studies, and every essay
    in Articles/institutions (the current focus).
  - Catalog: every other essay as title, date, URL and description.

Run:  python3 corpus/build_llms_full.py
"""

import os
import re
import sys

from build_index import CONTENT, BASE_URL, as_list, parse_frontmatter, slugify

OUT = os.path.join(CONTENT, "llms-full.txt")

PROFILE_PAGES = ["about.md", "work-with-me.md", "cv.md"]
FULL_TEXT_DIRS = ["Portfolio", os.path.join("Articles", "institutions")]
CATALOG_DIR = "Articles"

HEADER = """# Rohit Malekar

> Research, essays, and selected work on Ethereum in institutional finance, coordination and public goods, product craft, and living well.

This is the full-text companion to https://rohitmalekar.in/llms.txt. It holds Rohit's profile, CV, case studies and his essays on Ethereum in institutional finance in full, followed by a catalog of every other essay with its URL and summary. Fetch a catalog URL to read that essay in full.
"""


def load(relpath):
    text = open(os.path.join(CONTENT, relpath), encoding="utf-8").read()
    fm, body = parse_frontmatter(text)
    return fm, body


def url_for(relpath, fm):
    if fm.get("permalink"):
        return f"{BASE_URL}/{fm['permalink'].strip('/')}"
    stem = relpath[:-3]
    return BASE_URL + "/" + "/".join(slugify(p) for p in stem.split(os.sep))


def to_plain_markdown(body):
    """Keep the prose and headings, drop site furniture."""
    b = re.sub(r"<[^>]+>", "", body)                              # html
    b = re.sub(r"!\[\[[^\]]*\]\]", "", b)                          # embedded images
    b = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", b)                     # md images
    b = re.sub(r"\[\[([^\]|]*)\|([^\]]*)\]\]", r"\2", b)           # wikilink w/ alias
    b = re.sub(r"\[\[([^\]#]*)(#[^\]]*)?\]\]", r"\1", b)          # wikilink
    b = re.sub(r"^#{1,6}\s", lambda m: "#" + m.group(0), b, flags=re.M)  # demote under page heading
    b = re.sub(r"\n{3,}", "\n\n", b)
    return b.strip()


def full_text_entry(relpath):
    fm, body = load(relpath)
    title = fm.get("title") or os.path.basename(relpath)[:-3]
    lines = [f"## {title}", "", f"URL: {url_for(relpath, fm)}"]
    if fm.get("date"):
        lines.append(f"Date: {fm['date']}")
    lines += ["", to_plain_markdown(body), ""]
    return "\n".join(lines)


def md_files(reldir):
    out = []
    for root, dirs, files in os.walk(os.path.join(CONTENT, reldir)):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in files:
            if f.endswith(".md") and f != "index.md":
                out.append(os.path.relpath(os.path.join(root, f), CONTENT))
    return out


def by_date_desc(paths):
    return sorted(paths, key=lambda p: str(load(p)[0].get("date") or ""), reverse=True)


def main():
    parts = [HEADER, "# Profile", ""]
    parts += [full_text_entry(p) for p in PROFILE_PAGES]

    full_text = set()
    for d in FULL_TEXT_DIRS:
        index_fm, _ = load(os.path.join(d, "index.md"))
        parts += [f"# {index_fm.get('title') or d}", ""]
        for p in by_date_desc(md_files(d)):
            parts.append(full_text_entry(p))
            full_text.add(p)

    parts += ["# Catalog of other essays", ""]
    themes = sorted(
        d for d in os.listdir(os.path.join(CONTENT, CATALOG_DIR))
        if os.path.isdir(os.path.join(CONTENT, CATALOG_DIR, d))
    )
    count = 0
    for theme in themes:
        reldir = os.path.join(CATALOG_DIR, theme)
        paths = [p for p in by_date_desc(md_files(reldir)) if p not in full_text]
        if not paths:
            continue
        index_fm, _ = load(os.path.join(reldir, "index.md"))
        parts += [f"## {index_fm.get('title') or theme}", ""]
        for p in paths:
            fm, _ = load(p)
            title = fm.get("title") or os.path.basename(p)[:-3]
            date = fm.get("date") or "undated"
            desc = to_plain_markdown(" ".join(as_list(fm.get("description"))))
            desc = re.sub(r"\s+", " ", re.sub(r"[*_]{2,}|\[\[", "", desc))
            line = f"- [{title}]({url_for(p, fm)}) ({date})"
            parts.append(f"{line}: {desc}" if desc else line)
            count += 1
        parts.append("")

    open(OUT, "w", encoding="utf-8").write("\n".join(parts).rstrip() + "\n")
    size = os.path.getsize(OUT)
    print(f"{len(full_text) + len(PROFILE_PAGES)} pages in full, {count} in catalog -> content/llms-full.txt "
          f"({size/1024:.0f} KB, ~{size//4:,} tokens)")


if __name__ == "__main__":
    sys.exit(main())
