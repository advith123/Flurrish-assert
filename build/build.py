import re, os, sys, glob, html
from urllib.parse import quote
sys.path.insert(0, os.path.dirname(__file__))
from services_data import CATEGORIES, NRI_LINKS, SERVICES, BY_SLUG

ROOT = sys.argv[1]
SITE = "https://flourrishassets.com/"
TODAY = "2026-10-24"
WA_BASE = "https://wa.me/919944070397?text="

def wa(service=None):
    txt = "Hi Flourrish, I would like to know more about your property management services.\n\nProperty / land location: \nProperty type: \nService needed: " + (service or "")
    return WA_BASE + quote(txt, safe="")

def esc(s): return html.escape(s, quote=False)

TAG = {
 "land-ec-check":"Title and loan check on your land","land-patta-chitta-verification":"Revenue records matched to your deed",
 "land-site-visits":"Scheduled visits with photos and video","land-boundary-encroachment-check":"Stones, fences and neighbours checked",
 "land-leasing":"Earn from land you are not using","land-tax-payments":"Dues paid on time, receipts kept","land-sale-assistance":"From clean papers to registration",
 "tenant-sourcing":"Listing, enquiries and viewings","tenant-verification":"ID, employer and police checks","rent-agreements":"Drafted, signed and registered",
 "rent-collection":"Tracked, reminded, followed up","move-in-move-out":"Photos, inventory, deposit settled","property-inspections":"Regular visits with a report",
 "video-walkthroughs":"See every room yourself","maintenance-coordination":"Estimate, approval, repair, photos","emergency-response":"Leaks, faults, storms, break-ins",
 "vacant-property-care":"Empty home kept ready","commercial-tenant-sourcing":"The right business for your space","commercial-lease-management":"Lock-in, escalation, renewals tracked",
 "commercial-fit-out":"Build-out and restoration supervised","commercial-maintenance":"AC, electrical, fire safety on schedule",
 "property-tax":"Paid with your approval","utility-bills":"Electricity, water, gas, dues","rwa-association-liaison":"Dues, notices, approvals handled",
 "owner-reports":"One report every month","nri-support":"TDS, FEMA, POA with our partners",
}
# ------------------------------------------------------------------ MENU
def mega_menu(p):
    """Desktop Services item with the full-width panel. p = relative prefix."""
    tabs, panels = [], []
    for i, (cid, label, href, blurb) in enumerate(CATEGORIES):
        act = " is-active" if i == 0 else ""
        tabs.append(f'<button type="button" role="tab" id="mtab-{cid}" aria-controls="mpanel-{cid}" aria-selected="{"true" if i==0 else "false"}" class="mega__tab{act}" data-tab="{cid}">{label}</button>')
        if cid == "nri":
            links = "".join(f'<a href="{p}{h}"><b>{esc(n)}</b><span>{esc(d)}</span></a>' for h, n, d in NRI_LINKS)
        else:
            links = "".join(f'<a href="{p}services/{s["slug"]}.html"><b>{esc(s.get("menu", s["name"]))}</b><span>{esc(TAG[s["slug"]])}</span></a>'
                            for s in SERVICES if s["cat"] == cid)
        panels.append(f'<div class="mega__panel{act}" role="tabpanel" id="mpanel-{cid}" aria-labelledby="mtab-{cid}" data-panel="{cid}"{"" if i==0 else " hidden"}>'
                      f'<div class="mega__intro"><p>{esc(blurb)}</p><a class="link" href="{p}{href}">See all {label.lower() if cid!="nri" else "NRI"} services</a></div>'
                      f'<div class="mega__links">{links}</div></div>')
    return (f'<div class="nav__item has-mega">'
            f'<a href="{p}services.html" data-nav="services">Services</a>'
            f'<button class="nav__more" type="button" aria-expanded="false" aria-controls="mega-services" aria-label="Open services menu"><svg class="i" aria-hidden="true"><use href="#i-chev"/></svg></button>'
            f'<div class="mega" id="mega-services"><div class="wrap mega__in">'
            f'<div class="mega__tabs" role="tablist" aria-label="Service categories">{"".join(tabs)}</div>'
            f'{"".join(panels)}</div></div></div>')

def mobile_services(p):
    groups = []
    for cid, label, href, blurb in CATEGORIES:
        if cid == "nri":
            items = "".join(f'<a href="{p}{h}">{esc(n)}</a>' for h, n, d in NRI_LINKS)
        else:
            items = "".join(f'<a href="{p}services/{s["slug"]}.html">{esc(s.get("menu", s["name"]))}</a>' for s in SERVICES if s["cat"] == cid)
        groups.append(f'<div class="mnav__grp"><b>{label}</b>{items}</div>')
    return (f'<div class="mnav__svc">'
            f'<div class="mnav__row"><a href="{p}services.html" data-nav="services">Services</a>'
            f'<button class="mnav__tgl" type="button" aria-expanded="false" aria-controls="mnav-services" aria-label="Show all services"><svg class="i" aria-hidden="true"><use href="#i-chev"/></svg></button></div>'
            f'<div class="mnav__sub" id="mnav-services" hidden>{"".join(groups)}</div></div>')

CHEV = '<symbol id="i-chev" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></symbol>'

def patch_nav(doc, p):
    if '<symbol id="i-chev"' not in doc:
        doc = doc.replace('<symbol id="i-menu"', CHEV + '\n  <symbol id="i-menu"', 1)
    mob = f'data-nav="home">Home</a><a href="{p}services.html" data-nav="services">Services</a>'
    doc = doc.replace(mob, f'data-nav="home">Home</a>' + mobile_services(p), 1)
    doc = doc.replace(f'<a href="{p}services.html" data-nav="services">Services</a>\n', mega_menu(p) + "\n", 1)
    # footer services column
    old = f'<li><a href="{p}services.html#owner-support">Owner support</a></li>'
    new = (f'<li><a href="{p}services.html#land">Land services</a></li>'
           f'<li><a href="{p}services.html#tenants-rent">Building services</a></li>'
           f'<li><a href="{p}services.html#commercial">Commercial</a></li>' + old)
    if 'Land services</a>' not in doc:
        doc = doc.replace(old, new, 1)
    return doc

# ------------------------------------------------------------------ PAGES
def sprite_and_header(src_doc):
    """Take the inline sprite + header from an existing ../ page (areas/omr.html)."""
    m = re.search(r'(<svg xmlns="http://www.w3.org/2000/svg" style="display:none".*?</header>)', src_doc, re.S)
    return m.group(1)

def footer(src_doc):
    m = re.search(r'(<footer class="ftr".*?</body>\n</html>)', src_doc, re.S)
    return m.group(1)

def service_page(s, header_html, footer_html):
    cat = next(c for c in CATEGORIES if c[0] == s["cat"])
    cid, clabel, chref, _ = cat
    url = f'{SITE}services/{s["slug"]}.html'
    title = f'{s["name"]} in Chennai | Flourrish'
    desc = s["lede"]
    if len(desc) > 158: desc = desc[:155].rsplit(" ", 1)[0] + "…"
    n = len(s["steps"])
    steps = "".join(f'<li><span class="steps__n">{i+1}</span><h3>{esc(t)}</h3><p>{esc(x)}</p></li>' for i, (t, x) in enumerate(s["steps"]))
    included = "".join(f'<li>{esc(x)}</li>' for x in s["included"])
    receive = "".join(f'<li><svg class="i" aria-hidden="true"><use href="#p-document"/></svg>{esc(x)}</li>' for x in s["receive"])
    faqs = "".join(f'<details class="faq"><summary>{esc(q)}<svg class="i faq__i" aria-hidden="true"><use href="#i-plus"/></svg></summary><div class="faq__a"><p>{esc(a)}</p></div></details>' for q, a in s["faq"])
    related = "".join(f'<a href="{r}.html">{esc(BY_SLUG[r]["name"])}</a>' for r in s["related"] if r in BY_SLUG)
    waurl = wa(s["name"])
    faq_ld = ", ".join('{"@type": "Question", "name": %s, "acceptedAnswer": {"@type": "Answer", "text": %s}}' % (jq(q), jq(a)) for q, a in s["faq"])
    steps_ld = ", ".join('{"@type": "HowToStep", "position": %d, "name": %s, "text": %s}' % (i+1, jq(t), jq(x)) for i, (t, x) in enumerate(s["steps"]))
    ld = ('{"@context": "https://schema.org", "@graph": ['
          '{"@type": "WebPage", "@id": "%s#webpage", "url": "%s", "name": %s, "description": %s, "isPartOf": {"@id": "%s#website"}, "inLanguage": "en-IN", "dateModified": "%s", "breadcrumb": {"@id": "%s#breadcrumb"}},'
          '{"@type": "BreadcrumbList", "@id": "%s#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "%s"}, {"@type": "ListItem", "position": 2, "name": "Services", "item": "%sservices.html"}, {"@type": "ListItem", "position": 3, "name": %s, "item": "%s%s"}, {"@type": "ListItem", "position": 4, "name": %s, "item": "%s"}]},'
          '{"@type": "Service", "@id": "%s#service", "name": %s, "description": %s, "serviceType": "Property management", "provider": {"@id": "%s#organization"}, "areaServed": {"@type": "City", "name": "Chennai"}},'
          '{"@type": "HowTo", "@id": "%s#process", "name": %s, "step": [%s]},'
          '{"@type": "FAQPage", "@id": "%s#faq", "mainEntity": [%s]}]}'
          ) % (url, url, jq(title), jq(desc), SITE, TODAY, url,
               url, SITE, SITE, jq(clabel), SITE, chref, jq(s["name"]), url,
               url, jq(s["name"] + " in Chennai"), jq(s["short"]), SITE,
               url, jq("How " + s["name"].lower() + " works at Flourrish"), steps_ld,
               url, faq_ld)

    page = f'''<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<meta name="theme-color" content="#F97316">
<meta name="geo.region" content="IN-TN">
<meta name="geo.placename" content="Chennai">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Flourrish Asset Management">
<meta property="og:locale" content="en_IN">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{SITE}assets/brand/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<link rel="icon" href="../assets/brand/favicon.png" type="image/png" sizes="64x64">
<link rel="apple-touch-icon" href="../assets/brand/apple-touch-icon.png">
<link rel="manifest" href="../site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap">
<link rel="stylesheet" href="../css/style.css">
<script type="application/ld+json">{ld}</script>
</head>
<body data-page="services">
<a class="skip" href="#main">Skip to content</a>
{header_html}

<main id="main">
<section class="phero phero--plain">
  <div class="wrap">
    <div class="phero__grid">
      <div>
        <nav aria-label="Breadcrumb"><ol class="crumbs"><li><a href="../index.html">Home</a></li><li><a href="../services.html">Services</a></li><li><a href="../{chref}">{esc(clabel)}</a></li><li aria-current="page">{esc(s["name"])}</li></ol></nav>
        <span class="kicker" style="margin:22px 0 0">{esc(clabel)} services</span>
        <h1 style="margin-top:10px">{esc(s["name"])}.</h1>
        <p class="lede">{esc(s["lede"])}</p>
        <div class="qa"><b>In short</b><p>{esc(s["short"])}</p></div>
        <div class="phero__cta"><a class="btn btn--o" href="../contact.html#enquiry">Get a Free Consultation</a><a class="btn btn--line" href="{waurl}" target="_blank" rel="noopener"><svg class="wa" aria-hidden="true"><use href="#i-wa"/></svg>Ask about this on WhatsApp</a></div>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="process">
  <div class="wrap">
    <div class="head"><div><span class="kicker">How it works</span><h2 class="h">The process, step by step.</h2><p class="lede">This is exactly what happens from the moment you message us. You are informed at every step and nothing major goes ahead without your approval.</p></div></div>
    <ol class="steps steps--{n}">{steps}</ol>
  </div>
</section>

<section class="sec sec--cream" id="included">
  <div class="wrap split2" style="align-items:start">
    <div class="body-text">
      <span class="kicker">Who it's for</span>
      <h2 class="h">Is this service for you?</h2>
      <p>{esc(s["who"])}</p>
      <h3 style="margin-top:34px">What you receive</h3>
      <ul class="svc__mini">{receive}</ul>
    </div>
    <div class="card" style="margin-top:8px">
      <h3 style="margin-top:0">What's included</h3>
      <ul class="ticks">{included}</ul>
    </div>
  </div>
</section>

<section class="sec" id="faq">
  <div class="wrap faqwrap">
    <aside class="faqside">
      <span class="kicker">FAQ</span>
      <h2 class="h">Common questions.</h2>
      <p style="margin-top:22px"><a class="link" href="../faq.html">See all questions</a></p>
      <div class="ask"><b>Can't find your answer?</b><p>Message us and a member of our team will reply.</p><a class="btn btn--o" href="{waurl}" target="_blank" rel="noopener"><svg class="wa" aria-hidden="true"><use href="#i-wa"/></svg>Ask on WhatsApp</a></div>
    </aside>
    <div class="faqlist">{faqs}</div>
  </div>
</section>

<section class="sec" style="padding-top:0;padding-bottom:0"><div class="wrap"><div class="cpills"><span>Related services</span>{related}</div><div class="cpills"><span>All {esc(clabel.lower() if cid!="nri" else "NRI")} services</span><a href="../{chref}">{esc(clabel)}</a></div></div></section>

<section class="sec" aria-labelledby="final-h">
  <div class="wrap">
    <div class="final">
      <div>
        <h2 class="h" id="final-h">Your Property Deserves Someone You Can Trust.</h2>
        <p class="lede">Tell us about your property or land. We'll arrange a free consultation and share a proposal.</p>
        <div class="final__cta">
          <a class="btn btn--w" href="../contact.html#enquiry">Get a Free Consultation</a>
          <a class="btn btn--ghost" href="{waurl}" target="_blank" rel="noopener"><svg class="wa" aria-hidden="true"><use href="#i-wa"/></svg>Chat on WhatsApp</a>
        </div>
      </div>
      <div class="guide" id="checklist">
        <small>Free checklist</small>
        <h3>10 things every NRI property owner in Chennai should check every month</h3>
        <form id="guide-form">
          <button class="btn btn--o" type="submit"><svg class="wa" aria-hidden="true"><use href="#i-wa"/></svg>Get the checklist on WhatsApp</button>
        </form>
        <p>Opens WhatsApp with your request ready to send.</p>
      </div>
    </div>
  </div>
</section>
</main>

{footer_html}
'''
    return page

def jq(s):
    import json
    return json.dumps(s, ensure_ascii=False)

# ------------------------------------------------------------- services.html
def patch_services_overview(doc):
    def group(cid, label, lede, extra_id=None):
        items = "".join(
            f'<li><svg class="i" aria-hidden="true"><use href="#{s["icon"]}"/></svg><div><h3><a href="services/{s["slug"]}.html">{esc(s["name"])}</a></h3><p>{esc(s["lede"].split(". ")[0].rstrip(".") + ".")}</p></div></li>'
            for s in SERVICES if s["cat"] == cid)
        return f'''    <div class="sgroup" id="{cid}">
      <div><h2>{esc(label)}</h2><p class="lede">{esc(lede)}</p></div>
      <ul class="svc__list">{items}
      </ul>
    </div>
'''
    if 'id="land"' not in doc:
        land = group("land", "Land", "Plots and land checked, visited, leased and looked after.")
        doc = doc.replace('    <div class="sgroup" id="tenants-rent">', land + '    <div class="sgroup" id="tenants-rent">', 1)
    if 'id="commercial"' not in doc:
        com = group("commercial", "Commercial", "Offices, shops and warehouses, from lease to maintenance.")
        doc = doc.replace('    <div class="sgroup" id="owner-support">', com + '    <div class="sgroup" id="owner-support">', 1)
    # link existing service headings to their new pages
    for s in SERVICES:
        if s["cat"] in ("building", "owner"):
            doc = doc.replace(f'<h3>{esc(s["name"])}</h3>', f'<h3><a href="services/{s["slug"]}.html">{esc(s["name"])}</a></h3>', 1)
    doc = doc.replace('<h3>Move-in &amp; move-out</h3>', '<h3><a href="services/move-in-move-out.html">Move-in &amp; move-out</a></h3>')
    doc = doc.replace('<h3>RWA &amp; association liaison</h3>', '<h3><a href="services/rwa-association-liaison.html">RWA &amp; association liaison</a></h3>')
    return doc

# ------------------------------------------------------------------- RUN
os.makedirs(os.path.join(ROOT, "services"), exist_ok=True)
src = open(os.path.join(ROOT, "areas", "omr.html"), encoding="utf-8").read()
src = patch_nav(src, "../")
hdr = sprite_and_header(src)
ftr = footer(src)

for s in SERVICES:
    with open(os.path.join(ROOT, "services", s["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(service_page(s, hdr, ftr))

# patch every existing page
for path in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
    if os.sep + "services" + os.sep in path: continue
    rel = os.path.relpath(path, ROOT)
    p = "../" if os.sep in rel else ""
    doc = open(path, encoding="utf-8").read()
    new = patch_nav(doc, p)
    if rel == "services.html":
        new = patch_services_overview(new)
    if new != doc:
        open(path, "w", encoding="utf-8").write(new)

# sitemap
sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
if "services/land-ec-check.html" not in sm:
    entries = "".join(f'  <url>\n    <loc>{SITE}services/{s["slug"]}.html</loc>\n    <lastmod>{TODAY}</lastmod>\n  </url>\n' for s in SERVICES)
    sm = sm.replace("</urlset>", entries + "</urlset>")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(sm)

# llms.txt
lt = open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read()
if "services/land-ec-check.html" not in lt:
    lines = "\n".join(f'- [{s["name"]}]({SITE}services/{s["slug"]}.html): {s["lede"]}' for s in SERVICES)
    lt = lt.replace("- [Services](https://flourrishassets.com/services.html): all 15 services in three groups",
                    "- [Services](https://flourrishassets.com/services.html): all services in five groups: land, building, commercial, owner support and NRI\n" + lines)
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write(lt)

print("pages:", len(SERVICES))
