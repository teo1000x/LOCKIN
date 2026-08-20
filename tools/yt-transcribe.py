#!/usr/bin/env python3
"""
Pull a clean text transcript from a YouTube video using its captions.
Downloads no video or audio, only the caption track.

    python3 tools/yt-transcribe.py <youtube-url> [output-name]

Writes to transcripts/<output-name>.txt
"""
import os
import re
import subprocess
import sys
import tempfile
import glob

YT_DLP = os.path.expanduser("~/Library/Python/3.9/bin/yt-dlp")
OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "transcripts")

TAG_RE = re.compile(r"<[^>]+>")
TIMING_RE = re.compile(r"^\d{2}:\d{2}:\d{2}\.\d{3}\s+-->")


def fetch_vtt(url: str, workdir: str) -> str:
    """
    Ask yt-dlp for manual subs, falling back to auto-generated ones.

    YouTube periodically breaks individual player clients, so try several in
    order rather than failing on the first. If they all fail the video is
    likely private, age-gated, or region-blocked.
    """
    errors = []
    for client in ("android", "ios", "mweb", "web_safari", "tv"):
        subprocess.run(
            [
                YT_DLP,
                "--skip-download",
                "--write-sub",
                "--write-auto-sub",
                "--sub-lang", "en.*",
                "--sub-format", "vtt",
                "--extractor-args", f"youtube:player_client={client}",
                "-o", os.path.join(workdir, "cap"),
                url,
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        found = glob.glob(os.path.join(workdir, "*.vtt"))
        if found:
            print(f"[captions fetched via {client} client]")
            return found[0]
        errors.append(client)

    raise SystemExit(
        f"Could not fetch captions (tried: {', '.join(errors)}).\n"
        "Either the video has no captions, or it is private, age-gated, or region-blocked.\n"
        "A video with genuinely no captions needs audio transcription instead."
    )


def vtt_to_text(path: str) -> str:
    """Strip cues, tags and the rolling-duplicate lines auto-captions produce."""
    lines = []
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line == "WEBVTT" or TIMING_RE.match(line):
                continue
            if line.startswith(("Kind:", "Language:", "NOTE")) or line.isdigit():
                continue
            line = TAG_RE.sub("", line).strip()
            if line and (not lines or lines[-1] != line):
                lines.append(line)

    # Auto-captions repeat the previous line as the first line of the next cue.
    deduped = []
    for line in lines:
        if deduped and (line in deduped[-1] or deduped[-1].endswith(line)):
            continue
        deduped.append(line)

    text = " ".join(deduped)
    text = re.sub(r"\s+", " ", text).strip()
    # Break into readable paragraphs rather than one wall of text.
    sentences = re.split(r"(?<=[.!?]) ", text)
    paragraphs, buf = [], []
    for sentence in sentences:
        buf.append(sentence)
        if len(buf) >= 5:
            paragraphs.append(" ".join(buf))
            buf = []
    if buf:
        paragraphs.append(" ".join(buf))
    return "\n\n".join(paragraphs)


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    url = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 else "transcript"

    os.makedirs(OUT_DIR, exist_ok=True)
    with tempfile.TemporaryDirectory() as workdir:
        text = vtt_to_text(fetch_vtt(url, workdir))

    dest = os.path.join(OUT_DIR, f"{name}.txt")
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(text)

    words = len(text.split())
    print(f"\nWrote {words:,} words to transcripts/{name}.txt")


if __name__ == "__main__":
    main()
