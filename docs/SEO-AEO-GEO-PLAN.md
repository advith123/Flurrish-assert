# Search plan for flourrishassets.com

This covers three kinds of search, because owners now find a property manager in three different ways:

- **SEO** — ranking in normal Google and Bing results, and on Google Maps.
- **AEO** (answer engine optimisation) — being the answer Google pulls out directly: the snippet at the top, "People also ask", AI Overviews, and voice answers.
- **GEO** (generative engine optimisation) — being named and linked when someone asks ChatGPT, Perplexity, Gemini, Copilot or Claude for a property manager in Chennai.

The website already has the groundwork for all three (section 1). Most of what's left is off the website: Google Business Profile, reviews, and being mentioned in the places NRIs already talk (sections 5 to 7).

---

## 1. What's already built into the site

| What | Where | Why it matters |
|---|---|---|
| Canonical URLs on `https://flourrishassets.com` | `<head>` of every page | Tells search engines which address is the real one, so they don't split ranking between duplicates. |
| A written title and description for every page, under 62 and 158 characters | `<head>` of every page | Titles are the biggest single on-page ranking signal. Staying under the limits keeps Google from cutting them off. |
| Structured data (schema.org JSON-LD) on every page | `<script type="application/ld+json">` in each page | Describes the business, services, areas, FAQs, articles and glossary in a format machines read directly. Used by Google, Bing and AI assistants. |
| `sitemap.xml` | site root | Lists all 22 public pages with a last-updated date. Submit it to Google and Bing. |
| `robots.txt` | site root | Lets every search engine in and explicitly welcomes AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended and others). |
| `llms.txt` and `llms-full.txt` | site root | A plain-text summary of the business for AI assistants, with facts and links. It's a new convention; it costs nothing and some tools already read it. |
| "In short" answer boxes | Top of Services, NRI, Pricing, About, Contact, every area and country page, and the glossary | A 40–70 word direct answer. This is the text most likely to be lifted into a featured snippet or an AI answer. |
| 4 area pages and an areas hub | `areas/` | Targets people searching by place: "property management OMR", "ECR villa maintenance" and so on. Each page is written for that area, not copied. |
| 4 country pages for NRIs | `nri/` | Targets people by where they live: USA and Canada, UAE and the Gulf, UK and Europe, Singapore and Australia. Includes real time-difference tables. |
| Chennai property glossary | `chennai-property-glossary.html` | Short definitions of Patta, EC, POA, NRO, TDS and more. AI assistants quote clear definitions often. |
| 27 FAQs with search and topic filters | `faq.html`, plus FAQ blocks on the NRI, pricing, area and country pages | Covers the questions people type and speak. |
| "Flourrish in nine facts" table | `about.html` | One place with the facts an AI assistant needs to describe the company correctly. |
| Tables for fees and time differences | `pricing.html`, country pages | Tables are a favourite format for featured snippets. |
| Internal links between related pages | Area tags, "Owners in…" links, the footer's "Areas & NRI owners" column | Helps search engines understand how the site fits together. |
| Honest publish dates | Blog articles | Dated to launch rather than the mockup's 2024 dates. Freshness matters to AI answers. |

### Structured data on each page type

| Page | Types used |
|---|---|
| Every page | `RealEstateAgent` (the business), `WebSite`, `WebPage`, `BreadcrumbList` |
| Home, Services, Pricing, NRI | `Service` with offer details; Services also lists all 15 services in an `OfferCatalog` |
| FAQ | `FAQPage` with all 27 questions |
| Area pages | `Service` with `areaServed` set to the neighbourhoods, plus `FAQPage` |
| Country pages | `Service` with an `Audience` for NRIs in that region, plus `FAQPage` |
| Blog articles | `BlogPosting` |
| Glossary | `DefinedTermSet` with each term as a `DefinedTerm` |
| Areas hub | `CollectionPage` with an `ItemList` of the area pages |

A note on FAQ markup: since 2023, Google shows FAQ dropdowns in its results almost only for government and health sites. So don't expect them in Google. The markup is still worth having because Bing and AI assistants use it to understand the page.

---

## 2. Who we're trying to reach

Ten groups, in rough order of value. The "where they look" column matters as much as the keywords.

| # | Who | What's on their mind | What they type or ask | Page that answers | Where they look |
|---|---|---|---|---|---|
| 1 | NRIs in the USA and Canada, often in tech, with a flat on OMR or in South Chennai | Is my tenant paying? Who checks the flat? The time difference makes everything slow. | "NRI property management Chennai", "manage flat in Chennai from USA"; ChatGPT: "how do I rent out my Chennai apartment while living in the US" | `nri/usa-canada.html`, `nri-property-management.html` | Google, ChatGPT, LinkedIn, Tamil associations in North America, alumni WhatsApp groups, Reddit (r/nri, r/chennai) |
| 2 | NRIs in the UAE and Gulf | Visits are frequent but short. Many plan to come back and want the home kept ready. | "property maintenance Chennai for NRI in Dubai", "who can look after my flat in Chennai" | `nri/uae-gulf.html` | Google, Facebook and WhatsApp groups of Tamil expats in the Gulf, community associations |
| 3 | NRIs in the UK and Europe | Tax records for two tax years; easy call times | "rent out Chennai flat UK resident", "NRI rental income tax UK India" | `nri/uk-europe.html`, NRI tax article | Google, LinkedIn, UK Tamil associations |
| 4 | NRIs in Singapore, Malaysia and Australia | Same-day decisions; tenant trust | "Chennai property manager for NRI Singapore" | `nri/singapore-australia.html` | Google, ChatGPT, community groups |
| 5 | Adult children whose parents used to manage the property | Parents are older or unwell; the house needs someone new | "parents can't manage rental house Chennai", "someone to manage my parents' flat" | NRI page, "Does one of these sound familiar?" section | Google, family WhatsApp groups, word of mouth |
| 6 | People who have inherited a property | Empty house, paperwork unclear, family undecided | "inherited house in Chennai what to do", "patta transfer after death" | `areas/south-chennai.html`, glossary | Google, ChatGPT, Quora |
| 7 | Investors with a new flat in the suburbs | Flat handed over, earning nothing | "first tenant for new flat Chengalpattu", "rent out new apartment Tambaram" | `areas/tambaram-gst-road.html` | Google, builder customer WhatsApp groups, 99acres/Magicbricks |
| 8 | Busy local owners in Chennai with a second property | No time for tenants and repairs | "property management company Chennai", "rental management OMR" | Home, `areas/omr.html`, local owners section | Google, Google Maps, apartment association groups |
| 9 | ECR villa and beach house owners | Empty house, salt air, security, cyclones | "villa maintenance ECR", "beach house caretaker Chennai" | `areas/ecr.html` | Google, Google Maps, word of mouth |
| 10 | Tenants | A well-kept home with a responsive landlord | "flats for rent OMR", "house for rent Adyar" | Tenants section | Property portals, Google |

The full keyword and question list is in `docs/keyword-map.csv`. No search volumes are listed there on purpose: guessed numbers do more harm than good. Check real volumes in Google Keyword Planner before choosing new articles, and look at Search Console after the first two months to see which queries are actually bringing people in.

---

## 3. What each page is aimed at

| Page | Main search | Supporting searches |
|---|---|---|
| Home | property management company in Chennai | property management Chennai, rental management Chennai |
| NRI property management | NRI property management Chennai | property management for NRI in Chennai, NRI rental property management India |
| Services | property management services Chennai | tenant verification Chennai, rent collection service Chennai, vacant property management Chennai |
| Pricing | property management fees Chennai | property management charges Chennai, how much does a property manager charge in India |
| FAQ | property management questions | 27 individual questions, each written as someone would ask it |
| OMR | property management OMR Chennai | Sholinganallur, Perungudi, Thoraipakkam property management; gated community rental management |
| ECR | villa management ECR Chennai | beach house maintenance ECR, vacant house care ECR |
| South Chennai | property management Adyar / Velachery / Besant Nagar | inherited house management Chennai, old house maintenance Chennai |
| Tambaram and GST Road | property management Tambaram | Pallavaram, Medavakkam, Chengalpattu; first tenant for new flat; plot maintenance |
| Country pages | manage Chennai property from USA / UAE / UK / Singapore | time difference Chennai; rent from India when living abroad |
| Glossary | what is Patta / EC / NRO account | encumbrance certificate meaning, POA for NRI, TDS on rent to NRI |

---

## 4. AEO: being the answer

Search engines and AI tools pull out short, direct answers. The site is written for that. Keep writing this way for every new page and article.

**The rules**

1. **Answer first.** The first two or three sentences under a heading should answer the question fully, in 40–60 words. Explain afterwards.
2. **Headings as questions.** Use the words people type: "How much does a property manager charge in Chennai?" rather than "Our pricing philosophy".
3. **One question, one answer.** Don't bundle three questions into one FAQ.
4. **Use lists and tables** for steps, checklists and comparisons. Google lifts them as they are.
5. **Say the same number everywhere.** 12% of annual rent must read identically on every page, in the Google Business Profile and in every directory. Mixed numbers make AI tools distrust all of them.
6. **Name things in full once.** "OMR (Old Mahabalipuram Road, officially Rajiv Gandhi Salai)" the first time, then OMR.
7. **Write for voice.** Voice questions are longer and conversational: "Who can look after my flat in Chennai while I'm in Dubai?" Put phrasing like this in FAQs.

**Finding new questions**

- Type your main searches into Google and note every "People also ask" question. Click one and more appear.
- Ask ChatGPT and Perplexity "What questions do NRIs ask before hiring a property manager in Chennai?" and compare the answer with your FAQ.
- Every question an owner asks on WhatsApp is a candidate FAQ. Keep a running list.
- After two months, Search Console will show the exact questions people typed to find you.

---

## 5. GEO: being named by AI assistants

AI assistants decide who to mention from three things: what their search index returns, what the rest of the web says about you, and how clear and consistent your facts are. The website covers the third. The first two need work off the site.

**Keep your identity identical everywhere.** Use exactly the same name, description, phone number and website on the site, Google Business Profile, LinkedIn, Facebook, Instagram, Justdial, Sulekha and anywhere else. Copy the description below word for word:

> Flourrish Asset Management is a Chennai-based property management company for NRI and local property owners. Founded by Shakeel and Farrah, it looks after apartments, villas, independent houses, offices and vacant properties across OMR, ECR and South Chennai, for a fee of 12% of the annual rental value.

**Get into Bing, not just Google.** Microsoft Copilot runs on Bing, and ChatGPT's web search has drawn on Bing results too. Set up Bing Webmaster Tools (it can import everything from Google Search Console in one click) and submit the sitemap there as well.

**Be mentioned by other people.** AI tools lean heavily on third-party sources. In order of usefulness:
1. Google reviews from real owners (section 6).
2. Helpful answers on Reddit (r/chennai, r/nri) and Quora, always saying who you are.
3. YouTube videos. AI tools and Google both cite them often. A 3-minute walkthrough of a real monthly report (with the owner's permission, and no tenant faces) is the best single video to make.
4. Listings on Justdial, Sulekha, Bing Places and Apple Business Connect.
5. Mentions in NRI community newsletters, Tamil association websites abroad and Chennai city news coverage.

**Link your profiles in the schema.** Once the social profiles and Google Business Profile exist, add them to every page's structured data. In every `.html` file, find:

```
"knowsAbout":
```
and replace it with (using your real links):
```
"sameAs": ["https://www.linkedin.com/company/…", "https://www.instagram.com/…", "https://www.facebook.com/…", "https://www.youtube.com/@…"], "knowsAbout":
```
A find-and-replace across all files does this in one go.

**Test it every month.** Ask these in ChatGPT, Perplexity, Gemini, Copilot and Google's AI Mode, in a fresh chat each time. Log in a spreadsheet: was Flourrish mentioned, which page was linked, and was anything wrong?

1. Who can manage my apartment in Chennai while I live in the US?
2. Best property management company in Chennai for NRIs
3. Property management on OMR Chennai
4. How much do property managers charge in Chennai?
5. How do I rent out my flat in Chennai from Dubai?
6. Someone to look after my villa on ECR while it's empty
7. My parents can't manage our rental house in Adyar anymore. What are my options?
8. How do NRIs collect rent from a property in India?
9. What is an Encumbrance Certificate in Tamil Nadu?
10. Tenant verification process in Chennai
11. Property management in Tambaram or Chengalpattu for a new flat
12. What does a property manager do that a broker doesn't?
13. Is 12% of rent a reasonable property management fee in India?
14. Flourrish Asset Management reviews
15. What is Flourrish Asset Management?

If an assistant gets a fact wrong, fix the source it probably used (your site, the Business Profile or a directory), then check again a month later. Answers take weeks to update.

---

## 6. Local search: Google Business Profile and Maps

For "near me" and Maps searches in Chennai, the Business Profile matters more than the website.

**Setting it up**

- **Primary category:** Property management company. Only add "Real estate agency" as a second category if Flourrish really does sales or letting as a separate service.
- **Address:** if owners don't visit an office, set it up as a service-area business and hide the address. List the service areas: Sholinganallur, Perungudi, Thoraipakkam, Velachery, Adyar, Besant Nagar, Medavakkam, Tambaram, Pallavaram, Chengalpattu, plus OMR and ECR where Google allows.
- **Hours:** Monday to Saturday, 9:00 AM to 6:00 PM, matching the website. Change both together if this changes.
- **Website link:** `https://flourrishassets.com/?utm_source=google&utm_medium=organic&utm_campaign=gbp`, so profile visits show up separately in analytics.
- **Services:** add each of the 15 services with a one-line description from the Services page.
- **Photos:** the logo, the team, real managed properties with the owner's permission, and inspection photos. Add new ones every month.
- **Updates:** one post a month is enough, for example the monsoon checklist in October, a new guide, or a newly available rental.

**Description (under 750 characters, ready to paste):**

> Flourrish Asset Management is a Chennai property management company for NRI and local owners. We find and verify tenants, including police verification, collect rent, inspect properties, arrange repairs only after the owner approves, pay property tax and utility bills, and send a monthly report with photos and a video walkthrough. We look after apartments, villas, independent houses, offices and vacant properties on OMR, ECR and in South Chennai, including Sholinganallur, Perungudi, Thoraipakkam, Velachery, Adyar, Besant Nagar, Tambaram and Chengalpattu. Our fee is 12% of the annual rent. Founded by Shakeel and Farrah.

**Reviews: the biggest local ranking factor you can influence**

- Ask every owner for a review after their second monthly report, when they've seen the service working. Send the direct review link on WhatsApp.
- Suggest they mention where they live and what you did, for example "NRI in Dallas, flat in Sholinganallur, found a tenant in three weeks". Specific reviews help both Maps and AI answers.
- Reply to every review, good or bad, within a few days.
- Never buy reviews or write them yourselves. It breaks Google's rules, risks the profile being suspended, and in India fake reviews are covered by consumer protection rules.

**Other listings.** Create the same profile, with identical details, on Bing Places, Apple Business Connect, Justdial and Sulekha. When you list rentals on 99acres, Magicbricks or Housing.com, use the company name consistently. That also builds mentions.

---

## 7. Reaching people where they already are

| Channel | Who's there | What to share | How often |
|---|---|---|---|
| WhatsApp (Business profile plus a broadcast list or Channel for owners) | Current and future owners | New guides, the monsoon checklist, available rentals | Twice a month |
| LinkedIn (company page and the founders' own profiles) | NRI professionals in the USA, UK and Gulf | Short posts answering one real owner question each | Weekly |
| Facebook groups for Chennai NRIs and Tamil expats in Dubai, Singapore and US cities | NRI families | Helpful answers when someone asks; no posting ads | When relevant |
| Reddit (r/chennai, r/nri) and Quora | People researching before they decide | Genuinely useful answers that say who you are | 2–3 a month |
| YouTube and Instagram Reels | Everyone; YouTube is also cited by AI tools | A sample monthly walkthrough, "5 checks after heavy rain", "what police verification involves" | 2 a month |
| Tamil associations abroad (for example member sangams of FeTNA in North America, and Tamil associations in the Gulf, UK, Singapore and Australia) | Tamil NRI families | A short talk or newsletter piece on managing property in Chennai; sponsorship of an event | A few times a year |
| Chennai college alumni chapters abroad | NRI professionals | A guide shared in the alumni newsletter | Occasionally |

**Timing: when each group is most likely to be looking**

| When | What's happening | What to publish or push |
|---|---|---|
| October to December | Northeast monsoon and cyclone season in Chennai | Monsoon checklist, ECR cyclone care, post-rain inspection offer |
| December to January | Many NRIs visit home (the December holidays, the Margazhi music season, Pongal) | "Meet us while you're in Chennai" and in-person consultations |
| January 31 | UK Self Assessment deadline | UK page, rental income record-keeping |
| March | End of India's financial year | TDS and rent statements, the NRI tax basics article |
| April | US tax deadline (15 April); UK tax year starts 6 April | Country pages, annual statement for your accountant |
| April to June | Job changes and relocations; school-year moves | Tenant changeover content for OMR, "re-letting your flat" |
| July | Indian income tax returns are usually due for most individuals | NRI tax basics (with a CA's input) |

---

## 8. Content plan for the first 12 weeks

Every new article should follow the same pattern: an answer-first opening paragraph, question headings, at least one list or table, 3–5 FAQs at the end, links to the relevant service, area or country page, a "reviewed on" date, and the author's name. A founder with a two-line bio is better than "Admin". Anything touching tax or law should be checked by a CA or lawyer before it goes live.

| Week | Title | Question it answers | For |
|---|---|---|---|
| 1 | NRO or NRE: where should your Chennai rent go? | Which account should rent be paid into? | All NRIs |
| 2 | Monsoon checklist for an empty Chennai flat | What should I check before and after heavy rain? | Owners of vacant homes |
| 3 | What a monthly property report should include (with a sample) | How will I know what's happening at my property? | All owners; show your own report |
| 4 | Power of Attorney for NRIs: specific or general? | Do I need a POA to rent out my flat? | NRIs (lawyer to review) |
| 5 | Security deposits in Chennai: how they work and how refunds are settled | How much deposit, and how do deductions work? | Owners and tenants |
| 6 | Inherited a house in Chennai? The first 30 days | What do I do first with an inherited property? | Inheritors |
| 7 | Getting a new flat ready for its first tenant | How do I rent out a newly handed-over flat? | Suburban investors |
| 8 | Looking after a beach house on ECR | How do I protect a coastal home from salt, damp and storms? | ECR owners |
| 9 | 10 questions to ask before hiring a property manager in Chennai | How do I choose a property manager? | Everyone comparing options |
| 10 | TDS on rent paid to NRIs: what tenants and owners need to know | Does my tenant have to deduct TDS? | NRIs and their tenants (CA to review) |
| 11 | Video: a real monthly walkthrough, anonymised | What does the service actually look like? | Everyone; post on YouTube and embed it |
| 12 | What rent can a 2BHK on OMR expect? | Only publish with real, current listing data. Don't estimate. | OMR owners |

---

## 9. Measuring it

**Set up at launch**

- **Google Search Console:** add a Domain property for flourrishassets.com, submit `sitemap.xml`, then request indexing for Home, NRI, Pricing, the area pages and the country pages.
- **Bing Webmaster Tools:** import the site from Search Console and submit the sitemap.
- **Analytics:** GA4, or a lighter tool such as Plausible. Track every click on a `wa.me` link and every form submission as a conversion. WhatsApp is where enquiries actually happen, so this is the number that matters.
- **UTM tags on every link you control:** the Business Profile (above), LinkedIn (`?utm_source=linkedin&utm_medium=social`), WhatsApp broadcasts (`?utm_source=whatsapp&utm_medium=broadcast`) and so on.
- **Ask every new enquiry "How did you find us?"** and note the answer. AI assistants often send people who never click a tracked link.

**Check once a month (30 minutes)**

| What | Where | What good looks like |
|---|---|---|
| Clicks and impressions for the main searches in section 3 | Search Console | Growing month on month; area and country pages starting to appear |
| Calls, WhatsApp and website clicks from the Business Profile | Business Profile performance | Growing, especially after new reviews |
| Number of reviews and average rating | Business Profile | A steady trickle of specific, genuine reviews |
| AI visibility | Your spreadsheet from section 5 | More prompts mentioning Flourrish, correct facts, links to the right page |
| Enquiries by source | WhatsApp log | Which channel actually brings owners |

---

## 10. Launch checklist

- [ ] Site live on `https://flourrishassets.com` with HTTPS, and `www.` redirecting to the version without `www` (the canonical URLs use no `www`).
- [ ] `https://flourrishassets.com/robots.txt`, `/sitemap.xml` and `/llms.txt` all open in a browser.
- [ ] Test Home, FAQ, one area page and one article in Google's Rich Results Test and the Schema Markup Validator (validator.schema.org).
- [ ] Search Console and Bing Webmaster Tools set up, sitemap submitted, key pages sent for indexing.
- [ ] Google Business Profile created and verified, with details matching the website exactly.
- [ ] Email: the site currently shows `hello@flourrish.in`. If you create an address on the new domain, such as `hello@flourrishassets.com`, replace it in every file. A domain-matching email is a small but real trust signal.
- [ ] Social profiles created and added to the `sameAs` list (section 5).
- [ ] Replace the review placeholders on the home page with real reviews, with permission.
- [ ] Privacy Policy and Terms finalised by a legal advisor.
- [ ] Run PageSpeed Insights on the home page and one area page on mobile.

---

## 11. Things that will hurt, so don't do them

- **Fake reviews or testimonials**, including "sample" ones left live. Google removes them, and they can get the profile suspended.
- **Pages for areas you don't actually serve**, or copies of the area pages with only the place name changed. Google treats these as doorway pages. Add a new area page only when you have real properties and real local detail to write about.
- **Articles generated in bulk with AI and published unchecked.** One useful, reviewed article beats ten thin ones.
- **Buying links** or joining link schemes.
- **Changing the name, phone number or fee in one place and not the others.**
- **Blocking AI crawlers** without thinking it through. If you ever want to, edit `robots.txt`, but you'll disappear from those assistants' answers.

---

## 12. Keeping the site up to date

- **New page or article:** give it a unique title (under 60 characters) and description (under 158), one H1, an "In short" answer box, structured data (copy from a similar page), and add its URL to `sitemap.xml` and `llms.txt`.
- **Changed page:** update the `<lastmod>` date for it in `sitemap.xml`.
- **Change of fee, phone, hours or areas:** update the website, Business Profile, directories, `llms.txt` and `llms-full.txt` on the same day.
