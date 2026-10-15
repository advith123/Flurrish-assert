from common import *

# Per-service content. Keys: intro, problem, includes, process, receive, limits, faqs, img, subject
SERVICE_CONTENT = {
    "complete-property-management": dict(
        intro="One agreed plan that covers inspections, tenant and rent coordination, maintenance and owner reporting for a property in Chennai.",
        problem="Owning property from a distance usually means juggling a watchman, a relative, a plumber's number and an association WhatsApp group. Each one knows a piece of the picture. Nobody owns the whole of it, and small issues become expensive ones because no one was looking.",
        includes=[
            "A written management plan setting out scope, inspection frequency, approval limits and reporting schedule",
            "Scheduled property inspections with dated photographs and condition notes",
            "Tenant and rent coordination if the property is let, including renewals and move-outs",
            "Maintenance coordination: quotations, your approval, vendor supervision, completion check",
            "Liaison with the apartment association or society on routine matters",
            "Owner updates and periodic summary reports on the agreed channel",
            "A single point of contact for the property",
        ],
        process=[
            ("Onboarding visit", "We inspect the property, photograph its current condition, note meter readings, keys and access arrangements, and record existing issues."),
            ("Plan in writing", "You receive the proposed scope, fee, approval process and reporting frequency. Nothing starts until you confirm."),
            ("Routine care", "Inspections, tenant communication and maintenance follow the plan. Anything outside it is raised with you first."),
            ("Reporting", "Each inspection and each piece of work produces an update. A periodic summary ties the month or quarter together."),
        ],
        receive=["Onboarding condition report", "Inspection reports on the agreed schedule", "Quotations and approval requests before non-emergency work", "Completion photographs and final costs for each job", "Periodic summary of activity, costs and open items"],
        limits=["Legal representation, tax advice, property valuation and structural certification are not included; we can suggest independent professionals.", "Major renovation projects are quoted separately under Interior Improvements & Refurbishment.", "Vendor charges are paid by the owner and are separate from the management fee.", "Emergency response arrangements and spending limits are defined in the plan, not assumed."],
        faqs=[
            ("Do I need to be in Chennai for onboarding?", "No. Access can be arranged through a key handover with a person you nominate, or with the current tenant. The onboarding report shows you what we found."),
            ("Can I start with a smaller scope and expand later?", "Yes. Many owners begin with inspections and maintenance coordination and add tenant management later. The plan is amended in writing when the scope changes."),
            ("Who holds the keys?", "That is agreed at onboarding. Options include keys held by us under a signed record, a keybox at the property, or keys with a person you nominate."),
        ],
        img="service-complete", subject="Apartment building entrance and lobby, Chennai"),
    "tenant-management": dict(
        intro="Handling tenant enquiries, screening coordination, onboarding, day-to-day communication and move-outs, so the tenant has a responsive contact and you have a clear record.",
        problem="A good tenant is worth protecting, and most tenant problems start as unanswered messages. When the owner is in another time zone, a leaking geyser or a question about the society's parking rules can sit for days. That is how deposits get disputed and tenants leave.",
        includes=[
            "Responding to enquiries from prospective tenants and arranging viewings",
            "Coordinating background and reference checks through the channels you approve",
            "Move-in: inventory and condition report with photographs, meter readings, key handover",
            "Being the tenant's first point of contact for property-related issues during the tenancy",
            "Coordinating agreement renewals and rent-revision discussions on your instructions",
            "Move-out: inspection against the move-in report, settlement notes for the deposit, key return",
        ],
        process=[
            ("Listing and enquiries", "You decide the rent and the kind of tenant you want. We handle enquiries and viewings and send you a shortlist."),
            ("Checks and agreement", "Reference checks are coordinated as agreed. The rental agreement is prepared by the owner's chosen professional; we coordinate signing and registration logistics if required."),
            ("Tenancy", "Tenant requests come to us. Repairs follow the usual quotation-and-approval route. You receive a monthly note on anything that happened."),
            ("Move-out", "We inspect, compare with the move-in report, and send you a settlement recommendation with photographs."),
        ],
        receive=["Shortlist of enquiries with the details you asked for", "Move-in inventory and condition report", "Record of tenant requests and how each was closed", "Move-out inspection report with settlement recommendation"],
        limits=["We coordinate screening; the final decision on a tenant is yours.", "Drafting or vetting the rental agreement is a legal service and is arranged with a lawyer of your choice.", "Rent collection and payment follow-up are covered under Rental Management.", "Advertising or listing charges, if any, are agreed in advance and are separate from the management fee."],
        faqs=[
            ("Can you find a tenant for my flat?", "We handle enquiries and viewings for a listing and send you a shortlist. Advertising arrangements and any listing charges are agreed in advance."),
            ("What if the tenant stops responding or refuses to leave?", "We escalate to you immediately with the record of communication. Legal steps are taken by a lawyer you appoint; we support with documentation and access."),
            ("Do you handle the society or association formalities for the tenant?", "Yes, routine ones: NOC requests, move-in intimation, parking and ID formalities as the society requires."),
        ],
        img="service-tenant", subject="Keys handed over at an apartment door, India"),
    "rental-management": dict(
        intro="Rent follow-ups, payment-status communication, renewal reminders and the paperwork around a let property, kept in one record you can see.",
        problem="Rent that arrives late by a week every month is a small problem until it is three months. Most owners find out late because nobody was tracking it, and chasing from abroad is awkward.",
        includes=[
            "Tracking rent due dates and confirming receipt against the account you specify",
            "Follow-up with the tenant when a payment is late, within the steps you have approved",
            "Monthly payment-status note to you",
            "Reminders ahead of agreement expiry and rent-revision dates",
            "Coordinating renewal paperwork and any registration logistics",
            "Keeping copies of receipts, agreements and notices in an organised record",
        ],
        process=[
            ("Set-up", "We record the agreement terms, rent amount, due date, deposit and the account rent is paid into."),
            ("Each month", "Rent received is confirmed to you. If it is late, the agreed reminder sequence runs and you are told at each step."),
            ("Renewals", "Sixty to ninety days before expiry you receive a reminder with the options: renew, revise, or give notice."),
            ("Records", "Every receipt, agreement and notice is filed and available on request."),
        ],
        receive=["Monthly rent-status note", "Alerts on late payment with the follow-up taken", "Renewal reminders in good time", "Organised copies of all tenancy documents"],
        limits=["Rent is paid directly to the owner's account; we do not hold tenant funds unless a separate escrow arrangement is agreed in writing.", "Rent is not guaranteed. If a tenant defaults, we follow the agreed process and escalate to you.", "Tax filing, TDS advice and rental-income accounting are not included; we can share records with your accountant."],
        faqs=[
            ("Do you collect rent in cash?", "No. Rent goes to your bank account. We confirm receipt based on what you or the tenant share with us."),
            ("What do you do when rent is late?", "The reminder sequence is agreed with you in advance, for example a message on day 3, a call on day 7, and a formal notice coordinated with you on day 15."),
            ("Can you help with the rent revision at renewal?", "We share what similar properties in the area are asking and coordinate the discussion with the tenant. You decide the figure."),
        ],
        img="service-rental", subject="Rental apartment with balcony, residential complex in Chennai"),
    "property-inspection": dict(
        intro="Scheduled visits to your property with a dated report: photographs, condition notes, meter readings and recommended actions.",
        problem="A property nobody visits deteriorates quietly. Seepage spreads behind a cupboard, a balcony drain blocks before the monsoon, a tenant's 'small change' turns out to be a knocked-down wall. An inspection is the difference between finding out now and finding out at sale time.",
        includes=[
            "Visits at the frequency in your plan: monthly, quarterly or as agreed",
            "Checklist-based walk-through of every room, balcony, utility area and parking",
            "Dated photographs of each area and of any issue found",
            "Meter readings, water-tank and pump check, lock and door check",
            "Observations in plain language with a recommended action for each item",
            "Follow-up tracking until each item is closed",
        ],
        process=[
            ("Schedule", "Visit dates are set in advance. For tenanted properties, visits are arranged with the tenant with proper notice."),
            ("Inspect", "The same checklist is used every time, so reports are comparable visit to visit."),
            ("Report", "You receive the report within the agreed time after the visit, usually the same or next day."),
            ("Act", "Items needing work move into the maintenance process with a quotation for your approval."),
        ],
        receive=["Inspection report per visit with photographs", "Comparison notes against the previous visit", "Action list with status", "Copies kept so you can show the history to a buyer or tenant later"],
        limits=["Inspections are visual condition checks. Structural assessment, electrical certification and pest surveys are specialist services arranged separately.", "We do not enter a tenanted property without the notice required by the agreement."],
        faqs=[
            ("How often should my property be inspected?", "Vacant properties: monthly is typical. Tenanted: quarterly, with a check at every move-in and move-out. We will suggest a frequency after seeing the property."),
            ("What format is the report?", "A PDF or a structured WhatsApp/email update, depending on what you prefer. The sample on our home page shows the fields."),
            ("Can you check a property I am thinking of buying?", "We can do a condition visit and report what we see. It is not a valuation or a legal due-diligence check."),
        ],
        img="service-inspection", subject="Person photographing a room during a property inspection, India"),
    "maintenance-repairs": dict(
        intro="Plumbing, electrical work, painting, deep cleaning, carpentry, pest control and other approved jobs, coordinated with vendors and checked on completion.",
        problem="Finding a plumber in Chennai from Dubai or Dallas is not the hard part. Knowing whether the price is fair, whether the job was done properly, and whether anyone actually turned up, is.",
        includes=[
            "Diagnosis of the issue on site, with photographs",
            "Quotation from a vendor we have worked with, or from a vendor you nominate",
            "Approval request to you before non-emergency work starts",
            "Scheduling, access and supervision of the vendor",
            "Completion check with photographs and the final bill",
            "Follow-up if the fix does not hold",
        ],
        process=[
            ("Issue raised", "From an inspection, a tenant, or you."),
            ("Quote and approve", "You receive the description, the quotation and the expected cost. You say yes, no, or ask for another quote."),
            ("Work done", "We coordinate access and check the work before the vendor leaves."),
            ("Closed", "Completion photographs and the bill are sent to you. Payment to the vendor is made as agreed in your plan."),
        ],
        receive=["Issue report with photographs", "Written quotation before work", "Completion photographs and bill", "Record of all jobs with dates and costs"],
        limits=["Vendor charges are separate from the management fee and are paid by the owner.", "Emergency spending limits (for example a burst pipe at night) are agreed in the plan; without one, we contact you before spending.", "Vendors carry their own warranties; we coordinate follow-up but do not underwrite the work.", "Major renovation is handled under Interior Improvements & Refurbishment."],
        faqs=[
            ("Can I use my own plumber or electrician?", "Yes. Tell us who, and we coordinate access and check the work the same way."),
            ("What counts as an emergency?", "Anything that risks safety or rapid damage: water leaks into other flats, electrical faults, lock failures. The plan sets what we may do immediately and up to what amount."),
            ("Do you take a commission from vendors?", "No. Quotations are passed to you as received, and you can ask for a second one."),
        ],
        img="service-maintenance", subject="Electrician or plumber working inside an Indian apartment"),
    "vacant-property-care": dict(
        intro="Regular visits, ventilation, cleaning and condition updates for a property nobody lives in, so it stays ready for a tenant, a sale, or your return.",
        problem="Vacant flats attract three things: dust, damp and unwelcome attention. Seals dry out, drains block, bills go unpaid, and the society starts to wonder who to call. The cost of neglect shows up all at once.",
        includes=[
            "Scheduled visits with photographs and condition notes",
            "Opening windows for ventilation, running taps and flushing drains",
            "Light cleaning, or coordinating a cleaning service, as agreed",
            "Checking locks, water tank, pump, electrical mains and for signs of entry or pests",
            "Receiving society notices and reminding you of dues and utility bills",
            "Preparing the property for a viewing, handover or your visit",
        ],
        process=[
            ("Onboarding", "Condition photographs, meter readings, keys and a list of anything already needing attention."),
            ("Routine visits", "Usually monthly; more often during the monsoon if you prefer."),
            ("Updates", "A short report after each visit; issues go into the usual quotation-and-approval route."),
            ("Readiness", "When you need the property ready for a tenant or a visit, we coordinate cleaning and small repairs ahead of time."),
        ],
        receive=["Visit report with photographs each time", "Alerts on bills, notices and dues", "Readiness checklist before a viewing or handover"],
        limits=["Security guarding is not provided; we can coordinate with the society's security on your behalf.", "Utility bills and society dues are paid by the owner unless a payment arrangement is agreed in writing."],
        faqs=[
            ("Can you receive deliveries or courier documents at the property?", "By arrangement, for specific items, yes."),
            ("Will you keep the garden or plants alive?", "Yes, watering and basic garden upkeep can be part of the visit plan, or a gardener can be coordinated."),
            ("Can you prepare the flat for my family's holiday visit?", "Yes. Tell us the dates; we coordinate cleaning, linen if needed, and a check of appliances and water before you arrive."),
        ],
        img="service-vacant", subject="Empty, clean apartment interior with sunlight, India"),
    "nri-property-management": dict(
        intro="Property management built around an owner who lives abroad: remote communication, documented inspections and someone accountable in Chennai.",
        problem="Managing a flat in Chennai from the US, the Gulf, the UK, Singapore or Australia means time-zone gaps, relying on relatives who have their own lives, and never quite knowing what state the property is in. Every decision takes a week of messages.",
        includes=[
            "Everything in Complete Property Management, set up for remote decision-making",
            "Communication windows that fit your time zone where practical",
            "Reports designed to be read on a phone: photographs first, then the notes",
            "Approval requests with enough detail to decide without a call",
            "Coordination with a person you nominate in India for key access or signatures",
            "Support during your visits to Chennai: pre-arrival readiness and a walk-through together",
        ],
        process=[
            ("Remote onboarding", "A video call to understand the property and your expectations, then an onboarding visit with a full report."),
            ("Plan", "Scope, fee, approvals and reporting cadence in writing. Approval thresholds are tuned to how involved you want to be."),
            ("Ongoing", "Inspections, tenant matters and maintenance run as planned, with updates on WhatsApp and email."),
            ("When you visit", "We prepare the property and meet you there if you want to walk through it together."),
        ],
        receive=["Onboarding report", "Inspection reports and maintenance records on your phone", "A single contact who knows your property's history", "Organised records you can share with a buyer, tenant or accountant"],
        limits=["We do not give tax advice on NRI rental income, repatriation or FEMA matters; we can share records with your chartered accountant.", "Power of attorney, if ever needed for a specific transaction, is a legal arrangement between you and a lawyer, not something we hold by default."],
        faqs=[
            ("What time zones do you work with?", "Most owners are in the US, the Gulf, the UK, Singapore and Australia. Updates are sent so they are waiting when you wake up; calls are scheduled to overlap with our business hours (9 AM–7 PM IST)."),
            ("Do I need to give you power of attorney?", "No. Day-to-day management does not require it. If a transaction ever does, that is arranged through your lawyer."),
            ("Can my parents or a relative in Chennai still be involved?", "Yes. Many owners keep a relative as a nominated contact for keys or signatures while we handle the work and reporting."),
        ],
        img="service-nri", subject="Apartment towers along OMR, Chennai, skyline"),
    "interior-refurbishment": dict(
        intro="Coordination of approved painting, repairs, fittings and refurbishment with vendors and professionals, from scope to handover.",
        problem="A flat between tenants, or one you have just bought, often needs more than a repair: repainting, a kitchen fix, bathroom re-tiling, new fittings. Running that from abroad means paying for work you cannot see and hoping the schedule holds.",
        includes=[
            "Scoping visit with photographs and a written list of proposed work",
            "Quotations from vendors or contractors, itemised where possible",
            "Schedule and staged approvals for larger jobs",
            "Site visits during the work with progress photographs",
            "Snag list at completion and follow-up with the vendor until closed",
            "Coordination with an interior designer or architect you appoint, if the project needs one",
        ],
        process=[
            ("Scope", "What needs doing, what would be nice to do, and what each is likely to cost."),
            ("Approve", "You approve the scope and quotation. For larger projects, approval is staged by phase."),
            ("Execute", "Vendors are scheduled and supervised; you receive progress photographs."),
            ("Hand over", "Completion walk-through, snag list, and final photographs and bills."),
        ],
        receive=["Written scope with quotations", "Progress updates with photographs", "Snag list and completion report", "Bills and warranties from vendors"],
        limits=["We coordinate; the contract for the work is between the owner and the vendor.", "Structural changes, approvals from the society or authorities, and design services require the appropriate professionals.", "Projects are quoted separately from the routine management fee."],
        faqs=[
            ("Can you handle a full interior makeover?", "We coordinate it. For design-led projects we work alongside an interior designer you choose."),
            ("How do payments to contractors work?", "Payments go from you to the vendor at agreed milestones. We confirm that each milestone is complete before you release payment."),
        ],
        img="service-refurb", subject="Apartment being repainted, painter at work, India"),
}


def build_service_page(slug, title, line, icon):
    c = SERVICE_CONTENT[slug]
    includes = "".join(f"<li>{i}</li>" for i in c["includes"])
    steps = "".join(f'<div class="step"><h3>{h}</h3><p>{p}</p></div>' for h, p in c["process"])
    receive = "".join(f"<li>{i}</li>" for i in c["receive"])
    limits = "".join(f"<li>{i}</li>" for i in c["limits"])
    body = f'''
<section class="page-hero">
  <div class="container page-hero--split">
    <div>
      <p class="crumbs"><a href="index.html">Home</a> / <a href="services.html">Services</a> / {title}</p>
      <h1>{title}</h1>
      <p class="lede lede--lg">{c["intro"]}</p>
      <div class="btn-row" style="margin-top:28px">
        <a class="btn btn--primary" href="contact.html#enquiry">Discuss Your Property</a>
        <a class="btn btn--whatsapp" href="https://wa.me/{WHATSAPP_DIGITS}" data-wa="Hello Flourrish Asset Management, I would like to discuss {title} for my property in India.">{ICONS["whatsapp"]}WhatsApp Us</a>
      </div>
    </div>
    <div class="page-hero__img">{placeholder(c["img"], c["subject"], f"Service: {title}", eager=True)}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="two-col">
      <div class="prose">
        <h2 style="margin-top:0">The problem this solves</h2>
        <p>{c["problem"]}</p>
        <h2>What the service includes</h2>
        <ul class="checklist">{includes}</ul>
        <h2>How it works</h2>
        <div class="steps steps--vertical">{steps}</div>
        <h2>What you receive</h2>
        <ul class="checklist">{receive}</ul>
        <h2>Limits and exclusions</h2>
        <ul class="limits">{limits}</ul>
        <h2>Questions about this service</h2>
        {faq_block(c["faqs"])}
      </div>
      <aside class="sticky-aside">
        <div class="aside-card">
          <h3>Ask about {title.lower()}</h3>
          <p>Tell us where the property is and what is happening with it now. We will reply with questions and, if it fits, a written proposal.</p>
          <a class="btn btn--primary" href="contact.html#enquiry">Manage My Property</a>
          <a class="btn btn--whatsapp" href="https://wa.me/{WHATSAPP_DIGITS}" data-wa="Hello Flourrish Asset Management, I would like to discuss {title} for my property in India.">{ICONS["whatsapp"]}WhatsApp Us</a>
        </div>
        <div class="aside-card" style="margin-top:20px;background:#fff;border:1px solid var(--line)">
          <h3>Other services</h3>
          <ul style="list-style:none;padding:0;margin:0">
            {"".join(f'<li style="padding:8px 0;border-bottom:1px solid var(--line)"><a class="text-link" style="border:0;font-weight:500" href="service-{s}.html">{t}</a></li>' for s, t, _, _ in SERVICES if s != slug)}
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>
{cta_band()}
'''
    return page(f"service-{slug}.html", f"{title} in Chennai | {BRAND}", f"{line} {title} from Flourrish Asset Management for property owners in Chennai and abroad.",
                "services.html", body, extra_head=faq_jsonld(c["faqs"]), extra_scripts='<script src="assets/js/form.js"></script>\n')


def build_services_index():
    items = "\n".join(
        f'''<a class="service-card" href="service-{slug}.html">
  {placeholder(SERVICE_CONTENT[slug]["img"], SERVICE_CONTENT[slug]["subject"], f"Service: {title}", cls="service-card__img", sizes="(max-width: 640px) 100vw, (max-width: 1100px) 50vw, 380px")}
  <div class="service-card__body"><span class="service-item__icon">{ICONS[icon]}</span><h3>{title}</h3><p>{line}</p></div>
</a>''' for slug, title, line, icon in SERVICES)
    body = f'''
<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Services</p>
    <h1>Services for property owners in Chennai.</h1>
    <p class="lede lede--lg">Each service can stand alone or be combined into one management plan. The pages below say what is included, how the process runs, what you receive, and what sits outside the agreement.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="service-cards">
{items}
    </div>
    <div class="prose" style="margin-top:56px">
      <h2 style="margin-top:0">What is never included</h2>
      <p>Legal representation, tax advice, property valuation, structural certification and regulated financial services are not part of any Flourrish plan. Where a matter needs one of these, we say so and can suggest independent professionals. Vendor charges for repairs and improvements are always separate from the management fee and are paid by the owner.</p>
    </div>
  </div>
</section>
{cta_band("Not sure which service fits?", "Describe the property and what is bothering you about it. We will suggest a scope.")}
'''
    return page("services.html", f"Property Management Services in Chennai | {BRAND}", "Complete property management, tenant and rental management, inspections, maintenance coordination, vacant property care, NRI services and refurbishment coordination in Chennai.", "services.html", body)


def build_property_types():
    blocks = []
    for i, (slug, title, desc, link, img, subject) in enumerate(PROPERTY_TYPES):
        extra = {
            "apartments": "Apartment ownership comes with an association, shared services and neighbours above and below. We coordinate with the society on notices and dues, keep an eye on common-area issues that affect your flat, and handle the tenant or vacancy care inside it.",
            "villas": "A standalone house has no association to notice a problem. Gardens, compound walls, overhead tanks, terraces and gates all need someone to look. Visits are planned around the monsoon and your travel, and repairs are coordinated with vendors who know the area.",
            "rental": "A let property needs two things done well: the tenant looked after, and the money and paperwork tracked. Tenant Management and Rental Management cover both; most owners take them together.",
            "commercial": "Small offices and commercial units need maintenance coordination, access management and liaison with the building's management. We cover routine oversight; fit-out projects are quoted separately.",
            "vacant": "An unoccupied property needs regular ventilation, drain checks, bill reminders and a presence the society recognises. Monthly visits are typical, with readiness support when a tenant or a family visit is coming.",
        }[slug]
        cls = "split split--text-first" if i % 2 else "split"
        blocks.append(f'''<section class="section{' section--stone' if i % 2 else ''}" id="{slug}">
  <div class="container">
    <div class="{cls}">
      <div class="split__media">{placeholder(img, subject, "Property types page", cls="page-hero__img")}</div>
      <div>
        <h2>{title}</h2>
        <p class="lede">{desc}</p>
        <p>{extra}</p>
        <a class="btn btn--secondary" href="{link}">Explore this service</a>
      </div>
    </div>
  </div>
</section>''')
    body = f'''
<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Property types</p>
    <h1>Every property deserves the right care.</h1>
    <p class="lede lede--lg">A flat in a 300-unit tower and an independent house on a quiet ECR road need different attention. The plan is shaped around the property, not a fixed package.</p>
  </div>
</section>
{"".join(blocks)}
{cta_band()}
'''
    return page("property-types.html", f"Apartments, Villas, Rental, Commercial & Vacant Property Management | {BRAND}", "How Flourrish manages apartments and flats, villas and independent houses, rental properties, commercial units and vacant properties in Chennai.", "property-types.html", body)


def build_how_it_works():
    body = f'''
<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / How it works</p>
    <h1>Property management, made clear.</h1>
    <p class="lede lede--lg">Four steps from your first message to ongoing updates. The consultation is free of obligation; management starts only when the plan is agreed in writing.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="steps">
      <div class="step"><h3>Tell us about your property</h3><p>Use the enquiry form or WhatsApp. We need the property type, its location, whether it is occupied, and what you want handled. No documents at this stage.</p></div>
      <div class="step"><h3>Discuss your requirements</h3><p>A call or message exchange, in your time zone's reasonable hours, to understand the property, your expectations, how involved you want to be, and your budget.</p></div>
      <div class="step"><h3>Agree on the management plan</h3><p>You receive a written proposal: scope, fee, responsibilities, approval limits, reporting frequency and what is excluded. Ask questions, change things, then sign.</p></div>
      <div class="step"><h3>Stay informed</h3><p>After an onboarding inspection, routine care runs on the plan. Reports and approval requests reach you on the agreed channel.</p></div>
    </div>
  </div>
</section>
<section class="section section--stone">
  <div class="container">
    <div class="two-col">
      <div class="prose">
        <h2 style="margin-top:0">What the written plan covers</h2>
        <ul class="checklist">
          <li>Property details, access arrangements and who holds keys</li>
          <li>Services included and the inspection frequency</li>
          <li>The management fee, how it is calculated, billing schedule and GST</li>
          <li>Approval limits: what we may do without asking, and what always needs your yes</li>
          <li>Emergency procedure and any emergency spending limit</li>
          <li>Reporting: what you receive, how often, on which channel</li>
          <li>What is excluded, and how vendor charges are handled</li>
          <li>Notice period and how either side ends the arrangement</li>
        </ul>
        <h2>Enquiry is not onboarding</h2>
        <p>Sending an enquiry, or having a call, does not start the service and does not cost anything. Management begins on the date in the signed plan, after the onboarding inspection. Until then no visits are made and no fees apply.</p>
      </div>
      <aside>
        <div class="aside-card">
          <h3>Typical timeline</h3>
          <p>First reply within one business day. Proposal within a few days of the call, depending on whether a site visit is needed first. Onboarding inspection scheduled once the plan is signed. These are typical, not guaranteed.</p>
          <a class="btn btn--primary" href="contact.html#enquiry">Start with step one</a>
        </div>
      </aside>
    </div>
  </div>
</section>
{cta_band()}
'''
    return page("how-it-works.html", f"How Property Management Works | {BRAND}", "Four steps: tell us about the property, discuss requirements, agree a written management plan, then receive inspections and updates. Nothing starts until the plan is signed.", "how-it-works.html", body)
