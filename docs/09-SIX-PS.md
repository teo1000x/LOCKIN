# Go-to-Market Strategy: The Six Ps

_Compiled 2026-08-19. Builds directly on `docs/00-RESEARCH-SYNTHESIS.md`, `docs/01-PRODUCT-SPEC.md`, `research/01-competitive-landscape.md`, and `research/04-domain-and-economics.md`, plus fresh verbatim-complaint research gathered for this document (sources at the end). Every claim is either sourced or explicitly flagged as a hypothesis to test with real customers._

---

## 1. PAIN

### What they say vs. what they actually have

**What owners say when you ask them:** "I need more leads." "My phone isn't ringing enough." "I don't have time for marketing." These are real, but they are the surface layer, and a product built only to answer them repeats the mistake of every failed competitor in this category (see `research/01`, Section 3).

**What they actually have**, underneath that surface language:
- A specific, remembered betrayal (a named agency, a named dollar amount, a named number of months) rather than a generic "marketing doesn't work" belief.
- Attribution blindness: they cannot separate a real booked job from a call that never should have counted, so every number an agency or platform reports to them is inherently suspect.
- Sunk-cost fear of being burned *again* by the next vendor, which makes "AI does your marketing" a red flag phrase, not a selling point, for this specific audience.
- Genuine time poverty: managing a truck fleet, a crew, and the books already eats their week; marketing has to fit in minutes, not hours.
- A learned expectation that leaving a vendor costs them something (a website, an account, momentum) even when they never signed up for that trade-off knowingly.

### Ranked pains, with verbatim evidence

**1. The retainer betrayal: paying for months with nothing to show for it.**
This is the sharpest, most emotionally loaded pain in the research, and it recurs across every "done-for-you" agency studied.
> "No generated business came from them. They have great sales people, they must make their money on sign up bonuses because there is no way people are continuing to stay with HIBU."
> — Hibu customer complaint (ComplaintsBoard)

> "Locked into a contract with a proprietary system. Can't take our website with us. This should be illegal."
> — BBB complaint about Scorpion, 2025

An industry-side write-up of the retainer model makes the mechanism explicit: a six-to-twelve-month lock-in demanded before results are seen "protects the agency rather than the contractor," and if a bad month "would force you to make payroll from a line of credit, you should not sign it." (Minyona, "Pay Per Lead vs. Monthly Retainer")

**2. Junk leads dressed up as real ones.**
> "An agency might show that your phone rang 80 times last month, but if 50 of those calls were from outside your service area, 20 were people looking for free advice, and 5 were existing clients with billing questions, you effectively received 5 leads, not 80."
> — marketing-ops source (mosierdata.com)

> "bad leads out of all the leads only one is aware that they search to hire someone for a project the rest of the clients either block me"
> — Marquet Sjm, CraftJack complaint (PissedConsumer, Aug 9 2021)

> Roughly 85% of leads on one platform are fake, per a contractor complaint synthesized across Trustpilot's Angi/HomeAdvisor review pages (37,000+ reviews, 2.1/5 average), with one contractor reporting "3 leads a week, with 2/3 being fraudulent, bogus names and dead numbers."

A separate direct fraud case: one HVAC buyer paid for leads and received **19 of a promised 75 over three months, with none answering the phone** (per `research/01`, Section 4, sourced to home-services lead-gen coverage).

**3. Not knowing if the money is working (the black-box problem).**
This is the platforms' own automation now, not just agencies:
> Meta's Advantage+ has drawn advertiser backlash for inflating costs "as much as 10x," with small businesses reporting their "entire ad budgets have been wiped out" and "few to no revenues" in return.
> — eMarketer, "Meta faces backlash as automated ad system drains budgets with little payoff"

> "They give you zero feedback... The only people who are OK are massive spenders who get a Facebook rep."
> — digital marketing firm co-founder, on a Facebook ad account ban with no support (had to cut 12 jobs as a result); `research/01`

Google's Performance Max fares no better: independent PPC-agency commentary repeatedly calls it a "black box... where no one has full access to the data" (`research/01`).

**4. Being locked in, unable to leave cleanly.**
> "Locked into a contract with a proprietary system. Can't take our website with us."
> — Scorpion BBB complaint, 2025 (repeated above because it is the single cleanest quote for this pain specifically)

Angi/HomeAdvisor contracts can demand "35% of the remaining yearly contract value to break" (Trustpilot synthesis, 2026). Hibu customers report the company "discards the website... you only keep the content, not the page" on cancellation (`research/01`).

**5. Billing that feels like theft.**
> "I am repeatedly getting charged for one way transfers, which we do not offer, never have, never will."
> — Frank O, Thumbtack complaint (PissedConsumer, Feb 3 2026)

> "after canceling our card on file and hiding my business from the app, we were still charged."
> — Dashun Avl, Thumbtack complaint (PissedConsumer, Jan 25 2024)

> "I've been trying to cancel my account for about a month now. 5 calls later and still your charging my account."
> — Nanette K, CraftJack complaint (PissedConsumer, Aug 10 2021)

> "Took $500 out of my husbands account which was all we had left this month for bills and groceries"
> — Seth R Suj, CraftJack complaint (PissedConsumer, Oct 16 2020)

> "all it is is a money scheme, rather you get the lead or not you are charged anywhere between 19 to $100"
> — Justin S Uen, CraftJack complaint (PissedConsumer, Feb 22 2020)

**6. No time to run it themselves.**
Owner-operators describe marketing as something that "can easily consume a day of work per week" if self-managed (`research/01`, Section 4), which is exactly why Revealbot's "multi-day setup" and WordStream's service-quality collapse ("technical PPC specialists got replaced with general customer service reps who couldn't tell a keyword from a coffee cup," ticket SLA blown from 24 hours to 5-7 days) are fatal for this buyer even though the same friction is tolerable for an agency with staff.

**7. AI tools that promise everything and deliver a worse version of the same problems.**
> "This software is a total waste of time. Slow, unusable and clunky."
> — Icon user review, before the company (Founders Fund/Thiel-backed, $12M spent on the domain alone) went dark in 2025-26 without a formal shutdown announcement (`research/01`, Section 3)

> Madgicx: canceled a trial, was still charged $70; "customer support had terrible response times, unacknowledged questions, and demeaning answers from chat."

> AdCreative.ai: charged the wrong amount in a December 2025 review, refund refused.

**Read for product design:** owners are not primarily afraid the ads won't work. They are afraid they won't be able to tell, they'll be charged for something that didn't happen, and they won't be able to leave if it goes wrong. That is a trust and legibility problem before it is a performance problem, exactly as `docs/00-RESEARCH-SYNTHESIS.md` finding #4 states.

---

## 2. PROMISE

### The one sentence an owner would repeat to another owner

> **"Nothing runs until you approve it, it's your ad account, and you can leave anytime with everything you built."**

This sentence is chosen deliberately to answer pains #1, #3, #4, and #5 above in one breath, and to contain zero words ("AI," "automated," "optimize") that this specific audience has learned to distrust.

### Supporting promises (each one we can keep with the product as specced)

| Promise | What in the product backs it | Pain it answers |
|---|---|---|
| "You see every ad before it spends a dollar." | Approval gate is a database constraint, not a UI convention (`01-PRODUCT-SPEC.md`) | Black box, billing theft |
| "It's your account, your card. We never touch your ad spend." | Ads publish into the owner's own Meta ad account and card; we never sit in the money flow (Policy 10.5-aligned) | Lock-in, billing theft, "who's profiting from my spend" |
| "Cancel anytime. Keep your account, your ads, your lead history." | No proprietary CMS, no asset we hold hostage; export/disconnect is a stated feature | Lock-in |
| "We tell you why, in plain English, every time." | Rationale string attached to every AI decision ("targeting 12 miles because that's where your last 30 jobs came from") | Black box |
| "We talk in jobs and dollars, never CTR/CPM/ROAS." | Reporting layer speaks the language the owner actually uses | "Can't tell if it's working" |
| "A lead notifies you within 60 seconds." | Leadgen webhook to SMS/email; speed-to-lead is cheapest-to-build, highest-ROI feature identified in the spec | "Phone doesn't ring" / lost jobs to faster competitors |

### Promises we must NOT make

The Icon case study is the single most important cautionary data point in the whole research set: a Thiel-funded team with top AI talent led with "fully autonomous AI CMO," and it went dark within about a year, with its own pivot attempt being *toward* the human-agency model it was built to replace (`research/01`, Section 3). That is not a marketing lesson, it is a product-positioning constraint.

Explicitly out of bounds:
- **No "fully autonomous," "AI runs your marketing," or "set and forget."** The approval gate is the product's spine, not a feature to soft-pedal in copy.
- **No guaranteed lead volume or lead count.** This is the exact promise that makes pay-per-lead marketplaces (Angi, Thumbtack, HomeAdvisor) the most hated pricing model in the category (`research/04`, Section 5). We cannot control the Meta auction and must not imply we can.
- **No claim to replace human judgment on lead quality.** The research is explicit that judging a lead "real vs. junk" is the one layer that stays human (`research/01`, Section 2). We surface qualifying-question data; the owner still makes the call, at least in v1.
- **No implication that we hold, manage, or have discretion over ad spend.** Zero. This is both a trust argument and, from 2027-02-03, a Meta Policy 10.5 compliance requirement.
- **No results claims we can't back with real numbers.** At launch we have zero customers. Every performance claim in marketing copy must be sourced to a labeled design-partner result or clearly framed as industry benchmark data, never as "our customers see X."
- **No "no work required."** The owner still uploads photos, still approves ads, still answers a short wizard. Promising zero effort is the same overreach that broke Icon.

---

## 3. PRODUCT

Described as a buyer experiences it, mapped back to the pain it answers. Anything with no pain mapping is flagged as scope risk.

| What the owner gets | How they experience it | Pain it maps to |
|---|---|---|
| A 10-15 minute intake wizard | A short set of questions about the trade, the offer, the area, the budget, no jargon | #6 (no time) |
| An AI-built campaign, delivered as a real Facebook-style preview | They see the actual ad, not a spec sheet, and can edit or regenerate any piece before it exists on Meta | #3 (black box), #7 (AI tools that don't deliver) |
| The approval gate | Nothing is created or activated on Meta without their explicit, timestamped click; every campaign publishes paused first | #1, #3, #4, #7 |
| Plain-English "why" on every decision | "Targeting 12 miles around your shop because that's the radius your last 30 jobs came from," never a confidence score | #3 (can't tell if it's working) |
| Publishing into their own Meta Page/ad account, their own card | We never touch their money; account is theirs from day one | #4 (lock-in), #5 (billing theft), #1 (agency withholding accounts) |
| Meta Instant Forms with trade-specific qualifying questions | Fewer, better-targeted leads instead of raw call volume | #2 (junk leads) directly |
| Speed-to-lead notification (SMS + email within seconds) | They find out about a hot lead before a competitor does | #6 (no time), lost-job risk |
| Spend guardrails: hard daily cap, owner-set ceiling, anomaly alarm that pauses and notifies | The Advantage+ "budget wiped out overnight" failure mode is architecturally prevented, not just monitored | #3 (Meta Advantage+ 10x-cost complaint) |
| Policy pre-flight lint + Special Ad Category detection | Fewer ad rejections, fewer account-flag risks, less wasted time | #6 (no time), reliability underpinning #3 |
| One-button pause / export / disconnect | Leaving is trivially easy, by design | #4 (lock-in) directly |
| Plain-English reporting: "$2,400 spent, 14 real jobs, $18,200" | Speaks in the vocabulary owners actually use (`research/01`, Section 4) | #3 (can't tell if it's working) |

### Capabilities that map to no pain (flagged as scope to cut or defer)

- **AI image generation fallback.** Real job photos outperform stock imagery for trades and are what the product should push for; AI-generated imagery is a fallback for owners with zero photos, not a headline feature. Keep it minimal; do not market it as a differentiator.
- **The $1,999 "Multi" tier (up to 4 businesses).** This answers a monetization/expansion need (franchises, multi-location operators, small agencies), not a pain identified in Section 1, which is about the single-location owner-operator. Treat it as a later-stage revenue lever, not part of the core wedge pitch.
- **CRM integrations / offline conversion upload / call tracking.** These are explicitly out of scope for v1 in `01-PRODUCT-SPEC.md`, and correctly so: the research identifies the closed attribution loop as the real long-term moat (`00-RESEARCH-SYNTHESIS.md`, finding #3), but it answers a *future* pain (proving ROI to the ad platform's own algorithm), not a *launch* pain. Building it now would be effort spent on a real problem in the wrong sequence.
- **"AI image credits" as a metered/gated feature inside pricing tiers.** As written in the pricing hypothesis this reads as nickel-and-diming, which is precisely the "hidden add-on fees" pattern (Podium, Birdeye, Thryv) the research flags as a trust destroyer. If it stays, it should not be a visible scarcity mechanic.

---

## 4. PLUMBING

### Onboarding sequence and time-to-first-value

| Step | What happens | Target time |
|---|---|---|
| 0. Sign up | Owner creates account, connects Meta Page (OAuth) | Minutes |
| 1. Intake wizard | Trade, offer, geography, budget, creative inputs | 10-15 minutes |
| 2. Blueprint generation | AI builds campaign, ad set, lead form, 3-5 ad variants | Under 5 minutes, target |
| 3. Approval | Owner reviews in Facebook-style preview, edits/regenerates/approves | Same session, ideally |
| 4. Publish (paused) then activate | Campaign goes live only after the explicit activation step | Same day |
| 5. First lead | SMS/email notification within seconds of the leadgen webhook firing | Within 1-3 business days of activation, trade- and budget-dependent |

Target: **time-to-first-live-campaign under 24-48 hours from signup**, **time-to-first-lead under 3 business days**. This target is chosen because the research finding that "onboarding speed-to-value is a bigger retention lever than price" is specific and quantified: strong onboarding (time-to-first-value under 7 days) is associated with roughly 50% lower churn, and up to 70% of SMB SaaS churn happens in the first 90 days (`research/04`, Section 5).

**Sequencing caveat:** under the export/handoff model (Model A, per the `01-PRODUCT-SPEC.md` addendum), the owner still has to manually set the campaign up in Ads Manager, which adds real friction and real time versus the in-app-publish model (Model C). This is an honest gap for early design partners and should be disclosed, not hidden: "you'll need about 20 minutes in Ads Manager with our exact settings" is a truthful sentence; anything that implies zero-touch publishing under Model A is not.

### Support model for a solo founder

A solo founder cannot offer 24/7 human support and should not promise it. The model has three tiers:

1. **Self-serve / automated.** Help docs and in-product guidance for the mechanical stuff: photo upload issues, how to read the approval screen, how spend caps work. This should absorb the majority of questions.
2. **Async, same-business-day human response.** Email/chat for anything that needs judgment: a confusing rejection, a targeting question, a billing question. Explicit SLA stated to the customer up front ("we respond within one business day," not "24/7 support") so the promise matches solo-founder capacity.
3. **Urgent escalation.** Reserved for account-level emergencies: Meta account suspension, a spend anomaly the automated guardrail already caught and paused. Target under 1 hour response during business hours; explicitly, honestly communicated that outside business hours the automated guardrail (auto-pause) is the safety net, not a human, and the human follows up next business day.

For the first 3-10 design-partner customers specifically, tier 2 becomes a live onboarding call with the founder personally, because at that volume it is both feasible and the highest-leverage way to learn what breaks.

### Failure modes and what happens

| Failure | Automated response | Human required when |
|---|---|---|
| **Generation fails** (LLM error/timeout) | Auto-retry with backoff; if still failing, queue for regeneration and show the owner "still working on this" rather than a broken screen | Fails more than twice in a row; logged for founder review |
| **Ad rejected by Meta** | Webhook parses the rejection reason; if it maps to a known, common policy-lint miss, auto-regenerate a compliant variant and resubmit, and tell the owner in plain English what happened and that it's being handled | Rejection reason is novel or ambiguous; flagged for founder review within the same business day |
| **Meta OAuth token expires** (note: passkey sign-in required for new refresh tokens from 2026-08-05, per `00-RESEARCH-SYNTHESIS.md`) | Proactive expiry warning before it lapses; if it lapses, campaigns are paused (never left running un-monitored), and the owner is prompted to reconnect | Reconnect flow itself fails repeatedly for the owner |
| **Spend spikes** | Hard daily cap enforced at the Meta campaign level as the primary architectural guardrail (not just an alert); anomaly detection (e.g., pace exceeding a threshold within a short window) triggers auto-pause plus immediate SMS/email to the owner and an alert to the founder | Owner needs to understand what happened and decide whether to resume; founder reviews before re-approval in the early cohort |

**What is automated vs. requires a human, summarized:** pacing enforcement, token-refresh nudges, common policy-lint fixes, and rejection-reason translation are automatable and should be automated from day one, because they are exactly the mechanical layer the domain research says software already does well (`research/01`, Section 2). Judgment calls (ambiguous rejections, spend-spike root cause, refund/credit decisions, churn-risk conversations) require the founder, and the support model above is built around that being the actual bottleneck, not a hidden one.

---

## 5. PACKAGING

### Pricing tiers

| Tier | Price | Includes | Rationale |
|---|---|---|---|
| **Launch** | $499/mo | 1 business, 1 campaign, AI image credits | Undercuts PaceRev's $699 entry deliberately, and lands below the $500-800/mo range owners already pay for Podium/Broadly-style point solutions, so it reads as "in budget" rather than "one more expensive tool." |
| **Grow** | $999/mo | 1 business, up to 5 campaigns, priority generation | For multi-service trades (an HVAC shop running separate AC tune-up and furnace-install campaigns) or seasonal-surge needs (roofing storm season). |
| **Multi** | $1,999/mo | Up to 4 businesses | Matches PaceRev's top tier. This is an expansion/franchise tier, not core-wedge pricing (see Section 3's scope flag); it should not anchor the initial pitch to a single-location owner. |

Ad spend is always separate, always on the owner's own card, never touched by us. This is stated in pricing, not buried in fine print, because opacity about money flow is the single most common complaint mechanism identified across Hibu, Scorpion, Angi, and Thumbtack (Section 1).

### Trial vs. paid pilot vs. demo-then-buy

**Recommendation: paid first month with a guarantee, not a free trial.**

Two research findings drive this, both direct:
1. **Free-trial billing friction is itself a trust destroyer in this exact category.** AdCreative.ai's 7-day trial "auto-converts to paid" generates billing complaints; Madgicx customers report being "charged $70" after canceling a trial. A free trial that silently becomes a charge recreates the exact "we were still charged" pattern owners already associate with Thumbtack and CraftJack (Section 1, pain #5).
2. **A short free trial cannot honestly demonstrate value anyway.** The spend floor research shows paid ads need roughly $1,000-1,500/mo in spend and 7-14+ days just to exit the platform's learning phase (`research/04`, Section 7). A 7-day free trial would either show nothing meaningful or would need real ad spend running during it, which is a worse trust position than just being honest about the timeline.

So: **no free trial.** Instead, a demo (interactive or recorded) that shows the wizard-to-approval flow with a sample business, clearly labeled as a demo, followed by a paid first month backed by a guarantee (below). This also pre-qualifies for the actual ICP: an owner willing to commit to a real ad budget is closer to the $1,500+/mo spend floor that makes the product work at all.

**Design partners are a separate motion.** The first 3-10 customers should be recruited explicitly as founding/design partners: reduced or waived SaaS fee (never waived ad spend) in exchange for structured feedback, tolerance for rough edges, and permission to use honest results as case studies. This is distinct from the general-market pricing above and should not be advertised as the standard offer.

### Guarantee and risk reversal

Given how burned this audience is, the guarantee has to invert every pattern found in the research, not just be generically generous:

- **No long-term contract. Month-to-month from day one.** The research shows annual contracts suppress churn 40-60% (`research/04`, Section 5), which is a real reason to eventually offer an annual discount, but requiring a contract during the trust-building phase repeats the exact "locked into a contract" complaint that defines Scorpion and Angi in this research. Earn the annual commitment later; do not require it up front.
- **Written data and account portability guarantee.** Cancel anytime, keep the ad account, keep the campaigns, export the lead history. This directly answers pain #4 and should be a stated, specific promise, not a vague "no lock-in" slogan.
- **A first-month satisfaction guarantee scoped to what we control.** If the product did not deliver an approved, live campaign and a working leads inbox within 30 days, refund the SaaS fee (never the ad spend, since we never hold it). This must be scoped to *process* outcomes we control (a live campaign exists, leads flow to an inbox), not to lead volume or quality, per the "no guaranteed lead volume" rule in Section 2.
- **No setup fees, no mandatory onboarding fees.** Directly contrasts Thryv's "mandatory onboarding/support fees" and Birdeye's extra SMS-volume fees.

### Pricing model: what to avoid, explicitly

The domain research is unusually direct here (`research/04`, Section 5):
- **Never percentage-of-spend.** It creates the exact "you profit when I spend more" conflict of interest SMBs explicitly distrust, and it would be a strange model anyway given we structurally never see the spend move through us.
- **Never pay-per-lead.** This is "the most hated thing in the category," and the evidence is not abstract: Angi, Thumbtack, and CraftJack all show the identical failure pattern in Section 1's quotes (charged whether or not the lead was real, credits denied, disputed refunds). Flat SaaS fee only.
- A modest hybrid (small flat base plus a small percentage of spend, 5-8%, well under agency rates of 10-20%) is flagged in the domain research as an emerging, tolerated middle ground, but given how cleanly flat-fee-only answers the trust problem and how clean "we never touch your spend" is as a message, **flat fee only is the stronger choice for this specific brand**, at least until there's a specific reason (e.g., a customer segment explicitly asking for it) to complicate it.

---

## 6. PROOF

**Hard constraint restated: zero customers, zero results, today.** Every proof asset below is either (a) honestly buildable right now with no customers, or (b) explicitly marked as requiring real customers first. Nothing here proposes a fabricated statistic, an invented case study, or a composite/stock testimonial.

### What we can honestly show at launch with zero customers

- **A demo of the actual mechanism**, not a mockup: the wizard, the AI-generated blueprint, the Facebook-style approval preview, using a clearly labeled sample business. This is proof of *how it works*, which we can show today, not proof of *results*, which we cannot.
- **A guardrail explainer**: a short walkthrough of the approval gate, the spend caps, and the anomaly-pause behavior. This is the trust wedge itself made visible, and it costs nothing to build honestly because it describes the architecture, not a claim about outcomes.
- **A sourced comparison page**: "what happens with [Hibu/Scorpion/Angi], what we do differently," citing the public complaints in Section 1 with links. This is honest and provable today because it cites other companies' documented behavior, not our own unproven results.
- **An explicit "we're new" positioning statement**: stating plainly that this is a new company, and framing that as founding-member pricing and hands-on, personal onboarding from the founder, rather than hiding newness behind vague claims of experience. Given the Icon precedent (an extremely well-funded, well-credentialed entrant that still collapsed under exactly this audience's skepticism), false credibility signaling is a bigger risk than admitted newness.
- **A published summary of this research itself**, properly attributed, as a public "here is what we found asking hundreds of contractors and reading their actual complaints" piece. This builds trust by showing our homework without claiming any result we haven't earned yet.

### What requires real customers first (do not fabricate any of this)

- **Design partner selection.** Recruit 3-10 businesses via the niche-community-first channels the research flags as actually working for this buyer (trade Facebook groups, relevant subreddits used to *listen*, local trade associations, referral from a trusted local contact), not paid acquisition (`research/01`, Section 5).
- **Real, permissioned metrics from each design partner:** actual time-to-first-lead, actual number of ads approved vs. rejected, actual spend and actual leads, with explicit written permission to publish, or an anonymized version ("an HVAC company in Texas") if they decline attribution.
- **Before/after quotes**, specifically comparing the experience to their prior agency or tool, collected only from genuinely willing partners, never solicited under pressure or in exchange for a discount without disclosure.
- **A short video testimonial**, only if a partner is genuinely enthusiastic; never scripted, never paid for without disclosure.

### The exact sequence to build

1. **Pre-launch (zero customers needed).** Demo video, guardrail explainer, sourced comparison page, "we're new" honesty page. Buildable now.
2. **Design-partner recruitment (3-10 businesses).** Founding pricing plus hands-on founder onboarding in exchange for real feedback and case-study rights.
3. **First real numbers, roughly 30-60 days into the first partner's live campaign.** Time-to-first-lead, approved-vs-rejected ad counts, real spend and real leads (with permission). Published as the first case study, explicitly dated and explicitly labeled as a single business's result, not a guarantee.
4. **A second and third case study**, deliberately sought across different trades (e.g., not three HVAC shops) to test whether the result generalizes rather than to manufacture the appearance that it already does.
5. **Aggregate claims ("average X") only once n is large enough not to mislead.** As a hard rule: do not publish an "average" result from fewer than roughly 10 customers. This is a guardrail against the exact temptation a small early sample creates.
6. **Third-party review presence (G2/Capterra) only after real usage exists.** Do not solicit reviews before value has actually been delivered, and never trade a discount for a review without clear disclosure, given how much this exact category's credibility has been damaged by that pattern.

---

## Summary of what changed vs. the working pricing hypothesis

The tier structure and price points in `01-PRODUCT-SPEC.md` are kept as-is; this document adds the guarantee, contract terms, trial/pilot recommendation, and the explicit "never do this" pricing-model list, all grounded in Section 5 pain evidence rather than treating pricing as a separate exercise from trust.

---

## Source URLs

From existing research (`research/01-competitive-landscape.md` and `research/04-domain-and-economics.md`) — see those files for the full list. Key ones referenced directly above:
- [Hibu Small Business Owners Reviews and Complaints — ComplaintsBoard](https://www.complaintsboard.com/hibu-b135210)
- [Scorpion Reviews — Trustpilot](https://www.trustpilot.com/review/scorpion.co)
- [Icon AI ad startup shuts down — TechStartups](https://techstartups.com/2026/03/05/icon-the-ai-ad-startup-shuts-down-after-spending-12m-on-the-icon-com-domain/)
- [Meta faces backlash as automated ad system drains budgets — eMarketer](https://www.emarketer.com/content/meta-faces-backlash-automated-ad-system-drains-budgets-with-little-payoff)
- [Madgicx Pricing — G2](https://www.g2.com/products/madgicx/pricing)
- [AdCreative.ai Reviews — Capterra](https://www.capterra.com/p/253052/AdCreativeai/reviews/)
- [Why We Ditched WordStream — The Marketing Agency](https://themarketingagency.ca/blog/review-ditch-wordstream/)

New sources gathered for this document:
- [CraftJack Reviews and Complaints — PissedConsumer](https://craftjack.pissedconsumer.com/complaints/RT-P.html)
- [Thumbtack Reviews — PissedConsumer](https://thumbtack.pissedconsumer.com/review.html)
- [HomeAdvisor Reviews — PissedConsumer](https://homeadvisor.pissedconsumer.com/reviews/RT-P.html)
- [Angi Leads Reviews — Trustpilot](https://www.trustpilot.com/review/homeadvisorpros.com)
- [Thumbtack Reviews — Trustpilot](https://www.trustpilot.com/review/thumbtack.com)
- [Why isn't the phone ringing? — mosierdata.com](https://mosierdata.com/2025/05/14/why-isnt-the-phone-ringing/)
- [Pay Per Lead vs. Monthly Retainer: Which Contractor Marketing Model Actually Works? — Minyona](https://minyona.com/blog/pay-per-lead-vs-retainer)
- [Anyone use angi leads? — Contractor Talk](https://www.contractortalk.com/threads/anyone-use-angi-leads.448799/)
- [CraftJack.com Any feedback? — Contractor Talk](https://www.contractortalk.com/threads/craftjack-com-any-feedback.105071/)

**Note on source reliability, inherited from `research/01`:** review-aggregator sources (PissedConsumer, Trustpilot, ComplaintsBoard, BBB) are self-selected toward negative experiences. Verbatim quotes above are used as directional evidence of real, recurring pain patterns, not as statistically representative satisfaction data. Reddit itself was largely unreachable via search indexing during this research pass (consistent with the finding already logged in `research/01`), so forum-adjacent evidence (Contractor Talk) and review-platform verbatims were used as the closest available substitute for in-the-trade owner language.
