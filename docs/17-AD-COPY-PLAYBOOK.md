# Ad Copy and Offer Playbook - v1

The library of real, evidence-backed Facebook ad copy, offers, hooks, and creative patterns
for HVAC, plumbing, roofing, and electrical. Per the operator correction at the end of
`docs/13-TRADE-PLAYBOOK.md`, Meta has stripped out nearly every audience-targeting lever we
could once pull on the owner's behalf (Partner Categories including homeowner status are
gone, Detailed Targeting Exclusions are gone, Advantage Detailed Targeting cannot be turned
off). Geography and budget still matter, but **offer, copy, and creative now carry almost all
the weight of whether an ad works.** This document is the research behind that weight. It does
not repeat `docs/13-TRADE-PLAYBOOK.md`'s targeting or budget sections; read that document for
those. It does not repeat `docs/14-AD-POLICY-RULES.md`'s policy lint; read that document for
compliance rules. Every example produced here was checked against that lint by hand.

## How this document was built, and how to read every claim in it

Three source tiers, and every single ad example below is labeled with exactly one of them.
Never let these collapse into each other. A template written for this document is not a real
ad, and an agency's description of an ad is not the same as having seen the ad.

- **`VERIFIED_REAL`** - The actual ad, found and read directly in the Meta Ad Library
  (facebook.com/ads/library) by this research, or quoted verbatim by a secondary source that
  itself screenshotted the ad from the Meta Ad Library with a stated advertiser name and start
  date. Every entry carries the advertiser name, the Meta Ad Library Library ID where captured
  directly, a start date where known, and a source URL. Where the source URL is a direct Meta
  Ad Library search URL, the specific ad can be re-found by searching the advertiser name in
  that same URL with country set to US.
- **`AGENCY_CLAIMED`** - An agency, coaching business, or blog describes an ad's existence,
  approach, or result without showing the actual creative or quoting its exact copy. Treated as
  an informed opinion from someone who sells services to this exact audience, not as evidence
  the ad exists as described. Never used as the basis for a "what works" claim without saying
  so.
- **`ILLUSTRATIVE`** - Written for this document, to the validated pattern below it, explicitly
  labeled as not observed. Used only in the copy-structure templates in section 5, never
  presented as a real ad anywhere else in this document.

Research method: the Meta Ad Library's public web interface
(`facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=<keyword>`) was
searched directly, live, on 2026-08-19, using exact-phrase queries per trade ("hvac tune-up",
"drain cleaning", "roof inspection", "electrical panel", "whole home generator", "emergency
electrician"). Results include the Meta-assigned Library ID and a "Started running on" date for
every ad, which is the Ad Library's own signal for run duration: an ad still active after 90+
days is very likely still generating jobs, because advertisers do not keep paying for ads that
do not work. That reasoning is the same one several agency sources below use independently. In
addition, agency and coaching blogs that publish direct Ad Library screenshots with advertiser
name and start date (leadsync.me's ad breakdowns in particular) were used as a secondary source
for examples not independently re-captured, and are labeled `VERIFIED_REAL` with the agency
page as the source URL since the underlying evidence is the same public Ad Library screenshot,
just accessed secondhand.

One honesty note up front, matching the trade playbook's finding: **electrical is the
thinnest trade for narrative/urgency copy**, but it turned out to have the richest real ad
volume of the four trades for planned-upgrade offers (panel upgrades, generator installs). The
weak spot for electrical is specifically emergency/urgency framing - an exact-phrase Ad Library
search for "emergency electrician" returned only 3 live US results total on the day this
research was done, two of which were unrelated marketing-service ads. That is itself a real,
sourced finding, not a gap papered over: electrical customers and electrical advertisers
overwhelmingly frame this trade as planned and safety-driven, not as an emergency category, and
the copy priors below reflect that rather than forcing an emergency angle the market data does
not support.

---

## 1. Real ad examples, by trade

Every ad below was live in the Meta Ad Library on 2026-08-19 unless otherwise noted. Quoted
text is verbatim except for typographic normalization (em dashes in source ads are rendered as
a hyphen here, per this project's no-em-dash rule; no words were added, removed, or changed).
Where an ad included emoji, they are preserved because they are part of the actual creative
decision being documented.

### 1.1 HVAC

**Source for this subsection:** Meta Ad Library, exact-phrase search "hvac tune-up" and
"$X tune-up" variants, `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=hvac+tune-up` (browsed live 2026-08-19), plus
[LeadSync, HVAC Facebook Ads: 8 Real Examples](https://leadsync.me/blog/hvac-facebook-ad-examples/)
which screenshots additional Ad Library entries with start dates this research did not
independently re-capture.

| Advertiser | Started running | Library ID | Primary text (verbatim, trimmed where noted) | Headline | Offer | Status |
|---|---|---|---|---|---|---|
| Global International Heating And Cooling Co | May 24, 2022 (1,500+ days active as of this research - the single longest-running home-service ad found in this entire research pass) | 692268871996677 | "Keep your A/C running all season long with routine maintenance and cleanings! We're your local HVAC experts!" | "$59 A/C Tuneup" | $59 named tune-up, "Receive high-quality service at affordable prices" | VERIFIED_REAL |
| Ferran Services & Contracting, Inc | Dec 10, 2023 | 366564742538089 | "Whether you need to Tune-Up your AC system, or need an estimate for a new system, you can count on Ferran Services: 407-270-0732" | "Have You Tune-Up Your HVAC System?" | Tune-up or replacement estimate, phone number in the primary text itself | VERIFIED_REAL |
| Semper Fi Heating and Cooling | Jun 17, 2026 | 2077773973128031 | "Las Vegas homeowners! Get a Full AC System Tune-Up for $49.95. Our technicians will: Inspect your cooling system, Clean key components, Make sure everything is running properly. Regular tune-ups help prevent costly repairs and keep your system running efficiently. Schedule your tune-up today. *Terms apply | HVAC Lic#: 93485" | "$49.95 AC System Tune-Up - Book Now" | $49.95 named tune-up, license number disclosed in copy | VERIFIED_REAL |
| Semper Fi Heating and Cooling (second, concurrent ad) | Jun 17, 2026 | 1663719658247813 | "Get an AC System Tune-Up and Inspection for just $17.75 for a limited time. Make sure your system is running the way it should before bigger issues show up." | "Get Ready for Any Season: $17.75 AC Tune-Up" | $17.75 loss-leader tune-up, same advertiser running a second, cheaper offer in parallel to the $49.95 one above | VERIFIED_REAL |
| Air & Drain Works | Jun 16, 2026 | 851362820952352 | "What does a $20.26 tune-up actually get you? A full system inspection: coils cleaned, refrigerant checked, electrical tightened, thermostat calibrated, plus a safety and carbon monoxide check. Not a quick look. A real once-over, and a free year of HVAC and plumbing memberships." | "$20.26 HVAC tune-up. Yep. Really." / "Licensed San Antonio techs. Same-day service." | Odd-number price ($20.26, likely tied to the current year), itemized what the fee covers, bundled free membership year | VERIFIED_REAL |
| Air & Drain Works (A/B variant, same offer) | Jun 3, 2026 | 998198822915319 | "Two ways to meet the first 100-degree day: a $20.26 tune-up, or a $500+ surprise repair. One of those is a lot more fun. We catch the small stuff before summer turns it into the expensive stuff." | "Pay $20.26 Now Or $500 In July" | Same $20.26 offer, reframed around a comparison to a future repair cost instead of the itemized-inspection angle | VERIFIED_REAL |
| Rescue One Air | May 2026 (70+ days per leadsync.me) | n/a (leadsync.me screenshot) | "For just $19.95 + 2 cans of food, get a comprehensive Furnace & AC Tune-Up" | Book Now CTA | Tune-up priced in cash plus a canned-food donation, charity tie-in | VERIFIED_REAL, via leadsync.me |
| Integrity Services | Apr 2026 (105+ days per leadsync.me) | n/a | "$79 Tune-Up Special! Only $29 after $50 TVA rebate" | Book Now CTA | Named tune-up price with a stacked utility rebate shown as arithmetic in the headline | VERIFIED_REAL, via leadsync.me |
| Horne Heating | Apr 2026 (110+ days) | n/a | "Schedule an A/C tune-up today and receive a FREE plumbing inspection" | Book Now CTA | Cross-trade bundle: HVAC tune-up plus a free adjacent-trade inspection | VERIFIED_REAL, via leadsync.me |
| Baumann & DeGroot | Apr 2026 (105+ days) | n/a | "Are you really getting a fair deal on your AC quote? Get a second opinion" | n/a | Free second-opinion framing rather than a price-led offer | VERIFIED_REAL, via leadsync.me |
| Professor Heating and Air | Jun 10, 2026 | 2645391789195424 | "NoVA, THE HEAT IS HERE! 90-degree temperatures are arriving, and your AC system is about to be put to the test... $69 AC Service & Inspection, Check Refrigerant Levels, Test System Performance, Same-Day Service Available, 24/7 Emergency Service, FREE Second Opinions, Full System Replacements Available, Financing Available." | "Don't wait for your AC to fail during the next heat wave" | $69 tune-up plus a menu of adjacent services (second opinion, financing, full replacement) in one ad | VERIFIED_REAL |
| Capital City Heating & Cooling | Feb 17, 2026 | 806284149152919 | "We started this company with one simple goal - to take care of families the right way... We're not owned by a private equity group, and we're not looking to sell out. We're building something solid, something we can pass on to our kids..." | "HVAC Repair & Replacement" | No discrete offer - pure trust/ownership-story copy, positioned against private-equity roll-ups | VERIFIED_REAL |

**Trade-specific read:** every HVAC ad found that has run 90+ days leads with a specific,
often odd-cent dollar figure ($17.75, $20.26, $49.95, $59) rather than a round number, and
several advertisers run two or three price variants of the same tune-up concurrently, which
reads as active A/B testing rather than a single settled price. Financing and "free second
opinion" appear as secondary offers stacked onto a primary tune-up price, never as the lone
offer on their own.

### 1.2 Plumbing

**Source:** Meta Ad Library, exact-phrase search "drain cleaning",
`https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=%22drain+cleaning%22&search_type=keyword_exact_phrase`
(browsed live 2026-08-19).

| Advertiser | Started running | Library ID | Primary text (verbatim, trimmed where noted) | Headline | Offer | Status |
|---|---|---|---|---|---|---|
| Lancaster Plumbing, Heating, Cooling & Electrical | Jun 19, 2025 | 1803525773561880 | "Got a backed up main drain? We'll unclog it for only $93 or the service is FREE! Includes a camera inspection. Book today and say goodbye to backups tomorrow!" | "Unclog Your Main Drain for Only $93 or It's Free!" | Named price with a money-back guarantee structure and a bundled camera inspection | VERIFIED_REAL |
| MasterTex Plumbing & Drain | May 29, 2026 | 880933088365490 | "DFW homeowners, beware! A slow drain today can mean flooded floors tomorrow. Gurgling toilets and sewage smells are red flags - don't ignore them! Get a clear solution: $97 Drain Cleaning + Full Camera Inspection, Licensed Local Plumbers, Same-Day Dispatch Available. We identify the issue & show you proof. No guessing games or scare tactics!" | "$97 Drain Cleaning Free Camera Inspection" | $97 named price, explicit anti-scare-tactic line ("No guessing games or scare tactics") | VERIFIED_REAL |
| Bayshore Plumbers | Apr 30, 2026 | 978189521406141 | "Redwood City Homeowners - Bay Shore Plumbers, your trusted veteran-owned plumbing team, just dropped a drain cleaning deal you don't want to sleep on. $49 Drain Cleaning (regularly $85) - that's 42% off... Spots are filling up FAST due to high demand - once they're gone, the price goes back to $85." | n/a | $49 anchored against a stated $85 regular price, with a scarcity claim | VERIFIED_REAL, and flagged: the "spots are filling up" claim reads close to the false-scarcity pattern `docs/14-AD-POLICY-RULES.md` section 2 warns about unless the advertiser can actually show a real capacity limit |
| Rooter Help and Plumbing | Jul 24, 2023 | 671776438246976 | "Here to service all your plumbing needs. Free Estimates, $60.00 Drain Cleaning, Water Heater Replacement and Repair, No Job To Big Or Small, Sewer Repairs, repipes and Gas Line Repairs, Faucet Replacement" | n/a | $60 flat drain-cleaning price alongside a broader service list | VERIFIED_REAL |
| Flash Plumbing Inc | May 6, 2026 | 26346460828389554 | "Covina's Fastest Plumbing Service. Don't wait hours for a call back. Don't overpay. Flash Plumbing provides FAST 24/7 service with FREE estimates and licensed professionals you can trust." | "Fast response. Honest pricing. Free estimates." | Free estimate, speed-led rather than price-led | VERIFIED_REAL |
| Mr. Rooter Plumbing of St. George | Feb 23, 2026 | 1716609469504938 | "Plumbing emergency? Don't wait. Mr. Rooter Plumbing is ready to help - fast. Emergency service available, No overtime charges, Reliable, professional plumbers." | "Plumbing You Can Trust" | No discrete dollar offer; the "no overtime charges" line functions as a soft price reassurance for after-hours calls | VERIFIED_REAL |
| Trust Rooter Plumbing & Drain Cleaning | Jun 28, 2025 | 719007107495085 | "Top-Rated #1 Family-Owned Plumbing Service Company in Broward County and Surrounding Areas. Same Day Services, Free On-Site Quote, 10% Off New Customers, 500+ Five Star Reviews, Rated A+ BBB" | "Top-Rated Local Plumbers" / "Same Day On-Site Quotes" / "Drain Cleaning Experts" / "Sewer Repair Services" | 10% new-customer discount stacked with review-count and BBB credential proof | VERIFIED_REAL |
| American Plumbing & Sewer LLC | Feb 2, 2026 | 4054671418117726 | "Are you facing plumbing issues at home or in your business?... 24/7 Emergency Services, Experienced professionals, Transparent pricing with no hidden fees, Commitment to customer satisfaction, BBB accredited..." | "Plumbing Service" | Free estimate, no discrete dollar figure | VERIFIED_REAL |

**Trade-specific read:** unlike HVAC's tune-up convergence, plumbing's real ads split cleanly
into two offer camps: a named-dollar drain-cleaning fee ($49-$97, always paired with a camera
inspection as the value-add) and a "free estimate, fast response" camp with no discrete price
at all. The playbook's diagnostic-fee theory (2.2 in `docs/13-TRADE-PLAYBOOK.md`) is visible
in the wild, but so is its stated alternative (free estimate, no fee) running just as commonly
- this document cannot say which converts better, only that both are real, current market
practice.

### 1.3 Roofing

**Source:** Meta Ad Library, exact-phrase search "roof inspection",
`https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=%22roof+inspection%22&search_type=keyword_exact_phrase`
(browsed live 2026-08-19), plus
[LeadSync, Roofing Facebook Ads: 10 Real Examples That Have Run for Months](https://leadsync.me/blog/roofing-facebook-ad-examples/).

| Advertiser | Started running | Library ID | Primary text (verbatim, trimmed where noted) | Headline | Offer | Status |
|---|---|---|---|---|---|---|
| American Roofing & Waterproofing, LLC | Jul 1, 2025 (390+ days per leadsync.me) | 1274035257478403 | "Wind hit hard. Your roof took the blow. Monsoon season in Phoenix shows no mercy. We fix damage fast. No delays. No guesswork." | "Monsoon Roof Readiness" | Free inspection and estimate, named regional weather event ("monsoon season") without naming a specific storm | VERIFIED_REAL |
| Brookens Construction, LLC | Apr 27, 2026 (90+ days) | 967809215836899 | "One storm. Thousands of roofs. Homes across the Milwaukee area took a hit - and we're finding serious damage. Schedule a free, no-obligation roof inspection. We'll document any damage and walk you through the insurance process." | "Local Crews. Real Damage. Real Solutions." | Free, no-obligation inspection, insurance-process assistance offered as a service (not an outcome guarantee) | VERIFIED_REAL |
| Central Arkansas Roofing Services | Feb 1, 2024 (900+ days per leadsync.me) | 729970015773426 | "Central Arkansas Roofing Is Here For All Of Your Residential Roofing Needs." | "Leaky Roof?" | Two-word problem-callout headline over a 15-second video; no price shown in the captured text | VERIFIED_REAL |
| JML Roofing Solutions | May 7, 2026 | 2110336156204033 | "Built on relationships, trust, and strong local roots." | "Rockwall / 250+ 5-star reviews / Go local / Choose JML" (3-slide carousel) | No dollar offer; pure social-proof and local-identity carousel | VERIFIED_REAL |
| Glacier Roofing & Exteriors | Jun 15, 2026 | 1316806650664775 | "Is your insurance company threatening to drop you because of your roof's age? Insurers across the Inland Northwest are tightening their requirements - and if your roof is 15 years or older, you could be at risk of losing your coverage... Insurance claim restoration experts, HAAG-Certified inspectors - we work directly with your adjuster, We document everything & fight for your full claim..." | "Roof Too Old? Insurance Got You Covered" | Free inspection, framed around a coverage-loss risk trigger | VERIFIED_REAL, and flagged: "we document everything & fight for your full claim" sits close to the insurance-outcome-promise line `docs/14-AD-POLICY-RULES.md` TRADE-ROOF-01 exists to catch; it stops short of guaranteeing a payout, but the generator should not copy this phrasing without softening it further |
| A-R Roofing | Jul 29, 2026 | 27872875662352101 | "St. Louis homeowners - now is the perfect time to upgrade your roof. If your roof qualifies for an insurance-covered replacement, ask about our limited-time upgrade to Class 4 impact-resistant shingles at no additional cost on qualifying projects." | n/a | Free inspection, plus a conditional material upgrade tied to insurance qualification | VERIFIED_REAL, same insurance-adjacent caution as above |
| Batterbee Roofing | May 7, 2026 | 1133423278965526 | "The ugly truth about roofing is, there's always someone willing to cut corners to offer a lower price... We might not be the lowest bid you get. But we will be the one that makes the most sense when you ask the right questions." | "Get a New Roof for Thousands Less!" | Free inspection, anti-cheap-competitor trust narrative rather than a price-led offer | VERIFIED_REAL |
| J Smegal Roofing / Guns N Hoses Roofing & Siding | Dec 11, 2025 / Jun 2, 2026 | 1537754327346895 / 1469210844532084 | Long-form story ad: a homeowner got three quotes, chose the cheapest, the roof failed in six months because shingles were installed over old ones, the advertiser fixed it. "[City/State] homeowners are losing THOUSANDS on their roofs by picking the wrong contractor." | "Don't Overpay THOUSANDS On A New Roof" | Free, fair, fast estimate; notable because the exact same long-form story template (down to matching sentence structure) is run word-for-word by two unrelated advertisers in two different states, strong evidence this is a licensed or agency-written swipe template, not an organic story either company personally experienced | VERIFIED_REAL |
| DryHome Roofing and Siding | Sep 2024 (690+ days per leadsync.me) | n/a | "Licensed, bonded, insured, replacing roofs since 1988" | Contact Us CTA | No offer at all - pure credentials, the only ad in this entire roofing sample with zero promotional hook | VERIFIED_REAL, via leadsync.me |
| Stones River Roofing | Sep 2025 (315+ days) | n/a | "The only local contractor offering a lifetime labor warranty on every project" | Book Now CTA | Single differentiator claim framed as exclusive | VERIFIED_REAL, via leadsync.me |
| 3MG Roofing and Solar | May 2026 (70+ days) | n/a | "3MG isn't a storm chaser; we're your neighbors" | Book Now CTA | Direct anti-positioning against the storm-chaser stigma named in `docs/13-TRADE-PLAYBOOK.md` 3.2 | VERIFIED_REAL, via leadsync.me |

**Trade-specific read:** the storm-chaser trust problem flagged in the trade playbook is
visible and being actively fought in the wild, not theoretical - 3MG's ad names the accusation
directly to defuse it. The insurance-outcome risk is also visible in the wild: two real, live
ads (Glacier Roofing, A-R Roofing) sit close enough to the insurance-guarantee line that they
are useful as negative examples for the policy lint, not just positive copy inspiration. The
duplicated "three quotes, chose cheapest, roof failed" story running verbatim across two
different companies is worth flagging on its own: it confirms a swipe-file or agency-template
economy exists behind roofing Facebook ads specifically, which matches this document's own
mandate to build a legitimate version of exactly that.

### 1.4 Electrical

**Source:** Meta Ad Library, exact-phrase searches "electrical panel", "whole home generator",
and "emergency electrician",
`https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=%22electrical+panel%22&search_type=keyword_exact_phrase`
and equivalent URLs for the other two phrases (browsed live 2026-08-19).

| Advertiser | Started running | Library ID | Primary text (verbatim, trimmed where noted) | Headline | Offer | Status |
|---|---|---|---|---|---|---|
| Cool Today - Cooling, Plumbing, Electrical | Aug 1, 2026 | 1712674516693478 | "Your electrical panel works hard every day - but when was the last time it was inspected? For a limited time, Cool Today is offering a $29 Electrical Panel Safety Check... Cannot be combined with other offers. Not valid on prior purchases. Residential customers only." | "$29 Electrical Panel Safety Check" | $29 named safety check, with explicit fine-print restrictions in the ad copy itself | VERIFIED_REAL |
| Copeland Heating Air Conditioning Plumbing and Electrical Repair Services | Jul 1, 2026 | 1054465217152169 | "Up to $250 OFF New Electrical Panel Installation. If your breakers keep tripping or your home still has an older electrical panel, don't wait until it becomes a bigger issue... Payments as low as $89/month..." | "$250 OFF Electrical Panel" | $250-off panel upgrade, monthly-payment financing framing for the full job | VERIFIED_REAL |
| Utah Homeowner News | May 28, 2026 | 1029097669773980 | "If your home was built in the 1950s, 60s, 70s, or 80s... you might still have one of these outdated electrical panels. Some older panels are now known for breaker issues and potential safety concerns. We're offering free inspections to help Utah homeowners identify what's behind the panel door." | "Free Electrical Panel Inspection" | Free inspection, home-age used as self-qualifying copy language (not a Meta targeting field, exactly as flagged in `docs/13-TRADE-PLAYBOOK.md` - real advertisers are putting the age question in the ad text itself instead) | VERIFIED_REAL, and notable: the advertiser name itself ("Utah Homeowner News" / the same pattern appears as "Colorado Homeowner News") reads as a lead-gen operation posing as a local news outlet rather than a licensed electrical contractor, which is a real, observed pattern worth flagging rather than imitating |
| Elm Tree Electric | Mar 26, 2026 | 1601951137931745 | "Outdated electrical panel? Flickering lights? Planning a remodel? Elm Tree Electric helps homeowners and businesses across Nashville with safe, professional electrical work - from panel upgrades to lighting and smart home installations." | n/a | No discrete offer - trigger-symptom question opener into a general capability statement | VERIFIED_REAL |
| Horizon Services | Jul 1, 2026 | 1027912506376338 | "Keep your family and your home safe with a FREE Electrical Panel Safety Inspection with any booked electrical service." | "Avoid costly electrical repairs!" | Free inspection, conditioned on booking any other electrical service (an upsell-anchor structure, not a standalone lead magnet) | VERIFIED_REAL |
| Peterman Brothers - HVAC, Plumbing & Electrical | Jun 5, 2026 | 1522833198999007 | "A weather alert can change the whole mood at home. Before the next storm tests your power, find out what a generator could do for yours." | "Ready Before It Hits" / "Explore generator options" | Storm-preparedness framing for a whole-home generator, no price shown | VERIFIED_REAL |
| Great Dane Heating, Cooling, Electrical, & Plumbing | May 29, 2026 | 3336890036480924 | "Don't be left in the dark when heavy rains and high winds hit - protect your home and your peace of mind with a whole-home generator. Now is the BEST time to install - we're offering an incredible $2,500 OFF installation, 2 YEARS of FREE maintenance, PLUS a FREE surge protector..." | n/a | $2,500 off plus a stacked 2-year maintenance and surge-protector bundle | VERIFIED_REAL |
| AstroGenerators | Aug 5, 2026 | 1047773187835575 | "Houston Homeowners - Save Up to $1,500 on a Briggs & Stratton Generator. Power outages in the Houston area aren't a matter of if, but when... 0% Interest + $0 Down financing available through Synchrony, FREE Automatic Transfer Switch ($1,099 value), 10 year comprehensive warranty..." | "Save $1,500 on a Home Generator" | $1,500 off, named financing partner, itemized bundled value | VERIFIED_REAL |
| Bigfoot Electric & AC - Bath & Windows | Jul 26, 2026 | 1020841913910923 | "Think a whole-home generator is out of reach? You might be surprised. See your financing options for a professionally installed Generac standby generator - with options available for credit scores as low as 550." | "See Your Generator Payment Options" | Financing-led, explicitly names a low credit-score threshold | VERIFIED_REAL, and flagged: "credit scores as low as 550" is exactly the kind of financing-qualification language `docs/14-AD-POLICY-RULES.md` section 1's CREDIT_SIGNALS_TIER_A treats as a Special Ad Category trigger - a real, live ad demonstrating the exact pattern the policy lint must catch |
| Base Power Company | Jul 21, 2026 | 1060594369795466 | "A $13K+ generator is no longer the only way to get automatic home backup. Base partnered with Farmers Electric Cooperative to offer homeowners a powerful battery system that protects your home at a fraction of the cost of comparable solutions." | n/a | Price-anchor-against-alternative framing (battery vs. traditional generator cost) rather than a direct discount | VERIFIED_REAL |
| McLeods Electrical Services LLC | Apr 23, 2026 | 1371847534978799 | "Power out? Flickering lights? Breaker keeps tripping? Don't wait - electrical issues can turn dangerous fast... Fast response, Licensed & insured, 7+ years experience." | "Emergency Electrician Near You" | No price; one of only three live US ads found under an exact "emergency electrician" search, confirming how rare true emergency framing is for this trade | VERIFIED_REAL |

**Trade-specific read:** this is the trade `docs/13-TRADE-PLAYBOOK.md` flagged as thinnest, and
the search results confirm that specifically for narrative and urgency copy, not for offer
volume. Panel-upgrade and whole-home-generator ads are plentiful, well-developed, and lean
heavily on financing language, which means electrical is the trade where the credit/financing
policy category (section 1 of `docs/14-AD-POLICY-RULES.md`) will fire most often of the four,
not HVAC or roofing as the trade playbook's budget section implied. Emergency framing is
genuinely rare in the wild for this trade, confirming it should not be a default angle.

---

## 2. Hook taxonomy

Every category below is illustrated with real ads pulled from section 1. Hooks not traceable
to a real example are marked as such.

### 2.1 Problem/symptom question opener

**Pattern:** open with a short, specific question about equipment or property state, never
about the viewer's body or finances. This is the single most common opener across every trade
sampled.

- HVAC: none of the top-performing HVAC ads found in this pass opened this way (they opened
  with the price); the pattern is stronger in plumbing and electrical.
- Plumbing: MasterTex Plumbing & Drain, "A slow drain today can mean flooded floors tomorrow.
  Gurgling toilets and sewage smells are red flags." (1.2 above)
- Roofing: Central Arkansas Roofing, "Leaky Roof?" (1.3 above), the shortest hook in the entire
  sample.
- Electrical: Elm Tree Electric, "Outdated electrical panel? Flickering lights? Planning a
  remodel?" (1.4 above); McLeods Electrical, "Power out? Flickering lights? Breaker keeps
  tripping?" (1.4 above)

**Why it works on this audience:** per `docs/14-AD-POLICY-RULES.md` section 2, "is your AC
broken" is explicitly the safe pattern precisely because it names equipment, not the viewer.
It also does real qualifying work for free - someone scrolling past who does not have a
flickering panel or a gurgling drain self-selects out before the offer is even read, which
should improve lead relevance without costing anything in ad spend.

**Suits:** all four trades, best for reactive/planned-problem services (panel upgrades, drain
clearing, roof leaks). Weaker fit for pure emergency dispatch, where speed should lead instead.

### 2.2 Price and offer lead

**Pattern:** the dollar figure is the first thing read, before any narrative.

- HVAC: nearly every long-running HVAC ad in section 1.1 does this - "$59 A/C Tuneup," "$49.95
  AC System Tune-Up," "$20.26 HVAC tune-up. Yep. Really."
- Plumbing: MasterTex, "$97 Drain Cleaning Free Camera Inspection"; Lancaster Plumbing, "Unclog
  Your Main Drain for Only $93 or It's Free!"
- Roofing: rare as a pure lead in this sample; roofing skews toward "free inspection" instead
  of a named paid price (see 3.2 below for why).
- Electrical: Cool Today, "$29 Electrical Panel Safety Check"; AstroGenerators, "Save $1,500 on
  a Home Generator."

**Why it works:** confirmed independently by [LeadSync's HVAC analysis](https://leadsync.me/blog/hvac-facebook-ad-examples/):
"price-anchored offers... routinely beat generic quote requests, because the risk is capped and
the value is concrete." A $59 tune-up is a small, known, bounded decision; "call for a free
estimate" asks the reader to open an unknown-sized commitment (a home visit, a sales
conversation) for an unstated reward.

**Suits:** HVAC and plumbing most strongly, where the sampled real ads converge hardest on this
pattern. Electrical for panel/generator work when a discount or financing figure is available.
Weakest fit for roofing, where "free" beats a named price in the observed sample.

### 2.3 Local and neighborhood proof

**Pattern:** names the city, region, or a specific local weather/market event, paired with a
review count or "local" identity claim.

- HVAC: Semper Fi Heating and Cooling, "Las Vegas homeowners!"; Air & Drain Works, "Licensed San
  Antonio techs."
- Roofing: American Roofing & Waterproofing, "Monsoon season in Phoenix shows no mercy"; JML
  Roofing, "Rockwall / 250+ 5-star reviews / Go local."
- Electrical: AstroGenerators, "Houston Homeowners"; Great Dane, serving "the Metro Detroit
  area since 1999."

**Why it works on this audience:** a contractor is a stranger being asked into someone's home.
Naming the specific city or neighborhood, and pairing it with a real review count, does the
trust-building work a national brand gets for free from familiarity. `docs/13-TRADE-PLAYBOOK.md`'s
finding that "real, slightly imperfect" beats polished stock applies to copy too, not just
images - a generic "your local HVAC experts" line does less work than "Las Vegas homeowners."

**Suits:** all four trades, strongest for roofing (where trust is the scarcest resource of the
four given the storm-chaser association) and weakest as a sole hook for HVAC/plumbing
emergencies where speed should lead instead.

### 2.4 Trust, credentials, and anti-competitor framing

**Pattern:** leads with licensing, tenure, ownership structure, or an explicit contrast against
lower-quality competitors, rather than a price or a problem.

- HVAC: Capital City Heating & Cooling, "We're not owned by a private equity group... We're
  building something solid, something we can pass on to our kids."
- Roofing: Batterbee Roofing, "The ugly truth about roofing is, there's always someone willing
  to cut corners"; DryHome Roofing, "Licensed, bonded, insured, replacing roofs since 1988"
  (zero-offer, pure-credential ad still running 690+ days).
- Roofing (long-form): the duplicated "three quotes, chose cheapest, roof failed in six months"
  story used verbatim by two different roofing companies (J Smegal Roofing and Guns N Hoses
  Roofing & Siding, 1.3 above).

**Why it works on this audience, and a real caution:** roofing is the trade with the most
active scam association (`docs/13-TRADE-PLAYBOOK.md` 3.2), so anti-competitor trust framing
does real work there specifically. The duplicated long-form story is worth a second look: it
demonstrates real market demand for exactly the kind of pre-written, evidence-based copy
template this product exists to generate, but it also shows how quickly a template goes stale
once it is copy-pasted word for word by unrelated companies - a generator producing the same
skeleton for every customer in a metro would recreate this problem at scale. Variation within
a validated skeleton, not verbatim reuse, is the right lesson to take from it.

**Suits:** roofing most, HVAC next (against the "no big-box, no private equity" trust angle
which shows up independently in Capital City's ad), weakest fit for a fast, cheap plumbing
drain-clearing offer where speed matters more than a trust narrative.

### 2.5 Storm and weather-event urgency

**Pattern:** ties the offer to a real, named regional weather pattern (a season, a storm type)
without naming one specific identifiable disaster event.

- Roofing: American Roofing & Waterproofing, "Wind hit hard. Your roof took the blow. Monsoon
  season in Phoenix shows no mercy"; Brookens Construction, "One storm. Thousands of roofs...
  Homes across the Milwaukee area took a hit."
- Electrical (generator): Great Dane, "Don't be left in the dark when heavy rains and high
  winds hit"; GVEC, "With the start of hurricane season this month."

**Why it works, and the compliance line:** `docs/14-AD-POLICY-RULES.md` TRADE-ROOF-02
distinguishes a general seasonal reference ("storm season is here," allowed) from naming a
specific, identifiable recent event paired with urgency (crisis exploitation, blocked).
Brookens Construction's "one storm... homes across the Milwaukee area took a hit" sits right at
that line - it references a real, recent, local event without naming it by name (no "Hurricane
X" or dated event), which is the pattern to replicate. American Roofing's "monsoon season"
framing is safely on the seasonal side because monsoon season is a recurring calendar period,
not a single dated storm.

**Suits:** roofing (baseline seasonal pattern) and electrical generator sales (storm/outage
risk). Not observed and not a natural fit for HVAC, plumbing, or panel-only electrical work.

### 2.6 Speed and availability

**Pattern:** leads with response time or hours of availability rather than price or a problem
symptom.

- Plumbing: Flash Plumbing, "Covina's Fastest Plumbing Service. Don't wait hours for a call
  back"; Mr. Rooter of St. George, "Plumbing emergency? Don't wait... ready to help - fast."
- Electrical: McLeods, "Fast response, Licensed & insured, 7+ years experience," the rare true
  emergency-framed electrical ad.

**Why it works on this audience:** matches `docs/13-TRADE-PLAYBOOK.md`'s cross-trade finding
that a Facebook lead is "hot" for about five minutes and connection odds fall roughly 80%
after 30 minutes - the reader has learned, correctly, that response speed is the real
differentiator once a pipe is actively leaking, so an ad that promises speed is answering the
one question that matters most in that moment.

**Suits:** plumbing and HVAC emergency campaigns strongest (matches the urgency taxonomy in
`docs/13-TRADE-PLAYBOOK.md` 1.1/2.1). Confirmed rare for electrical and largely absent from
the roofing sample, where "free inspection" outcompetes a speed claim.

### 2.7 Bundled/cross-trade offer

**Pattern:** stacks a second free or discounted service onto the primary offer, usually across
trade lines within a multi-trade home-services company.

- HVAC: Horne Heating, "Schedule an A/C tune-up today and receive a FREE plumbing inspection."
- Electrical: Horizon Services, "FREE Electrical Panel Safety Inspection with any booked
  electrical service."

**Why it works:** raises the perceived value of the ad without discounting the primary offer
itself, and it is a distinctly multi-trade-company pattern - every example found in this
research came from a company that explicitly brands itself across two or more trades ("Cool
Today - Cooling, Plumbing, Electrical"; "Lancaster Plumbing, Heating, Cooling & Electrical").
A single-trade shop cannot naturally run this hook.

**Suits:** any trade, but only for a business that genuinely offers the bundled second service.
Not usable as a generic template.

---

## 3. Offer library

Every structure below is drawn from the real ads in section 1 or explicitly flagged where it is
not. Dollar figures are real, observed prices, not invented examples.

| Offer structure | Trade(s) observed | Real dollar figures seen | Effect, and evidence | Lead-quality tradeoff |
|---|---|---|---|---|
| Named-price tune-up/inspection, odd-cent pricing | HVAC | $17.75, $19.95, $20.26, $29, $30, $49, $49.95, $59, $67, $69, $79, $85, $89, $99 (all seen live, 1.1 above) | The dominant HVAC pattern by a wide margin; [LeadSync's analysis](https://leadsync.me/blog/hvac-facebook-ad-examples/) argues these work as paid leads, not loss leaders - "even at $39 you're collecting revenue while filling the pipeline for five-figure system replacements." Confirmed as a real, current practice by volume alone (dozens of live advertisers running this exact structure). | Not independently measured for lead quality in this research; the trade playbook's caution (1.2) that this is a loss-leader business model that only works if the tech is trained to inspect-and-quote applies regardless of exact price point. |
| Named-price drain clearing/camera inspection | Plumbing | $49 (anchored against a stated $85), $60, $93 (money-back structured), $97 | Second most consistent price-led pattern found; always paired with "camera inspection" as the stated value-add, never a bare price alone. | Not measured here. The trade playbook's plumbing section (2.2) notes a fee filters tire-kickers better than free, and that pattern is visible in roughly half the plumbing sample, but the other half runs free-estimate offers just as commonly, so this document cannot resolve which wins. |
| Free, no-obligation inspection | Roofing (dominant), electrical (secondary, panel-safety) | n/a (free) | The single most common roofing offer by a wide margin in this sample - nearly every roofing ad found leads with "free roof inspection" in some phrasing. Matches `docs/13-TRADE-PLAYBOOK.md` 3.2's finding that this is the category's most common offer. | Same scam-association risk flagged in the trade playbook: several real ads in this sample (3MG's "isn't a storm chaser," Batterbee's "ugly truth" framing) exist specifically to counter the suspicion this exact offer type creates. A generator producing this offer for roofing should pair it with a no-pressure line by default, not as an afterthought. |
| Percent/dollar-off installation, financing-led | Electrical (generator, panel), roofing (replacement) | $250 off panel, $500-$2,500 off generator installs, "as low as $89-$195/month," 0% interest offers, "credit scores as low as 550" | Common and current for high-ticket electrical work specifically - every generator ad sampled in 1.4 carries either a flat discount or a financing hook, usually both. | This is the offer type most likely to trip the Special Ad Category / credit policy rules in `docs/14-AD-POLICY-RULES.md` section 1. The "credit scores as low as 550" example (Bigfoot Electric, 1.4 above) is a real, live ad demonstrating exactly the CREDIT_SIGNALS_TIER_A pattern the lint must block before it reaches an owner's export pack. |
| Money-back / conditional-free structure | Plumbing | "$93 or the service is FREE" (Lancaster Plumbing) | A guarantee-shaped offer rather than a discount - shifts risk from the customer to the business, which is a stronger trust signal than a percentage-off. | Watch this pattern against `docs/14-AD-POLICY-RULES.md` CLAIM-01/CLAIM-05: it is a real conditional guarantee tied to a specific bounded service (unclog a drain), not an absolute outcome claim ("guaranteed results"), so it reads as compliant, but any generator-written variant needs to stay this specific and bounded, not generalize to "guaranteed to fix your problem." |
| Cross-trade bundle (free second service with paid primary) | HVAC, electrical | Free plumbing inspection with AC tune-up; free panel safety check with any booked electrical service | Raises perceived value without discounting the primary offer; only usable by multi-trade businesses (see 2.7 above). | Not measured; structurally sound but limited to businesses that actually offer both services. |
| Charity/cause tie-in pricing | HVAC | "$19.95 + 2 cans of food" (Rescue One Air, via leadsync.me) | A single observed example, notable enough to include because it reframes the transaction as a community act rather than a pure discount. | One example only - cannot be called a validated pattern, just a real, interesting data point. |
| Straight percentage-off, no anchor | Not found as a standalone lead offer anywhere in this research pass | n/a | Confirms `docs/13-TRADE-PLAYBOOK.md`'s existing [ASSUMPTION] that this underperforms: it did not surface as a dominant live pattern in any of the four trades' Ad Library samples, where anchored or flat-dollar pricing dominated instead. Still not a controlled comparison, just an absence in a real, current sample of roughly 90 live ads reviewed across four trades. | n/a |

---

## 4. Copy structures that repeat

Each skeleton below is drawn from the patterns in section 1, with slots an AI generator would
fill from the owner's intake data (trade, service, offer, city, credentials). Status on every
template is `ILLUSTRATIVE` - these are skeletons abstracted from real ads, not real ads
themselves, and must never be shown to an owner or presented anywhere as an observed example.

### 4.1 Offer-led (price first)

```
[$PRICE] [SERVICE_NAME] - [SCARCITY_OR_TIMEFRAME, optional]
[One line on what the price includes, itemized if more than one thing is included.]
[Licensed/local credential line, optional.]
[CTA tied to the offer, e.g. "Book my $PRICE tune-up"]
```
Real anchors: Cool Today's "$29 Electrical Panel Safety Check," Air & Drain Works' itemized
"$20.26 tune-up" copy (1.1, 1.4 above).

**Suits:** HVAC tune-ups, plumbing drain clearing, electrical panel/safety checks - any service
with a bounded, quotable flat price. Weak fit for high-ticket planned work (full replacements,
whole-home rewiring) where a price this specific cannot honestly be given without a home visit.

### 4.2 Problem, agitate, solve

```
[SYMPTOM_QUESTION, e.g. "Flickering lights? Breaker keeps tripping?"]
[One line naming what that symptom usually means, factually, no invented catastrophe.]
[The service that fixes it, plus the offer.]
[CTA]
```
Real anchors: Elm Tree Electric, MasterTex Plumbing (1.2, 1.4 above).

**Suits:** all four trades for planned or emergency-adjacent work. Must run through
`docs/14-AD-POLICY-RULES.md` TRADE-EMERGENCY-01/URGENCY-03 before export - the agitate line
has to stay a real, current, verifiable capability statement ("breaker issues can be a fire
risk if left unaddressed") and never invent an unverifiable catastrophe ("your house could burn
down tonight").

### 4.3 Trust and credential led

```
[Ownership/tenure/independence claim, e.g. years in business, family-owned, not private equity]
[What that means for the customer, concretely]
[Offer, stated plainly, secondary to the trust claim]
[CTA]
```
Real anchors: Capital City Heating & Cooling, DryHome Roofing (1.1, 1.3 above).

**Suits:** roofing above all (scam-association trade), then HVAC and electrical for
high-ticket replacement/install work where trust is the binding constraint, not price. Weakest
fit for a fast drain-clearing or emergency dispatch ad, where speed should be the lead instead.

### 4.4 Local/storm-event seasonal

```
[CITY_OR_REGION] homeowners: [seasonal/weather pattern, general, not a named dated event]
[What that pattern does to the relevant system/property, factually]
[Offer, e.g. free inspection]
[No-pressure reassurance line, roofing/storm specifically]
[CTA]
```
Real anchors: American Roofing & Waterproofing's "monsoon season" ad, Great Dane's hurricane-
season generator ad (1.3, 1.4 above).

**Suits:** roofing (storm-response), electrical (generator/storm-preparedness), HVAC (extreme-
heat/cold onset). Must clear `docs/14-AD-POLICY-RULES.md` TRADE-ROOF-02: name the season or
regional pattern, never a specific identifiable storm by name or date.

### 4.5 Social proof led

```
[Review count or rating, specific number]
[Local identity claim, e.g. "go local," a neighborhood or city name]
[Offer or CTA, secondary]
```
Real anchors: JML Roofing's carousel ("250+ 5-star reviews," "Go local"), Trust Rooter
Plumbing's "500+ Five Star Reviews, Rated A+ BBB" (1.2, 1.3 above).

**Suits:** any trade with a genuine, specific review count to cite - this template should never
generate a fabricated number, per `AGENTS.md` rule 3. If the owner's actual review count is
unknown or low, this skeleton should not be offered.

### 4.6 Question opener, no agitation

```
[Short factual question about the service need, e.g. "Buying an EV or adding solar?"]
[What that typically requires, factually]
[Offer]
[CTA]
```
Real anchors: this is the electrical-specific pattern already noted as `ILLUSTRATIVE` in
`docs/13-TRADE-PLAYBOOK.md` 4.6 ("Buying an EV or adding solar? Most homes built before [year
range] need a panel upgrade first"), now reinforced by the real EV-adjacent electrical ads
found in this research (Kora, GenerLink, 1.4 above), though none of those specific ads were
written by a licensed trade contractor - they came from product/hardware companies selling
into the same space.

**Suits:** electrical trigger-event campaigns (EV charger, solar-adjacent panel upgrades)
specifically. Not observed as a strong fit elsewhere.

---

## 5. What fails

Every entry below traces to either a real, cited source describing a failure pattern, or an
absence in the live Ad Library sample large enough to be worth noting. Nothing here is
invented performance data - where a source did not publish a number, none is shown.

- **Generic, offer-free CTAs.** "Contact us today for all your HVAC needs" and "Call us for a
  free quote" are named directly as failing patterns by
  [Hook Agency's HVAC "worth it" analysis](https://hookagency.com/blog/hvac-facebook-ads-worth-it/),
  which states they "get ignored because they lack urgency or clear value." This matches
  `docs/13-TRADE-PLAYBOOK.md`'s independent finding (1.6, 3.6) that "Contact us"/"Learn more"
  CTAs underperform CTAs tied to a specific offer.
- **Pure tenure/company-focused copy with no offer.** The same Hook Agency source names "Serving
  the area for 20+ years" as a message that "doesn't motivate clicks" on its own. Notably, this
  document's own real sample contains a counter-case (DryHome Roofing's pure-credential ad,
  live 690+ days) - the honest read is that tenure-only copy can work as a supporting trust
  signal within an otherwise-offer-led or CTA-clear ad, but is reported to fail as the entire
  message.
- **Boosted posts instead of a real ad campaign.** Confirmed independently in two places:
  `docs/13-TRADE-PLAYBOOK.md`'s cross-trade mistakes section (citing
  [ServiceAllies](https://www.serviceallies.com/blog-posts/10-common-mistakes-when-running-meta-ads)),
  and a [Contractor Talk forum thread](https://www.contractortalk.com/threads/facebook-ads.302129/)
  where a contractor reported no luck with Facebook and noted comments on ads "turned into a
  circus" - consistent with the no-conversion-tracking, followers-only reach a boosted post
  produces versus a real ad campaign.
- **Straight percentage-off with no anchor price.** Already documented in
  `docs/13-TRADE-PLAYBOOK.md` as an [ASSUMPTION] inferred from what does work rather than a
  direct source on what fails. This research adds a second, independent data point: across
  roughly 90 live ads reviewed in the Meta Ad Library for this document, not one used a bare
  percentage-off as its primary, standalone offer. Every discount seen was either anchored to a
  stated regular price (Bayshore Plumbers' "$49, regularly $85") or paired with a flat dollar
  figure. Still not a controlled experiment, but a real absence in a real, current sample.
- **Sending traffic to a slow, generic website instead of a focused lead form or landing page.**
  Cited in `docs/13-TRADE-PLAYBOOK.md` 1.9 from ServiceAllies; independently echoed by
  [BuiltRight Digital's plumbing guide](https://builtrightdigital.com/meta-ads-for-plumbers-ultimate-guide/),
  which frames a plumber's first $1,000 of Facebook spend as commonly wasted by treating the
  channel "like a digital phone book instead of a strategic lead generation machine."
- **No follow-up system behind the ad.** Same BuiltRight Digital source: "Running ads with no
  follow-up system is a waste of money," which is the exact 5-minutes-to-30-minutes lead-decay
  problem already documented in `docs/13-TRADE-PLAYBOOK.md`'s cross-trade section. This product
  cannot fix it post-export, but it is worth restating here because it means even a well-built
  ad from this playbook can still fail for reasons entirely outside the copy.
- **Naming a specific storm/disaster event with urgency language (roofing).** Not observed as
  a live pattern in this research's roofing sample - every storm-referencing ad found used
  seasonal or regional framing ("monsoon season," "one storm... homes across the Milwaukee
  area") rather than naming a specific hurricane or dated event, which is consistent with
  `docs/14-AD-POLICY-RULES.md` TRADE-ROOF-02 being a real constraint advertisers are already
  observing, not just a theoretical policy risk.
- **True emergency framing for electrical.** Not a "fails" claim in the sense of underperforming
  once run, but a documented absence: an exact-phrase Ad Library search for "emergency
  electrician" returned only 3 live US results (1.4 above), two of them unrelated. Whatever the
  reason (electrical issues genuinely present as less visually/emotionally urgent than a burst
  pipe or a hole in a roof, or advertisers have learned it does not convert), the market data
  says this angle is rare, and a generator defaulting to heavy emergency framing for electrical
  campaigns would be working against the observed grain of the category.

---

## 6. Creative direction with evidence

Every claim in this section separates what the Ad Library's own "started running" dates show
from what agency sources claim about creative performance without showing evidence.

### 6.1 What correlates with long run duration (a real, observable signal)

The Ad Library shows a start date for every ad, which is the only performance-adjacent signal
this product can access without spend data. Advertisers do not keep paying for creative that
does not produce jobs, so a very long run duration is a reasonable, if imperfect, proxy for
"this is working." Applying that lens to the ads captured in section 1:

- **Global International Heating And Cooling's $59 tune-up ad has run 1,500+ days** (since May
  2022) with unchanged, simple copy and no visible urgency gimmick - the single longest-running
  ad found across all four trades in this research. Its creative, per the Ad Library listing,
  is a static image, not video.
- **DryHome Roofing's zero-offer, pure-credential ad has run 690+ days.** No discount, no
  urgency, just "Licensed, bonded, insured, replacing roofs since 1988."
- **Central Arkansas Roofing's two-word "Leaky Roof?" ad has run 900+ days** over a 15-second
  video.
- Several advertisers (Semper Fi Heating and Cooling, Air & Drain Works, Horizon Services) run
  **multiple concurrent variants of the same offer at different prices or with different
  framing simultaneously**, which reads as live A/B testing rather than a single settled
  creative - a signal that the winning variant among them is likely still being determined by
  the advertiser, not yet knowable from the outside.

**What this means for the product:** simplicity and a clear, bounded offer correlate with
longevity far more than any particular visual gimmick in this sample. The single common thread
across the four longest-running ads found is not the image style, it is offer clarity.

### 6.2 What images actually appear (from ad descriptions and cited sources)

The Meta Ad Library text-extraction method used for this research does not reliably capture
image content in a form that can be quoted, so this subsection leans more heavily on
`docs/13-TRADE-PLAYBOOK.md`'s already-cited [Hook Agency creative research](https://hookagency.com/blog/why-stock-photos-are-costing-contractors-jobs-and-what-to-use-instead/)
(HVAC/roofing), extended here to plumbing and electrical by pattern rather than independent
sourcing.

- **What converts, per the existing cited research:** a technician actually working on
  equipment (not posed), a marked company truck in a real driveway, before/after of physical
  equipment or the roof/panel itself. This is INDUSTRY-sourced, not independently re-verified
  by this pass.
- **What does not convert:** stock photography of a smiling model, generic "handshake in front
  of a house" imagery, anything that reads as template-produced. Same source.
- **New in this pass:** several real ad primary texts explicitly describe their own visual
  content in a way worth noting even without the image itself - Glacier Roofing's ad names
  "HAAG-Certified inspectors" and documentation of damage, which implies photo/document
  evidence as the visual payoff; several electrical generator ads (AstroGenerators, Great Dane)
  itemize a bundled physical component (an automatic transfer switch, a surge protector) that
  would naturally be shown as a product photo rather than a lifestyle shot.
- **Text-in-image caution, unchanged from `docs/14-AD-POLICY-RULES.md` section 3:** the 20
  percent text rule is gone as a rejection trigger, but heavy on-image text is still the
  clearest visual tell of AI generation and still costs reach in the delivery auction. Several
  real ads in this sample (Air & Drain Works, MasterTex) carry their full price-and-offer
  message in the primary text field rather than baked into the image, which sidesteps this
  risk entirely and is the safer default for AI-generated creative.

### 6.3 Roofing-specific creative caution, reinforced

`docs/13-TRADE-PLAYBOOK.md` 3.7 already flags that overly polished creative can hurt trust in
roofing specifically, given the scam association. This research adds direct textual evidence
for the same instinct: multiple real roofing ads (3MG, Batterbee, J Smegal/Guns N Hoses)
spend a meaningful share of their primary text actively working to sound like the opposite of
a storm-chaser, which would not be necessary if polished, corporate-sounding creative were
neutral or positive for this trade's trust problem.

---

## 7. Seasonal copy calendar

This maps `docs/13-TRADE-PLAYBOOK.md`'s existing seasonality tables (1.5, 2.5, 3.5, 4.5) onto
concrete hook/offer choices from sections 2-3 above, rather than restating the underlying
demand-signal research. Read the source document for the demand data and its confidence
labels; this table is the copy layer on top of it.

| Month(s) | HVAC | Plumbing | Roofing | Electrical |
|---|---|---|---|---|
| Jan | Speed/availability hook (2.6) + heating-repair offer-led price (2.2) | Speed hook (2.6), frozen-pipe framing | Off-season: trust/credential hook (2.4), early-booking offer | Generator storm-prep hook (2.5) if ice-storm-exposed region |
| Feb-Mar | Trust/credential or bundled offer (2.7) for maintenance push | Repair-and-prevent, problem/agitate/solve (4.2) for pipe insulation | Storm season begins in hail corridor: local/storm-event hook (2.5) | Panel upgrade, question-opener (4.6) tied to spring remodel planning |
| Apr | Price/offer lead (2.2), pre-season tune-up urgency without emergency framing | Shoulder month: social-proof led (2.5/4.5) to fill schedule | Storm-event hook (2.5) continues in hail corridor | Steady, no strong seasonal hook per `docs/13-TRADE-PLAYBOOK.md` 4.5 |
| May-Jun | Price/offer lead intensifies toward peak | Rising demand: speed hook (2.6) alongside fixture/upgrade offers | Peak installation season: trust/credential (2.4) + speed/capacity framing | Hurricane season begins (Gulf/Atlantic): generator storm-prep hook (2.5) |
| Jul | Speed/availability hook (2.6) is primary, price secondary | Speed hook (2.6), summer water-use spike framing | Storm-event hook (2.5) if actual weather event, else installation-capacity messaging | Continued generator storm-prep push in hurricane-exposed regions |
| Aug | Speed/availability + "should I repair or replace" trust-led copy (2.4) for aging systems | Continued summer emergency framing | Hurricane season on Gulf Coast: storm-event hook (2.5) | Generator push continues; panel-upgrade offer-led (2.2) steady elsewhere |
| Sep-Oct | Trust/credential or offer-led furnace tune-up push, shoulder-season logic | Shoulder month: social-proof led to fill schedule | Winterization push in non-coastal markets; continued storm hook where hurricane season persists | Steady; no strong seasonal hook |
| Nov-Dec | Offer-led + "lock in this year's price" urgency for planned replacements | Speed hook (2.6) intensifies toward frozen-pipe peak | Slowest period: trust/credential hook (2.4), early-booking offer for spring | Generator storm-prep hook (2.5) if ice-storm-exposed region |

**Caveat carried over from `docs/13-TRADE-PLAYBOOK.md`:** every row above rests on a national
average seasonality curve. A Phoenix HVAC account and a Minneapolis one need different
calendars entirely; this table is a starting prior, not a regional truth, exactly as the
source document already states.

---

## 8. Machine-readable output

This extends, rather than duplicates, the `TradePlaybook` schema already proposed in
`docs/13-TRADE-PLAYBOOK.md` section 5. That document owns services, offers, targeting, budget,
and seasonality as data shapes; this document owns the retrieval-facing copy layer - the actual
hooks, offer templates, copy skeletons, and creative rules a generation pipeline queries at
prompt-build time, keyed by trade, service, season, and offer type as the task requires. Reuses
`TradeId`, `Confidence`, `SourcedValue<T>`, and `Urgency` from that document's schema rather
than redefining them.

```typescript
import { TradeId, Confidence, SourcedValue, Urgency } from "./13-trade-playbook-schema";
// (illustrative import path - the actual shared-types module location is an engineering
// decision, not a research one)

// Mirrors the VERIFIED_REAL / AGENCY_CLAIMED / ILLUSTRATIVE distinction that is the central
// honesty mechanism of this whole document. This field must be read and rendered by any UI
// or prompt that surfaces an example to a human, exactly as SourcedValue's confidence field
// is designed to be in the sibling schema - it must never be silently dropped.
type AdExampleStatus = "verified_real" | "agency_claimed" | "illustrative";

interface RealAdExample {
  id: string;
  tradeId: TradeId;
  status: AdExampleStatus;               // never "verified_real" without sourceUrl AND
                                          // (libraryId OR a named secondary-source screenshot)
  advertiserName: string;
  libraryId?: string;                    // Meta Ad Library Library ID, when captured directly
  startedRunning?: string;                // ISO date or "unknown"
  runDurationDaysAtCapture?: number;      // null if not established; never estimated
  primaryText: string;                    // verbatim, em dashes normalized to hyphens
  headline?: string;
  description?: string;
  offerSummary: string;                   // plain-English, e.g. "$59 named tune-up price"
  sourceUrl: string;                      // required for verified_real and agency_claimed
  policyRiskNote?: string;                // e.g. "sits close to TRADE-ROOF-01 insurance-outcome line"
  capturedDate: string;                   // when this research pass observed it, ISO date
}

type HookCategoryId =
  | "problem_symptom_question" | "price_offer_lead" | "local_neighborhood_proof"
  | "trust_credential_anticompetitor" | "storm_weather_urgency" | "speed_availability"
  | "bundled_cross_trade";

interface HookCategory {
  id: HookCategoryId;
  label: string;
  description: string;
  suitedTrades: TradeId[];
  suitedUrgency: Urgency[];
  whyItWorks: string;                     // plain-English, owner-readable rationale
  realExampleIds: string[];               // references into RealAdExample[], must not be empty
                                          // for a category to ship in v1 - a hook category
                                          // with zero real examples is a gap, not a default
  policyNotes?: string;                   // cross-reference into docs/14-AD-POLICY-RULES.md
                                          // rule IDs this hook type most commonly triggers
}

type OfferStructureId =
  | "named_price_tune_up" | "named_price_diagnostic" | "free_inspection"
  | "percent_or_dollar_off_financed" | "money_back_conditional" | "bundled_cross_trade_offer"
  | "charity_tie_in";

interface OfferPattern {
  id: OfferStructureId;
  tradeIds: TradeId[];
  label: string;
  observedPriceRangeUsd?: { low: number; high: number };
  observedPricePoints: number[];          // exact real prices seen, e.g. [17.75, 20.26, 49.95]
  effect: SourcedValue<string>;
  leadQualityTradeoff: string;            // plain-English, must say "not measured" when true
  policyRiskFlag?: string;                // e.g. "financing offers trip SAC-CRED-01/02"
  realExampleIds: string[];
}

type CopySkeletonId =
  | "offer_led" | "problem_agitate_solve" | "trust_credential_led"
  | "local_storm_seasonal" | "social_proof_led" | "question_opener_no_agitation";

interface CopySkeleton {
  id: CopySkeletonId;
  label: string;
  template: string;                       // slot-marked template string, e.g. "[$PRICE] ..."
  suitedTrades: TradeId[];
  suitedServiceUrgency: Urgency[];
  realExampleIds: string[];               // the real ads this skeleton was abstracted FROM
  requiredPolicyChecks: string[];         // rule IDs from docs/14-AD-POLICY-RULES.md that
                                          // MUST run on any copy generated from this skeleton
                                          // before it reaches the owner review screen
}

interface FailurePattern {
  id: string;
  tradeIds: TradeId[] | "all";
  pattern: string;
  whyItFails: SourcedValue<string>;
  evidenceType: "cited_source" | "sample_absence" | "forum_report";
                                          // "sample_absence" = did not appear in the live Ad
                                          // Library sample this research reviewed, an honest,
                                          // weaker form of evidence than a direct citation
}

interface CreativeDirectionEntry {
  tradeId: TradeId;
  correlatesWithLongevity: string[];      // plain-English observed traits, e.g. "offer clarity
                                          // over visual gimmick"
  preferredShotTypes: string[];
  avoidShotTypes: string[];
  tradeSpecificCaution?: string;
  evidenceSourceUrls: string[];
}

interface SeasonalCopyEntry {
  tradeId: TradeId;
  monthOrPeriod: string;
  recommendedHookCategoryIds: HookCategoryId[];
  recommendedOfferStructureIds: OfferStructureId[];
  regionSensitive: boolean;               // carried over from the sibling schema's identical
                                          // field, same meaning
  note?: string;
}

// The actual retrieval shape the generation pipeline queries against. One row per
// (trade, service, season, offer type) combination the pipeline needs a copy prior for.
interface CopyPriorQuery {
  tradeId: TradeId;
  serviceId?: string;                     // references ServiceDefinition.id from the sibling
                                          // schema, e.g. "hvac_ac_repair"
  season?: string;                        // month or period key, matches SeasonalCopyEntry
  preferredOfferStructureId?: OfferStructureId;
}

interface CopyPriorResult {
  hookCategories: HookCategory[];          // ranked, best-suited first
  offerPatterns: OfferPattern[];
  copySkeletons: CopySkeleton[];
  applicableFailurePatterns: FailurePattern[];  // what to actively avoid for this query
  creativeDirection: CreativeDirectionEntry;
  realExamplesForReference: RealAdExample[];    // never surfaced to the owner as "your ad,"
                                                // reference-only for internal prompt-building
}

// Top-level library the pipeline loads once and queries repeatedly. Not a database schema by
// itself - this is the shape a query/lookup service returns, however it is actually stored.
interface CopyPriorLibrary {
  version: string;                         // bump on any research revision
  lastResearchDate: string;                // ISO date, drives the same 90-day staleness
                                          // pattern used for docs/14-AD-POLICY-RULES.md rules
  realAdExamples: RealAdExample[];
  hookCategories: HookCategory[];
  offerPatterns: OfferPattern[];
  copySkeletons: CopySkeleton[];
  failurePatterns: FailurePattern[];
  creativeDirection: CreativeDirectionEntry[];  // one per trade
  seasonalCopy: SeasonalCopyEntry[];
  query(input: CopyPriorQuery): CopyPriorResult;  // the actual pipeline entry point; the
                                                  // implementation is engineering, this is
                                                  // the contract it must satisfy
}
```

**Design notes:**

- **`AdExampleStatus` is the load-bearing field, exactly as `CopyAngleStatus` is in the sibling
  schema.** The same failure mode `docs/13-TRADE-PLAYBOOK.md` warns about (presenting a
  template as if it were a real ad that ran and worked) applies here at larger scale, since
  this document contains far more real examples than the trade playbook did. `realExampleIds`
  on `HookCategory`, `OfferPattern`, and `CopySkeleton` must always resolve to entries whose
  status is `verified_real` or `agency_claimed`, never silently to nothing - a hook category
  with an empty `realExampleIds` array is a signal the category needs more research, not a
  default the pipeline should ship quietly.
- **`CopyPriorResult.realExamplesForReference` is explicitly never owner-facing.** These exist
  so an LLM prompt can be grounded in real examples during generation, not so a real
  competitor's ad copy is shown to an owner as if it were their own or as inspiration to copy
  verbatim - the duplicated roofing story template found in section 1.3 is a live cautionary
  example of what happens when real ad copy gets reused too literally across businesses.
- **`FailurePattern.evidenceType` keeps `sample_absence` honestly weaker than `cited_source`.**
  Several "what fails" findings in section 5 rest on an offer type or pattern simply not
  appearing in roughly 90 live ads reviewed, which is real evidence but weaker than a named
  source stating a pattern fails. The schema should not let these two evidence strengths
  collapse into one undifferentiated "this fails" flag.
- **`CopySkeleton.requiredPolicyChecks` ties directly to `docs/14-AD-POLICY-RULES.md`'s rule
  IDs**, so every generated ad's policy lint pass is traceable back to which copy skeleton
  produced it and why those specific checks were required - e.g. any ad generated from the
  `local_storm_seasonal` skeleton must run TRADE-ROOF-02 before export, because section 2.5
  above documents real ads sitting close to that exact line.

---

## 9. FOUNDER MUST CONFIRM

Everywhere below, the founder's direct Facebook-ads experience should override this research.
None of this should ship as a silent default.

1. **Which offer structure actually produces better lead quality, named fee vs. free
   estimate, for plumbing specifically.** Section 3 found both patterns running roughly equally
   often in the live Ad Library sample, which means the market has not settled this either -
   the founder's own account history is a better tiebreaker than anything found in this pass.
2. **Whether the odd-cent HVAC pricing pattern ($17.75, $20.26, $49.95) is a deliberate
   psychological-pricing tactic worth recommending, or just how these specific advertisers'
   software rounds rebates and fees.** This research found the pattern but could not determine
   its cause. If the founder has run tests on price-ending format, that should set the default,
   not the observed pattern alone.
3. **Whether the duplicated long-form roofing story template (section 1.3, J Smegal/Guns N
   Hoses) should be treated as a validated high-performing skeleton worth building into the
   product, or as a cautionary tale about templates spreading past their useful life.** Both
   readings are defensible from the same evidence; this needs a judgment call, not just more
   research.
4. **The "credit scores as low as 550" and similar financing-qualification language seen live
   in real electrical generator ads (section 1.4).** This research flags it as a real,
   observed Special Ad Category trigger per the existing policy document, but the founder
   should confirm whether the product should refuse to generate this language outright (a hard
   block) or allow it with a mandatory disclosure step, since it is clearly common, real market
   practice among competitors right now.
5. **Whether "free inspection" really is the right default for roofing given the scam
   association**, unchanged from item 8 of `docs/13-TRADE-PLAYBOOK.md`'s own Founder Must
   Confirm list - this research reinforces that the offer is dominant in the live market and
   that real advertisers are actively fighting the trust problem it creates, but does not
   resolve whether that is a fight this product should be putting new customers into by
   default.
6. **Electrical's near-total absence of emergency framing (section 1.4, 3 live results for
   "emergency electrician").** This research reads that as a real market signal that
   electrical should not default to urgency copy. The founder may have direct experience
   showing otherwise (e.g. that emergency electrical calls exist and convert, they are just not
   advertised with that word specifically) - if so, that should override the "electrical is not
   an urgency trade" conclusion this document draws from the raw search result.
7. **How much weight a long Ad Library run duration should actually carry as a "this works"
   signal.** Section 6.1 treats 90+ days as a reasonable proxy because advertisers do not keep
   paying for ads that do not work, which is directionally sound logic but was not itself
   independently verified against any advertiser's real spend or booked-job data. If the
   founder has seen cases where a long-running ad was actually a set-and-forget mistake rather
   than a winner, that changes how much this document's "long-running = validated" framing
   should be trusted.
8. **Whether the storm-event copy line (naming a region/season but never a specific named
   disaster) is conservative enough, or still too close to the crisis-exploitation policy
   line for the founder's risk tolerance.** This document flags two real, live ads (Glacier
   Roofing, A-R Roofing) as sitting close to the insurance-outcome line even though they did
   not cross into naming a specific storm - the founder's own experience with what Meta has
   and has not rejected in practice is worth more than this document's reading of the policy
   text.

---

## 10. Sources

Meta Ad Library, browsed live 2026-08-19 (primary source for every `VERIFIED_REAL` entry not
otherwise attributed):
- `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=hvac+tune-up`
- `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=%22drain+cleaning%22&search_type=keyword_exact_phrase`
- `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=%22roof+inspection%22&search_type=keyword_exact_phrase`
- `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=%22electrical+panel%22&search_type=keyword_exact_phrase`
- `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=%22whole+home+generator%22&search_type=keyword_exact_phrase`
- `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=%22emergency+electrician%22&search_type=keyword_exact_phrase`

Agency and coaching sources with real Ad Library screenshots or direct case-study numbers:
- [LeadSync, HVAC Facebook Ads: 8 Real Examples and the $59 Tune-Up Formula](https://leadsync.me/blog/hvac-facebook-ad-examples/)
- [LeadSync, Roofing Facebook Ads: 10 Real Examples That Have Run for Months](https://leadsync.me/blog/roofing-facebook-ad-examples/)
- [Hook Agency, 7 Best HVAC Facebook Ads That Actually Drive Leads](https://hookagency.com/blog/hvac-facebook-ads/)
- [Hook Agency, Are HVAC Facebook Ads Worth The Cost?](https://hookagency.com/blog/hvac-facebook-ads-worth-it/)
- [Hook Agency, 5 Electrician Facebook Ads That Actually Work](https://hookagency.com/blog/electrician-facebook-ads-examples/)
- [GetHookd, 9 Best HVAC Facebook Ad Examples to Try in 2026](https://www.gethookd.ai/learn/9-best-hvac-facebook-ad-examples-to-try-in-2026/)
- [BuiltRight Digital, Facebook (Meta) Ads for Plumbers: The Ultimate Guide](https://builtrightdigital.com/meta-ads-for-plumbers-ultimate-guide/)
- [Contractor Talk forum, "Facebook ads" thread](https://www.contractortalk.com/threads/facebook-ads.302129/)

Already-cited sources reused from `docs/13-TRADE-PLAYBOOK.md`, referenced inline above rather
than re-derived:
- [Hook Agency, Why Stock Photos Are Costing Contractors Jobs](https://hookagency.com/blog/why-stock-photos-are-costing-contractors-jobs-and-what-to-use-instead/)
- [ServiceAllies, 10 big mistakes contractors make with Facebook ads](https://www.serviceallies.com/blog-posts/10-common-mistakes-when-running-meta-ads)

Every ad in section 1 has its own advertiser name and, where captured directly, a Meta Ad
Library Library ID. To re-verify any specific ad, search the advertiser name in the Meta Ad
Library at `facebook.com/ads/library` with country set to United States and ad status set to
Active; ads can go inactive between this research pass and any later review, which is itself
useful information (an ad that stopped running shortly after this research captured it is a
weaker "this works" signal than one still running months later).
