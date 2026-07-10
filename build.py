"""
archive — a small static site generator.

Reads Markdown content, renders it through Jinja2 templates, and writes a
plain HTML site into dist/. No database, no JavaScript required to run the
site, no framework. You own every line of this.

Run:      python build.py
Preview:  python -m http.server 8000 --directory dist   (then open localhost:8000)

Content model
-------------
content/projects/<slug>.md      one Markdown file per project
content/photos/<slug>/index.md  one folder per photo set, images alongside
content/about.md                the about page

Each Markdown file starts with a YAML "frontmatter" block between --- fences,
followed by the Markdown body. Example:

    ---
    title: My Project
    date: 2026-05-18
    summary: One line for the index.
    ---
    The body, in **markdown**.
"""

from pathlib import Path
from datetime import date
import shutil

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

# ---------------------------------------------------------------------------
# Paths and global config
# ---------------------------------------------------------------------------
ROOT      = Path(__file__).parent
CONTENT   = ROOT / "content"
TEMPLATES = ROOT / "templates"
STATIC    = ROOT / "static"
DIST      = ROOT / "dist"

# Anything here is available in every template via the render() helper below.
SITE = {
    "revised": date.today().strftime("%Y·%m·%d"),  # stamped at build time
    "coords":  "33°58′S 18°28′E",                  # Cape Town
}

# Image file types we copy across for photo sets.
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".avif"}

# Jinja environment. autoescape on for safety; we mark trusted HTML with |safe.
env = Environment(
    loader=FileSystemLoader(str(TEMPLATES)),
    autoescape=select_autoescape(["html"]),
)


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------
def split_frontmatter(text):
    """Return (metadata_dict, body_markdown) from a --- fenced file."""
    if not text.startswith("---"):
        return {}, text
    # ['', yaml_text, body] — split on the first two fences only
    _, frontmatter_text, body = text.split("---", 2)
    meta = yaml.safe_load(frontmatter_text) or {}
    return meta, body.lstrip("\n")


def fmt_date(value):
    """YAML parses an ISO date to a date object; format it in the site style."""
    if isinstance(value, date):
        return value.strftime("%Y·%m·%d")
    return str(value) if value else ""


def render(template_name, out_path, **context):
    """Render a template with the shared SITE context and write it to dist."""
    html = env.get_template(template_name).render(site=SITE, **context)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")


# ---------------------------------------------------------------------------
# Loaders — read content off disk into plain dicts
# ---------------------------------------------------------------------------
def load_projects():
    projects = []
    for path in (CONTENT / "projects").glob("*.md"):
        meta, body = split_frontmatter(path.read_text(encoding="utf-8"))
        projects.append({
            "slug":      path.stem,
            "title":     meta.get("title", path.stem),
            "date":      meta.get("date"),
            "date_str":  fmt_date(meta.get("date")),
            "category":  meta.get("category", ""),
            "summary":   meta.get("summary", ""),
            "tags":      meta.get("tags", []),          # used for filtering, not shown
            "hero":      meta.get("hero"),              # optional image path
            "spec":      meta.get("spec", {}),          # optional key/value table
            "body_html": markdown.markdown(body, extensions=["extra"]),
        })
    # newest first; date objects sort correctly
    projects.sort(key=lambda p: p["date"] or date.min, reverse=True)
    return projects


def load_photo_sets():
    sets = []
    for folder in sorted((CONTENT / "photos").iterdir()):
        index = folder / "index.md"
        if not folder.is_dir() or not index.exists():
            continue
        meta, body = split_frontmatter(index.read_text(encoding="utf-8"))
        frames = meta.get("frames", [])
        sets.append({
            "slug":       folder.name,
            "folder":     folder,
            "title":      meta.get("title", folder.name),
            "location":   meta.get("location", ""),
            "date":       meta.get("date"),
            "date_str":   fmt_date(meta.get("date")),
            "cover":      meta.get("cover"),            # filename of the hero frame
            "frames":     frames,                       # list of {src, select?}
            "count":      len(frames),
            "body_html":  markdown.markdown(body, extensions=["extra"]),
        })
    sets.sort(key=lambda s: s["date"] or date.min, reverse=True)
    return sets


# ---------------------------------------------------------------------------
# The build
# ---------------------------------------------------------------------------
def build():
    # 1. Start clean, then copy static assets (css, fonts, images) across.
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    if STATIC.exists():
        shutil.copytree(STATIC, DIST / "static")

    # 2. Projects: one page each, plus the index (which is the site home).
    projects = load_projects()
    for p in projects:
        render("project.html", DIST / "projects" / f"{p['slug']}.html",
               project=p, active="projects")
    render("index.html", DIST / "index.html",
           projects=projects, active="projects")

    # 3. Photography: a cover landing, plus one contact-sheet page per set.
    #    Each set gets its own folder so its images sit beside its HTML and
    #    can be referenced with plain relative filenames.
    photo_sets = load_photo_sets()
    for s in photo_sets:
        out_dir = DIST / "photography" / s["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        for img in s["folder"].iterdir():
            if img.suffix.lower() in IMAGE_EXTS:
                shutil.copy2(img, out_dir / img.name)
        render("photoset.html", out_dir / "index.html",
               set=s, active="photography")
    render("photography.html", DIST / "photography" / "index.html",
           sets=photo_sets, active="photography")

    # 4. About.
    about_md = CONTENT / "about.md"
    if about_md.exists():
        meta, body = split_frontmatter(about_md.read_text(encoding="utf-8"))
        render("about.html", DIST / "about" / "index.html",
               title=meta.get("title", "About"),
               body_html=markdown.markdown(body, extensions=["extra"]),
               active="about")

    print(f"Built {len(projects)} project(s) and {len(photo_sets)} photo set(s) "
          f"into {DIST.relative_to(ROOT)}/")


if __name__ == "__main__":
    build()
