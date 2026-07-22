"""
Transcript format converter: .srt <-> .vtt <-> .ttml

Loss-lessly parses a timecoded caption file (.srt or .vtt, comma or dot
millisecond separators) into cues, then emits any of the three standard
caption formats. Used by the frameio-transcript-pipeline skill to produce
all three deliverables (.srt, .vtt, .ttml) from one proofread source file.

Usage:
    python transcript_formats.py <INPUT_FILE> --formats srt,vtt,ttml --outdir <DIR> [--lang en]

Writes <stem>.srt / <stem>.vtt / <stem>.ttml into --outdir (default: alongside input).
"""

import argparse
import os
import re
import sys
from xml.sax.saxutils import escape

TIME_RE = re.compile(
    r"(\d{2}):(\d{2}):(\d{2})[.,](\d{3})\s*-->\s*(\d{2}):(\d{2}):(\d{2})[.,](\d{3})"
)


def parse(path):
    """Parse a .srt or .vtt file into a list of cues: {index, start, end, text}."""
    with open(path, "r", encoding="utf-8-sig") as f:
        raw = f.read()

    is_vtt = raw.lstrip().startswith("WEBVTT")
    blocks = re.split(r"\r?\n\r?\n+", raw.strip())
    cues = []
    idx = 0
    for block in blocks:
        lines = [l for l in block.splitlines() if l.strip() != ""]
        if not lines:
            continue
        if is_vtt and lines[0].strip().upper().startswith("WEBVTT"):
            continue
        # Find the timing line within this block (skip numeric/id line if present).
        time_line_i = None
        for i, l in enumerate(lines):
            if "-->" in l:
                time_line_i = i
                break
        if time_line_i is None:
            continue
        m = TIME_RE.search(lines[time_line_i])
        if not m:
            continue
        h1, m1, s1, ms1, h2, m2, s2, ms2 = m.groups()
        start = f"{h1}:{m1}:{s1}.{ms1}"
        end = f"{h2}:{m2}:{s2}.{ms2}"
        text_lines = lines[time_line_i + 1:]
        text = "\n".join(text_lines).strip()
        if not text:
            continue
        cues.append({"index": idx, "start": start, "end": end, "text": text})
        idx += 1

    if not cues:
        print(f"Warning: no cues parsed from {path}", file=sys.stderr)

    return cues


def to_srt_time(t):
    return t.replace(".", ",")


def to_vtt_time(t):
    return t


def to_ttml_time(t):
    return t


def build_srt(cues):
    blocks = []
    for c in cues:
        blocks.append(
            f"{c['index'] + 1}\n{to_srt_time(c['start'])} --> {to_srt_time(c['end'])}\n{c['text']}"
        )
    return "\n\n".join(blocks) + "\n"


def build_vtt(cues):
    blocks = ["WEBVTT"]
    for c in cues:
        blocks.append(f"{to_vtt_time(c['start'])} --> {to_vtt_time(c['end'])}\n{c['text']}")
    return "\n\n".join(blocks) + "\n"


def build_ttml(cues, lang="en"):
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="{lang}">',
        "  <body>",
        "    <div>",
    ]
    for c in cues:
        text = escape(c["text"]).replace("\n", "<br/>")
        lines.append(
            f'      <p begin="{to_ttml_time(c["start"])}" end="{to_ttml_time(c["end"])}">{text}</p>'
        )
    lines += ["    </div>", "  </body>", "</tt>"]
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Convert a caption file into .srt/.vtt/.ttml")
    ap.add_argument("input_file", help="Path to the source .srt/.vtt file")
    ap.add_argument("--formats", default="srt,vtt,ttml", help="Comma list: srt,vtt,ttml")
    ap.add_argument("--outdir", default=None, help="Output directory (default: alongside input)")
    ap.add_argument("--lang", default="en", help="xml:lang for TTML output (default: en)")
    args = ap.parse_args()

    if not os.path.isfile(args.input_file):
        print(f"File not found: {args.input_file}", file=sys.stderr)
        sys.exit(1)

    cues = parse(args.input_file)
    stem = os.path.splitext(os.path.basename(args.input_file))[0]
    outdir = args.outdir or os.path.dirname(os.path.abspath(args.input_file))
    os.makedirs(outdir, exist_ok=True)

    builders = {"srt": build_srt, "vtt": build_vtt, "ttml": lambda c: build_ttml(c, args.lang)}
    written = []
    for fmt in [f.strip().lower() for f in args.formats.split(",") if f.strip()]:
        if fmt not in builders:
            print(f"Unknown format: {fmt}", file=sys.stderr)
            continue
        content = builders[fmt](cues)
        out_path = os.path.join(outdir, f"{stem}.{fmt}")
        with open(out_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        written.append(out_path)

    print(f"Parsed {len(cues)} cues from {args.input_file}")
    for p in written:
        print(f"  -> {p}")


if __name__ == "__main__":
    main()
