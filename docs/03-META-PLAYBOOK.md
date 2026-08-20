# Meta Marketing API — Critical Path

Everything in `research/02-ad-platform-apis.md`, compressed into what you must actually do.
**This is the long pole of the entire project. Start it before writing product code.**

## The two gates, in order

There are two *independent* approvals, and most people only plan for the first.

**Gate 1 — App Review (permissions).** Approval to request scoped permissions at all.
For this product's lead-ads flow, the bundle is:
`ads_management`, `ads_read`, `business_management`, `pages_show_list`,
`pages_read_engagement`, `pages_manage_metadata`, `leads_retrieval`, `instagram_basic`.

Meta's own 2026 guidance sets expectations at **~20 days**, up from 10. **Every rejection
restarts the clock.** Budget for at least one rejection cycle.

**Gate 2 — Business Verification.** A separate prerequisite requiring legal business documents
tied to the Business Manager. ~5 business days when clean; **1–3+ weeks when stuck**. The
number one cause of delay is a mismatch between submitted documents and profile fields —
business name, address, and domain must match *exactly* across your incorporation documents,
the Business Manager profile, and your website's WHOIS/domain.

**Then: Marketing API Access Tier.** Full Access requires **500+ API calls in the past 15 days
at under 15% error rate.** But in Development Mode the API only works on ad accounts you
personally administer.

> **The catch-22:** you cannot generate real-customer call volume before approval, and you
> cannot get approval without call volume. The resolution is to dogfood aggressively on your
> own and test ad accounts until you have the 500-call, low-error track record — *then* apply.

## Rate limits you must design against

- Business Use Case points, per ad account: **read = 1, write = 3**
- Limited Access: max 60 points, 300s decay, **300s block** on breach
- Full Access: max 9,000 points, 300s decay, 60s block
- A **spend-based hourly quota per ad account** layers on top and scales with trailing monthly
  spend — new low-spend customers are tightly capped regardless of your tier
- Hard caps: 100 mutations/sec per app+account, `spend_cap` changes 10/day,
  **ad set budget changes 4/hour** (this one directly limits optimization frequency)

## Tokens

Do **not** build on "Log in with Facebook" user tokens. Long-lived user tokens expire at ~60
days and the integration dies silently in month two. Use **Business Manager System User
tokens**, which can be issued non-expiring, with the app admin-connected to the client's
Business Manager and granted asset-level permission to the ad account and Page.

## Billing structure — mandatory, not optional

Meta **Policy 10.5, effective 2027-02-03**: any intermediary buying ads on a client's behalf
must expose complete, unaggregated spend and campaign data to that client. This kills the
mark-up-the-media agency model.

Our structure is compliant by construction and must stay that way:
- The customer owns their ad account, with **their own card on file at Meta**
- We charge a separately itemized SaaS subscription
- Media spend never touches our books or our Stripe account

## Also gated, also slow — start these in parallel

- **Twilio A2P 10DLC** registration for lead-alert SMS — its own multi-week approval
- **Business entity + EIN + a matching domain** — prerequisites for Business Verification
- A **privacy policy, terms of service, and data deletion callback URL** — App Review will
  reject without them

## Do this in week one

1. Register the business entity; get the EIN
2. Buy the domain; put up a real site with privacy policy, ToS, and data deletion endpoint
3. Create the Meta App and Business Manager with **exactly matching** name/address/domain
4. Submit Business Verification (longest, most unpredictable pole — start it first)
5. Build against your own ad account in Development Mode, accumulating clean API calls
6. Screen-record the full flow for the App Review submission
7. Submit App Review once you can demo end-to-end on your own account
