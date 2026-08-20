# 90-Day Roadmap

Written against a **sub-3-month runway**. The binding constraint is not engineering speed —
it is Meta's approval queue, which you do not control. So the plan runs two tracks in
parallel and deliberately decouples "getting paid" from "being API-approved."

## Track A — Approvals (start day one, mostly waiting)

| Week | Action |
|---|---|
| 1 | Business entity + EIN. Domain. Site with privacy policy, ToS, data-deletion callback |
| 1 | Meta App + Business Manager created with exactly matching name/address/domain |
| 1 | **Submit Business Verification** — longest, least predictable pole |
| 1 | Start Twilio A2P 10DLC registration (separate multi-week queue) |
| 2–5 | Dogfood on your own ad account, accumulating 500+ clean API calls at <15% error |
| 5 | Screen-record the end-to-end flow; **submit App Review** |
| 6–9 | Expect one rejection. Fix, resubmit. Apply for Full Access tier once call volume qualifies |

## Track B — Product (you control this entirely)

**Weeks 1–3 — the spine**
- Next.js + Drizzle + Neon + Better Auth orgs; Stripe subscription and Billing Portal
- Meta OAuth connect flow, envelope-encrypted token storage, token-health monitor
- Intake wizard, complete, with PostHog funnel instrumentation on every step

**Weeks 3–5 — generation and the gate**
- Campaign blueprint schema and the LLM generation pipeline (Anthropic tool-use structured output)
- Trade taxonomy with copy priors; offer suggestion engine
- Policy pre-flight lint + Special Ad Category detection
- **Approval UI**: real Facebook-style previews, per-variant edit / regenerate / reject
- Approval records persisted as a hard precondition on every publish path

**Weeks 5–7 — publish and close the loop**
- Meta publish pipeline via Inngest: idempotent, rate-limited, always publishes paused
- `leadgen` webhook → lead store → SMS + email alert in under 60 seconds
- Nightly performance sync; the simple owner-facing dashboard (spend, leads, cost per lead)

**Weeks 7–9 — the parts that decide retention**
- Variant proposals routed back through the approval gate
- Spend anomaly alarms; one-button pause-everything
- Clean disconnect and data export — the "easy to leave" promise, kept literally

## Track C — Customers (the one that actually kills solo founders)

Do not wait for either other track.

- **Weeks 1–2:** get 5 service business owners on the phone. Not a survey — show the wizard
  clicking through and ask what's wrong with it. Your ad experience is what makes this
  conversation credible; use it.
- **Weeks 2–6:** convert 3 into **paid design partners at a discount, starting immediately**.
  While the API is in review, run their ads *manually yourself* using the blueprints the
  software generates. This is legitimate, it is revenue during the queue, and it produces
  the exact training data and edge cases the automated version needs.
- **Weeks 6–12:** as approvals land, migrate design partners onto the automated pipeline. Their
  before/after results become the only marketing asset that matters in this category.

## The honest risk

Track A can slip past your runway through no fault of your own. Track C is the hedge: manual
delivery behind a real product creates revenue that is independent of Meta's queue. If you
skip Track C and wait for approval before selling, the most likely outcome is that you run out
of money holding a finished product with no customers.

## Definition of done for v1

A business owner who has never run an ad can, unassisted: sign up, pay, connect their Meta
account, answer the wizard, review AI-generated ads, approve them, see them go live in their
own ad account, and get an SMS when a lead comes in — with every step explainable in plain
English and reversible in one click.
