---
title: The Engine
date: 2026-06-29
category: Software
summary: The Python static-site generator that builds this site. Markdown plus YAML frontmatter, Jinja2 templates, one build script. The document that typeset itself.
tags: [python, jinja2, meta]
spec:
  Language: Python 3
  Dependencies: markdown, jinja2, pyyaml
  Output: Static HTML, no client-side JS
  Hosting: Cloudflare Pages
---

Every page on this site is a Markdown file with a little YAML on top. This
generator walks the content folders, renders each file through a Jinja2
template, and writes plain HTML into `dist/`. No database, no framework, nothing
to run on a server.

Building it rather than using a pre-made generator was the point: I wanted to
understand every adjustment I make, and to own the whole pipeline from a note I
type to the page you're reading.
