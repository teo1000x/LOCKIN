# What I Need From You

You've never launched a SaaS, so here is the honest division of labour. I can write all the
code. There are four categories of things I **cannot** do for you, and three of them are on
the critical path.

---

## 1. Legal & identity — start this week, it gates everything

None of this is optional, and Meta's Business Verification will not pass without it. It is
also the slowest thing in the entire project, so it starts before any product decision.

- [ ] **Register a business entity** (LLC is typical). Cost: $50–500 depending on state.
- [ ] **Get an EIN** from the IRS — free, takes minutes online.
- [ ] **Buy the domain.** Must match the business name.
- [ ] **Business bank account** — Stripe payouts need it.

> **Critical detail that causes most verification failures:** the business name, address, and
> domain must match *character for character* across your incorporation documents, your Meta
> Business Manager profile, and your domain registration. A mismatch here costs weeks.

**What I need from you:** the legal business name, address, and domain once they exist.

---

## 2. Accounts to create

Create these yourself and put the keys in `.env.local` — **do not paste secrets into chat.**
I'll write `.env.example` listing exactly which variable each key goes into.

| Service | Purpose | Cost to start | Priority |
|---|---|---|---|
| **GitHub** | Source of truth; Vercel deploys from it | Free | Now |
| **Vercel** | Hosting | Free | Now |
| **Neon** or **Supabase** | Postgres database | Free | Now |
| **Anthropic Console** | Claude API for ad generation | Pay per use, ~$20 to start | Now |
| **Meta Developer + Business Manager** | The ad platform | Free | Now — verification is slow |
| **Stripe** | Subscriptions | Free until you charge | Week 2 |
| **Resend** | Transactional email | Free tier | Week 2 |
| **fal.ai** | AI image generation | ~$10 credit | Week 3 |
| **Twilio** | Lead alert SMS | ~$20 + A2P registration | Week 3 — own slow approval |
| **Sentry / PostHog** | Errors and funnel analytics | Free tier | Week 4 |

> That "one other thing you were recommended" is almost certainly **Supabase** — the usual
> phrase is "Vercel + Supabase." It's a fine choice: Postgres, auth, storage, and file
> uploads in one. My spec calls for Neon + Better Auth for tighter control over the encrypted
> token table, but **if you'd rather have fewer vendors, Supabase is a legitimate swap** and I
> can build against either. Tell me which and I'll write it that way.

---

## 3. Decisions only you can make

- [ ] **The product name.** Everything currently says `Ignition`, a placeholder.
- [ ] **Which trades ship first.** I need 3–5 to build the taxonomy and copy priors properly.
      The research ranks HVAC, plumbing, and roofing highest on budget, ticket value, and
      urgency. Your call — but "all of them" produces a generic product that wins nothing.
- [ ] **Price points.** My draft: $499 / $999 / $1,999. PaceRev sits at $699 / $1,499 / $2,499.
- [ ] **Free trial, paid pilot, or demo-then-buy?** This changes the entire signup flow.

---

## 4. Your ad playbook — this is the actual product

**This is the most important section on the page and the easiest one to skip.**

The software's only durable advantage is that it encodes what *you* know from running these
accounts. Without it, the generation pipeline is a generic LLM wrapper — which is precisely
what every dead competitor in the research shipped. I cannot get this anywhere else.

I need you to write down, roughly, in whatever form is easy:

**Offers**
- Which offers actually make the phone ring for each trade? Real examples.
  ("$89 tune-up" vs "Free estimate" vs "$50 off first service" — which wins, and where?)
- What offers look appealing but produce junk leads?

**Copy**
- 3–5 ads you've run that genuinely worked. Full text, verbatim. Bad ones too — I need
  contrast to build the priors.
- Hooks that work on local service audiences. Angles that consistently die.

**Targeting**
- Default radius by trade — how far will an HVAC tech actually drive versus a roofer?
- Age/gender defaults, if any. Which interest targeting is worth it now that Advantage+
  exists, and which is theatre?

**Budget**
- Realistic daily minimum for a campaign to learn.
- How long before results mean anything, and what you do at each checkpoint.

**Lead forms**
- Which qualifying questions filter out tire-kickers without tanking volume?
- How many fields before conversion falls off a cliff?

**Failure modes**
- The mistakes small businesses always make with their own ads.
- What gets ads rejected by Meta in these categories.

Voice notes are fine. Bullet points are fine. Do not polish it — I'll structure it. This is
what turns generated ads from plausible into effective, and it is the entire reason this
product could beat someone else's LLM wrapper.

---

## 5. Customers — the thing that actually kills solo founders

Not a build task, but it outranks every build task. The research found that no winner in this
category grew through a self-serve funnel.

- [ ] **Name 5 service business owners you can call this week.** Former clients, people in
      your network, anyone.
- [ ] Get 3 of them to look at the wizard and tell you what's wrong with it.
- [ ] Convert 2 into paid design partners at a discount, **before the software is finished.**
      You run their ads manually using the blueprints the software generates. That's revenue
      while Meta's queue runs, plus the real edge cases the automated version needs.

If you do nothing else on this list, do this one.

---

## What happens next, on my side

Once you've got GitHub + Vercel + a database + an Anthropic key, I can build and you can see
it running:

1. Database schema and migrations
2. Auth and organizations
3. The intake wizard
4. The AI campaign generation pipeline
5. The approval UI with real ad previews
6. The dashboard and lead inbox
7. Stripe billing
8. The Meta publish pipeline (last — it's the piece gated on approval)
