"""Export the Docomotion knowledge base (https://www.docomotion.com/support/) to Markdown.

Uses the WordPress REST API to fetch every page under /support/, strips the
Elementor page chrome (search box, sidebar menu, table of contents) and writes
one Markdown file per article into knowledge_base/, mirroring the URL tree.

Usage:  python export_kb.py
"""

import hashlib
import html
import json
import re
import shutil
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

SITE = "https://www.docomotion.com"
SECTION = "/support/"
OUT_DIR = Path(__file__).parent / "knowledge_base"
MIN_CHARS = 80  # prose (excluding links) below this = a menu/landing/video-only page, not an article
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; docs-indexer/1.0)"}

# Page chrome repeated on every article that should not end up in the knowledge base
CHROME_SELECTORS = [
    "script", "style", "noscript", "form", "search",
    "nav",                                               # sidebar "bellows" menu + nav-menu widgets
    "[data-widget_type='search-form.default']",
    "[data-widget_type='nav-menu.default']",
    "[data-widget_type='table-of-contents.default']",
]


def fetch_pages():
    pages, page = [], 1
    while True:
        r = requests.get(
            f"{SITE}/wp-json/wp/v2/pages",
            headers=HEADERS,
            params={"per_page": 100, "page": page,
                    "_fields": "id,parent,title,link,modified,content"},
            timeout=60,
        )
        if r.status_code != 200 or not r.json():
            break
        pages += r.json()
        page += 1
    return [p for p in pages if SECTION in p["link"]]


def clean_html(raw: str) -> str:
    soup = BeautifulSoup(raw, "html.parser")
    for tag in soup.select(", ".join(CHROME_SELECTORS)):
        tag.decompose()

    # Elementor video widgets render no <iframe> in the API output; the URL lives in data-settings
    for w in soup.select("[data-widget_type='video.default']"):
        try:
            settings = json.loads(w.get("data-settings", "{}"))
        except json.JSONDecodeError:
            settings = {}
        url = next((settings[k] for k in ("youtube_url", "vimeo_url", "dailymotion_url",
                                          "videopress_url", "external_url") if settings.get(k)), None)
        if isinstance(url, dict):
            url = url.get("url")
        if url:
            p = soup.new_tag("p")
            a = soup.new_tag("a", href=url)
            a.string = "Video"
            p.append(a)
            w.replace_with(p)
        else:
            w.decompose()
    return str(soup)


def to_markdown(raw_html: str) -> str:
    text = md(
        clean_html(raw_html),
        heading_style="ATX",
        bullets="-",
        strip=["img"],  # images carry no text for RAG; alt text is rarely meaningful here
    )
    text = text.replace(" ", " ")
    text = re.sub(r"\]\((/[^)]*)\)", rf"]({SITE}\1)", text)  # relative links -> absolute
    text = re.sub(r"[ \t]+\n", "\n", text)      # trailing spaces
    text = re.sub(r"\n{3,}", "\n\n", text)      # collapse blank lines
    return text.strip()


def prose_length(markdown: str) -> int:
    """Characters of real text, ignoring links, so link-only landing pages count as empty."""
    no_links = re.sub(r"\[[^\]]*\]\([^)]*\)", "", markdown)
    return len(re.sub(r"[#*_>\-|`\s]", "", no_links))


def out_path(link: str) -> Path:
    rel = urlparse(link).path.strip("/").split("/")[1:]  # drop leading "support"
    if not rel:
        return OUT_DIR / "index.md"
    return OUT_DIR.joinpath(*rel[:-1], rel[-1] + ".md")


def front_matter(title: str, link: str, modified: str) -> str:
    parts = urlparse(link).path.strip("/").split("/")[1:]
    section = parts[0] if len(parts) > 1 else ""
    esc = title.replace('"', '\\"')
    return (f'---\ntitle: "{esc}"\nsource: {link}\nsection: {section}\n'
            f"last_modified: {modified}\n---\n\n")


def main():
    pages = fetch_pages()
    print(f"Fetched {len(pages)} pages under {SECTION}")

    # Clear previous export (contents only, so an Explorer/terminal open in the folder doesn't block it)
    OUT_DIR.mkdir(exist_ok=True)
    for child in OUT_DIR.iterdir():
        shutil.rmtree(child) if child.is_dir() else child.unlink()

    # Shorter URLs first, so when two pages are identical the canonical-looking one is kept
    pages.sort(key=lambda p: (len(p["link"]), p["link"]))
    seen, written, skipped_short, skipped_dup = {}, [], [], []

    for p in pages:
        title = html.unescape(p["title"]["rendered"]).strip()
        body = to_markdown(p["content"]["rendered"])
        if prose_length(body) < MIN_CHARS:
            skipped_short.append(p["link"])
            continue
        digest = hashlib.sha256(body.encode()).hexdigest()
        if digest in seen:
            skipped_dup.append((p["link"], seen[digest]))
            continue
        seen[digest] = p["link"]

        path = out_path(p["link"])
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(front_matter(title, p["link"], p["modified"]) + f"# {title}\n\n{body}\n",
                        encoding="utf-8")
        written.append((path, len(body)))

    print(f"Wrote {len(written)} Markdown files to {OUT_DIR}")
    if skipped_short:
        print(f"\nSkipped {len(skipped_short)} pages with no article text (link menus / video-only):")
        for link in skipped_short:
            print("  ", link)
    if skipped_dup:
        print(f"\nSkipped {len(skipped_dup)} exact duplicates:")
        for link, original in skipped_dup:
            print(f"   {link}\n      = {original}")


if __name__ == "__main__":
    main()
