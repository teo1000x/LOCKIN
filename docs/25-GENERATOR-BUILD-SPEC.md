# The Generator Build: spec and checklist

_Written 20 August 2026 from the founder's brief. This is the file of record for the build:
what the customer experiences, what gets built, in what order, and who builds it. Nothing on
the checklist starts until the founder approves this document. Decisions the founder made in
chat are marked FOUNDER. Decisions the operator made and the founder can veto are marked
OPERATOR CALL._

Companion documents, all binding where they apply: `docs/22` (intake questions, superseded in
shape by the FOUNDER decision below but not in reasoning), `docs/19` (ad creative spec, the
renderer builds exactly this), `docs/17` (copy playbook), `docs/14` (policy lint rules),
`docs/08` (design system), `AGENTS.md` (inviolable rules 1 through 7).

---

## 1. The customer flow, end to end

1. **Landing page.** Prospect scrolls, sees pricing with credits per plan, picks a tier.
2. **Checkout.** Stripe Checkout for the chosen tier ($499 / $1,300 / $2,500 per month).
   Payment creates the account: organization provisioned by the Stripe webhook, owner signs
   in with the email they paid with (Better Auth, magic link first, password optional).
3. **First landing in the dashboard.** Sidebar: Home, New campaign, Campaigns, Leads,
   Results, Settings. Home shows the credits balance, a useful empty state, and one primary
   action: Start your first campaign.
4. **The intake flow.** FOUNDER: one flow, not a setup-plus-wizard split. Ten questions,
   one per screen, autosaved on every keystroke, skippable wherever a default exists
   (section 3). The landing page's "six questions" promise is replaced (section 7).
5. **Generation.** The pipeline (section 4) produces: the marketing plan, and 6 ready-to-post
   ad variants (composited image + primary text + headline), each with a plain-English
   reason for every decision. Progress is shown honestly; target under 90 seconds to first
   ad on screen.
6. **Review and approval.** The owner approves, edits, regenerates, or rejects each variant
   individually. Approval writes a content-hash record through `publish-guard.ts`. Editing
   an approved ad voids its approval by design. Inviolable rule 1; no bulk approve.
7. **Ship it.** Until Meta App Review clears (Track A): the export walkthrough, a live
   versioned web page with a Copy button on every value the owner types into Ads Manager.
   After A3 clears: connect the Meta ad account and publish approved ads, paused, into the
   owner's account. The flow ends at the same approval gate either way.
8. **Results.** Home fills with measured numbers once a connection exists (spend, leads,
   labelled measured) and self-reported ones the owner types (booked jobs, labelled
   reported by you). Never rendered side by side without labels. Inviolable rule 3.

## 2. Credits and metering

FOUNDER: Starter 400 credits / month, Growth 1,600, Max 4,000.

OPERATOR CALL, the unit: credits price actions, and every action's true API cost is recorded
against the org (inviolable rule 6). Action prices:

| Action | Credits |
|---|---|
| Full campaign build (plan + 6 ad variants) | 100 |
| One new ad variant (image + copy) | 10 |
| Regenerate copy only on a variant | 2 |
| Regenerate image only on a variant | 5 |
| Refresh competitor read (post-v1, when B4 ships) | 20 |

So Starter is 4 full campaigns a month or 1 campaign plus roughly 30 fresh variants.
Pricing page shows the credit number plus one plain-English line per tier, for example:
"400 credits a month. Enough for 4 full campaigns, rebuilt monthly." Credits reset monthly,
do not roll over, and the balance is always visible in the dashboard. Hard stop at zero with
a plain sentence, never a surprise overage charge.

Enforcement is server-side in the metering module (operator-written): a ledger table with
one row per action, action type, credit cost, real cost in dollars, org id, timestamp. The
generation pipeline refuses to start any action the balance cannot cover.

## 3. The intake flow, ten screens

FOUNDER: one flow. Order preserves the docs/22 logic: frictionless first, money in the
middle, trust last. One question per screen, visible progress, back always available,
16px inputs minimum, autosave per keystroke. Only Q1 and Q2 block progress; everything else
has a skip or a default.

| # | Question | Notes |
|---|---|---|
| 1 | What kind of work do you do? | Autocomplete over the 96-trade taxonomy, alias matcher, category fallback stated in plain words. Never a 96-item dropdown. |
| 2 | What is your business called? | Business name, plus optional logo upload (PNG/SVG; low-res uploads rejected with a plain reason, wordmark fallback per docs/19 4.4). |
| 3 | Where do you work, and how far will your crew drive? | City or postcode + radius slider, default derived per trade. |
| 4 | What is one job worth to you, on average? | Dollar figure. The derived daily budget appears immediately with the arithmetic shown, editable. OPERATOR CALL: budget is derived, never asked cold (docs/22 Q3 reasoning; consistent with /estimate). |
| 5 | What is the one deal you want new customers to see? | Trade-specific offer library from `dominantOffer`, or write your own. One offer, not a list. |
| 6 | What makes you the one to call, in your own words? | Free text, trade-specific prompts to break the blank page. The only input a competitor cannot copy. |
| 7 | What can you honestly claim? | Fixed checklist: licensed (number + state), insured, bonded, background-checked, years in business, real review count. Only claimed items ever render (docs/19 COMP-08). Nothing is invented. |
| 8 | Got photos of real jobs? | Upload up to 6, or skip. Real photos beat generated every time and the screen says so. A matched before/after pair unlocks the split template (T1). FOUNDER: photos live in the flow, not deferred. |
| 9 | What should we never say about your business? | Optional, examples shown. Negative constraint on every generation. |
| 10 | Where should leads go? | Phone and email for lead alerts and the lead form. Prefilled from the account where possible. |

## 4. The generation pipeline

Stages, in order. Stages 2, 5, 6 and the metering wrapper are operator-written; the rest is
agent work reviewed by the operator.

1. **Blueprint.** Claude (tool-use, Zod schema) turns intake into a structured campaign:
   plan, offer framing, 6 variant briefs (template, headline, primary text, trust items,
   medallion content), each field carrying its plain-English reason. Template selection
   respects the docs/19 category matrix; T1 only if a matched photo pair exists; fitness
   never gets T1 (COMP-06). Owner text enters prompts as data, delimited and instructed as
   untrusted (inviolable rule 4).
2. **Policy lint.** docs/14 rules on every string, including the strings headed into pixels
   (COMP-01), credit/financing signals (COMP-07/SAC-CRED-01), urgency and claim structure.
   Failures regenerate with the violation fed back; the owner never sees a linted-out ad.
3. **Photo bed.** Owner photo (cropped to spec) or generated via fal.ai using the docs/19
   section 5 eight-part prompt with the mandatory no-text exclusion clause. Generated
   images are always labelled as generated. Generation is metered; compositing is free.
4. **Composite.** Deterministic renderer draws the six zones per docs/19: zone geometry,
   character budgets, contrast floors with worst-sample checking, trust-row degradation,
   logo fitting, wordmark fallback. Same inputs, same bytes, always (docs/19 7.5).
5. **Persist and hash.** Ads stored with a content hash covering copy fields AND the
   rendered image bytes (COMP-05), so the approval gate covers what the owner actually saw.
6. **Approval workspace.** Real records through `publish-decision.ts` / `publish-guard.ts`
   against the real database. Per-variant approve / edit / regenerate / reject. Edit voids
   approval. The existing 10 tests stay green and new integration tests cover the wiring.
7. **Export walkthrough** (interim terminal step): versioned web page, Copy buttons, the
   AI-disclosure line item always present (IMG-AI-DISCLOSURE-01).

## 5. Dashboard

Sidebar IA as in the deployed mock: Home, New campaign, Campaigns, Leads, Results, Settings.
Home before any data: credits balance, the one primary action, and honest empty states;
no fake numbers anywhere (inviolable rule 3; `mock.ts` never renders for a real org).
Campaigns lists campaigns with per-variant approval state. Settings: business details,
logo, photos, credentials, plan and credits, billing portal link.

## 6. Auth, billing, data

- Better Auth with organizations (one org per business; schema already has the tables).
- Stripe: three subscription prices, Checkout, webhook provisions the org and sets the
  monthly credit allowance, billing portal for card changes and cancellation. Media spend
  never touches our Stripe (docs/03 billing structure).
- Drizzle migrations, committed and reviewed. All new tables added by migration, no schema
  rewrites of settled tables.
- Secrets in env only. No token or key is ever logged.

## 7. Site fixes shipping with this build (FOUNDER, from review of the live page)

1. **No pill shapes anywhere.** Every `rounded-full` on buttons, chips, and badges becomes
   the squared scale: radius-md 10px for interactive elements, radius-sm 6px for tags and
   badges. This includes the trade chips and the elements inside the step-1 dashboard mock.
   `docs/08` 3.B is amended: the radius-full status-badge exception is deleted (the 4px
   progress bar keeps rounded ends; it is not a button or badge).
2. **The percent glyph.** Product figures render in the mono face; its % reads wrong.
   Figures stay mono, the % symbol renders in the UI sans. Applied wherever a percent
   appears, starting with the dashboard mock's cost-per-lead stat.
3. **Pricing shows credits.** 400 / 1,600 / 4,000 per tier plus the plain-English line from
   section 2.
4. **The "six questions" promise is replaced.** New claim: "Ten questions. About three
   minutes." The two-minute copy goes wherever it appears; the claim must match the built
   flow, and the wizard gets timed against it before launch (docs/22 section 3 discipline,
   updated numbers).

## 8. Explicitly not in v1

- The competitive read (B4: directory dependency, its own spec in docs/15). The plan ships
  without it; the credit price for it is reserved.
- Meta OAuth connect and publishing (blocked by A3). The approval gate and export path are
  built so publishing drops in as a second terminal step without rework.
- Voice input for Q6, seasonal rotation, depth-question drip (docs/22 section 4). Post-v1.

## 9. Build checklist, in dispatch order

Owner key: OP = operator writes it personally (inviolable paths). AGENT = dispatched with a
six-part prompt per `AGENTS.md`; operator reviews the artifact against this spec before it
merges. YOU = founder.

| # | Item | Owner | Gate |
|---|---|---|---|
| 0 | Keys into `.env.local`: DATABASE_URL, ANTHROPIC_API_KEY, FAL_KEY | YOU | **DONE 20 Aug**, all three verified working |
| 1 | Site fixes batch (section 7) | AGENT | **DONE 20 Aug**, deployed and verified on production |
| 2 | Provision Postgres, first migration runs, booking pipeline lights up | YOU + OP | **DONE 20 Aug** (Supabase, 4 migrations applied) |
| 3 | Better Auth + organizations (DONE 20 Aug, live on production); Stripe checkout, webhook, billing portal (waiting on founder's Stripe account) | AGENT, OP reviews | Stripe keys |
| 4 | Credits ledger + metering module + per-org ceilings | OP | **DONE 20 Aug**, 8 tests |
| 5 | Intake flow, ten screens per section 3, autosave, taxonomy autocomplete | AGENT | **BUILT 20 Aug**, on branch `wip/wizard-lint`, operator review pending |
| 6 | Blueprint schema + generation pipeline stages 1-3 | AGENT for schema/prompts, OP for injection hardening and lint | Lint and prompt hardening written on `wip/wizard-lint`, tests pending; pipeline itself not started |
| 7 | Deterministic compositor per docs/19 (zones, budgets, contrast, fallbacks) | AGENT, OP verifies determinism and hash coverage | **DONE 20 Aug**, 68 tests, byte-determinism verified. **Width gates added 25 Aug** (docs/19 section 9): probe defects fixed, all text measured against zone geometry, containment pinned by test |
| 8 | Persist + hash + approval workspace wired to `publish-guard.ts` | OP | **DONE 25 Aug**, browser-walked against the dev database: approve writes real approval rows, editing voids approval and re-lints, the gate blocks and passes exactly per publish-decision. Live end-to-end generation still gated by the API top-ups |
| 9 | Export walkthrough page with Copy buttons and AI disclosure | AGENT | 8 |
| 10 | Dashboard home: credits, empty states, measured/reported labelling | AGENT | 3 |
| 11 | End-to-end run of acceptance steps 1-9 (`ROADMAP.md` A-Z test) by a real person | YOU | all |
| 12 | A4 screencast recorded against the working flow; App Review filed | YOU + OP | 11, Track A steps 1-4 done |

Definition of done for every agent item: typecheck clean, tests pass, no em-dash anywhere,
no route around the approval gate, voice rules hold on every customer-facing string, and the
operator has read the artifact, not the agent's summary.

## 10. Open questions still yours

1. Confirm the OPERATOR CALLs: derived budget (section 3, Q4), credit action prices
   (section 2), "Ten questions. About three minutes." (section 7.4).
2. Tier names: the site currently implies tiers; "Starter / Growth / Max" is used here.
   Say if you want different names.
3. The dismissed budget question is settled by the section 3 OPERATOR CALL unless you say
   otherwise.
