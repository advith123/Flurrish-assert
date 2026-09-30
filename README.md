# Flourrish Asset Management — Website

Static website: plain HTML, one stylesheet, one script. No framework, no build step.
Open `index.html` in a browser to view it, or upload the whole folder to any web host.

## Folder structure

```
flourrish-website/
├── index.html                      Home
├── services.html                   All 15 services, approval flow, emergency response
├── nri-property-management.html    NRI owners
├── pricing.html                    12% fee, what's included, worked example
├── faq.html                        20 FAQs with search and topic filters
├── about.html                      Story, mission, vision, why Flourrish, areas
├── contact.html                    Free consultation form (sends via WhatsApp)
├── blog.html                       Article list
├── blog/
│   ├── manage-chennai-property-from-usa.html
│   ├── tenant-verification-checklist-tamil-nadu.html
│   └── nri-tax-basics-rental-income.html
├── areas/
│   ├── index.html                  Areas we serve (hub)
│   ├── omr.html                    OMR: Perungudi, Thoraipakkam, Sholinganallur
│   ├── ecr.html                    ECR: villas and beach houses
│   ├── south-chennai.html          Adyar, Besant Nagar, Velachery
│   └── tambaram-gst-road.html      Tambaram, Pallavaram, Medavakkam, Chengalpattu
├── nri/
│   ├── usa-canada.html             NRIs in the USA and Canada
│   ├── uae-gulf.html               NRIs in the UAE and Gulf
│   ├── uk-europe.html              NRIs in the UK and Europe
│   └── singapore-australia.html    NRIs in Singapore, Malaysia and Australia
├── chennai-property-glossary.html  Patta, EC, POA, NRO, TDS and more
├── legal.html                      Privacy, terms, disclaimer, photo credits
├── 404.html                        "Page not found" page
├── robots.txt                      Crawler rules (search engines and AI assistants welcome)
├── sitemap.xml                     All public pages, for Google and Bing
├── llms.txt                        Short summary of the business for AI assistants
├── llms-full.txt                   Full text reference for AI assistants
├── site.webmanifest                Browser/app icon settings
├── docs/
│   ├── SEO-AEO-GEO-PLAN.md         Who to target, where, what to publish, how to measure
│   └── keyword-map.csv             Page-by-page keywords, questions and audiences
├── css/
│   └── style.css                   All styles (contents list at the top of the file)
├── js/
│   └── main.js                     Menu, time-zone card, FAQ search, forms
└── assets/
    ├── brand/                      Logo (colour + white), favicon, apple icon, social share image
    ├── icons/                      Flourrish icon pack (SVG)
    ├── location/chennai-map.svg    Areas map
    └── images/
        ├── hero/                   Home hero photo
        ├── nri/                    NRI video call, monthly report, owner dashboard
        ├── properties/             Apartment, villa, house, office, commercial, vacant
        ├── sections/               Local owners, Chennai skyline, OMR apartments
        └── blog/                   Article cover images
```

Every photo has two sizes: `name.jpg` (large, for big and high-resolution screens)
and `name-700.jpg` / `name-800.jpg` etc. (small, for phones). Browsers pick the right
one automatically through `srcset`.

## Common edits

- **Replace a photo:** keep the same file name and export both sizes
  (e.g. `villa.jpg` at 1400px wide and `villa-700.jpg` at 700px wide).
- **WhatsApp number:** change `WHATSAPP_NUMBER` at the top of `js/main.js`, then
  search all `.html` files for `919392314373` and replace it.
- **Header and footer:** these are repeated in every page. If you change a menu link,
  change it in each `.html` file (find-and-replace works well).
- **Colours and fonts:** edit the tokens at the top of `css/style.css` (`--o`, `--ink`, …).
- **Icons:** the SVG files are in `assets/icons/`. Each page also contains an inline
  copy of the icon set (at the top of `<body>`) so pages work when opened straight
  from disk.

## Search (SEO, AEO, GEO)

Every page has a canonical URL on https://flourrishassets.com, a written title and
description, Open Graph tags and schema.org structured data in a
`<script type="application/ld+json">` block. The full plan, including Google Business
Profile setup, reviews, content calendar and measurement, is in
`docs/SEO-AEO-GEO-PLAN.md`.

When you add or change a page: give it a unique title and description, add its URL to
`sitemap.xml` and `llms.txt`, and update the `<lastmod>` date in `sitemap.xml`.

## Forms

The site has no server. The consultation form and checklist form open WhatsApp with
the visitor's details pre-filled. To collect submissions by email instead, connect a
form service (e.g. Formspree or Netlify Forms) and replace the handlers in section 5
of `js/main.js`.

## Before going live

- [ ] Replace the review placeholders on the home page with real client reviews (with permission).
- [ ] Add the real Facebook, Instagram, LinkedIn and YouTube links (footer, every page).
- [ ] Confirm `hello@flourrish.in` and the Mon–Sat 9:00–6:00 hours.
- [ ] Have the Privacy Policy and Terms (in `legal.html`) finalised by a legal advisor.
- [ ] Follow the launch checklist in `docs/SEO-AEO-GEO-PLAN.md` (Search Console, Bing,
      Google Business Profile, schema tests).
- [ ] Keep the Photo credits section in `legal.html` while the Wikimedia Commons photos are used.

## Hosting

Any static host works: Netlify (drag and drop the folder), Vercel, GitHub Pages,
Cloudflare Pages, or standard web hosting. `404.html` is picked up automatically by
Netlify, Cloudflare Pages and GitHub Pages.
