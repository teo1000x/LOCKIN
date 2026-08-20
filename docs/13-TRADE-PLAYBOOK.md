# Trade Playbook - v1

The per-trade knowledge base that drives every smart default and copy prior in the ad
generator. This is the core intellectual property of the product. Everything downstream -
targeting, budget, lead form, seasonality, copy, creative direction - is derived from this
document, never asked of the owner. Per the product spec and `AGENTS.md` rule 5, a default
with no reasoning behind it is a bug, so every entry below carries a plain-English reason a
non-technical trades owner could read and accept.

Four trades in v1: HVAC, plumbing, roofing, electrical.

## How this document was built, and its real status

This document is **research, not operational truth**. The founder has personally run Facebook
and Google ads for these trades and will supply his own playbook from direct experience. This
document bootstraps a first draft so the generation pipeline has something to run against
before that conversation happens. It does not replace him, and several entries below are
flagged for exactly that reason in the "Founder Must Confirm" section at the end.

### Confidence legend, applied to every number

- **[VERIFIED]** - Cross-checked against `research/04-domain-and-economics.md`, which itself
  cites Google Local Services Ads program data, WordStream, or comparable named-source
  benchmark aggregators. Still a benchmark, not a controlled experiment, but multiply-sourced.
- **[INDUSTRY]** - Sourced to a single marketing-agency blog, SEO content site, or vendor
  case study published in 2025-2026. Directionally useful, written by people who sell services
  to these trades and have a incentive to sound authoritative. Treat as an informed opinion,
  not a fact. Cited inline with a URL.
- **[ASSUMPTION]** - No source found in this research pass. Founder judgment call. Listed
  explicitly in "Founder Must Confirm."

Where sources disagree with each other, both figures are shown and the disagreement is
flagged rather than silently averaged.

---

## Cross-trade notes that apply to all four

### Meta targeting in 2026: what still matters vs. what is theatre

Meta made Advantage+ detailed targeting the default for new campaigns, and as of February
2026 interest selections are treated as suggestions rather than hard constraints. Meta also
removed dozens of detailed interest categories on January 15, 2026, so the old practice of
stacking 5-10 specific interests no longer does what it used to do. Meta's own reporting
claims Advantage+ cuts CPA up to 32% in ecommerce and that manual interest stacking
underperforms Andromeda (Meta's ad-ranking model) for cold lead generation in most
categories once an account has enough conversion data. **[INDUSTRY]**
([conversios.io](https://www.conversios.io/blog/meta-advantage-audience-vs-detailed-targeting-2026-guide/),
[adligator.com](https://adligator.com/blog/meta-broad-targeting-advantage-plus-audiences-2026))

The exception: manual detailed targeting reportedly still outperforms Advantage+ for accounts
with fewer than 50 weekly conversions, budgets under $30/day, or very niche/hyper-local
campaigns, because the algorithm does not have enough data to learn from. **[INDUSTRY]**
(same sources above)

**What this means for the product's defaults:**
- Geographic radius targeting is real and load-bearing for all four trades. It is not theatre.
- Broad "homeowner" interest/behavior targeting is worth setting as a *floor*, not a precision
  instrument, because Meta will expand past it anyway once the campaign has enough data.
- Every account we generate for starts cold (zero conversion history), which is exactly the
  regime where the research above says manual targeting still helps. So the defaults should
  set a real geographic radius, a real homeowner-likelihood signal, and a conservative age
  band, then let Advantage+ expand from there rather than fighting it once volume builds.
- Meta restricted credit-score-based targeting in September 2025; income-band targeting still
  exists and is the closest present-day substitute for a financial qualification signal.
  **[INDUSTRY]** ([baadigi.com](https://www.baadigi.com/blog/facebook-ads-for-contractors-complete-2026-guide-to-generating-quality-leads))
- One claim found repeatedly in trade-specific blogs - targeting homes built in specific year
  ranges (e.g. 1978-1995 for polybutylene plumbing, 1965-1973 for aluminum wiring) - is **not
  a native Meta Ads Manager targeting field** as far as this research could confirm. Native
  Detailed Targeting does not expose "year home was built." This is either referring to a
  third-party data overlay/custom audience upload the blog authors have access to and we do
  not, or it is simply inaccurate content written to rank in search. **Do not build this into
  the schema as a real targeting lever without founder or engineering verification that it is
  reachable through standard Ads Manager.** Flagged in Founder Must Confirm.

### Meta ad policy note relevant to creative direction

The product's own policy pre-flight lint (per `docs/01-PRODUCT-SPEC.md`) bans "before/after
imagery for aesthetics." That rule targets Meta's Personal Attributes and body-image policies
(weight loss, cosmetic procedures). It does not restrict before/after imagery of *property or
equipment* (a storm-damaged roof next to a finished one, a rusted panel next to a new one),
which is standard and permitted trade creative. The lint rule needs a scope condition so it
does not false-positive on legitimate trade before/after shots.

### Lead form length, generally

Across sources, the sweet spot beyond name/phone/email is **2-3 qualifying questions**, not
more. Facebook Lead Ads convert at 8-12% of people who open the form vs. 2-4% for a landing
page, but lead-to-appointment rate is lower (15-30% vs. 30-50% for landing-page leads) because
Lead Ads make it too easy to submit with low intent. **[INDUSTRY]**
([clicksgeek.com](https://clicksgeek.com/hvac-facebook-advertising/)) This is the central
tension the qualifying questions exist to resolve: more friction filters junk but also cuts
volume, and the 2-3 question range is where most practitioner sources converge as the balance
point.

### The single most common owner mistake, across all four trades

Two things came up independently across nearly every source: (1) setting one big radius (e.g.
25 miles) around a "homeowners" audience with no other filter, which the estimate below shows
can put 85%+ of ad spend in front of people who will never call **[INDUSTRY]**
([hookagency.com](https://hookagency.com/blog/facebook-ad-mistakes/)); and (2) slow lead
follow-up - a Facebook lead is described as "hot" for about 5 minutes, and the odds of
connecting drop roughly 80% after 30 minutes **[INDUSTRY]** (same source). The product cannot
fix problem 2 (we do not touch leads post-export, per the pivot), but the export pack's
instructions should say this plainly, because it is a real, correctable behavior. Problem 1 is
exactly what the targeting defaults in this document exist to prevent.

---

## 1. HVAC

### 1.1 Service taxonomy

| Service | Urgency | Typical ticket | Confidence |
|---|---|---|---|
| AC repair | Emergency | $150-$600 per repair; blended repair avg ~$1,205 in 2025 (includes larger repairs) | [VERIFIED] (research/04, [builtontenth.com](https://www.builtontenth.com/hvac-research/hvac-average-ticket-size-by-job-type)) |
| Furnace/heating repair | Emergency | $150-$600 typical repair | [ASSUMPTION], scaled from AC repair pattern |
| AC replacement | Planned (but often triggered by a failed emergency repair) | $6,000-$12,000+ | [ASSUMPTION], scaled from blended replacement figure below |
| Furnace replacement | Planned | $4,000-$9,000 | [ASSUMPTION] |
| Full system replacement (AC + furnace) | Planned | $11,600-$14,100 | [VERIFIED] (research/04, [sequoiageo.com](https://www.sequoiageo.com/hvac-statistics)) |
| Heat pump install | Planned | $8,000-$16,000 | [ASSUMPTION], directionally above single-system replacement |
| Duct cleaning | Planned, low urgency | $300-$700 | [ASSUMPTION] |
| Maintenance plan / tune-up | Planned, low urgency, recurring | $79-$150 per visit, or $10-$25/mo on a plan | [INDUSTRY] ([actglobalmarketing.com](https://actglobalmarketing.com/hvac-facebook-ad-examples/) cites $79; industry norm for plan pricing is an assumption) |

**Reasoning the owner reads:** "AC repair and furnace repair are treated as emergencies
because the customer is uncomfortable or unsafe right now and will call whoever answers
first. Replacement and maintenance are planned because the customer has days or weeks to
decide, so the ad can sell trust and price instead of speed."

### 1.2 Offers

| Offer | Effect | Confidence |
|---|---|---|
| $79-$89 tune-up special (named, with a "reg. $129-149" anchor and an expiration date) | Drives volume and low cost per lead, but the raw lead is low-margin on its own. Works as a business model only when the tech is trained to inspect for and quote bigger repairs on the same visit. Treated as a loss-leader, not a profit center. | [INDUSTRY] ([actglobalmarketing.com](https://actglobalmarketing.com/hvac-facebook-ad-examples/), [serviceallies.com](https://www.serviceallies.com/blog-posts/25-ideas-for-hvac-promotions)) |
| Free AC inspection for new movers | Targets a real trigger event (moving in = unknown system history) rather than a generic discount, which tends to produce a higher-intent lead than a blanket "free inspection" | [INDUSTRY] (actglobalmarketing.com example headline) |
| Financing framed as "$89/month" for a new system | Converts high-ticket replacement into an affordable-sounding monthly number, which is the standard framing for $6K+ purchases in this vertical | [INDUSTRY] (actglobalmarketing.com example) |
| Straight percentage-off ("20% off any repair") | Generally the weakest performer in trade advertising across sources - it is vague, has no anchor price, and does not give the reader a reason to believe the discount is real. Best avoided as a primary offer. | [ASSUMPTION], consistent with the "specific pricing beats vague discounts" pattern found across every trade's sources |
| Fully free diagnostic/service call with no minimum | Attracts the most volume and the most tire-kickers. Without a small fee or a stated minimum, expect a meaningfully higher no-show and price-shopper rate. | [ASSUMPTION], by analogy to plumbing's diagnostic-fee finding below, not independently verified for HVAC |

### 1.3 Targeting defaults, with reasoning

| Parameter | Default | Reasoning |
|---|---|---|
| Service radius | 15-25 miles in a metro; up to 30-40 miles in a rural/exurban market | An HVAC tech in a truck can reasonably reach 15-25 miles in a metro without eating the day in traffic; rural areas have fewer competitors and lower population density, so the radius has to widen to reach enough households. **[INDUSTRY]** ([leadenforce.com](https://leadenforce.com/blog/the-hvac-facebook-ad-formula-for-local-success), [transcendgtm.com](https://transcendgtm.com/blog/the-ultimate-2025-guide-to-facebook-ads-for-hvac-contractors)) |
| Age | 30-65 baseline; skew 35-65 for replacement/heat pump campaigns | This age band owns homes and has the income for a $6K+ purchase; younger renters are the segment most likely to see the ad and never be able to book the job. **[INDUSTRY]** ([baadigi.com](https://www.baadigi.com/blog/facebook-ads-for-contractors-complete-2026-guide-to-generating-quality-leads)) |
| Gender | No exclusion | No source found justifying a gender skew for HVAC purchase decisions; excluding a gender would be pure guesswork. **[ASSUMPTION]** |
| Homeowner vs. renter | Homeowner-likely signal on, not a hard filter | Renters do not choose or pay for HVAC replacement in nearly all cases, so this is one of the highest-value filters available; but Meta's homeowner signal is probabilistic, not verified, so it should narrow the pool, not exclude anyone outright. **[ASSUMPTION]** on the mechanism, **[INDUSTRY]** on renters being a poor fit for the trade generally |
| Interest targeting | Light layer only: home improvement / property ownership interests, as a floor, not the whole targeting strategy | Given Meta's 2026 shift toward Advantage+ suggestions over hard constraints, stacking many interests is closer to theatre than it used to be. A light layer still helps a cold account with zero conversion history, which is the state every new campaign in this product starts in. **[INDUSTRY]** (see cross-trade section above) |
| Emergency vs. planned split | Separate ad sets/creative for emergency repair vs. planned replacement, same radius | The two customer types make the decision on completely different timelines and respond to different offers (speed vs. price/trust), so collapsing them into one ad set wastes spend showing the wrong pitch to the wrong intent. **[ASSUMPTION]**, consistent with the taxonomy split in 1.1 |

### 1.4 Budget guidance

- **Daily minimum for the algorithm to learn:** Sources disagree meaningfully. `research/04`
  section 7 puts Meta's practical daily floor around $20-50/day. Newer 2026-dated blogs put
  the *practical* local-business floor at $50-100/day, and offer a formula: (target CPA x 50
  conversions) / 7 days = minimum daily budget per ad set, since Meta's delivery system wants
  roughly 50 conversion events per week to exit the learning phase. **[VERIFIED]** for the
  lower end (research/04), **[INDUSTRY]** for the higher end
  ([adsgo.ai](https://www.adsgo.ai/blog/meta-ads-learning-phase-budget-how-much-to-spend/),
  [get-ryze.ai](https://www.get-ryze.ai/blog/meta-ads-minimum-budget-guide-starting-budget)).
  **This range needs the founder's real number**, since it directly sets the floor warning the
  product shows the owner. See Founder Must Confirm.
- **Realistic monthly range:** $1,000-$3,000/mo for a starter account, $2,500-$7,500/mo in a
  competitive metro. **[VERIFIED]** (research/04)
- **Expected cost per lead:** LSA benchmark $51/lead (Feb 2026) **[VERIFIED]**. Meta-specific
  blended CPL estimate for 2026 is $45, with tune-up leads at $35-65, maintenance inquiries at
  $40-80, and replacement leads at $80-150. **[INDUSTRY]**
  ([webtonic.io](https://www.webtonic.io/blog/hvac-facebook-ads-statistics)). One agency case
  study reports $22-45 CPL depending on creative format (video reels cheapest, static image
  ads most expensive), which is directionally consistent but is a single account, not a
  category average. **[INDUSTRY]** ([actglobalmarketing.com](https://actglobalmarketing.com/hvac-facebook-ad-examples/))
- **How budget should scale with radius and population:** Wider radius means more households
  in the audience, which means the same daily budget buys fewer impressions per household and
  takes longer to accumulate the ~50 weekly conversions needed to exit the learning phase.
  Recommended rule: budget should scale roughly with the *population inside the radius*, not
  the radius in miles alone - a 15-mile radius around a dense suburb and a 35-mile radius
  around a small town can contain a similar number of households, and should get a similar
  budget. **[ASSUMPTION]**, this is sound media-buying logic but was not found stated
  explicitly in any source for this trade; flag for founder validation since it is a real
  input to the budget-recommendation algorithm.

### 1.5 Seasonality

| Month(s) | Demand signal | What the ad should say |
|---|---|---|
| Jan | Furnace/heating repair searches peak, +137% vs. baseline | Emergency heating repair, speed and availability framing ("heat out? we're on our way") |
| Feb-Mar | Heating demand tapering, cooling searches not yet started | Maintenance plan and duct cleaning push - fill the schedule gap before the cooling season starts |
| Apr | Cooling-related search volume starts rising | Early AC tune-up ("book before it's 95 degrees and everyone else is"), pre-season urgency without emergency framing |
| May-Jun | Cooling demand ramping toward peak | Tune-up push transitions to repair/replacement readiness messaging |
| Jul | AC repair searches peak, +266% vs. baseline; emergency AC repair up ~400% vs. late-fall low | Pure emergency framing - speed, same-day, "we're 30 minutes away" |
| Aug | Continued high AC demand, replacement conversations common (end-of-life systems failing under peak load) | Emergency repair alongside "should I repair or replace" replacement offers |
| Sep-Oct | Heating-focused search volume begins climbing | Furnace tune-up and inspection push, same shoulder-season logic as spring |
| Nov-Dec | Heating demand building toward January peak | Furnace repair and replacement, plus "lock in this year's price" urgency framing for planned replacements before winter |

**[INDUSTRY]**, syndicated seasonal-search data
([abc17news.com / Stacker](https://abc17news.com/stacker-small-business/2026/02/23/seasonal-search-shifts-in-home-services-demand-what-spikes-when-and-how-to-stay-booked-year-round/),
[webfx.com](https://www.webfx.com/blog/home-services/seasonal-search-trends/)). This is a
national average curve; it should be treated as a starting prior, not the true curve for
every climate zone (a Phoenix account's "AC season" and a Minneapolis account's "furnace
season" are each far larger shares of the year than this table implies). Regional climate
adjustment is listed in Founder Must Confirm and in the schema below as an open field.

### 1.6 Copy angles

**Works:**
- **Speed/emergency framing.** "AC Not Cooling? We're 30 Minutes Away." Direct, specific,
  answers the one question the reader has (how fast can you get here). Real example.
  **[INDUSTRY]** ([actglobalmarketing.com](https://actglobalmarketing.com/hvac-facebook-ad-examples/))
- **Named, anchored price offers.** "$79 Summer AC Tune-Up - Limited Slots." Specific number,
  specific scarcity, no vague "great deals." Real example, same source.
- **Local credential/face framing.** "Hi, I'm Mike - 15 Years Fixing Florida ACs." Puts a real
  person and a real local claim in front of the reader instead of a faceless company name.
  Real example, same source.
- **Loss-framed education.** "This Mistake Raises Your AC Bill 30%." Curiosity plus a concrete
  number performs better than generic "we're the best HVAC company" copy. Real example, same
  source.
- **Trigger-event targeting.** "Just Moved? Free AC Inspection." Ties the offer to a real life
  event instead of a generic discount. Real example, same source.

**Fails, consistently, across sources:**
- Generic "we're the best" / "quality service you can trust" copy with no number, no name, no
  urgency. **[ASSUMPTION]**, inferred from the consistent pattern of what *does* work (always
  specific) rather than a direct citation of failure data.
- "Contact us" / "Learn more" CTAs instead of an action tied to the offer ("Get my $79
  tune-up," "See if I qualify"). **[INDUSTRY]** (jobnimbus.com roofing article, same finding
  applies to HVAC by pattern)
- Straight percentage-off with no anchor price, per 1.2 above.

**Illustrative primary text template** (built to the voice pattern above, not an observed
real ad, since none was found in the research for this exact field):
> "It's 95 degrees and your AC picked today to quit. We're a local Orlando crew, 15 years in
> business, and we answer the phone. $79 gets you a same-day inspection - if it's a simple
> fix, most jobs are done same visit."

### 1.7 Creative direction

- **What converts:** a technician actually working on a unit (hands on the equipment, not
  posed), a marked company truck in a real driveway, and before/after shots of physical
  equipment (old rusted unit next to new install). Real, slightly imperfect photos
  consistently beat polished studio shots in controlled tests cited across sources.
  **[INDUSTRY]** ([hookagency.com](https://hookagency.com/blog/why-stock-photos-are-costing-contractors-jobs-and-what-to-use-instead/))
- **What does not convert:** stock photography of a smiling model in a hard hat, generic
  "customer service handshake" images, and anything that looks like it came from a template -
  homeowners have seen these thousands of times and their brain filters them out in
  milliseconds. **[INDUSTRY]**, same source.
- **Generated-image fallback rule:** when the owner has no real photos, AI-generated creative
  should still aim for the *texture* of a real photo (visible equipment, a real-looking
  residential setting, a technician mid-task) rather than a glossy hero shot. The goal is to
  not look like stock, even when it is not a real photo either.
- **Video note:** case-study data (single account, not a category benchmark) reported video
  reels as the cheapest-CPL creative format, ahead of carousel and static image ads.
  **[INDUSTRY]** ([actglobalmarketing.com](https://actglobalmarketing.com/hvac-facebook-ad-examples/)).
  Worth a v2 consideration; v1 image-only generation cannot act on this yet.

### 1.8 Lead form qualifying questions

Recommended fields beyond name/phone/email (cap at 2-3 per the cross-trade note):
1. "What do you need help with?" - AC repair / heating repair / new system quote / maintenance
   (routes urgency and lets the owner triage before calling back)
2. "How old is your current system?" - filters real replacement intent from casual browsers
3. "Are you the homeowner?" - Yes/No, removes renters and non-decision-makers who cannot
   authorize the work

**[INDUSTRY]**, converged pattern across multiple sources
([clicksgeek.com](https://clicksgeek.com/hvac-facebook-advertising/)). Do not add a fourth
qualifying question; sources are consistent that completion rate drops meaningfully past two.

### 1.9 Common owner mistakes this product should prevent by default

- Running one ad set with a wide radius and generic "homeowner" targeting and no split
  between emergency and planned intent (see 1.3 reasoning).
- Boosting a Facebook post instead of running an actual ad campaign - no conversion tracking,
  no algorithm optimization, reaches only existing followers. **[INDUSTRY]**
  ([serviceallies.com](https://www.serviceallies.com/blog-posts/10-common-mistakes-when-running-meta-ads))
- Sending the click to a slow, generic website instead of a focused lead form or landing page.
  **[INDUSTRY]**, same source.
- Using a straight percentage-off with no anchor price (1.2 above).
- Not adjusting creative for the season - running a generic "we fix HVAC" ad in July instead
  of emergency-framed AC copy, or in January instead of furnace copy (1.5 above).

---

## 2. Plumbing

### 2.1 Service taxonomy

| Service | Urgency | Typical ticket | Confidence |
|---|---|---|---|
| Emergency leak/burst pipe repair | Emergency | $150-$600 typical call | [ASSUMPTION], consistent with blended $1,714 avg ticket which includes larger jobs |
| Drain/clog clearing | Emergency-adjacent (urgent but not usually a safety issue) | $150-$450 | [ASSUMPTION] |
| Water heater repair | Emergency | $150-$600 | [ASSUMPTION] |
| Water heater replacement | Planned, often decided same-day after a failure | $1,200-$3,500 (tank); $3,000-$6,000+ (tankless) | [ASSUMPTION] |
| Repiping (whole-home) | Planned, high ticket | $4,000-$15,000+ | [ASSUMPTION] |
| Fixture install (faucets, toilets) | Planned, low urgency | $150-$600 | [ASSUMPTION] |
| Camera/sewer line inspection | Planned or emergency-adjacent (pre-purchase or recurring backups) | $200-$600 | [ASSUMPTION] |
| Maintenance/inspection plan | Planned, low urgency, recurring | Often bundled as a free or low-cost add-on rather than sold standalone | [ASSUMPTION] |

Blended average ticket for the trade is **$1,714** on Google LSA leads specifically; premium
operators report closer to $856 vs. a national service-call average of $315. **[VERIFIED]**
(research/04). The service-level breakdown above was not independently sourced this pass and
is scaled from that blended figure using general plumbing-industry pricing knowledge -
low-confidence, flagged for founder correction.

### 2.2 Offers

| Offer | Effect | Confidence |
|---|---|---|
| $99 diagnostic/service call fee | Filters tire-kickers - a real buyer with an actual problem does not object to $99 to have someone look at it. A common practice is to waive the fee if the customer proceeds with the repair, which keeps the filter without punishing people who convert. | [INDUSTRY], multiple sources agree on the mechanism ([youngdouglasinsurance.com](https://youngdouglasinsurance.com/blogs/plumber-insurance-advice/why-most-plumbers-charge-a-service-fee-and-why-it-makes-sense), synthesized search summary above) |
| Fully free estimate, no fee | Produces more volume and, in one cited real-world comparison (87 visits), closed at 38% with techs trained to qualify callers by phone before dispatch - meaning the free-estimate model only worked because of a phone-screening step, not because "free" alone was enough. Without that screening step, expect more no-shows and price-shoppers than the fee model. | [INDUSTRY], single-account data point, not a category benchmark |
| Free safety inspection for water heaters over 8 years old | Ties the offer to a real risk trigger (age-based failure risk) instead of a blanket discount, similar to the HVAC "just moved" pattern | [INDUSTRY] ([graphed.com](https://www.graphed.com/blog/facebook-ads-for-plumbers)) |
| 0% financing for tankless water heater upgrade | Standard high-ticket framing, makes a $4-6K purchase feel approachable | [INDUSTRY], same source |
| Straight percentage-off any repair | Same weak-performer pattern as HVAC - vague, no anchor, low credibility | [ASSUMPTION], by analogy |

### 2.3 Targeting defaults, with reasoning

| Parameter | Default | Reasoning |
|---|---|---|
| Service radius | 10-20 miles in a metro; up to 30 miles rural | Plumbing has a similar drive-time profile to HVAC but skews slightly tighter because emergency plumbing (active water damage) has a harder time-sensitivity than most HVAC calls - a plumber genuinely cannot be 40 minutes out on a burst-pipe call and still be useful. **[ASSUMPTION]**, directionally consistent with the HVAC radius reasoning but not independently sourced for plumbing specifically |
| Age | Emergency campaigns: 25-65, wide - a pipe bursting does not care how old the homeowner is. Planned/install campaigns: 25-55, narrower toward the group most likely to own a home and have discretionary budget for an upgrade. | **[INDUSTRY]** ([baadigi.com](https://www.baadigi.com/blog/facebook-ads-for-contractors-complete-2026-guide-to-generating-quality-leads)) |
| Gender | No exclusion | No source found justifying a skew. **[ASSUMPTION]** |
| Homeowner vs. renter | Homeowner-likely signal on, not a hard filter, same mechanism as HVAC | Renters typically call a landlord/property manager, not a plumber directly, for anything beyond a clog. **[ASSUMPTION]** |
| Interest targeting | Light layer (home improvement, homeownership) as a floor only | Same 2026 Advantage+ reasoning as HVAC, see cross-trade section. **[INDUSTRY]** |
| Home-age-based targeting (e.g. "homes built 1978-1995" for polybutylene pipe risk) | Do not implement as a native Meta targeting field | See the cross-trade flag above - this does not appear to be a real, native Ads Manager capability, and building it into the schema as if it were would be building on an unverified claim. |

### 2.4 Budget guidance

- **Daily minimum:** Same disputed range as HVAC ($20-50/day per research/04 vs. $50-100/day
  per 2026 blogs). See Founder Must Confirm.
- **Realistic monthly range:** $1,000-$3,000+/mo. **[VERIFIED]** (research/04)
- **Expected cost per lead:** LSA benchmark $57/lead. **[VERIFIED]** (research/04). No
  plumbing-specific Meta CPL breakdown by service type was found this pass (HVAC had one,
  plumbing did not) - flagged as a data gap, not filled with a guess.
- **Budget scaling with radius/population:** same logic as HVAC 1.4 - scale with households in
  radius, not raw miles. **[ASSUMPTION]**

### 2.5 Seasonality

| Month(s) | Demand signal | What the ad should say |
|---|---|---|
| Nov-Jan | Frozen pipe repair searches spike hard, +609% in January specifically; water heater repair also peaks in this window | Pure emergency framing - burst pipes, no heat/hot water, same-day response |
| Feb-Mar | Frozen-pipe demand tapering | Repair-and-prevent messaging (pipe insulation, pre-freeze inspection) as a bridge to shoulder season |
| Apr, Oct | Shoulder months, lower search volume overall | Maintenance and inspection offers to fill technician schedules during the lull |
| Jun-Aug | "Emergency plumber" and "plumber near me" searches rise, peaking mid-summer (~+36%), driven by heavier household water use (irrigation, pools, more people home) | Emergency framing again, but paired more with fixture/upgrade offers than the winter freeze framing |
| Sep | Building toward winter | Water heater and pipe-insulation prep messaging ahead of the freeze season |

**[INDUSTRY]** (Stacker syndicated seasonal search data, same family of sources as HVAC
above). Like HVAC, this is a national curve and needs regional adjustment - freeze risk is a
non-issue in most of Florida and central to demand in Minnesota.

### 2.6 Copy angles

No directly-quotable real plumbing ad examples were found in this research pass (the
plumbing-specific source reviewed described offer *categories* without concrete headline
copy). The templates below are built to the same voice pattern validated for HVAC and roofing
(specific dollar figure, local claim, urgency tied to a real trigger) and are explicitly
**illustrative, not observed live ad copy.**

**Works, by pattern (carried over from validated HVAC/roofing findings, applied to
plumbing):**
- Specific, anchored pricing: "$99 Diagnostic - Applied to Your Repair if You Book"
- Local, named-person framing: "Hi, I'm [Name] - Licensed [City] Plumber, On Call Today"
- Trigger-event targeting: "Water Heater Over 8 Years Old? Free Safety Check"
- Loss-framed education: "This $12 Part Fails First - Here's How to Tell"

**Illustrative primary text template:**
> "Water where it shouldn't be? We're a licensed local crew and we pick up the phone. $99 gets
> a same-day diagnostic, and it's credited back if you book the repair."

**Fails, by pattern:** generic "your trusted plumber" copy with no number or name; vague
percentage-off; "Contact us" CTAs with no offer attached.

### 2.7 Creative direction

Same pattern as HVAC 1.7: real technician mid-repair, real truck, before/after of the actual
fixture or pipe (not staged). Plumbing has a specific opportunity HVAC does not: the burst
pipe / water damage moment is highly visual and creates urgency on sight, so a real (not
staged) photo of active water damage performs as an attention-grabbing image where available
and policy-permitted. **[ASSUMPTION]** - this is a reasonable inference from the "real beats
polished" finding, not independently sourced for plumbing.

### 2.8 Lead form qualifying questions

1. "What's the problem?" - Leak/burst pipe / clog / water heater / new install / other
2. "Is this an emergency right now?" - Yes/No, routes urgency directly
3. "Are you the homeowner?" - Yes/No

**[ASSUMPTION]**, adapted from the HVAC pattern (2.8's sibling section, 1.8) since no
plumbing-specific lead-form study was found. The mechanism (route by urgency, filter
non-decision-makers) is well-supported; the exact wording is a reasonable adaptation, not a
sourced fact.

### 2.9 Common owner mistakes this product should prevent by default

- No diagnostic fee and no phone-screening step, producing high no-show/price-shopper rates
  from a "fully free" offer (2.2 above).
- Same radius/targeting and slow-follow-up mistakes as the cross-trade section.
- Running the same ad copy in January and July when the demand driver and the right message
  are completely different (2.5 above).

---

## 3. Roofing

### 3.1 Service taxonomy

| Service | Urgency | Typical ticket | Confidence |
|---|---|---|---|
| Storm/emergency tarping | Emergency | $300-$1,500 | [ASSUMPTION] |
| Leak repair | Emergency-adjacent | $300-$1,500 | [ASSUMPTION] |
| Full roof replacement | Planned (though often storm-triggered) | $8,000-$20,000+ | [VERIFIED] (research/04) |
| Roof inspection | Planned or storm-triggered | Often free or $79-$150 if paid | [INDUSTRY] ($79 figure from [jobnimbus.com](https://www.jobnimbus.com/blog/top-facebook-ads-for-roofers-boost-your-business-with-these-proven-strategies)) |
| Insurance claim assistance / storm damage assessment | Storm-triggered, high urgency for the homeowner emotionally, not physically | Bundled into inspection or replacement, not usually its own line item | [ASSUMPTION] |
| Gutter install/repair | Planned, low urgency | $500-$3,000 | [ASSUMPTION] |

**Reasoning the owner reads:** "Storm damage and leaks get emergency framing because the
homeowner is worried about active damage to their house. A full replacement is planned even
after a storm, because insurance and financing decisions take days to weeks, so the ad can
sell trust and process instead of pure speed."

### 3.2 Offers

| Offer | Effect | Confidence |
|---|---|---|
| Free roof inspection | The most common offer in the category and generally effective at generating volume, but this is also the exact offer scam "storm chasers" use to manufacture damage and pressure a same-day signature. A legitimate version of this offer must be paired with no-pressure language and scheduling flexibility in the copy, or the product risks training owners to sound like the predatory operators homeowners are actively warned about. | [INDUSTRY] (multiple sources on both the offer's effectiveness and its scam association - [visexterior.com](https://visexterior.com/blog/avoid-roofing-scams-local-roofers-vs-storm-chasers/), [preferredroofingkc.net](https://www.preferredroofingkc.net/how-to-spot-storm-chasers-vs-local-roofing-companies)) |
| $79 paid inspection, non-storm season | Filters casual browsers in the off-season when there is no urgent trigger event; less appropriate right after a storm, when free/urgent framing outperforms. | [INDUSTRY] (jobnimbus.com $79 example) |
| "Free estimate this week" paired with a warranty/credential claim | Combines a low-friction offer with a trust signal, which matters enormously in a category associated with scams | [INDUSTRY], same source |
| Percentage-off a full replacement | Weak, same pattern as other trades - vague and hard to believe at an $8-20K price point specifically, since a "20% off" on a number the homeowner does not know yet is meaningless | [ASSUMPTION] |

### 3.3 Targeting defaults, with reasoning

| Parameter | Default | Reasoning |
|---|---|---|
| Service radius | 15-20 miles baseline, but roofing is the trade most likely to run a **storm-response radius override**: a tight, ZIP-code-specific radius drawn around the actual storm-affected area, active for days not months | A roofing crew will drive further than an HVAC tech for a single $8-20K job, so the baseline radius is comparable to HVAC's low end, but storm response is roofing's unique targeting behavior - none of the other three trades has an equivalent "the addressable market changed overnight" event. **[INDUSTRY]** ([cinchlocal.com](https://www.cinchlocal.com/the-ultimate-2026-guide-to-meta-advertising-for-roofers)) |
| Age | 35-65 | Skews older than HVAC/plumbing because roof replacement is a large, often insurance-mediated financial decision that tends to sit with the primary homeowner of record. **[INDUSTRY]** (same source) |
| Gender | No exclusion | No source found justifying a skew. **[ASSUMPTION]** |
| Homeowner vs. renter | Hard filter is more justified here than any other trade - a renter essentially never commissions a roof replacement | Roofing has the highest ticket value of the four trades, so wasted impressions on non-homeowners are the most expensive mistake in the whole playbook. **[ASSUMPTION]**, but a low-risk one given the ticket size |
| Interest targeting | Light layer, plus storm/weather-event relevance where the platform supports it | Same 2026 Advantage+ reasoning as the other trades. **[INDUSTRY]** |
| Storm-response timing | Ad copy and radius should be able to update within hours of a hail/wind event, targeting the specific affected ZIPs | One cited case: a Savannah roofing contractor spent $650 after a hail event and reported $120,000 in revenue from 50 leads, a ~185x return - but this is a single anecdote reported by one marketing agency, not a category benchmark, and should not be presented to owners as an expected outcome. CPCs are reported to rise 40-120% in the first 48 hours after a storm as out-of-market "storm chaser" crews flood the same auction, so acting in the first 6-24 hours matters more here than in any other trade. **[INDUSTRY]** ([cinchlocal.com](https://www.cinchlocal.com/the-ultimate-2026-guide-to-meta-advertising-for-roofers)) |

### 3.4 Budget guidance

- **Daily minimum:** Same disputed range as the other trades (research/04's $20-50/day floor
  vs. 2026 blogs' $50-100/day). Roofing's higher CPL (below) means the *effective* minimum to
  generate a usable weekly lead volume is higher in dollar terms than HVAC/plumbing/electrical
  even at the same daily-spend floor.
- **Realistic monthly range:** $2,500-$7,500/mo baseline, with storm-season spikes well above
  that range for a business willing to chase the surge. **[VERIFIED]** (research/04)
- **Expected cost per lead:** $234-262 Jan-Mar (off-peak), $300+ in storm season, up to $600
  in hot metros. **[VERIFIED]** (research/04). Home-improvement-category Meta CPC is reported
  at $0.99 vs. a $5.26 Google Ads CPC average, which is a meaningfully cheaper click, though
  clicks are not leads and roofing's Meta lead volume/quality was not independently sourced
  this pass. **[INDUSTRY]** ([jobnimbus.com](https://www.jobnimbus.com/blog/top-facebook-ads-for-roofers-boost-your-business-with-these-proven-strategies))
- **Budget scaling with radius/population:** same population-based logic as the other trades,
  with the addition that storm-response campaigns should spike budget sharply and briefly
  rather than smoothly scale, because the addressable market is concentrated in a narrow time
  window. **[ASSUMPTION]** on the mechanism, **[INDUSTRY]** on the underlying storm-CPC-spike
  data point above.

### 3.5 Seasonality

Roofing has the widest geographic variance of any trade in this playbook - the "season" is
fundamentally a regional weather calendar, not a national one.

| Period | National pattern | What the ad should say |
|---|---|---|
| Winter (Dec-Feb) | Slowest period nationally; ~25-30% of a typical annual ad budget, weighted toward brand-building and early-booking incentives rather than volume | Early-booking discounts for spring replacement, financing offers, "lock in this year's price" framing |
| Spring (Mar-May) | Storm-damage season begins in much of the country (especially the Southern Plains/Midwest hail corridor); ~25-30% of annual budget | Storm damage and inspection offers, insurance-claim-assistance framing |
| Summer (Jun-Aug) | Peak installation season (dry weather = faster work); late-summer storm/hurricane spikes on the Gulf Coast; ~20-25% of annual budget | Installation speed and crew capacity messaging, plus emergency storm framing where a weather event actually occurs |
| Fall (Sep-Nov) | Hurricane season continues on the Gulf/Atlantic coast through November; ~20-25% of annual budget elsewhere, weighted toward winterization and preventative maintenance | Winterization and preventative-maintenance offers in non-coastal markets; continued storm-emergency framing in hurricane-exposed markets |

**[INDUSTRY]** ([jobnimbus.com](https://www.jobnimbus.com/blog/roofing-marketing-strategies-timing-campaigns-for-maximum-impact),
multiple corroborating sources in the same family). **This table needs a regional overlay to
be useful**: a Texas/Oklahoma hail-corridor business, a Florida/Gulf hurricane-corridor
business, and a mountain-region business with a compressed 6-8 month working season each have
genuinely different curves, not just a shifted version of the same one. Storm-response timing
(3.3/3.4 above) should override this baseline curve entirely whenever an actual weather event
is detected or reported by the owner.

### 3.6 Copy angles

**Works, real examples:**
- Storm-urgency framing tied to a named, current event: "Homeowners in Tampa: is your roof on
  the Beryl repair list?" **[INDUSTRY]** ([jobnimbus.com](https://www.jobnimbus.com/blog/top-facebook-ads-for-roofers-boost-your-business-with-these-proven-strategies))
- Direct seasonal question: "Will your roof make it through hurricane season?" Same source.
- Trust-plus-offer combination: "Lifetime warranty. Local crew. Free estimate this week." Same
  source.
- Anchored, dated pricing: "Spring roof inspections, only $79 through May 15." Same source.
- Specific, low-commitment CTAs beat generic ones: "Get my free roof inspection," "See if I
  qualify," "Claim my storm-damage assessment" outperform "Contact us" or "Learn more." Same
  source.

**Fails, consistently:**
- Generic "Contact us" / "Learn more" CTAs (documented directly in the source above).
- Given the storm-chaser association covered in 3.2, copy that manufactures urgency without a
  real trigger event ("Act now before it's too late!" with no storm, no date, no reason) risks
  reading as exactly the predatory pattern homeowners are warned about. **[ASSUMPTION]**, a
  brand-safety inference rather than a sourced performance claim.
- Primary text over roughly 125 characters gets truncated in feed and the source recommends
  keeping copy short for that reason. **[INDUSTRY]**, same source.

**Illustrative primary text template** (built to the validated pattern, not observed copy):
> "Storm rolled through [City] last week. If you've got missing shingles or a soft spot in the
> ceiling, we're doing free inspections through Friday - no obligation, no pressure, just a
> straight answer on what it'll cost to fix."

### 3.7 Creative direction

- **What converts:** the crew actually on a roof (not a stock "guy on a ladder" stock photo),
  before/after of the physical roof itself (this is standard, policy-permitted trade
  before/after imagery, not the aesthetic-attribute kind the policy lint bans - see cross-trade
  note above), and storm-damage documentation photos when available (real, not staged).
  **[INDUSTRY]**, consistent with the real-beats-stock pattern established for HVAC.
- **What does not convert:** generic stock roofing photos, and especially generic "handshake
  in front of a house" imagery, which reads as agency-produced rather than local.
  **[INDUSTRY]**, same source family as 1.7.
- **A roofing-specific creative risk:** because free-inspection offers are associated with
  scam operators, creative that looks too polished/corporate can actually hurt trust in this
  category specifically, more than in the other three trades. Leaning toward visibly real,
  slightly rough photography is a stronger trust signal here than anywhere else in this
  playbook. **[ASSUMPTION]**, inferred from the scam-association research in 3.2, not directly
  tested.

### 3.8 Lead form qualifying questions

1. "What's going on with your roof?" - Storm damage / leak / getting old / just want an
   inspection
2. "Are you working with an insurance claim?" - Yes/No/Not sure (this single question does
   more qualifying work in roofing than almost anywhere else, since insurance-claim jobs and
   out-of-pocket jobs are sold completely differently)
3. "Are you the homeowner?" - Yes/No

**[ASSUMPTION]**, adapted from the general pattern; the insurance-claim question specifically
was not found sourced but is a well-understood industry distinction worth flagging for the
founder to confirm or replace.

### 3.9 Common owner mistakes this product should prevent by default

- Running the same evergreen ad in January and immediately after a hailstorm, missing the
  6-72 hour window when post-storm engagement is reported to run roughly 50% higher than
  evergreen campaigns. **[INDUSTRY]** ([cinchlocal.com](https://www.cinchlocal.com/the-ultimate-2026-guide-to-meta-advertising-for-roofers))
- Using free-inspection copy that reads as high-pressure, which both underperforms and risks
  the business being lumped in with storm-chaser scams in the homeowner's mind (3.2, 3.6).
- Not narrowing the radius to the actual storm-affected ZIPs during a storm-response campaign,
  wasting the highest-CPC window of the season on people who were not affected.

---

## 4. Electrical

### 4.1 Service taxonomy

| Service | Urgency | Typical ticket | Confidence |
|---|---|---|---|
| Emergency repair (outage, sparking, breaker issues) | Emergency | $150-$500 | [ASSUMPTION], scaled from the $1,434 blended LSA average |
| Panel upgrade (100A to 200A) | Planned, often triggered by another project (EV, solar, remodel) | $1,800-$3,500 | [INDUSTRY] ([pipelineon.com](https://pipelineon.com/blog/electrician-contractor-advertising-ideas/), [build-folio.com](https://build-folio.com/contractor-guides/electrical-contractor-pricing-guide/)) |
| EV charger install (Level 2) | Planned | $1,200-$3,500, sometimes as low as $749 for panels with existing capacity | [INDUSTRY] ([evchargeright.com](https://evchargeright.com/blog/ev-charger-installation-cost)) |
| Generator install (whole-home standby) | Planned, but demand spikes sharply around storm risk | $4,000-$12,000 | [INDUSTRY] ([pipelineon.com](https://pipelineon.com/blog/electrician-contractor-advertising-ideas/)) |
| Whole-home rewiring | Planned, high ticket | $8,000-$20,000+ (older/larger homes) | [ASSUMPTION] |
| Lighting/fixture install | Planned, low urgency | $150-$600 | [ASSUMPTION] |
| Electrical safety inspection | Planned, low urgency, often pre-purchase or pre-sale | $150-$300 | [ASSUMPTION] |

Blended average ticket $1,434 on LSA leads, the lowest of the four trades, with the cheapest
LSA cost per lead ($39) and highest book rate (43.9%) - **[VERIFIED]** (research/04). This
makes electrical the trade with the most favorable unit economics on paper, but also the one
with the widest spread between its lowest-ticket service (a $150 outlet repair) and its
highest (a $12,000+ generator or full rewire), so a single blended default is the least useful
of the four trades without splitting by service.

### 4.2 Offers

| Offer | Effect | Confidence |
|---|---|---|
| Free electrical safety inspection | Same trigger-event logic as HVAC/plumbing - works best tied to a real reason (older home, pre-sale, recent renovation) rather than offered generically | [ASSUMPTION], by pattern from the other three trades |
| $X off panel upgrade when bundled with EV charger or generator install | Bundling the planned, discretionary upgrade with the higher-ticket item is a natural upsell path since a panel upgrade is frequently a prerequisite for the other two | [ASSUMPTION], inferred from the taxonomy relationship, not independently sourced |
| Financing framed as monthly payment for panel/generator/rewiring | Same high-ticket affordability framing as HVAC replacement | [ASSUMPTION], by pattern |
| Flat diagnostic/service call fee | Same tire-kicker-filtering logic as plumbing's $99 fee, not independently sourced for electrical this pass | [ASSUMPTION] |

Electrical is the weakest-sourced trade for offer-specific data in this research pass. No
electrical-specific real ad or offer case study was found (searches returned pricing guides,
not marketing case studies). This is a genuine gap, not filled with invented specifics -
flagged in Founder Must Confirm.

### 4.3 Targeting defaults, with reasoning

| Parameter | Default | Reasoning |
|---|---|---|
| Service radius | 15-25 miles in a metro, similar to HVAC | Electrical work has a similar drive-time and truck-based service model to HVAC; no source was found suggesting electrical should differ meaningfully from that baseline. **[ASSUMPTION]** |
| Age | Skew 35-65 for panel upgrade/major system campaigns | Same reasoning as electrical's HVAC-replacement analog: this age band owns homes and finances major systems. **[INDUSTRY]** ([baadigi.com](https://www.baadigi.com/blog/facebook-ads-for-contractors-complete-2026-guide-to-generating-quality-leads), citing electrical panel work specifically) |
| Gender | No exclusion | No source found. **[ASSUMPTION]** |
| Homeowner vs. renter | Homeowner-likely signal on, not a hard filter | Same logic as HVAC/plumbing. **[ASSUMPTION]** |
| Interest targeting | Light layer; for EV charger campaigns specifically, EV-ownership/EV-interest signals are a genuinely relevant, non-theatre interest layer since it directly identifies the buyer | This is the one place across all four trades where interest targeting is more than a floor - EV ownership or in-market-for-EV signals are a strong, directly relevant proxy the other services do not have an equivalent for. **[ASSUMPTION]**, sound targeting logic but not independently sourced as validated in Meta's current interest taxonomy |

### 4.4 Budget guidance

- **Daily minimum:** Same disputed range as the other trades.
- **Realistic monthly range:** $1,000-$2,500/mo. **[VERIFIED]** (research/04)
- **Expected cost per lead:** LSA benchmark $39/lead, the cheapest of the four trades, with a
  43.9% book rate producing an effective cost per *paying customer* around $233.
  **[VERIFIED]** (research/04, corroborated by [pipelineon.com](https://pipelineon.com/blog/local-service-ads-electrician/)).
  High-intent electrical keywords on Google run $8-20/click and $100-250/lead for terms like
  "panel upgrade [city]," which is a useful proxy for the top of the electrical CPL range even
  though it is a Google, not Meta, figure. **[INDUSTRY]**
- **Budget scaling with radius/population:** same population-based logic as the other trades.
  **[ASSUMPTION]**

### 4.5 Seasonality

Electrical is the least seasonal of the four trades in general demand, but has two sharply
seasonal sub-services:

| Period | Signal | What the ad should say |
|---|---|---|
| Hurricane season (Jun-Nov, Gulf/Atlantic coast) and ice-storm season (winter, especially in regions whose grid infrastructure is not built for ice) | Generator install demand spikes sharply around actual or anticipated outage events | Generator-specific storm-preparedness or storm-response framing, similar in spirit to roofing's storm-response behavior but tied to power outage risk rather than physical damage |
| Year-round, with likely secondary demand tied to home-sale season (spring/summer) and remodel season | Panel upgrades and rewiring, as prerequisite work for renovations and EV/solar additions | General planned-upgrade framing; tie panel-upgrade offers to renovation or EV-purchase trigger events rather than a specific month |
| No strong seasonal signal found | General repair and lighting/fixture work | Standard always-on framing, no seasonal message needed |

**[INDUSTRY]** for the generator/storm-season pattern
([pipelineon.com](https://pipelineon.com/blog/electrician-contractor-advertising-ideas/)).
**[ASSUMPTION]** for the panel-upgrade/home-sale-season correlation and for the "no strong
seasonal signal" conclusion on general repair work - this is the weakest-sourced seasonality
table of the four trades and should be treated as a placeholder pending founder input, not a
confident prior.

### 4.6 Copy angles

No electrical-specific real ad examples were found in this research pass (search results
returned pricing content, not marketing case studies). The templates below are adapted from
the validated cross-trade pattern (specific price, local claim, real trigger event) and are
explicitly **illustrative, not observed live ad copy** - electrical has the least-validated
copy section of the four trades.

**Works, by pattern:**
- Specific safety/risk framing tied to home age: "Is Your Panel Ready for an EV Charger? Free
  Assessment."
- Named-person, local-credential framing, consistent with the other three trades.
- Anchored pricing on the bundled upgrade path: "Panel Upgrade + EV Charger, One Visit, One
  Quote."

**Illustrative primary text template:**
> "Buying an EV or adding solar? Most homes built before [year range] need a panel upgrade
> first. We're a licensed local crew - free assessment tells you exactly what it'll cost,
> no surprises."

**Fails, by pattern:** same generic/no-offer/no-name failures as the other three trades.

### 4.7 Creative direction

Same real-beats-stock pattern as the other trades: an electrician actually working inside an
open panel, a marked truck, before/after of the physical panel or wiring. No electrical-
specific creative study was found; this section is inferred entirely from the pattern
established for HVAC/roofing. **[ASSUMPTION]**

### 4.8 Lead form qualifying questions

1. "What do you need?" - Repair / panel upgrade / EV charger / generator / other
2. "Is this urgent (power out, sparking, breaker tripping)?" - Yes/No
3. "Are you the homeowner?" - Yes/No

**[ASSUMPTION]**, adapted from the cross-trade pattern; no electrical-specific lead-form study
was found.

### 4.9 Common owner mistakes this product should prevent by default

- Treating all electrical inquiries as one funnel when a $150 outlet repair and a $12,000
  rewire are completely different sales motions (4.1 above) - same underlying mistake as
  HVAC's emergency/planned collapse.
- Missing the EV/generator-specific targeting opportunity by defaulting to the same generic
  "homeowner" targeting used for repair work, when these two sub-services have real,
  identifiable buyer signals available (4.3 above).
- Same radius/follow-up mistakes as the cross-trade section.

---

## 5. Machine-readable schema proposal

This is what the generation pipeline reads. Prose above is the research; this is the data
shape a smart-default and copy-generation service would actually query. TypeScript types,
matching the style of `src/db/schema.ts` referenced in `AGENTS.md`. No application code is
implied here beyond the type shape itself - this is a proposal for review, not a committed
schema.

```typescript
// Confidence tagging is first-class, not a comment. Every sourced number in the UI
// should be able to render its confidence level and, where applicable, a citation,
// so the "why" the product shows the owner can be honest about how solid the number is.
type Confidence = "verified" | "industry" | "assumption";

interface SourcedValue<T> {
  value: T;
  confidence: Confidence;
  source?: string;        // URL, required when confidence is "verified" or "industry"
  note?: string;           // short plain-English caveat, e.g. "national average, not regional"
  founderOverride?: T;     // set once the founder confirms or corrects the researched default
}

type TradeId = "hvac" | "plumbing" | "roofing" | "electrical";

type Urgency = "emergency" | "emergency_adjacent" | "planned";

interface ServiceDefinition {
  id: string;                          // e.g. "hvac_ac_repair"
  tradeId: TradeId;
  label: string;                       // owner-facing name, in their words: "AC repair"
  urgency: Urgency;
  ticketRange: SourcedValue<{ low: number; high: number }>;
  isEmergencyOfferEligible: boolean;   // can this service run "we're X minutes away" copy
}

interface OfferDefinition {
  id: string;
  tradeId: TradeId;
  applicableServiceIds: string[];      // which services this offer type fits
  label: string;                       // "Named diagnostic fee"
  template: string;                    // "${{amount}} diagnostic - credited if you book"
  effect: SourcedValue<string>;        // plain-English what-it-does, e.g. "filters tire-kickers"
  riskFlag?: string;                   // e.g. "associated with storm-chaser scam pattern in roofing"
}

interface TargetingDefaults {
  tradeId: TradeId;
  serviceRadiusMiles: SourcedValue<{ metro: [number, number]; rural: [number, number] }>;
  ageRange: SourcedValue<{ low: number; high: number }>;
  ageRangeByUrgency?: Partial<Record<Urgency, SourcedValue<{ low: number; high: number }>>>;
  genderExclusion: SourcedValue<"none">;   // explicit "none" default, not omitted, so the
                                            // absence of a skew is a documented decision,
                                            // not a gap
  homeownerFilterMode: SourcedValue<"signal_only" | "hard_filter">;
  interestLayerDepth: SourcedValue<"light_floor" | "meaningful">;
  interestLayerReasoning: string;          // owner-facing explanation of why this depth
  specialTargetingNotes?: SourcedValue<string>[]; // e.g. EV-owner signal for electrical
}

interface BudgetGuidance {
  tradeId: TradeId;
  dailyMinimumUsd: SourcedValue<{ low: number; high: number }>;
  monthlyRangeUsd: SourcedValue<{ starter: [number, number]; competitive: [number, number] }>;
  costPerLeadUsd: SourcedValue<{ low: number; high: number }>;
  costPerLeadByServiceId?: Record<string, SourcedValue<{ low: number; high: number }>>;
  scalingRule: SourcedValue<string>;       // plain-English rule, e.g. "scale with households
                                            // in radius, not radius in miles"
}

interface SeasonalityPoint {
  tradeId: TradeId;
  monthOrPeriod: string;                   // "Jul" or "storm_response" for event-driven trades
  demandSignal: SourcedValue<string>;
  recommendedAngle: string;                // owner-facing: what the ad should say this period
  regionSensitive: boolean;                // true means the national curve is a weak prior and
                                            // should be adjusted by the owner's climate/region
  eventTriggered?: boolean;                // true for roofing storm-response, electrical
                                            // generator-storm-response
}

type CopyAngleStatus = "validated_real_example" | "illustrative_template" | "pattern_inferred";

interface CopyAngle {
  tradeId: TradeId;
  serviceId?: string;
  angleType: "speed" | "trust_credential" | "price_anchor" | "trigger_event" |
             "loss_framed_education" | "storm_urgency";
  headline: string;
  primaryText?: string;
  status: CopyAngleStatus;                 // never present a template as a real example
  source?: string;
}

interface CopyAngleAntiPattern {
  tradeId: TradeId;
  pattern: string;                         // e.g. "straight percentage-off, no anchor price"
  whyItFails: string;
  confidence: Confidence;
}

interface CreativeDirection {
  tradeId: TradeId;
  preferredShotTypes: string[];            // ["technician_mid_task", "marked_truck", "before_after_equipment"]
  avoidShotTypes: string[];                // ["stock_handshake", "posed_studio", "generic_office"]
  generatedImageFallbackRule: string;
  tradeSpecificNote?: string;              // e.g. roofing's scam-association creative caution
}

interface LeadFormQuestion {
  tradeId: TradeId;
  order: number;                           // enforce the 2-3 question cap in code, not just docs
  question: string;
  fieldType: "single_select" | "yes_no" | "short_text";
  options?: string[];
  purpose: string;                         // owner-facing: what this question filters for
}

interface OwnerMistake {
  tradeId: TradeId;
  mistake: string;
  howDefaultPrevents: string;              // ties directly back to a TargetingDefaults or
                                            // BudgetGuidance field, so every prevented mistake
                                            // traces to a concrete default
}

interface TradePlaybook {
  tradeId: TradeId;
  services: ServiceDefinition[];
  offers: OfferDefinition[];
  targeting: TargetingDefaults;
  budget: BudgetGuidance;
  seasonality: SeasonalityPoint[];
  copyAngles: CopyAngle[];
  copyAntiPatterns: CopyAngleAntiPattern[];
  creative: CreativeDirection;
  leadFormQuestions: LeadFormQuestion[];
  ownerMistakesPrevented: OwnerMistake[];
  lastReviewedByFounder?: string;          // ISO date, null until the founder has actually
                                            // confirmed this trade's defaults - the generation
                                            // pipeline can use this to flag "researched, not
                                            // yet founder-verified" in an internal admin view
}
```

Design notes on the schema:

- **`SourcedValue<T>` is the load-bearing pattern.** Every number the AI presents to an owner
  as a "why" should be traceable back to a confidence level and, where applicable, a citation.
  This makes it structurally impossible to accidentally present a researched guess as
  validated fact in the product UI - the confidence field has to be read and rendered, not
  just known by whoever wrote the seed data.
- **`founderOverride` on every `SourcedValue`** is how the founder's real experience wins
  without deleting the research trail. Once set, generation logic should prefer
  `founderOverride` over `value`, and the UI should be able to show "your number" vs. "our
  research" if that's ever useful for debugging or for the founder's own review pass.
- **`CopyAngleStatus`** exists specifically because this research mixed real, cited ad
  examples (HVAC, roofing) with illustrative templates (plumbing, electrical). The schema
  should never let those collapse into an undifferentiated "example" - the product must not
  present a template as if it were a real ad that ran and worked, which would itself be the
  fabricated-performance-statistic problem `AGENTS.md` rule 3 exists to prevent, just moved
  one level up from "results" to "copy examples."
- **`eventTriggered` seasonality points** (roofing storm-response, electrical generator
  storm-response) are structurally different from calendar seasonality and need a separate
  activation path - likely fed by a weather/storm data source in a later version, manually
  toggled by the owner in v1 ("has your area had storm damage recently?").
- **`OwnerMistake.howDefaultPrevents`** forces every entry in section 9 of the research above
  to point at an actual field in `TargetingDefaults` or `BudgetGuidance`. If a mistake can't be
  traced to a concrete default, either the default is missing or the mistake doesn't belong in
  the schema yet.

---

## 6. FOUNDER MUST CONFIRM

Every one of these is a place where this research is a starting guess and the founder's
direct experience running Facebook and Google ads for these trades should override it. None
of the numbers below should ship as a silent default without his sign-off; the honest move
until then is to mark them clearly as "researched, not yet confirmed" wherever they surface in
product or investor-facing material.

1. **Meta daily budget floor.** Sources genuinely disagree - $20-50/day (research/04, citing
   2026 minimum-budget guides) vs. $50-100/day (newer 2026 blogs, using a learning-phase
   formula). This directly sets a warning threshold the owner sees. Needs the founder's real
   number from accounts he has actually run.
2. **Service radius per trade.** The 15-25 mile HVAC/electrical, 10-20 mile plumbing, and
   15-20 mile roofing (plus storm override) defaults above are built mostly from marketing-
   blog guidance, not from actual job-location data. The founder's own campaigns likely have
   real answers to "how far did our booked jobs actually come from," which is the single best
   possible input and beats every source cited here.
3. **Whether "home built in year range X" targeting is real or fabricated content.** Flagged
   throughout as likely not a native Meta Ads Manager field. Needs verification before it goes
   anywhere near the schema as an actual targeting lever, or it should be dropped entirely.
4. **Diagnostic/service-fee offer amounts** ($79-99 range used throughout). These came from
   agency blogs, not from A/B-tested outcomes. The founder likely knows, from real spend,
   whether a fee offer or a free offer produces better lead quality in his own markets.
5. **Age-band defaults per trade** (25-55 vs 25-65 vs 35-65 splits). Sourced to a single
   agency blog (baadigi.com) across all four trades - one source repeated four times is a
   weak evidentiary base for something that directly shapes who sees every ad.
6. **Ticket ranges for every service *below* the trade-level blended average** - i.e., every
   number in each trade's 1.1/2.1/3.1/4.1 table except the top-line blended figures that trace
   to research/04. These were extrapolated from the blended average, not independently sourced,
   and the founder likely has real invoice data that beats extrapolation entirely.
7. **Seasonality curves, especially electrical's** (weakest-sourced of the four) and the
   region-sensitivity problem across all trades - the tables above are national averages and
   the product needs either a regional adjustment mechanism or the founder's read on how wrong
   the national curve is for the specific markets early customers will be in.
8. **Whether the free-inspection-vs-paid-inspection call is right for roofing**, given the
   scam-association risk flagged in 3.2/3.6. This is as much a brand-safety and legal-adjacent
   judgment call as a marketing one, and it should not be decided by a document built from
   marketing blogs.
9. **Lead form question wording for plumbing, roofing, and electrical** (2.8/3.8/4.8) - all
   three were adapted from the HVAC pattern (1.8, itself only lightly sourced) rather than
   independently validated per trade. The founder's experience with which questions actually
   got answered honestly vs. abandoned the form is the real data here.
10. **Electrical's entire offer section (4.2) and most of its copy section (4.6)** - this
    trade returned the thinnest research of the four across nearly every category. It should
    be treated as the least-trustworthy quarter of this document until the founder fills the
    gap, not silently reused from the HVAC pattern as if it were equally validated.
11. **Whether percentage-off offers really underperform as consistently as this document
    claims.** That conclusion is stated multiple times but is inferred by pattern ("the
    working examples are always specific dollar amounts") rather than a direct source
    comparing percentage-off to fixed-dollar offers head to head. Worth a direct gut-check
    against the founder's own account history before it becomes a hard rule the AI enforces.
12. **Budget-scaling-with-population rule** (all four "1.4/2.4/3.4/4.4" sections) is sound
    media-buying logic that this research could not find independently stated for these
    specific trades. It should be validated as a real, implementable rule (and its exact
    formula) before the budget-recommendation logic ships on it.

---

## 7. Sources

All URLs cited inline above. Consolidated here for reference. Every source below is a
2025-2026 dated marketing-agency blog, SEO content site, or vendor page unless otherwise
noted; none is a peer-reviewed study or a platform-published (Meta/Google) primary benchmark
except where explicitly marked [VERIFIED] and traced to research/04's own primary-source
citations.

- [Meta Advantage+ Audience vs Detailed Targeting: 2026 Guide](https://www.conversios.io/blog/meta-advantage-audience-vs-detailed-targeting-2026-guide/)
- [Meta Broad Targeting 2026: Why Advantage+ Audiences Replace Interest Targeting](https://adligator.com/blog/meta-broad-targeting-advantage-plus-audiences-2026)
- [Facebook Ads for Contractors 2026 Setup, BaaDigi](https://www.baadigi.com/blog/facebook-ads-for-contractors-complete-2026-guide-to-generating-quality-leads)
- [The HVAC Facebook Ad Formula for Local Success, LeadEnforce](https://leadenforce.com/blog/the-hvac-facebook-ad-formula-for-local-success)
- [The Ultimate 2025 Guide to Facebook Ads for HVAC Contractors, Transcend GTM](https://transcendgtm.com/blog/the-ultimate-2025-guide-to-facebook-ads-for-hvac-contractors)
- [12 HVAC Facebook Ad Examples That Drive Calls, AGMarketing](https://actglobalmarketing.com/hvac-facebook-ad-examples/)
- [HVAC Facebook Ads Statistics: CPL & ROI (2026), Web Tonic](https://www.webtonic.io/blog/hvac-facebook-ads-statistics)
- [Facebook Marketing for Roofing: Playbook to Win More Local Leads, JobNimbus](https://www.jobnimbus.com/blog/top-facebook-ads-for-roofers-boost-your-business-with-these-proven-strategies)
- [Roofing marketing strategies: timing campaigns for maximum impact, JobNimbus](https://www.jobnimbus.com/blog/roofing-marketing-strategies-timing-campaigns-for-maximum-impact)
- [Ultimate 2026 Roofer Facebook Ad Strategy, Cinch Local](https://www.cinchlocal.com/the-ultimate-2026-guide-to-meta-advertising-for-roofers)
- [How to Avoid Roofing Scams: Local Roofers vs Storm Chasers, Vis Exterior](https://visexterior.com/blog/avoid-roofing-scams-local-roofers-vs-storm-chasers/)
- [Avoid Storm Chaser Roofing Companies, Preferred Roofing](https://www.preferredroofingkc.net/how-to-spot-storm-chasers-vs-local-roofing-companies)
- [Facebook Ads for Plumbers: The Complete 2026 Strategy Guide, Graphed](https://www.graphed.com/blog/facebook-ads-for-plumbers)
- [Why Most Plumbers Charge a Service Fee, Young Douglas Insurance](https://youngdouglasinsurance.com/blogs/plumber-insurance-advice/why-most-plumbers-charge-a-service-fee-and-why-it-makes-sense)
- [Electrical Contractor Marketing Ideas That Book $300+ Panel Jobs, Pipeline On](https://pipelineon.com/blog/electrician-contractor-advertising-ideas/)
- [Free Electrical Pricing Guide 2026, Build-Folio](https://build-folio.com/contractor-guides/electrical-contractor-pricing-guide/)
- [EV Charger Installation Cost (2026), ChargeRight](https://evchargeright.com/blog/ev-charger-installation-cost)
- [The 2026 Google Guaranteed Playbook for $39 Leads, Pipeline On](https://pipelineon.com/blog/local-service-ads-electrician/)
- [Facebook Ad Mistakes Home-Service Businesses Make, Hook Agency](https://hookagency.com/blog/facebook-ad-mistakes/)
- [Why Stock Photos Are Costing Contractors Jobs, Hook Agency](https://hookagency.com/blog/why-stock-photos-are-costing-contractors-jobs-and-what-to-use-instead/)
- [10 big mistakes contractors make with Facebook ads, ServiceAllies](https://www.serviceallies.com/blog-posts/10-common-mistakes-when-running-meta-ads)
- [25 HVAC Promotion Ideas and HVAC Marketing Strategies, ServiceAllies](https://www.serviceallies.com/blog-posts/25-ideas-for-hvac-promotions)
- [HVAC Facebook Advertising Complete Guide, ClicksGeek](https://clicksgeek.com/hvac-facebook-advertising/)
- [Meta Ads Learning Phase Budget: How Much to Spend (2026), AdsGo](https://www.adsgo.ai/blog/meta-ads-learning-phase-budget-how-much-to-spend/)
- [Meta Ads Minimum Budget 2026: How Much You Really Need, Get Ryze](https://www.get-ryze.ai/blog/meta-ads-minimum-budget-guide-starting-budget)
- [Seasonal search shifts in home services demand, Stacker/ABC17](https://abc17news.com/stacker-small-business/2026/02/23/seasonal-search-shifts-in-home-services-demand-what-spikes-when-and-how-to-stay-booked-year-round/)
- [Seasonal search shifts in home services demand, WebFX](https://www.webfx.com/blog/home-services/seasonal-search-trends/)

Plus every source already cited in `research/04-domain-and-economics.md`, referenced above
wherever a figure is marked [VERIFIED].

---

## OPERATOR CORRECTION, verified 2026-08-19

The agent flagged "home built in year range" as possibly fabricated blog content. It was right
to be suspicious, and the real situation is broader and more damaging to the targeting
sections of this document.

**Verified against multiple 2026 sources:**

1. **Homeownership targeting no longer exists.** Meta stripped Partner Categories entirely,
   removing roughly half of about 1,200 targeting criteria, homeownership status among them.
   Every "homeowner signal" recommendation in this document rests on a field that is gone.
   What remains is proxy interest stacking (home improvement pages, HGTV, Lowe's engagement,
   recently-moved signals), which is far weaker and far less precise.
2. **Advantage Detailed Targeting is forced on** for conversion and link-click objectives as of
   January 2026. Advertisers cannot turn it off. Any audience we specify is a suggestion Meta
   is free to expand past.
3. **Detailed Targeting Exclusions were removed entirely** by 31 January 2026. You cannot
   exclude by interest at all any more.
4. **Special Ad Category Housing** strips age, gender, ZIP, and income targeting, and imposes a
   15 mile minimum radius. Relevant wherever a trade offer touches housing or financing.

Sources: [Web Blend](https://webblend.au/blog/meta-ads-targeting-changes/),
[Hook Agency](https://hookagency.com/blog/targeting-homeowners-facebook/),
[LeadSync](https://leadsync.me/blog/facebook-ads-targeting-guide/)

### What this means for the product

**Audience micro-targeting is no longer a lever we can pull on the owner's behalf.** Meta took
the steering wheel. This does not weaken the product, but it relocates where its value lives.

The defaults that still genuinely matter, and where the smart-defaults engine should
concentrate:

- **Geography and radius**, still fully controllable and still the highest-value setting
- **The offer**, entirely ours, and the single biggest driver of whether the phone rings
- **Creative**, images and copy, entirely ours
- **Budget and pacing**, still controllable
- **Objective and optimization goal**, still a real choice
- **Lead form design and qualifying questions**, entirely ours and the main lever on lead quality
- **Seasonal and event timing**, especially roofing storm response

The defaults that are now mostly theatre and should NOT be sold as sophistication:

- Interest stacking, since Advantage will expand past it anyway
- Age and gender narrowing, low value and blocked outright under Special Ad Category
- Any exclusion-based strategy, which is no longer possible

This independently confirms the finding in `docs/00-RESEARCH-SYNTHESIS.md` that mechanical
optimization has been commoditized by the platforms. Our value is offer, creative, plan, and
lead-form design. Say that plainly rather than implying targeting wizardry we cannot deliver.

**Every targeting recommendation above must be re-read with this correction applied.**
Items 3 and 5 of FOUNDER MUST CONFIRM are resolved by this note: item 3 is confirmed as not a
usable field, item 5 is largely moot under Special Ad Category and Advantage expansion.
