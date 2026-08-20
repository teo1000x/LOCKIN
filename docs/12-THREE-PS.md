# Go-to-Market: Positioning, Packaging, Pricing

Compiled 2026-08-19. This is the offer-lock document. It builds on `docs/01-PRODUCT-SPEC.md`
(the pivot section governs), `docs/09-SIX-PS.md`, `research/01-competitive-landscape.md`, and
`research/04-domain-and-economics.md`, plus fresh research gathered for this document (source
list at the end). `docs/09-SIX-PS.md` already covers Pain, Promise, Product, Plumbing, and a
tactical version of Packaging, and Proof. This document does not repeat that work. It exists to
answer one question straight: does the generator model, priced anywhere near PaceRev, survive
contact with an honest reader, and if not, what price does.

Working name used throughout: **Ignition** (placeholder, per `01-PRODUCT-SPEC.md`).

---

## 1. POSITIONING

### The one-sentence statement

> For single-location HVAC, plumbing, roofing, and electrical contractors who need a real ad
> campaign running this month and have no marketing staff to build one, Ignition is the
> **campaign strategist** that turns six questions into a marketing plan, a read on what
> contractors near you are actually running on Facebook right now, and ready-to-post ads with a
> plain-English reason behind every choice, unlike a Boost Post button, which guesses at
> targeting with no strategy behind it, and unlike an agency retainer, which locks you into a
> contract and won't show you what it's doing with your money.

### Category choice and its consequences

Four candidates, each with a different price ceiling and a different competitor set:

- **Ad tool.** Ceiling $39-99/mo (AdCreative.ai, Adzooma). Competitor set is DIY creative
  generators. Undersells the marketing plan and the competitive read, and prices us into the
  "low-price, high-churn band every dead competitor lived in" that `01-PRODUCT-SPEC.md`
  explicitly warns against.
- **Agency replacement.** Ceiling $1,500-25,000/mo (`research/01`, Section 2). Competitor set is
  Hibu, Scorpion, Blue Corona. This is the category that invites the direct PaceRev comparison
  at its worst, because it claims full-service parity we cannot deliver: we do not publish, do
  not optimize daily, and do not capture leads.
- **Marketing department in software.** Implies an ongoing operational function the owner can
  stop thinking about. We cannot honor that either. The owner still uploads photos, still
  approves every ad, still posts it themselves.
- **Campaign strategist.** Ceiling roughly $300-1,500/mo, matching what a freelance strategist
  or a single-service agency starter package costs (`research/01` cites single-service starter
  packages beginning around $1,500/mo, and Blue Corona's site audit alone runs $2,500-3,500;
  a self-serve strategist product should sit below the human floor, not at it). Competitor set
  becomes freelance marketers, DIY tools, and the "planning" layer of an agency retainer, not
  the full retainer itself.

**Decision: campaign strategist.** It is the only category that matches what the product
actually does after the pivot: it thinks, it does not execute. It sets a price ceiling
consistent with the price band this document lands on below, and it structurally protects
against the Icon failure mode, since a strategist is not claiming to run anything.

**What we give up:** the "we run it all for you" narrative, the higher price ceiling that comes
with full-service management, and any framing that implies we are responsible for what happens
after export. We also give up the ability to claim result ownership in marketing copy, which
0-customer honesty requires anyway (`AGENTS.md`, inviolable rule 3).

### Against five real alternatives

| Alternative | The wedge | The objection we will hear |
|---|---|---|
| **Doing nothing** | The owner already knows competitors are running ads; the free competitive read (Section 2) makes that visible and specific, not abstract | "I don't have time even for this" |
| **DIY Boost Post** | Boost Post has no strategy, no targeting logic, and no idea what a nearby competitor is running; Ignition ships a plan and a reason for every decision | "Boost Post is free or $20, why pay $299/mo for something I could figure out myself" |
| **Local agency retainer** ($1,500-15,000+/mo per `research/01`) | A fraction of the cost, no contract, no proprietary CMS, nothing to lose on exit | "An agency does everything, I don't have to think about it at all" |
| **PaceRev** (publishes for them) | Owner keeps the account, keeps control, no dependency on a vendor executing daily decisions unsupervised | The central objection, addressed head-on in Section 3: "Why pay something close to PaceRev for a tool that makes me do the last step myself?" |
| **Freelancer** | Consistent trade-specific quality and compliance knowledge in minutes, not a multi-day turnaround, flat transparent price instead of an unpredictable one-off quote | "A freelancer builds a relationship with me and I can call them" |

### What we deliberately do NOT claim

`docs/09-SIX-PS.md`'s Promise section lists the full set (no "fully autonomous," no guaranteed
lead volume, no claim to judge lead quality, no claim to hold or manage spend, no fabricated
results). Positioning-specific additions on top of that list:

- **No full-service parity claim against PaceRev or any agency.** We do not say "everything
  PaceRev does, cheaper." We say what we actually do: strategy, competitive intelligence, and
  creative, handed off for the owner to post.
- **No implied outcome ownership once the export pack leaves our hands.** The owner posts it;
  what happens after that is between them and Meta's auction, which we do not touch and cannot
  see. The Icon case (`research/01`, Section 3, a Thiel-funded team that spent $12M on a domain
  and still collapsed under exactly this audience's skepticism of end-to-end AI claims) is the
  standing reason this line is not negotiable.

### Proof points honestly available with zero customers

`docs/09-SIX-PS.md` Proof section covers the full sequence; the one positioning-specific point
worth adding here: **the competitive read is the strongest zero-customer proof asset in the
product**, because it is not a claim, it is a live artifact. A prospect can watch it pull real,
current ads from real nearby competitors, using public Meta Ad Library data, during a demo. No
other proof point in the product can be shown this concretely before a single paying customer
exists.

---

## 2. PACKAGING

### Tier structure

| Tier | Price | Includes | What forces the upgrade |
|---|---|---|---|
| **Starter** | $299/mo | 1 business, 1 active campaign, monthly competitive-read refresh, full export pack (marketing plan, ad copy, images, targeting spec, Ads Manager setup instructions), email support | - |
| **Grow** | $599/mo | 1 business, up to 5 concurrent campaigns/services, weekly competitive-read refresh, priority generation queue, priority support | Multi-service trades running separate campaigns at once (an HVAC shop running AC tune-up and furnace-install offers simultaneously, or roofing storm-season surge campaigns) genuinely need more than one live campaign to manage. This is a real complexity increase, not an arbitrary gate. |
| **Multi** | $1,499/mo | Up to 4 businesses/locations, Grow-level features per business | Franchise, multi-location, and small-agency use is a different buyer with a different unit of work (per business, not per campaign). |

**What we deliberately do not gate on: generation count or "AI credits."** PaceRev gates on
image credits (150/600/3,000 across its three tiers, confirmed at pacerev.com). `09-SIX-PS.md`
already flags metered AI credits as a visible scarcity mechanic that reads as nickel-and-diming,
in the same family as the hidden add-on fees that make Podium, Birdeye, and Thryv trust
destroyers in this research. Ignition regenerates freely within a tier's active-campaign limit.
Internal cost metering per `AGENTS.md` rule 6 still exists (one power user must not destroy
margin), but it is a backstop the customer never sees or is charged against, not a customer-
facing pricing lever. This is a deliberate, statable difference from PaceRev, not just an
implementation detail.

### Where the competitive read sits

The competitive read needs no Meta approval (it reads public Ad Library data via a token we
hold, per the pivot addendum in `01-PRODUCT-SPEC.md`) and could ship before any other part of
the product.

**Decision: it is both.** A one-time, ungated, single competitive-read report ("see what 5 HVAC
companies near you are running on Facebook right now") ships as a free lead magnet, no login
beyond an email address required. This is the cheapest, highest-leverage top-of-funnel asset
available with zero customers, it demonstrates the mechanism rather than claiming it, and it is
the one proof point PaceRev does not appear to market at all (its own site pitches automation
and optimization, not competitive visibility). The **living version** (refreshed automatically
on a cadence, integrated into campaign generation, tied to a specific offer) is a paid-tier
feature, because ongoing refresh has real recurring cost and real recurring value, and giving it
away entirely would remove the one built-in reason to keep paying month to month (see Pricing
Risk 2, Section 3).

### Trial, paid pilot, or demo-then-buy

`docs/09-SIX-PS.md` already recommends demo-then-paid-first-month-with-guarantee over a free
trial, for two reasons specific to this audience: free-trial billing friction is itself a trust
destroyer here (AdCreative.ai and Madgicx both generate exactly this complaint), and a trial too
short to reach the $1,000-1,500/mo, 7-14+ day spend floor where Meta's algorithm exits learning
phase (`research/04`, Section 7) cannot honestly demonstrate anything anyway.

Fresh research adds a second, independent argument for the same conclusion. Demo-qualified B2B
SaaS customers convert at 20-35% of qualified demos and churn at roughly 3.5% annually, against
free-trial converts churning around 7.5% annually and converting at single digits to
high-teens depending on ACV band. For a high-ticket, trust-sensitive SMB product, demo-led
motions both convert better and retain roughly twice as well as trial-led motions.

**Firm recommendation, reaffirmed: demo, then paid first month with the guarantee below. No
free trial.** This is not a new decision, it is `09-SIX-PS.md`'s decision with independent
supporting evidence attached.

### Guarantee and risk reversal

`docs/09-SIX-PS.md`'s guarantee was written the same day as the pivot and one clause is now
stale: it scopes the refund to "a working leads inbox within 30 days," and post-pivot there is
no leads inbox, because the product never touches Meta or lead data at all. This document
replaces that clause with one built for the generator model:

**If Ignition does not deliver, within 30 days of a completed intake wizard, an approved
marketing plan, a competitive read, and a complete export pack ready to post, refund the SaaS
fee.** This is scoped entirely to artifacts the product controls end to end (our own generation
pipeline), not to what happens after export (ad delivery, Meta's auction, the owner's follow-
through in Ads Manager) or to spend, since we never hold it. That scoping is what makes it
actually a stronger promise than a results-based guarantee, not a weaker one: delivery is
deterministic on our side, so it is a guarantee a solo founder can always honor, not one that
depends on Meta behaving or the owner acting.

Anti-abuse guardrail: one refund per business per 12 months, and it requires a completed wizard
with real business inputs, not an account that was never used.

Other terms, all carried forward from `09-SIX-PS.md` and consistent with the pivot: no
long-term contract, month-to-month from day one, no setup fees.

### Contract terms, cancellation, and what the customer keeps on exit

Month-to-month, cancel anytime. On cancellation, the customer keeps every marketing plan,
competitive read, and export pack ever generated. This is a stronger portability story than
PaceRev's, not just an equal one: PaceRev's customer disconnects a Meta ad-management connection
on exit; Ignition's customer has nothing to disconnect, because we never had access to anything
in the first place. There is no technical debt on exit because there was never a connection to
begin with. This is worth stating plainly in marketing copy, since it directly answers the
sharpest pain in the research: asset lock-in on exit (Scorpion's proprietary CMS, Hibu
discarding the website on cancellation, per `research/01`, Section 2).

### Multi-location and small-agency packaging

The Multi tier ($1,499/mo, up to 4 businesses) is an expansion lever, not the core wedge, per
`09-SIX-PS.md`'s existing scope flag. One addition: a small agency or local marketing consultant
could plausibly use the Multi tier to generate plans and ads for several trade clients at a
lower incremental cost than hiring creative staff. This is real but deliberately deferred:
building anything agency-facing (white-label export, seat management, client-switching UI)
before the core single-owner wedge is proven would be effort spent on a future problem ahead of
the current one, the same reasoning `01-PRODUCT-SPEC.md` uses to defer CRM integrations.

---

## 3. PRICING

### The PaceRev parity problem, addressed directly

PaceRev, confirmed at pacerev.com: $699 / $1,499 / $2,499 per month, "runs the entire marketing
campaign for you, builds, launches, and optimizes every ad," 24/7 optimization, automatic
text/email follow-up, no contract. That is a materially larger scope of ongoing work than
Ignition performs. Ignition generates a plan, a competitive read, and a creative pack; the
owner does the posting, and there is no ongoing optimization at all, because there is no Meta
connection to optimize through.

Working through the honest defenses one at a time:

- **"The owner keeps full control and never grants account access."** Real, but weaker than it
  first sounds: PaceRev's own site states customers keep their own Meta account and can
  disconnect anytime with no contract. PaceRev is not asking for the kind of irrevocable lock-in
  that made Hibu and Scorpion infamous; it is using standard delegated ad-account access, which
  the domain research (`research/04`, Section 6) already treats as the expected, trust-safe
  norm. The differentiator is real in magnitude (zero access granted, versus scoped and
  revocable access granted) but it is a difference of degree, not the categorical difference the
  pitch wants it to be.
- **"No dependency on a vendor that could vanish."** More convincing. PaceRev's daily
  optimization is a live dependency: if PaceRev's automated pacing misfires, the failure mode is
  the exact one the research already documents at the platform level, Meta's Advantage+
  "inflating costs as much as 10x" and wiping out small-business budgets overnight
  (`research/01`, Section 4; `09-SIX-PS.md`, Pain #3). A generator has no equivalent live-money
  failure mode, because it never touches money. This is a genuine structural advantage, not just
  a talking point.
- **"The marketing plan and competitive read are artifacts the competitor does not provide."**
  Real and provable. PaceRev's own marketing describes automation and optimization; it does not
  describe a competitive-intelligence report or a written plan the owner keeps. This is the
  clearest, most defensible differentiator available, and it is why the competitive read is the
  lead proof asset in Section 1 and Section 2.
- **"The customer is buying strategy plus creative rather than button-pushing."** Directionally
  true but double-edged. It is also, honestly, less convenient: the owner has to spend real time
  in Ads Manager, and time poverty is pain #6 in `09-SIX-PS.md`, not a minor friction. A
  strategist who hands you a finished plan and then makes you type it into a foreign interface
  yourself is a real cost this pitch cannot argue away, only disclose honestly, which
  `09-SIX-PS.md`'s Plumbing section already commits to doing ("you'll need about 20 minutes in
  Ads Manager with our exact settings").

**Verdict: the differentiators are real, but they do not add up to parity.** Two of the four
survive scrutiny (vendor dependency risk, and the plan/competitive-read artifacts); one is
weaker than claimed (account access, since PaceRev already offers a no-lock-in exit); and one is
a genuine cost to the customer, not a benefit (doing the last mile themselves). An honest reader
who does this same arithmetic would not pay PaceRev-adjacent prices for meaningfully less
automation. The price band from `01-PRODUCT-SPEC.md`'s working hypothesis ($499/$999/$1,999,
already below PaceRev at every tier) does not go far enough down to reflect that arithmetic.

**Decision: cut the price band further, to $299 / $599 / $1,499.** That is roughly 55-60% of
PaceRev's respective tiers, not 70-85%. The gap is sized to the gap in scope: PaceRev optimizes
daily, publishes, and follows up automatically; Ignition does none of those things. The price
should say so before the sales conversation has to.

### Why not percentage-of-spend

Beyond the trust argument `09-SIX-PS.md` already makes (SMBs read it as "you profit when I
spend more," a documented complaint pattern), there is a structural reason specific to the
pivoted product: **Ignition never sees the customer's spend move through any system we control.**
There is no Meta connection, so there is no reliable, verifiable spend figure to compute a
percentage against, other than what the owner chooses to self-report. A pricing model built on
unenforceable self-reported numbers is worse than a bad pricing model, it is an invitation to
dispute, which recreates exactly the billing-trust complaints (Thumbtack, CraftJack, per
`09-SIX-PS.md` Pain #5) this product is positioned against.

### Why not pay-per-lead

Fresh research reinforces `09-SIX-PS.md`'s existing case with harder numbers: Angi/Thumbtack/
HomeAdvisor-style marketplaces share a single lead across 3-8 contractors, and because roughly
78% of customers hire whoever responds first, the true cost per booked job on these platforms
commonly runs 6-10x the quoted per-lead price. The BBB logged over 1,200 complaints against this
category in three years (2023-2026), and the FTC ordered HomeAdvisor to pay up to $7.2M in 2023
for false claims about lead quality and source. This is not a model to soften and adapt, it is
the single most reputationally toxic pricing pattern available in this category, and it is
doubly inapplicable here because Ignition does not generate leads at all post-pivot; there is no
unit called a "lead" for this product to charge against.

### Price metric: per business

Four candidates considered: per business, per campaign, per location, per generation.

**Decision: per business**, as a flat monthly fee, with campaign concurrency and business count
as the tier-differentiating axes (Section 2), not as separately metered units.

- **Per generation** is rejected outright. It recreates PaceRev's own "image credits" mechanic,
  the exact nickel-and-diming pattern `09-SIX-PS.md` flags as a trust destroyer, and it would
  charge the customer more for using the product the way it is meant to be used (regenerating
  ad variants until they are right).
- **Per campaign** was considered and rejected as the primary metric, because it would make the
  bill unpredictable month to month for a multi-service trade, the opposite of the "predictable
  flat fee" preference the research documents SMBs already have (`research/04`, Section 5).
  Campaign count is used instead as a tier boundary, where it is legible and fixed in advance.
- **Per location** is folded into the Multi tier rather than kept as an independent metric,
  because for the vast majority of the target buyer (single-location owner-operators, per
  `research/04`, Section 1) it is not a relevant axis at all, and introducing it as a separate
  dimension for the 95% case would add pricing complexity for no one's benefit.

Per business wins because it matches how the buyer already thinks about cost: one bill for the
business, the same way Podium, Broadly, and HighLevel are billed (`research/04`, Section 5), not
a bill that fluctuates with how many times they clicked regenerate.

### Expected ACV and unit economics

Blended ACV, assuming an early-cohort mix weighted toward the entry tier (roughly 70% Starter,
25% Grow, 5% Multi, a reasonable assumption for a single-location-first go-to-market):

| Tier | Monthly | Annual | Assumed mix |
|---|---|---|---|
| Starter | $299 | $3,588 | 70% |
| Grow | $599 | $7,188 | 25% |
| Multi | $1,499 | $17,988 | 5% |

Weighted blended ACV: approximately **$5,200/year (~$434/mo)**. This lands at the top of the
$1,200-$6,000/year range `research/04` (Section 5) synthesizes from adjacent point-solution
pricing (Podium, Broadly, HighLevel), which is defensible because Ignition is vertical-specific
and higher-touch than a generic communications tool, and vertical-specific providers see 34%
higher 3-year SMB retention than horizontal ones per the same research (`research/01`, Section
2).

**Per-customer monthly cost, LLM and image generation:**

Estimating a full campaign generation cycle (marketing plan, competitive-read synthesis, and
3-5 ad variants with copy) at roughly 30K input tokens and 8K output tokens against current
Claude Sonnet-class pricing (approximately $3/M input, $15/M output tokens), text generation
costs roughly $0.21 per full cycle. Image generation for 3-5 ad variants, using current
mid-tier image API pricing (GPT Image 1.5-class models run $0.04-0.21/image depending on
quality tier, per current OpenAI image API pricing), costs roughly $0.20-1.00 per cycle at
moderate quality. Assuming a customer regenerates a full cycle 3-4 times in a month (initial
generation plus edits), total LLM plus image cost lands in a **$5-15/month** range for a typical
customer, and a plausible worst-case heavy user (aggressive regeneration, higher-quality image
tier) lands around **$25-30/month**. Meta Ad Library reads are public API calls against a token
we hold, with negligible marginal cost.

**Gross margin at $299/mo (Starter):** at $10/mo typical cost, gross margin is approximately
**96.7%**. At the $30/mo worst-case cost, gross margin is still approximately **90%**. Add
payment processing (~3%) and this remains a very high-margin business at every tier; the LLM/
image cost line is not the constraint on this pricing, the market's willingness to pay is. This
is consistent with `AGENTS.md` rule 6 existing as an abuse backstop (one outlier user should not
destroy margin) rather than because typical margin is thin.

### Design-partner discounting, and raising prices later without punishing early believers

Carrying forward `09-SIX-PS.md`'s design-partner motion (3-10 businesses, reduced or waived SaaS
fee, never waived ad spend, in exchange for structured feedback and case-study rights) with one
addition: **design partners get their price locked for 24 months in writing, stated as a promise
at signup, not a temporary teaser that quietly expires.** This matters specifically for this
audience: a "founding member" deal that vanishes without notice is a smaller version of the
exact "price kept going up... via unsigned contract addenda" pattern that defines the Hibu
complaint set (`research/01`, Section 2). The same discipline extends past the design-partner
cohort: any future price increase for existing customers requires stated advance notice (a
minimum of 30 days, matching standard SaaS practice, disclosed in the guarantee/terms language),
never a silent change to an existing bill.

### Three pricing risks and how to detect each early

1. **The generator-versus-manager gap surfaces as a lost-deal objection.** Risk: a prospect
   compares Ignition to PaceRev directly and concludes the price cut was not deep enough to
   offset doing the last mile themselves. Detection: log the stated reason for every stalled or
   lost conversation in the first 10-20 sales/demo calls. If "but PaceRev does it for me" or
   equivalent appears in more than roughly 30% of them, the price needs to move further down, or
   the packaging needs an optional paid add-on (for example, a one-time guided Ads Manager setup
   session) rather than a further blanket price cut.

2. **Bursty usage undercuts the case for a recurring fee.** Risk: an owner generates one
   campaign, exports it, and has no reason to open the product again until the next offer
   season, making a flat monthly fee feel unjustified by month two, the exact mechanism behind
   the 30% two-year retention `research/01` reports for single-product, low-engagement SMB
   tools. Detection: track login and generation activity by month-since-signup per customer. A
   cliff below roughly 10% of customers returning in month 2 is the early signal, and the fix is
   product, not price: lean harder on the automatically refreshed competitive read (Section 2)
   as a passive, no-login-required recurring-value hook, delivered by email.

3. **Design-partner discounting suppresses the real anchor price before it is tested.** Risk:
   too many early customers lock in below full price, so the business never learns whether
   $299-$1,499 is actually what the market will pay. Detection: cap design partners at the
   stated 3-10 and track blended ACV weekly once general-market pricing opens. If discounted or
   grandfathered accounts still exceed roughly 20% of total customer count by the time the 10th
   full-price customer signs, pause any further discounting until full-price willingness-to-pay
   is confirmed.

---

## Source URLs

Inherited from `research/01-competitive-landscape.md` and `research/04-domain-and-economics.md`
(see those files for the complete lists); key ones referenced directly above are not repeated
here. New sources gathered for this document:

- [PaceRev](https://pacerev.com) - pricing tiers, image-credit gating, and publish/optimize claims, fetched directly
- [Marketing Agency Monthly Retainer Cost: 2026 Guide - ClicksGeek](https://clicksgeek.com/marketing-agency-monthly-retainer-cost/)
- [HVAC Marketing Agency Pricing Guide 2026 - Sureshot Systems](https://www.sureshotsystems.com/insights/hvac-marketing-agency-pricing-guide-2026-commercial-retainers-performance-based-models-roi-benchmarks)
- [HomeAdvisor vs Angi: $15-$100 Lead Fees Compared (2026) - AllBetterApp](https://allbetterapp.com/allbetter-vs-homeadvisor-vs-thumbtack-vs-angi/)
- [Thumbtack Pro Review 2026 - Savul LLC](https://savullc.com/thumbtack-pro-reviews/)
- [B2B SaaS Trial-to-Paid Conversion Rate Benchmarks 2026 - Growthspree](https://www.growthspreeofficial.com/blogs/b2b-saas-trial-to-paid-conversion-rate-benchmarks-2026-by-trial-type-acv-length-credit-card)
- [Why Enterprise SaaS Trials Convert at 10% in 2026 (Demos vs Trials) - Growleads](https://growleads.io/blog/b2b-saas-trials-vs-demo-sales-conversion/)
- [B2B SaaS Conversion Rate Benchmarks 2026 - Orbix Studio](https://www.orbix.studio/blogs/b2b-saas-conversion-rate-benchmarks)
- [Image Generation API Pricing 2026: Complete Cost Comparison - CostLayer](https://costlayer.ai/blog/image-generation-api-pricing-2026-complete-cost-comparison)
- [OpenAI Image Generation API Pricing in 2026 - AI Free API](https://www.aifreeapi.com/en/posts/openai-image-generation-api-pricing)
- [AI Image Generation API Pricing (July 2026) - BuildMVPFast](https://www.buildmvpfast.com/api-costs/ai-image)
- [SaaS Pricing Strategy Guide 2026 - NxCode](https://www.nxcode.io/resources/news/saas-pricing-strategy-guide-2026)
- [Seat vs. Usage: How to Choose a Pricing Model for B2B SaaS in 2026 - Bridges](https://withbridges.com/blog/seat-vs-usage-pricing-b2b-saas-2026)

**Note on source reliability**, inherited from `research/01` and `research/04`: SEO/affiliate
content and review aggregators dominate this space; figures here are used as directional
benchmarks, not precise category-specific data, and the LLM/image cost estimates above are this
document's own synthesis against current published API pricing, not a reported figure for this
exact workload.

---

## FOUNDER OVERRIDE, 2026-08-19: pricing locked

**Locked price points: $499 / $1,300 / $2,500 per month.**

This overrides the $299 / $599 / $1,499 recommendation above. The founder reviewed the
PaceRev parity analysis and chose the higher band. Recorded as decided.

Positioning against PaceRev's $699 / $1,499 / $2,499:

| Tier | Ours | PaceRev | Ratio |
|---|---|---|---|
| Entry | $499 | $699 | 71% |
| Mid | $1,300 | $1,499 | 87% |
| Top | $2,500 | $2,499 | **100%** |

**The tier to watch is the top one.** At $2,500 we are at full parity with a competitor
that publishes campaigns, optimizes daily, and captures leads automatically, while we hand
over an export pack the owner posts themselves. The entry tier's 71% ratio is defensible.
The top tier needs either a materially different feature set or a different buyer (multi
location, franchise, small agency) to justify parity. Revisit after the first ten sales
conversations, and treat objections at the top tier as signal rather than noise.

Margin is not the constraint at any of these prices. See the unit economics section above:
generation cost runs single-digit dollars per customer per month against a $499 floor.
