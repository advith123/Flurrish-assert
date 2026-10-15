"""Shared data and partials for the Flourrish static site build.

Single source of truth for contact details, navigation and service areas.
Run build.py to regenerate dist/.
"""
import html
import json
import os

SITE_URL = "https://flourrishassets.com"
BRAND = "Flourrish Asset Management"
TAGLINE = "Where Assets Flourish"
SUPPORT_LINE = "Your Property. Our Care. Always."

WHATSAPP_DISPLAY = "+91 99440 70397"
WHATSAPP_DIGITS = "919944070397"
PHONE2_DISPLAY = "+91 73585 86876"
PHONE2_TEL = "+917358586876"
EMAIL = "admin.flourrishassets@gmail.com"
HOURS = "Open all days, 9:00 AM – 7:00 PM IST"
WA_DEFAULT_MSG = "Hello Flourrish Asset Management, I would like to discuss property management for my property in India."

# Service areas — the one place to edit localities. Rendered into HTML and into assets/js/areas.js.
AREAS = [
    {"zone": "South Chennai & OMR", "areas": ["OMR (Old Mahabalipuram Road)", "Velachery", "Tambaram", "Tambaram Radial Road", "Adyar", "Besant Nagar"]},
    {"zone": "ECR", "areas": ["ECR (East Coast Road)", "Injambakkam"]},
    {"zone": "Central Chennai", "areas": ["Anna Nagar", "Nungambakkam"]},
]

NAV = [
    ("Home", "index.html"),
    ("Services", "services.html"),
    ("Property Types", "property-types.html"),
    ("How It Works", "how-it-works.html"),
    ("Areas We Serve", "areas.html"),
    ("About Us", "about.html"),
    ("Resources", "resources.html"),
    ("Contact", "contact.html"),
]

# Services: slug, title, short line, icon key
SERVICES = [
    ("complete-property-management", "Complete Property Management", "One agreed plan covering inspections, tenants, maintenance and owner updates.", "home"),
    ("tenant-management", "Tenant Management", "Enquiries, screening coordination, onboarding, communication and move-outs.", "people"),
    ("rental-management", "Rental Management", "Rent follow-ups, payment-status updates, renewal reminders and paperwork.", "receipt"),
    ("property-inspection", "Property Inspection", "Scheduled visits with dated photographs, observations and recommendations.", "camera"),
    ("maintenance-repairs", "Maintenance & Repairs", "Plumbing, electrical, painting, cleaning, carpentry and pest control, coordinated with your approval.", "tools"),
    ("vacant-property-care", "Vacant Property Care", "Regular visits, ventilation, cleaning and condition updates while nobody lives there.", "key"),
    ("nri-property-management", "NRI Property Management", "Remote communication, inspection updates and on-the-ground coordination for owners abroad.", "globe"),
    ("interior-refurbishment", "Interior Improvements & Refurbishment", "Coordination of approved improvement work with vendors and professionals.", "brush"),
]

PROPERTY_TYPES = [
    ("apartments", "Apartments & Flats", "Ongoing care for individual flats: association coordination, tenant communication and maintenance follow-up.", "service-complete-property-management.html", "apartment-exterior", "Modern apartment building in Chennai, exterior"),
    ("villas", "Villas & Independent Houses", "Regular property checks, garden and exterior upkeep, and vendor coordination for standalone homes.", "service-property-inspection.html", "villa-exterior", "Independent villa in a Chennai residential street"),
    ("rental", "Rental Properties", "Tenant enquiries, move-in and move-out coordination, rent follow-ups and agreement-renewal reminders.", "service-tenant-management.html", "rental-interior", "Furnished rental apartment interior, India"),
    ("commercial", "Commercial Properties & Offices", "Maintenance coordination and routine oversight for small offices and commercial units.", "service-maintenance-repairs.html", "commercial-exterior", "Commercial building with offices, Chennai"),
    ("vacant", "Vacant Properties", "Scheduled checks, condition updates, cleaning and upkeep coordination while the property is unoccupied.", "service-vacant-property-care.html", "vacant-interior", "Empty residential interior, India"),
]

IMAGE_SLOTS = []  # (slug, subject, where used)
PHOTOS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "photos.json")))


def placeholder(slug, subject, used_in, ratio="4x3", eager=False, cls="", sizes="(max-width: 640px) 100vw, (max-width: 1180px) 50vw, 600px", dims=(1600, 1200)):
    """Return responsive <picture> markup for a sourced photo, or an honest placeholder if none exists yet."""
    IMAGE_SLOTS.append((slug, subject, used_in))
    if slug in PHOTOS:
        alt = html.escape(PHOTOS[slug]["alt"])
        base = f"assets/img/photos/{slug}"
        load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
        c = f' class="{cls}"' if cls else ""
        return (f'<picture><source type="image/webp" srcset="{base}-800.webp 800w, {base}-1600.webp 1600w" sizes="{sizes}">'
                f'<img src="{base}-1600.jpg" srcset="{base}-800.jpg 800w, {base}-1600.jpg 1600w" sizes="{sizes}" alt="{alt}" width="{dims[0]}" height="{dims[1]}" {load}{c}></picture>')
    path = f"assets/img/ph/{slug}.svg"
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return f'<img src="{path}" alt="Placeholder image: {html.escape(subject)}" width="1600" height="1200" {load}{c}>'


def write_placeholders(out_dir):
    seen = set()
    for slug, subject, used_in in IMAGE_SLOTS:
        if slug in seen or slug in PHOTOS:
            continue
        seen.add(slug)
        w, h = 1600, 1200
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Placeholder">
<rect width="{w}" height="{h}" fill="#F5F2ED"/>
<rect x="{w*0.06:.0f}" y="{h*0.1:.0f}" width="{w*0.88:.0f}" height="{h*0.8:.0f}" fill="none" stroke="#C9C1B6" stroke-width="3" stroke-dasharray="14 12" rx="12"/>
<text x="{w/2:.0f}" y="{h/2:.0f}" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="{w*0.026:.0f}" fill="#8C847C">Photo to be supplied: {html.escape(subject)}</text>
</svg>'''
        os.makedirs(os.path.join(out_dir, "assets/img/ph"), exist_ok=True)
        with open(os.path.join(out_dir, f"assets/img/ph/{slug}.svg"), "w", encoding="utf-8") as f:
            f.write(svg)


def write_images_md(out_dir):
    lines = ["# Image inventory", "",
             "All photographs are real, openly licensed photographs from Wikimedia Commons, chosen for Indian (and wherever possible Chennai) subjects. "
             "No AI-generated imagery. Files were cropped to 4:3 and exported at 800 px and 1600 px as JPG and WebP. "
             "Attribution for CC BY / CC BY-SA images is published on `photo-credits.html`, which is linked from the footer; keep that page live while these photos are in use.", "",
             "Where no suitable open-licence photo existed for the exact subject (keys at a door, an empty interior, an inspector with a camera, a balcony), the nearest genuine subject was used and is flagged below. "
             "Replacing those with Flourrish's own photography of managed properties (with owner permission) is the single biggest remaining visual upgrade.", "",
             "| Slot | Used on | Subject wanted | Photo used | Licence / author | Files |", "|---|---|---|---|---|---|"]
    FLAGGED = {"vacant-interior": "nearest available", "service-tenant": "nearest available", "service-inspection": "nearest available", "villa-exterior": "Indian villa, not Chennai", "rental-interior": "Indian interior, not Chennai", "service-maintenance": "Indian trade work, not Chennai", "service-refurb": "Indian trade work, not Chennai", "article-maintenance": "Indian trade work, not Chennai", "service-vacant": "Tamil Nadu, not Chennai"}
    seen = set()
    for slug, subject, used_in in IMAGE_SLOTS:
        if slug in seen:
            continue
        seen.add(slug)
        if slug in PHOTOS:
            p = PHOTOS[slug]
            flag = f" ({FLAGGED[slug]})" if slug in FLAGGED else ""
            lines.append(f"| `{slug}` | {used_in} | {subject} | [{p['title']}]({p['source']}){flag} — alt: \"{p['alt']}\" | {p['lic']}, {p['artist'] or 'see source'} | `assets/img/photos/{slug}-{{800,1600}}.{{jpg,webp}}` |")
        else:
            lines.append(f"| `{slug}` | {used_in} | {subject} | MISSING — placeholder in use | — | `assets/img/ph/{slug}.svg` |")
    lines += ["", "Logo and icon assets supplied by Flourrish: `flourrish-logo.svg`, `flourrish-logo-full.svg`, the on-dark variants, `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `icon-512.png`, `og-image.jpg`."]
    with open(os.path.join(out_dir, "IMAGES.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def build_credits():
    rows = []
    seen = set()
    for slug, subject, used_in in IMAGE_SLOTS:
        if slug in seen or slug not in PHOTOS:
            continue
        seen.add(slug)
        p = PHOTOS[slug]
        rows.append(f'<li><a href="{p["source"]}" rel="noopener" target="_blank">{html.escape(p["title"])}</a> by {html.escape(p["artist"] or "the uploader credited at the source")}, {html.escape(p["lic"])}, via Wikimedia Commons. Cropped and resized. Used on: {html.escape(used_in)}.</li>')
    body = f'''
<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Photo credits</p>
    <h1>Photo credits.</h1>
    <p class="lede">The photographs on this site are real photographs of Indian properties and trades, published by their photographers under open licences. They are illustrative and do not show properties under Flourrish management.</p>
  </div>
</section>
<section class="section">
  <div class="container--narrow prose">
    <ul>{"".join(rows)}</ul>
    <p>Images licensed CC BY-SA may be reused under the same licence. Images licensed CC BY may be reused with attribution. Licence texts: <a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="noopener" target="_blank">CC BY-SA 4.0</a>, <a href="https://creativecommons.org/licenses/by/2.0/" rel="noopener" target="_blank">CC BY 2.0</a>.</p>
  </div>
</section>
'''
    return page("photo-credits.html", f"Photo Credits | {BRAND}", "Attribution for the openly licensed photographs used on the Flourrish Asset Management website.", "", body)


def write_areas_js(out_dir):
    with open(os.path.join(out_dir, "assets/js/areas.js"), "w", encoding="utf-8") as f:
        f.write("/* Generated by build/build.py from common.AREAS — edit there, not here. */\n")
        f.write("window.FLOURRISH_AREAS = " + json.dumps(AREAS, indent=2) + ";\n")


ICONS = {
    "whatsapp": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91S17.5 2 12.04 2zm0 18.15c-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.26 8.26 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24 4.54 0 8.24 3.7 8.24 8.24s-3.7 8.24-8.23 8.24zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.12-.17.25-.64.81-.78.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.51.11-.11.25-.29.37-.43.12-.14.17-.25.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.22.25-.86.85-.86 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.14-1.18-.06-.1-.22-.16-.47-.28z"/></svg>',
    "menu": '<svg class="icon-menu" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    "close": '<svg class="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>',
    "home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z"/></svg>',
    "people": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="2.5"/><path d="M15.5 14.5A5 5 0 0 1 21.5 20"/></svg>',
    "receipt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M6 3h12v18l-3-2-3 2-3-2-3 2z"/><path d="M9 8h6M9 12h6"/></svg>',
    "camera": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/></svg>',
    "tools": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M14.5 6.5a4 4 0 0 1 5-4.5l-2.5 2.5 1 2 2 1 2.5-2.5a4 4 0 0 1-5.5 5.5L8 19a2 2 0 1 1-3-3z"/></svg>',
    "key": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="8" cy="12" r="4"/><path d="M12 12h9M18 12v3M15 12v2"/></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/></svg>',
    "brush": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M3 21c3 0 5-1 5-4 0-1.5-1-2.5-2.5-2.5S3 15.5 3 17v4z"/><path d="M8.5 14.5L19 4a1.4 1.4 0 0 1 2 2L10.5 16.5"/></svg>',
    "report": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M5 3h10l4 4v14H5z"/><path d="M9 12h6M9 16h6M9 8h2"/></svg>',
    "approve": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.5 2.5L16 9.5"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12.5h5"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M12 21s-6-5.5-6-10.5a6 6 0 0 1 12 0C18 15.5 12 21 12 21z"/><circle cx="12" cy="10.5" r="2.2"/></svg>',
}


def head(title, description, path, og_image="assets/img/og-image.jpg", extra_head=""):
    canonical = f"{SITE_URL}/{'' if path == 'index.html' else path}"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#FB5206">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@700;800&display=swap">
<link rel="stylesheet" href="assets/css/style.css">
<script src="assets/js/config.js"></script>
<script src="assets/js/areas.js"></script>
{extra_head}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
'''


def nav_links(current, mobile=False):
    out = []
    for label, href in NAV:
        cur = ' aria-current="page"' if href == current else ""
        out.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return "\n".join(out)


def header(current):
    return f'''<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html" aria-label="{BRAND} home">
      <img src="assets/img/flourrish-logo.svg" alt="{BRAND}" width="176" height="36">
    </a>
    <nav class="nav" aria-label="Main">
      <ul class="nav__list">
{nav_links(current)}
      </ul>
    </nav>
    <div class="header-actions">
      <a class="btn btn--whatsapp" href="https://wa.me/{WHATSAPP_DIGITS}" data-wa="">{ICONS["whatsapp"]}<span>WhatsApp Us</span></a>
      <a class="btn btn--primary" href="contact.html#enquiry">Manage My Property</a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu">{ICONS["menu"]}{ICONS["close"]}</button>
    </div>
  </div>
</header>
<nav class="mobile-nav" id="mobile-nav" aria-label="Mobile">
  <ul>
{nav_links(current, mobile=True)}
  </ul>
  <div class="btn-row">
    <a class="btn btn--primary" href="contact.html#enquiry">Manage My Property</a>
    <a class="btn btn--whatsapp" href="https://wa.me/{WHATSAPP_DIGITS}" data-wa="">{ICONS["whatsapp"]}WhatsApp Us</a>
  </div>
</nav>
<main id="main">
'''


def area_items_flat():
    items = []
    for g in AREAS:
        items.extend(g["areas"])
    return items


def footer():
    services = "\n".join(f'<li><a href="service-{slug}.html">{title}</a></li>' for slug, title, _, _ in SERVICES)
    types_ = "\n".join(f'<li><a href="property-types.html#{slug}">{title}</a></li>' for slug, title, *_ in PROPERTY_TYPES)
    areas = "\n".join(f'<li><a href="areas.html">{a}</a></li>' for a in area_items_flat())
    return f'''</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="assets/img/flourrish-logo-full-on-dark.svg" alt="{BRAND} — Your Assets. Our Expertise" width="212" height="45">
        <p class="footer-tagline">{TAGLINE}</p>
        <p>Property management for owners of apartments, villas and other property in Chennai, wherever in the world they live.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
{services}
        </ul>
      </div>
      <div>
        <h4>Property types</h4>
        <ul>
{types_}
        </ul>
        <h4 style="margin-top:22px">Company</h4>
        <ul>
          <li><a href="about.html">About us</a></li>
          <li><a href="how-it-works.html">How it works</a></li>
          <li><a href="proposal.html">Management proposal</a></li>
          <li><a href="faq.html">FAQs</a></li>
          <li><a href="resources.html">Resources</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Areas we serve</h4>
        <ul>
{areas}
        </ul>
      </div>
      <div>
        <h4>Get in touch</h4>
        <ul class="footer-contact">
          <li><a href="https://wa.me/{WHATSAPP_DIGITS}" data-wa="">{WHATSAPP_DISPLAY}</a><span>WhatsApp</span></li>
          <li><a href="tel:{PHONE2_TEL}">{PHONE2_DISPLAY}</a><span>Phone 2</span></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a><span>Email</span></li>
          <li>{HOURS}<span>Business hours</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div>© <span data-year>2026</span> {BRAND}. All rights reserved.</div>
      <div><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Service</a><a href="photo-credits.html">Photo credits</a></div>
    </div>
  </div>
</footer>
<a class="wa-float" href="https://wa.me/{WHATSAPP_DIGITS}" data-wa="" aria-label="Chat on WhatsApp">{ICONS["whatsapp"]}</a>
<script src="assets/js/main.js"></script>
'''


def page(path, title, description, current, body, extra_head="", extra_scripts=""):
    return head(title, description, path, extra_head=extra_head) + header(current) + body + footer() + extra_scripts + "</body>\n</html>\n"


COUNTRIES = [
    ("India", "+91"), ("United States", "+1"), ("United Kingdom", "+44"), ("United Arab Emirates", "+971"), ("Singapore", "+65"),
    ("Australia", "+61"), ("Canada", "+1"), ("Qatar", "+974"), ("Saudi Arabia", "+966"), ("Oman", "+968"), ("Kuwait", "+965"),
    ("Bahrain", "+973"), ("Malaysia", "+60"), ("Germany", "+49"), ("Netherlands", "+31"), ("Ireland", "+353"), ("France", "+33"),
    ("Switzerland", "+41"), ("New Zealand", "+64"), ("Japan", "+81"), ("Hong Kong", "+852"), ("South Africa", "+27"), ("Other", ""),
]


def enquiry_form(heading="Tell us about your property.", intro="Share a few details and our team will contact you to discuss the right management approach. No documents are needed at this stage."):
    countries = "\n".join(f'<option value="{c}" data-code="{code}">{c}</option>' for c, code in COUNTRIES)
    services = "\n".join(f'<option>{t}</option>' for _, t, _, _ in SERVICES)
    return f'''<div class="form-card" id="enquiry">
  <h2 style="font-size:clamp(1.6rem,2.6vw,2.1rem)">{heading}</h2>
  <p class="lede" style="margin-bottom:28px">{intro}</p>
  <form data-enquiry novalidate>
    <div class="form-grid">
      <div class="field">
        <label for="f-name">Full name</label>
        <input id="f-name" name="name" type="text" autocomplete="name" data-required="Enter your name.">
        <span class="error"></span>
      </div>
      <div class="field">
        <label for="f-email">Email address</label>
        <input id="f-email" name="email" type="email" autocomplete="email" data-required="Enter your email so we can follow up.">
        <span class="error"></span>
      </div>
      <div class="field">
        <label for="f-country">Country of residence</label>
        <select id="f-country" name="country" autocomplete="country-name" data-required="Choose your country.">
          <option value="">Select a country</option>
{countries}
        </select>
        <span class="error"></span>
      </div>
      <div class="field">
        <label for="f-phone">WhatsApp or phone number</label>
        <div class="phone-row">
          <input name="phone_code" type="text" inputmode="tel" aria-label="Country calling code" placeholder="+91" autocomplete="tel-country-code">
          <input id="f-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel-national" data-required="Enter a phone or WhatsApp number.">
        </div>
        <span class="error"></span>
      </div>
      <div class="field">
        <label for="f-location">Property location in India</label>
        <select id="f-location" name="property_location" data-areas data-required="Tell us where the property is.">
          <option value="">Select the locality</option>
        </select>
        <span class="hint">If it is not listed, choose "Other" and add the locality in the details box.</span>
        <span class="error"></span>
      </div>
      <div class="field">
        <label for="f-type">Property type</label>
        <select id="f-type" name="property_type" data-required="Choose the property type.">
          <option value="">Select a type</option>
          <option>Apartment / flat</option>
          <option>Villa / independent house</option>
          <option>Commercial property / office</option>
          <option>Plot / land</option>
          <option>Other</option>
        </select>
        <span class="error"></span>
      </div>
      <div class="field">
        <label for="f-occupancy">Occupancy status</label>
        <select id="f-occupancy" name="occupancy" data-required="Tell us who is living there, if anyone.">
          <option value="">Select status</option>
          <option>Vacant</option>
          <option>Tenant-occupied</option>
          <option>Owner-occupied</option>
          <option>Under construction / handover pending</option>
        </select>
        <span class="error"></span>
      </div>
      <div class="field">
        <label for="f-service">Service required</label>
        <select id="f-service" name="service" data-required="Choose the service you are interested in.">
          <option value="">Select a service</option>
{services}
          <option>Not sure yet — need advice</option>
        </select>
        <span class="error"></span>
      </div>
      <div class="field">
        <label for="f-count">Number of properties <span class="hint">(optional)</span></label>
        <input id="f-count" name="properties_count" type="number" min="1" max="50" inputmode="numeric">
      </div>
      <div class="field">
        <label for="f-contact">Preferred contact method</label>
        <select id="f-contact" name="contact_method" data-required="Choose how you would like us to reach you.">
          <option value="">Select one</option>
          <option>WhatsApp</option>
          <option>Phone call</option>
          <option>Email</option>
        </select>
        <span class="error"></span>
      </div>
      <div class="field field--full">
        <label for="f-details">Anything else we should know? <span class="hint">(optional)</span></label>
        <textarea id="f-details" name="details" placeholder="Current tenant situation, known repairs, how often you would like updates, time zone…"></textarea>
      </div>
      <div class="field field--full">
        <label class="check">
          <input type="checkbox" name="consent" data-required="Please confirm we may contact you about this enquiry.">
          <span>I agree that Flourrish Asset Management may contact me about this enquiry by the method I have chosen. Details are handled as described in the <a href="privacy.html">privacy policy</a>.</span>
        </label>
        <span class="error"></span>
      </div>
      <div class="hp" aria-hidden="true"><label>Leave this field empty <input type="text" name="company_website" tabindex="-1" autocomplete="off"></label></div>
    </div>
    <div class="form-actions">
      <button class="btn btn--primary btn--lg" type="submit">Send my enquiry</button>
      <span class="hint">Prefer messaging? <a href="https://wa.me/{WHATSAPP_DIGITS}" data-wa="">Write to us on WhatsApp</a> instead.</span>
    </div>
    <div class="form-status" tabindex="-1"></div>
  </form>
</div>'''


def cta_band(heading="Ready to talk about your property?", lede="Tell us what you own and where it is. We will come back to you with questions, not a sales pitch."):
    return f'''<section class="section section--tight cta-band">
  <div class="container">
    <div>
      <h2>{heading}</h2>
      <p class="lede">{lede}</p>
    </div>
    <div class="btn-row">
      <a class="btn btn--primary btn--lg" href="contact.html#enquiry">Discuss Your Property</a>
      <a class="btn btn--whatsapp btn--lg" href="https://wa.me/{WHATSAPP_DIGITS}" data-wa="">{ICONS["whatsapp"]}WhatsApp Us</a>
    </div>
  </div>
</section>
'''


def faq_block(items, searchable=False):
    rows = "\n".join(f'<details><summary>{q}</summary><div><p>{a}</p></div></details>' for q, a in items)
    search = '''<div class="faq-search"><label class="visually-hidden" for="faq-q">Search questions</label><input id="faq-q" type="search" placeholder="Search questions, e.g. inspections, tenants, fees" data-faq-search></div>''' if searchable else ""
    return f'''{search}
<div class="faq" data-faq>
{rows}
<p class="faq-empty">No questions match that. Ask us directly on WhatsApp or through the contact page.</p>
</div>'''


def faq_jsonld(items):
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items],
    }
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'


def business_jsonld():
    data = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": BRAND,
        "url": SITE_URL,
        "email": EMAIL,
        "telephone": "+91-99440-70397",
        "description": "Property management for apartment, villa and commercial property owners in Chennai, including owners living abroad.",
        "areaServed": {"@type": "City", "name": "Chennai"},
        "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "09:00", "closes": "19:00"},
        "sameAs": [],
    }
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'
