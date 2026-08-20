# Ad Platform APIs — Technical & Policy Feasibility Investigation

**Purpose:** Feasibility research for a SaaS that programmatically creates, manages, and optimizes ads on behalf of small service businesses (home services, local trades, etc.).
**Date of research:** 2026-08-19
**Note on sources:** Meta and Google's own docs are treated as authoritative; third-party blog posts (agency tool vendors, "2026 guide" content-marketing sites) are used for texture/timeline color but flagged as such since they are not primary sources and can be stale or self-serving.

---

## A) META (Facebook/Instagram) MARKETING API

### A1. App Review — permissions and approval

Meta restructured its access model on **May 4, 2026**: "Ads Management Standard Access" (AMSA) was renamed **Marketing API Access Tier**, with tiers renamed from Standard/Advanced to **Limited Access** and **Full Access**. This is a *separate, second approval gate* from standard App Review permission approval — i.e., there are two independent things to get through:

1. **Permission-level App Review** — approval to request scoped permissions at all: `ads_management`, `ads_read`, `business_management`, `pages_show_list`, `pages_read_engagement`, `pages_manage_metadata`, `leads_retrieval` (for lead ads), `instagram_basic`. For lead-gen webhook flows specifically, five permissions are typically bundled: `leads_retrieval`, `pages_manage_metadata`, `pages_show_list`, `pages_read_engagement`, `ads_management`.
   Source: [Meta Marketing API Use Cases](https://developers.facebook.com/docs/development/create-an-app/marketing-api-use-cases/), [Facebook Lead Ads API guide](https://leadsync.me/blog/meta-lead-gen-api-guide/)

2. **Marketing API Access Tier (Limited vs Full)** — a usage-gated tier that controls Business Manager scope and rate limits. To qualify for **Full Access** (formerly "Advanced"), Meta now requires **500+ Marketing API calls in the past 15 days** with an **error rate under 15% over the last 500 calls** (lowered from a prior 1,500-call / fixed-window threshold). Screen-recording upload was dropped from the submission. Requirements now show live in the App Dashboard.
   Source: [Meta Developer Blog — Update to Ads Management Standard Access](https://developers.meta.com/blog/updates-to-ads-management-standard-access-feature/)

**Catch-22 for a new SaaS:** you need real API call volume to qualify for Full Access, but in Development Mode (pre-approval) the API only works for ad accounts you personally administer. Practically this means: build and dogfood on your own/test ad accounts to accumulate the 500-call, low-error-rate track record, *then* apply for Full Access before onboarding real customers.

### A2. Business Verification

Business Verification is a **separate prerequisite**, mandatory before Full Access to `ads_management` or before programmatic ad-account creation is possible. It requires legal business documents tied to the Business Manager.
- Reported timeline: document review averaged ~2 days in early 2024, now closer to **~5 business days** for straightforward cases; **escalated/stuck cases run 1–3 weeks**, and mismatches between submitted documents and profile fields (business name, address, domain) are the most common cause of delay. A rejected/resubmitted verification effectively costs another week.
Sources: [singhamandeep.com — What Is Meta Advanced Access](https://singhamandeep.com/what-is-meta-advanced-access/), [Meta Community Forums thread — stuck in review for weeks](https://communityforums.atmeta.com/discussions/Questions_Discussions/business-verification-has-been-stuck-in-in-review-for-several-weeks-meta-develop/1376671), [zenweb.my — Meta Business Verification Stuck](https://zenweb.my/blog/meta-business-verification-stuck/)

### A3. Tech Provider vs Advertiser use case

- **Advertiser use case**: an individual business managing its own ads — does not need App Review at all if just using Meta's own tools (Ads Manager).
- **Tech Provider / Marketing Partner status**: a formally vetted third-party app in Meta's Partner Directory. Getting *listed* as a Tech Provider is a higher, optional bar (separate partner review) that unlocks a named partner support channel and early access to beta Graph API features — **not required to operate**, but useful credibility/support signal later.
- What this SaaS actually needs is standard **App Review for a "manage ads on behalf of other users" use case** — i.e., an app that other businesses log into and grant permission to, which is exactly the gate described in A1.
Source: [Meta Marketing API Use Cases](https://developers.facebook.com/docs/development/create-an-app/marketing-api-use-cases/), [creatorlanehq.com — Meta Tech Provider glossary](https://creatorlanehq.com/glossary/meta-tech-provider)

### A4. Timeline reality

- Standard App Review: officially quoted as 2–7 business days, but Meta's own 2026 guidance now sets expectations at **~20 days**, up from 10 days previously. **Every rejection restarts the clock.** Plan on submitting at minimum two weeks ahead of any target launch, and budget for at least one rejection cycle.
Source: [bundle.social — Meta App Review Now Takes 20 Days](https://bundle.social/blog/meta-app-review-20-days)

### A5. Access tiers / rate limits (Business Use Case scoring)

Official doc: [Rate Limiting — Marketing API](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting/)

- Uses a **Business Use Case (BUC)** point system, per ad account, shared across all endpoints in the same BUC (e.g., all "Ads Management" endpoints share one pool).
- **Read call = 1 point, write call = 3 points.**
- **Limited Access (dev tier):** max score 60, decay 300s, 300s block on breach.
- **Full Access (standard tier):** max score 9,000, decay 300s, only 60s block on breach.
- On top of BUC, Meta layers a **spend-based hourly quota per ad account** that scales with the account's trailing monthly spend — meaning a brand-new customer ad account (near-zero spend) starts with a *very* tight ceiling regardless of your app's tier. This directly matters for a multi-tenant SaaS onboarding many small, low-spend accounts at once.
- **Hard caps regardless of score:** 100 mutation (create/edit) requests per second per app+ad-account pair; `spend_cap` changes limited to 10/day; ad set budget changes limited to 4/hour.
- Ad *creation* volume is separately gated by the account's daily spend limit — low-spend new accounts can only have a small number of active ad objects at once.

**Implication:** at scale (hundreds of small-business ad accounts, most spending $500–$3,000/mo), the per-account spend-based throttle — not the app-level BUC score — is likely the binding constraint on optimization frequency (e.g., how often you can auto-adjust budgets/creative).

### A6. System User tokens vs user tokens

- **User access tokens** (standard OAuth from a business owner logging in): short-lived tokens last 1–2 hours; long-lived tokens last **~60 days**, then must be refreshed via re-auth (or programmatically extended only within a window). This is a real operational liability for "set and forget" automation — if a customer doesn't re-auth, the integration silently breaks in ~2 months.
- **System User tokens** (created inside a Business Manager, tied to the business rather than an individual): can be generated as **non-expiring** tokens (Business Manager-issued System User tokens, distinct from regular Graph API long-lived tokens) and are the standard pattern for production SaaS automation. Requires the app to be admin-connected into the client's Business Manager and given asset-level permission (ad account, page) via System User assignment — this is the correct architecture, not "log in with Facebook" per user session.
Sources: [singhamandeep.com — Meta System User Access Tokens: SaaS Guide](https://singhamandeep.com/meta-system-user-access-tokens/), [Meta — Long-Lived Access Tokens](https://developers.facebook.com/documentation/facebook-login/guides/access-tokens/get-long-lived), [adamigo.ai — Meta API Key Expiration Policies](https://www.adamigo.ai/blog/meta-api-key-expiration-policies-explained)

### A7. End-customer onboarding friction (the real product risk)

This is repeatedly flagged as the **#1 practical bottleneck** for any agency/SaaS tool, independent of API mechanics:
- Manual flow: business owner must go to Business Settings → Partners → Add → enter your Business Manager ID → select assets (Page, ad account, Instagram, pixel) → assign per-asset permission level. Missing the final "assign assets" step leaves a partner connected but with **zero functional access** — reported as the cause of ~90% of failed manual onboardings.
- Confusion between "Ad Account" and "Business Manager" as concepts commonly stalls unsophisticated small-business owners (exactly this SaaS's target customer).
- OAuth-based one-click connection flows (e.g., "Login with Facebook Business" using System User provisioning behind the scenes, as tools like Leadsie/OneClick Onboard implement) are reported as materially faster and less error-prone than the manual Business ID exchange, and should be the v1 build target rather than manual instructions.
- Agencies/tools report onboarding commonly **delays campaign launch by over a week** when done manually.
Sources: [sellforte.com — Grant partner access](https://sellforte.com/support/how-to-grant-a-partner-access-to-business-assets-in-your-meta-business-portfolio), [oneclickonboard.com — Get Meta Business Manager Access From Clients](https://oneclickonboard.com/blog/how-to-get-meta-business-manager-access-from-clients-2026), [herocontent.ai — Add a Partner in Meta Business Manager](https://herocontent.ai/en/blog/add-partner-in-meta-business-manager)

### A8. Special Ad Categories — does this vertical get caught?

Meta requires declaring **Credit, Employment, Housing**, and (new in 2025) **Financial Products and Services** (banking, savings, insurance, investment) as Special Ad Categories, which strip demographic/behavioral targeting.
- **Straightforward home-service verticals (plumbing, HVAC, landscaping, cleaning, roofing, electrical, pest control, auto repair) are NOT Special Ad Categories** and retain full targeting.
- **Watch-outs within "small service businesses"**: mortgage brokers, financial/insurance advisors, debt consolidation, and staffing/recruiting services **would** be swept into Special Ad Category restrictions. If the SaaS's ICP ever expands into financial services, insurance agents, or recruiting/staffing companies, targeting features must be conditionally disabled and category self-declaration enforced in-app (Meta's classifier plus manual review both apply, and misclassification risks ad rejection or account-level enforcement).
Sources: [Jon Loomer — Special Ad Categories: A Guide](https://www.jonloomer.com/special-ad-categories-meta-ads/), [Data Axle — 2025 Meta special ad categories rules](https://www.data-axle.com/resources/blog/meta-special-ad-categories-rules/)

### A9. Creative automation, Advantage+, and what's API-controllable in 2026

- Meta is aggressively pushing all campaign creation toward a **unified Advantage+ structure**. As of **Marketing API v25.0 (Q1 2026)**, creating legacy separate ASC (Advantage+ Shopping) / AAC campaign types is **prohibited** — everything funnels through the unified Advantage+ campaign object, with AI optimization toggled per-component (audience, placement, budget, creative) via API flags rather than choosing a distinct campaign type.
- Creative enhancement/AI-generation controls are set via the **`creative_features_spec`** parameter — you can enable/disable specific auto-enhancement types and (per recent updates) request previews of AI-modified creative before it goes live. This is API-controllable, good news for a tool that wants to auto-generate and iterate creative.
- Current stable Graph/Marketing API version referenced: **v25.0 (Feb 2026)**.
Sources: [ppc.land — Meta launches unified API structure for Advantage+ campaigns](https://ppc.land/meta-launches-unified-api-structure-for-advantage-campaigns/), [ppc.land — Meta deprecates legacy campaign APIs](https://ppc.land/meta-deprecates-legacy-campaign-apis-for-advantage-structure/), [socialmediatoday.com — Meta Updates Marketing API](https://www.socialmediatoday.com/news/meta-updates-marketing-api-to-align-with-latest-ad-shifts/812648/)

### A10. Agency spend-disclosure policy (Policy 10.5) — directly threatens a markup billing model

**This is a major, underappreciated finding.** Meta Developer Policy 10.5, effective **February 3, 2027**, requires **all ad-buying intermediaries (agencies, platforms, resellers) to give the end advertiser direct, unaggregated access to complete spend data, campaign-level breakdowns, and ad account data** — not summarized/rolled-up reporting. It applies to exactly the category this SaaS falls into (a platform buying ads on behalf of clients). Non-compliance risks **account restriction or platform API access revocation**.
- Practical effect: the product **cannot** hide raw Meta spend behind an opaque "package price" if it is itself the buyer of record — the small business must be able to see exactly what Meta charged, separate from any platform fee. This pushes the business model toward **client-owned ad accounts + separate SaaS/management fee** (cleaner) rather than **agency-owned ad account with spend baked into a blended price** (now explicitly against policy, effective Feb 2027 — well within this product's likely launch window).
Source: [Prooflytics — Meta Policy 10.5: Agency Spend Disclosure Compliance Guide](https://prooflytics.io/blog/meta-developer-policy-10-5-agency-spend-disclosure-2027)

---

## B) GOOGLE ADS API

### B1. Developer token — access levels

Official docs: [Access levels and RMF](https://developers.google.com/google-ads/api/docs/productionize/access-levels), [Developer Token](https://developers.google.com/google-ads/api/docs/api-policy/developer-token)

- **Test Account Access**: default on token creation, test accounts only, 15,000 operations/day.
- **Basic Access**: production + test accounts, **15,000 operations/day**, requires application review. This is the workhorse tier for a single-org/single-app integration and covers the full permissible-use set. Brand verification is optional here but speeds approval.
- **Standard Access**: production + test, **unlimited operations**, but triggers **Required Minimum Functionality (RMF)** — Google mandates your product implement a baseline set of campaign-management capabilities, and can levy **non-compliance fees** if you fall short. Only pursue Standard once volume genuinely requires it.

### B2. Application requirements & rejection reasons

- Requirements: real company name (or "Individual" + an online presence URL like GitHub/LinkedIn — generic placeholder URLs like "test.com" get rejected), a **functioning company website**, and a monitored API contact email (Google's compliance team may email for clarification and will reject if unreachable).
- **Common rejection reasons**: vague use-case description, insufficient spend history (<$1,000 under the applying manager account), account policy violations, or an application that reads as personal rather than business use.
- **Timeline**: initial review commonly 5–7 business days for Basic; some reports of 6-month delays for edge cases/appeals. Google explicitly recommends applying **well before** you need the access, since review can stretch into weeks.
Sources: [groups.google.com — Ads API application took 6 months](https://groups.google.com/g/adwords-api/c/Eq9uxpNbeA0), [ppc.land — Google faces developer token application backlog](https://ppc.land/google-faces-developer-token-application-backlog-as-new-api-tier-debuts/)

### B3. MCC (manager account) requirement & OAuth

- All API access is anchored to a Google Ads **Manager (MCC) account**; the developer token is issued at the MCC level.
- Linking a client account is a **two-step, mutual-consent process**: manager account creates a `CustomerClientLink` (PENDING), client account must separately accept via `CustomerManagerLink` update to ACTIVE — this requires the client to take an action (log in and accept), which is an onboarding friction point analogous to Meta's partner-access flow, though generally simpler.
- OAuth uses `login-customer-id` header to operate on client accounts through the manager's credentials once linked.
Source: [Linking to Manager Accounts — Google Ads API](https://developers.google.com/google-ads/api/docs/account-management/linking-manager-accounts)

### B4. Performance Max, Search, Local — API coverage in 2026

- **Performance Max campaign creation is fully supported via the API** (bulk mutate: CampaignBudget, Campaign, CampaignAssets, AssetGroups, AssetGroupAssets in one request) — this is good news, PMax is Google's flagship format for lead-gen local service businesses.
Source: [Add Performance Max Campaign — Google Ads API](https://developers.google.com/google-ads/api/samples/add-performance-max-campaign)
- **Search campaigns**: fully API-supported (long-standing, mature surface).

### B5. Google Local Services Ads (LSA) API — the critical gap for home services

This is a **major blocker specific to the target market** (home services / local trades are LSA's core use case — pay-per-lead plumbers, electricians, HVAC, lawyers, locksmiths).
- Google is **retiring the standalone LSA dashboard in 2026**, folding existing LSA pay-per-lead campaigns into the main Google Ads platform as a specialized **Performance Max for pay-per-lead-goals** campaign subtype.
- **Current API support is read/update only for existing LSA-PMax campaigns**: retrieve, edit status/budget, set bidding strategy (ManualCpa, MaximizeConversions), set ad schedule, location targeting, service-type targeting.
- **Campaign creation is NOT supported via API** — you cannot programmatically stand up a new Local Services campaign, nor manage sub-entities (ad groups/ads/criteria) for LSA-type campaigns. A human must create the LSA campaign once through the UI; the API can only manage it afterward.
Sources: [Local Services campaigns — Google Ads API](https://developers.google.com/google-ads/api/docs/campaigns/local-service-campaigns), [TechWyse — Google Kills LSA Dashboard](https://www.techwyse.com/news/platform-updates/google-local-services-ads-performance-max-migration-local-inventory-ads-default-2026), [Local Services API overview](https://developers.google.com/local-services-ads/guides/local-services-api-overview)

**Implication:** LSA — arguably the single best-fit, highest-intent ad product for the stated ICP (plumbers, electricians, HVAC, roofers) — cannot be a fully self-serve, API-only product in this SaaS. v1 should lead with **Google Search + Performance Max** (fully API-buildable) and treat LSA as a semi-manual, concierge-assisted add-on (assisted setup, then API-managed optimization) rather than a core automated flow.

### B6. Rate limits / operations quotas

- Basic Access: 15,000 operations/day (an "operation" is roughly one mutate on one resource — creating 50 ads with 5 fields each still counts efficiently since operations batch).
- Standard: unlimited operations but subject to RMF compliance requirements.
- The API itself is **free** at all tiers (Explorer/Basic/Standard) — no Google-side usage fee, unlike some platforms.
Source: [Access levels and RMF](https://developers.google.com/google-ads/api/docs/productionize/access-levels)

---

## C) OTHER PLATFORMS

### C1. TikTok Ads (Marketing API)

- Requires: Business Center onboarding, a registered developer app (client_key/client_secret), OAuth 2.0 advertiser authorization, and — for meaningful production volume — **passing TikTok's app review plus a data-security compliance audit**. Business verification required for higher-volume access. 2026 commentary notes review has gotten **stricter** and more conditional for higher-volume/sensitive use cases.
- **Pricing: free**, no published per-call fee or subscription tier.
- **Assessment**: viable second platform, but the compliance audit is a real, non-trivial gate — treat as a v2 addition once Meta+Google flows are proven, not part of the MVP critical path.
Sources: [getphyllo.com — TikTok API Integration Guide 2026](https://www.getphyllo.com/post/tiktok-api-integration-guide-2026-setup-endpoints-common-pitfalls), [blotato.com — TikTok API Pricing](https://www.blotato.com/blog/tiktok-api-pricing)

### C2. Microsoft Advertising (Bing Ads) API

- Requires three credentials together: a **Developer Token** (requested once per Super Admin account via the Microsoft Advertising Developer Portal — no lengthy review process described, closer to self-serve than Meta/Google), **Microsoft Entra ID OAuth app registration** (client ID/secret), and per-user delegated OAuth tokens.
- **2026 migration note**: legacy SOAP API (Bing Ads v13) enters feature freeze **Oct 1, 2026** and is fully decommissioned **Jan 31, 2027** — any new build should target the **REST API** directly, not SOAP.
- **Assessment**: lowest-friction of the major ad platforms for developer onboarding (single Super Admin-issued token, no separate business verification gate found in research). Reasonable **third platform** to add — small service businesses do get meaningful low-CPC volume on Bing/Microsoft Search, and the integration lift looks materially lower than Meta or Google.
Source: [Get Started With the Bing Ads API](https://learn.microsoft.com/en-us/advertising/guides/get-started?view=bingads-13), [FAQ — Microsoft Advertising API](https://learn.microsoft.com/en-us/advertising/guides/faq?view=bingads-13)

### C3. Yelp Ads / Nextdoor Ads

- **Yelp Ads API**: exists, but restricted to **"Approved Yelp Advertising Partners"** — an explicit partner-qualification gate before any API access is granted (not self-serve app review like Meta/Google). Endpoints exist for program creation/modification/termination.
Source: [Yelp Ads API docs](https://docs.developer.yelp.com/docs/ads-api)
- **Nextdoor Ads API**: launched as a formal "Ads API Program" (April 2024), also **partner-gated** (early partners), enabling full campaign creation/management/reporting. Nextdoor is specifically pitched as high-intent/high-trust for **local/neighborhood SMB advertisers** — a strong product-market fit with this SaaS's ICP, but access is by partner application, not automatic.
Source: [Nextdoor Launches Ads API Program](https://about.nextdoor.com/press-releases/nextdoor-launches-ads-api-program-offering-advertisers-an-easier-way-to-extend-their-campaigns-to-nextdoor), [Nextdoor Advertising Overview docs](https://developer.nextdoor.com/docs/advertising-overview)
- **Assessment**: both are worth a partner-access application in parallel with v1 build (Nextdoor especially, given ICP fit), but neither should block launch — expect a business-development-style approval process, not a self-serve API key.

### C4. Call tracking & offline conversion import

- **CallRail**: mature, purpose-built for this use case. Native Google Ads integration auto-reports call/form conversions; **manual or automated offline conversion import** supported; pricing starts **~$30/mo**, scaling to ~$120/mo depending on plan/number count. Google's own **Offline Conversion Import API** (`Import call conversions` — [docs](https://developers.google.com/google-ads/api/docs/conversions/upload-calls)) requires caller ID, conversion datetime, and the conversion action resource name; conversions typically appear in Google Ads within ~3–24 hours.
- **Twilio**: lower-level primitive (programmable voice/SMS + Twilio Studio) — no out-of-the-box ad-platform conversion mapping; would require building the CallRail-equivalent logic yourself (call recording, number pooling per campaign/source, webhook to Conversions API). More engineering effort, more flexibility/lower marginal cost at scale.
- **Meta side**: equivalent mechanism is the **Conversions API (CAPI)**, which supports offline/call-based conversion events server-side.
- **Assessment**: for v1, **CallRail as a metered pass-through/reseller integration** is the fastest path — it's the de facto standard in the home-services agency world and already solves dynamic number insertion + Google/Meta offline conversion upload. Build your own call-tracking layer only once volume justifies the engineering cost.
Sources: [CallRail — Google Ads integration](https://support.callrail.com/hc/en-us/articles/5711821111053-Google-Ads-integration), [Google Ads API — Import call conversions](https://developers.google.com/google-ads/api/docs/conversions/upload-calls)

### C5. Payment/billing model constraints — can you charge a % of ad spend?

- **No blanket prohibition** on percentage-of-spend management fees at either Meta or Google — this is standard agency practice (industry norm cited at **10–20% of monthly spend** plus retainers).
- **The real constraint is architectural, not about the percentage**: as covered in A10, **Meta Policy 10.5 (effective Feb 3, 2027)** requires that if your platform is the buyer of ad inventory on behalf of clients, the client must get **direct, unaggregated visibility into exact platform spend** — you cannot blend platform spend into an opaque bundled price. A "true reseller" model where you buy inventory and mark it up invisibly (the "buy $43.5k, bill $50k, keep the spread" pattern documented in agency-fee research) is now explicitly against policy for Meta.
- Google requires similar **transparency in reporting** to end-advertisers for third parties operating campaigns via API, though no single named policy number was found equivalent to Meta's 10.5.
- **Recommended model given policy risk**: **client owns/pays for their own ad account directly** (their card/invoicing on file with Meta/Google) + **separate, clearly-itemized SaaS/platform fee** (flat or % of spend, billed by you, clearly labeled as your fee, not blended into "ad spend"). This is both the lower-compliance-risk path and avoids the SaaS ever floating client ad spend on its own balance sheet (the "agency as short-term lender" cash-flow risk documented for float-based invoicing models).
Sources: [Prooflytics — Policy 10.5](https://prooflytics.io/blog/meta-developer-policy-10-5-agency-spend-disclosure-2027), [Google Ads API policies](https://support.google.com/adspolicy/answer/6169371?hl=en), [adamigo.ai — Agency playbook: Meta ad spend without credit cards](https://www.adamigo.ai/blog/meta-ad-spend-no-credit-cards-agency-playbook-monthly-invoicing)

---

## D) THE BIG BLOCKERS — ranked by severity/timeline risk

1. **[SEVERE, months-scale risk] Meta App Review + Business Verification stacking.** Two independent gates (permission review ~20 days with restart-on-rejection, + Business Verification ~5 days typical but 1–3+ weeks when stuck) must both clear before you can onboard any real customer beyond your own test ad accounts. Combined worst-case realistically **4–8 weeks**, and rejections are common enough to plan for at least one resubmission cycle. **This is the single biggest schedule risk for the whole project.**

2. **[SEVERE, architectural] Meta Policy 10.5 spend-disclosure mandate (effective Feb 3, 2027).** If the product's billing model assumes buying media and marking it up invisibly (the classic agency float/markup model), it is walking directly into a policy that revokes exactly that pattern. Must be designed around from day one — client-owned ad accounts + itemized platform fee, not blended billing.

3. **[HIGH, product-shape risk] No API for creating Google Local Services Ads campaigns.** LSA is the best product-market fit for home-service SMBs (pay-per-lead, Google Guaranteed badge) but campaign *creation* is UI-only; API only manages existing campaigns. Any "fully automated, zero-touch" pitch cannot include LSA in v1 without a manual/concierge setup step.

4. **[HIGH, chicken-and-egg] Meta's Full Access qualification requires existing API call volume (500 calls/15 days, <15% error rate) — but Development Mode only works on accounts you administer.** Must build and generate synthetic/test volume on owned test ad accounts before customer-facing usage is possible at Full Access rate limits (9,000 vs 60 BUC points).

5. **[MEDIUM-HIGH, ongoing operational risk] Per-account spend-based rate throttling on Meta.** New, low-spend small-business ad accounts get tight hourly API quotas regardless of your app's own tier — this caps how aggressively you can "optimize" (auto-adjust budgets/creative) for exactly the low-spend customers this SaaS targets, especially early in a customer's lifecycle.

6. **[MEDIUM, onboarding UX risk, not a hard blocker] End-customer connection friction on Meta.** Manual Business Manager partner-access flows are commonly abandoned or mis-completed by non-technical small-business owners (~90% failure rate cited for the "forgot to assign assets" failure mode alone). Must invest early in a guided/OAuth-based one-click connection flow rather than instructing users through raw Business Settings.

7. **[MEDIUM, review-timeline risk] Google Ads developer token review (5–7 days typical, but reports of multi-week/multi-month edge cases) + Required Minimum Functionality obligations once you outgrow Basic's 15,000 ops/day** — lower risk than Meta but still a real dependency; apply early and build toward RMF compliance if scale is expected.

8. **[LOW-MEDIUM, partner-gated but not urgent] Yelp and Nextdoor both require explicit partner approval before any API access** (not self-serve). Not launch-blocking since they're reasonable v2 additions, but the BD-style approval process should be kicked off early in parallel if they're on the roadmap, since timelines are opaque/unpublished.

9. **[LOW, manageable] Meta System User token architecture and Special Ad Category edge cases** are both solvable with correct engineering (System User tokens for stability; conditional Special Ad Category handling if the ICP ever includes financial/insurance/staffing verticals) — flagged for design awareness, not schedule risk.

### Fastest legitimate path to a working v1 for a solo founder

1. **Pick Google Ads as the lead platform, not Meta.** Google's Basic Access review is faster and less layered (single gate, ~5–7 days typical, no separate "business verification" blocker), the API is free, and **Search + Performance Max campaign creation is fully API-buildable today** — a complete, real, automatable product surface without a second approval gate.
2. **In parallel, start the Meta App Review + Business Verification process on day one** (it's the longest lead-time item, ~4–8 weeks realistic), using your own ad account(s) to accumulate the 500-call/15-day track record Meta requires for Full Access — by the time Google's side is shipped, Meta should be clearing review.
3. **Architect billing as client-owned ad accounts (their card on file with Google/Meta directly) + a separate, clearly itemized SaaS fee** (flat or % of spend) from day one — avoids Policy 10.5 exposure and avoids becoming an unintentional lender floating client ad spend.
4. **Use System User tokens (Meta) and MCC-linked OAuth (Google)** from the start, not personal user tokens — building on short-lived user tokens now means a costly re-architecture later when they expire and silently break customer campaigns.
5. **Bolt on CallRail** (not a custom-built call-tracking stack) for offline conversion import — it's the fastest way to close the loop on lead-gen ROI reporting, which local service businesses will demand as proof of value.
6. **Defer Local Services Ads to a semi-manual "concierge setup, API-managed thereafter" flow** rather than promising full automation — the API simply doesn't support LSA campaign creation yet.
7. **Treat TikTok, Microsoft Advertising, Yelp, and Nextdoor as v2/v3** — Microsoft is the cheapest to add next (simplest token issuance, no separate verification gate found), Nextdoor is the best ICP fit but partner-gated so worth applying early even if not built immediately, TikTok and Yelp are lowest priority given audit/partner overhead relative to likely ROI for this specific ICP (contractors/home services skew older, lower TikTok ad reliance).

---

## Sources (consolidated)

- [Meta Developer Blog — Update to Ads Management Standard Access](https://developers.meta.com/blog/updates-to-ads-management-standard-access-feature/)
- [Meta — Rate Limiting, Marketing API](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting/)
- [Meta — Marketing API Use Cases](https://developers.facebook.com/docs/development/create-an-app/marketing-api-use-cases/)
- [Meta — Long-Lived Access Tokens](https://developers.facebook.com/documentation/facebook-login/guides/access-tokens/get-long-lived)
- [Meta Community Forums — Business Verification stuck in review for weeks](https://communityforums.atmeta.com/discussions/Questions_Discussions/business-verification-has-been-stuck-in-in-review-for-several-weeks-meta-develop/1376671)
- [Prooflytics — Meta Policy 10.5: Agency Spend Disclosure Compliance Guide](https://prooflytics.io/blog/meta-developer-policy-10-5-agency-spend-disclosure-2027)
- [ppc.land — Meta launches unified API structure for Advantage+ campaigns](https://ppc.land/meta-launches-unified-api-structure-for-advantage-campaigns/)
- [ppc.land — Meta deprecates legacy campaign APIs for Advantage+ structure](https://ppc.land/meta-deprecates-legacy-campaign-apis-for-advantage-structure/)
- [Jon Loomer Digital — Special Ad Categories: A Guide for Meta Ads](https://www.jonloomer.com/special-ad-categories-meta-ads/)
- [Data Axle — The 2025 Meta special ad categories rules](https://www.data-axle.com/resources/blog/meta-special-ad-categories-rules/)
- [singhamandeep.com — Meta System User Access Tokens: SaaS Guide (2026)](https://singhamandeep.com/meta-system-user-access-tokens/)
- [singhamandeep.com — What Is Meta Advanced Access](https://singhamandeep.com/what-is-meta-advanced-access/)
- [bundle.social — Meta App Review Now Takes 20 Days](https://bundle.social/blog/meta-app-review-20-days)
- [sellforte.com — How to grant a partner access to Meta Ad accounts](https://sellforte.com/support/how-to-grant-a-partner-access-to-business-assets-in-your-meta-business-portfolio)
- [oneclickonboard.com — How to Get Meta Business Manager Access From Clients (2026)](https://oneclickonboard.com/blog/how-to-get-meta-business-manager-access-from-clients-2026)
- [Google — Access levels and RMF, Google Ads API](https://developers.google.com/google-ads/api/docs/productionize/access-levels)
- [Google — Developer Token, Google Ads API](https://developers.google.com/google-ads/api/docs/api-policy/developer-token)
- [Google — Linking to Manager Accounts, Google Ads API](https://developers.google.com/google-ads/api/docs/account-management/linking-manager-accounts)
- [Google — Add Performance Max Campaign sample](https://developers.google.com/google-ads/api/samples/add-performance-max-campaign)
- [Google — Local Services campaigns, Google Ads API](https://developers.google.com/google-ads/api/docs/campaigns/local-service-campaigns)
- [Google — Local Services API overview](https://developers.google.com/local-services-ads/guides/local-services-api-overview)
- [TechWyse — Google Kills LSA Dashboard, Forces Local Inventory Ads On](https://www.techwyse.com/news/platform-updates/google-local-services-ads-performance-max-migration-local-inventory-ads-default-2026)
- [Google — Import call conversions, Google Ads API](https://developers.google.com/google-ads/api/docs/conversions/upload-calls)
- [Google Ads API policies — Advertising Policies Help](https://support.google.com/adspolicy/answer/6169371?hl=en)
- [groups.google.com — Ads API application took 6 months for review](https://groups.google.com/g/adwords-api/c/Eq9uxpNbeA0)
- [ppc.land — Google faces developer token application backlog](https://ppc.land/google-faces-developer-token-application-backlog-as-new-api-tier-debuts/)
- [Microsoft Learn — Get Started With the Bing Ads API](https://learn.microsoft.com/en-us/advertising/guides/get-started?view=bingads-13)
- [Microsoft Learn — FAQ, Microsoft Advertising API](https://learn.microsoft.com/en-us/advertising/guides/faq?view=bingads-13)
- [Yelp Developers — Ads API](https://docs.developer.yelp.com/docs/ads-api)
- [Nextdoor — Launches Ads API Program](https://about.nextdoor.com/press-releases/nextdoor-launches-ads-api-program-offering-advertisers-an-easier-way-to-extend-their-campaigns-to-nextdoor)
- [Nextdoor Developer — Advertising Overview](https://developer.nextdoor.com/docs/advertising-overview)
- [getphyllo.com — TikTok API Integration Guide 2026](https://www.getphyllo.com/post/tiktok-api-integration-guide-2026-setup-endpoints-common-pitfalls)
- [blotato.com — TikTok API Pricing: Full Breakdown for 2026](https://www.blotato.com/blog/tiktok-api-pricing)
- [CallRail — Google Ads integration](https://support.callrail.com/hc/en-us/articles/5711821111053-Google-Ads-integration)
- [adamigo.ai — Agency playbook: how to run Meta ad spend without credit cards](https://www.adamigo.ai/blog/meta-ad-spend-no-credit-cards-agency-playbook-monthly-invoicing)
