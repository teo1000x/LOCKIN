# Delivery model: connected. Supersedes the export-only pivot.

_Decided 19 August 2026 by the founder. This document is authoritative and overrides any
contradicting statement in the files listed at the bottom until those are rewritten._

---

## The decision

Foreman connects to the customer's Meta ad account and publishes the ads it builds.

This reverses the July pivot, in which the product built ads and handed them over as an export
pack for the owner to post themselves in Ads Manager. That model ("Model A" in the older docs)
is now the **interim** behaviour only, used while Meta App Review is pending, and is no longer
the destination.

## What does not change, and cannot

The approval gate. No ad is submitted to Meta unless the owner has read that exact ad and
approved it, and editing an approved ad voids the approval. This is enforced in
`publish-decision.ts` and `publish-guard.ts`, not in the interface.

Connecting to Meta makes this rule **more** load-bearing, not less. In the export model, the
owner physically had to paste the ad into Ads Manager, so the gate was a formality. Now the gate
is the only thing standing between generated content and a live ad on a stranger's card. Do not
weaken it, do not add a bypass flag, and do not let a scheduler publish anything that was not
individually approved.

## What this changes in the product

| Area | Export model (old) | Connected model (now) |
|---|---|---|
| Publishing | Owner pastes into Ads Manager | We publish approved ads via the Marketing API |
| Spend and leads | Owner self-reports everything | Read from the ad account, labelled as measured |
| Booked jobs and value | Owner self-reports | Still self-reported. This never becomes measured. |
| Ad account ownership | Owner's, untouched | Owner's, created in their name, we hold scoped access |
| Token storage | Not needed | Envelope encrypted, `crypto.ts`, never logged |
| Ad rejections | Owner discovers after posting | We see it, fix it, bring a corrected version to approve |

The measured-versus-reported distinction must be visible on every screen that shows a number.
Never render a Meta-sourced figure beside a self-reported one without saying which is which.

## What this changes in the plan

App Review and Business Verification move from optional to **blocking**, and they are the longest
lead-time item in the entire project: two sequential queues, roughly 8 to 12 weeks combined,
neither of which requires any code to exist. They should be filed before further feature work.

App Review requires three live URLs, all of which now exist:

- `/privacy` including a data deletion section at `#deletion`
- `/terms`
- `/refunds`

None have been reviewed by a lawyer. Each page says so on its face. That review has to happen
before the first customer is charged.

## Scoping the OAuth permission

Request the narrowest set that supports publishing and reading results. The terms page commits
publicly to not touching the personal profile, messages, friends, or page inbox, and to being
unable to raise the daily budget or alter a payment method. Those commitments are now published,
so the implementation has to match them.

## Interim behaviour while review is pending

Until publishing is approved, the product builds the campaign and walks the owner through
posting it themselves, and the FAQ says so in a note attached to the first question. The note
lives in `src/components/Faq.tsx` and is commented for removal the day App Review clears. Do not
sell a plan whose main feature is not yet available without that note on the page.

## Files this supersedes

These still describe the export-only model and need a rewrite pass. Read them with this document
in hand.

- `ROADMAP.md`
- `AGENTS.md`
- `docs/01-PRODUCT-SPEC.md`
- `docs/09-SIX-PS.md`
- `docs/10-CLIENT-HANDOFF.md`
- `docs/11-UX-SPEC.md`
- `docs/12-THREE-PS.md`
- `docs/14-AD-POLICY-RULES.md`
- `docs/16-EXPORT-PACK-SPEC.md` (now describes interim behaviour, not the product)
- `docs/07-NAMING.md`, `docs/07-NAMING-V2.md` (positioning language only)

The landing page, the app shell, the legal pages and `docs/08-DESIGN-SYSTEM.md` are already
consistent with this decision.
