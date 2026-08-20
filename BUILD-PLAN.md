# BUILD PLAN

Parallel execution plan. Last updated 2026-08-19.
Companion to `ROADMAP.md`, which holds the what. This holds the order and the concurrency.

## The product, locked

Small service businesses (HVAC, plumbing, roofing, electrical) buy self-serve software.
The owner answers six questions plus optional detail. AI produces three artifacts:

1. A **marketing plan** they actually understand
2. A **competitive read** of what other contractors nearby are running right now
3. **Ready-to-post ads**, copy and images

The owner reviews and approves every ad, downloads an **export pack**, and posts the campaign
themselves in Meta Ads Manager. We never connect to Meta. Smart defaults carry every
optimization decision so the owner never configures targeting, placements, or bidding.

Results tracking is **A plus B**: the product is fully useful with zero tracking, and
self-reporting is offered but never required.

---

## WAVE 1: running right now, 7 agents in parallel

All seven are independent. None blocks another.

| # | Agent | Output | Why it can run now |
|---|---|---|---|
| 1 | Name and domain lock | `docs/07-NAMING.md` | Depends on nothing |
| 2 | UX specification | `docs/11-UX-SPEC.md` | Design system already done |
| 3 | Positioning, packaging, pricing | `docs/12-THREE-PS.md` | Research already done |
| 4 | Trade playbook and smart defaults | `docs/13-TRADE-PLAYBOOK.md` | Pure domain research |
| 5 | Ad policy compliance ruleset | `docs/14-AD-POLICY-RULES.md` | Pure policy research |
| 6 | Ad Library API integration spec | `docs/15-AD-LIBRARY-API.md` | Pure API research |
| 7 | Export pack specification | `docs/16-EXPORT-PACK-SPEC.md` | Pure UX and Meta research |

**Two of these carry unusual weight.**

Agent 4 produces the trade playbook, which is the core intellectual property. With no Meta
connection there is no performance data to learn from, so the smart defaults are entirely
encoded judgement. The agent bootstraps it from public benchmarks and marks every item the
founder must confirm from his own experience.

Agent 7 specifies the export pack, the highest-risk deliverable in the product. The owner
must take our output and build the campaign in Ads Manager alone. If they cannot, nothing
else matters. That agent has been instructed to give an honest verdict on completion
likelihood rather than an encouraging one.

---

## WAVE 2: unblocked as Wave 1 lands

| # | Task | Blocked by | Can parallelize with |
|---|---|---|---|
| 8 | Logo and wordmark | Name (1) | 9, 10, 11 |
| 9 | Landing page rebuilt to design system | Name (1) | 8, 10, 11 |
| 10 | Strip Meta-connection code from schema | Nothing, operator does it | 8, 9, 11 |
| 11 | Blueprint schema, Zod types for plan plus ads | UX (2), trade playbook (4) | 8, 9, 10 |

---

## WAVE 3: the application, once accounts exist

Needs `DATABASE_URL`, `ANTHROPIC_API_KEY`, `BETTER_AUTH_SECRET` in `.env.local`.

Three parallel streams that only converge at the end.

**Stream A, the shell**
- Better Auth with organizations, signup and login
- Stripe subscription and billing portal
- Deploy pipeline, GitHub to Vercel with preview builds

**Stream B, the input side**
- Trade taxonomy from the playbook, as queryable data
- Intake wizard, six required plus optional depth, state saved on every keystroke
- Mobile-first, since these people fill this out on a phone between jobs

**Stream C, the generation side**
- Anthropic tool-use pipeline producing structured blueprints
- Smart defaults engine, every derived setting carrying a plain-English reason
- Ad policy lint from the ruleset
- Image generation via fal.ai, real photos always preferred
- Ad Library client with caching
- Per-org cost metering

**Convergence**
- Approval UI, honest previews, per-variant approve, edit, regenerate, reject
- Wire to the existing approval gate, which already has 7 passing tests
- Export pack generation
- Dashboard in three states: empty, day one, steady
- Optional self-report flow

---

## Dependency graph, the short version

```
Name ─────────────┬──> Logo ──> Landing page
                  │
Design system ────┘   (both already unblocked)

Trade playbook ───┬──> Smart defaults engine ──┐
UX spec ──────────┤                            ├──> Approval UI ──> Export pack
Policy ruleset ───┼──> Generation pipeline ────┘
Ad Library spec ──┘

Accounts ─────────────> Auth ──> Billing ──> Deploy
```

The critical path runs through the trade playbook and the generation pipeline. Everything
else can be built around it or after it.

---

## What is NOT on the critical path anymore

Deleted by the no-Meta pivot. Do not build any of it.

- Meta App Review and Business Verification, both gates
- Marketing API access tiers and the 500-call qualification
- OAuth connect flow, System User tokens, token refresh and health monitoring
- Envelope encryption of customer tokens, there are no customer tokens
- Publish pipeline, idempotency keys, per-ad-account rate limiting
- Leadgen webhook and automatic lead ingestion
- Business entity and EIN work, the founder already holds an LLC

That removed roughly 8 to 12 weeks of schedule risk entirely outside our control.

---

## Blocking on the founder

| # | Item | Blocks |
|---|---|---|
| 1 | GitHub repo created and URL supplied | Deploy, backup, everything |
| 2 | `DATABASE_URL`, `ANTHROPIC_API_KEY`, `BETTER_AUTH_SECRET` in `.env.local` | All of Wave 3 |
| 3 | **The ad playbook** | Quality of every generated ad |
| 4 | Stripe account | Taking money |
| 5 | Meta identity verification, government ID, one time | Competitive read |
| 6 | 20 names of service business owners to call | Track C, the only track that decides whether this is a company |

Item 3 is the one no agent can produce. With no Meta connection there is no performance data,
so the smart defaults are the founder's experience encoded. Without it the generator is a
generic LLM wrapper, which is exactly what every dead competitor in the research shipped.

---

## Definition of done for v1

One real contractor who has never run an ad, unassisted:

1. Understands the site in under 10 seconds
2. Signs up and pays
3. Finishes the wizard on a phone in under 3 minutes
4. Reads a marketing plan they understand
5. Sees what competitors nearby are running
6. Reviews 5 finished ads and a reason for every decision
7. Edits one, regenerates one, rejects one, approves the rest
8. Confirms an edited ad correctly demands re-approval
9. Downloads the export pack
10. **Gets the campaign live in Ads Manager without calling anyone**
11. Cancels and exports their data without emailing anyone

Step 10 is the whole risk. Test it with a stranger in week 3, not month 3.
