# Flourrish Asset Management — website

Static site: HTML5, CSS3, vanilla JavaScript and SVG. No frameworks, no build step required to run it. Open `dist/index.html` directly from disk or upload the contents of `dist/` to any static host.

## Folder layout

```
dist/                      ← the website (deploy this folder)
  index.html, services.html, service-*.html, property-types.html,
  how-it-works.html, areas.html, about.html, resources.html,
  article-*.html, faq.html, contact.html, proposal.html,
  privacy.html, terms.html, 404.html
  sitemap.xml, robots.txt, IMAGES.md
  assets/css/style.css     ← all styles; design tokens at the top of the file
  assets/js/config.js      ← contact details + form endpoint (edit this)
  assets/js/areas.js       ← generated from build/common.py (do not edit by hand)
  assets/js/main.js        ← header, mobile nav, WhatsApp links, FAQ search, area selects
  assets/js/form.js        ← enquiry form validation and submission
  assets/js/globe.js       ← hero globe (canvas, no libraries)
  assets/js/land-dots.js   ← precomputed land dot grid for the globe
  assets/img/logo.svg      ← PLACEHOLDER: replace with the approved logo
  assets/img/favicon.svg   ← placeholder favicon in the brand orange
  assets/img/og-default.png
  assets/img/ph/*.svg      ← placeholder images (see IMAGES.md)
build/                     ← Python generator for the HTML pages (optional)
  build.py                 ← python3 build/build.py → regenerates dist/*.html, sitemap, areas.js, placeholders
  common.py                ← contact details, navigation, service areas, services list, shared partials
  content_home.py          ← home page
  content_services.py      ← service pages, services index, property types, how it works
  content_pages.py         ← areas, about, FAQ, contact, proposal, privacy, terms, 404
  content_resources.py     ← resources index and articles
```

You can edit the HTML in `dist/` directly. The generator exists so that header, footer, navigation and the areas list change in one place; if you use it, make content edits in `build/` and rerun `python3 build/build.py` (Python 3, no packages needed; Pillow is optional for regenerating the OG image).

## Things to do before launch

1. **Logo** — done. The supplied `flourrish-logo.svg` is in the header, `flourrish-logo-full-on-dark.svg` in the footer, and `favicon.svg` / `favicon-32.png` / `apple-touch-icon.png` are linked. `og-image.jpg` (supplied) is the social-sharing image on every page. Note: the supplied logo carries the line "Your Assets. Our Expertise"; the site copy uses "Where Assets Flourish" as the primary tagline per the brief. Confirm which line is current.
2. **Photographs** — all 19 slots now hold real, openly licensed photographs from Wikimedia Commons (no AI imagery), cropped to 4:3 and exported as JPG + WebP at 800/1600 px. `dist/IMAGES.md` is the full inventory with source, licence, author, alt text and which slots are "nearest available" rather than exact. `photo-credits.html` carries the required CC BY / CC BY-SA attribution and is linked from the footer; keep it live. The best remaining upgrade is replacing the nine flagged slots with Flourrish's own photography of Chennai properties (with owner permission) — see the flags in `IMAGES.md`.
3. **Form endpoint** — done in code; needs one secret at deploy time. `config.js` points the form at `/api/enquiry`, which is served by `functions/api/enquiry.js` on Cloudflare Pages or by `server/server.js` on any Node host (see Deployment). Set `RESEND_API_KEY` (and `ENQUIRY_FROM` on a verified domain) or the endpoint returns a clear "not configured" error and the form tells the visitor to use WhatsApp — it never shows a false success. Opened from disk, the form always falls back to WhatsApp.
4. **Legal pages** — `privacy.html` and `terms.html` carry a "Draft for review" box. Have them reviewed, then delete that paragraph (search for `callout` in those two files or in `build/content_pages.py`).
5. **Founder bios** — the About page lists Farrah (Founder) and Shakeel (Co-Founder) with a note that bios will follow. No photos or portrait sections, per the current decision.
6. **Analytics / Search Console** — nothing is wired in. Add the verification tag and any analytics snippet to `head()` in `build/common.py` (or to each page's `<head>`), and update the cookies paragraph in the privacy policy if tracking is added.
7. **Fonts** — Inter and Manrope load from Google Fonts with system fallbacks, so the site still reads correctly offline or from `file://` without the webfonts.

## Changing contact details or service areas

- WhatsApp number, pre-filled message, email and form endpoint: `dist/assets/js/config.js` (runtime) and `build/common.py` (what is printed in the HTML). Keep both in sync, or just rebuild.
- Service areas: edit `AREAS` in `build/common.py` and rebuild. That single list feeds the home-page section, the Areas page, the footer and the "Property location" select in the form.
- Business hours: `HOURS` in `build/common.py`.
- Second number is labelled "Phone 2" throughout.

## Deliberate choices

- No pricing appears anywhere. `proposal.html` explains what the fee depends on and ends in "Request a proposal".
- No testimonials, ratings, client counts, years in business, awards or guarantees. The About page has an "Our approach to property care" section in place of testimonials until permissioned ones exist.
- The sample inspection report on the home page is labelled illustrative in two places.
- Overseas cities on the globe are owner locations; copy states repeatedly that properties are managed in Chennai only.
- Wording avoided site-wide: "local team", "Chennai team", "not a broker".

## Checks run before handover

Headless Chromium, every page: no console errors; no horizontal overflow from 320px to 1600px; all internal links resolve; all images load; mobile menu opens, closes on Escape and on link tap; WhatsApp links are built from `config.js`; the form blocks empty submission with field-level errors and opens WhatsApp with the enquiry when no endpoint is set; FAQ search filters and shows an empty state; the globe renders a static frame under `prefers-reduced-motion`.

Not yet measured: Core Web Vitals on a live host (the globe scripts are deferred and under 40 KB total; real photographs will dominate LCP, so size them to the slot and serve WebP/AVIF where possible).


## Revision 2 (refinement pass)

Changed files: `build/common.py` (logo/favicon/OG tags, responsive `<picture>` markup, credits page, inventory writer), `build/build.py`, `build/photos.json` (new), `build/content_home.py` (hero copy, sample-report label, hero photo), `build/content_services.py` (services index now uses photo cards), `dist/assets/css/style.css` (brand orange #FB5206 to match the logo, header/footer logo sizing, photo cards, picture handling, header fit), `dist/assets/js/globe.js` (depth shading, dot contrast, brand orange), all 25 generated pages, `dist/IMAGES.md`, `dist/assets/img/photos/*` (76 files), supplied brand assets copied into `dist/assets/img/`.

Design changes with a reason: real photography replaces every dashed placeholder (credibility); the approved logo at consistent sizes in header, footer and icons (brand integrity); the services index moved from an icon list to photo cards so the page is not a wall of identical rows; the globe gained edge shading and darker land dots so it reads as a sphere on bright screens; the header was tightened so all eight nav items, both buttons and the wider logo fit at 1280–1600 without wrapping.

QA results: zero console errors and zero failed requests on all 25 pages; no horizontal overflow at 320, 375, 390, 430, 768, 1024, 1100, 1200, 1280, 1366, 1440, 1600 and 1920 px; every internal link resolves; every image loads after scroll (lazy images included); form, mobile nav, FAQ search and WhatsApp links re-tested. Core Web Vitals still need measuring on the live host; the hero image is 1600 px JPG/WebP with `fetchpriority="high"`, everything else lazy-loads.

Honest rating: 8/10. What holds it back from 9: a few photos are "nearest available" (towers instead of keys at a door, an electrician's panel instead of an inspector with a camera), the villa and interior photos are Indian but not Chennai, and no real testimonials or founder bios exist yet. Those are content dependencies on Flourrish, not code.

## Revision 3 (push further)

- Hero headline now carries the brand's orange accent on the second sentence ("Our responsibility."), echoing the supplied og-image treatment, with a short dash-marked eyebrow above it. The same orange-dash eyebrow labels every home-page section, which gives the long page a consistent rhythm without resorting to all-caps labels.
- New full-bleed brand-statement band between the trust section and services: wide Chennai skyline photograph (same CC BY-SA source as the NRI service hero, cropped 2.4:1) with the supporting tagline "Your property. Our care. Always." This is the one place the site goes edge to edge.
- The NRI section's numbered list became a sample owner-update card (three messages: inspection, quotation awaiting approval, completion), labelled illustrative. It shows the approval loop instead of describing it; nothing in it is a working control.
- Quiet hover states on property, service and article cards (2 px lift, slow image zoom); the sample-report thumbnails use dashed tiles instead of flat grey blocks.
- QA re-run after these changes: zero console errors, no horizontal overflow at 320/390/1024/1440/1600 on all 25 pages, no broken links or failed requests.

Rating after this pass: 8.5/10. The remaining half point is still photography and real social proof from Flourrish.

## Deployment (revision 4 — production hardening)

Folder layout now includes a small backend for the enquiry form, with no dependencies:

```
functions/api/enquiry.js        Cloudflare Pages Function: POST /api/enquiry
functions/api/_lib/enquiry.js   shared validation, rate-limit, email payload (Resend API)
server/server.js                Node 18+ alternative: serves dist/ and handles /api/enquiry
package.json                    npm run build | start | dev (dev = dry-run, no email sent)
dist/_headers                   security headers + CSP + cache rules (Cloudflare Pages / Netlify format)
dist/site.webmanifest           PWA manifest with the supplied icons
```

### Option A — Cloudflare Pages (recommended, free tier is enough)
1. Push this folder to a Git repo. In Cloudflare Pages: Create project → connect repo → build command: *(none)* → build output directory: `dist`. Pages picks up `functions/` automatically.
2. Settings → Environment variables: `RESEND_API_KEY` (from resend.com after verifying `flourrishassets.com`), `ENQUIRY_FROM` = `Flourrish Website <enquiries@flourrishassets.com>`, optionally `ENQUIRY_TO` (defaults to admin.flourrishassets@gmail.com).
3. Optional: create a KV namespace and bind it as `RATE_KV` to enable per-IP rate limiting (5 submissions / 10 min). Without it the honeypot and validation still run.
4. Custom domain → `flourrishassets.com`. Canonical URLs and the sitemap already use that domain.

### Option B — any Node host / VPS
`npm start` serves `dist/` on port 8787 with the same `/api/enquiry` handler and in-memory rate limiting. Put nginx or Caddy in front for TLS. Same environment variables as above. `npm run dev` runs in dry-run mode (validates, returns success, sends nothing) for local testing.

### Option C — pure static host (GitHub Pages, S3, shared hosting)
No backend is available, so set `formEndpoint` in `dist/assets/js/config.js` to a Formspree URL (and add `https://formspree.io` to `connect-src` in `_headers` if the host honours it), or to `''` to route all enquiries through WhatsApp.

### What the backend does
Validates every field server-side with length limits, rejects on missing consent, silently accepts honeypot hits, rate-limits per IP, emails the enquiry through Resend with the owner's address as reply-to, and returns field-level errors that the form displays inline. The frontend only shows "sent" on a `200 {ok:true}`.

### Verified in this revision
Node server tested locally in dry-run: validation returns per-field errors (400), honeypot returns 200 without sending, GET returns 405, unknown paths serve `404.html` with a 404 status, full form submission end-to-end from the browser shows the success state and resets the form, server-side field errors surface inline, and the sixth request from one IP inside ten minutes gets 429. The Cloudflare function shares the same validation module; it has not been run under wrangler here, so do one test submission after the first deploy.

### Not done, by design
No analytics, no cookies, no third-party scripts (the CSP would block them anyway — extend `script-src` when you add Search Console verification or analytics). Core Web Vitals should be measured with PageSpeed Insights once the site is on its real host and CDN.
