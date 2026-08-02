#!/usr/bin/env python3
"""
Build a compact, context-loadable index of the digital garden.

Reads every markdown file under content/ and emits:
  corpus/index.txt  -- one 2-line record per note: metadata + thesis. Small
                       enough to load whole, rich enough to select from.
  corpus/links.txt  -- wikilink graph, grepped on demand to expand a shortlist.

Run:  python3 corpus/build_index.py
"""

import os
import re
import sys
import json
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
OUT_DIR = os.path.join(ROOT, "corpus")
BASE_URL = "https://rohitmalekar.in"

SKIP_DIRS = {".obsidian", "Attachments", "Drafts", "temp"}
SKIP_FILES = {"index.md", "llms.txt", "robots.txt"}

THESIS_WORDS = 30


# ---------- helpers ----------

def slugify(text):
    """Quartz's slugifier: lowercase, '&'->'and', whitespace->'-'. Punctuation is kept.
    Verified against the built site: 'A - B & C' -> 'a---b--and--c'."""
    s = text.lower().replace("&", " and ")
    return re.sub(r"\s", "-", s)


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    if not m:
        return {}, text
    raw, body = m.group(1), text[m.end():]
    fm, key, buf = {}, None, []

    def flush():
        if key:
            fm[key] = buf[:] if buf else fm.get(key, "")

    for line in raw.split("\n"):
        if re.match(r"^\S.*?:", line):
            flush()
            k, _, v = line.partition(":")
            key, buf = k.strip(), []
            v = v.strip()
            if v:
                if v.startswith("[") and v.endswith("]"):
                    fm[key] = [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
                    key, buf = None, []
                else:
                    fm[key] = v.strip("\"'")
                    key, buf = None, []
        elif key and re.match(r"^\s*-\s+", line):
            buf.append(re.sub(r"^\s*-\s+", "", line).strip().strip("\"'"))
        elif key and line.strip() and not line.startswith(" "):
            flush()
            key, buf = None, []
    flush()
    return fm, body


def as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def clean_body(body):
    """Strip the furniture so the first real sentence surfaces."""
    b = body
    b = re.sub(r"<[^>]+>", " ", b)                      # html
    b = re.sub(r"!\[.*?\]\(.*?\)", " ", b)              # images
    b = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", b)      # md links -> text
    b = re.sub(r"\[\[([^\]|]*)\|([^\]]*)\]\]", r"\2", b)  # wikilink w/ alias
    b = re.sub(r"\[\[([^\]]*)\]\]", r"\1", b)           # wikilink
    b = re.sub(r"^\s*>.*$", " ", b, flags=re.M)         # blockquotes
    b = re.sub(r"^#+\s*", "", b, flags=re.M)            # headings
    b = re.sub(r"[*_`]", "", b)
    return b


def first_paragraph(body):
    b = clean_body(body)
    for para in [p.strip() for p in b.split("\n\n")]:
        if not para:
            continue
        # skip editorial preambles like "(This essay is part of a series...)"
        if para.startswith("(") and para.endswith(")"):
            continue
        if len(para.split()) < 6:
            continue
        return re.sub(r"\s+", " ", para)
    flat = re.sub(r"\s+", " ", b).strip()
    return flat


def truncate(text, n=THESIS_WORDS):
    words = text.split()
    if len(words) <= n:
        return text
    return " ".join(words[:n]).rstrip(",;:") + "…"


def public_url(relpath):
    """Quartz slugs the file path, not the frontmatter title."""
    stem = relpath[:-3] if relpath.endswith(".md") else relpath
    return BASE_URL + "/" + "/".join(slugify(p) for p in stem.split(os.sep))


IMG = re.compile(r"\.(png|jpe?g|gif|webp|svg|pdf)$", re.I)


def extract_links(body):
    out = set()
    for m in re.findall(r"\[\[([^\]]+)\]\]", body):
        target = re.sub(r"#.*$", "", m.split("|")[0]).strip()
        if target and not IMG.search(target):
            out.add(target)
    return sorted(out)


# ---------- walk ----------

def collect():
    records = []
    for root, dirs, files in os.walk(CONTENT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for f in sorted(files):
            if not f.endswith(".md") or f in SKIP_FILES:
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, CONTENT)
            text = open(path, encoding="utf-8", errors="ignore").read()
            fm, body = parse_frontmatter(text)

            title = fm.get("title") or os.path.splitext(f)[0]
            if isinstance(title, list):
                title = title[0]

            desc = fm.get("description")
            if isinstance(desc, list):
                desc = " ".join(desc)
            thesis = truncate(re.sub(r"\s+", " ", desc).strip()) if desc else truncate(first_paragraph(body))

            typ = as_list(fm.get("type"))
            typ = typ[0] if typ else ("Article" if rel.startswith("Articles") else "Note")

            records.append({
                "title": title,
                "path": os.path.join("content", rel),
                "section": os.path.dirname(rel).replace(os.sep, "/") or "root",
                "type": typ,
                "date": str(fm.get("date", ""))[:10],
                "tags": as_list(fm.get("tags")),
                "words": len(body.split()),
                "url": public_url(rel),
                "thesis": thesis,
                "links": extract_links(body),
            })
    return records


def main():
    recs = collect()
    recs.sort(key=lambda r: (r["date"] or "0000", r["title"]), reverse=True)
    os.makedirs(OUT_DIR, exist_ok=True)

    today = date.today().isoformat()
    lines = [
        f"# CORPUS INDEX — generated {today} — {len(recs)} notes, newest first",
        "# Record = 2 lines:  TITLE ~ type ~ date ~ tags ~ words ~ path-under-content/",
        "#                    thesis",
        "# Read full text with: content/<path>. Public URLs live in corpus/index.jsonl.",
        "",
    ]
    for r in recs:
        tags = ",".join(r["tags"]) or "-"
        short = r["path"][len("content/"):] if r["path"].startswith("content/") else r["path"]
        lines.append(f'{r["title"]} ~ {r["type"]} ~ {r["date"] or "undated"} ~ {tags} ~ {r["words"]}w ~ {short}')
        lines.append(f'  {r["thesis"]}')
    open(os.path.join(OUT_DIR, "index.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")

    link_lines = [f'# WIKILINK GRAPH — generated {today}', ""]
    for r in recs:
        if r["links"]:
            link_lines.append(f'{r["title"]} -> {"; ".join(r["links"])}')
    open(os.path.join(OUT_DIR, "links.txt"), "w", encoding="utf-8").write("\n".join(link_lines) + "\n")

    with open(os.path.join(OUT_DIR, "index.jsonl"), "w", encoding="utf-8") as fh:
        for r in recs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    size = os.path.getsize(os.path.join(OUT_DIR, "index.txt"))
    print(f"{len(recs)} notes indexed → corpus/index.txt ({size/1024:.0f} KB, ~{size//4:,} tokens)")
    print(f"date range: {min(r['date'] for r in recs if r['date'])} → {max(r['date'] for r in recs if r['date'])}")
    undated = [r["title"] for r in recs if not r["date"]]
    if undated:
        print(f"undated ({len(undated)}): {', '.join(undated[:8])}")


if __name__ == "__main__":
    sys.exit(main())
