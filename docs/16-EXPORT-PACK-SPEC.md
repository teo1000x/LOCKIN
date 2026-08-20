# Export Pack Spec

> This is the highest-risk deliverable in the project. The product generates a campaign but
> does not publish it. If the owner cannot take our output and build it in Meta Ads Manager
> alone, the product has failed regardless of how good the generated ads are. Read
> `AGENTS.md` and the PIVOT section of `docs/01-PRODUCT-SPEC.md` before touching this file -
> this spec implements Model A, the export/handoff model, made permanent.

---

## 0. Research method and a caution about sources

Meta changes Ads Manager's screens, field names, and flow order on a rolling basis - even
within 2026 there was a reported campaign-creation flow change in February and a billing
system change in April. Most of what is publicly written about "the current Ads Manager UI"
comes from marketing agency blogs, not Meta's own documentation, and those blogs republish
stale screenshots under fresh dates. I could not get Meta's own Business Help Center pages to
render through automated fetch (they are JavaScript-rendered and returned only page titles),
so the click path below is reconstructed from multiple third-party walkthroughs that agree
with each other on sequence and field names, cross-checked against Meta's help-center article
titles and known 2026 platform changes (the Advantage+/manual flow merge, the April 2026
billing overhaul, the Conversions API requirement for the "conversion leads" goal).

**Operational consequence for this product, not just this document:** the exact screen text
in the export pack must be re-verified against the live Ads Manager UI on a recurring
schedule (recommend monthly, or triggered by a support ticket that says "I don't see that
button"). Treat every screen name and button label below as correct as of this writing and
liable to drift. Section 8 specifies how the product detects and absorbs that drift without
the founder rewriting the pack by hand every time Meta ships a redesign.

Sources are cited inline per claim below.

---

## 1. The click path: opening Ads Manager to a live campaign

### 1.1 Prerequisite: a Meta Business Account (not a personal profile)

A Facebook ad cannot run from a personal profile. The account must have a Facebook Page
(the public-facing business identity) and a Meta Business Account, sometimes labeled
Business Portfolio (the backend that holds the Page, the ad account, and permissions). Using
a personal profile to represent a business is against Facebook's Terms and risks the personal
account being locked. [Netplanet Digital](https://netplanetdigital.com.au/how-to-create-a-facebook-business-page-and-portfolio/),
[Leadsie](https://www.leadsie.com/blog/how-to-create-meta-business-manager-and-facebook-ad-account)

If the owner has neither:
1. Go to `business.facebook.com`, click **Create Account**.
2. Log in with a personal Facebook login (required as the human identity behind the
   business account - this does not mean the ads run from that personal profile).
3. Enter the business's legal or trading name, the Business Portfolio name, and a business
   email address, then **Create**.
4. When prompted, select or create the Facebook Page for the business. If no Page exists
   yet, it is created here.
5. Fill in business details: email, phone, physical address.
6. Add a profile photo and cover image for the Page (logo and a real photo of the shop,
   truck, or crew - not a placeholder).
[Superchat](https://help.superchat.com/en/articles/14980-how-to-create-your-meta-business-account),
[Leadsie](https://www.leadsie.com/blog/how-to-create-meta-business-manager-and-facebook-ad-account)

### 1.2 Prerequisite: an ad account with a payment method

Inside Business Settings, an ad account must exist under the Business Portfolio, and it needs
a payment method before any campaign can spend money. As of April 1, 2026, Meta stopped
accepting credit cards as the primary payment method for higher-spend accounts and requires
either monthly invoicing (a credit line requiring a business tax ID and bank details, 24-48
hour approval) or direct debit from a bank account. A five-day read-only lockout on billing
settings occurred around the March 30 to April 4, 2026 transition window; that window has
passed by the time this pack is used, but the underlying requirement (no bare credit card on
file for accounts above Meta's threshold) persists. Confirm current requirements at
Ads Manager > Billing & Payments before advising a specific path.
[Adamigo](https://www.adamigo.ai/blog/meta-ads-billing-change-2026-credit-cards-removed-accounts-guide),
[Meta Business Help Center - Add a Payment Method](https://www.facebook.com/business/help/132073386867900)

### 1.3 Campaign level

1. In Ads Manager, click the green **Create** button.
2. Choose **Leads** as the campaign objective (not "Lead Generation" - Meta's current
   objective picker uses the shorter label).
3. Name the campaign. Use a name the owner will recognize on a busy screen six months from
   now, not a generic one - see Section 4 for the exact naming convention our export pack
   supplies.
4. Decide Advantage+ campaign budget on or off. Meta's 2026 unified flow enables AI-driven
   budget, audience, and placement optimization by default, with each one individually
   toggleable. Advantage+ leads campaigns have shown materially lower cost per lead in
   reported benchmarks (14 percent lower cost per lead, 10 percent lower cost per qualified
   lead versus manual setups; one franchise case cited 36 percent lower cost per lead and 53
   percent more leads). Our default recommendation: leave Advantage+ on for budget and
   placements, keep manual control on audience geography only (see Section 1.5) - the owner
   is not equipped to second-guess Meta's delivery algorithm, but they are the only one who
   knows their real service radius.
   [1clickreport](https://www.1clickreport.com/blog/meta-advantage-plus-campaign-setup-2026),
   [Marketing Agent Blog](https://marketingagent.blog/2026/05/06/the-complete-roadmap-to-using-meta-advantage-in-2026/)
5. If prompted, answer the Special Ad Category question (see Section 2.5 - this is a stop
   point, not a skip point).
6. Click **Next**.

### 1.4 Ad set level

7. Name the ad set.
8. Choose **Conversion location**: select **Instant Forms**. Other options on this screen
   (Website, Calls, Messenger, Instagram, WhatsApp, App) are not what our export pack builds
   toward for v1 - the pack tells the owner to pick Instant Forms explicitly, because the
   default selection on this screen is not reliably Instant Forms.
9. **Performance goal**: leave on "Maximize number of leads" unless our export pack
   specifically instructs otherwise. ("Maximize number of conversion leads" requires
   Conversions API integration, which this product does not set up - never recommend it.)
10. Confirm the Facebook Page selected matches the business (this matters more than it
    sounds - accounts with access to multiple Pages have shipped ads under the wrong
    business identity).
11. **Budget and schedule**: enter the daily budget our software recommended, and start
    date. Leave end date open-ended unless the owner specifically wants a fixed run, because
    lead-gen campaigns need a learning period Meta will not get through on a short fixed run.
12. **Audience**: enter the geography (address plus radius, or explicit city/ZIP list) and
    any exclusions exactly as configured in our intake wizard. Age minimum defaults to 18.
    Leave Advantage+ audience on for interest/demographic expansion beyond geography unless
    Special Ad Category restrictions apply (see 2.5).
13. **Placements**: leave on Advantage+ placements (automatic). Manual placement selection is
    a targeting decision the owner has no basis to make and our product does not generate
    placement-specific creative variants for v1.
14. Click **Next**.

### 1.5 Ad level

15. Name the ad (our export pack supplies this name - see Section 4).
16. Confirm Page and, if used, Instagram account identity.
17. The first time a Page runs lead ads, Meta requires a one-time acceptance of Lead Ads
    Terms of Service on this screen. This is a stop point (Section 2).
18. Choose creative format: single image (this product's v1 creative output).
19. Upload the image file (Section 5 covers exactly which file).
20. Enter primary text, headline, and description in their respective fields.
21. Choose the call-to-action button from Meta's fixed list (e.g., "Get Quote," "Sign Up,"
    "Learn More," "Call Now"). Our export pack specifies exactly which CTA button label to
    pick, because the visible options do not always match our software's internal wording.
[Multiple sources cross-checked: AdsUploader step guides](https://adsuploader.com/blog/how-to-create-facebook-lead-ads),
[LeadSync](https://leadsync.me/blog/create-facebook-lead-ad-campaign/)

### 1.6 The instant form builder

22. Click **Create Form** (or select a previously created form - first-time users always
    create new).
23. Select form type. Meta's current builder offers **More Volume**, **Higher Intent**, and
    **Rich Creative**. Our default recommendation is **More Volume** for trades lead gen -
    fewer taps to submit, and lead quality is controlled by qualifying questions rather than
    friction. Note the reach caveat: Higher Intent only serves on mobile feeds, Rich Creative
    only inside the Facebook app - both narrow delivery in ways a first campaign should not
    absorb.
24. **Intro screen**: headline and description (our pack supplies exact copy).
25. **Questions screen**: prefilled contact fields (name, email, phone - Meta auto-fills
    these from the user's profile) plus our software's custom qualifying questions, added in
    the exact order specified in Section 6.
26. **Privacy policy screen**: paste the business's privacy policy URL. If the business has
    none, this is a hard stop (Section 2) - Meta will not let the form save without it.
27. **Thank-you screen**: confirmation headline, description, and either a link or a phone
    number as the closing CTA.
28. Test the form using Meta's built-in test tool before finishing, then click **Finish** /
    **Save**.

Critical constraint for the export pack and for support load: **a published instant form
cannot be edited.** Once it is attached to a live ad, changes require duplicating the form,
editing the copy, and reattaching the new version to the ad. Our export pack must say this
explicitly before the owner publishes, not after they discover it.
[AdsUploader - Facebook Instant Form](https://adsuploader.com/blog/facebook-instant-form)

### 1.7 Publish

29. Review the ad preview panel on the right side of the screen against our pack's
    reference screenshot (Section 7).
30. Click **Publish**.
31. The campaign enters Meta's review queue. Typical review time is under 24 hours; it can
    run longer. The campaign will not spend money or show to anyone until it clears review.
[SaveMyLeads timing estimate](https://savemyleads.com/blog/other/how-long-does-it-take-to-learn-facebook-ads),
general beginner-setup-time sources cross-checked above.

---

## 2. Every place a non-technical person gets stuck

Each entry: the symptom as the owner will describe it, the actual cause, and the fix our
export pack must pre-empt or resolve.

**2.1 "It's asking me to make a Page but I already have a business on Facebook."**
Cause: they have a personal profile with the business name, not a Page. A personal profile
cannot run ads. Fix: our pack includes a one-screen decision test ("do you see a blue Follow
button or a green Message button on your business's Facebook presence - Follow means it's
already a Page, Message-only likely means a personal profile") and the Page-creation steps
from 1.1 as a branch, not an afterthought.
[Netplanet Digital](https://netplanetdigital.com.au/how-to-create-a-facebook-business-page-and-portfolio/)

**2.2 "It won't let me publish, something about payment."**
Cause: no valid payment method on the ad account, or the account fell into Meta's April 2026
invoicing/direct-debit requirement and a stored card silently stopped being accepted. Fix:
direct link to Ads Manager > Billing & Payments plus the specific current requirement
(monthly invoicing needs a business tax ID and banking details; approval takes 24-48 hours,
so this cannot be resolved same-night if the owner is doing this at 8pm the night before they
want ads live - our pack must say this up front, not discover it at step 29).
[Adamigo](https://www.adamigo.ai/blog/meta-ads-billing-change-2026-credit-cards-removed-accounts-guide)

**2.3 "It's asking me for a code from my phone and I don't know why."**
Cause: two-factor authentication enforcement at the Business Portfolio level, which cascades
to every admin's personal Facebook login. This is often triggered automatically by Meta's
fraud-prevention systems, not something the owner turned on. Fix: pack includes a short
"what this screen is and why" note plus a link to Facebook's own 2FA setup, since we cannot
and should not touch their login credentials (see Inviolable Rule 2 in AGENTS.md - we never
touch customer credentials, and 2FA setup is exactly that boundary).
[Vivid Image](https://vimm.com/how-to-setup-two-factor-authentication-on-facebook/)

**2.4 "I don't see 'Create' or it looks completely different from the screenshot."**
Cause: Meta UI drift between when we wrote the pack and when the owner opens Ads Manager.
This is a certainty, not a risk. Fix: Section 8 - a live, versioned instruction source rather
than a static PDF, plus a "does this not match what you see" escape hatch on every screen of
the pack that leads to a support path, not a dead end.

**2.5 "It's asking if this is about housing, employment, or credit and I don't know what to
pick."**
Cause: the Special Ad Category prompt, mandatory on every campaign since it governs targeting
restrictions (no age, gender, ZIP, or many interest-based targeting options once flagged).
Most trades (HVAC, plumbing, roofing, electrical) are correctly "None," but anything touching
financing offers, property management, or staffing may not be. Fix: our software must
determine this classification during intake (per Guardrail 1 in `docs/01-PRODUCT-SPEC.md`)
and the export pack states the exact answer to give on this screen - the owner should never
be making this legal-adjacent judgment call live in Ads Manager.
[Jon Loomer - Special Ad Categories](https://www.jonloomer.com/special-ad-categories-meta-ads/)

**2.6 "The account spending limit thing - what number do I put?"**
Cause: confusing the account-level lifetime Spending Limit (a safety cap across all campaigns
that pauses everything at 100 percent) with the ad set's daily/lifetime Budget (what actually
paces spend day to day). These are two different settings on two different screens and the
names are similar enough to cause real confusion. Fix: pack explains both terms with the
plain distinction ("Budget is what you spend per day. Spending Limit is a stop-everything
safety net across your whole account - set it once, higher than you think you need, and
forget it") and gives the exact daily budget number, never a range, so there is no
in-the-moment math.
[Orbee - Ad Account Spending Limit](https://kb.orbee.com/meta-ads-spending-limit)

**2.7 "The form builder has a million options and I don't know what any of them do."**
Cause: the instant form builder exposes form type (three options with different reach
implications), five question types, conditional logic, and screens most first-time users have
never seen before, with post-publish edits locked. Fix: Section 6 below - our pack turns this
into a fill-in-the-blank sequence with no live decisions left for the owner to make, because
this is empirically the single most confusing screen in the entire flow.
[AdsUploader](https://adsuploader.com/blog/facebook-instant-form)

**2.8 "My image got rejected" or "it looks cropped weird."**
Cause: uploading a single image sized for one placement (e.g., a square 1:1) into a flow that
also serves Stories/Reels placements (9:16), producing a cropped, awkward result rather than
an outright rejection - the old 20 percent text-overlay hard rejection was retired in 2020 and
no longer applies, but heavy text still measurably hurts delivery under Meta's algorithmic
ranking. Fix: Section 5 - exact file per placement, named so there is no ambiguity about which
file goes where, and a text-density check performed by our software before export, not left
to the owner to judge in Ads Manager.
[Orbee - 20% Rule](https://kb.orbee.com/meta-20-rule),
[NealSchaffer](https://nealschaffer.com/facebook-ads-text-rule-change/)

**2.9 "It says I need admin access to the Page and I don't know if I have it."**
Cause: Meta's 2026 Page Access system replaced the old Page Roles system, and after May 20,
2026, anyone with legacy Page access was auto-migrated into the Business Portfolio at "basic
access," which is not sufficient to publish ads. Fix: pack includes a specific check ("go to
Business Settings > People, find your name, confirm it says Admin - if it says anything else,
that is why you're stuck") before the owner reaches the ad-creation screens, not after a
failed publish.
[Creatifbd - Facebook Page Access 2026](https://creatifbd.com/facebook-page-access-2026-guide/),
[3-Prime - Meta Page Access Update](https://www.3-prime.com/2026/04/meta-is-updating-page-access-what-businesses-need-to-know-before-may-20-2026/)

**2.10 "I can't edit the form, I already published it."**
Cause: instant forms lock permanently on publish - this is by design on Meta's side, not a
bug. Fix: pre-publish warning at step 28 (Section 1.6) is mandatory, worded plainly: "Once you
publish, this form is locked forever. Check it against the checklist in Section 7 before you
click Publish, not after."

---

## 3. Recommended pack format

**Primary format: a web page, not a PDF.** Specifically, a private, versioned link (one per
generated campaign) hosted by our own product, opened on the owner's phone or laptop while
Ads Manager is open in a second tab or the next browser tab over.

Reasoning, weighed against the alternatives:

- **PDF.** Fails on the exact failure mode this document exists to prevent: it goes stale the
  moment Meta reorders a screen, it cannot offer live copy-paste (see Section 4), and a
  contractor working at 8pm on a laptop has to alt-tab between a static document and a
  changing web app with no way to check off progress. A PDF is also unfixable after Meta
  drifts without us re-issuing every customer's file.
- **Annotated screenshots alone.** Necessary as a supplement (Section 7's verification
  checklist needs them) but insufficient alone, because screenshots are the single most
  fragile artifact against UI drift and give the owner nothing to click.
- **A short video.** Good for building confidence before starting, bad as the primary
  reference during the task itself - nobody scrubs a video back and forth forty times while
  filling in eleven form fields, and video cannot offer copy-paste. Recommend a single
  60-90 second orientation video embedded at the top of the web page, not as the primary
  vehicle.
- **A live checklist web page with per-field copy-paste blocks and embedded reference
  screenshots at each step, plus the short orientation video at the top.** This is the
  combination recommended. It survives Meta UI drift better than any static format (the page
  itself can be updated centrally without touching past customers' data), it supports one-tap
  copy for every field (Section 4), it lets the owner check off each of the ~30 steps in
  Section 1 so they always know where they are if they get interrupted mid-task (a real
  scenario for a contractor doing this between jobs or at night), and it degrades gracefully
  on a phone if they start there before moving to a laptop.

A downloadable PDF/image bundle is still offered, but as a secondary export ("download
everything" button) for the owner's own records and for the image files themselves, which
must be real downloadable files regardless of the primary format.

---

## 4. The copy-paste problem

Every field the owner has to type or paste into Ads Manager must be reproducible with zero
transcription error. Specification:

- **One-click copy per field, not per section.** Every individual value that goes into a
  distinct Ads Manager field (campaign name, ad set name, ad name, primary text, headline,
  description, form intro headline, form intro description, each qualifying question, privacy
  policy URL, thank-you headline, thank-you description) gets its own copy button on the
  export page, positioned directly next to a label that names the exact Ads Manager field it
  belongs to and the step number from Section 1 where it is used. Never a single block of text
  the owner has to manually split.
- **Field labels on our page must match Meta's field labels, not our internal names.** If our
  database calls something `primary_text`, the export page must show the label "Primary text"
  (the literal string on the Ads Manager screen), because the owner is pattern-matching by
  sight, not by data model.
- **Naming convention, applied automatically, never typed by the owner:**
  `{Business short name} - {Campaign type} - {Month YYYY}` for the campaign,
  `{Business short name} - {Geography or audience} - {Month YYYY}` for the ad set,
  `{Business short name} - {Ad variant label, e.g. "Offer A"} - {Month YYYY}` for each ad.
  These names are generated by our software and shown pre-filled with their own copy button;
  the owner never invents a name, because inconsistent naming is what makes an account
  unmanageable six months later and is not a decision a first-timer should be making.
- **A downloadable bundle** (zip or single PDF) containing every field value in the same
  order as Section 1's steps, as a backup for an owner who prefers printing this out or who
  loses their place in the web flow. This is the fallback path, not the primary path, per
  Section 3.
- **No field ships to the owner with placeholder or lorem-ipsum text.** Every field is either
  the AI-generated real content or explicitly flagged as needing the owner's own input (e.g.,
  privacy policy URL if their software cannot supply one) before the pack is considered
  complete. Ties to Inviolable Rule 1 - nothing exports without an approval record, and
  nothing in that approval record should be a stand-in value.

---

## 5. Image handoff

**Required files, sized per current placement groups** (dimensions cross-checked across
multiple 2026 spec sources):
[Hootsuite](https://blog.hootsuite.com/facebook-ad-sizes/),
[TheOptimizer](https://theoptimizer.io/blog/every-meta-ad-size-you-need-in-2026-dimensions-formats-and-placements-complete-guide),
[Superscale](https://superscale.ai/learn/meta-ad-sizes)

| Placement group | Aspect ratio | Pixel dimensions | Notes |
|---|---|---|---|
| Feed (Facebook and Instagram) | 4:5 | 1080 x 1350 | Meta's recommended feed ratio, takes ~25% more mobile screen than square |
| Universal / all-placement fallback | 1:1 | 1080 x 1080 | Crops predictably everywhere; use if only one file will be supplied |
| Stories and Reels | 9:16 | 1080 x 1920 | Only ratio that fills the screen; required if Reels/Stories placements are left on under Advantage+ placements |

File requirements: JPG or PNG, under 30 MB.
[Superscale](https://superscale.ai/learn/meta-ad-sizes)

**Our export pack ships two files per ad variant by default: the 1:1 universal file and the
9:16 Stories/Reels file**, because Advantage+ placements (recommended default, Section 1.4
step 13) serves across both groups automatically, and a 1:1-only upload gets awkwardly
cropped in Stories/Reels rather than rejected outright - a quality problem, not an error
message, which makes it worse because nothing tells the owner it happened.

**File naming**: `{BusinessShortName}_{AdVariantLabel}_{AspectRatio}.jpg`, e.g.
`AcmeHVAC_OfferA_1x1.jpg` and `AcmeHVAC_OfferA_9x16.jpg`. The export page shows each file
next to the exact ad variant it belongs to and the exact upload step number, so there is never
a moment where the owner is guessing which of several downloaded images goes with which ad.

**Text-overlay and quality checks, performed by our software before export, not left to the
owner:**
- Meta's hard 20 percent text-overlay rejection was retired in 2020 and does not apply in
  2026, but text-heavy images still measurably underperform under Meta's algorithmic delivery
  ranking. Our generation pipeline should flag and warn (not silently block) any image where
  text coverage exceeds roughly one-third of the frame, and the export pack never ships an
  image the owner has not already seen flagged in-app during the approval step.
  [Orbee](https://kb.orbee.com/meta-20-rule), [NealSchaffer](https://nealschaffer.com/facebook-ads-text-rule-change/)
- Minimum resolution enforced at generation time so nothing shipped to the export pack is
  below Meta's recommended pixel dimensions - never let the owner discover a blurry image
  after publish.

---

## 6. The instant form handoff, field by field

Our software designs the form; the owner builds it in Meta's form builder by hand (Meta does
not accept a form import from outside its own tools for standard advertisers). The export
pack must therefore present the form content in **the exact order Meta's builder presents its
screens**, so the owner is never scrolling our page hunting for the next value while sitting
on a live Meta screen. Per Section 1.6:

1. **Form type**: pack states "More Volume" as the selection to make, with a one-sentence
   plain-English reason ("More Volume gets you more leads per dollar for a first campaign -
   the other two options trade volume for a narrower audience you don't need yet").
2. **Intro headline** - copy-paste block.
3. **Intro description** - copy-paste block.
4. **Prefilled contact fields to select**: pack states exactly which of name/email/phone to
   turn on (default: all three, since Meta prefills these automatically from the user's
   profile and turning them off only adds friction).
5. **Custom qualifying questions**, in the exact order to add them, each as its own
   copy-paste block with its answer type stated ("Multiple choice" or "Short answer") because
   the owner has to select the type in a dropdown before the question text field even appears
   - stating the type up front avoids a dead-end where they paste text into the wrong widget.
6. **Privacy policy URL** - copy-paste block, or a flagged blocker if the business has none
   (see Section 8 - this is one of the few true hard stops).
7. **Thank-you screen headline** - copy-paste block.
8. **Thank-you screen description** - copy-paste block.
9. **Thank-you screen button/phone number** - exact value and which of the two options to
   pick.
10. An explicit line, placed immediately before the "click Finish" instruction: **"This form
    cannot be edited once it goes live. Check every field above against what you just typed
    before you continue."**

---

## 7. Verification checklist, before spending money

Presented as the final section of the export page, checked off in this order, with a plain
statement of what "correct" looks like at each line - never just "check this," always "here
is what right looks like":

1. **Campaign name matches our naming convention** (Section 4) - right: `AcmeHVAC - Leads -
   Aug 2026`. Wrong: "Campaign" or "New Campaign" (Meta's default placeholder, meaning a field
   was skipped).
2. **Objective is Leads, not any other objective** - visible on the campaign-level breadcrumb
   in Ads Manager.
3. **Special Ad Category matches what our software determined** - right: "None" for the vast
   majority of trades; flagged category for anything financing/staffing-adjacent (Section
   2.5).
4. **Conversion location is Instant Forms** - visible on the ad set screen; wrong if it shows
   Website, Calls, or any other location.
5. **Daily budget matches the number our software recommended, exactly** - a mismatch here is
   the single highest-consequence error in the whole checklist, because it directly changes
   spend.
6. **Geography matches the radius or ZIP list from intake** - spot-check the map preview Ads
   Manager shows on the audience screen against the radius the owner specified during intake.
7. **Both images uploaded, correct aspect ratio each** (Section 5) - preview panel should show
   a properly filled frame, not an awkwardly cropped one, in both the feed and Stories preview
   tabs Ads Manager offers.
8. **Ad copy free of placeholder text** - scan primary text, headline, description for
   anything that reads like a template variable or generic filler.
9. **Instant form: every question from Section 6 present, in order, privacy policy URL
   live-tested** (click it in the preview and confirm it opens a real page).
10. **Test lead submitted through Meta's own form-preview tester** and received - if
    it does not show up, the form is not wired correctly and must not go live.
11. **Payment method valid** - Billing & Payments screen shows no error banner.
12. **Only after all eleven are confirmed**: click Publish.

This checklist is the last thing standing between a first-timer and a live ad spending real
money on a possibly-broken setup. It should be impossible to reach the Publish button inside
our export page's flow without having interacted with (not just scrolled past) this list.

---

## 8. The failure path: self-service boundary and support load

The founder is a solo operator. The support model must resolve the large majority of stuck
points without a human, because a support queue that requires the founder personally does not
scale past a handful of customers.

**Design principle: every stuck point in Section 2 gets a specific, numbered answer inside
the product, reachable from the exact step where it occurs - not a general FAQ page the owner
has to search.** Concretely: each step in the export page's checklist (Section 1's ~30 items)
carries an optional "this doesn't match what I see" link that expands an inline answer
specific to that step, pulled from Section 2's catalog. This resolves the highest-frequency
failures (2.1 through 2.10) without any message reaching the founder.

**What stays self-service, permanently:**
- Everything in Section 2 with a deterministic fix (personal profile vs Page, payment method
  location, 2FA explanation, Special Ad Category answer, spending limit vs budget
  distinction, image-placement mismatch, Page access level check).
- Anything where the fix is "go to this exact Meta screen and do this exact thing" - these are
  Meta's own flows and we are only pointing at them.

**What crosses into contacting us, by design, and must be labeled as such rather than left
ambiguous:**
- The export pack's content itself being wrong - wrong offer, wrong geography, an ad the
  owner disapproved of after export. This routes back into our product's edit/regenerate
  flow, not into Ads Manager troubleshooting.
- A Meta screen that does not match this document at all (Section 2.4) - UI drift beyond what
  the inline per-step answers cover. This is the one category that should reach the founder,
  because it is also the signal that the document itself needs updating for every other
  customer, not just this one. Treat every such report as a documentation bug, not a support
  ticket to close and forget - log the reported screen and step number, and treat two or more
  independent reports on the same step as a mandatory pack update, not a coincidence.
- Anything Meta itself has flagged on their account (ad rejected for policy reasons, account
  under review, ad account disabled) - genuinely outside our software's ability to fix, and
  the pack should say plainly "this is a Meta decision, here is Meta's own support path,"
  rather than implying we can resolve it.

**What must never happen:** the export pack silently stopping with no next action. Every dead
end in Section 2 has either an inline fix or an explicit "contact us" path with what
information to include (screenshot of the exact screen, step number from the checklist) so a
single email resolves it instead of a back-and-forth.

---

## 9. Time estimate and drop-off risk

Beginner Facebook ad setup, per cross-checked general sources, runs roughly 30 minutes to 2
hours for the ad-creation portion alone, plus up to 24 hours of Meta review before the
campaign actually goes live.
[SaveMyLeads](https://savemyleads.com/blog/other/how-long-does-it-take-to-learn-facebook-ads),
cross-checked against general beginner setup-time sources found above.

Applied to this specific flow, with our export pack in hand (meaning content is pre-written
and the owner is executing a checklist rather than making decisions):

| Stage | Est. time, first-timer | Drop-off risk |
|---|---|---|
| Business account / Page setup (1.1), if starting from zero | 15-30 min | High - this is the stage most likely to reveal the personal-profile-vs-Page confusion (2.1) and is furthest from any visible payoff |
| Payment method setup (1.2) | 5-20 min, or 24-48 hrs if a credit line application is required (2.2) | High if a credit line is needed - this is the one stage that cannot be finished same-night, and an owner who hits it at 8pm with no warning is the likeliest to abandon entirely |
| Campaign, ad set, ad-level fields (1.3-1.5) | 15-25 min with copy-paste blocks | Moderate - mostly mechanical if the pack's naming and field-matching (Section 4) works as specified; risk concentrates at the Special Ad Category prompt (2.5) if not pre-answered |
| Instant form builder (1.6) | 15-30 min | High - independently confirmed as the most confusing single screen in the flow (2.7); this is where the field-by-field ordering in Section 6 matters most |
| Verification checklist (Section 7) | 5-10 min | Low, but this is also the stage most likely to be skipped under time pressure, which is precisely the stage that exists to prevent an expensive mistake |
| Publish + Meta review | under 1 min to click, up to 24 hrs to clear review | Low for the click itself; moderate anxiety risk during the review wait, since the owner has no visibility into why it's pending - the pack should set this expectation explicitly so a 20-hour wait is not read as a failure |

**Total hands-on time for a returning owner with an existing Business account and payment
method already on file: roughly 30-45 minutes.** For a true first-timer starting from zero,
including account setup and a possible payment-method delay: realistically 45 minutes to 2
hours of hands-on time, potentially spread across two sessions if a credit line application
is required, plus up to 24 hours of Meta's own review queue before the campaign is live.

---

## 10. Honest verdict

**A typical non-technical contractor, alone, at night, on a laptop, following only a static
document: unlikely to complete this successfully on the first try.** The research supports
this plainly rather than optimistically:

- The instant form builder is independently reported as confusing even outside a first-time
  context, with feature availability that shifts depending on where you start building it,
  five question types, and a permanent lock on publish that turns a small mistake into a
  redo rather than an edit.
- Page/Portfolio/personal-profile confusion, payment method changes, two-factor cascades, and
  the 2026 Page Access migration are all real, currently-active failure modes independently
  documented across many small businesses, not hypothetical edge cases.
- Meta's own UI changes on a timeline this document cannot outrun. Any static artifact -
  PDF, printed sheet, a set of screenshots handed over once - will be measurably wrong within
  months, and wrong in exactly the way that strands a non-technical user with no idea whether
  they made a mistake or the software did.
- The billing change in April 2026 shows the platform can impose a multi-day mandatory delay
  (credit line approval) with no warning baked into most existing guides - a contractor
  who budgets one evening for this and hits that wall is the median failure case, not the
  edge case.

**What changes the odds meaningfully, in order of impact:**

1. **The live, versioned web-page format over a PDF (Section 3), with the inline
   step-specific troubleshooting (Section 8) built into every step of the checklist, not
   bolted on as a separate FAQ.** This is the single highest-leverage decision in this
   document. A static document handed over once is close to guaranteed to go stale and strand
   someone; a page we can correct centrally the day we learn about a UI change is not.
2. **Doing the payment-method and Business-account status check before generating the export
   pack, not after.** If our software already knows during onboarding whether the owner has a
   Page, a Business Account, and a payment method on file, it can front-load the 24-48 hour
   credit-line delay to happen in parallel with campaign generation instead of surfacing it as
   a dead-end at 8pm on publish night. This is a product sequencing fix, not a documentation
   fix, and it should be treated as equally load-bearing as the pack itself.
3. **Treating every "I don't see that button" report as a mandatory pack update (Section 8),
   not a one-off support reply.** Without this discipline the pack decays exactly as fast as
   Meta ships changes, and the founder's support load grows instead of shrinking over time.
4. **Real user testing before this ships to a single paying customer.** Nothing in this
   research substitutes for watching one actual non-technical contractor go through the real
   flow, on their own laptop, with no one coaching them. The failure points catalogued here
   are the best available approximation from public reporting, not a substitute for that
   observation. This should happen before the export pack is considered done, not after the
   first support ticket arrives.

Without item 1 and item 4 specifically, the honest expectation is a meaningful fraction of
paying customers stalling out somewhere in Section 2's catalog and never reaching a live
campaign - which is the exact failure mode that kills this product regardless of ad quality.
With them, the flow is mechanical and repetitive enough (largely copy-paste against a checked
list) that a motivated owner should get through it, even if it takes two sessions rather than
one.
