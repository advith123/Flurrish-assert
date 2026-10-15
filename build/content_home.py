from common import *

HOME_FAQ = [
    ("Can Flourrish manage my property if I live abroad?", "Yes. Most of our owners are not in Chennai. Inspection reports, maintenance quotations and approvals move over WhatsApp and email, and property visits happen locally in Chennai. The frequency of visits and updates is set in your management plan."),
    ("How are maintenance costs approved?", "For anything that is not an emergency, you receive the issue, the vendor's quotation and the expected cost first. Work starts only after you approve it. Emergency handling is defined in the agreement before onboarding."),
    ("How are inspections documented?", "Each scheduled visit produces a dated report with photographs, observations and recommended actions, sent to you by the channel agreed in your plan."),
    ("What does a management plan cost?", "Fees depend on the property, its occupancy, how often you want inspections and what you need coordinated. We prepare a written proposal after a short call, so you can see the scope and fee together before deciding."),
    ("Does the service start as soon as I enquire?", "No. An enquiry starts a conversation. Management begins only after the scope, fee and reporting arrangement are agreed in writing."),
]


def build_home():
    services_html = "\n".join(
        f'''<a class="service-item" href="service-{slug}.html">
  <span class="service-item__icon">{ICONS[icon]}</span>
  <span><h3>{title}</h3><p>{line}</p></span>
</a>''' for slug, title, line, icon in SERVICES)

    type_cards = "\n".join(
        f'''<article class="type-card" id="{slug}">
  {placeholder(img, subject, "Home + Property types", cls="type-card__img")}
  <div class="type-card__body">
    <h3>{title}</h3>
    <p>{desc}</p>
    <a class="text-link" href="{link}">Explore this service</a>
  </div>
</article>''' for slug, title, desc, link, img, subject in PROPERTY_TYPES)

    area_groups = "\n".join(
        f'''<div class="area-group"><h3>{g["zone"]}</h3><ul>{"".join(f"<li>{a}</li>" for a in g["areas"])}</ul></div>''' for g in AREAS)

    body = f'''
<section class="hero">
  <div class="container">
    <div class="hero__grid">
      <div class="hero__copy">
        <p class="eyebrow">Property management in Chennai</p>
        <h1>Your property in India. <span class="accent">Our responsibility.</span></h1>
        <p class="lede lede--lg">From tenant coordination and property inspections to maintenance and owner updates, Flourrish helps you care for your Indian property while you focus on what matters most.</p>
        <div class="btn-row">
          <a class="btn btn--primary btn--lg" href="contact.html#enquiry">Manage My Property</a>
          <a class="btn btn--secondary btn--lg" href="services.html">Explore Our Services</a>
        </div>
        <p class="hero__tertiary">Prefer to talk first? <a href="https://wa.me/{WHATSAPP_DIGITS}" data-wa="">Speak to our team on WhatsApp</a></p>
      </div>
      <div class="hero__visual">
        <div class="globe-wrap" data-globe>
          <canvas aria-label="Globe showing owner locations around the world connected to Chennai, India" role="img"></canvas>
          <svg class="globe-fallback" viewBox="0 0 400 400" aria-hidden="true">
            <defs><radialGradient id="gf" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#E9E2D9"/></radialGradient></defs>
            <circle cx="200" cy="200" r="184" fill="url(#gf)" stroke="#D4CEC5"/>
            <ellipse cx="200" cy="200" rx="184" ry="60" fill="none" stroke="#E7E2DB"/><ellipse cx="200" cy="200" rx="184" ry="130" fill="none" stroke="#E7E2DB"/>
            <ellipse cx="200" cy="200" rx="60" ry="184" fill="none" stroke="#E7E2DB"/><ellipse cx="200" cy="200" rx="130" ry="184" fill="none" stroke="#E7E2DB"/>
            <circle cx="262" cy="214" r="7" fill="#FC5200"/><text x="276" y="219" font-family="Manrope, Inter, sans-serif" font-weight="700" font-size="15" fill="#1F1A16">Chennai</text>
          </svg>
          <figure class="hero__photo">
            {placeholder("hero-property", "Premium residential apartment building in Chennai, warm evening light", "Home hero", eager=True, sizes="(max-width: 960px) 0px, 220px")}
            <figcaption>Residential towers, Chennai</figcaption>
          </figure>
        </div>
        <p class="globe-caption">Your world. Your property in India. Our care in Chennai.</p>
      </div>
    </div>
  </div>
</section>

<div class="trust-strip">
  <div class="container">
    <span>Property care in Chennai</span>
    <span>Clear, documented communication</span>
    <span>Confidence from anywhere in the world</span>
  </div>
</div>

<section class="section" id="property-types">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Property types</p>
      <h2>Every property deserves the right care.</h2>
      <p class="lede">From a single apartment to a standalone villa, the management plan is shaped around what your property needs, not a fixed package.</p>
    </div>
    <div class="card-grid card-grid--5">
{type_cards}
    </div>
  </div>
</section>

<section class="section section--stone" id="trust">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">How we work</p>
      <h2>Confidence comes from knowing what's happening.</h2>
      <p class="lede">You are handing a valuable asset to people you may never meet in person. So we show you the process rather than ask you to take our word for it.</p>
    </div>
    <div class="trust-layout">
      <div class="pillars">
        <div class="pillar">
          <span class="pillar__mark">{ICONS["camera"]}</span>
          <div><h3>Documented property inspections</h3><p>Scheduled visits are recorded with dated photographs, condition notes and a list of follow-up actions, so you see the state of the property rather than a summary of it.</p></div>
        </div>
        <div class="pillar">
          <span class="pillar__mark">{ICONS["approve"]}</span>
          <div><h3>Maintenance you approve before it starts</h3><p>For non-emergency work you receive the issue description, the vendor's quotation and the expected cost, and the work proceeds only after your approval, as set out in your service terms.</p></div>
        </div>
        <div class="pillar">
          <span class="pillar__mark">{ICONS["chat"]}</span>
          <div><h3>Clear owner communication</h3><p>Updates on inspections, tenants, maintenance requests and completed work arrive on the channel and schedule agreed in your plan, usually WhatsApp and email.</p></div>
        </div>
        <div class="pillar">
          <span class="pillar__mark">{ICONS["pin"]}</span>
          <div><h3>Accountable support on the ground</h3><p>Vendors, property visits and follow-up tasks are coordinated in Chennai by people who are answerable to you for each item until it is closed.</p></div>
        </div>
      </div>
      <div class="report" aria-label="Sample inspection report (illustrative)">
        <div class="report__head"><strong>Inspection report</strong><span class="badge">Sample report — illustrative example</span></div>
        <div class="report__body">
          <dl class="report__row"><dt>Property</dt><dd>2 BHK apartment, 4th floor (example)</dd></dl>
          <dl class="report__row"><dt>Visit date</dt><dd>14 March (example)</dd></dl>
          <dl class="report__row"><dt>Status</dt><dd><span class="badge badge--neutral">Vacant · inspected</span></dd></dl>
          <div class="report__thumbs" aria-label="Photo thumbnails"><span>Living room</span><span>Kitchen</span><span>Bathroom ceiling</span><span>Balcony</span></div>
          <dl class="report__row"><dt>Observations</dt><dd>Minor seepage mark on the bathroom ceiling, likely from the flat above. Balcony drain clear. All taps checked; no leaks. Electricity meter reading noted.</dd></dl>
          <dl class="report__row"><dt>Recommended action</dt><dd>Raise the seepage with the association; get a plumber to inspect the upstairs bathroom outlet.</dd></dl>
          <dl class="report__row"><dt>Estimated cost</dt><dd>Illustrative figure, pending vendor quotation</dd></dl>
          <dl class="report__row"><dt>Owner approval</dt><dd><span class="badge">Awaiting approval</span></dd></dl>
          <dl class="report__row"><dt>Completion</dt><dd>Not started</dd></dl>
        </div>
        <div class="report__foot">This is a demonstration of the report format. It does not describe a real property, client or visit.</div>
      </div>
    </div>
  </div>
</section>

<section class="statement" aria-labelledby="statement-h">
  {placeholder("statement-skyline", "Wide Chennai skyline", "Home brand statement band", cls="statement__img", sizes="100vw", dims=(1600, 667))}
  <div class="container">
    <h2 id="statement-h">Your property. <span class="accent">Our care. Always.</span></h2>
    <p>Apartments, villas and commercial property in Chennai, looked after for owners in Adyar, Dubai, London, Singapore and Seattle alike. Where assets flourish.</p>
  </div>
</section>

<section class="section" id="services">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Services</p>
      <h2>What we take care of.</h2>
      <p class="lede">Choose a single service or combine them into one management plan. Each service has its own page explaining what is included and what is not.</p>
    </div>
    <div class="service-list">
{services_html}
    </div>
    <p style="margin-top:28px"><a class="text-link" href="services.html">See all services in detail</a></p>
  </div>
</section>

<section class="section section--stone" id="how-it-works">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">The process</p>
      <h2>Property management, made clear.</h2>
      <p class="lede">Four steps from first message to ongoing updates. Nothing starts until the plan is agreed.</p>
    </div>
    <div class="steps">
      <div class="step"><h3>Tell us about your property</h3><p>Share the property type, location, occupancy and what you need handled, through the form or WhatsApp.</p></div>
      <div class="step"><h3>Discuss your requirements</h3><p>We call or message you to understand the property, your expectations, service needs and budget.</p></div>
      <div class="step"><h3>Agree on the management plan</h3><p>You receive the proposed scope, fee, responsibilities, approval process and reporting frequency in writing before onboarding.</p></div>
      <div class="step"><h3>Stay informed</h3><p>After onboarding, inspections, updates and reports follow the schedule in your plan.</p></div>
    </div>
    <p style="margin-top:36px"><a class="text-link" href="how-it-works.html">Read how it works in more detail</a></p>
  </div>
</section>

<section class="section section--night" id="nri">
  <div class="container">
    <div class="split split--top">
      <div>
        <p class="eyebrow">For owners abroad and out of town</p>
        <h2>Your property is in India. You don't have to be.</h2>
        <p class="lede">Owners abroad and owners in other Indian cities share the same problems:</p>
        <ul class="concerns">
          <li>You cannot fly in every time a tap leaks or a tenant has a question.</li>
          <li>You want to see the property's condition, not just hear that it is "fine".</li>
          <li>You want to know what a repair will cost before anyone starts.</li>
          <li>You need someone to coordinate tenants, vendors and the association.</li>
          <li>You want one accountable point of contact, in your time zone's waking hours where possible.</li>
        </ul>
        <div class="btn-row">
          <a class="btn btn--primary" href="service-nri-property-management.html">NRI Property Management</a>
          <a class="btn btn--ghost-light" href="contact.html#enquiry">Discuss Your Property</a>
        </div>
      </div>
      <div>
        <div class="night-photo" style="margin-bottom:28px">{placeholder("nri-apartment", "Apartment living room with balcony view, Chennai", "Home NRI section")}</div>
        <div class="update-card" aria-label="Sample owner update (illustrative)">
          <div class="update-card__head"><strong>Owner update</strong><span class="badge">Sample — illustrative example</span></div>
          <div class="update-card__msg">
            <span class="update-card__meta">Inspection completed · 2 BHK apartment (example)</span>
            <p>Visited today. Taps, switches, geyser and balcony drain checked. One item needs your decision: a seepage mark on the bathroom ceiling, probably from the flat above. Photos attached.</p>
            <div class="update-card__thumbs"><span>Ceiling</span><span>Geyser</span><span>Balcony</span></div>
          </div>
          <div class="update-card__msg">
            <span class="update-card__meta">Recommendation and quotation</span>
            <p>Plumber to inspect the upstairs outlet and reseal. Vendor quotation attached (illustrative). Reply with approval, or ask a question.</p>
            <span class="update-card__status">Awaiting your approval</span>
          </div>
          <div class="update-card__msg update-card__msg--done">
            <span class="update-card__meta">Completed</span>
            <p>Reseal done and checked on site. Completion photographs and the bill attached.</p>
          </div>
        </div>
        <p style="color:var(--night-muted);font-size:.88rem;margin-top:20px">Channels, inspection frequency and reporting schedule depend on the management plan you agree with us.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="areas">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Areas we serve</p>
      <h2>Local knowledge, right where your property is.</h2>
      <p class="lede">We currently manage property in these parts of Chennai. If your locality is not listed, ask — coverage is growing.</p>
    </div>
    <div class="areas-groups">
{area_groups}
    </div>
    <p class="area-note">Properties are managed in Chennai, Tamil Nadu, India. Owners may live anywhere in the world; we do not manage property outside India.</p>
    <p style="margin-top:20px"><a class="text-link" href="areas.html">Areas we serve</a></p>
  </div>
</section>

<section class="section section--stone" id="faq">
  <div class="container">
    <div class="two-col">
      <div>
        <p class="eyebrow">Questions</p>
        <h2>Questions owners ask first.</h2>
        <p class="lede">Short answers here; the full list is on the FAQ page.</p>
        <p><a class="text-link" href="faq.html">All frequently asked questions</a></p>
      </div>
      <div>
        {faq_block(HOME_FAQ)}
      </div>
    </div>
  </div>
</section>

<section class="section" id="enquire">
  <div class="container">
    <div class="two-col two-col--form">
      <div>
        {enquiry_form()}
      </div>
      <aside class="sticky-aside">
        <div class="aside-card">
          <h3>What happens after you send this</h3>
          <p>We read it, then contact you by your preferred method during business hours ({HOURS.replace("Open all days, ", "")}, all days). The first conversation is about your property and what you need; a written proposal follows if it makes sense to continue.</p>
          <p>We do not ask for ownership documents, ID or bank details at this stage.</p>
          <a class="btn btn--whatsapp" href="https://wa.me/{WHATSAPP_DIGITS}" data-wa="">{ICONS["whatsapp"]}Message us on WhatsApp</a>
        </div>
        <div class="contact-side" style="margin-top:28px">
          <div class="contact-block"><h3>WhatsApp</h3><p><a href="https://wa.me/{WHATSAPP_DIGITS}" data-wa="">{WHATSAPP_DISPLAY}</a></p></div>
          <div class="contact-block"><h3>Phone 2</h3><p><a href="tel:{PHONE2_TEL}">{PHONE2_DISPLAY}</a></p></div>
          <div class="contact-block"><h3>Email</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
          <div class="contact-block"><h3>Business hours</h3><p>{HOURS}</p></div>
        </div>
      </aside>
    </div>
  </div>
</section>
'''
    scripts = '<script src="assets/js/land-dots.js" defer></script>\n<script src="assets/js/globe.js" defer></script>\n<script src="assets/js/form.js"></script>\n'
    return page("index.html", "Property Management in Chennai for NRIs & Local Owners | Flourrish Asset Management",
                "Flourrish Asset Management looks after apartments, villas and commercial property in Chennai for owners anywhere in the world: inspections, tenants, maintenance and clear owner updates.",
                "index.html", body, extra_head=business_jsonld(), extra_scripts=scripts)
