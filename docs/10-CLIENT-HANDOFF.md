# Client Handoff and Onboarding Protocol - v1

_Compiled 2026-08-19. Read `00-RESEARCH-SYNTHESIS.md`, `01-PRODUCT-SPEC.md`, `03-META-PLAYBOOK.md`,
and `ROADMAP.md` first - this document assumes that context and does not repeat it._

## Why this document exists

The research synthesis found that 40-70% of all SaaS churn happens in the first 90 days, and
that onboarding speed-to-value is a bigger retention lever than price. Independent research on
SaaS onboarding backs the same number from the other direction: customers who hit "first value"
within 14 days retain at 80%+ at month 12, while customers who miss first value in the first 30
days retain at only 35-50%. Incomplete onboarding produces 3x higher 90-day churn (25% versus
8% for completed flows), and the top causes of stalled onboarding are lack of guidance (40%),
slow response times (40%), and incomplete documentation (31%) - all three of which a solo founder
controls directly ([Arcade](https://www.arcade.software/post/customer-onboarding-best-practices),
[SaaSmag](https://www.saasmag.com/time-to-value-saas-onboarding-retention-2026/),
[Onramp](https://onramp.us/blog/customer-onboarding-process)).

For this product specifically, one step in that journey - granting access to a Meta Business
Manager asset - is the single highest-friction, highest-abandonment moment in the entire flow.
This document treats it accordingly.

Everything below is written for a solo founder with no support team. Nothing here assumes a
customer success hire.

---

## 1. The full client journey, stage by stage

| # | Stage | Target elapsed time | Primary drop-off risk | Mitigation |
|---|---|---|---|---|
| 1 | First contact (site, referral, cold call) to sign-up | Owner understands the offer in under 10 seconds | Vague value prop; owner cannot tell if this is another lead-gen scam like Angi/Thumbtack | Lead with "we build your Facebook ads, you approve every one before it spends a dollar" - the approval gate, not the AI, is the trust hook |
| 2 | Sign-up and payment | Under 2 minutes | Being asked to pay before seeing any output - the single biggest sign-up-page drop-off in this category | For design partners: discounted rate, framed as "founding client," collected after a live demo, not cold off a landing page. For self-serve later: consider a short satisfaction guarantee so payment does not feel like a leap of faith |
| 3 | Intake wizard | Under 3 minutes, on a phone (this is the A-Z acceptance bar) | Field fatigue; being asked something that feels irrelevant or invasive; being asked for Meta access before they trust the product enough to grant it | Keep the wizard to business facts only (Section 2). Never request Meta access inside the wizard - request it only after the owner has seen and approved real ads |
| 4 | Blueprint generation | Under 60 seconds, with a visible progress state | Long silent spinner reads as broken, especially on a phone with a weak connection | Show named steps ("Reading your service area... Writing your offer... Building your first ad") rather than a bare loader |
| 5 | Approval | Under 10 minutes for the first pass | Decision overload (5+ ads, targeting, budget, all at once); fear of the "why" behind AI decisions | One card at a time, plain-English rationale on every field, sensible defaults pre-selected so approving is the fast path and editing is opt-in |
| 6 | Meta access handoff (concierge) or setup-pack handoff (self-serve export) | Concierge: access granted within 48 hours of approval. Self-serve export: campaign live in the owner's own account within 3-7 days | **The single largest drop-off risk in the entire journey.** Owner gets stuck in Meta's UI, gives up, and the subscription sits paid-for-but-inactive | See Section 3 in full. This step needs proactive founder follow-up, not a "waiting on you" ticket that sits silent |
| 7 | Campaign goes live | Within 24-48 hours of access/handoff completing | Founder becomes the bottleneck under concierge model if several clients hit this stage at once | Cap concurrent design partners at a number one person can hand-launch inside 48 hours (see Section 4) |
| 8 | First lead arrives | Owner is texted and emailed within 60 seconds of the lead landing (this is a hard product requirement, not a target) | If the first lead is spam or out-of-area, the owner loses faith in the entire product immediately, before it has had time to work | Lead-form qualifying questions tuned to filter junk before it reaches the owner; set expectations up front that a few junk leads are normal and here is how to tag them |
| 9 | First booked job | Within the first 7-14 days of the campaign being live | No bookings in two weeks with no explanation reads as "this doesn't work" even when the underlying funnel is fine and just needs a data point or two | Proactive day-7 and day-14 check-ins (Section 5) that read the lead tags and explain what is happening in plain language, before the owner reaches that conclusion alone |
| 10 | First bill after trial/pilot period | Day 30 | Owner has not yet connected spend to a booked job in their own head | The week-4 check-in (Section 5) exists specifically to make that connection explicit before the charge hits |
| 11 | Renewal decision | Day 90 | This is where 40-70% of category-wide churn lands | Full week-by-week plan in Section 5 |

---

## 2. The intake data contract

Every field costs conversion. The rule from the product spec stands: a field earns its place
only if it changes the generated campaign. This maps directly to the wizard fields in
`01-PRODUCT-SPEC.md`.

### Required - ask, and ask early

| Field | Why it is required |
|---|---|
| Trade / business type | Drives copy priors, compliance rules (Special Ad Category), and the entire taxonomy |
| Business name, phone | Needed for the ad itself and the lead form |
| Services to advertise | Scopes what the campaign is even for |
| The offer | The single highest-leverage field in the whole wizard - what converts a click into a lead |
| Service address, radius or ZIP list | Targeting cannot exist without it |
| Daily budget | Gates the spend-floor warning and the whole campaign structure |

### Optional - offer, do not require

| Field | Why it stays optional |
|---|---|
| Photo upload | Real job photos outperform stock, and the wizard should push hard for them, but AI-generated fallback imagery means this cannot be a blocking field |
| Logo, brand colors | Nice-to-have polish, never worth a drop-off |
| Exclusions (areas they refuse to drive to) | Small feature owners care about a lot when they think of it, but few think of it unprompted - surface it as an optional add-on after the primary radius, not a required step |
| Website | Most trades ads should point to the lead form, not a website, so this is reference-only |

### Infer or default - never ask directly

| What we need | How we get it without asking |
|---|---|
| Budget floor / recommendation | Compute from trade + average job value + the $1,000-1,500/mo research floor; show it as a pre-filled recommendation with a "why," not a blank field |
| Radius default | Default to a sane per-trade radius (for example 12 miles) pre-filled on the map; owner drags to adjust rather than typing a number |
| Age/gender targeting | Never ask. Infer from trade and Special Ad Category rules |
| Ad schedule / day-parting | Default to business hours plus an emergency-hours flag, itself inferred from a single "do you take after-hours emergency calls" yes/no already in the wizard |
| Special Ad Category determination | System infers this from the trade taxonomy; the owner should never see the term "Special Ad Category" unless a determination requires them to confirm something |
| Average job value | Ask once, in plain language ("what's a typical job worth to you") - it looks like a business question, not a marketing question, and owners answer it readily |

### Never ask - these kill conversion

- Meta Business Manager ID, ad account ID, or any Meta-internal identifier, inside the wizard. A
  non-technical owner does not know what these are, and asking signals "this is going to be
  technical," which is the exact fear the product exists to remove.
- CTR, CPC, ROAS, or any advertising-metric vocabulary. The research synthesis is explicit that
  owners think in jobs and dollars, not marketing metrics, and correctly do not care about the
  difference.
- Campaign objective, bid strategy, or optimization event as a manual choice. These are ours to
  decide and explain, never theirs to configure.
- A "tell us about your business" open text field. It feels like homework, produces low-signal
  data, and is the kind of field that turns a 3-minute wizard into an 8-minute one.
- Competitor names or competitive positioning questions. This reads as a consulting engagement,
  not a software sign-up, and slows momentum for no product benefit.
- Legal/tax identifiers (EIN, business license number) anywhere in the client-facing wizard. Keep
  legal identity strictly inside our own Business Verification paperwork with Meta - it is never
  the client's problem and asking for it mid-wizard reads as a scam pattern this exact audience
  has been burned by before (Angi, Thumbtack, HomeAdvisor).

---

## 3. The Meta access handoff - the riskiest step in the journey

This is the step where the product's entire trust proposition is tested in the real world, not
in a pitch. Two different versions of it exist right now, and a third replaces both once Track A
clears.

### Why this step is dangerous

Search-based research on this exact flow is consistent: the failure points are not conceptual,
they are mechanical. Owners get lost inside Meta's own settings UI, not inside ours, and Meta
gives almost no help along the way
([Jotform](https://www.jotform.com/blog/how-to-add-an-agency-partner-to-my-facebook-business-manager/),
[Leadsie](https://www.leadsie.com/blog/request-facebook-ad-account-access)).

### The three paths, and when each applies

| Path | When it applies | Who does the Meta-side work | Meta permissions needed |
|---|---|---|---|
| **A - self-serve export** | General Model A clients, self-serve, no founder involvement | The owner, alone, in their own Ads Manager, following our generated setup pack | None - we never touch their account |
| **A - concierge (design partners)** | Current state per `ROADMAP.md` Track C5, while Track A is in Meta's review queue | The founder, using access the owner grants manually | Owner grants the founder personal Advertiser-level partner access |
| **C - automated publish** | Unlocked once Meta App Review and Business Verification clear | Our app, via a Business Manager System User token | `ads_management`, `ads_read`, `business_management`, `pages_show_list`, `pages_read_engagement`, `pages_manage_metadata`, `leads_retrieval`, `instagram_basic` |

Path A self-serve requires nothing from the client but following instructions inside their own
account - it is the lowest-risk path precisely because no third party ever touches their assets.
Paths A-concierge and C both require the client to hand access to someone else, which is where
the real risk concentrates. Document the click path below for both.

### The click path - granting partner access (concierge, and the manual fallback for Model C)

This is what the owner is actually asked to do, step by step, using Meta's own Business Manager
partner flow
([Jotform](https://www.jotform.com/blog/how-to-add-an-agency-partner-to-my-facebook-business-manager/),
[Leadsie](https://www.leadsie.com/blog/request-facebook-ad-account-access)):

1. Go to `business.facebook.com` and log in with the Facebook account they use for their business
   Page (not a personal profile with no Page role).
2. Open Business Settings (menu icon, or the "Business Settings" link).
3. Under Users, click Partners (sometimes labeled "Partner Center").
4. Click Add, then choose "Give a partner access to your assets" (or "Ask a partner to share
   their assets," depending on which side initiates - we should always initiate, so the owner is
   receiving and approving a request, not composing one from a blank state).
5. Enter our Business Portfolio ID, which we supply pre-filled in a link or a copy-paste field -
   never ask the owner to type or find this themselves.
6. Select the specific assets: the Facebook Page, and the ad account (or "create a new ad
   account" if they do not have one yet, which is common and needs its own guided sub-step).
7. Select the permission level. We should always request Advertiser, never Admin - Admin is
   more access than the task needs and is a needless trust cost to ask for.
8. Confirm and send.
9. On our side, accept the request and confirm receipt back to the owner in plain language
   ("You're connected - we can see your Page and ad account now").

### Common failure modes, and what breaks at each one

| Failure mode | What actually happens | What our UI must do about it |
|---|---|---|
| Personal ad account instead of business | Many owners have only ever run a $20 "boost post" on a personal ad account tied to their profile, with no Business Manager at all | Detect this state before asking for access and walk them through creating a Business Manager and a proper ad account first - do not let them discover this mid-flow |
| Wrong Business Manager | Owner has two Business Manager accounts (common if a prior agency or a well-meaning employee created one) and grants access from the wrong one | Ask "do you already work with a marketing agency on Facebook?" before starting the flow, since the answer usually explains which Business Manager is live |
| Missing Page admin role | The owner is not actually an admin of their own Facebook Page - often an employee, a defunct agency, or a website developer set it up years ago and left the business as an Editor at best | This is the hardest failure mode to unstick and needs a documented recovery path (Meta's Page-role recovery flow) surfaced proactively, not discovered after the owner gives up |
| Two-factor authentication required | Meta requires 2FA on the account for most business-asset actions; if it is not set up, the grant silently fails or gets blocked | Check for 2FA status before starting the flow where possible, and if not, tell the owner up front: "Meta will ask you to turn on two-factor authentication - this takes two minutes and is required before you can share access" |
| An existing agency already holds partner access | A prior agency or website vendor (Hibu, Scorpion, and similar incumbents show up repeatedly in the research as parties that will not release assets willingly) still holds Admin access and has to be removed or the account is a mess of conflicting permissions | Ask directly during the wizard: "Does anyone else currently manage your Facebook ads?" This is also a trust moment - contrast our clean, revocable access model against the incumbent that will not let go |
| Silent abandonment | No confirmation screen, no error, the owner just stops midway and never says anything | Every step of our UI must show explicit state ("waiting for you to confirm in Facebook," "we haven't received access yet," with a manual "I'm stuck" escape hatch to a real human at every stage) |

### What our UI must show at each point

- Before starting: a one-screen preview of exactly what will be asked ("You'll grant us
  Advertiser access to your Page and ad account - this never gives us your password and you can
  remove it any time"), because unexplained permission requests are where trust breaks.
- During: a persistent status indicator ("waiting on you in Facebook") rather than a spinner,
  since the owner has left our product entirely and is now inside Meta's UI.
- On stall (no confirmation after roughly 24 hours): an automatic, human-toned nudge, not a
  robotic reminder - see the template in Section 8.
- On success: immediate, specific confirmation naming the actual Page and ad account connected,
  so the owner knows it worked and knows exactly what they connected.
- Always: a visible "I'm stuck" button that routes straight to the founder, because this step is
  the one place in the journey where self-serve is least likely to work unassisted.

### A note on tooling

Third-party access-request tools such as Leadsie exist specifically because this flow is broken
industry-wide - agencies report cutting onboarding time in half by using a single secure link
instead of the native multi-step Meta flow
([Leadsie](https://www.leadsie.com/blog/request-facebook-ad-account-access)). Worth evaluating
as a build-vs-buy decision once Model C is live and access requests are happening at volume;
not worth building custom for the handful of design partners under the current concierge model.

---

## 4. Design partner handoff protocol - Model A, manual period

This is the live protocol per `ROADMAP.md` Track C5: while Meta's review queue runs, the founder
runs client ads by hand using blueprints the software generates. Define it precisely so it stays
repeatable across every design partner rather than improvised per client.

### What the client is told, at kickoff

- "Ignition builds your campaign - the targeting, the offer, the ad copy, and the images. Right
  now, while we finish our direct-publish integration with Facebook, I personally take that
  finished plan and build it in your ad account by hand. You'll see and approve every ad before
  it goes live either way - that part never changes."
- A concrete timeline: campaign live within 48 hours of granting access.
- A concrete cadence: a written report every Friday (Section 8 template) until automated
  publishing takes over, at which point reporting moves into the in-app dashboard.
- An explicit statement that this is temporary and that nothing changes for them when it
  automates - same approval gate, same reports, just faster and inside the product instead of
  a weekly email.

### What the client hands over

- Partner access to their Facebook Page and ad account, Advertiser level, via the click path in
  Section 3.
- Confirmation of their daily budget and payment method already on file with Meta (never ours -
  spend never touches our books, per the Meta Policy 10.5 requirement in `03-META-PLAYBOOK.md`).
- Approval on every ad variant inside our product, exactly as Model C will work later. The manual
  step is invisible to the client's actual workflow.

### What the founder does

1. Receive the approved blueprint from the product (same schema Model C will publish
   automatically later - this is why B5.1/B5.2 export the blueprint in a structured format, not
   free text).
2. Log into the client's ad account using the granted partner access.
3. Build the campaign exactly as specified: same targeting, same budget, same lead form
   fields, same ad copy and images, in the same order the blueprint lists them.
4. Publish paused, then activate as a separate explicit step - identical discipline to the
   architectural rule in `01-PRODUCT-SPEC.md`, even though no code is enforcing it during the
   manual period. This is a personal process rule, not optional judgment.
5. Screenshot the live campaign and send the client the "you're live" confirmation same day.
6. Log every manual decision or deviation from the blueprint as a copy prior candidate for
   B3.3, per Track C6. This is where the product's actual differentiation gets built.

### What gets reported back weekly

See the template in Section 8. Structure: leads this week, tagged breakdown (Booked / Not a fit
/ No answer / Spam), cost per lead, and one plain-English observation. Never send raw Ads Manager
screenshots - the client should never have to interpret a platform dashboard, which is the exact
failure mode the research found owners hate about agencies ("80 calls" reported when 5 were real).

### Capacity limit

Manual, hand-built campaigns do not scale past a handful of concurrent clients for one person.
Cap active concierge design partners at a number that keeps every weekly report and every new
campaign build inside a normal work week - roughly 5-8 concurrent clients is a reasonable ceiling
for one founder also building the product. Do not take a 9th design partner client until Model C
is live or a design partner graduates off the manual list.

### Migrating to automated publishing without the client feeling downgraded

The client experience must not visibly change at the moment of cutover:

- Same approval screen, same wording, same "why" explanations - the only thing that changes is
  what happens after approval, and that happens behind the scenes.
- Send a short, positive note at cutover, not a technical one: "Your campaigns now publish
  automatically the moment you approve them - no more waiting on me. Everything else is exactly
  the same." Frame it as a speed upgrade, never as "the manual thing is over," which implies the
  manual thing was a lesser product.
- Preserve their weekly report cadence for at least two more cycles after cutover before folding
  it into the in-app dashboard, so the transition is felt as continuity, not a sudden withdrawal
  of attention.
- Never surprise a client with a changed campaign structure at cutover. The blueprint schema is
  shared between manual and automated publishing specifically so the campaign that goes live
  under Model C is identical to the one already running under manual Model A.

---

## 5. The first 90 days - week-by-week retention plan

Built directly against the research finding that 40-70% of churn happens here, and that
properly executed onboarding lifts 90-day retention by 15-25 percentage points over a generic
flow ([Arcade](https://www.arcade.software/post/customer-onboarding-best-practices)).

| Week | Proactive touch | What it checks for |
|---|---|---|
| Day 0 | Kickoff email immediately on payment (Section 8 template); wizard completed same session where possible | Momentum - the biggest drop-off in SaaS onboarding generally is the gap between day 1 and day 2 |
| Day 1-2 | "Your campaign is ready to review" notification the moment generation finishes | Did they come back to actually approve, or did payment stall out into silence |
| Day 2-3 | Manual check on Meta access handoff status; proactive nudge if not completed (Section 3, Section 8 template) | This is the highest-risk stall point in the entire journey |
| Day 7 | Personal check-in (text or call): "How did week one go? First leads coming in?" | Zero leads by day 7 is an early red flag worth a same-day look, not a wait-and-see |
| Day 14 | Weekly report (Model A) or dashboard nudge (Model C); explicit read of lead tags | Zero bookings by day 14 needs a plain-language explanation before the owner draws their own, worse conclusion |
| Day 21-28 | Offer/targeting tuning touch if lead quality is weak (many "Not a fit" or "Spam" tags) | Confirms the product is adjusting to real data, which is the entire pitch of "AI that learns," made visible |
| Day 30 | First bill lands. Send a "your first month" recap: leads, bookings, cost per booked job, in plain dollars | This is the moment that has to make the roughly $500-2,000/mo charge feel obviously worth it, or it does not survive the second month |
| Day 45 | Mid-point ROI check-in with real numbers, framed as "here's what this month bought you" | Confirms the value story is landing before the day-90 decision point |
| Day 60 | Expansion conversation if healthy (second campaign, second trade, tier upgrade); intervention if at risk (see below) | Distinguishes accounts worth growing from accounts worth saving |
| Day 75-80 | Case study / testimonial ask if the account is clearly healthy (this is the marketing asset the research says the whole category lacks) | Turns a healthy design partner into a distribution asset |
| Day 90 | Renewal decision point. Every account should already know, going in, exactly where it stands | This is the day the research says the category loses 40-70% of its customers - nothing here should be a surprise to either party |

### Churn-risk signals and interventions

Leading indicators predict churn before it happens; lagging indicators (a cancellation request)
confirm it after the decision is already made. Research on SaaS churn detection stresses acting
inside the 30-90 day window between disengagement and the churn event, since that is the only
window where intervention reliably works
([Perspective AI](https://getperspective.ai/blog/early-churn-warning-signals-2026-catch-at-risk-customers-before-they-leave),
[Rework](https://resources.rework.com/libraries/saas-growth/churn-risk-detection)).

| Signal | What it means | Intervention |
|---|---|---|
| Zero leads 14 days into a live campaign | Targeting, offer, or budget floor problem, or the campaign never actually launched | Same-day founder review of the live campaign; do not wait for the owner to notice and ask |
| 20+ leads with 0% tagged Booked | Lead quality problem (wrong offer, bad targeting) or the owner has stopped answering calls | Personal call, not email - this is a "your business, not just the software" conversation |
| Owner has not opened the lead inbox or tagged a lead in 7+ days | Disengagement - they have mentally checked out even if the campaign is performing fine | Text, not email, with a specific data point ("You've got 4 new leads waiting") to re-hook attention |
| No response to two consecutive weekly reports | Same as above, escalated | Phone call. If unreachable twice, flag as high risk for the day-60/day-90 review |
| Payment failure or card decline | Financial stress or has mentally moved on | Immediate personal outreach before an automated dunning email, which reads as impersonal at exactly the wrong moment |
| Support message containing "pause" or "cancel" | Direct signal | Same-day personal response; never let a cancellation request sit in a queue |
| Meta access handoff stalled 5+ days | Onboarding never actually completed, which means nothing downstream can work | This is the single most fixable churn cause in the whole journey - treat it as a fire, not a ticket |

---

## 6. Support model for one person

A solo founder cannot offer 24/7 live support and should not promise it. Set expectations that
are true on day one and stay true at 50 clients, and invest documentation time against the
highest-frequency, highest-friction question rather than answering it individually every time.

### Self-serve (documentation, no human involved)

- How to add photos / why real job photos beat stock
- What makes a good offer, with trade-specific examples
- How to read the lead inbox and what each tag means
- How to pause everything (one button, per B8.2)
- How to disconnect and export data (Section 7)
- Billing, plan changes, and cancellation
- **The Meta access click path, as a short video plus screenshots, not just text.** This is the
  single highest-frequency support question in the entire product and the one most worth
  over-investing in once, rather than walking someone through by hand every time. Every minute
  spent making this walkthrough clearer is worth more than any other support investment
  available to a one-person team.

### Async (email or text, same-business-day response committed)

- General "how do I..." questions not covered in docs
- Weekly report questions (Model A)
- Requests to adjust the offer, budget, or targeting
- Non-urgent billing questions

Commitment: reply within one business day, target under 4 business hours during 9am-6pm on
weekdays. No weekend response commitment - state this plainly during kickoff so it is never a
broken promise, only an honest one.

### Requires a call, no exceptions

- Meta access handoff stuck after one async attempt to unstick it
- Spend anomaly alarm triggered (B8.1) - always a call, never an email, given the stakes
- Any message containing "pause," "cancel," or "this isn't working"
- Business Verification document mismatches affecting a client indirectly (rare, but always a
  call given how confusing Meta's own rejection messages are)
- First campaign kickoff for every design partner during the concierge period (Section 4) - this
  one is a deliberate high-touch exception, not a general policy

### Where documentation beats repeated answering

Rank investment by frequency times friction, not just frequency. The Meta access walkthrough
sits at the top of that ranking by a wide margin: it is both the most common question and the
one most likely to end in a lost customer if answered slowly. Second priority: "what's a good
offer for my trade," since it recurs across every trade taxonomy and benefits from concrete,
trade-specific examples rather than generic advice.

---

## 7. Offboarding

The product's differentiator against Hibu, Scorpion, and the rest of the incumbent field is a
clean, fast, unconditional exit - the research synthesis is explicit that "I couldn't leave" is
one of the loudest complaints in the category, and that a clean exit is cheap for a newcomer to
build and structurally impossible for incumbents whose revenue depends on lock-in. Offboarding
is therefore a trust feature, not an administrative afterthought, and it should be at least as
polished as onboarding.

| What happens | How fast | Notes |
|---|---|---|
| Cancel subscription | Immediate, self-serve, no phone call or retention gauntlet required | Per the A-Z acceptance test: "cancel without emailing anyone" |
| Campaigns paused (not deleted) | Immediate | Never leave live spend running after a cancellation |
| Full data export - leads, blueprint history, creative assets, performance history | Immediate self-serve download (CSV plus images), or within 24 hours if any part requires manual assembly | Standard, portable formats only - no proprietary lock-in format |
| Our partner access to their Meta Page and ad account revoked | Within 24 hours, confirmed in writing | Applies to both the concierge partner-access model and any System User token issued under Model C |
| Billing stops | End of current billing cycle, no early-termination fee | State this plainly at kickoff so it is never a surprise mid-relationship |
| Confirmation | A specific email confirming exactly what was exported, what access was revoked, and that billing has stopped | Closes the loop explicitly - silence after a cancellation is exactly the kind of thing that turns an ex-customer into a bad reference |

---

## 8. Templates

### Kickoff email

> Subject: Welcome to Ignition - here's exactly what happens next
>
> Hi [Owner first name],
>
> Thanks for signing up. Here's the plan, step by step, so nothing is a surprise:
>
> 1. You'll answer a few quick questions about [Business name] - trade, service area, your best
>    offer. Takes about 3 minutes, and you can do it from your phone between jobs.
> 2. Ignition builds a complete campaign - targeting, offer, lead form, and several ad variants
>    with real copy and images.
> 3. You review every single ad before anything goes live. Nothing spends a dollar without your
>    approval - that's true today and it stays true forever, no matter how the product changes.
> 4. Once you approve, [I'll personally get this live in your ad account within 48 hours / this
>    publishes straight to your ad account automatically].
> 5. The moment a lead comes in, you get a text and an email within 60 seconds.
>
> The one step that trips people up is connecting your Facebook Page and ad account - it's a
> Meta thing, not an us thing, and their screens are confusing even for people who do this daily.
> I'll walk you through it directly when we get there, and there's a video guide too. If you get
> stuck for more than a minute, just reply to this email or text me at [number] - a real person
> answers, not a ticket queue.
>
> Let's get your first campaign built. [Start the wizard →]
>
> [Founder name]

### Intake checklist (internal, used to confirm a client is actually ready before generation)

- [ ] Trade / business type selected
- [ ] Business name, phone confirmed
- [ ] Services to advertise selected
- [ ] Offer entered (flag if left at the AI-suggested default with no owner input - worth a
      quick personal check that it's actually right for their business)
- [ ] Average job value entered
- [ ] Service radius or ZIP list set
- [ ] Daily budget set (flag if below the recommended floor and confirm the owner saw the warning)
- [ ] Emergency/after-hours flag answered
- [ ] Photos uploaded, or AI-image fallback explicitly acknowledged
- [ ] Existing agency/vendor question answered (feeds Section 3 risk check)
- [ ] Facebook Page admin status confirmed before starting the access request
- [ ] Two-factor authentication status confirmed before starting the access request

### Weekly report structure (Model A manual period)

> Subject: [Business name] - week of [date]
>
> **This week:** [N] new leads, [N] tagged Booked, [N] Not a fit, [N] No answer, [N] Spam
>
> **Cost per lead:** $[X] | **Cost per booked job:** $[X]
>
> **What I saw:** [One or two plain-English sentences - e.g. "Most of your leads this week came
> from the $50-off-first-visit offer. The two spam leads were from outside your service area,
> so I tightened the radius slightly for next week."]
>
> **What's next:** [Any change being made, or "no changes needed, campaign is performing well"]
>
> Questions or want something changed? Just reply.

### Churn-risk intervention email

Used when a churn-risk signal fires (Section 5) and a direct call has not yet connected. Tone
matters here more than any other template in this document - it must read as a business owner
checking in on a peer's business, not a vendor chasing a renewal.

> Subject: Quick check on [Business name]'s campaign
>
> Hi [Owner first name],
>
> I noticed [your campaign hasn't had a booked job in a couple weeks / you haven't had a chance
> to look at your leads recently / your last couple of leads came back as not a good fit] - I
> wanted to reach out myself rather than let it sit.
>
> This kind of thing is usually fixable fast: sometimes it's the offer, sometimes it's the
> radius, sometimes it's just that the leads need a faster callback. I'd rather spend ten
> minutes with you now than have you wonder if this is working.
>
> Do you have a few minutes for a quick call this week? Or if it's easier, just reply here and
> tell me what's going on with the leads you have gotten - I'll take a look at the campaign
> either way.
>
> [Founder name]
> [Phone number]

---

## Sources

- [Arcade - Customer Onboarding Best Practices for SaaS in 2026](https://www.arcade.software/post/customer-onboarding-best-practices)
- [SaaSmag - Time-to-Value: The New SaaS Retention Battleground](https://www.saasmag.com/time-to-value-saas-onboarding-retention-2026/)
- [Onramp - Customer Onboarding Process: 7 Stages to Reduce Churn in 2026](https://onramp.us/blog/customer-onboarding-process)
- [Upbeat Agency - How Do I Give An Agency Access To My Facebook Ad Account?](https://upbeatagency.com/how-to-give-agency-access-on-facebok/)
- [Leadsie - How to Request Access to a Facebook Ad Account in 2026](https://www.leadsie.com/blog/request-facebook-ad-account-access)
- [Leadsie - How to Grant Access to a Facebook Ad Account](https://www.leadsie.com/blog/grant-facebook-ad-account-access)
- [Jotform - How to add an agency partner to your Facebook Business Manager](https://www.jotform.com/blog/how-to-add-an-agency-partner-to-my-facebook-business-manager/)
- [DASH TWO - Ad Agency Access to Your Facebook Page Guide](https://dashtwo.com/blog/giving-agency-access-to-facebook-page/)
- [AgencyAccess - How to Give Access to a Facebook Business Page & Ads Account](https://www.agencyaccess.co/blog/how-to-give-access-to-facebook-business-page-and-ads-account)
- [Follow Up Boss - Troubleshooting Facebook Lead Ad Direct Integration: Two-Factor Page Permission Warning](https://help.followupboss.com/hc/en-us/articles/1500000016202-Troubleshooting-Facebook-Lead-Ad-Direct-Integration-Two-Factor-Page-Permission-Warning)
- [Command.ai - White glove vs. self-serve onboarding in SaaS](https://www.command.ai/blog/white-glove-vs-self-serve-onboarding-in-saas/)
- [Cyclr - Self-service vs white glove SaaS onboarding](https://cyclr.com/blog/self-service-vs-white-glove-saas-onboarding)
- [Perspective AI - Early Churn Warning Signals 2026](https://getperspective.ai/blog/early-churn-warning-signals-2026-catch-at-risk-customers-before-they-leave)
- [Rework - Churn Risk Detection: Early Warning Systems for Proactive Intervention](https://resources.rework.com/libraries/saas-growth/churn-risk-detection)
- [Housecall Pro vs Jobber (2026 comparison)](https://www.housecallpro.com/compare/housecall-pro-jobber/)
- [Field Service Software - Housecall Pro vs Jobber vs ServiceTitan: FSM ROI Breakdown](https://fieldservicesoftware.io/housecall-pro-vs-jobber-vs-servicetitan/)
