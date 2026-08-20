# Technical Architecture & Stack — Ad Management SaaS for Small Service Businesses

Research date: 2026-08-19. All pricing verified via web search against current (2026) vendor pricing pages and third-party trackers; where sources conflicted, the vendor's own pricing page framing is preferred and noted. This is a solo-founder / very-small-team, ship-fast, cheap-at-low-scale, don't-repaint-into-a-corner brief.

## Summary decision table

| Category | Primary recommendation | Runner-up | ~$/mo @ 0 customers | ~$/mo @ 50 customers | ~$/mo @ 500 customers |
|---|---|---|---|---|---|
| Framework | Next.js (App Router) | React Router 7 (Remix) | $0 | $0 | $0 |
| Hosting | Railway | Fly.io | $0–5 | $20–60 | $150–500 |
| Database | Neon (Postgres) | Supabase | $0 | $19–69 | $200–700 |
| ORM | Drizzle | Prisma 7 | $0 | $0 | $0 |
| Background jobs | Inngest | Trigger.dev | $0 | $30–75 | $300–1,000+ |
| Auth | Better Auth (self-hosted) | WorkOS AuthKit | $0 | $0 | $0–125 (if SSO needed) |
| Time-series metrics | Postgres + materialized views → ClickHouse Cloud/Tinybird at scale | Timescale (Tiger Data) | $0 | $0–25 | $200–800 |
| UI | shadcn/ui + Tailwind v4 + Tremor (charts) | Recharts | $0 | $0 | $0 |
| LLM | Claude API — Sonnet 5 default, Opus 5 for hard creative work | — | $0 | $20–100 | $300–1,500 |
| Monitoring/analytics/secrets | Sentry + PostHog + Doppler | Better Stack + Infisical | $0 | $26–60 | $150–400 |
| **Total infra (excl. LLM, excl. Claude's own dev time)** | | | **$0–15** | **$115–330** | **$1,300–4,100** |

Cost bands are wide on purpose — actual spend depends heavily on ad-account count per customer, sync frequency, and LLM usage per customer. Detailed reasoning and per-category source links follow.

---

## 1. Framework: Next.js App Router

**Primary: Next.js 15/16 (App Router).** Next.js remains the safest default for most B2B SaaS in 2026 due to ecosystem maturity, hosting-default gravity (Vercel, but also runs fine elsewhere via `next start` / standalone output), the largest hiring pool, and the deepest density of boilerplates (ShipFast, Supastarter, MakerKit, next-forge) that already wire up auth + billing + email. For a solo founder who needs to borrow scaffolding rather than build it from scratch, this ecosystem gravity is the deciding factor over any raw technical merit.

**Known pain points (2026, current):**
- Four separate cache layers (Router Cache, Data Cache, Full Route Cache, Request Memoization) interact non-obviously; teams routinely invalidate one layer while another still serves stale UI. Debugging requires `NEXT_PRIVATE_DEBUG_CACHE`, an undocumented env var.
- A known Data Cache memory leak in standalone mode causes OOM crashes in some configurations (workaround: avoid unique per-request headers in `fetch`, or set `cacheMaxMemorySize: 0`); unresolved in the repo as of mid-2026.
- Layout persistence causes state "stickiness" across route changes under the same layout — surprises teams new to the mental model.
- None of this is disqualifying for a CRUD + dashboard + billing app; it mostly bites teams doing aggressive ISR/PPR tuning, which this product doesn't need early on.

**Runner-up: React Router 7 (formerly Remix).** Remix merged into React Router v7 in early 2025, becoming the most widely installed routing library in the React ecosystem. Pick this if the team wants web-standards-first data loading (loaders/actions map directly to HTTP) without the RSC learning curve, or wants framework portability across hosts without Vercel-shaped defaults. Particularly strong for form-heavy flows (OAuth connect flows, campaign-builder wizards) which this product has plenty of.

**Not recommended for this brief:** TanStack Start (best client caching and type safety, but younger ecosystem — a bigger bet for a solo founder who needs battle-tested boilerplates, not the best DX on paper) and a separate Nest/Fastify/Hono backend + SPA (doubles the surface area — two deploys, two auth stories, CORS — for no benefit at this scale; only justified once the team is large enough to split frontend/backend ownership).

**What people are actually shipping serious B2B SaaS on right now:** Next.js App Router remains the majority default; React Router 7 gets picked for teams that value web-standards portability or got burned by App Router caching; TanStack Start shows up in greenfield, edge-first, type-safety-obsessed teams, especially those already on Cloudflare Workers.

Sources: [React Router v7 vs TanStack Start vs Next.js: Full-Stack 2026 - Kanopy](https://kanopylabs.com/blog/react-router-v7-vs-tanstack-start-vs-nextjs), [TanStack Start vs Next.js vs Remix 2026 — PkgPulse](https://www.pkgpulse.com/guides/tanstack-start-vs-nextjs-vs-remix-2026), [Next.js App Router in Production](https://pages.edgeone.ai/resources/nextjs-app-router-in-production), [Next.js App Router in 2026: Should Production Teams Adopt It Yet?](https://meisteritsystems.com/news/next-js-app-router-in-2026-is-it-ready-for-production/)

---

## 2. Hosting

**Primary: Railway.** For a solo founder, Railway wins on developer experience: Hobby is $5/mo (single developer), Pro is $20/mo flat including $20 of usage credits and unlimited seats, and everything (web app, Postgres if not using Neon, worker processes, cron) deploys from one dashboard with no separate configuration for long-running processes — which matters because this product needs long-running/scheduled jobs (nightly syncs, optimization loops) that Vercel's serverless model actively fights.

**Runner-up: Fly.io.** Pure pay-as-you-go per second, no base plan fee — cheapest at true near-zero usage (smallest instance ~$2/mo if left running), and better if the team wants multi-region latency control or needs to run genuinely long-lived processes/websockets. Steeper ops learning curve (fly.toml, machines API) than Railway's git-push-deploy simplicity.

**Vercel — do not use as primary compute for this product.** Vercel is excellent for the Next.js frontend/API routes themselves, but its serverless function model actively fights the "long-running + scheduled background jobs" requirement: functions bill at $0.128/Active-CPU-hour, $0.60/million invocations, with only 1,000 GB-hours included on Pro ($20/mo) before overage — a nightly sync job for hundreds of ad accounts risks blowing past that. Vercel Cron exists but is designed for short triggers, not durable multi-minute optimization loops. **Recommendation: use Vercel for the Next.js app (frontend + thin API layer) and Railway/Fly for the background-job workers**, OR skip Vercel and run the whole Next.js app on Railway/Fly to avoid managing two providers. Given "shippable fast," a single-provider Railway deployment (Next.js app + worker + Postgres if desired) is the simplest starting point; move the web tier to Vercel later only if edge/ISR performance becomes a bottleneck.

**Render:** wins on pricing predictability (fixed instance prices, free workspace for solo devs) but Standard tier ($25/mo for 1 CPU/2GB) is less cost-efficient than Railway's credit model at low scale, and cold starts on the free tier are a real UX cost during early demos.

**Cloudflare Workers — do not use for this product's compute.** CPU-time billing is attractive ($5/mo base) but standard Workers cap execution time hard; long-running jobs need Cloudflare Queues/Durable Objects/Workflows, which is a fundamentally different programming model than "write a Node.js background job." This is the right architecture for a Workers-native rewrite, not for a team that wants Next.js + Postgres + a standard job queue shipped fast. Revisit only if the team commits to TanStack Start + Workers end-to-end.

**Plain AWS:** skip entirely at this stage — EC2/ECS/Lambda-direct means the team owns networking, IAM, autoscaling, and CI/CD wiring that Railway/Fly/Render give for free. Revisit only past several thousand customers when infra cost optimization outweighs engineering time cost.

**Cost estimate (compute + hosting only, excl. DB):**
- 0 customers: $0–5/mo (Railway Hobby or Fly free-tier-adjacent usage)
- 50 customers: $20–60/mo (Railway Pro base + worker usage, or Fly with a couple of always-on machines)
- 500 customers: $150–500/mo depending on sync frequency and worker concurrency — this is the line item most sensitive to how often nightly syncs and optimization loops run per ad account.

Sources: [Render vs Railway vs Fly.io: 2026 Pricing Showdown](https://expresstech.io/render-vs-railway-vs-fly-io-2026-pricing-showdown/), [Railway vs Render vs Fly.io for Solo Developers in 2026](https://devtoolpicks.com/blog/railway-vs-render-vs-fly-io-solo-developers-2026), [Vercel Pricing (2026): The $20 Plan Is Only the Floor](https://omidsaffari.com/blog/vercel-pricing), [Cloudflare Workers Pricing 2026](https://developers.cloudflare.com/workers/platform/pricing/)

---

## 3. Database + ORM

**Primary DB: Neon.** Post-Databricks-acquisition pricing cuts (storage $1.75 → $0.35/GB-month, compute ~25% cheaper) plus scale-to-zero make it the cheapest standalone Postgres for a product with uneven traffic (most service-business ad accounts get checked once a day, not continuously). Instant branching is also genuinely useful for a solo founder testing schema migrations against production-shaped data without touching prod.

**Runner-up: Supabase.** If the team wants auth, storage, and realtime bundled with the database (reducing the number of vendors to manage), Supabase Pro at $25/mo (8GB DB, 100GB storage, 5GB egress, 100K MAU) is a reasonable bundle — but this brief already calls for Better Auth (not Supabase Auth, for OAuth-token-storage flexibility — see Auth section) and a dedicated object store, so Supabase's bundling advantage is partially wasted here. Choose Supabase over Neon only if the team wants Supabase Storage for creative assets too, collapsing two vendors into one.

**Skip:** RDS (too much ops overhead for a solo founder at this stage — no branching, manual scaling, more expensive at low volume), Railway Postgres (fine as a bundled convenience if hosting on Railway, but lacks Neon's branching and scale-to-zero).

**ORM Primary: Drizzle.** SQL-like control, ~7.4KB bundle, and — critically for this product's Meta/Google Ads OAuth token storage and time-series metrics tables — a query API that maps directly to the SQL it generates, which matters when hand-tuning materialized-view refresh queries and encrypted-column access patterns later. Drizzle Kit's `push` command is convenient for the early rapid-iteration phase.

**Runner-up: Prisma 7.** As of Prisma 7 (November 2025), the Rust query engine was replaced with a TypeScript/WASM implementation, removing the native binary and most of the old serverless cold-start/bundle-size penalty — so the historical "don't use Prisma on serverless" advice is now mostly stale. Prisma's batteries-included migration flow (`migrate` + `generate`) is genuinely faster to start with than Drizzle for a team that hasn't hand-written SQL migrations before. If the team is more comfortable with an ORM-first mental model than raw SQL, Prisma 7 is a legitimate choice with less of the historical downside.

**Edge compatibility:** both work fine on Vercel Edge/Cloudflare Workers now; Drizzle remains the lighter option if the web tier ever moves edge-native.

**Cost estimate (Postgres only, Neon):**
- 0 customers: $0 (free tier: 0.5GB storage, generous compute hours, scale-to-zero)
- 50 customers: $19–69/mo (Neon Launch/Scale tier depending on storage — ad-metrics tables grow fast even at 50 accounts)
- 500 customers: $200–700/mo (this is where the "plain Postgres for time-series" decision below starts to matter — see Section 6)

Sources: [Neon vs Supabase 2026: $1B Deal, Scale-to-Zero](https://tech-insider.org/neon-vs-supabase-2026/), [Supabase vs Neon Pricing Comparison (2026)](https://makerkit.dev/pricing-calculator/supabase-vs-neon), [Drizzle vs Prisma in 2026 - Which TypeScript ORM Should You Choose – Encore](https://encore.dev/articles/drizzle-vs-prisma), [Drizzle ORM vs Prisma in 2026: The Honest Comparison](https://dev.to/pockit_tools/drizzle-orm-vs-prisma-in-2026-the-honest-comparison-nobody-is-making-3n6g)

---

## 4. Background jobs — the most critical infra decision for this product

This product needs: nightly metric syncs (fan-out per connected ad account), optimization loops (scheduled + potentially triggered), webhook ingestion (Meta/Google webhook events), all with retries and idempotency. Compared side by side:

| | Inngest | Trigger.dev | Temporal | BullMQ + Redis | Cloudflare Queues | pg-boss |
|---|---|---|---|---|---|---|
| DX | Very high — functions as event handlers, step-based durability, no infra to run | Very high — similar model, open source, self-hostable free | High but steep — you design workflows explicitly, own the worker fleet | Medium — you write the queue/worker wiring yourself | Medium — Workers-native, ties you to CF compute | Medium — thin wrapper over Postgres SKIP LOCKED |
| Pricing @ low volume | Free: 50K runs/mo, 1K steps/run | Free: ~1,500 runs/mo, 5 concurrent | No free production tier; $100/mo + worker fleet cost | Free (self-hosted); pay only for Redis (Upstash ~$0–10/mo) | $5/mo base (Workers), queues billed separately | Free (self-hosted); pay only for Postgres you already have |
| Durability / retries | Built-in step-level durability, automatic retries per step | Built-in, same category as Inngest | Best-in-class — designed for exactly this | Manual — you configure retry/backoff yourself | Built-in retry logic, "unlimited CPU time" per Cloudflare | ACID via Postgres transactions; manual retry config |
| Long-running workflow support | Yes — steps can span arbitrary wall-clock time (waits, sleeps) | Yes — same category | Yes — this is Temporal's whole reason to exist | Weak — BullMQ is a queue, not a workflow engine; long workflows need hand-rolled state | Workflows product exists (Cloudflare Workflows) but young | Weak — same limitation as BullMQ, it's a job queue not orchestrator |
| Local dev | Good — local dev server with UI, replay | Good — local dev server with UI | Heavier — needs local Temporal server or dev namespace | Simple — just Redis locally | Harder — Workers local emulation (Miniflare) has rough edges | Trivial — it's just Postgres, already running |
| Infra to operate | None (hosted) | None (hosted) or self-host | You run and scale worker fleet yourself | You run and scale Redis + workers | You're already on Workers, or you're not | None — reuses existing Postgres |

**Primary: Inngest.** For a solo founder, Inngest's event-driven model maps naturally onto this product's actual jobs (`account.connected` → sync job; `nightly.tick` → fan-out sync per account; `optimization.triggered` → loop with waits). The free tier (50K function runs/month) comfortably covers dozens of customers' nightly syncs before any bill starts, and step-level durability means a failed Meta API call mid-sync doesn't require re-running the whole job — critical for idempotent metric syncs. No infrastructure to run is the deciding factor over BullMQ/Temporal for a one-person team.

**Runner-up: Trigger.dev.** Nearly identical value proposition to Inngest, cheaper at the very bottom of the pricing ladder (Hobby $20/mo vs Inngest Basic $30/mo) and fully open-source with a genuinely free unlimited self-host option — a real exit ramp if Inngest's pricing at scale becomes unattractive. Choose Trigger.dev over Inngest if self-hosting optionality matters more than a slightly more mature product; otherwise they're close enough that either is a safe pick.

**Why not BullMQ+Redis as primary:** it's the cheapest at massive scale (no per-run pricing) but it is a *queue*, not a durable-workflow engine — building retry/idempotency/multi-step-with-waits semantics on top of it is exactly the kind of infrastructure work a solo founder should not be doing in month one. Worth revisiting only if Inngest/Trigger.dev pricing becomes the dominant cost line at large scale (thousands of customers) and the team has grown enough to own the Redis ops burden.

**Why not Temporal:** best-in-class durability but no free production tier ($100/mo minimum) *plus* the team must run and scale its own worker fleet — this is solving for a scale and complexity this product doesn't have yet. Revisit if the "optimization loop" logic becomes a genuinely long-running, complex, multi-day stateful workflow with human-in-the-loop steps.

**Why not Cloudflare Queues as primary:** only makes sense if the whole stack is Workers-native (see Section 2's hosting note) — don't adopt it in isolation from that architectural choice.

**pg-boss** is worth a specific callout: if the team wants to minimize vendor count and is comfortable owning retry/idempotency logic by hand, pg-boss (Postgres `SKIP LOCKED`, no Redis) is a legitimate zero-additional-infra choice since Postgres is already running. It's a downgrade in DX versus Inngest/Trigger.dev but a real option for extreme cost minimization.

**Cost estimate:**
- 0 customers: $0 (Inngest free tier)
- 50 customers: $30–75/mo (Inngest Basic, or free tier if sync volume stays low)
- 500 customers: $300–1,000+/mo (Inngest Pro tier or above, scales with fan-out volume — this is the line item to watch most closely as ad-account count grows, since nightly syncs fan out per connected account)

Sources: [Inngest vs Trigger.dev: which background-job platform fits your SaaS?](https://www.promptstoproduct.com/inngest-vs-trigger-dev), [Inngest vs Trigger.dev vs BullMQ for Next.js 2026](https://www.buildmvpfast.com/blog/inngest-vs-trigger-dev-vs-bullmq-background-jobs-nextjs-2026), [Temporal Cloud vs Self-Hosted 2026: True Cost](https://automationatlas.io/guides/temporal-cloud-vs-self-hosted-2026/), [Inngest vs Temporal: Durable execution that developers love](https://www.inngest.com/compare-to-temporal), [BullMQ Alternatives for Webhook Retries](https://hookdeck.com/webhooks/platforms/bullmq-alternatives-for-webhook-retries), [BullMQ vs Bee-Queue vs pg-boss 2026 — PkgPulse](https://www.pkgpulse.com/guides/bullmq-vs-bee-queue-vs-pg-boss-job-queues-nodejs-2026)

---

## 5. Auth — org/workspace model + third-party OAuth token storage

**Primary: Better Auth (self-hosted, BYO database).** This is the one call worth explaining carefully because it's contentious.

- Better Auth's organization plugin generates schema and APIs for multi-tenant orgs, members, teams, roles, and invitations out of the box — covers the "org/workspace model with role-based access" requirement directly.
- It's free and open-source (bring your own Postgres, which the team already has via Neon) — no per-MAU billing, which matters because this product's OAuth-connection-heavy model (Meta + Google Ads tokens per customer) doesn't map cleanly onto "monthly active user" pricing anyway.
- Critically, Better Auth gives full schema control over the `account` table where third-party OAuth tokens (Meta, Google Ads) get stored — meaning the encrypted-token-at-rest pattern (Section 9) is straightforward to implement directly, versus fighting a hosted auth vendor's opaque token-storage model.
- The documented migration pattern in 2026 is "ship on Clerk to reach product-market fit, then move to Better Auth or Supabase Auth around the 50K-MAU mark when the bill starts catching engineering attention" — for a solo founder who wants to avoid that migration entirely, starting on Better Auth is the right call, at the cost of writing slightly more auth UI/glue code up front than Clerk would give for free.

**Runner-up: WorkOS AuthKit.** If the team anticipates needing enterprise SSO/SCIM for larger service-business customers (agencies with IT departments), WorkOS's free tier is unusually generous — 1 million MAU free, 100 monthly active organizations free — and its Admin Portal lets customer IT teams self-serve SSO setup without developer involvement. WorkOS is the better choice specifically if "sell to bigger agencies with SSO requirements" is on the roadmap; Enterprise SSO connections cost $125/mo each beyond the free tier, which only bites once actual enterprise customers exist to pay for it.

**Why not Clerk:** Clerk's DX is the best in class (which is why it's the default "ship fast" recommendation elsewhere), and its free tier is genuinely generous now (50,000 monthly retained users as of Feb 2026, up from 10K). But B2B/organizations auth is a $100/mo add-on, Administration is another $100/mo, and each Enterprise SSO connection is $75/mo — for a product whose core value prop *is* multi-tenant orgs with roles, that add-on cost is effectively mandatory from day one, not an at-scale problem. Given Better Auth covers the same org/roles ground for free with full control over OAuth token storage, Clerk's DX advantage doesn't outweigh paying for a feature the product needs immediately.

**Why not Auth.js (NextAuth):** weaker built-in organization/roles primitives than Better Auth — the team would be building the org model from scratch either way, so Better Auth's purpose-built organization plugin is strictly better for this specific requirement.

**Why not Supabase Auth:** reasonable if already committed to Supabase as the database, but this brief's Neon-primary recommendation and the need for full control over encrypted OAuth-token columns make Better Auth's flexibility the better fit.

**Cost estimate:**
- 0/50/500 customers: $0 across the board (self-hosted, no per-MAU billing) — unless/until enterprise SSO is sold, at which point either WorkOS's per-connection pricing kicks in or Better Auth's own SAML/SCIM support (built in) is used, still free.

Sources: [Better Auth vs Clerk vs NextAuth vs Supabase Auth: Which Authentication for Next.js SaaS in 2026](https://makerkit.dev/blog/tutorials/better-auth-vs-clerk), [WorkOS vs. BetterAuth vs. Clerk: Which should you choose? — WorkOS](https://workos.com/blog/workos-vs-betterauth-vs-clerk), [Clerk Pricing 2026: What You Actually Pay Per User](https://www.budgetforge.dev/tools/clerk-pricing-2026), [WorkOS Pricing Explained (2026): Free 1M Users & Per-Connection Costs](https://idsync.com/guides/workos-pricing)

---

## 6. Analytics / time-series storage for ad metrics

The core question is: at what scale does plain Postgres break for storing and querying spend/impressions/clicks/leads/cost-per-lead time series?

**Primary: Plain Postgres + materialized views, with a defined migration trigger.** For a solo founder at 0–500 customers with, say, a handful of ad accounts per customer and daily-granularity metrics, raw row counts stay in the low tens of millions — well within what Postgres handles fine with proper indexing (composite index on `account_id, date`) and daily-refreshed materialized views for dashboard aggregates. This avoids standing up a second database system before it's needed.

**Where it breaks:** materialized views recompute the *entire* query on every refresh — a view over 100 million rows takes the same time to refresh whether 10 rows or 10 million rows changed since the last refresh. One documented case: materialized views worked well to ~31 million rows, then required migrating to regular tables with nightly refresh logic as maintenance windows grew (30 seconds at 10M rows → 5 minutes at 100M rows). For this product, that threshold is realistically reached somewhere in the "many hundreds of customers with hourly-granularity metrics across multiple platforms" range — plan the migration trigger around **row count crossing ~20–50 million** or **refresh time exceeding your acceptable dashboard-staleness window**, not around customer count directly.

**Migration path when that trigger hits: ClickHouse Cloud or Tinybird.** Both are purpose-built for exactly this workload (high-cardinality time-series aggregation for dashboards).
- **ClickHouse Cloud**: $0.22–0.39/compute-unit-hour + $25.30/TB-month storage; production clusters run $200–100K+/mo depending on scale — more control, steeper ops learning curve, better if the team wants to also self-host or move providers later.
- **Tinybird**: managed ClickHouse with ingestion + storage + API requests bundled into one plan, free tier with no time limit (10GB storage, unlimited processing, 1,000 API requests/day) — better developer experience for a solo founder who wants "give it events, get a dashboard API" without operating ClickHouse directly.

**Runner-up: Timescale (Tiger Data).** A Postgres extension rather than a separate system — meaningfully lower migration cost than ClickHouse/Tinybird since it's still Postgres underneath (same ORM, same connection pool, same backup tooling), with purpose-built time-series compression and continuous aggregates that solve the materialized-view refresh problem natively. Worth strongly considering *instead of* the "plain Postgres → ClickHouse" two-stage plan above if the team wants to avoid a second query language (ClickHouse SQL has real differences from Postgres SQL) — Timescale is a lower-friction upgrade path from plain Postgres because it's the same database.

**Recommendation for this product specifically:** start on plain Postgres + materialized views (zero new infra, ships fastest). If/when refresh times or query latency become a problem — realistically past a few hundred customers with multi-platform hourly metrics — migrate to **Timescale** first (lowest-friction, stays in the Postgres ecosystem) and only reach for ClickHouse/Tinybird if Timescale's compression and continuous aggregates don't keep up at your specific cardinality (which is unlikely before thousands of customers).

**Cost estimate:**
- 0 customers: $0 (Postgres you're already running)
- 50 customers: $0–25/mo (still fits in Neon's included compute/storage, maybe a small bump in DB tier)
- 500 customers: $200–800/mo — either a larger Postgres/Timescale instance, or if migrated, ClickHouse Cloud/Tinybird at moderate scale

Sources: [PostgreSQL Materialized Views: From Manual Refresh to Real-Time](https://risingwave.com/blog/postgresql-materialized-views-real-time/), [How I Optimised PostgreSQL Materialized Views Serving 31 Million Rows](https://kuldeepkr16.medium.com/how-i-optimised-postgresql-materialized-views-serving-31-million-rows-81e23b5d1af8), [Tinybird vs ClickHouse Cloud cost comparison explained](https://www.tinybird.co/blog/tinybird-vs-clickhouse-cloud-cost-comparison), [ClickHouse vs TimescaleDB: Best for real-time analytics](https://www.tinybird.co/blog/clickhouse-vs-timescaledb)

---

## 7. UI: shadcn/ui + Tailwind v4 + charting

**Primary: shadcn/ui + Tailwind v4 (unambiguous default).** Both are the default SaaS UI stack in 2026 — every popular boilerplate (ShipFast, Supastarter, MakerKit, Bedrock, next-forge) ships with them. Tailwind v4 moved config from `tailwind.config.js` to CSS (`@theme` directive), switched to OKLCH colors, and the build engine is 3.5x faster for full builds — no reason to consider anything else for a solo founder who wants copy-paste components rather than a component library dependency.

**Charting — Primary: Tremor.** Tremor was acquired by Vercel; all Tremor products (including the previously-paid Tremor Blocks — 300+ prebuilt sections) are now free and open source, and its cofounders now work on Vercel's design-engineering team. Tremor is purpose-built for exactly this product's need — pre-styled chart components that match shadcn/ui's aesthetic out of the box (spend/impressions/CPL charts, KPI tiles), minimal customization needed to look production-ready fast. It is actively maintained and thriving, not a legacy/abandoned project — a legitimate concern to check given it changed hands, but the acquisition strengthened rather than weakened its status.

**Runner-up: Recharts (v3).** The lower-level default for React charting — 2.4M weekly downloads, SVG-based, composable. Reach for Recharts directly (or drop down to it from Tremor) when a specific chart needs behavior Tremor's higher-level API doesn't expose — custom animations, unusual axis configurations, mixed chart types on one canvas.

**Not recommended:** visx (lower-level, more setup work than this product needs) or ECharts (heavier, more suited to data-dense internal tools than a clean customer-facing dashboard).

**Cost:** $0 at every scale — all open source, no hosted-service billing.

Sources: [The State of Shadcn UI in 2026: Ecosystem, Tools, and Trends](https://blocks.serp.co/blog/state-of-shadcn-ui-2026), [Vercel acquires Tremor to invest in open source React components](https://vercel.com/blog/vercel-acquires-tremor), [Recharts v3 vs Tremor vs Nivo: React Charts 2026 — PkgPulse](https://www.pkgpulse.com/guides/recharts-v3-vs-tremor-vs-nivo-react-charting-2026)

---

## 8. LLM integration: Anthropic Claude API

**Model selection, per skill/live pricing check (Claude API, first-party rates as of August 2026):**

| Model | ID | Input $/MTok | Output $/MTok | Context | Notes |
|---|---|---|---|---|---|
| Claude Haiku 4.5 | `claude-haiku-4-5` | $1.00 | $5.00 | 200K | Fast/cheap — good for simple ad-copy variants, classification |
| Claude Sonnet 5 | `claude-sonnet-5` | $3.00 ($2.00 intro through 2026-08-31) | $15.00 ($10.00 intro) | 1M | **Default for this product** — best speed/intelligence balance, near-Opus quality on structured generation tasks |
| Claude Opus 5 | `claude-opus-5` | $5.00 | $25.00 | 1M | Reserve for the hardest creative-strategy work (e.g. full campaign strategy generation, complex multi-account optimization reasoning) |
| Claude Fable 5 | `claude-fable-5` | $10.00 | $50.00 | 1M | Most capable widely-released model — overkill for ad copy/creative generation at this product's stage; not recommended as default |

**Recommendation: default to Claude Sonnet 5 for ad copy and creative-brief generation**, with an escalation path to Claude Opus 5 for higher-stakes generation (e.g., a "generate full campaign strategy" feature) where quality matters more than per-call cost. This mirrors Anthropic's own guidance to reserve the most capable tier for demanding reasoning, not routine generation.

**Structured outputs:** use `output_config.format` (JSON schema) rather than free-text parsing for ad-copy generation — guarantees valid, parseable output for headline/description/CTA fields without prompt-engineering a JSON-only instruction. Supported on Sonnet 5, Opus 5, Haiku 4.5, and Fable 5.

**Cost control levers, in order of impact for this product:**
1. **Prompt caching** — cache the system prompt (brand voice guidelines, ad-platform constraints, few-shot examples of good copy) across generation calls; cached reads cost ~90% less than uncached input. Minimum cacheable prefix is 512 tokens on Opus 5, 1024 on Sonnet 5 — a well-built system prompt for ad-copy generation easily clears that.
2. **Batch API** — for non-interactive generation (e.g., overnight bulk regeneration of underperforming ad variants), batch processing is 50% cheaper; combine with caching for up to ~95% total savings versus uncached synchronous calls.
3. **Model tiering** — Haiku 4.5 for cheap/fast tasks (classifying ad performance, simple variant tweaks), Sonnet 5 for the default generation path, Opus 5 only behind an explicit "generate strategic plan" feature.

**Guardrails:** track per-customer and per-org token spend (store `usage.input_tokens`/`output_tokens` from every response against the org, surface a soft cap in billing metadata) since this is a usage-sensitive cost center that scales with customer count and how aggressively customers regenerate creative. Use `strict: true` on tool definitions and `output_config.format` for anything that must parse — malformed generation output is a support-ticket generator, not just a cost problem.

**Cost estimate (LLM spend, highly dependent on generation volume per customer):**
- 0 customers: $0
- 50 customers: $20–100/mo (light ad-copy generation volume, mostly Sonnet 5 with caching)
- 500 customers: $300–1,500/mo — wide range because this scales directly with how many ad variants per account per week customers generate; model this against your actual expected generation frequency once you have usage data, and revisit caching/batching aggressively if this becomes the dominant line item.

Sources: claude-api skill (live-cached model/pricing table, verified current as of 2026-06-24 cache with August 2026 pricing confirmed), [Claude Pricing 2026: Every Model, Every Tier, Full Breakdown](https://coursiv.io/blog/claude-pricing-2026), [Anthropic API Pricing in 2026: Complete Guide](https://www.finout.io/blog/anthropic-api-pricing)

---

## 9. Other critical infrastructure

**Error monitoring — Primary: Sentry.** Free Developer tier (5,000 errors/mo, 1 user) covers a solo founder through early customers; Team plan is $26/mo once a second team member joins or volume grows past the free tier. Usage-based overage ($0.000290/event) is the main risk — a bad third-party API failure (e.g., Meta API returning errors in a retry loop) can spike a bill quickly, so pair with sane retry/backoff limits in the background-job layer (Inngest's built-in retry caps help here directly).

**Product analytics + feature flags — Primary: PostHog.** Genuinely comprehensive free tier (1M analytics events, 5,000 session replays, 1M feature-flag requests/month, no time limit) covers product analytics, feature flags, experiments, surveys, and session replay in one tool — collapsing what would otherwise be 2-3 separate vendors (analytics + flags + replay) into one for a solo founder. Feature-flag pricing beyond the free tier is usage-based and cheap ($0.0001/request at low volume, dropping further with step-down discounts).

**Secret management — Primary: Doppler.** Free for up to 3 users (covers a solo founder or tiny team), $8/user/mo beyond that; seat-based pricing (not per-machine-identity) is simpler to reason about than Infisical's per-identity model for a small team with few machine credentials. Doppler is managed-only (not self-hostable), which is fine at this stage — self-hosting is a distraction, not a requirement.

**Runner-up on secrets: Infisical.** Open-source and self-hostable if the team wants to avoid a third-party secrets vendor entirely; per-identity pricing ($18/mo/identity on Pro as of mid-2026) can work out cheaper or more expensive than Doppler depending on human-to-machine-credential ratio — worth comparing directly once the number of service accounts (Meta API app, Google Ads API app, Stripe, Anthropic API key, etc.) is known.

**Encryption of third-party OAuth tokens at rest — this is a hard requirement, not optional.** Meta and Google Ads access/refresh tokens are the crown jewels of this product (they grant ad-spend authority on customer accounts) and must never sit in plaintext in Postgres. Recommended pattern for 2026:
- **Envelope encryption**: encrypt each token with a per-record Data Encryption Key (DEK), then wrap that DEK with a Key Encryption Key (KEK) held in a KMS (AWS KMS, or a managed secrets service) — not with a static application-level key baked into an env var.
- Store encrypted token columns as `BYTEA` in Postgres if using `pgcrypto`-style column encryption, or handle encryption/decryption at the application layer with a library like `libsodium`/`node:crypto` (AES-256-GCM with a nonce prepended to ciphertext) before the value ever touches the ORM.
- Keep the KMS/KEK **separate from both the app server and the database** — if either is compromised, the encryption keys aren't sitting next to the ciphertext.
- Rotate the KEK on a fixed schedule; re-encrypting existing DEKs on rotation is far cheaper than re-encrypting every token directly.

**Token lifecycle specifics that affect the background-job design:**
- **Meta Marketing API**: short-lived tokens (~1–2 hours) exchange for long-lived tokens (~60 days) via a server-side call with the app secret. For production automation, use **System User tokens** created in Business Manager — these don't expire on a timer (only on manual revocation or refresh), which is the right pattern for a background sync job rather than juggling 60-day token refresh windows per customer.
- **Google Ads API**: OAuth refresh tokens plus a developer token (obtained via a Google Ads manager account) are both required for every call. As of August 5, 2026, **new** OAuth refresh tokens require passkey-based sign-in during the consent flow (password + 2FA/TOTP alone is no longer sufficient) — existing tokens are unaffected, but the customer-facing OAuth-connect UI needs to account for this when a customer connects (or reconnects) their Google Ads account. Service-account flows are exempt from the passkey requirement but Google's guidance is that service accounts are meant for automated/offline access patterns, which may or may not map cleanly onto "connect my personal Google Ads account" — validate this against the actual OAuth consent screen flow before shipping.
- Both platforms' token-refresh logic belongs in the background-job layer (Inngest) as a scheduled, idempotent job per connected account — not something triggered ad hoc from request handlers.

**File/image storage for creative assets:** not deeply researched in this pass, but the standard 2026 pattern is **Cloudflare R2** (S3-compatible, zero egress fees — relevant since ad creatives get served/previewed frequently) or Supabase Storage if already on Supabase. Given the Neon-primary recommendation above, R2 is the natural pairing.

**Transactional email + notifications:** not deeply researched in this pass; **Resend** is the current default for a Next.js-adjacent stack (good DX, reasonable free tier, React Email templates) and pairs naturally with the rest of this stack — worth a dedicated research pass if email deliverability becomes a priority (billing receipts, sync-failure alerts, weekly performance digests).

**Cost estimate (Sentry + PostHog + Doppler combined):**
- 0 customers: $0 (all free tiers)
- 50 customers: $26–60/mo (Sentry Team tier likely triggers first)
- 500 customers: $150–400/mo (Sentry usage overage + PostHog usage beyond free tier + Doppler seats)

Sources: [Sentry Pricing 2026: Plans, Costs & How to Reduce Your Bill](https://last9.io/blog/sentry-pricing/), [PostHog Pricing Guide 2026](https://flexprice.io/blog/posthog-pricing-guide), [Doppler vs Infisical: Secrets management solutions](https://www.doppler.com/doppler-vs-infisical), [Refresh Token Security: Best Practices for OAuth Token Protection](https://www.obsidiansecurity.com/blog/refresh-token-security-best-practices), [Long-Lived Access Tokens - Meta for Developers](https://developers.facebook.com/documentation/facebook-login/guides/access-tokens/get-long-lived), [Google Ads API Requires Passkeys From 5 August](https://www.relevantaudience.com/google-ads-en/google-ads-api-passkey-requirement/)

---

## Full recommended stack at a glance

```
Framework:        Next.js (App Router)
Hosting:          Railway (app + workers), or Vercel (web) + Railway/Fly (workers)
Database:         Neon (Postgres)
ORM:              Drizzle
Background jobs:  Inngest
Auth:             Better Auth (self-hosted, org plugin, encrypted OAuth token columns)
Time-series:      Postgres + materialized views → Timescale if/when refresh times break
UI:               shadcn/ui + Tailwind v4 + Tremor (charts)
LLM:              Claude Sonnet 5 default, Claude Opus 5 for high-stakes generation
Monitoring:       Sentry (errors) + PostHog (product analytics + feature flags)
Secrets:          Doppler
File storage:     Cloudflare R2
Email:            Resend (not deeply researched — verify before committing)
```

This stack minimizes vendor count, keeps everything at or near $0/month pre-launch, avoids Redis as an operational dependency (Inngest is hosted, no self-managed queue infra), and defers the one genuinely hard infrastructure decision (time-series storage at scale) behind a clear, measurable trigger rather than over-engineering for scale the product doesn't have yet.
