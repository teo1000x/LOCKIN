# AGENTS.md

> **Delivery model: connected, decided 19 August 2026.** Foreman connects to the customer's
> Meta ad account and publishes approved ads. This file has been brought in line with
> `docs/18-MODEL-DECISION.md`, which remains authoritative. Several documents under `docs/`
> have not been, and `docs/18` lists which ones.

Operating manual for any AI agent working on this project. Tool-agnostic.
If you are Claude Code, also read `CLAUDE.md`. If you are being dispatched as a subagent,
this file plus your task prompt is your full context. Read it before touching anything.

---

## The product in one paragraph

Self-serve SaaS bought directly by small local service businesses. The owner logs in, starts a
campaign, and answers six required questions plus an optional depth section. The AI produces
three artifacts: a **marketing plan**, a **competitive read** of what other businesses in
their area are running right now, and a set of **ready-to-post ads**. The owner reviews and
approves every ad, and Foreman publishes the approved ads into the owner's own Meta ad
account, billed to the owner's own card.

**The product connects to the customer's Meta ad account.** The account stays in the
customer's name, we hold scoped access, tokens are envelope encrypted through `crypto.ts` and
never logged. Smart defaults carry the optimization knowledge the owner does not have, so they
never configure targeting, placements, or bidding by hand. Full reasoning in
`docs/18-MODEL-DECISION.md`.

**Interim behaviour, until Meta App Review clears.** Publishing is not available yet, so the
product builds the campaign and walks the owner through posting it themselves. A note saying
so is attached to the first FAQ answer in `src/components/Faq.tsx`, commented for removal the
day App Review clears. Do not sell a plan whose main feature is unavailable without that note
on the page, and do not treat the export handoff as the destination.

Separate from all of the above: the **Meta Ad Library API** reads PUBLIC ad data using a token
WE hold. It needs one-time identity verification by the founder, no App Review, and no
permission or connection from the customer.

**The product covers 96 trades across 17 categories**, defined in
`~/Projects/ignition/src/lib/trades.ts`, which is the only correct source. Any doc that still
says four trades (HVAC, plumbing, roofing, electrical) is stale. Five trades carry
`researched: true`, meaning we have read their live ads. The other 91 run on category-level
patterns, and every surface must say so in those words rather than implying research we have
not done.

Pricing is $499, $1,300 and $2,500 per month. **Sales are final. There is no refund policy and
no money-back guarantee.** Any copy promising a refund window is wrong and must be corrected,
not repeated. Reference competitor: pacerev.com at $699 / $1,499 / $2,499 per month.

## Inviolable rules

Violating any of these is shipping broken work, regardless of how good the rest is.

1. **No ad is published to Meta, or included in an export pack, without a persisted approval
   record whose content hash matches the ad's current content.** Enforced in
   `src/lib/publish-decision.ts` and `src/lib/publish-guard.ts`, tests in `src/lib/__tests__/`.
   Editing an ad after approval invalidates that approval by design. Never route around the
   gate, never add a bypass flag, and never let a scheduler or a bulk action publish anything
   that was not individually approved. Connecting to Meta makes this rule more load-bearing,
   not less: the gate is now the only thing between generated content and live spend on a
   stranger's card.
2. **We never touch the customer's media spend, and we take no cut of it.** Meta bills the
   owner's own card directly. Our access is scoped to publishing and reading results: no
   personal profile, no messages, no friends, no page inbox, no raising a daily budget, no
   altering a payment method. Those limits are published on the terms page, so the
   implementation has to match them. Customer tokens are envelope encrypted via `crypto.ts`
   and never logged.
3. **Never publish a performance statistic we cannot source to a real account.** No invented
   case studies, no illustrative-but-fake numbers on any user-facing surface. The product has
   zero customers and zero results, so the honest answer is to show no numbers. The founder's
   prior work running ads for roughly 400 local businesses is his experience, not a product
   result: describe it in the first person or not at all. This rule has been broken once
   already.
   **Corollary, from the connected model:** the measured-versus-reported distinction must be
   visible on every screen showing a number. Spend and leads come from the ad account and are
   labelled as measured. Booked jobs and job value are self-reported and stay that way
   permanently. Never render one beside the other without saying which is which.
4. **Owner-supplied text is untrusted input.** Business descriptions, offers, and service
   names flow into LLM prompts. Treat them as data, never as instructions.
5. **Smart defaults are the product.** Every setting the owner is not asked about must be
   derived deliberately and carry a plain-English reason. A default with no reasoning behind
   it is a bug.
6. **Meter LLM and image generation per organization.** Every generation call records its
   cost. One power user must not destroy the margin on a subscription.
7. **No em-dash characters (U+2014) anywhere.** Not in code, docs, comments, or UI copy. Use
   a regular hyphen or restructure. This is the most-violated AI tell and the design skill
   bans it outright.

## Design authority

`docs/08-DESIGN-SYSTEM.md` is the binding specification for every visual decision. It
derives from the anti-slop design skill installed at `~/.claude/skills/taste-skill/SKILL.md`.

Before building or changing any UI:
1. Read `docs/08-DESIGN-SYSTEM.md`.
2. Read Section 9 of the taste skill, the forbidden AI-tell patterns.
3. Run the pre-flight checklist at the end of the design system doc before declaring done.

Design read for this project, already decided, build to it:
> B2B SaaS for non-technical trades owners reading on a phone between jobs. Plain-spoken
> utilitarian language. `DESIGN_VARIANCE 6 / MOTION_INTENSITY 3 / VISUAL_DENSITY 4`.
> Motion is deliberately low. This audience is not design-conscious and trust beats delight.

Palette is locked to white, cool grey, and one saturated cobalt accent. One accent color
across the entire product. Do not introduce a second.

---

## Voice rules for anything a customer reads

The buyer is a contractor, not a marketer. Every one of these is a hard rule.

- **Leads, jobs, and dollars.** Never CTR, CPM, ROAS, or impressions as a primary metric.
- **Plain-English rationale on every AI decision.** "Targeting 12 miles around your shop
  because that is where your last 30 jobs came from." Never a confidence score.
- **Specifics beat adjectives.** "$89 tune-up" not "compelling offers." "Your ad ran 4 days
  and booked 3 jobs" not "strong performance."
- **Banned filler verbs:** elevate, seamless, unleash, revolutionize, supercharge, next-gen,
  streamline, empower.
- Read every sentence back as if a plumber is reading it. If it sounds like software
  marketing, rewrite it.

---

## The delegation model

One operator, many scoped agents.

**The operator** holds architecture, sequencing, and review. It writes the inviolable code
paths (the approval gate, encryption, rate limiting, cost metering) and does not delegate
them. It integrates and reviews everything an agent returns.

**Agents** get one scoped deliverable each, with explicit file boundaries. An agent never
decides product strategy, never changes the inviolable rules, and never writes outside the
paths named in its prompt.

### Dispatching an agent

Every agent prompt must contain all six of these. A prompt missing any of them will produce
work that has to be redone.

1. **Required reading**, with exact file paths. Agents start cold and know nothing.
2. **The scoped deliverable**, stated as an artifact, not a topic.
3. **Exact output file paths.** An agent must never write outside them.
4. **The constraints that apply**, including the em-dash ban and any relevant inviolable rule.
5. **The definition of done.** What must be true for this to be accepted.
6. **What to return**, and how long. Agent output is not shown to the user, so the operator
   must relay it.

### Reviewing agent output

Never accept an agent's summary as fact. Verify:
- Does the artifact exist at the stated path, and is it the stated length?
- Does it obey the inviolable rules, especially the em-dash ban and the no-fabricated-stats rule?
- For code: does it typecheck, do tests pass, does it route around the approval gate?
- For research: are claims sourced, or asserted?

---

## Repository layout

```
LOCK IN/                      docs, research, strategy. Lives in iCloud.
  ROADMAP.md                  master plan, three tracks, ownership
  CLAUDE.md                   Claude Code project instructions
  AGENTS.md                   this file
  docs/                       numbered specs, 00 through 18
  research/                   four source research reports with citations
  tools/yt-transcribe.py      pull YouTube captions to text
  transcripts/                transcription output

~/Projects/ignition/          the application. Local disk, NOT iCloud.
  src/db/schema.ts            full data model, includes metaConnections
  src/lib/crypto.ts           envelope encryption for OAuth tokens
  src/lib/content-hash.ts     hash of approvable ad content
  src/lib/publish-decision.ts THE APPROVAL GATE, pure logic
  src/lib/publish-guard.ts    approval gate, database-backed
  src/lib/trades.ts           96 trades, 17 categories. The taxonomy.
  src/lib/market.ts           real Ad Library advertisers for researched trades
  src/lib/mock.ts             mock data for the app shell. Never a marketing surface.
  src/lib/__tests__/          gate tests, currently 7 passing
  src/app/page.tsx            landing page, deployed
  src/app/estimate/           estimator, deployed
  src/app/{terms,privacy,refunds}/  legal pages, deployed, not lawyer reviewed
  src/app/(app)/app/          logged-in shell. MOCK DATA ONLY, no auth behind it.
```

Built and deployed: landing page, estimator, legal pages. Mock only: the logged-in shell.
Not built at all: auth, billing, wizard, generation, competitive read, publishing, leads.
`DATABASE_URL`, `ANTHROPIC_API_KEY` and `BETTER_AUTH_SECRET` are missing and block all server
work. If a task assumes a working database or a logged-in user, check `ROADMAP.md` first.

The application deliberately lives outside iCloud. `node_modules` inside iCloud causes sync
conflicts and phantom build failures. Do not move it back.

---

## Document map

| File | What it settles |
|---|---|
| `docs/18-MODEL-DECISION.md` | **Authoritative.** The connected delivery model, and what it supersedes. Read first. |
| `ROADMAP.md` | Everything to be done, who owns it, in what order |
| `docs/00-RESEARCH-SYNTHESIS.md` | Market evidence behind every strategic decision |
| `docs/01-PRODUCT-SPEC.md` | What we are building. Stale below the reversal section; its pricing and its four-trade taxonomy are both wrong. |
| `docs/02-TECH-STACK.md` | Locked stack decisions with cost estimates |
| `docs/03-META-PLAYBOOK.md` | Meta approval gates, rate limits, token strategy |
| `docs/04-ROADMAP.md` | 90-day sequencing under a short runway |
| `docs/05-UI-DESIGN.md` | Screen inventory and information architecture |
| `docs/06-WHAT-I-NEED-FROM-YOU.md` | Founder-blocking items |
| `docs/07-NAMING.md` | Name and domain decision with verification |
| `docs/08-DESIGN-SYSTEM.md` | Binding visual specification |
| `docs/09-SIX-PS.md` | Pain, Promise, Product, Plumbing, Packaging, Proof |
| `docs/10-CLIENT-HANDOFF.md` | Client journey, onboarding, support, offboarding |
| `research/01` through `research/04` | Source research with citations |

---

## Current phase

**File Meta App Review and Business Verification, and build the web app behind them.** The two
Meta queues are roughly 8 to 12 weeks combined, neither needs any code to exist, and neither
has been filed. They are the critical path. The product name is still a placeholder and the
domain is not owned, which now blocks the filing. See `ROADMAP.md` Track A.

`docs/10-CLIENT-HANDOFF.md` was written before the export pivot, so its Meta access handoff
section is relevant again rather than obsolete. Read it against `docs/18-MODEL-DECISION.md`.

**Agent delegation is currently blocked** by the account monthly spend limit. Six dispatched
agents were killed mid-task. Until the limit is raised, the operator works inline.
