#!/usr/bin/env python3
"""Generate the Flourrish static site into ../dist. No dependencies beyond Python 3.

    python3 build/build.py

Edit content in common.py (contact details, areas, services), content_*.py (pages).
The output is plain HTML/CSS/JS that opens from file:// and deploys to any static host.
"""
import os
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
DIST = os.path.join(os.path.dirname(HERE), "dist")

import common
from common import *
from content_home import build_home
from content_services import build_service_page, build_services_index, build_property_types, build_how_it_works
from content_pages import build_areas, build_about, build_faq, build_contact, build_proposal, build_privacy, build_terms, build_404
from content_resources import build_resources_index, build_article, ARTICLES

LOGO_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 80" width="360" height="80" role="img" aria-label="flourrish">
<!-- PLACEHOLDER: replace this file with the approved Flourrish logo (orange circle-wave mark + "flourrish" wordmark). -->
<circle cx="40" cy="40" r="34" fill="#FC5200"/>
<path d="M14 44c8-10 18-10 26 0s18 10 26 0" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<path d="M18 56c7-8 15-8 22 0s15 8 22 0" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".8"/>
<text x="92" y="52" font-family="Manrope, Inter, Arial, sans-serif" font-weight="800" font-size="40" letter-spacing="-1" fill="#1F1A16">flourrish<tspan font-size="14" font-weight="600" dy="-18">™</tspan></text>
</svg>
'''

FAVICON_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="#FC5200"/><path d="M12 36c7-9 15-9 20 0s13 9 20 0" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/><path d="M16 46c6-7 12-7 16 0s10 7 16 0" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".8"/></svg>
'''


def write(path, content):
    full = os.path.join(DIST, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return path


def make_og_image(out_path):
    """1200x630 PNG for link previews. Falls back silently if Pillow is missing."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return False
    img = Image.new("RGB", (1200, 630), "#FFFFFF")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1200, 14], fill="#FC5200")
    d.ellipse([80, 110, 180, 210], fill="#FC5200")
    try:
        big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 68)
        small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
    except Exception:
        big = small = ImageFont.load_default()
    d.text((80, 270), "Your property in India.", fill="#1F1A16", font=big)
    d.text((80, 350), "Our responsibility.", fill="#1F1A16", font=big)
    d.text((80, 470), "Flourrish Asset Management  |  Property management in Chennai", fill="#5F5750", font=small)
    img.save(out_path, "PNG", optimize=True)
    return True


def main():
    os.makedirs(os.path.join(DIST, "assets/img/ph"), exist_ok=True)
    pages = {}
    pages["index.html"] = build_home()
    pages["services.html"] = build_services_index()
    for slug, title, line, icon in SERVICES:
        pages[f"service-{slug}.html"] = build_service_page(slug, title, line, icon)
    pages["property-types.html"] = build_property_types()
    pages["how-it-works.html"] = build_how_it_works()
    pages["areas.html"] = build_areas()
    pages["about.html"] = build_about()
    pages["faq.html"] = build_faq()
    pages["contact.html"] = build_contact()
    pages["proposal.html"] = build_proposal()
    pages["privacy.html"] = build_privacy()
    pages["terms.html"] = build_terms()
    pages["404.html"] = build_404()
    pages["resources.html"] = build_resources_index()
    for a in ARTICLES:
        pages[f"article-{a['slug']}.html"] = build_article(a)
    pages["photo-credits.html"] = common.build_credits()

    for path, html_ in pages.items():
        write(path, html_)

    common.write_placeholders(DIST)
    common.write_images_md(DIST)
    common.write_areas_js(DIST)

    today = date.today().isoformat()
    urls = [p for p in pages if p not in ("404.html",)]
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in urls:
        loc = SITE_URL + "/" + ("" if p == "index.html" else p)
        pri = "1.0" if p == "index.html" else ("0.8" if p.startswith("service") or p in ("contact.html", "about.html") else "0.6")
        sitemap.append(f"  <url><loc>{loc}</loc><lastmod>{today}</lastmod><priority>{pri}</priority></url>")
    sitemap.append("</urlset>\n")
    write("sitemap.xml", "\n".join(sitemap))
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")

    print(f"Built {len(pages)} pages into {DIST}")


if __name__ == "__main__":
    main()
