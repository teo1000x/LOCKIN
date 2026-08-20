# UX Specification - v1

> Companion to `01-PRODUCT-SPEC.md` (build to the PIVOT section at the end), `08-DESIGN-SYSTEM.md`
> (binding visual spec, referenced by token name only, no colors/fonts/spacing redefined here), and
> `05-UI-DESIGN.md` (superseded in places, noted inline). This document specifies behavior,
> structure, copy, and state for the product web app. It contains no application code.

**The product, restated so every decision below is legible on its own:** the owner logs in,
starts a campaign, answers six required questions plus an optional depth section, and the AI
produces a marketing plan, a competitive read of local competitor ads, and a set of ready-to-post
ads. The owner approves every ad, downloads an export pack, and posts the campaign themselves in
Meta Ads Manager. **We never connect to Meta.** No OAuth, no publish button, no automatic lead
capture, no Meta-sourced metrics. Every screen below is designed against that constraint, not
around it.

Marketing site IA is out of scope for this document; it is covered structurally in
`05-UI-DESIGN.md` and is unaffected by the pivot. Everything below is the logged-in application.

---

## A. Information architecture

### Screen inventory

| Screen | Purpose |
|---|---|
| Sign up / Log in | Account creation, auth |
| Dashboard | Home. Three states specified in Section C. |
| Campaign wizard | Six required questions, optional depth section |
| Generation wait | The 30 to 90 second build, specified in Section B |
| Campaign detail: Plan | Marketing plan artifact |
| Campaign detail: Competitors | Competitive read artifact |
| Campaign detail: Ads | Approval workspace |
| Campaign detail: Export | The export pack and Ads Manager walkthrough |
| Results log | Self-report entry and history |
| Settings | Business profile, billing, account |

### Navigation model

Three destinations, flat, no nesting: **Dashboard, Campaigns, Settings.** Desktop uses a left
rail carrying those three plus a pinned "New campaign" action above the fold. Below 768px, a
bottom tab bar carries the same three destinations; "New campaign" is not a fourth tab, it is the
primary button at the top of the Dashboard screen, because campaign creation is an infrequent,
high-intent action (an owner runs one to a few campaigns a year), not a place someone browses to.
Tab bars read best at three to five destinations with none of them representing an occasional
action, so the campaign wizard lives one tap deep from Dashboard instead of occupying a permanent
slot.

Campaign detail (Plan, Competitors, Ads, Export) is not four nav items. It is one destination
reached from the Campaigns list, with four tabs inside it, because all four are facts about the
same campaign and an owner thinking "let me check my ad campaign" should land in one place and
find everything, not hunt across a flat list of unrelated top-level screens. This mirrors how a
non-technical user actually models the product: not "I want the Ads screen," but "I want to look
at my campaign."

Results (the self-report log) is deliberately **not** a fourth top-level tab. It lives as a card
on the Dashboard with a drill-in screen behind it. Two reasons, both direct consequences of the
locked self-reporting rule. First, a permanent "Results" tab that an owner who never reports
would open to find empty is a dead end built into primary navigation, which is worse than not
having it. Second, keeping report entry inside the Dashboard means the ask is always presented in
context, next to the numbers it would fill in, rather than as a separate chore screen the owner
has to remember exists.

**Why not a deeper information architecture (sidebar tree, settings sub-nav, multi-level menus):**
this is a person who does not want to learn software. Every additional nesting level is a chance
to get lost mid-task on a phone with one thumb free. Three flat destinations plus one drill-in
pattern (list to detail, detail to tabs) is the entire navigation vocabulary of the product. It
never grows past two taps from anywhere to anywhere.

**Wizard and export walkthrough are not nav destinations at all.** They are full-screen guided
flows entered from a specific button and exited only through an explicit "Save and exit" or
"Done," never through the persistent nav (which is hidden during both flows, replaced by a
progress indicator and a back arrow). This keeps a person who is mid-task from tapping "Dashboard"
by habit and losing their place, and it makes the flow read as a distinct, bounded task rather than
another corner of a big app to get lost in.

**Usability flag:** if self-reporting turns out to be heavily used once there is real usage data,
burying Results inside the Dashboard could become a scaling limitation, an owner with months of
history may want a dedicated, filterable log screen with its own nav slot. That is a deliberate v1
trade-off in favor of a simpler nav for a non-reporting majority, and it should be revisited against
real self-report engagement numbers, not assumed away.

---

## B. First-run experience

Signup to first generated campaign, designed against the finding that most churn lands in the
first 90 days and is dominated by time-to-first-value. The sequence has no detour, no empty
dashboard tour, and no screen between signup and the first real question.

**Step 1, Sign up.** Email and password, or continue with Google. Single screen, no separate
"tell us about your business" marketing-qualification step before the product starts. Copy:

> **Heading:** Get your first campaign built today
> **Subtext:** Answer six questions. We build the plan, the competitor read, and the ads. You
> post them yourself, no ad account needed yet.
> **Button:** Create account

**Step 2, straight into the wizard.** No welcome screen, no empty dashboard shown first. The
moment the account exists, the owner is on question one of the wizard. Skipping a "welcome tour"
is deliberate: a tour is a screen with nothing to show yet, and the fastest path to first value is
the actual first question.

**Step 3, six required questions, then the optional depth section offer** (full spec in Section
D). The optional section is presented as a genuine choice, not a guilt screen:

> **Heading:** Want sharper ads? A few more details help.
> **Subtext:** This takes about 5 minutes and is entirely optional. Skip it and we will still
> build you a full campaign, just with a bit more guesswork filled in by defaults.
> **Buttons:** Add more details (primary) / Skip, build my ads now (secondary)

**Step 4, generation wait, 30 to 90 seconds.** Specified in full below.

**Step 5, land on the Plan tab of the finished campaign,** not the Dashboard. The Dashboard at
this point would be an empty shell wrapped around one campaign; landing directly on the artifact
the owner just requested is the shortest path to the payoff. A single-line banner above the plan
reads:

> Your plan is ready. Here is what we built and why.

From there the natural reading order carries the owner through Plan, then Competitors, then Ads,
which is also the reading order specified in Section E.

**Step 6, approval, then export.** The first-run sequence is not complete until the owner has
approved at least one ad and seen the export pack, because that is the actual deliverable, a
generated ad nobody has approved is not yet a thing the owner can use. The wizard-to-export arc is
one continuous session by design, no forced "come back later" break, because coming back later is
exactly where a self-serve tool loses a first-time user for good.

### Solving the 30 to 90 second wait

This is treated as a real design problem, not a spinner. Four decisions:

**1. The progress shown is real, not decorative.** Generation is genuinely a multi-stage pipeline:
pulling competitor ads from the Meta Ad Library, drafting the plan, drafting ad copy, generating or
processing images, and running the policy lint. The UI shows those exact stages as a checklist that
fills in as each stage actually completes on the backend, not a fake percentage counting up. This
matters twice over: it is honest (the design system's ban on fake precision applies here too, no
invented "73%"), and multi-stage checklists measurably read as faster than a single spinner because
the person can see concrete work happening.

> Checking what other HVAC companies near you are running
> Writing your marketing plan
> Drafting your ad copy
> Preparing your images
> Running a final check on your ads

Each line sits greyed out until its stage starts, gets a filled accent checkmark when it completes,
and the currently active line carries a subtle pulse (opacity fade only, per the motion spec, and
disabled under reduced motion). No spinner icon anywhere; the checklist itself is the loading state,
laid out in the exact shape the finished activity feed will later take, which is the skeleton
loader principle applied to a list of stages instead of a static layout.

**2. Time expectation is set once, honestly, and not as a countdown.** Under the checklist, a
single static line:

> Usually done in under a minute.

No ticking timer, no "37 seconds remaining" (fake precision the system cannot actually promise). If
generation runs long, past 90 seconds, the line changes once to acknowledge it rather than silently
lying:

> Taking a bit longer than usual, still working.

**3. The wait is safely interruptible, because this audience gets interrupted constantly.** A
secondary link under the checklist reads:

> You can leave this page. We will keep working and let you know.

Tapping it returns to the Dashboard, where an in-progress campaign shows as a card with the same
live checklist state (not a generic "processing" label). When generation finishes, the owner gets
a push notification or email (channel chosen at signup) reading:

> Your ads are ready. See what we built for [Business name].

This directly answers the "these people get interrupted constantly" requirement: a phone call, a
customer walking up, or a dropped signal mid-generation never loses work or forces a restart, and
the product proactively closes the loop instead of expecting the owner to remember to check back.

**4. Nothing about the wait screen requires the owner to stay and watch.** The checklist is there
for the owner who does wait (most first-time users will, this is the payoff moment), but the
product does not require attention during it. This is the resolution to the "genuinely guided
flow" requirement at a moment where guidance has nothing left to guide, the owner already answered
every question, so the UI's job shifts from guiding to reassuring and then getting out of the way.

---

## C. Dashboard, three states

The dashboard is designed to be genuinely useful with zero self-reported data and to get better
as data arrives, per the locked decision. The mechanism: the numbers that require Meta or
self-reporting are never faked, padded with zeros, or replaced with placeholder metrics. Instead,
each state shows the most honest, most complete picture of what is actually known at that point,
and the layout itself changes shape as more becomes known rather than showing permanently empty
tiles.

**Enforcement of the metrics rule applies twice here.** Not only are CTR, CPM, ROAS, and
impressions never shown (the product has no access to them at all, so this is structurally
guaranteed), but internal generation metrics (ad variants generated, images produced, tokens
spent) must also never masquerade as performance. Those are our costs, not the owner's results,
and showing them would violate the spirit of the rule even though it is not literally a Meta
metric.

### State 1: Empty (no campaign yet)

No stat tiles at all. A zeroed-out stat tile ("0 leads, 0 booked, $0 cost per lead") is not
useful, it is noise dressed as data, and it violates the fake-precision spirit of showing numbers
that mean nothing. Instead:

```
[ H1: Let's build your first campaign ]
[ Body: Answer six questions and we'll build your marketing plan, check what
  competitors near you are running, and write your ads. Usually done in
  under a minute once you finish the questions. ]
[ Button, primary, lg: Start your first campaign ]

[ H2: What you'll get ]
[ Three plain rows, not cards, checkmark icon + sentence: ]
  A marketing plan you can actually read
  A look at what other [trade] companies near you are advertising right now
  A set of ads ready to post, in your own words

```

### State 2: Day one (campaign generated, approved, exported, zero self-reported results yet)

The pre-pivot dashboard used three Meta-sourced stat tiles. Those numbers do not exist post-pivot.
Rather than leave the stat-tile slot empty or fake it, this state replaces it entirely with facts
the product actually knows, which are true and substantive on day one:

```
Main Street Heating & Air                         [ status pill: Ready to post ]
Round Rock, TX and 12 miles around

[ Strip, three facts, same visual weight as the old stat tiles: ]
  5 ADS EXPORTED          $89 A/C TUNE-UP          $1,200/MO RECOMMENDED
  ready to post            your offer               your budget

[ H2: What we did ]
  ✓ Checked 9 other HVAC companies near you
  ✓ Built your marketing plan
  ✓ Wrote and approved 5 ads
  ✓ Packed everything for Meta Ads Manager

[ Card: Did you get this live? ]
  Have you posted this campaign in Meta Ads Manager yet?
  [ Yes, it's live ]  [ Not yet ]  [ Having trouble ]
```

That last card is deliberate and answers a gap the locked decisions create (flagged in full at the
end of this document): with no tracking at all, the product cannot tell the difference between "the
owner downloaded the pack and posted it" and "the owner downloaded the pack and it is sitting in
Downloads." This single three-way tap is the cheapest possible signal to recover that distinction,
well below the cost and friction of the full weekly self-report, and it is the first thing Day One
asks, before any request for lead numbers.

If the answer is "Having trouble," the card expands in place to a short list of the most common
export-pack failure points with links back into the Export screen's walkthrough (Section G), not a
dead end.

### State 3: Steady (owner has been self-reporting)

Only once the owner has logged at least one result does the dashboard show the pacerev-style stat
strip, and every figure in it is qualified as self-reported, never presented with the implied
precision of a real tracking integration:

```
[ Small label, text-muted: Numbers you've logged ]
[ Stat strip, three tiles: ]
  LEADS THIS MONTH        BOOKED JOBS              MONEY BOOKED
       14                      6                      $2,340
  you logged 3 this week   you logged 2 this week   from jobs you logged

[ H2: What we did ]
  (same activity feed pattern as Day One, continues accumulating)
```

The "you logged" qualifier on every delta line is not decorative, it is the honesty mechanism that
lets this screen use the same confident stat-tile layout as a tracking-integrated competitor
without ever implying we verified any of it ourselves. Cost per lead is only shown if the owner has
also logged a spend figure; if they have not, that tile is simply omitted rather than divided by a
guess, because a computed number built on an unentered denominator is exactly the kind of invented
statistic the inviolable rules forbid.

The Results log entry point remains visible in this state too, now framed around continuation
rather than a first ask:

> Log this week's leads. Takes about 20 seconds.

---

## D. Campaign wizard, screen by screen

One question per screen, mobile-first, per the design system's wizard component. Every field
below: label above input, helper text or error below, never placeholder-as-label, autosave on a
500ms debounce with a static "Saved" indicator next to the step counter (matches design system
Section 4.C). State persists per-account server-side, not local-only storage, so an owner who
starts on a phone between jobs and finishes on a laptop that night resumes exactly where they
stopped. If an owner returns with an incomplete wizard, the Dashboard shows a single card instead
of the Start-your-first-campaign hero:

> Pick up where you left off. You're on question 4 of 6.
> [ Continue ]

### Required questions (six)

**1. Business name**
- Label: `What's your business name?`
- Helper: `This is how customers will see you in your ads.`
- Input: single-line text, required
- Error (empty): `Enter your business name to continue.`
- Error (too long, >60 chars): `Keep it under 60 characters, the name people actually use.`

**2. Trade / service type**
- Label: `What kind of work do you do?`
- Helper: `This shapes everything else we build, so pick the closest match.`
- Input: searchable single-select from curated taxonomy (HVAC, Plumbing, Roofing, Electrical,
  Garage Door, Pest Control, Landscaping, Pool Service, Appliance Repair, Locksmith, Other)
- If "Other" selected, reveal a follow-up text field: `Tell us what you do` (required when Other
  is chosen)
- Error (none selected): `Choose the trade closest to your business.`

**3. Your offer**
- Label: `What's the one deal you want new customers to see?`
- Helper: `Pick your best offer, not a list. One clear deal converts better than five. Example:
  $89 A/C tune-up, Free roof inspection, $50 off your first cleaning.`
- Input: single-line text, required
- Inline AI suggestion chip once trade is known (per design system 4.C pattern): `Most [trade]
  businesses near you lead with something around $79 to 99.`
- Error (empty): `Enter the offer you want us to advertise.`

**4. Service area**
- Label: `Where do you want customers to come from?`
- Helper: `We'll show your ads to people within this distance of your shop.`
- Input: address or ZIP text field, plus a radius control (5, 10, 15, 20, 25, 30 miles), defaulted
  by trade (a locksmith defaults tighter than a roofer, a smart default carrying its own stated
  reason beneath the control: `We default roofers to a wider radius because roofing jobs are worth
  driving further for.`)
- Error (invalid address): `We couldn't find that address. Try adding your city and state.`
- Error (no radius): defaults always pre-selected, so this cannot be empty

**5. Average job value**
- Label: `What's a job like this usually worth to you?`
- Helper: `A rough average is fine. This helps us recommend a budget that makes sense for your
  business.`
- Input: dollar amount, numeric
- Error (empty): `Enter a rough average job value.`
- Error (zero or negative): `Enter an amount greater than $0.`

**6. Monthly ad budget**
- Label: `How much are you comfortable spending on ads each month?`
- Helper: `This is separate from what you pay us. You'll spend this directly in Meta Ads Manager,
  on your own card, when you're ready.`
- Input: dollar amount, numeric, with a recommended floor shown beneath (derived from the product
  spec's ~$1,000 to $1,500/mo learning floor)
- Warning, non-blocking, shown inline below the field if the owner enters under the floor: `Ads
  usually need at least $1,000 a month to gather enough results to improve. You can still start
  lower, we'll just say so in your plan.`
- Error (empty): `Enter a monthly budget, even a rough one.`
- Error (zero or negative): `Enter an amount greater than $0.`

### Optional depth section, roughly 15 fields

Presented as named groups, each opening with one sentence stating what it improves, per the
locked decision that skipping must never feel like failure. The section entry screen groups them
so the owner sees the shape of what is optional before committing time to it:

> **Heading:** A few more details help us build sharper ads
> **Subtext:** Add as many or as few as you want. Each one below shows exactly what it changes.
> **Buttons:** Add details / Skip this, build my ads now

Fields, grouped, each with the "what it improves" line shown directly under its label rather than
buried in a tooltip:

**Reach your customers**
1. `Phone number` (helper: shown on your ads so people can call directly. Improves: call-based
   ads instead of form-only.)
2. `Website, if you have one` (optional, improves: adds a link option to your ads)
3. `Do you take emergency or after-hours calls?` (yes/no toggle. Improves: unlocks urgency-based ad
   copy, "Call now, we answer 24/7," when true)
4. `When do customers usually call you?` (single select: mornings, afternoons, evenings, all day.
   Improves: timing guidance in your plan)

**What you actually do**
5. `Which services should we advertise?` (multi-select, scoped to the chosen trade. Improves: ad
   variants split by service instead of one generic ad)
6. `Are there areas you don't want to work in?` (free text or map exclusion. Improves: keeps your
   ads from reaching people you'd have to turn away)
7. `What do customers pick you over competitors for?` (free text, examples shown: same-day
   service, 20 years in business, licensed and insured. Improves: the actual differentiator line in
   your ad copy, instead of a generic one)

**Proof and trust**
8. `Do you have any licenses or certifications worth mentioning?` (free text. Improves: adds
   credibility language your competitors might not have)
9. `Any warranty or guarantee you offer?` (free text. Improves: a guarantee is one of the strongest
   converting lines in trade ads)
10. `Roughly how many 5-star reviews do you have?` (numeric, optional. Improves: a real, specific
    number in your ad, "Rated 4.9 from 140 local reviews," never a rounded or invented one)

**Look and feel**
11. `Upload your logo` (image upload. Improves: your ads carry your actual branding)
12. `Upload a few photos of your work` (multi-image upload. Improves: real job photos convert
    better than any stock or generated image. If you skip this, we'll generate images for you,
    and we'll always label which is which so you know what's real)
13. `Do you have brand colors?` (optional color picker or "use what's in my logo." Improves: visual
    consistency across your ads)

**Voice**
14. `How should your ads sound?` (single select: straightforward and no-nonsense, friendly and
    approachable, premium and polished. Improves: the tone of every line we write)
15. `Anything else we should know?` (open text, capped helper: `A sentence or two is plenty.`
    Improves: catches anything the questions above missed)

Every optional field is individually skippable, no field-level "are you sure" friction. The
section as a whole can be exited at any point via a persistent `Skip the rest, build my ads now`
link in the footer, which carries forward whatever was filled in and drops nothing already entered.

**Usability flag:** the AI suggestion chip on the offer question and the recommended-floor warning
on budget are the two required-flow moments where the "smart defaults carry the optimization
knowledge" promise brushes against the "genuinely guided flow" requirement, both still ask the
owner to commit to a real number (a price, a dollar figure) with only a suggestion to lean on, not
a filled-in answer. That moment of numeracy cannot be fully engineered away without picking the
number for them, which the product deliberately does not do since it is their money and their
price. The mitigation is a strong, reasoned default plus permission to just accept it, not the
elimination of the moment itself.

---

## E. The three output artifacts

Reached as tabs inside Campaign detail: Plan, Competitors, Ads. Reading order matches tab order,
plan first because it is the only artifact that requires zero prior knowledge of advertising to
understand, and it frames everything that follows.

### Plan (Marketing plan artifact)

Written for someone who has never bought an ad. No jargon words appear anywhere on this screen,
not "CPM," not "reach," not "conversion rate," not "targeting" used as a bare noun without an
explanation attached the first time it appears.

Reading order:

```
[ H1: Your plan, in plain terms ]
[ One paragraph, plain-English summary: what we're doing and why, e.g.
  "We're going to show ads for your $89 A/C tune-up to homeowners within
  12 miles of your shop, for about $1,200 a month. Based on similar
  businesses, that's usually enough to get consistent calls without
  overspending while you're still learning what works." ]

[ H2: Who you'll reach ]
[ Plain description of the audience, with the reasoning: "People who live
  within 12 miles of [address]. We picked that radius because that's how
  far most HVAC companies your size can profitably send a technician." ]

[ H2: Your budget ]
[ The recommended number restated, with the reasoning, and what happens
  if they set it lower than recommended (no scare language, just honest
  expectation-setting) ]

[ H2: Your offer ]
[ Restates their offer and why it was chosen or how it compares to
  competitors, if the competitive read found relevant data ]

[ H2: What to expect ]
[ Honest, unhyped timeline language: "Ads usually need one to two weeks
  to find their audience. Don't judge results in the first few days." No
  promised numbers, no fabricated case studies, per the no-invented-
  statistics rule; this section never cites a performance figure we
  cannot source to a real account. ]
```

### Competitors (Competitive read artifact)

Sourced live from the public Meta Ad Library. Sorted by how long each ad has been running
(longest first), with the heuristic stated plainly since it is the entire rationale for the
ordering and this audience should never have to infer why a list is sorted the way it is:

```
[ H1: What other [trade] companies near you are running right now ]
[ One-line explainer: "Ads that have been running a long time are usually
  working, since businesses don't keep paying for ads that don't. We
  sorted these by how long they've been live." ]

[ List of competitor ad cards, each: ]
  Business name
  Ad screenshot (real, pulled from the Ad Library)
  "Running since [date], [N] days"
  Their offer, extracted in plain terms if detectable
```

If zero competitors are found in the area (a real, expected case in low-density service areas),
the screen states that honestly rather than showing placeholder or fabricated entries:

> No other [trade] companies in your area are currently running Meta ads that we could find. That
> can be a good thing, it means less competition for attention. We've built your plan without a
> competitor benchmark.

### Ads (the ad set)

The approval workspace, specified fully in Section F. Grid of ad-preview cards on desktop, one
per row stacked full-width on mobile, using the design system's ad-preview card component
unmodified (Section 4.E of the design system doc), because that card is exempt from the
fake-screenshot ban specifically because it is a functional review surface, and reusing it exactly
here is what makes the review honest.

---

## F. Approval experience

Every ad ships as an ad-preview card (design system 4.E) with the mandatory rationale strip and
an action row: Edit, Regenerate, Approve. Per-variant, not a single "approve all" for the set,
because the inviolable rule requires a persisted approval record per ad whose content hash matches
the ad's current content, and a bulk approval that could silently cover a future edit would defeat
that guarantee in spirit even where the code enforces it.

**Approve.** The card's action row collapses the three buttons to a single status: a filled
`Approved` pill with a small checkmark, plus a quiet `Edit` link if they change their mind. No
confirmation modal, this is a low-stakes, fully reversible action (approving is not publishing,
nothing leaves the product yet), so a modal here would be friction without protection.

**Edit.** Opens the card's fields inline (headline, primary text, description, image) for direct
editing, not a separate modal, so the owner can see the live preview update as they type.

**Regenerate.** Produces a new variant in the same slot, with a one-line note of what changed:
`New headline and image, same offer and audience.` The prior version is not silently discarded, a
small `Undo` toast appears for a few seconds after regeneration.

**Reject.** Removes the variant from the set entirely (destructive-style button per design system
4.A, used only for genuinely destructive actions). Confirmation is a single inline
"Are you sure? This ad won't be included." with Cancel and Confirm, not a full modal, since the
action is reversible in principle if the owner regenerates a replacement.

### What happens when an edit invalidates a prior approval

This is the moment the inviolable approval-gate rule becomes visible to the owner, and it must
read as protection, not obstruction. The moment an approved ad's content changes (any edit, or a
regeneration), the card's status silently reverting from `Approved` back to needing review would
feel like the product losing track of what happened. Instead, the change is narrated directly on
the card:

```
[ Card, still showing the edited content ]
[ Status pill changes from a filled "Approved" (accent) to an outlined
  "Review your changes" pill, not just a blank reset ]
[ Inline strip, replacing the rationale strip's usual spot for one view: ]
  You edited this ad after approving it. We're asking you to look at it
  again so nothing goes out that you haven't actually seen.
[ Action row returns to: Edit · Regenerate · Approve ]
```

The copy explicitly states the reason ("so nothing goes out that you haven't actually seen")
because naming the mechanism is what turns it from a mysterious status flip into a visible safety
feature. The Export screen (Section G) additionally will not include any ad that is not currently
in the `Approved` state, and if the owner tries to proceed to export with any ad sitting in
`Review your changes`, the export button stays enabled for the approved subset but a banner names
what is being left out:

> 1 ad needs another look before it's included in your export. [ Review it ]

---

## G. The export pack handoff

This is the highest-risk screen in the product, and the section receives disproportionate
attention accordingly, because the entire value of every prior screen depends on a non-technical
person successfully turning our output into a running campaign with nobody to call for help.

### The core design decision: never make the owner hold the plan in their head

A downloadable PDF that the owner reads once, then alt-tabs away from into Meta Ads Manager and
tries to remember, is the single most likely failure mode. The export experience is instead an
**in-app, step-by-step checklist that mirrors the actual screens of Meta Ads Manager**, kept open
in one browser tab side by side with Ads Manager in another, so the owner never has to hold more
than one instruction at a time in their head or scroll back to find a value they already read
past.

### What is in the pack

A single download (ZIP) plus the same content rendered as the in-app walkthrough. The ZIP exists
for owners who want an offline copy or want to hand it to someone else; the in-app walkthrough is
the primary path and the one the product actively guides toward.

Contents:
- Images, one file per ad, named descriptively (`tune-up-offer-photo-1.jpg`, not `IMG_4821.jpg`)
so a confused owner can tell which file is which without opening each one.
- One page per ad with every text field already broken out by exact Meta field name (Primary
  text, Headline, Description, Call-to-action), not run together as paragraphs the owner has to
  parse and re-split themselves.
- A targeting spec pre-translated into Meta's own field labels and exact values ("Location: 12
  mile radius around 4110 Rutland Dr, Austin, TX," "Daily budget: $40"), never our internal terms.
- A written, numbered, step-by-step guide to building the campaign in Ads Manager, including how
  to create a Meta ad account from scratch for owners who do not have one yet, since that is a real
  and common starting condition for this audience, not an edge case.

### The in-app walkthrough

```
[ H1: Post your campaign in Meta Ads Manager ]
[ Subtext: Keep this open in one tab and Meta Ads Manager open in
  another. Work through these steps in order. Each one tells you exactly
  what to click and what to type. ]

[ Progress: "Step 3 of 11", plain counter, same idiom as the wizard ]

[ Step card: ]
  [ What to do, one sentence, imperative: "Create a new campaign" ]
  [ Where: a labeled screenshot or simple annotated diagram of the real
    Ads Manager screen, with the exact button circled, e.g. the
    "+ Create" button in the top left ]
  [ What to enter, if anything, shown as a value with a one-tap Copy
    button next to it so nothing is retyped by hand: ]
    Campaign name:  [ Main Street Heating tune-up - Aug 2026 ]  [ Copy ]
  [ Checkbox: "I've done this" ]

[ Footer: Back · Next step ]
```

Every field the owner needs to enter anywhere in Ads Manager (campaign name, budget number,
radius, age range if applicable, ad copy, headline, description, CTA label) is shown with its own
Copy button. This is the single highest-leverage detail on this screen: transcription error, an
owner mistyping a budget or dropping a line of ad copy, is the most likely way this handoff fails
silently, and copy-paste removes it almost entirely.

**Step completion persists**, exactly like wizard state, because this audience gets interrupted
mid-task constantly and building a campaign in Ads Manager is a 10-to-15-minute task that will
very plausibly get paused by a phone call or a customer walking in. Returning to the walkthrough
later resumes on the exact step left off, with completed steps shown collapsed and checked above
the current one, never restarting from step one.

### The "still stuck" fallback

Below the walkthrough, permanently visible, not hidden until an error state:

> **Stuck on something?**
> [ Link: See common problems and fixes ]

That page covers the failure modes most likely to actually occur: an ad rejected by Meta's own
review, not finding the "Ads Manager" link from a personal Facebook account, not having a business
Facebook Page yet, a payment method Meta rejects. Each entry is a short, specific fix, not a
generic "contact support" dead end, because there is no live agent behind this product and the
page has to actually solve the problem on its own.

### Marking the campaign live

Once the walkthrough reaches its last step, the closing screen ties directly back into the Day One
dashboard state from Section C:

> **Heading:** That's everything.
> **Body:** Once your campaign is live in Ads Manager, come back and tell us. It only takes a
> second and it's how we make your dashboard useful.
> **Buttons:** It's live now / I'll do this later

Answering `It's live now` here is the same three-way check-in described in Section C's Day One
state, just asked at the moment it is most natural to answer honestly, right after finishing the
task, rather than only waiting for the owner to notice the card on their next dashboard visit.

### Usability flag: this screen has a real, unresolved external dependency

Meta Ads Manager's own interface changes over time, screenshots go stale, buttons move, field
names get renamed. Because we never connect to Meta, we have no automated way to detect when our
walkthrough drifts out of sync with the real product it is describing, and a walkthrough that is
wrong even once for a non-technical user attempting this alone is exactly the failure mode this
section exists to prevent. This is not a problem the interface design can fully solve on its own.
It requires an operational commitment (a recurring manual QA pass against the live Ads Manager UI,
and a visible "content last verified" date on the walkthrough itself so staleness is at least
disclosed rather than silent) that sits outside this document's scope but must exist for this
screen to keep working. Flagging it here rather than quietly designing around it, because
designing around it is not actually possible from the UI layer alone.

---

## H. The optional self-report flow

Governed by the locked decision: self-reporting is offered, never forced, and the product must
degrade gracefully when ignored (specified in Section C's Day One state, which shows a full,
useful dashboard with zero reports logged).

**How we ask.** Two moments, both low-friction, neither a blocking modal:

1. The three-way "Did you get this live?" check-in at the end of the export walkthrough and again
   as a Dashboard card (Section C, G), which is the cheapest possible signal and is asked first.
2. A weekly prompt, starting roughly seven days after export, not before, since asking for results
   before there has been time to get any is asking the owner to report nothing. Delivered by
   whichever channel they chose at signup (email or SMS), with a direct link into the Results log,
   not a login wall:

> **Subject / message:** How did this week go?
> **Body:** Quick one, takes about 20 seconds. How many calls or leads came in, and did any turn
> into a booked job? [ Log this week ]

**The Results log screen itself:**

```
[ H1: Log your results ]
[ Three simple numeric fields, largest text, tabular numerals: ]
  Leads or calls this week    [       ]
  Of those, how many booked   [       ]
  What were they worth, total [ $     ]  (optional, skippable independently)
[ Button: Save ]
[ Below: a plain running history, most recent week first, same visual
  idiom as the activity feed, not a data table ]
```

**How we make it feel worth doing.** Immediately after the first save, the Dashboard visibly
changes shape, the stat strip appears where the "What we did" facts strip used to be alone, which
is a direct, visible reward for the 20 seconds spent: the owner can see their own dashboard
becoming a real instrument instead of an activity log. The copy on the log screen names this
directly the first time:

> The more you log, the more useful your dashboard gets, and the sharper we can make your next
> campaign.

**How it degrades gracefully when ignored.** An owner who never opens the weekly prompt or the
Results screen sees exactly the Day One dashboard state indefinitely: the facts strip, the
activity feed, the soft "Did you get this live?" card. Nothing on that screen is broken, blank, or
apologetic about the missing numbers, because it was designed as a complete state on its own, not
a degraded version of the steady state. The weekly prompt itself stops after a small number of
unanswered sends (recommend three) rather than nagging indefinitely, replaced by a single
permanent, low-emphasis Dashboard card rather than a recurring notification, so an owner who has
opted out by inaction is not chased.

---

## I. Every state for every screen

Skeleton loaders match final layout shape everywhere, never a generic spinner, per the design
system's motion rules. Summarized per major screen; component-level states (button, input) are
fully specified in the design system doc and are not repeated here.

**Dashboard**
- Loading: skeleton of the current state's shape (facts strip skeleton as three label/value
  rectangles, activity feed skeleton as three text-line rows) rather than a spinner, since which
  state (empty, day one, steady) is about to render is already known before the data arrives.
- Empty: Section C, State 1.
- Partial (campaign generating): the live checklist card from Section B, shown inline as a card
  rather than the facts strip.
- Error (dashboard data fails to load): `We couldn't load your dashboard. [ Try again ]`, no
  broken layout underneath, the skeleton stays in place behind the error message rather than
  collapsing to blank.
- Success: Section C, States 2 and 3.

**Campaign wizard**
- Loading: none needed per-question, fields render instantly from local state.
- Empty: not applicable, every screen has exactly one question.
- Error: inline, below the field, specified per-field in Section D.
- Partial (resuming): the "Pick up where you left off" Dashboard card, then the wizard opens on
  the exact next unanswered question with everything prior pre-filled.
- Success: transitions directly to the generation wait screen.

**Generation wait**
- Loading: the honest staged checklist, Section B.
- Error (a stage fails, e.g. Ad Library lookup times out): that stage's line shows an outlined
  warning icon instead of a checkmark, generation continues with the remaining stages, and the
  finished Plan screen discloses the gap plainly rather than silently proceeding as if nothing
  happened: `We couldn't check competitor ads in your area right now. Your plan and ads are ready,
  the competitor read isn't. [ Try again ]`
- Success: routes to the Plan tab.

**Plan / Competitors / Ads tabs**
- Loading: skeleton matching each tab's real layout (paragraph-shaped bars for Plan, card
  skeletons for Competitors and Ads).
- Empty (Competitors, zero local competitors found): the honest empty state written in Section E.
- Error: `Something went wrong building this. [ Try again ]`, scoped to the failed tab only, the
  other two tabs remain usable.
- Partial (ads still regenerating one variant): that single card shows its own inline skeleton
  (image block plus text-line bars in the ad-preview card's shape) while the rest of the grid stays
  interactive.
- Success: Sections E and F.

**Export**
- Loading: skeleton of the step-card layout.
- Error (an ad included in the pack was edited after the pack was generated, going stale): the
  Export tab shows a banner before the walkthrough: `Your ads changed since you last built this
  pack. [ Rebuild pack ]`, never lets a stale pack silently persist as if current.
- Partial (mid-walkthrough): completed steps collapsed and checked, current step expanded, as
  specified in Section G.
- Success: the closing "That's everything" screen, Section G.

**Results log**
- Loading: skeleton of the three-field form plus a few placeholder history rows.
- Empty (no history yet): `Nothing logged yet. Your first entry starts your dashboard's real
  numbers.`
- Error: inline per field, standard numeric validation (`Enter a number, or leave this blank.`).
- Success: entry saves, history list updates immediately above the form, Dashboard reflects the
  new totals on next visit.

---

## J. Interface copy

Additional real strings not already embedded above, organized by kind. All follow the AGENTS.md
voice rules: leads, jobs, and dollars, plain-English rationale on every AI decision, specifics
over adjectives, no filler verbs.

**Primary buttons**
- `Start your first campaign`
- `Continue`
- `Approve`
- `Regenerate`
- `Build my export pack`
- `Save`
- `Log this week`

**Secondary buttons**
- `Back`
- `Skip, build my ads now`
- `Edit`
- `Try again`
- `I'll do this later`

**Destructive buttons**
- `Reject this ad`
- `Delete this campaign`
- `Remove my photos`

**Empty states**
- Dashboard, empty: covered in Section C.
- Competitors, none found: covered in Section E.
- Results log, no history: `Nothing logged yet. Your first entry starts your dashboard's real
  numbers.`
- Campaigns list, none yet: `You haven't started a campaign yet. [ Start your first campaign ]`

**Errors, general**
- Network failure on save: `We couldn't save that. Check your connection and try again.`
- Session expired: `You were logged out. Log back in and we'll take you right back here.`
- Generic unexpected failure: `Something went wrong on our end. Try again, and if it keeps
  happening, [ let us know ]`

**Confirmations, transient**
- Ad approved: no toast needed, the pill state change is confirmation enough.
- Wizard field autosaved: `Saved`, static text next to the step counter, 2 seconds, no animated
  toast (design system 4.C).
- Export pack rebuilt: `Your export pack is up to date.`

---

## K. Mobile behavior, below 768px

**Dashboard.** Single column throughout. The facts strip and stat strip stack their three tiles
vertically rather than side by side (design system's stat tile spec already calls for this). The
bottom tab bar (Dashboard, Campaigns, Settings) replaces the desktop left rail entirely, it does
not collapse into a hamburger, a persistently visible tab bar is worth the vertical space it costs
for an audience that should never have to discover navigation behind an icon. The "New campaign"
button sits pinned near the top of the Dashboard content, not floating over the tab bar, so it
never competes with or obscures the bottom navigation.

**Campaign wizard.** Already specified mobile-first in the design system (Section 4.C): one
question per screen, sticky footer with Back and Continue, single focus target per screen. Nothing
in this document adds desktop-only wizard behavior; the wizard is the same experience at every
width, which is itself the mobile-first resolution, there is no reduced mobile version to design
because the full version was never wider than a phone needs.

**Approval workspace.** Ad-preview cards stack full width, one per screen-width row, in the same
reading order as desktop (no reordering by screen size, so an owner switching from phone to
desktop mid-review finds ads in the same order). The action row (Edit, Regenerate, Approve) stays
horizontal within the card rather than stacking to three full-width buttons, since three buttons at
comfortable tap-target height fit a phone width without wrapping.

**Export walkthrough.** Each step renders as its own full-height screen on mobile rather than a
scrolling list of steps, since a phone screen showing three stacked step cards at once invites
losing track of which step is current. The Copy buttons next to each field value are full tap
targets, not small inline icons, since this is the exact moment transcription accuracy matters
most and a mis-tap here has the highest cost on the whole handoff.

**Results log.** The three numeric fields stack vertically, each at the same 16px-minimum input
text size as the wizard (design system 2.C), so mobile Safari never auto-zooms on focus mid-entry.

---

## Usability problems flagged by the locked decisions

Consolidated from throughout this document, so they are not lost inside individual sections.

1. **The export walkthrough depends on Meta's own UI staying still, and we have no way to detect
   when it moves.** With no Meta connection at all, there is no automated signal that our
   screenshots or step instructions have gone stale. This requires an operational QA process
   outside this document's scope, and the walkthrough should visibly disclose a last-verified
   date so staleness is at least honest rather than silent. Full detail in Section G.

2. **Zero tracking means the product cannot tell "exported and posted" apart from "exported and
   forgotten."** The three-way "Did you get this live?" check-in (Sections C and G) is the
   cheapest recoverable signal for this gap, but it depends entirely on the owner answering
   honestly, there is no ground truth to check it against.

3. **Required budget and offer fields still ask a non-technical owner to commit to a specific
   number, which "smart defaults carry the optimization decisions" cannot fully remove.** A
   strong, reasoned default with permission to accept it as-is is the mitigation; the moment of
   deciding a real dollar figure cannot be automated away without the product picking the number
   on the owner's behalf, which was explicitly ruled out. Detail in Section D.

4. **AI-generated fallback images carry a trust risk this document cannot resolve on its own.**
   When an owner skips the photo upload, generated images fill the gap. The approval screen must
   label generated images plainly as generated, never blended in as if they were the owner's own
   photos, extending the anti-fabrication spirit of the inviolable rules to imagery even though
   that rule is written about statistics. This is a content-generation quality question as much as
   a UX one and sits partly outside this document's scope.

5. **A three-item flat navigation model, chosen deliberately for this audience, could become a
   limitation if self-reporting usage grows.** Burying Results inside the Dashboard keeps the nav
   honest for a non-reporting majority today; it is a v1 trade-off to revisit against real
   engagement data, not a permanent architectural stance. Detail in Section A.
