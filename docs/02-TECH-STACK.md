# Tech Stack — locked for v1

Derived from `research/03-tech-stack.md`, adjusted for this product's actual shape:
webhook ingestion, long-running generation jobs, encrypted third-party OAuth tokens,
and a solo founder on a short runway.

## Decision table

| Layer | Choice | Why this, not the alternative |
|---|---|---|
| Language | TypeScript (strict) | One language across app, jobs, and scripts |
| Framework | **Next.js 15+, App Router** | Server Actions suit wizard-and-approval flows; largest hiring/AI-assist surface |
| Hosting | **Railway** | Long-running containers. Vercel's function timeouts fight campaign generation and Meta sync |
| Database | **Neon Postgres** | Serverless PG, branching per PR, generous free tier |
| ORM | **Drizzle** | Owns its own schema — critical, since we hand-roll the encrypted token table |
| Jobs | **Inngest** | Durable multi-step workflows with retries + idempotency. BullMQ is a queue, not a workflow engine; Temporal is right at scale but costs $100/mo and a worker fleet on day one |
| Auth | **Better Auth** + organization plugin | Multi-tenant orgs free. Clerk charges $100/mo for orgs — mandatory from day one for a product whose core object *is* an org |
| UI | **Tailwind v4 + shadcn/ui** | Own the components; no vendor lock, best AI-assisted iteration |
| Charts | **Recharts** | Tremor's maintenance story is unreliable; Recharts is boring and stable |
| LLM | **Anthropic SDK — Claude Sonnet 5** default, **Opus 5** for campaign strategy | Structured outputs via tool-use for the blueprint schema |
| Images | **fal.ai** (Flux) | Fast, cheap per image, good at photoreal. Real customer job photos beat generation — treat this as fallback |
| Object storage | **Cloudflare R2** | Zero egress fees; creative assets get re-served constantly |
| Email | **Resend** | React Email templates, trivial setup |
| SMS | **Twilio** | Lead alerts. Register A2P 10DLC early — it has its own multi-week approval |
| Payments | **Stripe** | Billing Portal handles the "cancel anytime" promise without custom UI |
| Errors | **Sentry** | |
| Analytics | **PostHog** | Funnel visibility on the wizard, which is where activation will die |
| Secrets | Railway env vars → **Doppler** if it gets messy | |

## Estimated monthly cost

| | Pre-launch | 50 customers | 500 customers |
|---|---|---|---|
| Infra (host, DB, jobs, auth, storage) | $0–20 | $120–300 | $900–2,500 |
| LLM + image generation | $10–50 | $150–600 | $1,500–6,000 |
| Twilio / Resend | ~$5 | $30–80 | $300–800 |
| **Total** | **~$20–75** | **~$300–1,000** | **~$2,700–9,300** |

LLM and image spend is the widest-variance line. Meter generation per org from day one and
attach a hard credit ceiling per tier — otherwise one power user destroys the margin on a
$499/mo plan.

## Three things that are non-negotiable in the architecture

### 1. OAuth tokens get envelope encryption
Meta ad-account tokens are the crown jewels — a leak means an attacker spends real customer
money. Encrypt with a data key, wrap the data key with a KMS-held master key, and never store
the master alongside the ciphertext. Owning the Drizzle schema is precisely why Better Auth
beat Clerk here.

### 2. Prefer System User tokens over user tokens
Standard OAuth user tokens are long-lived for **~60 days**, then die. For a "set it and forget
it" product that means every customer's integration silently breaks around month two — a
churn machine disguised as a bug. Business Manager System User tokens can be issued
non-expiring and are the correct production pattern. Build a token-health monitor regardless,
with proactive re-auth prompts well before expiry.

### 3. Every Meta write is idempotent and rate-aware
Meta's Business Use Case limits: read = 1 point, write = 3. Limited Access caps at 60 points;
Full Access at 9,000. On top of that sits a **per-ad-account throttle scaled to trailing
spend** — so brand-new low-spend customers, which is all of them at first, have a very tight
ceiling no matter what tier our app holds. Every mutation carries an idempotency key and
flows through a per-ad-account rate limiter.

## Not chosen, and why

- **Supabase** — fine, but its auth pushes toward its own token model and we need schema control
- **Vercel** — excellent for the marketing site; function timeouts fight our workloads
- **Prisma** — heavier migrations, less schema control than Drizzle for our custom tables
- **ClickHouse / Timescale** — premature. Postgres with materialized views holds well past
  500 customers; migrate to Timescale when refresh time actually degrades, not before
