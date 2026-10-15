from common import *

ALL_FAQ = [
    ("What does property management include?", "It depends on the plan, but the core is scheduled inspections with photographic reports, maintenance coordination with your approval before work starts, tenant and rent coordination if the property is let, liaison with the society or association, and regular updates to you. Each service page lists what is included and what is not."),
    ("Can Flourrish manage my property if I live abroad?", "Yes. Most owners we work with are outside Chennai, many outside India. Reports, quotations and approvals move over WhatsApp and email; visits and vendor supervision happen in Chennai. Communication windows are planned around your time zone where practical."),
    ("Which Indian cities and localities are covered?", "Chennai only, at present. The current localities are listed on the Areas We Serve page. We do not manage property outside India, and overseas locations on this site refer to where owners live, not where properties are managed."),
    ("Do you manage apartments, villas and independent houses?", "Yes: apartments and flats, villas and independent houses, let properties, small commercial units and vacant properties. Plots and land can be discussed case by case."),
    ("Can you manage vacant properties?", "Yes. Vacant Property Care covers scheduled visits, ventilation, cleaning, lock and utility checks, bill and society-dues reminders, and readiness before a tenant or a family visit."),
    ("How are property inspections documented?", "Each visit produces a dated report with photographs of each area, meter readings, observations and a recommended action for every item found. Reports follow the same checklist each time so you can compare visits."),
    ("How are maintenance costs approved?", "For non-emergency work you receive the issue, the vendor quotation and the expected cost before anything starts, and work proceeds only on your approval. Emergency handling and any spending limit are written into your plan."),
    ("Do you find and coordinate tenants?", "We handle enquiries and viewings for a listing, coordinate reference checks through channels you approve, and manage move-in, the tenancy and move-out. The decision on a tenant is yours. The rental agreement is prepared by a lawyer of your choice."),
    ("How are rent follow-ups handled?", "Rent is paid to your account. We confirm receipt, run an agreed reminder sequence if it is late, and send a monthly status note. Rent is not guaranteed; defaults are escalated to you with the record of communication."),
    ("How often will I receive updates?", "After every inspection and every completed job, plus a periodic summary. The schedule and channel are set in your plan. Urgent matters are raised as they happen."),
    ("How are management fees calculated?", "Fees depend on the property type, location, occupancy, inspection frequency, maintenance coordination needed and reporting requirements. You receive a written proposal with the fee, billing schedule and GST before deciding. See the Management Proposal page."),
    ("What happens during an urgent repair?", "The plan defines what counts as an emergency and what we may do immediately, up to what amount. Without an agreed limit, we contact you before spending. Either way you receive photographs and the bill afterwards."),
    ("How do I get started?", "Send the enquiry form or a WhatsApp message with the property type, location, occupancy and what you need. We reply with questions, arrange a call, and send a written proposal if it fits."),
    ("Which services are outside the management agreement?", "Legal representation, tax advice, property valuation, structural certification and regulated financial services. Vendor charges for repairs and improvements are separate from the management fee. Anything else outside the plan is quoted separately before it is done."),
    ("Do I need to give you power of attorney?", "No. Routine management does not need it. If a specific transaction ever does, that is arranged between you and your lawyer."),
    ("Who holds the keys to my property?", "Agreed at onboarding and recorded in writing: keys held by us, a keybox at the property, or a person you nominate."),
]


def build_areas():
    groups = "\n".join(
        f'''<div class="area-group"><h3>{g["zone"]}</h3><ul>{"".join(f"<li>{a}</li>" for a in g["areas"])}</ul></div>''' for g in AREAS)
    body = f'''
<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Areas we serve</p>
    <h1>Local knowledge, right where your property is.</h1>
    <p class="lede lede--lg">Flourrish manages property in Chennai, Tamil Nadu. These are the localities currently covered. Owners can live anywhere; the property has to be here.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="areas-groups">
{groups}
    </div>
    <div class="prose" style="margin-top:56px">
      <h2 style="margin-top:0">Property somewhere else in Chennai?</h2>
      <p>Coverage grows as we take on properties. If your locality is not listed, send the address area in your enquiry and we will tell you honestly whether we can service it well. We would rather say no than manage a property badly from too far away.</p>
      <h2>Other Indian cities</h2>
      <p>Not yet. We will add a city only after operations there are in place. Until then, no coverage is claimed outside Chennai.</p>
      <h2>Owners outside India</h2>
      <p>Most owners we work with live in the United States, the Gulf, the United Kingdom, Singapore, Australia and Canada. Those are owner locations, not service locations: all properties under management are in Chennai.</p>
    </div>
  </div>
</section>
{cta_band("Is your property in one of these areas?", "Tell us the locality and property type. We will confirm coverage in our first reply.")}
'''
    return page("areas.html", f"Areas We Serve in Chennai: OMR, ECR, Adyar, Anna Nagar & more | {BRAND}", "Flourrish Asset Management currently manages property in OMR, ECR, Adyar, Besant Nagar, Anna Nagar, Nungambakkam, Tambaram, Tambaram Radial Road, Velachery and Injambakkam, Chennai.", "areas.html", body)


def build_about():
    body = f'''
<section class="page-hero">
  <div class="container page-hero--split">
    <div>
      <p class="crumbs"><a href="index.html">Home</a> / About us</p>
      <h1>Where assets flourish.</h1>
      <p class="lede lede--lg">Flourrish Asset Management exists for one reason: a property in Chennai should be looked after properly whether its owner lives in Adyar or Atlanta.</p>
    </div>
    <div class="page-hero__img">{placeholder("about-hero", "Residential street with apartment buildings and trees, Chennai", "About page", eager=True)}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="two-col">
      <div class="prose">
        <h2 style="margin-top:0">Why we do this</h2>
        <p>Property is often the single largest asset an Indian family owns, and the one that gets the least attention once nobody is living in it. Ask any NRI what happens to their flat and you hear the same story: a relative with the keys, a plumber who may or may not turn up, a society that sends notices to an address no one checks, and a slow erosion of value that nobody notices until it is time to sell or let.</p>
        <p>We started Flourrish to be the person who is accountable for that property. Not a watchman with the keys, not a well-meaning cousin, but a service with a written scope, a schedule, photographs, and someone who answers when you message.</p>
        <h2>How we work</h2>
        <p>Three habits run through everything on this site. Show, don't tell: inspections come with photographs, maintenance comes with quotations, completion comes with evidence. Ask before spending: non-emergency work waits for your approval. Say what is excluded: every service page lists its limits, because an owner who knows what is not covered is an owner who is not surprised later.</p>
        <h2>Where we work</h2>
        <p>Chennai, in the localities listed on the <a href="areas.html">Areas We Serve</a> page. We do not claim coverage we cannot deliver, and we do not manage property outside India.</p>
        <h2>Company formation</h2>
        <p>Separately from property management, Flourrish also assists clients with company formation in India. It is a distinct service with its own process; ask us directly if it is relevant to you.</p>
      </div>
      <aside>
        <div class="aside-card">
          <h3>The people behind Flourrish</h3>
          <p>Flourrish is founded and run by Farrah and Shakeel. Biographies and photographs will be added once approved.</p>
          <div class="people" style="grid-template-columns:1fr;max-width:none;margin-top:16px">
            <div class="person" style="background:#fff;border:1px solid var(--line)"><strong>Farrah</strong><span>Founder</span></div>
            <div class="person" style="background:#fff;border:1px solid var(--line)"><strong>Shakeel</strong><span>Co-Founder</span></div>
          </div>
        </div>
      </aside>
    </div>
  </div>
</section>
<section class="section section--stone">
  <div class="container">
    <div class="section-head">
      <h2>Our approach to property care.</h2>
      <p class="lede">Testimonials will appear here only when owners have given permission to publish them. Until then, the process is the evidence.</p>
    </div>
    <div class="values">
      <div class="value"><h3>Documented inspections</h3><p>Dated photographs and a consistent checklist, so each visit can be compared with the last.</p></div>
      <div class="value"><h3>Approval before spending</h3><p>Quotation first, work second. Emergency limits are agreed in writing, never assumed.</p></div>
      <div class="value"><h3>Written scope</h3><p>Included, excluded, fee, schedule and notice period, all on paper before the first visit.</p></div>
      <div class="value"><h3>One point of contact</h3><p>Someone who knows your property's history and is answerable for every open item.</p></div>
      <div class="value"><h3>Plain reporting</h3><p>Reports written to be read on a phone, photographs first, with a clear recommended action.</p></div>
      <div class="value"><h3>Honest coverage</h3><p>We take on properties we can reach and service well. If we cannot, we say so.</p></div>
    </div>
  </div>
</section>
{cta_band()}
'''
    return page("about.html", f"About {BRAND} | Property Management in Chennai", "Flourrish Asset Management, founded by Farrah and Shakeel, manages property in Chennai for owners in India and abroad with documented inspections, approved maintenance and clear reporting.", "about.html", body)


def build_faq():
    body = f'''
<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / FAQs</p>
    <h1>Frequently asked questions.</h1>
    <p class="lede lede--lg">Answers reflect how Flourrish works today. Where something depends on your management plan, the answer says so.</p>
  </div>
</section>
<section class="section">
  <div class="container--narrow">
    {faq_block(ALL_FAQ, searchable=True)}
    <p style="margin-top:40px;color:var(--ink-2)">Not answered here? <a href="https://wa.me/{WHATSAPP_DIGITS}" data-wa="">Ask on WhatsApp</a> or use the <a href="contact.html#enquiry">contact form</a>.</p>
  </div>
</section>
{cta_band()}
'''
    return page("faq.html", f"Property Management FAQs | {BRAND}", "Answers on what property management includes, managing from abroad, inspections, maintenance approvals, tenants, rent follow-ups, fees and getting started with Flourrish in Chennai.", "faq.html", body, extra_head=faq_jsonld(ALL_FAQ))


def build_contact():
    body = f'''
<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Contact</p>
    <h1>Tell us about your property.</h1>
    <p class="lede lede--lg">Use the form or message us on WhatsApp. Either way we reply during business hours with questions about the property, not a pitch.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="two-col two-col--form">
      <div>{enquiry_form(heading="Enquiry form")}</div>
      <aside class="sticky-aside">
        <div class="contact-side">
          <div class="contact-block"><h3>WhatsApp</h3><p><a href="https://wa.me/{WHATSAPP_DIGITS}" data-wa="">{WHATSAPP_DISPLAY}</a></p><p class="hint" style="color:var(--ink-3);font-size:.85rem">Fastest for owners abroad. Messages received outside business hours are answered the next morning IST.</p></div>
          <div class="contact-block"><h3>Phone 2</h3><p><a href="tel:{PHONE2_TEL}">{PHONE2_DISPLAY}</a></p></div>
          <div class="contact-block"><h3>Email</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
          <div class="contact-block"><h3>Business hours</h3><p>{HOURS}</p></div>
          <div class="contact-block"><h3>Where we manage property</h3><p>Chennai, Tamil Nadu, India. <a href="areas.html">See the localities</a>.</p></div>
        </div>
        <div class="aside-card" style="margin-top:28px">
          <h3>What we will ask you</h3>
          <p>Where the property is, what type it is, who lives there now, what you would like handled, and how involved you want to be. We do not need ownership documents, ID or bank details to start the conversation.</p>
        </div>
      </aside>
    </div>
  </div>
</section>
'''
    return page("contact.html", f"Contact {BRAND} | WhatsApp +91 99440 70397", "Contact Flourrish Asset Management about managing your property in Chennai. WhatsApp +91 99440 70397, email admin.flourrishassets@gmail.com, open all days 9 AM–7 PM IST.", "contact.html", body, extra_scripts='<script src="assets/js/form.js"></script>\n')


def build_proposal():
    body = f'''
<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Management proposal</p>
    <h1>How a management proposal is put together.</h1>
    <p class="lede lede--lg">We do not publish package prices, because two flats in the same building can need very different attention. What we do publish is exactly what the fee depends on and what the proposal will spell out.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head"><h2>What shapes the fee</h2></div>
    <div class="factors">
      <div class="factor"><h3>Property type</h3><p>An apartment with an association behind it needs different work from a standalone villa with a garden, tank and compound wall.</p></div>
      <div class="factor"><h3>Location</h3><p>Travel time to the property affects how often it can be visited economically. See the <a href="areas.html">areas we cover</a>.</p></div>
      <div class="factor"><h3>Occupancy and tenant status</h3><p>Vacant, tenant-occupied and owner-occupied properties call for different visit patterns and different coordination.</p></div>
      <div class="factor"><h3>Inspection frequency</h3><p>Monthly, quarterly, or around specific events such as the monsoon and tenant changes.</p></div>
      <div class="factor"><h3>Maintenance coordination</h3><p>A newly built flat and a fifteen-year-old house generate very different volumes of repair work to coordinate.</p></div>
      <div class="factor"><h3>Reporting requirements</h3><p>Some owners want a photo update after each visit; others want a quarterly summary for their accountant as well.</p></div>
      <div class="factor"><h3>Additional services</h3><p>Tenant sourcing, readiness for a family visit, refurbishment coordination and similar work are scoped and quoted separately.</p></div>
      <div class="factor"><h3>Number of properties</h3><p>Several properties in the same area can be covered more efficiently, and the proposal reflects that.</p></div>
    </div>
  </div>
</section>
<section class="section section--stone">
  <div class="container">
    <div class="two-col">
      <div class="prose">
        <h2 style="margin-top:0">What the proposal states</h2>
        <ul class="checklist">
          <li>Scope: every included service, with the inspection frequency</li>
          <li>The management fee and how it is calculated</li>
          <li>Billing schedule and GST</li>
          <li>Any minimum fee, if applicable</li>
          <li>Approval limits and the emergency procedure</li>
          <li>What is excluded, and that vendor charges are separate and paid by the owner</li>
          <li>Reporting: what, how often, on which channel</li>
          <li>Notice period for ending the arrangement</li>
        </ul>
        <h2>What you will not find in it</h2>
        <p>Guarantees of rent, promises of zero risk, or "no hidden charges" slogans. Vendor costs are by nature not known in advance; the proposal explains how they are quoted and approved instead of pretending they do not exist.</p>
      </div>
      <aside>
        <div class="aside-card">
          <h3>Request a tailored proposal</h3>
          <p>Tell us about the property and we will send a written proposal after a short call. No obligation, no fee for the consultation.</p>
          <a class="btn btn--primary" href="contact.html#enquiry">Request a proposal</a>
          <a class="btn btn--whatsapp" href="https://wa.me/{WHATSAPP_DIGITS}" data-wa="Hello Flourrish Asset Management, I would like a management proposal for my property in India.">{ICONS["whatsapp"]}WhatsApp Us</a>
        </div>
      </aside>
    </div>
  </div>
</section>
'''
    return page("proposal.html", f"Management Fees & Proposals | {BRAND}", "What determines a property management fee at Flourrish Asset Management in Chennai, what a written proposal includes, and how to request one.", "proposal.html", body)


def build_privacy():
    body = f'''
<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Privacy policy</p>
    <h1>Privacy policy.</h1>
    <p class="lede">How {BRAND} handles the information you share with us through this website and during our work together.</p>
  </div>
</section>
<section class="section">
  <div class="container--narrow prose">
    <p class="callout"><strong>Draft for review.</strong> This policy has been prepared as a working draft and should be reviewed by a qualified professional before publication. Remove this notice when approved.</p>
    <h2 style="margin-top:0">Who we are</h2>
    <p>{BRAND} ("Flourrish", "we") provides property management services in Chennai, Tamil Nadu, India. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <h2>What we collect</h2>
    <p>Through the enquiry form or WhatsApp: your name, email address, phone or WhatsApp number, country of residence, the property's location and type, its occupancy status, the service you are interested in, and anything else you choose to tell us. We do not request ownership documents, identity documents or bank details through this website.</p>
    <p>Once you become a client, we collect what is needed to manage the property: access and key arrangements, tenant details where relevant, inspection photographs, vendor quotations and bills.</p>
    <h2>How we use it</h2>
    <ul>
      <li>To respond to your enquiry and prepare a management proposal</li>
      <li>To deliver the services in your management plan</li>
      <li>To send inspection reports, approval requests and updates</li>
      <li>To keep records of work done and costs incurred</li>
    </ul>
    <p>We do not sell your information. We do not use it for marketing unrelated to our services without asking you first.</p>
    <h2>Who we share it with</h2>
    <p>Vendors and professionals engaged for your property receive only what they need to do the job, for example access timing and the issue description. Form submissions may be processed by a third-party form service; WhatsApp messages are handled by WhatsApp under its own terms. We share information with authorities only where the law requires.</p>
    <h2>How long we keep it</h2>
    <p>Enquiry details are kept while we are in conversation and for a reasonable period afterwards. Client records are kept for the duration of the management agreement and as required for accounting and legal purposes.</p>
    <h2>Your choices</h2>
    <p>You can ask us what we hold about you, ask for corrections, or ask us to delete enquiry information we no longer need. Write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <h2>Cookies and analytics</h2>
    <p>This website does not set tracking cookies. If analytics are added later, this section will be updated and consent requested where required.</p>
    <h2>Changes</h2>
    <p>If this policy changes, the updated version will be published on this page with the date of revision.</p>
  </div>
</section>
'''
    return page("privacy.html", f"Privacy Policy | {BRAND}", "How Flourrish Asset Management collects, uses and protects information shared through its website and during property management services.", "privacy.html", body)


def build_terms():
    body = f'''
<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Terms of service</p>
    <h1>Terms of service.</h1>
    <p class="lede">The terms on which this website is provided. Property management itself is governed by the written management agreement signed with each owner.</p>
  </div>
</section>
<section class="section">
  <div class="container--narrow prose">
    <p class="callout"><strong>Draft for review.</strong> These terms have been prepared as a working draft and should be reviewed by a qualified professional before publication. Remove this notice when approved.</p>
    <h2 style="margin-top:0">Use of this website</h2>
    <p>This website describes the services of {BRAND}. Information on it is general and is not legal, tax, financial or valuation advice. Service availability, scope and fees are confirmed only in a written management proposal and agreement.</p>
    <h2>Enquiries</h2>
    <p>Submitting an enquiry does not create a management agreement and does not oblige either party. Management services start only on the date set out in a signed agreement.</p>
    <h2>Service area</h2>
    <p>Property management is provided in Chennai, India, in the localities listed on the Areas We Serve page. References to other countries describe where owners live, not where services are provided.</p>
    <h2>Accuracy</h2>
    <p>We try to keep this website accurate and current. Photographs are illustrative and do not depict properties under Flourrish management unless stated. Sample reports are demonstrations of format and do not describe real properties or clients.</p>
    <h2>Third-party services</h2>
    <p>Links to WhatsApp, email and other services are provided for convenience and are subject to those services' own terms.</p>
    <h2>Intellectual property</h2>
    <p>Text, design and the Flourrish name and logo on this website belong to {BRAND} or its licensors and may not be reproduced without permission.</p>
    <h2>Governing law</h2>
    <p>These terms are governed by the laws of India. Disputes are subject to the jurisdiction of the courts in Chennai, Tamil Nadu.</p>
    <h2>Contact</h2>
    <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </div>
</section>
'''
    return page("terms.html", f"Terms of Service | {BRAND}", "Terms governing use of the Flourrish Asset Management website. Property management services are governed by a written agreement with each owner.", "terms.html", body)


def build_404():
    body = f'''
<section class="section">
  <div class="container--narrow" style="text-align:center;padding-block:40px">
    <h1>This page doesn't exist.</h1>
    <p class="lede">The link may be out of date. The pages below cover everything on the site.</p>
    <div class="btn-row" style="justify-content:center;margin-top:28px">
      <a class="btn btn--primary" href="index.html">Go to the home page</a>
      <a class="btn btn--secondary" href="services.html">See services</a>
      <a class="btn btn--secondary" href="contact.html">Contact</a>
    </div>
  </div>
</section>
'''
    return page("404.html", f"Page not found | {BRAND}", "The page you requested could not be found.", "", body)
