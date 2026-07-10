# Archive

A hand-built static site generator for a personal portfolio — projects and
photography — in a grey-on-grey technical-document style. Plain Python, plain
HTML output, no JavaScript needed to run the finished site.

## Run it

```bash
python -m venv .venv
source .venv/bin/activate           # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python build.py                     # writes the site into dist/
python -m http.server 8000 --directory dist
```

Then open <http://localhost:8000>. Rebuild with `python build.py` and refresh;
the server reads files live, so it never needs restarting.

> On Windows, always serve with `--directory dist` from the project root (not
> from *inside* `dist/`), because each build wipes and recreates that folder.

## How it's laid out

```
build.py              the whole engine
templates/            base.html + one template per page type
static/style.css      all styling (the engine never touches this)
content/
  projects/*.md       one file per project
  photos/<slug>/      one folder per photo set (index.md + image files)
  about.md            the about page
dist/                 generated output — do not edit, it's rebuilt each run
```

## Adding a project

Drop a new `.md` file in `content/projects/`. Frontmatter fields:

```yaml
---
title: My Project
date: 2026-07-09          # controls sort order (newest first) and the shown date
category: Electronics     # small label in the eyebrow (optional)
summary: One paragraph for the index and the abstract.
tags: [pcb, stm32]        # used for filtering later; not displayed per-entry
hero: /static/img/foo.jpg # optional hero image (optional)
spec:                     # optional key/value table (optional)
  MCU: STM32F405
  Status: Working
---

Body text in **markdown**.
```

Pick one meaning for `date` and keep it consistent — completion date is a good
choice. For a project hero image, put the file in `static/img/` and point
`hero:` at it, e.g. `hero: /static/img/aoa-board.jpg`.

## Adding a photo set

Make a folder `content/photos/<slug>/`, drop the image files in it, and add an
`index.md`:

```yaml
---
title: Star Trails
location: Simon's Town
date: 2026-06-14
cover: 03.jpg             # which frame is the landing-page cover
frames:
  - src: 01.jpg
  - src: 02.jpg
  - src: 03.jpg
    select: true          # selects print larger on the contact sheet
  - src: 04.jpg
---

Optional writeup for the set.
```

The build copies every image in the folder next to the generated page, so
`src:` is just the filename. The photography landing shows one cover per set;
clicking a set opens its contact sheet with the selects enlarged.

The starter sets use throwaway `.svg` placeholders — delete them and drop in
your real photos, then update `frames:` accordingly.

## Deploy to Cloudflare Pages (free)

1. Push this repo to GitHub.
2. In the Cloudflare dashboard: **Workers & Pages → Create → Pages → Connect to
   Git**, pick the repo.
3. Build settings:
   - **Build command:** `pip install -r requirements.txt && python build.py`
   - **Build output directory:** `dist`
4. Deploy. Every push rebuilds and publishes automatically. You get a free
   `*.pages.dev` URL; add a custom domain later under the project's settings
   with no change to the build.

## Notes

- Fonts (Jost + Courier Prime) load from Google Fonts via `base.html`. Jost
  stands in for Futura; Courier Prime is the typewriter body.
- To restyle the whole site, edit the variables at the top of
  `static/style.css`. To change the accent from international orange, change
  `--accent`.
- Possible next steps: real tag filtering from the `tags:` field, thumbnail
  generation for contact sheets (add Pillow), an RSS/JSON feed of projects.
```
