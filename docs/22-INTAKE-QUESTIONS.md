# The intake questions

_Written 19 August 2026. Supersedes any six-question list implied elsewhere. The landing page
promises "six questions", so this is a contract with the buyer, not a suggestion._

---

## 0. The rule that decides what makes the cut

A question earns a slot only if **the generator cannot produce a good ad without it, and we
cannot infer it**. Everything else is either derived from the trade taxonomy in
`src/lib/trades.ts`, looked up, or asked later once the owner has already seen value.

That test kills most of what an ad platform would normally ask. Targeting, placements,
objective, optimisation event, audience, schedule: all removed. Not to be friendly, but because
Meta removed homeowner targeting and forced Advantage detailed targeting on for conversion
objectives in 2026 (`docs/13`), so asking an owner to guess at an audience is asking them to do
work that no longer changes the outcome.

---

## 1. The six

Order matters. The first two are frictionless and build momentum. The money question sits
fourth, after commitment is established but before fatigue. The last one is the highest-value
question in the set and only works once trust exists.

### Q1. What kind of work do you do?

Free text with autocomplete against the 96-trade taxonomy. Never a dropdown of 96 items.

**Drives:** template selection (`docs/19` section 2), offer library, seasonality curve, the
policy risk profile, and the competitor query. This single answer does more work than the other
five combined.

**Why it is first:** it is the one question every owner can answer instantly and correctly,
which sets the tone that this will be easy. `[INFERENCE]`

**Fallback if unmatched:** accept the free text, map to the nearest category, tell them plainly
that they are running on category patterns rather than trade-specific research. Never dead-end.

### Q2. Where do you work, and how far will your crew drive?

City or postcode, plus a radius with a smart default by trade.

**Drives:** the geo target, the competitor pull, and the local proof language in the copy.

**Default:** from the trade. A locksmith defaults tighter than a roofer, because a roofer will
drive an hour for a re-roof and a locksmith will not drive twenty minutes for a rekey. Show the
default already filled and let them drag it.

**Why not just the city:** radius is the only targeting input left that materially changes
delivery, so it is the one geographic thing worth an owner's attention.

### Q3. What is one job worth to you, on average?

A number, in dollars.

**Drives:** the daily budget arithmetic that is already live on `/estimate` (about a seventh of
one average job, floored at $40, capped at $150), the lead-form qualifying questions, and
whether the plan recommends a lead-gen offer or a straight quote request.

**Why this and not "what is your budget":** an owner asked for a budget guesses, anchors low,
and blames the software when a low budget underdelivers. An owner asked what a job is worth
answers accurately in two seconds because they know it cold. We then derive the budget and show
the arithmetic. `[INFERENCE]`

### Q4. What is the one deal you want new customers to see?

Pick from a trade-specific offer library, or write your own.

**Drives:** the headline, the price medallion, the lead-form logic, the policy lint path.

**The library is the product here.** For HVAC it offers named-price tune-ups because that is
what every long-running HVAC ad in the research runs (`docs/17` section 1.1, prices from $17.75
to $99 all observed live). For roofing it offers a free inspection because that is the dominant
structure, and it attaches the no-pressure language by default because half that market spends
its copy proving it is not a storm chaser.

**One offer, not a list.** A list of five offers produces five weak ads. The screen says so.

### Q5. What makes you the one to call, in your own words?

Free text, one or two sentences, with three trade-specific prompts underneath to break the
blank-page problem. For a plumber: how long you have been at it, what you will not do, who
answers the phone.

**Drives:** the trust layer, the credential row on the creative (`docs/19` section 1.6), and
the anti-competitor angle when the trade needs one.

**Why it is worth a slot:** this is the only input in the entire set that a competitor using the
same software cannot produce. Everything else is derivable from trade plus geography. Without
it, two HVAC companies in the same city get near-identical ads, which is the failure mode that
kills this category of product. `[INFERENCE]`

### Q6. What should we never say about your business?

Free text, optional to skip, with examples.

**Drives:** a negative constraint on every generation, and a real reduction in the regenerate
loop.

**Why it is last and why it matters more than it looks:** it is the question that signals we
expect to be corrected, which is the opposite of how every other AI tool presents itself. It
also catches the specific landmines that make an owner reject an ad and never come back:
"never call us cheap", "we do not do warranty work", "do not mention financing". `[ASSUMPTION]`
that this reduces rejection rates; it needs measuring once there are users.

---

## 2. What we deliberately do not ask, and where it comes from instead

| Not asked | Where it comes from |
|---|---|
| Target audience, age, interests | Meta removed the useful ones and forces expansion. Radius plus offer does the work. |
| Daily budget | Derived from Q3, with the arithmetic shown. Editable after they see it. |
| Campaign objective, optimisation event | Fixed to lead generation. Owners cannot evaluate this choice and it is the same choice every time. |
| Brand colours | Sampled from the logo, or from the trade default palette. Editable later. |
| Logo | Asked at account setup, not in the campaign flow. Fallback in `docs/19` section 4.4. |
| Photos | Offered as an upload after the first ads are generated, when the owner has seen what generated images look like and wants better ones. `[INFERENCE]` that asking after beats asking before. |
| Licence and insurance numbers | Account setup, once, reused across every campaign. |
| Business hours, phone, address | Pulled from the connected Facebook page where possible. |
| Website | Never required. The lead form lives inside Facebook. |

---

## 3. Screen rules

- **One question per screen.** Six screens, a visible position indicator, back always available.
- **Saves on every keystroke.** An owner interrupted by a service call must lose nothing.
- **No question blocks progress except Q1.** Everything else has a default or a skip. A blocked
  wizard on a phone in a truck is an abandoned wizard.
- **Sixteen pixel inputs minimum**, per `docs/08`, because anything smaller triggers iOS zoom and
  the zoom never fully reverses.
- **Show the derived number immediately after Q3.** Do not make them reach the end to learn what
  the budget will be. `[INFERENCE]`
- **Total time target: under two minutes.** The landing page says two minutes. Instrument it and
  hold it.

---

## 4. Deepening later, not now

After the first campaign exists, the product asks for more, one item at a time, each attached to
a reason the owner can see: real photos, more offers for seasonal rotation, review counts,
service-specific pricing, crew size. Each addition improves the next generation and the product
says which. Front-loading these into intake is the most common way this product could fail
before an owner has seen a single ad. `[INFERENCE]`

---

## 5. Open questions for the founder

1. Should Q5 be voice? An owner talking for thirty seconds gives better material than an owner
   typing two sentences, and every one of them has a phone in their hand.
2. Is Q6 worth a slot, or is it better placed on the first rejection, where it would carry more
   context? Cutting it would give a five-question intake and a stronger landing-page claim.
3. Do we ask for the Meta connection before or after the six? Before means no wasted generation
   on an owner who cannot publish. After means they see value before granting access. The
   research in `docs/20` may settle this.
