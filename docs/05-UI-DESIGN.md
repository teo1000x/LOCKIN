# UI & Design System

Reference: **pacerev.com** (captured 2026-08-19). Take the design language and the
information architecture; do not copy the copy.

## Design language observed

**Palette**
- Background: pure white, with a very faint grid pattern behind the hero
- Text: near-black `#0F172A` for headings, mid-grey `#4B5563` for body
- Primary: strong blue `#2563EB`, hover `#1D4ED8`
- Accents: pale blue pill badges, green dot for "active/optimizing" status

**Typography**
- Headings: heavy weight, tight tracking, large. Geist or Inter at 700–800.
- Body: regular weight, generous line-height, grey. Never bold body copy.

**Components**
- Pill badge with a leading dot for status and eyebrow text
- Solid rounded-lg primary button + outline secondary, side by side
- Product screenshot framed in browser chrome (three dots + fake URL bar)
- Stat tile: tiny uppercase label → very large number → small delta line
- Generous whitespace. When in doubt, add more.

**Voice**
- Two-clause outcome contrast: _"PaceRev runs your Facebook ads. You book the jobs."_
- Objection handling as a quiet row under the CTA: _"No agency retainers · No wasted ad
  spend · No website needed"_
- Never feature-speak. Always outcome-speak.

## The dashboard — steal this information architecture

```
Main Street Co.                              ● Optimizing
Austin, TX metro

┌──────────────────┬──────────────────┬──────────────────┐
│ LEADS THIS MONTH │ BOOKED CUSTOMERS │ COST PER LEAD    │
│       47         │       16         │      ↓31%        │
│  +14 this week   │   this month     │   this month     │
└──────────────────┴──────────────────┴──────────────────┘

What we did this week
  ✓ Built and launched 5 fresh ads for you
  ✓ Scaled your 2 best ads, +30% budget
  ✓ Your top ad booked 18 leads this week
```

Three principles this encodes, all of which match the research:

1. **Three numbers, not thirty.** Leads, booked customers, cost per lead. Nothing else on the
   primary screen. No CTR, no CPM, no ROAS, no impressions.
2. **A plain-English activity feed.** The owner needs to see the software working, in
   sentences they'd use themselves. This single component is most of the perceived value and
   most of the retention — an owner who can see what happened this week does not churn.
3. **"Booked customers" is the key metric** — and it can only come from the owner. Which
   gives us the cheapest possible version of the revenue loop.

## The lead inbox is the highest-leverage screen

Every lead arrives with one question attached: **did this become a job?**

```
Sarah M. · (512) 555-0142 · A/C not cooling · 4 min ago
   [ Booked ]  [ Not a fit ]  [ No answer ]  [ Spam ]
   ┌ Booked? → job value $______
```

Two taps from the owner. In exchange we get:

- The "booked customers" number that makes the dashboard meaningful
- Lead-quality labels — which ad, which audience, which offer produced *real jobs* versus junk
- Later: exactly the dataset needed to push offline conversions back to Meta, so Meta's own
  optimization targets booked revenue instead of cheap clicks

This is the closed revenue loop from the research, obtained without a single CRM integration.
Build the inbox early. It looks like a small feature and it is the whole moat.

## Screens for v1

1. **Marketing site** — hero, how it works, pricing, book a call
2. **Sign up / log in**
3. **Intake wizard** — one question per screen, progress bar, all state saved as you go
4. **Connect Meta** — Page + ad account, with a clear plain-English permissions explanation
5. **Campaign review / approval** — real Facebook-style ad previews, edit / regenerate / reject
6. **Dashboard** — three stat tiles + activity feed
7. **Lead inbox** — the tagger above
8. **Settings** — billing, team, disconnect and export

## Non-negotiable UI rules

- Never show a metric the owner wouldn't say out loud to a friend
- Every AI decision gets a one-sentence plain-English "why", inline
- Every destructive or spending action is reversible and clearly labelled
- Wizard state persists on every keystroke — owners fill these out on phones, between jobs
- Mobile-first for the dashboard and lead inbox; desktop-first is acceptable for the wizard
