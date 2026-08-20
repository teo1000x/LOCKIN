# Meta Ad Library API - Technical Spec for the Competitive Read

Verified against current Meta documentation and product pages on 2026-08-19. No application
code in this document, per the assignment. See `AGENTS.md` and the PIVOT section of
`docs/01-PRODUCT-SPEC.md` for why this is the only live external data source left in the
product after the no-Meta-connection pivot.

## Verdict up front, because it changes the plan

The founder's framing in `AGENTS.md` ("reads PUBLIC ad data with a token WE hold... no App
Review") is correct about the mechanics of access. It is **not fully correct about what the
API can return.** The critical fact, confirmed directly against Meta's own endpoint reference:

> "Ads that did not reach any location in the EU will only return if they are about social
> issues, elections or politics."
> - [developers.facebook.com/docs/graph-api/reference/ads_archive](https://developers.facebook.com/docs/graph-api/reference/ads_archive/)

And from Meta's own Ad Library API landing page, describing the tool's actual purpose:

> "a deeper analysis of ads about social issues, elections or politics, as well as ads that
> deliver to the EU and associated territories."
> - [facebook.com/ads/library/api](https://www.facebook.com/ads/library/api)

Translated: **a purely US-local HVAC, plumbing, roofing, or electrical company's commercial
Facebook/Instagram ad is, in the general case, invisible to this API**, because it is neither
a political/issue ad nor an ad that reached the EU or UK. This is not a quota problem or a
tier problem. It is a coverage wall, and it is the single most important thing in this
document. Section 2 below goes through it in full, including the one real exception (Special
Ad Category ads) and why that exception mostly does not rescue the trades use case.

## 1. Access and authentication

Steps the founder takes, in order:

1. **Identity confirmation.** Go to `facebook.com/ID` and confirm identity on the personal
   Facebook account that will own the developer app. Meta's Business Help Centre describes
   this as required to run or fully use tools tied to the Ad Library:
   ["confirm your identity and location at Facebook.com/ID"](https://www.facebook.com/business/help/167836590566506).
   This is a one-time step per person, not per app.
2. **Create a Meta for Developers app.** A standard app is sufficient. Reading `ads_archive`
   is public-data access and does **not** require App Review, which matches the founder's
   claim in `AGENTS.md`. App Review exists to gate advanced permissions like
   `ads_management` or access to another user's data; `ads_read` against the public archive
   does not need it.
3. **Generate an access token with the `ads_read` scope.** Via Graph API Explorer or a
   server-side OAuth exchange, request `ads_read` (not `ads_management`, which the product
   deliberately never touches per Inviolable Rule 2 in `AGENTS.md`).
4. **Exchange for a long-lived token.** Short-lived tokens from web login last about one
   hour. Exchange server-side with the app secret for a long-lived token, which Meta's own
   docs describe as lasting "approximately 60 days," with an explicit warning:
   ["Do not depend on these lifetimes remaining the same, they may change without warning or
   expire early."](https://developers.facebook.com/docs/facebook-login/guides/access-tokens/)

**The operational trap, confirmed real.** A long-lived user token does not silently renew
itself. It is not tied to activity; it just expires around day 60 and then every Ad Library
call fails until a human re-authenticates. For a solo-founder product with no ops team, this
is exactly the "churn machine disguised as a bug" pattern `docs/02-TECH-STACK.md` already
called out for the (now-deleted) Marketing API OAuth flow. It resurfaces here because this is
now the only Meta integration left.

Two mitigations, not mutually exclusive:

- **Minimum viable: a token health monitor.** A scheduled job (Inngest, daily) makes a
  trivial `ads_archive` call and records success/failure plus token-issued-at. Alert the
  founder by email at day 45 and day 55 with the exact re-auth steps. This is cheap and
  should ship on day one, because there is no customer-facing fallback for "our own token
  died silently."
- **Harder but durable: a System User token.** Meta allows non-expiring tokens for a System
  User inside a verified Business Manager. Multiple current integration guides describe this
  path: "add a System User in Business Manager... though this requires a verified Business
  Manager with business documentation." This is the same pattern `docs/02-TECH-STACK.md`
  recommends for the Marketing API, and it appears to extend to Ad Library access, but it
  should be smoke-tested against a real Business Manager before being relied on, since the
  Ad Library's identity-verification step is tied to an individual account, not a business
  asset, and the two systems are not guaranteed to compose cleanly. Treat this as a fast
  follow, not a launch blocker; ship the health monitor first.

Cost: the Ad Library API itself has no paid tier and no per-call charge.

## 2. The critical limitation, investigated honestly

This is the section the founder is planning around, so it gets a direct answer per field.

**Can we search by advertiser location (a US business's own location)?** Only indirectly.
`ad_reached_countries` filters by where the ad *was delivered*, not where the advertiser is
based, and it is a mandatory parameter on every call. There is no radius or ZIP-based
geo-targeting filter in the API for where an ad was delivered; that granularity is not
exposed. Local delivery targeting used by the advertiser is not a searchable field.

**Can we search by keyword?** Yes, via `search_terms` (up to 100 characters, unordered
keywords or exact phrase via `search_type`), but this is a keyword match against ad text and
page name, not a geographic filter, and it is subject to the same coverage wall below.

**Can we search by Page?** Yes, `search_page_ids` accepts up to ten Facebook Page IDs per
call and returns that Page's archived ads directly. This is the one search mode not gated
by the political/EU coverage rule in the same way, because it is scoped to a specific,
already-identified advertiser rather than an open query. See Section 3.

**Can we filter to a geographic radius around Austin, TX?** No. There is no radius or
lat/long parameter. Geographic filtering is limited to `ad_reached_countries` (country-level,
or an EU/UK-only region designation), nothing finer.

**What fields come back, and for whom?** `ad_type` accepts `ALL`, `EMPLOYMENT_ADS`,
`FINANCIAL_PRODUCTS_AND_SERVICES_ADS`, `HOUSING_ADS`, and `POLITICAL_AND_ISSUE_ADS`. Fields
on a returned ad include creative body text, link titles/descriptions, image and video
references, publisher platforms (Facebook, Instagram, Messenger, Audience Network),
`ad_delivery_start_time`, and `ad_delivery_stop_time`. Spend ranges, impression ranges, and
demographic reach breakdowns are documented as EU/UK-only additions and are not populated for
ordinary US commercial ads. So even for the ads that *do* surface, US commercial results will
never carry the spend and impressions data political ads or EU-delivered ads carry.

**The coverage wall itself, precisely.** Per Meta's own endpoint reference and product page
(cited above), the archive holds two overlapping sets: (a) ads about social issues, elections,
or politics, delivered anywhere in the world, retained seven years, and (b) ads of any kind
delivered into the EU or UK, retained about one year (the EU Digital Services Act is the
reason this second bucket exists at all, not a Meta product choice). **A US commercial ad
that never reached the EU or UK falls into neither bucket and does not return from
`ads_archive`, full stop**, regardless of `ad_type=ALL` or how the query is built.

**The one real exception: Special Ad Category ads.** `HOUSING_ADS`, `EMPLOYMENT_ADS`, and
`FINANCIAL_PRODUCTS_AND_SERVICES_ADS` are US-specific mandatory compliance classifications
tied to fair-housing and fair-employment law, and Meta requires all ads in those categories to
be archived regardless of political status. This does not rescue the trades use case in
general: HVAC, plumbing, roofing, and electrical ads are not housing, employment, or credit
ads. The one place it matters is if a contractor's ad promotes **financing** ("0% financing
on a new system," "buy now pay later") strongly enough to be classified
`FINANCIAL_PRODUCTS_AND_SERVICES_ADS`; those specific ads would be archived and searchable
even without EU reach. That is a narrow, unreliable win, not a strategy.

**Bottom line for this section:** for the stated goal ("what other HVAC companies within 25
miles of Austin are running right now"), a keyword or open search against `ads_archive` will
return close to nothing, because almost no local trades company runs ads that reach the EU or
qualify as political/issue/financing ads. The workable path is the Page-lookup mode in
Section 3, and it has its own real limits.

## 3. Query strategy, given the real capabilities

Open keyword search cannot find local competitors because of the coverage wall. The only
reliable path is: **resolve competitor Facebook Pages first, by means outside the Ad Library
API, then query those Pages directly with `search_page_ids`,** which returns that Page's
active and recently-inactive ads without depending on the EU/political gate in the same way
an open search does. This is a two-stage pipeline, not a single query.

**Stage A: find candidate competitor Pages for "HVAC within 25 miles of Austin, TX."**
The Ad Library API cannot do this step; nothing in `ads_archive` resolves "local businesses of
trade X near location Y" to Page IDs. Realistic sources for Stage A, roughly in order of
reliability and cost:
- The **public Ad Library website** (`facebook.com/ads/library`), which has its own search
  UI, is not the same product as the API, and can sometimes be searched by an advertiser name
  a human already knows. It is a manual fallback, not an automatable one, and should not be
  scraped (Section 7).
- A **local business directory pass**: Google Places / Google Business Profile data (or
  similar) for "HVAC contractor" within a 25-mile radius of the business's stored
  `latitude`/`longitude`/`radiusMiles` in `businesses`, which typically yields a business name
  and website. This is the most reliable resolver and is worth building regardless, since it
  also seeds the "how many competitors are advertising at all" metric in Section 6.
- **Website-to-Page resolution**: fetch the candidate's website and look for a Facebook Page
  link (common in trades-company footers), or use the Graph API's Page search
  (`/pages/search`) with the business name as a secondary resolver.
- Manual seeding for the first cohort of design-partner metros, since volume is low early on
  and this directly improves Stage B's hit rate.

**Stage B: query the Ad Library API per resolved Page.** Call `ads_archive` with
`search_page_ids` (batch up to ten Page IDs per call), `ad_type=ALL`, `ad_reached_countries`
set to `US`, and a fields list covering creative body, images/video, link titles, delivery
platforms, and start/stop time. Because this call is scoped to a known Page rather than an
open query, it surfaces that Page's ads whether or not they hit the EU/political gate that
blocks open keyword search. Persist every returned ad against the resolving market (Section
5).

**Concrete algorithm:**

```
1. Given a business record (trade, lat/lng, radiusMiles):
2. If a fresh cache entry exists for (trade, geography-bucket) within the TTL (Section 4),
   serve it and stop.
3. Else, resolve candidate competitor Pages:
   a. Query a business-directory source for "{trade} contractor" within radiusMiles of
      lat/lng, cap at ~25-40 candidates.
   b. For each candidate without a known Page ID, attempt website-footer scan, then Graph
      API Page search by name, keep only confident matches.
4. Batch resolved Page IDs into groups of 10, call ads_archive with search_page_ids for each
   batch, ad_type=ALL, ad_reached_countries=["US"].
5. Normalize and store every returned ad (Section 5), tagging each with the market key and
   fetch timestamp.
6. Compute market-level aggregates (competitor count, offer patterns, longest-running ad,
   run-length distribution) and hand to the LLM summarizer (Section 6).
7. Cache the result under the market key with the TTL from Section 4.
8. If Stage 3 resolves zero or near-zero Pages, or Stage 4 returns zero ads across all
   resolved Pages, mark the market "no signal" and route to the fallback (Section 8) instead
   of showing an empty competitive read.
```

This algorithm's accuracy ceiling is set by Stage A, the directory resolution step, not by
the Ad Library API itself. That is worth flagging to the founder directly: the API is the
easy 20%, resolving real local competitor Pages is the hard 80%.

## 4. Rate limits and caching

**Limits.** `ads_archive` runs under the Graph API's general Business Use Case rate limiting.
Current third-party integration guides converge on roughly 200 calls per hour per token for
standard access, with a rolling one-hour window; Meta's own rate-limiting overview documents
the mechanism (throttling on breach) without publishing a fixed ads_archive-specific number in
the page fetched for this spec, so treat 200/hour as a working assumption to build headroom
against, not a contractual ceiling. ([developers.facebook.com/docs/graph-api/overview/rate-limiting](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/))

**On breach.** Requests fail with a Graph API error (reports cite codes in the 80000-range
family, e.g. "There have been too many calls to this Page account. Wait a bit and try
again."). The response's usage headers report estimated time to regain access. Treat this as
a hard stop, not a retry-immediately condition: back off per the header, alert if it recurs.

**Caching strategy.** Competitor ad creative changes slowly, on the order of weeks, and the
Stage A/B pipeline above is the expensive part, not the API call itself. Design the cache
around the market, not the customer, so every business of the same trade in the same metro
shares one fetch:

- **Cache key**: `(trade, geography-bucket)`, where the geography bucket is a coarsened
  grouping (for example, a rounded lat/lng cell or metro name) so that two HVAC contractors
  three miles apart in Austin resolve to the same market and share one Stage A/B run, rather
  than each customer triggering an independent competitor search.
- **TTL: 14 days** for a market with active data. Ad creative for local trades companies is
  not a fast-moving category; a two-week-old read is still directionally correct, and this
  keeps monthly API and directory-lookup volume low even at hundreds of customers.
- **TTL: 3 days** for a market that returned "no signal" (Section 3, step 8), so a genuinely
  under-advertised metro gets rechecked reasonably often without hammering the directory
  lookup on every page view.
- **Manual bypass**: allow a forced refresh from an internal admin action only, never
  customer-triggered, to avoid a customer's page-load accidentally burning the rate budget.
- **Sharing math**: at 200 calls/hour and one call per ten resolved Pages, a metro with 40
  competitor Pages costs 4 calls per refresh; refreshing weekly across, say, 50 distinct
  metro/trade markets is trivially inside quota. The real cost driver is Stage A directory
  lookups, which are outside the Ad Library API's own limits and should be budgeted and
  cached independently.

## 5. Data model

Read `~/Projects/ignition/src/db/schema.ts` conventions: `pgTable`, `text` primary keys via
`$defaultFn(createId)`, `jsonb` with `.$type<...>()`, `pgEnum` for status fields, explicit
`index`/`uniqueIndex`, `organizationId`/`businessId` scoping, `timestamp` audit columns. The
tables below follow that pattern exactly and would live alongside `businesses` and
`campaigns` in the same file.

**`ad_library_markets`** - the cache unit, one row per `(trade, geography-bucket)`, shared
across every business that falls in it. Columns: `id`, `marketKey` (unique text, e.g.
`"hvac|austin-tx"`), `trade`, `city`, `region`, `countryCode`, `latitude`, `longitude`,
`radiusMiles`, `status` (`pgEnum`: `fresh`, `stale`, `no_signal`, `error`), `competitorPageCount`
(int, from Stage A), `adCount` (int, from Stage B), `lastFetchedAt`, `nextRefreshAt`,
`createdAt`, `updatedAt`. Index on `marketKey` (unique) and on `(trade, status)`.

**`ad_library_ads`** - normalized individual ads returned from `ads_archive`, scoped to a
market. Columns: `id`, `marketId` (references `ad_library_markets`, cascade), `metaAdArchiveId`
(unique text, Meta's own archive ID), `pageId`, `pageName`, `creativeBodies` (jsonb
`string[]`, since an ad can have multiple text variants), `linkTitle`, `linkDescription`,
`imageUrls` (jsonb `string[]`), `videoUrls` (jsonb `string[]`), `callToActionText`,
`publisherPlatforms` (jsonb `string[]`: facebook, instagram, etc.), `adDeliveryStartTime`
(timestamp), `adDeliveryStopTime` (timestamp, nullable, null means still running),
`daysRunning` (int, computed at fetch time), `spendRangeJson` / `impressionsRangeJson`
(jsonb, nullable, populated only in the rare EU/UK-reach case, kept for schema honesty rather
than deleted), `rawPayload` (jsonb, the full API response for audit and reprocessing),
`fetchedAt`, `createdAt`. Index on `marketId`, unique index on `metaAdArchiveId`.

**`competitive_reads`** - the customer-facing artifact record, one per business (refreshed,
not per-campaign-duplicated, though it can be regenerated alongside a campaign). Columns:
`id`, `organizationId`, `businessId` (references `businesses`, cascade), `campaignId`
(references `campaigns`, nullable, set null on delete), `marketId` (references
`ad_library_markets`, nullable, null when degraded/no data), `status` (`pgEnum`: `ready`,
`degraded_no_ads`, `degraded_no_pages_resolved`, `degraded_api_error`), `competitorCount`
(int), `summary` (text, the LLM-written plain-English paragraph), `insights` (jsonb,
structured: top offers seen, longest-running ad reference, run-length distribution, an
explicit "nobody is saying X" gap list), `sourceAdIds` (jsonb `string[]`, the
`ad_library_ads.id` values the summary was built from, for traceability), `generatedAt`,
`createdAt`, `updatedAt`. Index on `(businessId, generatedAt)`.

This keeps the expensive, shared data (`ad_library_markets`, `ad_library_ads`) fully separate
from the cheap, per-customer artifact (`competitive_reads`), which is what makes the caching
strategy in Section 4 actually work: many businesses' `competitive_reads` rows can point at
the same `ad_library_markets` row.

## 6. The customer-facing artifact

Never show raw API output; a contractor does not want a JSON dump of ad archive IDs. What
`docs/09-SIX-PS.md`-style plain-spoken output looks like, built from the `insights` jsonb
above:

- **How many competitors are even advertising.** "3 of the 14 HVAC companies near you are
  running Facebook ads right now." This number alone is often the whole sales hook: either it
  says "everyone's doing this but you," or "almost nobody's doing this, here's your opening."
- **What offers they're running**, extracted and normalized, not pasted verbatim: "$49 AC
  tune-up," "free second opinion on a quote," "$500 off a new system." Group near-duplicates.
- **How long ads have been live**, the single most useful signal in the whole feature. An ad
  running for 60+ days is very likely a working ad. Surface it directly: "One competitor has
  run the same tune-up offer for 71 days. That means it's working for them." Use
  `adDeliveryStartTime` to `now` (or to `adDeliveryStopTime` if it has stopped) as
  `daysRunning`, and call out the single longest-running active ad as the anchor insight.
- **What nobody is saying that this owner could say.** This is the LLM's real job, not a
  literal API field: compare the set of offers/angles present across competitor ads against
  the trade's known-converting offer patterns (already used elsewhere in the product for offer
  suggestions per `docs/01-PRODUCT-SPEC.md`), and name a specific gap. "None of your local
  competitors mention emergency after-hours service in their ads. You take those calls; say
  so."
- **Where the LLM summarizes vs. dumps.** The LLM receives only the normalized, aggregated
  `insights` structure (offer clusters, run-length stats, platform mix, gap candidates) built
  deterministically in code from `ad_library_ads`, never the raw API payload and never
  unbounded free text, and its output is one short paragraph plus the specific callouts above.
  This keeps the summarization step cheap, auditable, and impossible to prompt-inject via ad
  copy text scraped from a competitor's page, consistent with Inviolable Rule 4 (untrusted
  input) even though the untrusted text here is a competitor's, not the customer's.
- **What it explicitly does not show**: spend, impressions, or reach numbers, because for the
  US commercial case those fields are not populated (Section 2) and Inviolable Rule 3 bans
  fabricated statistics on any user-facing surface. Do not estimate spend from ad count or
  run length; say what is known and stop.

## 7. Legal and ethical boundaries

- **The data is public by Meta's own design.** The Ad Library exists specifically for
  transparency and public research into advertising; Meta's own materials describe it as
  built "for researchers, academics, journalists and the public." Displaying what a
  competitor is publicly advertising, sourced through Meta's own transparency tool, is
  materially different from scraping private data.
- **Do not scrape the public Ad Library website as a substitute for the API.** Section 3
  names the public site only as a manual, human-driven fallback. Automated scraping of
  `facebook.com/ads/library` would sit outside the terms that govern the API and outside this
  spec's recommended path; if the product ever needs that data, it must come through the API
  or a Meta-provided export, not a scraper.
- **Attribution and identity.** Ads returned by the API already carry the advertiser's own
  Page name and Page ID, information the advertiser itself chose to make public by running
  the ad. Showing a competitor's business name and their own ad creative back to another
  local business in the same trade is showing them their own public advertising, not
  disclosing anything Meta or the advertiser treated as private. This is materially different
  from, for example, screen-scraping a competitor's private ad-account dashboard, which this
  product never does and never could (Inviolable Rule 2).
- **Storage.** Store only the fields the API itself returns (Section 5); do not enrich with
  data from other sources about the competitor without separately verifying that source's own
  terms. Retention should track Meta's own archive retention logic loosely (ads age out of
  relevance quickly in this feature anyway per the 14-day TTL in Section 4), and stale
  `ad_library_ads` rows should be prunable without harming `competitive_reads`, which stores
  its own summary text independent of the source rows still existing.
- **What this spec could not fully verify**: Meta's Ad Library API Terms of Service govern
  redistribution and commercial use of the data in detail (rate limits on republishing,
  restrictions on using the data to build a competing ad-transparency product, etc.). Those
  terms should be read in full and signed off on by the founder before this feature ships,
  since they were not directly fetchable during this research pass; treat that as an open
  action item, not a settled fact.

## 8. Fallback, never an empty box

Per the algorithm in Section 3, a market lands in a degraded state when Stage A resolves too
few competitor Pages, or Stage B returns zero ads across all resolved Pages, or the API itself
errors (token expired, rate-limited). Each maps to a specific, still-useful message rather
than a blank panel:

- **`degraded_no_pages_resolved`** (directory lookup found few or no competitor Pages): "We
  couldn't confidently identify other {trade} companies advertising near {city} yet. That
  usually means this is a lighter-competition market, which can be good news." Still ship the
  generated plan and ads; this section becomes a short note, not a hole in the page.
- **`degraded_no_ads`** (Pages resolved, but none have active or recent ads): "None of the
  {N} {trade} companies we checked near {city} appear to be running Facebook or Instagram ads
  right now." This is itself the insight (an open competitive lane), and should be framed as
  one, using the real `competitorPageCount` from Stage A.
- **`degraded_api_error`** (token/rate-limit failure): never surface a raw error to the
  customer. Show the same graceful copy as `degraded_no_pages_resolved`, log the real cause
  internally, and let the health monitor from Section 1 alert the founder. The customer should
  never see evidence that our own integration broke.
- In all degraded states, the rest of the generated output (marketing plan, ads, export pack)
  ships in full. Per the pivot decision in `docs/01-PRODUCT-SPEC.md`, the product must deliver
  complete value even when this one section has nothing to show.

## 9. Feasibility verdict

**Yellow.** Not Green, because the feature as described in `AGENTS.md` ("show them what other
contractors in their service area are currently advertising") cannot be delivered by a
straightforward keyword/geo search against the Ad Library API; the coverage wall in Section 2
is real, current, and confirmed against Meta's own endpoint reference. Not Red, because a
real, honest version of the feature survives through the Page-resolution pipeline in Section
3: identify likely local competitor Pages through an independent directory step, then query
the Ad Library API per-Page, which is not blocked by the political/EU gate. That pipeline is
more engineering than the founder's mental model assumed (a directory-resolution stage,
matching, and a two-stage cache), and its output will sometimes be thin or empty for a given
metro and trade, which is exactly why Section 8's fallback is not optional polish but a
required part of the feature.

If Stage A directory resolution proves unreliable in practice (low match confidence between
directory listings and Facebook Pages), the closest viable fallback within the same access
model is to narrow the promise: instead of "what competitors near you are running," ship
"what {trade} companies are running nationally right now" using open keyword search filtered
to ads that happen to satisfy the EU/political gate or are self-reported by page name search,
explicitly framed as national pattern-matching rather than hyperlocal competitive
intelligence. That is a materially weaker but still honest claim, and should only be adopted
if Stage A's real-world match rate, measured against the first design-partner metros, comes
in too low to support the local claim.

## Sources

- [Meta Ad Library API landing page](https://www.facebook.com/ads/library/api)
- [Graph API reference: ads_archive](https://developers.facebook.com/docs/graph-api/reference/ads_archive/)
- [Meta Transparency Center: Ad Library tools](https://transparency.meta.com/researchtools/ad-library-tools)
- [Meta Business Help Centre: About ads about social issues, elections or politics](https://www.facebook.com/business/help/167836590566506)
- [Facebook Login: access tokens guide](https://developers.facebook.com/docs/facebook-login/guides/access-tokens/)
- [Graph API rate limiting overview](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/)

---

## OPERATOR NOTE, verified 2026-08-19: web interface vs API

While building the ad copy playbook (`docs/17-AD-COPY-PLAYBOOK.md`), an agent browsed the
Meta Ad Library **web interface** and successfully retrieved 46 live US commercial ads from
HVAC, plumbing, roofing, and electrical contractors, with full creative, headlines, run
dates, and Library IDs.

The operator independently confirmed one of them. Library ID `692268871996677`, Global
International Heating And Cooling Co, still active, started running 2022-05-24, headline
"$59 A/C Tuneup". Exact match to the agent's entry.

**This does not contradict the API finding above; it clarifies it.**

- The **web interface** at `facebook.com/ads/library` serves US commercial ads and is
  searchable by advertiser name.
- The **API** restricts *open keyword and geographic search* on commercial ads, which is why
  a query like "HVAC companies within 25 miles of Austin" returns nothing.
- The **`search_page_ids` API endpoint** is not subject to that gate, which is exactly why
  the two-stage pipeline works: resolve competitor Pages first, then query by Page ID.

**This raises confidence in the competitive read.** Once we can resolve a contractor's local
competitor Pages, the ad data behind them is real, current, and rich. The feasibility rating
stays YELLOW only because directory resolution is still an unbuilt engineering stage, not
because the underlying data is thin. It is not thin.

Practical consequence: the web interface is a usable manual research tool today, with no
token and no verification. Use it to sanity-check a metro before building the automated path.
