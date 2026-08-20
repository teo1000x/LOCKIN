# Product Spec — v1

> Working codename: **Ignition**. Placeholder — replace throughout when you pick a name.

## What it is

Self-serve software a small service business buys directly. The owner answers a short set of
questions about their business, an AI builds a complete Meta campaign — targeting, budget,
lead form, and multiple ad variants with copy and imagery — and **nothing goes live until the
owner clicks approve.** The ads then publish into the owner's own Meta ad account, billed to
the owner's own card.

Reference point: PaceRev ($699 / $1,499 / $2,499 per month, Meta-only, 40+ trades).

## The core loop

```
1. ONBOARD    Owner connects Meta Page + ad account, answers the intake wizard
2. GENERATE   AI builds a campaign blueprint: structure, targeting, lead form, N ad variants
3. APPROVE    Owner reviews every ad in a real Facebook-style preview. Edit, regenerate, or reject.
              Nothing is created on Meta until this gate clears.
4. PUBLISH    Approved blueprint is written to Meta via the Marketing API into the owner's account
5. LEARN      Leads flow back in, performance syncs nightly, new variants are proposed —
              which re-enter the approval gate. The loop never bypasses step 3.
```

## Why the approval gate is the mechanism, not a limitation

The single loudest complaint about Meta Advantage+ and Google Performance Max is that they are
black boxes that spend money in ways the owner cannot see, predict, or veto. The competitive
research found the same theme under every failed self-serve competitor and every hated agency:
owners don't distrust automation, they distrust *unaccountable* automation. Icon — Thiel-funded,
elite team — led with "fully autonomous AI CMO" and went dark.

So the gate is the product's spine and it must be enforced architecturally, not by convention:

- **No code path may create or activate a Meta ad object without a persisted, timestamped
  approval record.** This is a database constraint and a service-layer invariant, not a UI rule.
- Every campaign is published **paused**, then activated as a separate, explicit step.
- Every AI decision ships with a plain-English "why": _"Targeting 12 miles around your shop
  because that's the radius your last 30 jobs came from"_ — never a confidence score, never jargon.
- The owner can pause everything from one button, and export or disconnect at any time.

Radical transparency is also cheap for us and structurally expensive for incumbents whose
margins depend on opacity — and Meta Policy 10.5 (effective 2027-02-03) forces the whole
market our direction anyway.

## Intake wizard — the inputs

Kept deliberately short. Every field must either change the generated campaign or be dropped.

**Business**
- Trade / business type (from a curated taxonomy — drives copy priors and compliance rules)
- Business name, website, phone
- Meta Page + ad account (OAuth)
- Hours, and whether they take emergency/after-hours calls

**Services & offer**
- Services to advertise (multi-select, scoped to the trade)
- The offer — the single highest-leverage field. Examples: "$89 A/C tune-up",
  "Free roof inspection", "$50 off first clean". Owners routinely get this wrong, so this
  field gets AI suggestions benchmarked against what converts in their trade.
- Average job value (drives the cost-per-lead target and the budget recommendation)

**Geography**
- Address + radius, or explicit list of ZIPs / cities
- Exclusions (areas they refuse to drive to) — a small feature owners care about enormously

**Budget**
- Daily budget, with a recommended floor. Research puts the floor where paid ads can learn at
  roughly $1,000–1,500/mo total spend; the product should warn, not silently underperform.

**Creative inputs**
- Photo upload (real job photos outperform stock for trades — push hard for these)
- Logo, brand colors
- AI image generation as the fallback when they have no photos

## What the AI generates

A **campaign blueprint** — a single reviewable, versioned object:

- Campaign: objective, Special Ad Category determination, naming
- Ad set: geo targeting, age/gender, placements, optimization goal, schedule, daily budget
- Lead form: field schema plus qualifying questions tuned to filter out the junk leads that
  make owners hate lead ads
- 3–5 ad variants: primary text, headline, description, CTA, and image (uploaded or generated)
- A plain-English rationale attached to every one of these decisions

## Guardrails (must exist before a single real customer)

1. **Special Ad Category detection.** Housing, employment, and credit force restricted
   targeting. Most trades are clear, but property management, staffing, and anything with
   financing offers are not. Misclassifying this gets ads rejected or the account flagged.
2. **Policy pre-flight lint.** Screen generated copy against Meta's ad policies before it ever
   reaches review — no personal-attribute language ("are you overweight?"), no before/after
   imagery for aesthetics, no unsupported superlatives or guarantees.
3. **Spend guardrails.** Hard daily cap, a spend ceiling the owner sets, and an anomaly alarm
   that pauses and notifies rather than quietly burning budget.
4. **Prompt injection defense.** Owner-supplied text (business description, offer) flows into
   LLM prompts. It must be treated as untrusted data, never as instructions.

## Leads

Meta Instant Forms are the v1 lead surface — they convert far better for trades than sending
cold traffic to a website. On `leadgen` webhook: store the lead, notify the owner by SMS and
email within seconds, and expose it in a simple inbox.

Speed-to-lead is the highest-ROI feature in the entire product and among the cheapest to build.
An owner who books a job from a lead our software delivered within 60 seconds does not churn.

## Pricing (starting hypothesis)

Anchored on PaceRev and on what these businesses already pay adjacent vendors
(Podium $399–599/mo, Broadly ~$799/mo):

| Tier | Price | Includes |
|---|---|---|
| Launch | $499/mo | 1 business, 1 campaign, AI image credits |
| Grow | $999/mo | 1 business, up to 5 campaigns, priority generation |
| Multi | $1,999/mo | Up to 4 businesses — franchises, multi-location, small agencies |

Ad spend is always separate and always on the customer's own card. We never touch their media
budget — this is a Policy 10.5 requirement and a trust argument, in that order.

Undercutting PaceRev's $699 entry gives a clear wedge without landing in the low-price,
high-churn band where every dead competitor lived.

## Explicitly out of scope for v1

- Google Ads (v2 — the API gate is easier but Meta is where the described product lives)
- TikTok, Nextdoor, Yelp, Microsoft
- CRM integrations and offline conversion upload (v2 — this is the long-term moat, but it is
  not what gets a first paying customer)
- Call tracking
- Agency multi-client dashboards
- Automated budget reallocation without approval

---

## Addendum — the delivery model (clarified 2026-08-19)

The owner owns the ad account. We build the ads; nothing launches without their approval.

Three implementations of that promise, which differ *only* in the final step:

| | Mechanism | Meta permissions | Launch lead time |
|---|---|---|---|
| **A. Export / handoff** | We produce copy, creative, and a targeting spec. Owner sets it up in Ads Manager. | **None** | ~3 weeks |
| **B. Paused draft** | We create the campaign paused in their account; they publish it. | `ads_management` (both gates) | 8–12 weeks |
| **C. In-app approval, we publish** | They approve in our UI; we push it live. PaceRev's model. | `ads_management` (both gates) | 8–12 weeks |

**Key finding: B and C require identical permissions and identical approvals.** Making the
owner perform the final click buys no schedule relief. So if approval is coming regardless,
C is strictly better than B — it keeps the trust guarantee while removing the friction of
making a non-technical owner navigate Ads Manager.

The genuine fork is **A vs B/C**, and it is a runway decision, not a product one.

### Sequencing decision

Build A and C as the same product with a swappable terminal step.

Everything upstream of publishing — wizard, trade taxonomy, offer engine, blueprint schema,
LLM generation, policy lint, Special Ad Category detection, creative generation, and the
approval UI — is **identical in all three models**. That is roughly 95% of the build.

So: build the shared 95%, ship **A** to earn revenue while Meta's queue runs, and switch on
**C** as a one-click upgrade when `ads_management` is approved. Design partners acquired
under A migrate to C without changing anything they see except the disappearance of a
manual step.

This makes revenue independent of Meta's approval timeline — the single biggest risk to the
whole plan.

---

## PIVOT, 2026-08-19: no Meta connection. Generator, not manager.

Founder decision. The product does NOT connect to Meta at all. We generate the campaign and
the ads. The business owner posts them themselves. Smart defaults carry the optimization
thinking so the owner does not have to understand Meta's settings.

This is Model A from the addendum above, made permanent for v1. Model B and Model C are
withdrawn, not deferred.

### What this deletes

Gone entirely, along with every dependency on them:

- Meta App Review and Business Verification. Both gates, all 8 to 12 weeks of them.
- Marketing API Full Access tier and the 500-call catch-22.
- OAuth connect flow, System User tokens, token refresh, token health monitoring.
- Envelope encryption of customer ad tokens. There are no customer tokens.
- The publish pipeline, idempotency keys, and per-ad-account rate limiting.
- The `leadgen` webhook and lead ingestion.
- Business entity and EIN work as a blocker. The founder already holds an LLC and it is not
  on the critical path.

**Track A of the roadmap collapses to nothing.** The single largest schedule risk in the
project is removed. Time to a sellable product drops from 8 to 12 weeks down to roughly 3.

### What this costs, and it is not nothing

**Without a Meta connection we receive no performance data.** No spend, no impressions, no
leads, no cost per lead. The dashboard as previously specified cannot work, because every
number on it came from Meta.

The knock-on effects:

- The lead inbox has no leads to ingest. Meta instant-form leads go to the owner, not to us.
- "Booked customers" and "cost per lead" cannot be computed by us.
- The closed revenue loop and offline conversion upload are impossible. That was the
  long-term moat identified in the research, and it is now off the table for v1.
- Proof of results depends on owners voluntarily telling us what happened.

This is a real trade, and it is defensible for a v1 whose job is to reach revenue fast. It
should be a conscious choice, not a discovery made in month three.

### What survives, and one thing that gets better

- The intake wizard, unchanged.
- AI generation of the marketing plan and the ads, unchanged and now the entire product.
- Smart defaults encoding the optimization knowledge the owner lacks. This is now the core
  value, not a supporting feature.
- The review and approval step, which becomes review-before-export rather than
  review-before-publish. Still the trust spine of the product.
- The export pack: copy, images, targeting spec, and generated step-by-step Ads Manager
  instructions.

**The Meta Ad Library competitive read survives and becomes more important.** Worth being
precise about why, because it sounds like a contradiction: the Ad Library API reads
PUBLIC ad data and requires only that WE complete identity verification once. It does not
touch the customer's ad account, needs no permission from them, and involves no App Review.
It is the only live external data in the product and the strongest sales hook available.

### The open question the founder must answer

Since we cannot read results from Meta, how does the product show whether it worked?

- **Option A, pure generator.** No results tracking at all. We sell the plan and the ads.
  Simplest, fastest, and honest. Weakest retention, because the owner has no reason to
  return after generating.
- **Option B, owner self-reporting.** A lightweight weekly prompt: how many leads, how many
  booked, what were they worth. Cheap to build, keeps the dashboard meaningful, and produces
  the proof assets and copy priors we need. Depends entirely on owner discipline.
- **Option C, read-only Meta later.** Ship A or B now, add a read-only connection in v2.
  Read-only permissions are a materially lower approval bar than write access.

**DECIDED 2026-08-19: a mix of A and B.**

The core product is a generator and must be completely useful to someone who reports nothing
back. Self-reporting is offered, never required, and never nags.

Concretely:
- The product delivers full value on first use with zero tracking. Plan, competitive read,
  ads, export pack. An owner who never returns still got what they paid for.
- The dashboard must be genuinely useful with no self-reported data at all. It shows what was
  generated, what was approved, what was exported, and what to do next.
- Self-reporting is one lightweight prompt: how many leads, how many booked, what were they
  worth. It unlocks the results view rather than gating the product.
- The interface must make the payoff visible so reporting feels worth doing, and must degrade
  gracefully and silently when ignored.

This is a real design problem rather than a checkbox. A dashboard built assuming everyone
reports will be empty and demoralizing for the majority who do not. Read
`docs/11-UX-SPEC.md` section C for the three dashboard states.

Option C, a read-only Meta connection, stays on the table for v2. Read permissions are a
materially lower approval bar than write access.

---

## DECISION REVERSAL, 2026-08-19: Meta connection is back on

Founder decision. The product will connect to Meta after all. Work starts tomorrow.

This reverses the no-Meta pivot recorded above. What comes back:

- Meta App Review and Business Verification, both gates, roughly 8 to 12 weeks
- OAuth connect flow and System User tokens
- Envelope encryption of customer tokens, which `src/lib/crypto.ts` already implements
- Publishing to the customer's ad account after in-app approval
- The `leadgen` webhook and a real leads inbox
- Meaningful performance data, which unblocks the dashboard and the results loop

### Do this first, before writing any code

**File Meta App Review and Business Verification immediately.** They are the longest lead
time in the entire business and they run in parallel with everything else. Every day of
delay is a day added to the end. Permissions needed: `ads_management`, `ads_read`,
`business_management`, `pages_show_list`, `pages_read_engagement`, `pages_manage_metadata`,
`leads_retrieval`, `instagram_basic`. Full detail in `docs/03-META-PLAYBOOK.md`.

### Sequencing that does not waste the wait

The generator still ships first and still sells. Approval lands later and upgrades existing
customers in place. Nobody waits for Meta to get value, and revenue does not depend on the
queue. This is the same reasoning that made Model A the right v1; the only change is that
Model C is now a committed destination rather than an option.

### Copy consequence, immediate

Marketing copy written today around "you post it yourself" and "we never touch your ad
account" becomes false when publishing lands. **Write landing copy that is true in both
worlds.** The durable promise is the approval gate:

- Durable: "Nothing runs until you approve it." True before and after publishing.
- Durable: "Your ad account stays in your name, your card, cancel whenever."
- Expires: "You post it yourself."
- Expires: "We never connect to your ad account."

Lead with the approval gate, not the delivery mechanism. The gate is the actual product
promise and it survives the change.
