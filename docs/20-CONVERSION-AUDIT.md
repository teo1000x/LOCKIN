# Conversion Audit: the landing page, the competitive set, and the evidence

Compiled 2026-08-19. Audits `~/Projects/ignition/src/app/page.tsx` and every component it
imports, against pacerev.com and five other live competitor pages, against published CRO
evidence, and against the constraints in `AGENTS.md` (zero customers, no refunds, no
fabricated statistics).

Written to be useful, not encouraging. Every external claim carries an inline URL. Anything
not sourced is tagged `[INFERENCE]` or `[ASSUMPTION]` on the line where it appears.

**A note on source quality before you read the numbers.** Conversion research is dominated by
SEO content farms recycling each other's figures. Where a number traces to a real study with a
stated sample (Nielsen Norman Group, Unbounce's own dataset, HockeyStack Labs, Edelman/LinkedIn)
I say so. Where it only appears in aggregator blogs with no visible methodology, I say that too,
and you should treat it as directional at best. Several of the claims most flattering to the
recommendations below are in the second category. I have not laundered them.

---

## 1. Competitive teardown

### The table

| | Leads with | Price shown on page | Proof used | Primary CTA | Guarantee | Best single thing |
|---|---|---|---|---|---|---|
| **PaceRev** ([pacerev.com](https://pacerev.com)) | "PaceRev runs your Facebook ads. You book the jobs." Badge above it: "Done-for-you Meta ads, run on your own Facebook account" | Yes. $699 / $1,499 / $2,499 per month, plus add-ons: extra campaign +$79/mo, extra business +$149/mo | A stats band: "1,000+ businesses served", "10 to 40x return on ad spend", "100% exclusive leads". No testimonials, no logos, no case studies, no video. Six fabricated-looking sample businesses with generated ad mockups | "Start getting leads" (pricing and body), "Book a call" (header) | No refund guarantee. Instead a value framing: "For most businesses, one new customer covers PaceRev for an entire year", asterisked to "Based on a typical customer value against an annual plan. Varies by business and ticket size" | The stats band. Three numbers in the highest-value slot on the page that answer scale, return, and exclusivity in one glance. Unsourced, but it does the job the slot exists for |
| **Podium** ([podium.com/pricing](https://www.podium.com/pricing/)) | "AI lead conversion with every plan" | No. "Plans designed to fit your specific business needs, talk to our sales team for details" | Heavy. "Over 100,000 businesses", named brand logos (La-Z-Boy, Ashley Furniture, Mattress Firm), and six named-customer outcome lines including "Mountaineer HVAC: 20% more weekly sales calls & $96K additional monthly revenue" | "Get a demo", "Watch a demo" | None stated | The named-customer outcome format. Company name plus one number plus one dollar figure. Concrete, attributable, repeatable |
| **Hatch** ([usehatchapp.com](https://www.usehatchapp.com/)) | "The AI CSR platform for service businesses" / "Scale conversion, not headcount, with AI CSRs across voice, SMS, and email." | No. Book-a-demo only | Customer logos organised by customer revenue band ($1-10M, $10-50M, $50-100M, $100M+). Named case studies with a single stat each: High Ground 81% of leads booked by AI, Bone Dry Roofing $7M rehash revenue, Peaden 3x conversion on after-hours calls. Review score shown: "Rated 4.3 (76 Reviews)" | "Get a demo" | None stated | Segmenting logos by revenue band. A $2M roofer sees other $2M roofers, not enterprise logos that read as "not for me" |
| **Broadly** ([broadly.com/pricing](https://www.broadly.com/pricing/)) | Flat single price, stated plainly | Yes. "$799 /month", reframed as "Roughly $26/day" | "Over 16,000 local pros use Broadly". Google / Capterra / G2 rating badges. Three named testimonials with specifics, e.g. Blessed Oasis Pet Resort going from 151 to 239 Google reviews in two months. Integration logos (ServiceTitan, Jobber, QuickBooks) | "Book a demo", "Get Started For Free" | Yes, and it is the strongest in the set: "no long-term contract", "cancel anytime if you're not seeing value", and "If you don't see value in your first month, you can cancel and stop being billed, no fees, no questions" | The daily reframe plus the first-month cancel. $799/mo becomes $26/day and the downside becomes zero, without ever promising a refund |
| **Housecall Pro** ([housecallpro.com/pricing](https://www.housecallpro.com/pricing/)) | Transparent three-tier pricing | Yes. $59 / $149 / $299 per month billed annually ($79 / $189 / $329 monthly), with per-seat overage stated | "Trusted by 200,000+ Pros". Capterra 4.7 stars from 2,700+ reviews. Three named testimonials with first name, last initial, and company. Aggregate claims: "35% avg. revenue growth after the first year", "8+ avg. hours saved per week" | "Start Free Trial", "Book a Demo" | "Try 14 days free. No credit card required. Cancel anytime." No money-back guarantee | The rating block. A number, a star score, a review count, and a source, in one line, above the price |
| **Thryv** ([thryv.com/pricing](https://www.thryv.com/pricing/)) | Transparent entry price, custom top tier | Yes. $99 / $399 / custom, 15% annual discount | "100,000+ Businesses", "4.8 average rating", one named testimonial (Mark Martin, Interior Tropical Gardens) | "Start free trial", "Talk to Sales", "Get a Demo" | Two-week trial, framed conversationally | Publishing a real entry price ($99) while keeping the top tier custom. Anchors low, negotiates high |

Also examined, as evidence of what the trust-damaged end of this market does:
[Home Service Direct](https://www.homeservicedirect.net/) sells on "If you don't see qualified
leads in 30 days, we'll work for free until you do", and
[Brands That Last](https://brandsthatlast.com/) on "We generate your full investment back in 90
days, or we work for free." Both are results guarantees we cannot and must not copy under
`AGENTS.md` rule 3, but they set the risk-reversal expectation this buyer walks in with.

### Where the gap actually is

Every company above sits in one of two buckets. Bucket one, Podium and Hatch, hides price and
sells to a sales team, which works because they are selling to $10M-plus operators with a
budget line for software. Bucket two, Broadly, Housecall Pro and Thryv, publishes a price under
$800 and sells self-serve to everyone, which works because at $99 to $799 the decision is
reversible enough to make on a phone.

PaceRev is the only company in the set trying to do a third thing: publish a $699 to $2,499
price and sell it self-serve to a single-location owner, with no testimonials, no logos, no
case studies, no video and no refund. It does that by putting three unsourced numbers in the
band under the hero and hoping they hold the weight. That is not a gap in the market, that is a
company betting nobody checks. [INFERENCE]

The actual gap is narrower and more defensible: **nobody in this set shows the buyer anything
real about their own market before asking for money.** Podium shows other people's results.
Hatch shows other people's logos. Broadly shows other people's review counts. PaceRev shows
sample ads for six invented businesses. Not one of them shows the prospect what is happening in
their own postcode. The competitive read described in `docs/12-THREE-PS.md` Section 1 is the
only asset in this competitive set that is proof of mechanism rather than a claim about
outcomes, and it is currently buried behind a nav link labelled "Results" that goes to an
estimator. That is the gap, and the page does not occupy it.

The second gap is the trust position itself. Broadly is the only competitor with a genuinely
strong risk reversal, and it is prospective rather than retrospective: cancel in month one and
stop being billed. That is compatible with an all-sales-final policy and nobody in this
category besides Broadly is using it. More on that in Section 3.

---

## 2. The cracks in our page, ranked by how much money they cost

Ranked by expected revenue lost, which is roughly (share of visitors affected) times (severity),
not by how easy each is to fix. Line references are to files under
`~/Projects/ignition/src/`.

---

### 1. Every conversion path on the site dead-ends. There is no way to buy and no way to book.

`SiteHeader.tsx:34-39`, `Hero.tsx:41-46`, `Pricing.tsx:161-170` all point at `/book`.
`app/book/page.tsx:78-96` then says the scheduler is not connected and offers
`tel:+15125550100` and `mailto:hello@foreman.example`. `555-0100` is a reserved fictional number
([North American Numbering Plan 555 line assignments](https://www.nationalnanpa.com/number_resource_info/555_numbers.html))
and `foreman.example` is a reserved non-routable domain
([RFC 2606](https://datatracker.ietf.org/doc/html/rfc2606)). A visitor who is fully sold, has
read the whole page, and wants to hand over $1,300 a month has nowhere to do it.

**Cost:** 100% of conversions. Every other item on this list is downstream of this one.
**Fix:** Wire a real scheduler and a real phone number before anything else on this list. If the
scheduler cannot be wired this week, replace the whole `/book` right column with a two-field
form (name, phone) that emails the founder. Do not ship a fictional phone number on a page whose
entire pitch is that we do not deceive contractors.

---

### 2. The only tier a single-location owner can afford is marked sold out, at zero customers.

`Pricing.tsx:31-32` sets `soldOut: true` with the note "Starter is capped at 20 accounts so
support stays real. Currently full." `Pricing.tsx:153-159` replaces the buy button with a
disabled "Join the waitlist" span that is not a link and does not go anywhere.

The comment at `Pricing.tsx:26-30` says "Keep this true: if Starter is not actually full, set
soldOut to false." The product has zero customers per `AGENTS.md`. So either the claim is false,
which detonates the transparency positioning the whole page is built on, or it is true in some
technical sense and the effective entry price for the target buyer defined in
`docs/09-SIX-PS.md` (single-location owner-operator) is $1,300 a month.

This mechanic was copied from PaceRev, whose Launch plan at $699 is also marked "Sold out". They
can carry it because they claim 1,000+ businesses served. We cannot.

**Cost:** The largest single revenue leak on the page after item 1. `docs/12-THREE-PS.md`
Section 3 assumes 70% of the early cohort buys the entry tier. That 70% currently cannot buy.
**Fix:** Set `soldOut: false`. If capacity is genuinely the concern, cap it honestly with a
number that is true ("3 of 20 Starter accounts open") and make the button work.

---

### 3. Zero social proof of any kind. No testimonial, no logo, no name, no face, no rating.

Search the entire component tree: there is not one customer name, one photo, one quote, one
star rating, one review count, one integration logo, or one third-party badge anywhere on
`page.tsx` or any of its twelve imported components. Every competitor in Section 1 has at least
three of those. Housecall Pro leads its pricing page with a Capterra score and a review count.
Hatch shows a 4.3 from 76 reviews, which is a mediocre score they publish anyway because
publishing a mediocre real score beats publishing nothing.

Nielsen Norman Group's eyetracking research (120 participants, 130,000+ fixations) found 57% of
page-viewing time is spent above the fold and 74% within the first two screenfuls
([nngroup.com](https://www.nngroup.com/articles/scrolling-and-attention/)). Our first two
screenfuls contain a headline, a lede, two buttons, a sample dashboard labelled as sample data,
three icon claims about ourselves, and four statistics about our own research process. Nothing
from a third party.

Documented A/B tests attribute large lifts to adding testimonials (Groove 2.3% to 4.7%,
ContentVerve +64.53% from placement alone) but I could only find these repeated in aggregator
posts such as [saashero.net](https://www.saashero.net/content/landing-page-social-proof-examples/)
without access to the primary write-ups, so treat the magnitudes as unverified. The direction is
not in dispute.

**Cost:** High and permanent until fixed. A trust-damaged buyer with no third-party signal has
no reason to believe any sentence on the page.
**Fix:** You cannot fabricate customers. You can, this week, put the founder's real full name,
real photo, and a link to a verifiable public profile in the hero, and you can add third-party
identity signals that do not require customers (Section 3). Within 30 days, three named design
partners with photos and written case-study rights, per `docs/09-SIX-PS.md` Proof section.

---

### 4. The page is a near-verbatim clone of pacerev.com, including the headline.

Side by side:

| | PaceRev | Foreman |
|---|---|---|
| Hero headline | "PaceRev runs your Facebook ads. You book the jobs." | `Hero.tsx:31` "Foreman runs your Facebook ads. You book the jobs." |
| Hero badge | "Done-for-you Meta ads, run on your own Facebook account" | `Hero.tsx:25-28` "Facebook and Instagram ads, run in your own account" |
| Section order | hero, value prop, dashboard shot, benefits, comparison table, ROI band, four-step how it works, trades, features, multi-business, pricing, FAQ, footer | `page.tsx:36-85` hero, value band, numbers band, comparison table, four-step walkthrough, ad showcase, pricing, features, trades, FAQ, footer |
| Comparison table columns | Agency / DIY / Shared services | `Comparison.tsx:70-81` "Marketing agency" / "Running them yourself" / "Shared lead services" |
| Entry tier state | Sold out | `Pricing.tsx:31` `soldOut: true` |
| Dashboard numbers | 47 leads this month, +14 this week, 16 booked customers, cost per lead down | `DashboardPreview.tsx:16-18` "47" leads, "+14 this week", "16" booked jobs, "$31" cost per lead, "down from $44" |
| Pricing footnote | cancel anytime, no contracts, ad spend separate and billed to the card on your own Facebook ad account | `Pricing.tsx:177-180` "Cancel anytime, no contracts. Ad spend is separate and goes on the card attached to your own Meta ad account, never through us." |

`Hero.tsx:6-12` and `Walkthrough.tsx:6-9` both state in comments that the layout follows "the
reference the founder chose". Following a reference is fine. Reproducing a competitor's headline
with one noun swapped is not a reference, and the dashboard sample numbers matching theirs
digit-for-digit is not coincidence.

**Cost:** Two ways. First, any prospect who has seen both pages, which in a category this small
is a meaningful share, concludes we are the copy and they are the original. Second, headline and
layout copying at this density is the kind of thing a competitor's lawyer sends a letter about,
and a startup with no customers cannot absorb that. [INFERENCE, I am not a lawyer and this is
not a legal opinion]
**Fix:** Rewrite the headline around the one thing PaceRev does not have and does not market:
the competitive read. Change the sample dashboard figures. Reorder the page per item 12 below.

---

### 5. Pricing is invisible until roughly the seventh scroll section.

`page.tsx:77` places `<Pricing />` after the hero, value band, numbers band, comparison table, a
four-step walkthrough with four full-width panels, and the ad showcase. There is a nav link at
`SiteHeader.tsx:12`, but nothing in the hero states a price, a range, or a floor.

HockeyStack Labs analysed 31 million unique visitors across 80 B2B SaaS companies and found
hidden-pricing pages generate 64% more form submissions but convert those to pipeline at 1.7x
lower rates
([hockeystack.com](https://www.hockeystack.com/lab-blog-posts/state-of-pricing-demo-case-study-pages)).
That is the closest thing to primary evidence in this whole audit. Broadly, Housecall Pro and
Thryv all publish an entry price. Only Podium and Hatch hide it, and both sell to a different
buyer with a sales team attached.

Our buyer is described in `AGENTS.md` as "non-technical trades owners reading on a phone between
jobs" and in `docs/09-SIX-PS.md` as price-sensitive and burned. For that buyer, price is the
first question, not the seventh.

**Cost:** Every visitor who scrolls two screens, does not find a number, and leaves. Given the
NN/g figure that 26% of viewing time falls beyond the second screenful, a large share never
reaches `Pricing.tsx` at all.
**Fix:** One line under the hero CTAs: "From $499 a month. Ad spend is separate and goes on your
own card." That is nine seconds of work and it pre-qualifies every visitor.

---

### 6. No risk reversal at all, on top of an explicit all-sales-final policy.

`app/refunds/page.tsx:23-33` states every card payment is final including the first, with no
trial refund, no satisfaction refund, and no money-back guarantee. The landing page does not
mention this at all. The only place it surfaces on a conversion path is
`app/book/page.tsx:104-109`.

So the ask is: $499 to $1,300 a month, from a company with no customers, no testimonials, no
video, a fictional phone number, and no refund. Against Broadly's "If you don't see value in
your first month, you can cancel and stop being billed, no fees, no questions"
([broadly.com/pricing](https://www.broadly.com/pricing/)), Housecall Pro's "14 days free, no
credit card required" ([housecallpro.com/pricing](https://www.housecallpro.com/pricing/)), and
the contractor agencies promising to work for free until leads arrive.

The refunds page is honest and well written and the reasoning in its header comment is sound.
That does not change the arithmetic the buyer does.

**Cost:** Severe at these price points. A published case study reports a visible 30-day
money-back guarantee raising sales 21% with 12% requesting refunds, but it appears only in
secondary write-ups such as
[revenueflows.ai](https://revenueflows.ai/blog/does-money-back-guarantee-increase-shopify-conversion-rate)
with no primary source, so treat the number as unverified. The direction is well established.
**Fix:** You do not need a refund to have a risk reversal. See Section 3, mechanism 2. The
shortest version: do not charge the card until the first ad is approved and live in the owner's
account. Money never taken is never refunded, so the all-sales-final policy stands untouched.

---

### 7. No email capture anywhere. The only conversion offered is a phone call.

There is no email field on `page.tsx` or any component it imports. The secondary CTA
(`Hero.tsx:47-52`) goes to `/estimate`, which is a client-side calculator that captures nothing
(`app/estimate/page.tsx`). `Trades.tsx:117-122` offers "Open the demo" at `/app`, which also
captures nothing.

`docs/12-THREE-PS.md` Section 2 already decided this: "A one-time, ungated, single
competitive-read report... ships as a free lead magnet, no login beyond an email address
required. This is the cheapest, highest-leverage top-of-funnel asset available with zero
customers." The page does not implement it.

Unbounce's own dataset (41,000 landing pages, 464 million visitors, 57 million conversions, Q4
2024) puts the median landing page conversion rate at 6.6%
([unbounce.com](https://unbounce.com/average-conversion-rates-landing-pages/)). Even at that
median, roughly 93 of every 100 visitors leave. Right now all 93 leave with no trace and no way
to be contacted again.

**Cost:** The entire remarketable audience. At a pre-launch stage with no paid acquisition, this
is the difference between a list and nothing.
**Fix:** Ship the single-field email gate on the competitive read. Aggregator summaries of
Unbounce's benchmark data put single-field forms at 13.4% versus 10.1% at three fields and 5.3%
at seven ([digitalapplied.com](https://www.digitalapplied.com/blog/form-conversion-rate-benchmarks-2026-data-points)).
I could not find these figures on unbounce.com itself, so treat the exact percentages as
secondhand, but "ask for one field, not five" is not a controversial position.

---

### 8. No video, and the one asset that proves the mechanism is never shown running.

Nothing on the page moves except `Reveal.tsx` scroll transitions and the `AdShowcase.tsx` tab
switcher. There is no product walkthrough, no screen recording, no founder to camera.
PaceRev has no video either, so this is parity rather than disadvantage, but parity with a
company that has 1,000 claimed customers is a losing trade for a company with zero.

`docs/12-THREE-PS.md` Section 1 is explicit that "the competitive read is the strongest
zero-customer proof asset in the product, because it is not a claim, it is a live artifact. A
prospect can watch it pull real, current ads from real nearby competitors, using public Meta Ad
Library data, during a demo." The Ad Library read needs no App Review and no customer
permission. It is buildable today and it is nowhere on the page.

Video lift figures circulate widely (a Vidyard/Unbounce case study is cited as 6.5% to 11%
inline and 6.5% to 13% in a lightbox, per
[unbounce.com](https://unbounce.com/conversion-rate-optimization/case-study-using-video-to-lift-landing-page-conversion-rate-by-100/)),
but that is a single case study, not a benchmark, and the aggregators repeating it inflate it.
Wistia's engagement data across 13M+ videos showing engagement dropping sharply past 120 seconds
is the more useful number
([chiefmarketer.com summary](https://www.chiefmarketer.com/wistia-state-of-video-report-engagement-down-content-under-promoted/)).

**Cost:** Moderate on its own, large in combination with item 3. Video is how a company with no
testimonials substitutes founder presence for customer proof. [INFERENCE]
**Fix:** One 60-second screen recording: type a real trade and a real postcode, watch real
competitor ads load from the Ad Library, then the plan, then the ad, then the approval screen.
No music, no voiceover script, founder's actual voice. Keep it under 90 seconds.

---

### 9. The page describes a product that does not exist yet, and contradicts itself doing it.

`Faq.tsx:23` carries the interim note: "Publishing into your account is pending Meta's app
review. Until that clears we build the campaign and walk you through posting it yourself."
Correct and required by `AGENTS.md`.

But `Walkthrough.tsx:44-52` presents step 3 as "Every lead lands in one inbox you own", present
tense, with a `LeadsPanel` mockup. `Walkthrough.tsx:54-63` presents step 4 as "We watch it,
adjust it, and show our work", with "Budget moves toward the ads that are actually booking
jobs". `DashboardPreview.tsx:22-26` shows "Built and published 5 ads you approved" and "Shifted
budget to your 2 best performers".

Meanwhile the header comment at `Pricing.tsx:6-9` states, in the same repository: "We do not
optimise ads daily and we do not run a leads inbox, so neither appears here." The pricing
feature lists honour that. The walkthrough two sections above them does not. `Trades.tsx:117-122`
then sends people to `/app`, which `AGENTS.md` documents as mock data only with no auth behind
it, labelled on the page as "Open the product with a sample HVAC campaign already built."

**Cost:** This is not primarily a conversion cost, it is a refund-dispute and chargeback cost,
which on an all-sales-final policy is worse. A contractor who buys on the strength of steps 3
and 4 and finds neither exists has a straightforward complaint.
**Fix:** Either move steps 3 and 4 behind a clearly labelled "what ships when App Review clears"
frame, or hoist the App Review note out of FAQ answer one into the walkthrough itself. Right now
the single most important caveat on the site is inside a collapsed `<details>` element.

---

### 10. Nothing on the page says this is a real company run by a real person.

No founder name. No photo. No company address. No registered entity. No team page. No LinkedIn.
The footer (`SiteFooter.tsx:63-70`) gives a copyright line and a Meta non-affiliation
disclaimer. The contact details are a 555 number and an `.example` domain. `AGENTS.md` notes the
product name is a placeholder and the domain is not owned.

Compare: Broadly leads with "Over 16,000 local pros", Housecall Pro with "Trusted by 200,000+
Pros" plus a Capterra score, Hatch with a review count. CXL's original trust-seal research and
Baymard's work on perceived security both find that recognisable third-party marks raise
perceived trustworthiness, and Baymard's checkout research found 19% of US shoppers abandoned an
order because they did not trust the site with their card
([baymard.com](https://baymard.com/blog/perceived-security-of-payment-form)). We currently
present a card-taking business with fewer identity signals than a personal blog.

The Edelman/LinkedIn 2025 B2B Thought Leadership report (n=1,934 management-level professionals,
seven markets) found 53% of decision-makers said strong thought leadership mattered more to them
than brand name recognition
([edelman.com](https://www.edelman.com/expertise/Business-Marketing/2025-b2b-thought-leadership-report)).
That is the closest defensible evidence that a named, credible individual can substitute for
company scale. It is not the same claim and I am not going to pretend it is.

**Cost:** Compounds with items 3 and 6. A buyer who cannot verify who they are paying, cannot
get a refund, and cannot see another customer, does not pay.
**Fix:** Founder name, face, and a real phone number in the hero or immediately under it. Real
registered entity and address in the footer. This costs nothing and is the single highest
ratio-of-trust-to-effort change available.

---

### 11. Nowhere does the page say who this is not for.

The trades section (`Trades.tsx:58-64`) says the opposite: "If you sell a service inside a
service area, this works... Anything not on the list still runs." The dashed card at
`Trades.tsx:78-90` says "It almost certainly still works."

The real disqualifier is money, and it is buried. `Faq.tsx:39` ("budget for your subscription
plus at least $1,000 a month in ad spend") and `Faq.tsx:47` ("Below roughly $1,000 a month, Meta
does not gather enough results to improve and you are mostly buying noise") are both inside
collapsed FAQ items at positions five and seven. So the total real cost of entry, $499 plus
$1,000 minimum, appears nowhere a scanning visitor will see it.

**Cost:** Two-sided. Unqualified prospects consume founder call time that a solo operator does
not have. Qualified prospects who would happily spend $1,500 a month never learn that this is
priced for them and not for the $200-a-month Boost Post crowd. Naming a floor is also a status
signal that raises perceived value. [INFERENCE]
**Fix:** A short honest block: "This is not for you if your whole marketing budget is under
$1,500 a month, if you want someone else to approve the ads for you, or if you need leads this
week." `docs/09-SIX-PS.md` already commits to disclosure over concealment. This is that.

---

### 12. The second screenful, the most valuable real estate after the hero, is spent on facts about our research process.

`page.tsx:24-29` and `ValueBand.tsx:23-42` together occupy roughly the whole second screenful
with seven statistics: "400+ local businesses advertised for", "100% of your leads are yours
alone", "$0 of your ad budget goes to us", "1,548 days", "46 real ads", "4 researched", "Any
local service business".

NN/g measured the second screenful at about 17% of total viewing time and the first two
screenfuls at 74% ([nngroup.com](https://www.nngroup.com/articles/scrolling-and-attention/)).
We are spending the second-most-valuable slot on the page on "46 real ads read line by line in
the Meta Ad Library" and "the longest-running contractor ad we found is still live for 1,548
days".

A contractor does not care how many ads you read. The "400+ local businesses advertised for"
statistic is the strongest thing in the block by a wide margin and it is one of seven, sharing
a row with two abstractions. The framing decision documented in `ValueBand.tsx:5-11`, attributing
it to the operator in the first person rather than to the product, is correct and should not be
loosened. But it should not be competing with "46".

**Cost:** Moderate. This is dilution, not damage.
**Fix:** Cut the `NUMBERS` band at `page.tsx:24-63` entirely or move it far down. Promote the
400-businesses line to the hero, in first person, with the founder's name attached: "I have
personally run Facebook ads for more than 400 local service businesses. This is that, as
software." Move "46 real ads" and "1,548 days" into the ad showcase where they support the copy
rationale, which is where they actually earn their place.

---

### 13. The nav link labelled "Results" goes to a calculator.

`SiteHeader.tsx:10` maps the label "Results" to `/estimate`. `app/estimate/page.tsx:20-27`
is an input-driven estimator that returns offer structures and budget guidance. It contains no
results.

In a category where `docs/09-SIX-PS.md` Pain 2 is literally "junk leads dressed up as real ones"
and Pain 3 is not knowing whether the money is working, a nav item that promises results and
delivers a calculator is the exact bait-and-switch shape this buyer is primed to detect. It is
also the highest-intent click on the nav bar, because a burned contractor checks results first.

**Cost:** Small in volume, high in the specific segment that clicks it, which is the most
skeptical and most valuable segment.
**Fix:** Relabel to "Estimate" or "See your market". Do not use the word Results until there are
results.

---

### 14. The sample dashboard shows the competitor's numbers.

`DashboardPreview.tsx:15-19` shows 47 leads this month, +14 this week, 16 booked jobs, $31 cost
per lead down from $44. PaceRev's dashboard screenshot shows 47 leads this month, +14 this week,
16 booked customers, cost per lead down. The sample-data label at `DashboardPreview.tsx:34-39`
is honest and the header comment explaining why the label is mandatory is exactly right. The
numbers underneath it are somebody else's.

`DashboardPreview.tsx:112-117` then adds a banner reading "More booked jobs, at a lower cost per
lead", which is a performance claim rendered as a product feature. It is inside a frame labelled
sample data, so it is not a rule 3 violation, but it is the closest the page comes to one.

**Cost:** Low in isolation, but it is the item that makes item 4 undeniable if anyone compares.
**Fix:** Change the figures. Change the framing of the banner from an outcome to a mechanism.

---

### 15. There is no reason to act today, and the only scarcity present pushes people away.

No deadline, no cohort, no founding-member window, no price-lock offer, no limited onboarding
slots. The one scarcity mechanic on the page (`Pricing.tsx:31-32`, the sold-out Starter tier)
removes an option rather than creating a reason to move.

`docs/12-THREE-PS.md` Section 3 already specifies a real, honest, time-bound offer: design
partners get their price locked for 24 months in writing, stated at signup, explicitly not a
teaser that expires quietly. That is a legitimate urgency mechanic grounded in a real commitment,
and it appears nowhere on the page.

**Cost:** Moderate. Fake urgency is worse than none for this audience, which is why the page is
right to avoid countdown timers. Real urgency is still missing.
**Fix:** "First ten customers: this price, locked in writing for 24 months. Nine remaining." Only
ship it with a real number that decrements truthfully.

---

## 3. The trust problem specifically

The position is: no customers, no results, no refund, high price, a category the buyer has
already been burned in twice. `docs/09-SIX-PS.md` documents the pattern in verbatim complaints:
paying for months with nothing to show, junk leads, black-box reporting, lock-in, and billing
that feels like theft.

The instinct is to solve this with a guarantee. You cannot, because the founder has ruled out
refunds. The good news is that a guarantee is only one of several mechanisms, and it is not the
strongest one available to a company in this specific position. Five concrete, buildable
mechanisms, in order of impact per unit of effort.

### 1. Do not take the money until the thing exists. Authorise, do not charge.

The all-sales-final rule constrains refunds. It says nothing about when you charge. Collect card
details at signup, place a hold or a zero-dollar authorisation, and take the first payment only
when the owner has approved their first ad and it is live in their own Meta account. If they
never approve anything, they are never charged, and there is nothing to refund.

This is functionally what Broadly promises ("If you don't see value in your first month, you can
cancel and stop being billed, no fees, no questions",
[broadly.com/pricing](https://www.broadly.com/pricing/)) except stronger, because Broadly bills
first and you would not. It is the single best available answer to `docs/09-SIX-PS.md` Pain 1
(paying for months with nothing to show) and Pain 5 (billing that feels like theft), and it
costs nothing when the product works.

Buildable now: it is a Stripe `setup_intent` at signup and a `payment_intent` fired by the same
approval record that `publish-guard.ts` already persists. The approval gate is already the
system of record for "the owner said yes", so tie billing to it. [INFERENCE on the exact Stripe
mechanics; verify against current Stripe docs before building]

### 2. Publish the scope of access as a specific, checkable list, and show the revoke path.

`Faq.tsx:27` already does this well in prose: authorised on Facebook's own screen, no password
seen, covers ads and ad results only, not the personal profile, not messages, not friends, not
the page inbox, revocable in two clicks. `AGENTS.md` inviolable rule 2 makes this a binding
implementation constraint rather than marketing copy, which is unusual and valuable.

Turn it into a standalone page with the exact Meta permission scope names we request, a
screenshot of Meta's own authorisation dialog, a screenshot of the Facebook settings screen
where access is revoked, and a plain statement of what we technically cannot do (raise a daily
budget, change a payment method). Link it from the hero, not the FAQ.

Why this works here specifically: this buyer's fear is not that the ads fail, it is that they
cannot tell what is happening and cannot get out. A checkable permission list is verifiable by
the buyer against Meta's own screens, which makes it the rare trust claim that does not require
trusting us.

### 3. Run the competitive read live, in public, with no signup.

Already decided in `docs/12-THREE-PS.md` Section 2 and Section 1, already technically unblocked
(public Meta Ad Library data, a token we hold, one-time founder identity verification, no App
Review), and still not built. It is the only proof asset in the entire competitive set that
shows the prospect something true about their own market before they pay.

Gate it at one field, an email, not five. Aggregator summaries of Unbounce benchmark data put
single-field forms at 13.4% against 5.3% at seven fields
([digitalapplied.com](https://www.digitalapplied.com/blog/form-conversion-rate-benchmarks-2026-data-points));
secondhand, treat magnitude as unverified.

This solves the trust problem sideways. It does not ask the buyer to believe a claim. It hands
them a fact about their own postcode that they can verify by opening the Ad Library themselves.

### 4. Founder identity, verifiable, in first person, above the fold.

Full name, real photograph, a real phone number that rings, and a link to a public profile with
a checkable history. Then the 400-businesses claim in first person, exactly as
`ValueBand.tsx:5-11` insists, attached to that name.

The supporting evidence here is weaker than I would like. The Edelman/LinkedIn 2025 report
(n=1,934) found 53% of decision-makers rate strong thought leadership above brand name
recognition and 64% trust thought leadership more than product sheets
([edelman.com](https://www.edelman.com/expertise/Business-Marketing/2025-b2b-thought-leadership-report)),
which is adjacent but not the same claim. Everything I could find that directly addresses
"founder-attributed track record versus company stats" is marketing-blog content with no
methodology, for example [revboss.com](https://revboss.com/blog/how-founder-brands-build-trust-through-content).
**The evidence for this recommendation is thin.** The argument for doing it anyway is structural
rather than empirical: we have no company stats to attribute, so the founder's record is the
only true proof asset in the building. [INFERENCE]

### 5. Third-party identity marks that do not require customers.

Ranked by what is obtainable before a first sale:

- A real registered legal entity, named with its address, in the footer.
- A Stripe-hosted checkout so the card form is visibly not ours. Baymard found 19% of US
  shoppers abandoned an order over card trust
  ([baymard.com](https://baymard.com/blog/perceived-security-of-payment-form)).
- BBB accreditation. It requires no customers and it is the mark this specific audience
  recognises, because BBB complaints are how they research vendors in the first place
  (`docs/09-SIX-PS.md` cites BBB complaints against Scorpion and the 1,200-plus against the lead
  marketplaces).
- Meta Business Partner status the day App Review clears, which turns the compliance queue on
  the critical path into a marketing asset.
- A G2 or Capterra listing, created now and left empty until real usage exists, per
  `docs/09-SIX-PS.md` Proof rule 6.

CXL's original trust-seal research and Baymard's 2013-2022 series both find that recognisable
marks raise perceived trustworthiness and that even a generic unfamiliar seal raised it somewhat
([cxl.com](https://cxl.com/research-study/trust-seals/), summarised at
[trustsignals.com](https://www.trustsignals.com/blog/trust-badges-work-and-we-have-the-receipts-to-prove-it)
because cxl.com blocked direct fetch). Both are ecommerce checkout studies, not B2B SaaS landing
pages, so the transfer is an assumption. [ASSUMPTION]

**One thing to stop doing.** The refunds page reasoning at `app/refunds/page.tsx:11-16` says a
final-sale term discovered after paying is what produces chargebacks. That is correct and it
means the term belongs on the pricing section, not only on a linked legal page. Putting "all
payments are final" next to the price, with mechanism 1 above sitting beside it, converts the
weakest fact on the site into a statement of confidence. Hiding it converts it into a dispute.

---

## 4. What we should steal, and what we should not

### Steal

**From Broadly.** The prospective cancel guarantee, verbatim in structure: cancel in your first
month and stop being billed, no fees, no questions
([broadly.com/pricing](https://www.broadly.com/pricing/)). It is the only risk reversal in the
competitive set that survives an all-sales-final policy intact. Also steal the daily reframe,
"$799/month, roughly $26/day". At $499 that is roughly $16 a day, which is less than a single
shared lead on Angi.

**From Housecall Pro.** The proof block shape: customer count, star score, review count, source
name, all in one line, above the price
([housecallpro.com/pricing](https://www.housecallpro.com/pricing/)). Build the empty version of
that block now so it is ready the day there is something true to put in it.

**From Hatch.** Segmenting proof by the customer's own size band
([usehatchapp.com](https://www.usehatchapp.com/)). For us that is trade and market size, not
revenue: a plumber should see plumbers. Also steal the courage to publish a 4.3, not just a 4.9.
A real mediocre number reads as real.

**From Podium.** The named-outcome one-liner format: company name, one metric, one dollar figure
("Mountaineer HVAC: 20% more weekly sales calls & $96K additional monthly revenue",
[podium.com/pricing](https://www.podium.com/pricing/)). That is the exact template for the first
three design-partner case studies, and it is compatible with `AGENTS.md` rule 3 as long as the
number is real, dated, permissioned, and attributed to one named business.

**From Thryv and Housecall Pro.** Publishing a real entry price
([thryv.com/pricing](https://www.thryv.com/pricing/)). Both do it. Both sell to SMBs. Do the same
and put the floor in the hero.

**From PaceRev.** Two things only. The add-on structure, extra campaign +$79/mo and extra
business +$149/mo, which is expansion revenue at near-zero marginal cost given the margin
analysis in `docs/12-THREE-PS.md`. And the fact that they put three numbers in the band under
the hero, which is the correct use of that slot even though their three numbers are not
defensible.

**From the contractor agencies.** The plainness of
[Home Service Direct's](https://www.homeservicedirect.net/) guarantee language. Not the promise
itself, which we cannot make. The register: one short sentence, no hedging, no asterisk. Our
version of that sentence is about delivery, not results.

### Do not steal

**PaceRev's stats band content.** "10 to 40x return on ad spend" is unsourceable, and the
comparison table we already ship (`Comparison.tsx:112-117`) attacks HomeAdvisor using the FTC's
$7.2M order for misleading lead-quality claims. Publishing a return multiple after writing that
paragraph hands a contractor's lawyer the same case against us. The comment at
`ValueBand.tsx:13-17` already says this. It is right.

**PaceRev's "sold out" tier.** They have a claimed base to make capacity plausible. We do not.
See crack 2.

**PaceRev's headline, badge, section order and dashboard figures.** Already taken. Give them
back. See crack 4.

**PaceRev's "one new customer covers PaceRev for an entire year."** That is an ROI claim wearing
a value-framing costume, and the asterisk ("Based on a typical customer value against an annual
plan") does not make it sourceable.

**Podium's and Hatch's hidden pricing.** They sell to operators with a procurement process. We
sell to a person in a truck. HockeyStack's 31-million-visitor dataset shows hidden pricing
raising form volume and lowering pipeline conversion by 1.7x
([hockeystack.com](https://www.hockeystack.com/lab-blog-posts/state-of-pricing-demo-case-study-pages)).

**Thryv's and Housecall Pro's free trial.** `docs/09-SIX-PS.md` Packaging already ruled this out
with category-specific evidence: AdCreative.ai and Madgicx both generate "charged after I
cancelled" complaints from trial auto-conversion, which is the exact billing-theft pain this
product is positioned against. Mechanism 1 in Section 3 gets the same de-risking effect without
the auto-convert trap.

**Housecall Pro's aggregate performance claims** ("35% avg. revenue growth after the first
year"). Prohibited outright by `AGENTS.md` rule 3, and by `docs/09-SIX-PS.md` Proof rule 5,
which sets a floor of roughly ten customers before publishing any average.

**The contractor agencies' results guarantees.** "We work for free until you get leads" requires
controlling an outcome we explicitly do not control, and `docs/09-SIX-PS.md` Promise bans
guaranteed lead volume by name.

---

## 5. Evidence-backed recommendations, ranked

Ranked by expected revenue effect. Each carries its supporting source and an honest note on
evidence strength.

**1. Make one conversion path actually work.**
Wire a scheduler or a two-field callback form at `/book`, and replace the 555 number.
*Source:* none needed, this is arithmetic. *Expected effect:* everything, because current
conversion capacity is zero. *Evidence: not applicable.*

**2. Un-sell-out the Starter tier.**
Set `Pricing.tsx:31` to false, or state a true remaining count.
*Source:* `docs/12-THREE-PS.md` Section 3 assumes a 70% entry-tier mix. *Expected effect:*
restores the buying path for the majority of the target segment. *Evidence: internal assumption,
not measured.*

**3. Put the price floor in the hero.**
One line under the CTAs: "From $499 a month. Ad spend separate, on your own card."
*Source:* HockeyStack Labs, 31M visitors across 80 B2B SaaS companies, hidden pricing converts to
pipeline at 1.7x lower rates
([hockeystack.com](https://www.hockeystack.com/lab-blog-posts/state-of-pricing-demo-case-study-pages)).
Broadly, Housecall Pro and Thryv all publish entry prices. *Expected effect:* fewer, better
qualified conversations. *Evidence: strong for the direction, unmeasured for our specific page.*

**4. Ship the authorise-do-not-charge model and say so next to the price.**
*Source:* Broadly's live implementation of the equivalent promise
([broadly.com/pricing](https://www.broadly.com/pricing/)); risk-reversal lift figures exist but
only in secondary write-ups such as
[revenueflows.ai](https://revenueflows.ai/blog/does-money-back-guarantee-increase-shopify-conversion-rate).
*Expected effect:* the largest single trust gain available without customers. *Evidence: thin on
magnitude, strong on direction and on competitor behaviour.*

**5. Put a named, photographed founder above the fold with the 400-businesses line in first
person.**
*Source:* NN/g eyetracking, 57% of viewing time above the fold, 74% in the first two screenfuls
([nngroup.com](https://www.nngroup.com/articles/scrolling-and-attention/)) establishes that the
slot matters. Edelman/LinkedIn 2025 (n=1,934), 53% rate thought leadership above name recognition
([edelman.com](https://www.edelman.com/expertise/Business-Marketing/2025-b2b-thought-leadership-report))
is adjacent support. *Expected effect:* unmeasured. **The direct evidence for founder attribution
beating company stats is thin.** Everything specific to it that I found was unsourced marketing
content. The structural argument stands on its own: we have no company stats. [INFERENCE]

**6. Ship the free competitive read behind a one-field email gate.**
*Source:* already decided in `docs/12-THREE-PS.md` Section 2. Form-length figures (13.4%
single-field versus 5.3% at seven) come from aggregator summaries of Unbounce data
([digitalapplied.com](https://www.digitalapplied.com/blog/form-conversion-rate-benchmarks-2026-data-points)),
not from Unbounce directly. Unbounce's own published median of 6.6% across 41,000 pages
([unbounce.com](https://unbounce.com/average-conversion-rates-landing-pages/)) is the verified
figure. *Expected effect:* creates a remarketable list where none exists. *Evidence: strong on
"one field beats seven", weak on the exact percentages.*

**7. Record one 60-to-90-second demo of the competitive read running on a real postcode.**
*Source:* Wistia engagement data across 13M+ videos shows engagement falling sharply past 120
seconds
([chiefmarketer.com](https://www.chiefmarketer.com/wistia-state-of-video-report-engagement-down-content-under-promoted/)).
The widely quoted 69% and 100% video lift figures trace to a single Vidyard/Unbounce case study
([unbounce.com](https://unbounce.com/conversion-rate-optimization/case-study-using-video-to-lift-landing-page-conversion-rate-by-100/)),
not a benchmark. *Expected effect:* unmeasured. *Evidence: thin on magnitude, defensible on
duration.*

**8. Reorder the page. Cut the research-process numbers band.**
Proposed order: hero with price and founder, competitive-read demo, comparison table, pricing,
walkthrough with the App Review caveat visible, ad showcase, features, trades, FAQ.
*Source:* NN/g scrolling and attention ([nngroup.com](https://www.nngroup.com/articles/scrolling-and-attention/)),
74% of viewing time in the first two screenfuls. *Expected effect:* moves price and proof into
the measured attention window. *Evidence: strong for the principle, unmeasured for this ordering.*

**9. Fix the internal contradictions before they become chargebacks.**
Reconcile `Walkthrough.tsx:44-63` with `Pricing.tsx:6-9` and hoist `Faq.tsx:23` out of the
collapsed FAQ.
*Source:* `AGENTS.md` interim-behaviour clause; `app/refunds/page.tsx:11-16` on chargeback cost.
*Expected effect:* dispute avoidance rather than conversion gain. *Evidence: internal policy,
not external data.*

**10. Add the "not for you if" block and name the $1,500 all-in monthly floor.**
*Source:* `docs/09-SIX-PS.md` Plumbing section already commits to disclosure over concealment;
`Faq.tsx:39` and `Faq.tsx:47` already state the number where nobody reads it. *Expected effect:*
fewer wasted founder calls, higher perceived value. *Evidence: no external data found. This is a
judgement call.* [INFERENCE]

**11. Add third-party identity marks: legal entity, address, Stripe checkout, BBB.**
*Source:* Baymard, 19% of US shoppers abandoned over card trust
([baymard.com](https://baymard.com/blog/perceived-security-of-payment-form)); CXL trust-seal
research ([cxl.com](https://cxl.com/research-study/trust-seals/)). *Expected effect:* small
individually, compounding together. *Evidence: real studies, but ecommerce checkout studies, so
transfer to a B2B SaaS landing page is an assumption.* [ASSUMPTION]

**12. Relabel the "Results" nav item.**
*Source:* `docs/09-SIX-PS.md` Pain 2 and Pain 3 on this audience's sensitivity to inflated
claims. *Expected effect:* small. Zero cost. *Evidence: none external.* [INFERENCE]

### Where the evidence is thinnest, stated plainly

- **Founder track record versus company statistics.** No credible study found. Recommendation 5
  rests on a structural argument, not data.
- **Video lift magnitude.** One case study, endlessly recycled. The duration guidance is better
  supported than the lift claim.
- **Risk reversal magnitude.** The 21% figure has no traceable primary source. Competitor
  behaviour is the stronger argument.
- **Form-field percentages.** Attributed to Unbounce by aggregators; not found on unbounce.com.
- **Trust badge transfer.** Real research, wrong context (ecommerce checkout, not B2B landing).
- **Every conversion figure in this document is a benchmark from other people's pages.** None of
  it is measured on ours, because ours has never converted anyone. With zero traffic history,
  the correct next step after the fixes above is not more benchmarks, it is ten real sales
  conversations logged against the risk-detection plan already written in `docs/12-THREE-PS.md`
  Section 3.

---

## Source list

- [PaceRev](https://pacerev.com), fetched 2026-08-19
- [Podium pricing](https://www.podium.com/pricing/)
- [Hatch](https://www.usehatchapp.com/)
- [Broadly pricing](https://www.broadly.com/pricing/)
- [Housecall Pro pricing](https://www.housecallpro.com/pricing/)
- [Thryv pricing](https://www.thryv.com/pricing/)
- [Home Service Direct](https://www.homeservicedirect.net/)
- [Brands That Last](https://brandsthatlast.com/)
- [Nielsen Norman Group, Scrolling and Attention](https://www.nngroup.com/articles/scrolling-and-attention/)
- [Unbounce, average landing page conversion rates](https://unbounce.com/average-conversion-rates-landing-pages/)
- [Unbounce, video landing page case study](https://unbounce.com/conversion-rate-optimization/case-study-using-video-to-lift-landing-page-conversion-rate-by-100/)
- [HockeyStack Labs, State of Pricing, Demo and Case Study Pages](https://www.hockeystack.com/lab-blog-posts/state-of-pricing-demo-case-study-pages)
- [Baymard, perceived security of the payment form](https://baymard.com/blog/perceived-security-of-payment-form)
- [CXL, which site seals create the most trust](https://cxl.com/research-study/trust-seals/)
- [TrustSignals summary of Baymard trust-seal research](https://www.trustsignals.com/blog/trust-badges-work-and-we-have-the-receipts-to-prove-it)
- [Edelman and LinkedIn, 2025 B2B Thought Leadership Impact Report](https://www.edelman.com/expertise/Business-Marketing/2025-b2b-thought-leadership-report)
- [Chief Marketer summary of Wistia State of Video](https://www.chiefmarketer.com/wistia-state-of-video-report-engagement-down-content-under-promoted/)
- [DigitalApplied, form conversion benchmarks](https://www.digitalapplied.com/blog/form-conversion-rate-benchmarks-2026-data-points) (aggregator, unverified)
- [RevenueFlows, money-back guarantee and conversion](https://revenueflows.ai/blog/does-money-back-guarantee-increase-shopify-conversion-rate) (aggregator, unverified)
- [SaaS Hero, landing page social proof examples](https://www.saashero.net/content/landing-page-social-proof-examples/) (aggregator, unverified)
- [RevBoss, founder brands and trust](https://revboss.com/blog/how-founder-brands-build-trust-through-content) (marketing content, no methodology)
- [RFC 2606, reserved top-level DNS names](https://datatracker.ietf.org/doc/html/rfc2606)
- [NANPA, 555 line number assignments](https://www.nationalnanpa.com/number_resource_info/555_numbers.html)

Internal documents referenced: `AGENTS.md`, `docs/09-SIX-PS.md`, `docs/12-THREE-PS.md`,
`docs/18-MODEL-DECISION.md` (via AGENTS.md).
