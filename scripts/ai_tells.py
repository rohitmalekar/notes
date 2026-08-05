#!/usr/bin/env python3
"""
Audit content/ for tell-tale signs of AI-assisted writing.

The point of calibration: the pre-2023 corpus was written before LLM writing tools
existed, so whatever rate of em-dashes, "leverage/foster/navigate", and one-line
paragraphs it shows is Rohit's own voice, not a fingerprint. Every detector is scored
as an excursion above that baseline, and the flag threshold is the 90th percentile
score of the provably-human cohort.

Emits playbook/ai-tells-audit.md -- a ranked, checkbox todo list with quoted evidence
and absolute line numbers, for manual correction.

Run:  python3 scripts/ai_tells.py
"""

import os
import re
import sys
import statistics
from datetime import date
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
OUT = os.path.join(ROOT, "playbook", "ai-tells-audit.md")

sys.path.insert(0, os.path.join(ROOT, "corpus"))
from build_index import parse_frontmatter  # noqa: E402

# Unlike the corpus builder we DO want index.md, Drafts/ and Portfolio/ -- the site
# copy is some of the most AI-inflected prose in the repo.
SKIP_DIRS = {".obsidian", "Attachments", "temp"}

BASELINE_CUTOFF = "2023-01-01"
MAX_EXAMPLES = 4
MIN_PROSE = 120  # below this there's no draft to fix, only a line to delete


# ---------- detectors ----------
# (key, weight, human-readable label, regex)

DETECTORS = [
    ("not-X-its-Y", 4, '"It\'s not X — it\'s Y"',
     r"\b(?:It'?s|That'?s|This is|It is)\s+not\s+(?:just|only|merely)?[^.?!\n]{3,70}[,;—–.]\s*(?:it'?s|that'?s|this is|It'?s|That'?s|This is)\b"),
    ("isnt-about", 4, '"X isn\'t about A. It\'s about B."',
     r"\b(?:is|are|was|were)(?:n'?t| not)\s+about\s"),
    ("isnt-just", 3, '"isn\'t just / not merely"',
     r"\b(?:is|are|was|were|do|does|did)(?:n'?t| not)\s+(?:just|only|merely)\s"),
    ("neg-triad", 4, '"Not because X, not because Y, but because Z"',
     r"[Nn]ot because[^.?!\n]{2,90},?\s*not because[^.?!\n]{2,90},?\s*but because"),
    ("heres-the", 4, '"Here\'s the thing / why / what most people miss"',
     r"\bHere'?s (?:the|why|what|how|where)\b"),
    ("thats-the-point", 3, '"And that\'s the point" / "that changes everything"',
     r"\b(?:And )?that'?s (?:exactly )?the point\b|\bthat changes everything\b"),
    ("from-to-to", 2, '"From X to Y to Z" (range without specifics)',
     r"\bFrom [^.,;:\n]{2,35} to [^.,;:\n]{2,35} to [^.,;:\n]{2,35}"),
    ("whether-youre", 3, '"Whether you\'re a beginner or…"',
     r"\bWhether you'?re\b"),
    ("worth-noting", 3, '"It\'s worth noting / important to remember"',
     r"\bIt'?s (?:worth noting|important to (?:remember|note|understand))\b"),
    ("in-todays-era", 4, '"In today\'s… / In an era of… / In the age of…"',
     r"\bIn (?:today'?s|an era|a world|the age)\b"),
    ("not-only-but", 2, '"not only … but also"',
     r"\bnot only\b[^.\n]{2,90}\bbut also\b"),
    ("para-glue", 1, 'paragraph glue ("That said," / "Ultimately," / "Moreover,")',
     r"(?m)^\s*(?:That said,|Ultimately,|Moreover,|Furthermore,|In essence,|Importantly,)"),
    ("buzz", 4, '"game-changer" / "deep dive" / "at the intersection of"',
     r"\bgame[- ]chang(?:er|ing)\b|\bdeep dive\b|\bat the intersection of\b"),
    ("in-conclusion", 4, '"In conclusion / To sum up / In summary"',
     r"(?m)^\s*(?:\*\*)?(?:In conclusion|To sum up|In summary)\b"),
    ("uplift-close", 3, 'uplifting forward-looking close',
     r"(?:continues to evolve|as the (?:field|world|space|industry)\b[^.\n]{0,40}(?:evolv|chang|matur)|journey (?:is just|has only)|only just beginning|the future (?:belongs|is)\b)"),
    ("gerund-tail", 2, 'trailing gerund clause (", making it a powerful tool for…")',
     r",\s+(?:making|creating|allowing|ensuring|enabling|providing|helping|turning|leaving|offering|driving|fostering|transforming|shaping|reflecting|highlighting|underscoring|reinforcing|positioning)\b[^.\n]{3,90}[.]"),
    ("vocab", 2, 'LLM vocabulary (delve, robust, crucial, leverage, foster, navigate…)',
     r"\b(?:delve\w*|tapestry|testament|landscape|realm|nuanced|robust|pivotal|crucial|seamless(?:ly)?|underscor\w+|leverag\w+|foster\w*|navigat\w+|harness\w*|unlock\w*|elevat\w+|myriad|plethora)\b"),
    ("emoji-head", 3, 'emoji-headed section',
     r"(?m)^#{1,6} .*[\U0001F300-\U0001FAFF✨✅⚡].*$"),
]

BOLD_LIST = re.compile(r"(?m)^[ \t]*(?:[-*+]|\d+[.)])\s+\*\*[^*\n]{2,90}\*\*\s*[:—–-]")
RHET_Q = re.compile(
    r"(?m)^([^\n>#|*\-][^\n]{5,140}\?)\n\n((?:It|That|The answer|Because|Yes|No|Not|Partly|Mostly|Simple)\b[^\n]{5,200})$"
)
STUB_LINK = re.compile(
    r"Access the (?:complete )?article|web\.archive|Read the (?:full|complete) article|paragraph\.xyz|originally published",
    re.I,
)
DESC_FRAME = re.compile(
    r"^(?:This (?:article|post|essay|piece|write-up)\b|In this (?:article|post)\b|The article\b)"
    r"|\bhighlights the importance\b|\bdiscusses\b",
    re.I,
)
DESC_BLURB = re.compile(
    r"\bthis (?:piece|essay|article|post|note) (?:explores|examines|argues|unpacks|traces|makes)\b"
    r"|\b(?:explores|examines|unpacks) (?:how|why|what|where)\b",
    re.I,
)
DESC_VOCAB = re.compile(
    r"\b(?:delve\w*|underscor\w+|crucial|seamless\w*|foster\w*|leverag\w+|empower\w*)\b", re.I
)
# Rhetorical shapes borrowed from the body detectors — unambiguous enough to apply to
# a one-line description.
DESC_RHETORIC = [k for k in ("not-X-its-Y", "isnt-about", "isnt-just", "in-todays-era",
                             "from-to-to", "whether-youre", "not-only-but", "gerund-tail")]


def classify_desc(d):
    """Return (tier, reason) or None.

    A single tell-word isn't enough on its own: several descriptions are Rohit's own
    opening paragraph, which is allowed to say "crucial". Those go in a second tier for
    a human to glance at rather than being silently included or silently dropped — each
    one is five seconds to eyeball, and a miss ships into every search result.
    """
    if not d:
        return None
    frame = DESC_FRAME.search(d)
    vocab = sorted({m.group(0).lower() for m in DESC_VOCAB.finditer(d)})
    if frame:
        return "strong", f'opens as a summary — "{frame.group(0)}"'
    blurb = DESC_BLURB.search(d)
    if blurb:
        return "strong", f'"{blurb.group(0)}…" — the shared template'
    if len(vocab) >= 2:
        return "strong", "LLM vocabulary: " + ", ".join(vocab)
    for key, _w, label, rx in DETECTORS:
        if key in DESC_RHETORIC and re.search(rx, d):
            return "possible", f"reads like body copy — {label}"
    if vocab:
        return "possible", f'single tell-word: "{vocab[0]}"'
    return None

WORD = re.compile(r"[A-Za-z][A-Za-z'’-]*")


# ---------- text prep ----------

def mask(raw):
    """Blank frontmatter, code, quotes and link targets while preserving line numbers.

    Detectors run against the masked *full* text so match offsets convert straight to
    absolute line numbers in the file. Blockquotes go too: quoting Huxley or the
    Upanishads shouldn't count against Rohit.
    """
    chars = list(raw)

    def blank(a, b):
        for i in range(a, b):
            if chars[i] != "\n":
                chars[i] = " "

    m = re.match(r"^---\n.*?\n---\n?", raw, re.S)
    if m:
        blank(*m.span())
    for pat in (r"(?ms)^```.*?^```", r"(?m)^\s*>.*$", r"\]\([^)\n]*\)", r"https?://\S+", r"`[^`\n]+`"):
        for m in re.finditer(pat, raw):
            blank(*m.span())
    return "".join(chars)


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def snippet(s, n=95):
    s = re.sub(r"\s+", " ", s).strip().replace("`", "'")
    return s[:n] + ("…" if len(s) > n else "")


SENTENCE_ITEM = 12  # words


def prose_only(masked):
    """Drop headings, tables, and list items too short to be written sentences.

    The line to draw isn't list-vs-paragraph. `off-the-track/BRM Checklist.md` is a gear
    list ("Charge lights", "Helmet") where an em-dash is notation, while `work-with-me.md`
    is a sales page whose every bullet is a full sentence — the bulleted list *is* the copy.
    Keep items that read as sentences; blank the rest. Line numbers are preserved either way.
    """
    out = []
    for line in masked.split("\n"):
        if re.match(r"^\s*(?:#{1,6}\s|\|)", line) or re.match(r"^\s*(?:[-*+]|\d+[.)])\s*\[[ x]\]", line):
            out.append(" " * len(line))
        elif re.match(r"^\s*(?:[-*+]|\d+[.)])\s", line):
            text = re.sub(r"\[\[[^\]]*\]\]|\*\*|[•·]", " ", line)
            out.append(line if len(WORD.findall(text)) >= SENTENCE_ITEM else " " * len(line))
        else:
            out.append(line)
    return "\n".join(out)


def paragraph_lengths(masked_body):
    paras = [p.strip() for p in re.split(r"\n\s*\n", masked_body) if p.strip()]
    paras = [p for p in paras if not re.match(r"^[#>\-*|!\[0-9]", p)]
    return [n for n in (len(WORD.findall(p)) for p in paras) if n]


# ---------- per-file analysis ----------

def analyse(relpath):
    raw = open(os.path.join(CONTENT, relpath), encoding="utf-8", errors="replace").read()
    fm, _ = parse_frontmatter(raw)
    masked = mask(raw)
    fm_match = re.match(r"^---\n.*?\n---\n?", raw, re.S)
    body = masked[fm_match.end():] if fm_match else masked

    words = len(WORD.findall(body))
    if words < 60:
        return None

    hits = Counter()
    ex = defaultdict(list)

    def record(key, m):
        hits[key] += 1
        ex[key].append((line_of(masked, m.start()), snippet(m.group(0))))

    for key, _w, _label, rx in DETECTORS:
        for m in re.finditer(rx, masked):
            record(key, m)
    for m in RHET_Q.finditer(masked):
        record("rhet-q-answer", m)

    # bolded-colon list items, grouped into blocks; 3- and 5-item blocks are the tell
    bold_lines = [line_of(masked, m.start()) for m in BOLD_LIST.finditer(masked)]
    blocks, cur = [], []
    for ln in bold_lines:
        if cur and ln - cur[-1] > 2:
            blocks.append(cur)
            cur = []
        cur.append(ln)
    if cur:
        blocks.append(cur)
    hits["bold-colon-list"] = len(bold_lines)
    parallel = [b for b in blocks if len(b) in (3, 5)]

    prose = prose_only(body)
    prose_words = len(WORD.findall(prose))
    emdash = [line_of(masked, m.start()) for m in re.finditer("—", prose_only(masked))]
    emdash_lines = sorted(set(emdash))

    plens = paragraph_lengths(body)
    oneline = sum(1 for n in plens if n <= 15)
    cv = statistics.pstdev(plens) / statistics.mean(plens) if len(plens) >= 8 else None

    return dict(
        path=relpath,
        words=words,
        prose_words=prose_words,
        date=str(fm.get("date", "") or ""),
        type=(fm.get("type") or [""])[0] if isinstance(fm.get("type"), list) else str(fm.get("type") or ""),
        desc=str(fm.get("description", "") or ""),
        hits=hits,
        ex=ex,
        blocks=blocks,
        parallel=parallel,
        emdash=len(emdash),
        emdash_lines=emdash_lines,
        # A 60-word note with two dashes is not a 33/1k spike. Floor the denominator.
        emdash_rate=len(emdash) / max(prose_words, 250) * 1000,
        oneline_rate=oneline / len(plens) if len(plens) >= 8 else 0.0,
        cv=cv,
        npara=len(plens),
        stub=words < 260 and bool(STUB_LINK.search(body)),
        raw=raw,
    )


WEIGHTS = {k: w for k, w, _l, _r in DETECTORS}
WEIGHTS.update({"rhet-q-answer": 3, "bold-colon-list": 1})
LABELS = {k: l for k, _w, l, _r in DETECTORS}
LABELS.update({
    "rhet-q-answer": "rhetorical question answered immediately",
    "bold-colon-list": "bolded list item + one explanatory sentence",
})


def score(a, base):
    """Weighted tell density, blended geometrically so a 120-word stub with four hits
    doesn't outrank a 2,500-word essay with forty, plus excess-over-baseline evenness."""
    weighted = sum(WEIGHTS[k] * v for k, v in a["hits"].items() if k in WEIGHTS)
    per_k = weighted / max(a["prose_words"], 250) * 1000
    a["weighted"] = weighted
    a["per_k"] = per_k
    # Four dashes is where a habit starts; below that it's one sentence, not a pattern.
    a["em_excess"] = max(0.0, a["emdash_rate"] - base["emdash"]) if a["emdash"] >= 4 else 0.0
    a["ol_excess"] = max(0.0, a["oneline_rate"] - base["oneline"])
    a["evenness"] = max(0.0, base["cv"] - a["cv"]) if a["cv"] is not None else 0.0
    return (
        (weighted ** 0.5) * (min(per_k, 40) ** 0.5) * 0.9
        + a["em_excess"] * 1.5
        + a["ol_excess"] * 25
        + a["evenness"] * 12
    )


def surface(p):
    if p.startswith("Drafts/"):
        return "draft"
    if p.startswith("Notes/"):
        return "note"
    if p.startswith("Portfolio/") or os.path.basename(p) == "index.md" or "/" not in p:
        return "site copy"
    return "essay"


# ---------- report ----------

def evidence(a, base):
    """One bullet per triggered detector, with quoted examples at absolute line numbers."""
    out = []
    ranked = sorted(
        (k for k in a["hits"] if a["hits"][k] and k in WEIGHTS),
        key=lambda k: -(WEIGHTS[k] * a["hits"][k]),
    )
    for k in ranked:
        n = a["hits"][k]
        head = f"- **{LABELS[k]}** ×{n}"
        if k == "bold-colon-list":
            spans = ", ".join(
                f"L{b[0]}–L{b[-1]} ({len(b)} items)" for b in a["blocks"][:5] if len(b) > 1
            ) or ", ".join(f"L{b[0]}" for b in a["blocks"][:5])
            if a["parallel"]:
                head += " — includes " + " and ".join(
                    f"a {len(b)}-item block" for b in a["parallel"][:3]
                ) + " (the exactly-parallel shape)"
            out.append(head)
            out.append(f"  - blocks at {spans}")
            continue
        out.append(head)
        for ln, txt in a["ex"][k][:MAX_EXAMPLES]:
            out.append(f"  - L{ln} `{txt}`")
        if n > MAX_EXAMPLES:
            out.append(f"  - …{n - MAX_EXAMPLES} more")

    if a["em_excess"] > 0.5:
        lines = ", ".join(f"L{n}" for n in a["emdash_lines"][:12])
        more = "…" if len(a["emdash_lines"]) > 12 else ""
        out.append(
            f"- **em-dashes {a['emdash_rate']:.1f}/1k words** — {a['emdash']} of them "
            f"(your pre-2023 baseline: {base['emdash']:.1f}/1k)"
        )
        out.append(f"  - {lines}{more}")
    if a["ol_excess"] > 0.04:
        out.append(
            f"- **one-line paragraphs {a['oneline_rate']*100:.0f}%** of {a['npara']} paragraphs "
            f"(baseline {base['oneline']*100:.0f}%) — the drama beat, used constantly"
        )
    if a["evenness"] > 0.04:
        out.append(
            f"- **paragraph lengths unusually even** (CV {a['cv']:.2f} vs baseline {base['cv']:.2f}) — "
            "no paragraph runs long because you got going"
        )
    return out


def main():
    files = []
    for dirpath, dirnames, filenames in os.walk(CONTENT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(".md"):
                files.append(os.path.relpath(os.path.join(dirpath, fn), CONTENT))
    files.sort()

    docs = [d for d in (analyse(f) for f in files) if d]
    for d in docs:
        d["baseline"] = bool(d["date"]) and d["date"] < BASELINE_CUTOFF
    baseline_docs = [d for d in docs if d["baseline"]]
    scan_docs = [d for d in docs if not d["baseline"]]

    if not baseline_docs:
        sys.exit("no pre-2023 files found — cannot calibrate")

    bw = sum(d["prose_words"] for d in baseline_docs) / 1000
    base = {
        "n": len(baseline_docs),
        "words": sum(d["prose_words"] for d in baseline_docs),
        "emdash": sum(d["emdash"] for d in baseline_docs) / bw,
        "oneline": statistics.mean([d["oneline_rate"] for d in baseline_docs if d["npara"] >= 8]),
        "cv": statistics.mean([d["cv"] for d in baseline_docs if d["cv"] is not None]),
        "rates": {
            k: sum(d["hits"][k] for d in baseline_docs) / bw
            for k in list(WEIGHTS)
        },
    }

    for d in docs:
        d["score"] = score(d, base)

    # Flag threshold = 90th percentile of the provably-human cohort. "Noisier than 90%
    # of what you wrote before any of this existed."
    bscores = sorted(d["score"] for d in baseline_docs)
    threshold = bscores[int(len(bscores) * 0.90)]

    stubs = [d for d in scan_docs if d["stub"]]
    ranked = sorted(
        (d for d in scan_docs
         if not d["stub"] and d["score"] >= threshold and d["prose_words"] >= MIN_PROSE),
        key=lambda d: -d["score"],
    )
    # Descriptions are scanned across the *whole* corpus, baseline included: they were
    # written in the July 2026 SEO pass, not when the essay was, so the date cutoff
    # that calibrates prose doesn't apply to them.
    stub_paths = {d["path"] for d in stubs}
    bad_desc = []
    for d in docs:
        c = classify_desc(d["desc"])
        if not c:
            continue
        tier, reason = c
        if tier == "possible" and d["path"] in stub_paths:
            tier, reason = "strong", reason + " (and the body is a machine abstract)"
        bad_desc.append((tier, reason, d))
    desc_strong = [x for x in bad_desc if x[0] == "strong"]
    desc_possible = [x for x in bad_desc if x[0] == "possible"]

    today = date.today().isoformat()
    L = []
    A = L.append

    A("# AI-tell audit — `content/`")
    A("")
    A(f"Generated {today} by `scripts/ai_tells.py`. Re-run it after edits; a fixed file should "
      "drop down the list or fall off it.")
    A("")
    A(f"**{len(scan_docs)} files scanned** (2023-present, plus undated site copy) against a baseline of "
      f"**{base['n']} files written before {BASELINE_CUTOFF}** — the Medium-era essays, "
      "provably yours.")
    A("")
    A(f"- **{len(ranked)} files flagged** for manual review, worst first")
    A(f"- **{len(stubs)} crosspost stubs** where the body *is* an LLM abstract (batch section below)")
    A(f"- **{len(desc_strong)} frontmatter descriptions** reading as machine summaries, "
      f"plus {len(desc_possible)} worth a glance (batch section below)")
    A("")

    A("## How to read this")
    A("")
    A("A flag is a prompt to look, not a verdict. The threshold is the 90th percentile score of your "
      "own pre-2023 writing, so everything here is *noisier than 90% of what you wrote before LLMs "
      "existed* — which is a real signal, and still not proof.")
    A("")
    A("Known false-positive shapes, found while calibrating:")
    A("")
    A("- **Rule-of-three and em-dashes are partly your voice.** The 2021 essays use both. Only the "
      "excess over baseline is scored, but a flagged instance may still be how you'd have written it.")
    A("- **Aphoristic closes.** `Notes/reference/Building Destiny.md` ends \"one choice at a time\" — "
      "that's a gloss on the Brihadaranyaka Upanishad, not an AI uplift-close.")
    A("- **Technical prose legitimately needs the vocabulary.** \"landscape\", \"navigate\" and "
      "\"leverage\" carry real meaning in the grants and governance essays.")
    A("- **Quoted material is masked out** — blockquotes, code fences, link targets and URLs are "
      "excluded, so nothing here is charged to someone you were citing.")
    A("")
    A("The deepest tell isn't in any single line: it's evenness. Where a file is flagged for even "
      "paragraph lengths or a high one-liner share, the fix isn't a find-and-replace — it's letting "
      "one paragraph run long and cutting another to a fragment.")
    A("")

    A("## Ranked todo")
    A("")
    for i, d in enumerate(ranked, 1):
        meta = " · ".join(filter(None, [
            f"score {d['score']:.0f}",
            f"{d['words']}w",
            d["date"] or "undated",
            surface(d["path"]),
        ]))
        A(f"### {i}. [ ] `content/{d['path']}`")
        A("")
        A(meta)
        A("")
        L.extend(evidence(d, base))
        A("")

    A("## Batch: crosspost stubs")
    A("")
    A(f"{len(stubs)} files whose entire body is a short machine abstract followed by a link to the "
      "original. Different problem from AI-inflected prose — there's no draft here to fix, only an "
      "abstract to replace. Per file: rewrite the summary in your own voice, cut it to a one-line "
      "pointer, or leave it.")
    A("")
    for d in sorted(stubs, key=lambda d: d["path"]):
        body = re.sub(r"^---\n.*?\n---\n?", "", d["raw"], flags=re.S).strip()
        first = re.split(r"\n\s*\n", body)[0]
        A(f"- [ ] `content/{d['path']}` — {d['words']}w · {d['date'] or 'undated'}")
        A(f"  > {snippet(first, 220)}")
    A("")

    A("## Batch: frontmatter descriptions")
    A("")
    A("`description:` fields reading as machine summaries. These are the most public prose in the "
      "repo — they ship into `<meta>` tags, RSS, and `corpus/index.jsonl`, so they're what a "
      "stranger sees first, often instead of the essay. Edit in place.")
    A("")
    A(f"### Reads as a machine abstract ({len(desc_strong)})")
    A("")
    templated = [x for x in desc_strong if "shared template" in x[1]]
    if templated:
        A(f"**{len(templated)} of these open with the same construction** — \"This essay "
          "explores / examines / argues / traces / unpacks…\". One template across essays written "
          "years apart, which means they were all generated in a single pass rather than written "
          "with the piece. Worth fixing as a set: the uniformity is more legible than any single "
          "word choice.")
        A("")
    for _t, reason, d in sorted(desc_strong, key=lambda x: x[2]["path"]):
        A(f"- [ ] `content/{d['path']}` — {reason}")
        A(f"  > {snippet(d['desc'], 200)}")
    A("")
    A(f"### Worth a glance ({len(desc_possible)})")
    A("")
    A("One tell-word and nothing else. Several of these are your own opening paragraph, which is "
      "allowed to say \"crucial\" — check rather than assume.")
    A("")
    for _t, reason, d in sorted(desc_possible, key=lambda x: x[2]["path"]):
        A(f"- [ ] `content/{d['path']}` — {reason}")
        A(f"  > {snippet(d['desc'], 200)}")
    A("")

    A("## Your baseline")
    A("")
    A(f"Measured over {base['n']} files ({base['words']:,} words) dated before {BASELINE_CUTOFF}.")
    A("")
    A("| Signal | Your natural rate |")
    A("|---|---|")
    A(f"| em-dashes | {base['emdash']:.2f} per 1,000 words |")
    A(f"| one-line paragraphs | {base['oneline']*100:.0f}% of paragraphs |")
    A(f"| paragraph-length CV | {base['cv']:.2f} (higher = spikier = more human) |")
    for k, r in sorted(base["rates"].items(), key=lambda kv: -kv[1]):
        if r > 0.001:
            A(f"| {LABELS[k]} | {r:.2f} per 1,000 words |")
    A("")
    A(f"Flag threshold: score ≥ {threshold:.1f} (90th percentile of the baseline cohort).")
    A("")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write("\n".join(L) + "\n")

    print(f"baseline: {base['n']} files, {base['words']:,} words (pre-{BASELINE_CUTOFF})")
    print(f"  em-dash {base['emdash']:.2f}/1k · one-line {base['oneline']*100:.0f}% · CV {base['cv']:.2f}")
    print(f"  vocab {base['rates']['vocab']:.2f}/1k · bold-list {base['rates']['bold-colon-list']:.2f}/1k "
          f"· gerund {base['rates']['gerund-tail']:.2f}/1k")
    print(f"scanned {len(scan_docs)} files; threshold {threshold:.1f}")
    print(f"  {len(ranked)} flagged · {len(stubs)} stubs · {len(desc_strong)} descriptions (+{len(desc_possible)} maybe)")
    print(f"→ {os.path.relpath(OUT, ROOT)}")
    print("\ntop 10:")
    for i, d in enumerate(ranked[:10], 1):
        print(f"{i:>3}. {d['score']:6.1f}  {d['date'] or 'undated':10} {d['path']}")


if __name__ == "__main__":
    main()
