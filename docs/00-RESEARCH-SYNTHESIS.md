# Research Synthesis — v1
_Compiled 2026-08-19 from `research/01`–`research/04`. Read those for sources._

## The one-paragraph version

Small service businesses will pay real money to make their phone ring with good jobs.
They will not pay for an ads dashboard. Every previous attempt to sell them "AI runs your
ads" self-serve has either died (Icon, Qwaya), been absorbed (AdEspresso, Automate Ads,
Pattern89), or survived only by fleeing upmarket to agencies (Revealbot, Metadata.io,
Smartly). The mechanical work those tools automated — bidding, budget pacing, negative
keywords — has since been commoditized by Google Smart Bidding and Meta Advantage+ and is
worth approximately nothing as a moat. What is still broken, universally, is the loop
between ad spend and actual booked revenue. That gap is the only defensible place to build.

## Five findings that should change the plan

### 1. The mechanical automation moat is gone
Google's Smart Bidding and Meta's Advantage+ already do bid management, budget pacing, and
audience expansion better than a third-party tool can. Building "AI that optimizes your
campaigns" in 2026 means competing with the platforms' own free, better-informed systems.
It is also the exact feature set every dead competitor led with.

### 2. Owners judge ads by jobs, not metrics
Verbatim from the field: an agency reports "80 calls" when 5 were real — the other 75 were
out-of-area, spam, wrong service, or existing customers asking about a bill. Owners think in
jobs and dollars. They have no idea what a CTR is and correctly do not care. Any product
whose primary surface is CPM/CTR/ROAS is speaking a language the buyer does not use.

### 3. The closed loop is the actual white space
The chain — **ad click → tracked call/form → lead qualified as real or junk → job booked in
CRM → revenue recorded → pushed back to Google/Meta as an offline conversion** — is what
makes the platforms' own AI optimize toward profitable jobs instead of cheap clicks.
ServiceTitan does this natively for its large customers. The long tail on Housecall Pro,
Jobber, and HighLevel mostly cannot, and duct-tapes it through Zapier if at all. Housecall
Pro gates full API access behind its top-tier MAX plan. That gap is the product.

### 4. Trust and legibility are the emotional wedge, not capability
The loudest complaints about incumbents are not "it doesn't work" — they are "I can't tell
if my money is working" and "I couldn't leave." Hibu sits at 2.1/5 with reports of a price
increase via unsigned addendum and websites held hostage on cancellation. Scorpion locks
clients into a proprietary CMS. The differentiator available to a newcomer is radical
transparency and a clean exit — which is cheap to build and impossible for incumbents whose
revenue depends on opacity.

### 5. Meta Policy 10.5 is a tailwind, if the billing model is right
Effective 2027-02-03, any intermediary buying ads on a client's behalf must expose complete,
unaggregated spend and campaign data to that client. This kills the classic agency
mark-up-the-media model. **Design implication, day one:** the customer owns their ad account
with their own card on file at Google/Meta; we charge a separately itemized SaaS fee. Never
run their spend through our books.

## Hard constraints from the platform research

| Constraint | Impact |
|---|---|
| Meta App Review ≈ 20 days per Meta's own 2026 guidance; each rejection restarts it | 4–8 weeks realistic worst case |
| Meta Business Verification is a **separate, sequential** gate (~5 days, 1–3+ weeks if documents mismatch) | Stacks on top of the above |
| Meta Full Access needs 500+ calls in 15 days at <15% error, but Dev Mode only touches accounts you own | Chicken-and-egg; must be farmed on test accounts first |
| Google Ads Basic Access: single gate, faster review, ~15,000 ops/day free | **Fastest legitimate path to a working v1** |
| Google Local Services Ads has **no campaign-creation API** — UI only | Zero-touch LSA is impossible; needs a manual setup step |
| Google Ads requires passkey sign-in for **new** OAuth refresh tokens from 2026-08-05 | Build into the connect flow now, not later |

## Unit economics from the domain research

- **Spend floor:** below ~$1,000–1,500/mo in ad spend, paid ads do not gather enough data to
  work. This is the hard bottom of the addressable market and it excludes most salons, most
  barbers, and a lot of small gyms.
- **Best-fit verticals:** HVAC, plumbing, roofing (budgets $1,000–$7,500+/mo, tickets
  $1,400–$20,000+, phone-driven, urgent). Pest control is a strong #4 on recurring-revenue
  economics. PI law has the biggest dollars per lead but the most sophisticated buyer.
- **Weak fits:** dentists and med spas are already served by vertical-specific agencies;
  gyms, salons, chiropractors are creative-driven, not attribution-driven, at lower budgets.
- **Pricing:** avoid pure %-of-spend (SMBs explicitly distrust the "you profit when I spend
  more" conflict) and avoid pay-per-lead entirely (the Angi/Thumbtack/HomeAdvisor model is
  the most hated thing in the category). Flat fee, or a small flat base plus a modest 5–8%
  spend component well under agency rates. Anchors already in the customer's budget: Podium
  $399–599/mo, Broadly ~$799/mo, HighLevel $97/mo entry.
- **Realistic ACV:** $1,200–$6,000/yr. **Expect churn** of 3–5%/mo, with 40–70% of all losses
  in the first 90 days. Onboarding speed-to-value is a bigger retention lever than price.

## Risks that are not solvable by building better software

1. **Platform risk is severe and immediate.** Google and Meta are shipping this exact
   capability into their own free tools. Anything we build that is a thin wrapper on their
   APIs can be deleted by a product launch.
2. **SMB churn is structural.** Single-product SMB vendors retain ~30% at two years; 
   four-product bundles retain ~80%. A one-feature product bleeds regardless of quality.
3. **No winner in this category used a normal self-serve SaaS funnel.** Jobber and
   ServiceTitan won through trade shows, trade associations, and peer trust. That is slow
   and does not suit a solo founder on a short runway — which is a go-to-market problem, not
   a product problem, and it will not be fixed by writing more code.
