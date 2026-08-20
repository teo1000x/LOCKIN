# MASTER ROADMAP

> **Delivery model: connected.** Foreman connects to the customer's Meta ad account and
> publishes the ads the owner approves. `docs/18-MODEL-DECISION.md` is authoritative and this
> file is written to it. The export handoff still exists, but only as interim behaviour while
> App Review is pending, not as the destination.

Single source of truth. Last updated 2026-08-19.

## The critical path, stated once

**Meta App Review and Business Verification have not been filed.** They are two sequential
queues, roughly 8 to 12 weeks combined, and **neither requires a single line of code to
exist.** Nothing else in this document takes as long or is as far outside our control. Every
day they sit unfiled is a day added to the end of the project.

File them first. Build in parallel behind them.

## What is actually true today

**Built and deployed.**
- Landing page, with the pricing, comparison, FAQ and trades sections.
- Estimator at `/estimate`, running against the full trade taxonomy.
- Legal pages at `/terms`, `/privacy` (with the `#deletion` section App Review requires) and
  `/refunds`. None have been reviewed by a lawyer, and each says so on its face.
- The booking pipeline: /book form, /api/callback persisting to Postgres, and /admin/leads
  behind fail-closed basic auth. Dark until DATABASE_URL and ADMIN_PASSWORD are set.

**Built but mock only.** The logged-in shell at `/app` renders entirely from
`src/lib/mock.ts`. It is a layout, not a product. There is no auth behind it, nothing is
persisted, and nothing it displays came from a database or from Meta.

**Not built at all.** Auth, billing, the intake wizard, the generation pipeline, the
competitive read, the approval workspace wired to real records, the export walkthrough,
publishing, and the leads inbox. Zero of these exist.

**Settled code, do not rewrite.** `src/db/schema.ts`, `src/lib/crypto.ts`,
`src/lib/content-hash.ts`, `src/lib/publish-decision.ts`, `src/lib/publish-guard.ts` with 10
passing tests, and `src/lib/trades.ts`. The schema already carries a `metaConnections` table,
so the reversal back to the connected model costs no schema rework.

**The trade taxonomy is 96 trades across 17 categories**, in `src/lib/trades.ts`. Any doc,
prompt, or wizard field that still assumes four trades (HVAC, plumbing, roofing, electrical)
is stale. Four trades carry `researched: true`, meaning we have read their live ads in the Ad
Library. The other 91 run on category-level patterns and every surface must say so in those
words rather than implying research we have not done.

**Three environment keys block all server work:** `DATABASE_URL`, `ANTHROPIC_API_KEY`,
`BETTER_AUTH_SECRET`. Nothing in Track B past B1.5 can start without them.

**Pricing is $499, $1,300 and $2,500 per month.**

**There is no refund policy.** Every card sale is final, `/refunds` states it in its first
line with the fine print the founder asked for, and no page on the site promises a refund.
Fixed 19 August, same day it was flagged.

**The name is a placeholder.** "Foreman" is not owned, and `foremanhq.com` is registered to
someone else. App Review is filed against a real app and a real domain, so this decision now
sits in front of the critical path rather than beside it.

## Owners

| Owner | Who | Meaning |
|---|---|---|
| **YOU** | Mateo | Accounts, money, legal, customer conversations, the ad playbook |
| **OP** | Claude, operator | Architecture, the inviolable code paths, review, integration |
| **AGENT** | Delegated subagent | Scoped work with explicit file boundaries |

---

# TRACK A: APPROVALS AND IDENTITY

Restored by the model decision. This track is the schedule. It is almost entirely YOUR work
and almost none of it is engineering.

| # | Item | Owner | Status |
|---|---|---|---|
| A1 | **Decide the name and buy the domain.** Recommendation delivered in `docs/21-NAME-AND-LOGO.md`: Bonded Crew, `bondedcrew.com` verified free at the Verisign registry on 19 August. Free domains get sniped, so buy immediately. | YOU | RECOMMENDED, waiting on purchase |
| A2 | Meta Business Verification: business documents, address, phone | YOU | NOT STARTED |
| A3 | Meta App Review submission for the publishing permissions: `ads_management`, `ads_read`, `business_management`, `pages_show_list`, `pages_read_engagement`, `pages_manage_metadata`, `leads_retrieval`, `instagram_basic`. Detail in `docs/03-META-PLAYBOOK.md`. | YOU + OP | NOT STARTED, longest lead time in the project |
| A4 | Screencast walkthrough App Review requires, showing each permission in use | OP | Needs enough UI to record. The only part of this track gated on code. |
| A5 | Meta identity verification for the Ad Library API, government ID, one time, separate from A2 and A3 and needs no App Review | YOU | NOT STARTED |
| A6 | Lawyer review of `/terms`, `/privacy` and `/refunds` before the first customer is charged | YOU | NOT STARTED |
| A7 | **Rewrite `/refunds` and the landing page value band to the no-refund policy.** A live page currently promises a refund the business will not honour. | OP | NOT STARTED, urgent |

**A4 is the only ordering constraint between this track and Track B.** Verification and the
permission request can be prepared and filed before the wizard exists. Do not let the build
schedule become the reason the filing is late.

---

# TRACK B: PRODUCT

## B0. Brand and design
| # | Item | Owner | Status |
|---|---|---|---|
| B0.1 | Name locked with a domain actually purchased | YOU | NOT STARTED, blocks A3 |
| B0.2 | Design system spec | AGENT | **DONE**, `docs/08-DESIGN-SYSTEM.md` |
| B0.3 | Logo and wordmark | AGENT | Blocked by B0.1 |
| B0.4 | Landing page | OP | **DONE and deployed.** Rename pass needed after B0.1. |
| B0.5 | Estimator at `/estimate` | OP | **DONE and deployed** |
| B0.6 | Legal pages | OP | **DONE and deployed**, lawyer review outstanding (A6) |

## B1. Foundation
| # | Item | Owner | Status |
|---|---|---|---|
| B1.1 | Next.js 16, TypeScript, Tailwind v4 scaffold | OP | **DONE** |
| B1.2 | Database schema including `metaConnections` | OP | **DONE**, valid under the connected model |
| B1.3 | Approval gate, pure logic plus database guard, 7 tests passing | OP | **DONE**, inviolable, do not rewrite |
| B1.4 | Envelope encryption for customer tokens, `crypto.ts` | OP | **DONE**, now load-bearing again |
| B1.5 | `DATABASE_URL`, `ANTHROPIC_API_KEY`, `BETTER_AUTH_SECRET` in `.env.local` | YOU | **BLOCKING everything below** |
| B1.6 | Provision Postgres, run the first migration | YOU + OP | Blocked by B1.5 |
| B1.7 | Better Auth with organizations | OP | Blocked by B1.5 |
| B1.8 | Stripe subscriptions at $499 / $1,300 / $2,500, billing portal | OP | Needs your Stripe account |
| B1.9 | GitHub repo, Vercel project, preview deploys | YOU + OP | |

## B2. Intake wizard
Six required questions produce a campaign. An optional depth section of roughly 15 fields
visibly sharpens the output. Skipping it must never feel like failure. Screen-by-screen copy
is specified in `docs/11-UX-SPEC.md` section D, which still describes a four-trade select and
needs a pass.

| # | Item | Owner | Status |
|---|---|---|---|
| B2.1 | Wire the wizard's trade question to the full 96-trade taxonomy in `src/lib/trades.ts`, searchable with the alias matcher, grouped by the 17 categories | OP | Taxonomy done, wizard not started |
| B2.2 | Wizard UI, one question per screen, state saved server-side on every keystroke | OP | |
| B2.3 | Service area, radius, exclusions | OP | |
| B2.4 | Offer input with per-category suggestions from `dominantOffer` | OP | |
| B2.5 | Budget input with the spend floor warning | OP | |
| B2.6 | Optional depth section with visible payoff | OP | |
| B2.7 | Photo upload and brand assets | OP | |
| B2.8 | **Ad account readiness check during onboarding**, not at the end: does the owner have a Page, a Business account, and a payment method Meta has approved. Meta's credit approval runs 24 to 48 hours, so this has to start in parallel with generation, not after it. | OP | |

## B3. Generation
| # | Item | Owner | Status |
|---|---|---|---|
| B3.1 | Zod blueprint schema for plan plus ads | OP | |
| B3.2 | Anthropic tool-use pipeline, structured output | OP | |
| B3.3 | **Smart defaults engine**: targeting, placements, budget pacing, schedule, optimization goal, each derived and each carrying a plain-English reason | OP | |
| B3.4 | Copy priors per category, built from YOUR ad playbook. 17 categories, not 4 trades. | OP + YOU | Blocked on the playbook |
| B3.5 | The marketing plan artifact, readable by someone who has never bought an ad | OP | |
| B3.6 | Image generation via fal.ai, real photos preferred, generated images always labelled as generated | OP | |
| B3.7 | Meta ad policy pre-flight lint, using the per-category `watchOut` rules already in `trades.ts` | OP | |
| B3.8 | Special Ad Category detection. Financing copy in remodel, specialty install and interior is the most likely trigger. | OP | |
| B3.9 | Plain-English rationale on every decision | OP | |
| B3.10 | Per-org cost metering and generation ceilings | OP | Inviolable rule 6 |
| B3.11 | Prompt injection hardening on all owner-supplied text | OP | Inviolable rule 4 |

## B4. Competitive read, feasibility YELLOW

**The correction still stands.** Ad Library access is easy, identity verification only, no App
Review. But open keyword and geographic search does not return US local ads: Meta returns
non-EU ads only when they concern social issues, elections or politics. There is no radius
filter and no advertiser-location filter.

The pipeline that works is two stage. Resolve candidate competitor Facebook Pages from an
outside local business directory such as Google Places, filtered by the business's stored
coordinates and radius. Then batch query `ads_archive` with `search_page_ids`, 10 Page IDs per
call. Accuracy is bottlenecked by directory resolution, not by Meta.

| # | Item | Owner | Status |
|---|---|---|---|
| B4.1 | Local business directory integration to resolve competitor Pages by trade and geography. Paid dependency, needs an API key. | OP | |
| B4.2 | Ad Library client using `search_page_ids`, batched 10 per call | OP | |
| B4.3 | Market-level cache keyed on trade plus geography bucket, never per customer, so every business in a metro shares one fetch. 14 day TTL with data, 3 day for thin markets. Rate limit is roughly 200 calls per hour per token. | OP | |
| B4.4 | Fallback UX so a thin market never shows an empty box | OP | |
| B4.5 | Token rotation. The 60 day expiry is real and unmitigated by default. A System User token likely fixes it but must be smoke tested against the real Business Manager flow. | OP | |
| B4.6 | YOU read the Ad Library terms on data redistribution before shipping | YOU | |

Data model proposed in `docs/15-AD-LIBRARY-API.md`.

## B5. Review, approval and publishing

This is where the connected model differs from the export model. Everything upstream is
identical; the terminal step is swappable, and both terminal steps have to work because the
export path is what we sell on while App Review runs.

| # | Item | Owner | Status |
|---|---|---|---|
| B5.1 | Honest Facebook-style ad previews | OP | Component exists, mock data only |
| B5.2 | Per-variant approve, edit, regenerate, reject | OP | Mock only |
| B5.3 | Approval records with content hash, wired to `publish-guard.ts` against the real database | OP | Guard done, wiring not |
| B5.4 | **Meta OAuth connect flow**, requesting only the scopes the terms page publicly commits to. No personal profile, no messages, no friends, no page inbox, no budget or payment method writes. | OP | Blocked by A3 |
| B5.5 | **Publish pipeline**: campaign, ad set, creatives, lead form, written to the owner's account via the Marketing API. Published paused, activated as a separate explicit step. Idempotency keys and per-ad-account rate limiting. | OP | Blocked by A3 |
| B5.6 | Publish path routes through `publish-guard.ts` with no bypass. No scheduler and no batch action may publish anything not individually approved. | OP | Inviolable rule 1 |
| B5.7 | Ad rejection handling: we see the rejection, we bring a corrected version back to the approval gate | OP | |
| B5.8 | **Interim export path**: export pack plus a live versioned web walkthrough, never a static PDF, with a Copy button on every value the owner has to type. Ships first and sells first. | OP | |
| B5.9 | The FAQ interim note in `src/components/Faq.tsx` is removed the day A3 clears, and not before | OP | Note is live and correct today |

## B6. Results

Under the connected model, spend and leads become measurable. Booked jobs and job value stay
self-reported permanently.

| # | Item | Owner | Status |
|---|---|---|---|
| B6.1 | `leadgen` webhook and leads inbox, with notification inside seconds | OP | Blocked by A3 |
| B6.2 | Nightly performance sync from the ad account | OP | Blocked by A3 |
| B6.3 | **Measured versus reported labelling on every screen that shows a number.** Never render a Meta-sourced figure beside a self-reported one without saying which is which. | OP | |
| B6.4 | Self-report entry for booked jobs and job value, offered and never required | OP | |
| B6.5 | Dashboard that is useful before any connection exists and gets better after | OP | Mock version exists |

## B7. Trust and operations
| # | Item | Owner | Status |
|---|---|---|---|
| B7.1 | Clean disconnect, token revocation, and full data export | OP | Required by the published privacy commitments |
| B7.2 | Spend guardrails: hard daily cap, owner-set ceiling, anomaly alarm that pauses and notifies | OP | |
| B7.3 | Sentry, PostHog, structured logging, with a rule that no token is ever logged | OP | |

---

# TRACK C: CUSTOMERS

Still the track that decides whether this becomes a company. It does not wait on Meta, because
the interim export path lets a customer get value before App Review clears.

| # | Item | Owner | When |
|---|---|---|---|
| C1 | List 20 service business owners you can contact | YOU | This week |
| C2 | Call 5. Show the estimator, which is live today and needs no login. Ask what is wrong with it. | YOU | Week 1 to 2 |
| C3 | Record objections verbatim | YOU | Ongoing |
| C4 | Convert 3 into paid design partners | YOU | Week 2 to 4 |
| C5 | **Watch one real non-technical owner attempt the export walkthrough cold**, before a paying customer. Nothing substitutes for this. | YOU | Week 3 to 6 |
| C6 | Capture every manual decision you make for them as a copy prior for B3.4 | YOU + OP | Ongoing |
| C7 | Document real results with real numbers, sourced to a real account | YOU | Once campaigns have run |

**How your background is used, and how it is not.** You have personally run ads for roughly
400 local businesses through prior work, and that experience is the single most valuable input
into B3.4 and B3.3. It is not a product result. Foreman has zero customers and zero results,
and inviolable rule 3 means no user-facing surface may present your prior work as though the
software produced it. Describe it as your experience, in the first person, or not at all.

---

# WHAT YOU OWE ME

1. **File Business Verification and App Review.** Longest lead time in the project, needs no
   code, not started. Everything else is negotiable and this is not.
2. **The name and the domain.** `foremanhq.com` is gone. This now blocks the filing above.
3. **The three environment keys**: `DATABASE_URL`, `ANTHROPIC_API_KEY`, `BETTER_AUTH_SECRET`.
   Put them in `.env.local` yourself. Never paste a secret into chat.
4. **Accounts**: GitHub, Vercel, a Postgres provider, Stripe, Anthropic.
5. **Your ad playbook.** Offers that worked per category, copy that won and copy that died,
   radius defaults, budget floors, qualifying questions, and the mistakes owners always make.
   Voice memo is fine, `tools/yt-transcribe.py` transcribes it.
6. **Meta identity verification** for the Ad Library, government ID, one time.
7. **A lawyer on the three legal pages** before the first card is charged.

---

# THE A-Z ACCEPTANCE TEST

Not done until one real person who has never run an ad completes all of this unassisted.

1. Land on the site and understand what it does in under 10 seconds
2. Sign up and pay
3. Complete the wizard on a phone in under 3 minutes, finding their own trade among the 96
4. See a marketing plan they actually understand
5. See what competitors in their area are running right now
6. See finished ads with copy and images
7. Read a plain-English reason for every decision the software made
8. Edit one ad, regenerate another, reject a third
9. Approve the rest, and confirm an edited ad correctly demands re-approval
10. Connect their ad account, and see exactly which permissions were requested and why
11. Publish the approved ads, and find them paused in their own account under their own name
12. Activate, and later see spend and leads clearly labelled as measured while booked jobs are clearly labelled as reported by them
13. Cancel, disconnect, and export their data without emailing anyone

Until A3 clears, step 11 is replaced by the export walkthrough, and that substitution is the
single highest-risk step in the interim product.

Test with a real stranger. You know where the buttons are, which makes you the worst possible
tester.

---

# RISK REGISTER

| Risk | Severity | Mitigation |
|---|---|---|
| App Review and Business Verification not filed, 8 to 12 weeks of queue not yet started | **CRITICAL, ACTIVE** | Track A. File this week. Neither needs code. |
| A live page promises a 14 day refund the business will not honour | **CRITICAL, ACTIVE** | A7. Rewrite `/refunds` and the landing page value band. |
| No name and no domain, which now blocks the filing | **CRITICAL, ACTIVE** | A1 and B0.1 |
| No distribution, no customers | CRITICAL | Track C starts this week. The estimator is live and is a real conversation opener. |
| Owner cannot complete the interim export handoff alone | HIGH | Researched verdict says a typical non-technical owner working from a static document is unlikely to succeed first try. B5.8 plus C5. Shrinks to zero once publishing lands. |
| Publishing to a stranger's ad account with the owner's money on the card | HIGH | The approval gate is the only thing between generated content and live spend. B5.6, plus spend guardrails in B7.2. |
| Founder's 400-business track record gets presented as product results | HIGH | Inviolable rule 3. First person, or not at all. |
| Generated ads are generic across 96 trades when only 5 are researched | HIGH | Category-level priors from B3.4, and every surface says plainly which trades we have read live ads for. |
| Three missing env keys stall all server work | ACTIVE NOW | B1.5 |
| Competitive read is thinner than hoped | MEDIUM | Needs directory resolution and a paid API. Do not sell it as a headline feature until proven on a real metro. |
| Ad account token expiry at 60 days | MEDIUM | B4.5, System User token, smoke tested not assumed |

---

# CURRENT STATE

**Done:** landing page, estimator, three legal pages, all deployed. Next.js scaffold, database
schema, approval gate with 7 passing tests, envelope encryption, content hashing, the 96-trade
taxonomy. Nineteen strategy and spec documents, four research reports.

**Mock only:** the logged-in shell at `/app`.

**Blocked on you:** App Review, Business Verification, the name and domain, the three
environment keys, the ad playbook, the lawyer.

**Next, in order:** file Track A, fix the refund copy, then auth and the wizard against the
real taxonomy.
