# Ad Creative Spec: the composited photo ad

Status: v1 spec. Written 2026-08-19; compositor built 2026-08-20. **The fixed type sizes in
sections 1.4, 1.5, 2.1, 3.3 and 3.4 are superseded by the measured-width amendment in section
9 (25 Aug):** the original sizes never fit this document's own calibration strings in Public
Sans. Zone geometry, budgets-as-contract discipline, and everything else stand as written.

## 0. What this document is, and how to read a claim in it

This is the build specification for the image half of a generated ad: the square or portrait
picture with the logo, the price, the headline and the trust icons composited on top of a photo.
The copy half is owned by `docs/17-AD-COPY-PLAYBOOK.md`. The compliance half is owned by
`docs/14-AD-POLICY-RULES.md`. Neither is repeated here.

Three labels are used, and they never collapse into each other.

- **Unlabelled**: traceable to `docs/17-AD-COPY-PLAYBOOK.md`, `docs/14-AD-POLICY-RULES.md`,
  `docs/08-DESIGN-SYSTEM.md`, or `src/lib/trades.ts`, cited on the line.
- **`[INFERENCE]`**: my reasoning from those documents, not stated in them.
- **`[ASSUMPTION]`**: a guess with no evidence behind it. Treat every one as a question.

No performance number appears anywhere below. The company has zero customers, so there is
nothing to measure and nothing honest to say about conversion (`AGENTS.md` rule 3).

Spelling is British throughout. No em-dash or en-dash characters appear in this file, per
`AGENTS.md` rule 7.

**One thing to settle before reading section 1.** `docs/08-DESIGN-SYSTEM.md` is binding for the
product UI. It is not binding inside the ad creative: the composited image carries the
customer's brand, and the locked Cobalt 600 accent is ours, not theirs. What carries over from
that document into this one is the discipline, not the palette: WCAG ratios stated as numbers
and checked rather than eyeballed, one radius scale, no serif, no decorative dots, no
uppercase eyebrow used as a default pattern, and the em-dash ban applied to every string that
gets rendered into a pixel.

---

## 1. The anatomy of the composited ad creative

Six zones, stacked. The photo bed is the only one that is an image; the other five are drawn.
All coordinates below are given in a **1080 unit layout grid**, origin top left. Output is
rendered at 1.3333x scale to 1440x1440, because `docs/14-AD-POLICY-RULES.md` section 3 puts
Meta's recommended maximum at 1440x1440 for square and treats anything below 1080 as a hard
block (IMG-RES-01). Specify once at 1080, render up. [INFERENCE]

### 1.1 Zone map, 1080x1080

| Zone | Name | Y range | Height | Purpose |
|---|---|---|---|---|
| A | Logo lockup | 0 to 132 | 132 | Says who is talking, before anything is sold |
| B | Photo bed | 132 to 700 | 568 | The evidence: real work, real property, real crew |
| C | Price medallion | overlay on B | 360 dia | The offer, readable at thumbnail size |
| D | Headline bar | 700 to 820 | 120 | The promise in one line |
| E | Trust row | 820 to 976 | 156 | The reasons to let a stranger in the door |
| F | Tagline strip | 976 to 1080 | 104 | Brand sign-off, and a colour anchor |

Outer safe margin is 48 units on all four sides. Nothing but background fill crosses it. The
medallion centre sits at (540, 416), which is the optical centre of the photo bed rather than
the centre of the canvas. [INFERENCE] Placing it at the canvas centre (540, 540) would drop it
onto the boundary between the photo bed and the headline bar.

### 1.2 Zone A, logo lockup

- **Purpose.** Attribution. A local business ad that does not say whose it is wastes the
  strongest asset a local business has, which is being local and named (`docs/17` 2.3).
- **Contains.** The owner's logo, or the wordmark fallback from section 4.4. Optionally a
  second line of 1 short credential ("Licensed and insured", "Serving Boise since 2009").
- **Never contains.** The offer. A phone number. A CTA. A star rating. A second logo, including
  any manufacturer badge (Trane, Generac, Carrier) the owner did not supply and we cannot prove
  they are authorised to display. [INFERENCE]
- **Geometry.** Logo bounding box 460 wide by 96 tall, centred at (540, 66). Fitting rules for
  wide wordmarks are in section 7.3.

### 1.3 Zone B, photo bed

- **Purpose.** The only zone that carries proof. `docs/17` 6.2 cites Hook Agency's finding that
  a technician actually working on equipment, a marked truck in a real driveway, and before and
  after shots of the equipment or roof are what converts, and that stock photography of a
  smiling model and generic handshake imagery do not.
- **Contains.** One photograph, or two in a split (template T1, section 2.1).
- **Never contains.** Rendered text of any kind produced by the image model. Any text in this
  zone is composited by us, in a real font, on top. The reasons are in section 5.4.
- **Never contains.** A person's face at a scale where an AI-generated face is legible, when the
  photo bed is generated rather than supplied. [INFERENCE] `docs/17` 6.2 says template-produced
  imagery reads badly to this audience, and a synthetic face is the most reliable place for that
  to show.
- **Geometry.** Full bleed to the canvas edge horizontally, 132 to 700 vertically. The image is
  cropped to fill, never letterboxed. A 0 to 40 percent vertical dark scrim may be applied at
  the top edge only if zone A sits on the photo rather than on a solid band.

### 1.4 Zone C, price medallion

- **Purpose.** Carries the offer at a size that survives a thumbnail. `docs/17` 2.2 and 3
  document the price-led hook as the dominant pattern in HVAC and plumbing, with real figures
  from $17.75 to $99, and `docs/17` 6.1 reports that the common thread across the four
  longest-running ads found was offer clarity rather than any visual gimmick.
- **Contains.** Three text runs at most: a label line, the figure, an optional sub-line. Budgets
  in section 3.2.
- **Never contains.** A sentence. Fine print. Terms. An asterisk. A percentage with no anchor
  price (`docs/17` section 5 records that across roughly 90 live ads reviewed, not one used a
  bare percentage-off as its standalone offer). A monthly payment figure or any financing
  wording, because that pushes the whole ad into the CREDIT Special Ad Category under
  SAC-CRED-01 (`docs/14` section 1).
- **Geometry.** 360 diameter disc, centred at (540, 416). 24 units of clearance to every zone
  boundary and to the split seam. Ring stroke 6 units, which must clear 3:1 against whatever
  sits behind it (section 7.1). Sparkle marks, if used, are 4 units wide maximum and sit outside
  the disc, never over a numeral.
- **This zone is an offer container, not decoration.** If there is no offer, the zone is deleted
  and the template changes. Rules in section 3.4.

### 1.5 Zone D, headline bar

- **Purpose.** One line that says what the reader gets. In the founder's reference ad this is
  the two-colour "A CLEAN HOME. A BETTER YOU." bar.
- **Contains.** One line, up to two colour runs. Sentence-level punctuation only.
- **Never contains.** The price (that is zone C). A phone number. Two lines at square. Any
  guarantee word, because CLAIM-01 in `docs/14` is a regex BLOCK on `guarantee(d)?` and it will
  fire on composited text once the lint reads the rendered image (section 6.7).
- **Geometry.** Full bleed, 700 to 820. Text centred at (540, 760), cap height 56, tracking
  0.01em, weight 800. Solid background fill, never a gradient over photography.

### 1.6 Zone E, trust row

- **Purpose.** The credentials that let a stranger into a house. `docs/17` 2.4 documents
  credential-led ads running for a long time on nothing else, including a roofing ad reading
  "Licensed, bonded, insured, replacing roofs since 1988" still live after 690 or more days.
- **Contains.** 2 to 4 items. Each is one icon over two lines of small caps. Every item must be
  a credential the owner actually claimed at intake.
- **Never contains.** An invented credential used to fill a fourth column. A star rating or
  review count the owner did not supply (`AGENTS.md` rule 3, `docs/17` 4.5). A decorative status
  dot (`docs/08` section 6). The word "Guaranteed" as written in the reference ad, unless the
  owner has attached substantiation through the CLAIM-01 override path in `docs/14` section 8.
- **Geometry.** 4 items: columns of 270, icons 56 square, icon centre at y 872, text baselines
  at 918 and 946. Degradation to 3, 2 and 1 items is specified in section 7.4.

### 1.7 Zone F, tagline strip

- **Purpose.** Brand sign-off and the one place a saturated brand colour can run edge to edge
  without fighting the photo.
- **Contains.** One short line of the owner's own tagline.
- **Never contains.** A claim. A price. A CTA ("Call now"). A URL. `docs/17` section 5 names
  generic offer-free CTAs as a documented failure pattern, and a strip is exactly where one
  would get parked out of habit.
- **Geometry.** Full bleed, 976 to 1080. Text centred at (540, 1028), cap height 30, tracking
  0.06em. If the owner has no tagline, the strip is deleted and its 104 units go to the photo
  bed. Never auto-write one.

### 1.8 What changes at 1080x1350 portrait

The extra 270 units all go to the photo bed. Nothing else grows, because the drawn zones are
sized by legibility, not by proportion, and stretching them makes the ad read as a poster
rather than a photo. [INFERENCE]

| Zone | Portrait Y range | Height | Change |
|---|---|---|---|
| A | 0 to 132 | 132 | none |
| B | 132 to 970 | 838 | plus 270 |
| C | overlay, centre (540, 551) | 400 dia | plus 40 dia |
| D | 970 to 1090 | 120 | none |
| E | 1090 to 1246 | 156 | none |
| F | 1246 to 1350 | 104 | none |

Other portrait deltas:

- Output renders at 1440x1800, the portrait maximum named in `docs/14` section 3.
- The headline bar may run to two lines at portrait, which raises its cap from 34 to 60
  characters (section 3.2). If it does, zone D takes 176 units and the photo bed gives them up.
- The split seam in template T1 switches from diagonal to vertical at portrait. A diagonal seam
  across an 838 tall bed puts one photo's subject in a corner. [INFERENCE]
- Portrait is the better default for a feed placement and square is the safer default when the
  same asset has to serve more than one placement. [ASSUMPTION] Neither `docs/14` nor `docs/17`
  states a placement preference and I have no evidence for one.

---

## 2. The layout template system

Six templates. A template is a fixed arrangement of the six zones plus a rule about what fills
zone C. The trade category decides which templates are offered; the offer structure decides
which one is preselected.

### 2.1 T1, Split Proof

The founder's reference composition. Photo bed is split into two panels with BEFORE and AFTER
corner labels; the medallion sits on the seam.

- **Fits.** Any trade where the same physical thing looks different after the work, and where
  the difference photographs at thumbnail size.
- **Requires.** Two real photographs from the owner, same property, same angle. There is no
  fallback and no generated substitute. See section 4.5.
- **Offer structures it suits.** Named flat price for a defined scope, first-visit price.
- **Corner labels.** 96 by 40 plates, 6 unit radius, at (48, 180) and at (1032, 652) anchored to
  the opposite corner. Caps, 22 cap height, maximum 8 characters.
- **Policy note.** Property before and after is not a violation. `docs/14` section 2 states the
  restriction is a Health and Wellness rule about body-image framing, and that a roofing or deck
  pair is fine on its own. It becomes IMG-BA-01 when paired with a health claim.

### 2.2 T2, Price Medallion

One photograph, no split, medallion dead centre. The default template.

- **Fits.** Any trade with a bounded quotable price and no visible transformation.
- **Offer structures it suits.** The named-price tune-up or inspection and the named diagnostic
  fee, both documented in `docs/17` section 3 with real observed figures.
- **Anchors.** The $59, $49.95, $29 and $97 named-price ads in `docs/17` 1.1, 1.2 and 1.4.

### 2.3 T3, Free Offer

Same geometry as T2, medallion carries a word rather than a figure.

- **Fits.** Trades whose category-dominant offer in `src/lib/trades.ts` is a free inspection,
  free estimate or free assessment.
- **Offer structures it suits.** Free no-obligation inspection, the offer `docs/17` section 3
  records as dominant by a wide margin in roofing.
- **Mandatory extra.** For roofing specifically, `docs/17` section 3 says a generator producing
  this offer should pair it with a no-pressure line by default, because real advertisers are
  actively fighting the storm-chaser association this offer creates. That line goes in zone D,
  not in a fifth trust column.

### 2.4 T4, Credential Wall

No medallion at all. Photo bed shrinks to 132 to 640; a credential block of 3 stacked lines
takes 640 to 820; the trust row runs 4 items; zone D is deleted.

- **Fits.** Trades where trust is the binding constraint rather than price.
- **Offer structures it suits.** No discrete offer. `docs/17` 2.4 records a pure-credential
  roofing ad live 690 or more days with no discount and no urgency, and `docs/17` section 5
  records the counter-case that tenure-only copy is reported to fail as the entire message.
  Both readings are in the evidence, so this template exists but is never the default.

### 2.5 T5, Tier Card

Medallion replaced by 2 or 3 price cards in a row, each with a tier name, a figure and one line
of scope.

- **Fits.** Categories whose `dominantOffer` in `src/lib/trades.ts` already names tiers, bands
  or a recurring rate that must be disclosed.
- **Why it exists.** Four category watch-outs in `trades.ts` demand a disclosed second number:
  outdoor ("say the recurring price in the ad"), pool ("with the monthly rate stated"), pets
  ("put the size bands in the ad"), fitness ("with the ongoing membership price stated"). A
  single medallion cannot hold two numbers without breaking the budgets in section 3.2.
- **Geometry.** 3 cards of 296 wide by 300 tall, 24 gutters, radius 16, centred at y 416. At 2
  cards, 400 wide with a 64 gutter.

### 2.6 T6, Season Card

Medallion replaced by a date or season plate, 520 by 200, radius 16, with a season line and an
optional booking window.

- **Fits.** Demand that arrives on a calendar rather than on a symptom.
- **Offer structures it suits.** The local and seasonal skeleton in `docs/17` 4.4.
- **Hard constraint.** Name a season or a regional pattern, never a specific dated storm or
  disaster. `docs/14` TRADE-ROOF-02 blocks the second, and `docs/17` 2.5 records that every real
  storm-referencing ad found used seasonal framing instead.
- **Scarcity constraint.** If the plate carries a deadline, `offer.expiresAt` must be populated
  or URGENCY-01 fires (`docs/14` section 6).

### 2.7 The category matrix

Every category id below is from `src/lib/trades.ts`. Yes means offer it, Conditional means offer
it with the stated gate, No means the renderer does not list it.

| Category | T1 Split | T2 Price | T3 Free | T4 Credential | T5 Tier | T6 Season |
|---|---|---|---|---|---|---|
| mechanical | No | Yes | Yes | Yes | Conditional | Conditional |
| exterior | Yes | Conditional | Yes | Yes | No | Yes |
| interior | Yes | Conditional | Yes | Yes | Yes | No |
| outdoor | Yes | Yes | Yes | Conditional | Yes | Yes |
| cleaning | Yes | Yes | Conditional | Conditional | Yes | Conditional |
| pest | No | Yes | Yes | Yes | Yes | Yes |
| restoration | Conditional | No | Yes | Yes | No | Conditional |
| structure | Yes | Conditional | Yes | Yes | No | Conditional |
| access | No | Yes | Conditional | Yes | Conditional | No |
| pool | Yes | Yes | Conditional | Conditional | Yes | Yes |
| auto | Conditional | Yes | No | Conditional | Yes | Conditional |
| hauling | Conditional | Yes | Yes | Conditional | Yes | No |
| repair | Conditional | Yes | No | Conditional | No | No |
| specialty | Conditional | Conditional | Yes | Yes | Conditional | No |
| fitness | **Never** | Yes | Yes | Conditional | Yes | Conditional |
| pets | Conditional | Yes | Conditional | Conditional | Yes | No |
| events | No | Yes | Conditional | Conditional | Yes | Yes |

### 2.8 Why each row reads that way

**mechanical** (hvac, plumbing, electrical, solar, septic, water-treatment, well-drilling).
No split: a heat pump, a repipe and a panel upgrade look identical from the kerb, and the work
is inside a wall. T2 is the default because the category's `dominantOffer` is a named-price
inspection or tune-up and `docs/17` 1.1 records that pattern converging hard across every
long-running HVAC ad found. T5 conditional: maintenance plans exist but are not the ad's job.
T6 conditional: pre-season HVAC and generator storm preparedness are in the `docs/17` section 7
calendar; panel work is not seasonal.

**exterior** (roofing, gutters, siding, windows, exterior-painting, stucco, masonry, chimney,
awning). Split is strong here and it is the visible half of the trade. T2 is conditional, not
default: `docs/17` 2.2 states price lead is the weakest fit for roofing and that free beats a
named price in the observed sample. T3 and T4 are both first-class, which is unusual, because
`trades.ts` names the free inspection as the category offer and `docs/17` 2.4 and 6.3 both
document real advertisers spending copy on proving they are not storm chasers.

**interior** (interior-painting, drywall, flooring, tile, carpentry, cabinets, kitchen-remodel,
bath-remodel, general-remodel, handyman, insulation, closets). Split is strong. T2 conditional
because most of these are quoted after a visit, so a medallion figure would be a number the
owner cannot honour; handyman first-hour and per-room painting are the exceptions. T5 fits
room-count packages, which the category watch-out already implies by asking for a room count or
square footage in the ad.

**outdoor** (landscaping, lawn-care, tree-service, irrigation, sod, hardscaping, snow-removal,
land-clearing). Split is strong for lawn, tree, hardscape and clearing. T2 and T5 both apply,
and whichever is chosen, the `trades.ts` watch-out is binding: the recurring price is stated in
the ad, not buried. T6 is the strongest fit in the taxonomy for snow-removal.

**cleaning** (house-cleaning, commercial-cleaning, carpet-cleaning, pressure-washing,
window-cleaning, air-duct-cleaning). The category the founder's reference ad comes from, and
the best split candidate of the seventeen. T2 is equally strong given the category offer is a
flat price for a defined scope. The scope has to be visible somewhere in the composite, because
the watch-out says a price with no scope attached brings arguments at the door: put it in the
medallion sub-line or the headline bar. Air-duct cleaning gets an extra gate: a duct before and
after is fine as hardware, and `docs/14` section 5 puts "eliminate 99 percent of allergens" and
air-quality health framing squarely inside CLAIM-03.

**pest** (pest-control, termite, wildlife). No split, for two separate reasons. An insect
before and after is either invisible at thumbnail size or graphic enough to engage
IMG-PROHIBITED-01, and the category watch-out already says health and safety claims about what
an infestation does to a family get the ad rejected. T3 and T2 both match the category offer.
T4 matters because pest work is state-licensed.

**restoration** (water-damage, fire-damage, mold, asbestos, biohazard). Split is conditional and
the gate is tight: property only, water and fire only, never mould, never asbestos, never
biohazard, and never paired with any health wording in zones D, E or F. Three rules stack here:
IMG-BA-01 fires when a before and after is read as a health outcome, TRADE-MOLD-01 is a
soft-block on health claims about mould and air quality, and IMG-PROHIBITED-01 covers shocking
imagery, which `docs/14` section 3 names water-damage and mould photos as a live risk for. T2
is No: there is no flat price for a mitigation job. T4 and T3 carry this category.

**structure** (concrete, asphalt, foundation, fencing, decking, demolition). Split works for
sealcoating, concrete cleaning and levelling, deck restoration and demolition. T2 is
conditional and the watch-out is the reason: quoting a per-foot price without naming the
conditions that change it produces quotes the owner cannot honour, so a medallion carrying a
per-unit figure must also carry the condition in the sub-line.

**access** (garage-doors, locksmith, security-systems, gates). No split, because a lock, a
camera and an opener look the same before and after. T2 matches the category offer of a
named-price service call waived on booking. T4 is first-class: bonded and licensed is the whole
pitch for a locksmith. The watch-out bans danger framing, which is the same line `docs/14`
URGENCY-03 draws.

**pool** (pool-service, pool-construction). Green water to blue water is one of the clearest
transformations in the taxonomy, so T1 is Yes. T5 and T6 are both strong, and the category
watch-out is blunt about seasonality mattering more than the creative.

**auto** (auto-detailing, mobile-mechanic, auto-glass, towing, fleet-service). Split is
conditional and the gate is the trade, not the category: detailing yes, towing and glass and
mechanic no. T5 is the primary template because the category offer is literally a named package
price with the tiers shown. Whatever template is used, the service radius claim has to be one
the van will actually drive.

**hauling** (moving, junk-removal, dumpster, storage). Split is conditional: junk removal and
cleanouts are strong, moving and storage are not. T3 matches the category offer of a free quote
from photographs. T5 covers load and container sizes.

**repair** (appliance-repair, small-engine, electronics-repair, furniture-repair). Split is
conditional: furniture restoration yes, a washing machine no. T2 is the default and carries the
named diagnostic fee credited against the repair. T3 is No on purpose, because the category
watch-out states a free diagnostic brings tire-kickers and a named fee credited back filters
them.

**specialty** (welding, glass, av-smart-home, ev-charger, signage, marine, elevator,
home-inspection). Mostly T3 and T4, matching a free consultation with the typical project range
named. Split is conditional: signage and vehicle wraps yes, welding no. The watch-out flags
financing copy on high-ticket installs as a Special Ad Category trigger, which lands directly on
zone C (section 6.5).

**fitness** (gym, martial-arts, yoga-pilates, dance, swim-school). T1 is the one hard No in the
matrix, and it is a refusal rather than a warning. The `trades.ts` watch-out states before and
after imagery and body claims are a reliable Meta health-policy rejection and says to sell the
room and the coaching, not the body. `docs/14` section 2 says the same from the policy side:
body transformation comparisons and framing that manufactures negative self-perception are
prohibited under Health and Wellness. The renderer must not list T1 for this category at all,
because a template offered and then blocked teaches the owner that the software is broken, which
is the exact churn mechanism `docs/14` section 0 exists to prevent. T3 and T5 carry the
category, and T5 is the one that satisfies the watch-out's demand that the ongoing membership
price is stated.

**pets** (pet-grooming, dog-training, pet-care, veterinary). Split is conditional and the gate
is the trade: grooming yes, the other three no. A groomed dog is an animal, not a human body,
so the Health and Wellness body-image rule in `docs/14` section 2 does not engage. [INFERENCE]
That policy text is about the viewer's own body, and I could not find any statement either way
about animal before and after imagery. Veterinary gets a second gate: medical outcome wording
in any zone is CLAIM-03. T5 is the primary template because the category watch-out requires the
size bands in the ad.

**events** (photography, catering, event-rentals, entertainment). No split: a portfolio pair is
not a before and after, it is two nice photographs, and labelling one BEFORE misrepresents it.
T5 matches the category offer of a named package price, and T6 matches the watch-out that
date-driven demand makes an evergreen ad waste money.

---

## 3. The text layers, and their limits

### 3.1 Why budgets rather than autoshrink

Autoshrinking text to fit is how a medallion ends up with a 40 unit numeral that nobody reads at
thumbnail size. The budget is the contract: over budget is a generation failure that gets
regenerated, not a layout problem that gets solved by making the type smaller. [INFERENCE] The
one permitted step-down is named per zone below and is a single step, never a continuous fit.

### 3.2 Budgets

Counts are characters including spaces. "Cap" is the hard limit that fails generation; "target"
is what the copy generator aims at.

| Zone | Run | Target | Cap | Step-down allowed |
|---|---|---|---|---|
| A | Wordmark fallback (business name) | 24 | 32 | one step, then two lines |
| A | Credential line under the mark | 30 | 38 | none |
| B | BEFORE / AFTER corner labels | 6 | 8 | none |
| C | Label line above the figure | 11 | 14 | none |
| C | Figure | 4 | 7 | one step (see 3.3) |
| C | Sub-line below the figure | 10 | 12 | none |
| D | Headline bar, square | 27 | 34 | none |
| D | Headline bar, portrait two lines | 44 | 60 | none |
| E | Trust item, per line, 2 lines | 11 | 14 | none |
| F | Tagline strip | 40 | 46 | one step |
| T5 | Tier name | 10 | 14 | none |
| T5 | Tier scope line | 24 | 30 | none |
| T6 | Season line | 22 | 28 | none |

Calibrated against the founder's reference ad, which sits inside every one of these: "FIRST
CLEAN" is 11, "$99" is 3, "A CLEAN HOME. A BETTER YOU." is 27, the longest trust line is
"ECO-FRIENDLY" at 12, and "BRIGHT SPACES. TIDY PLACES. HAPPY FACES." is 40.

Two text fields sit outside the image and are not composited, so they are governed by `docs/17`
rather than by this document: the primary text above the image and the headline shown under it.
One note that belongs here anyway, because it changes what zone C has to carry: `docs/17` 6.2
records real ads (Air and Drain Works, MasterTex) carrying the full price and offer message in
the primary text field rather than baked into the image, and calls that the safer default for
AI-generated creative. Meta's own field character limits are not stated in `docs/14` or
`docs/17`, so any number the renderer enforces on those two fields is an `[ASSUMPTION]` until
someone checks Ads Manager (section 8, question 2).

### 3.3 Zone C when the offer is a dollar figure

- Figure is set in the same family as everything else, weight 700, optical cap height 168.
- Currency symbol at 62 percent of the numeral cap height, baseline aligned to the numeral top,
  not to the baseline.
- Cents, when present, at 48 percent, raised to the numeral cap line. This matters because the
  real observed prices in `docs/17` section 3 are frequently odd-cent figures ($17.75, $19.95,
  $20.26, $49.95), so cents are the normal case, not the exception.
- The single step-down: a figure of 6 or 7 glyphs ("$49.95", "$149.95") drops the numeral cap
  height to 132. Above 7 glyphs, generation fails. A four-figure price does not belong in a
  medallion; it belongs in a T5 tier card or in the primary text.
- Never put a range in the medallion ("$99-$149"). Two numbers in a disc read as one broken
  number at thumbnail size. [INFERENCE] Ranges go to T5.

### 3.4 Zone C when the offer is free

"FREE" is four wide letters, and setting it at numeral cap height makes it collide with the
disc. Rules:

- The word FREE sets at cap height 116, not 168, with tracking 0.02em.
- The label line above becomes optional and the sub-line becomes mandatory, because "FREE" alone
  states nothing. "FREE" over "ROOF INSPECTION" is the shape. The sub-line cap rises to 18
  characters in this case only, and wraps to two lines at 15.
- "FREE" is never combined with a struck-through anchor price inside the disc. The anchor goes in
  the headline bar if it is used at all, and CLAIM-04 in `docs/14` requires the offer object to
  carry a matching structured discount value or the claim gets flagged.
- If the free offer is conditional, the condition is composited or the offer is not free.
  `docs/17` 1.4 records a real conditional free inspection ("with any booked electrical
  service"), and `docs/14` section 2 puts unbacked free and discount claims under the same
  deceptive-practices standard. The condition goes in the sub-line, and if it does not fit in 18
  characters the template changes to T2 or T4.

### 3.5 Zone C when there is no price at all

There is no empty-medallion state and no placeholder. Specifically banned inside the disc:
"CALL FOR PRICING", "GET A QUOTE", "CONTACT US", "LEARN MORE", the business's own logo repeated,
a star rating, and a phone number. `docs/17` section 5 names generic offer-free CTAs as a
documented failure pattern, citing Hook Agency's finding that they get ignored for lacking
urgency or clear value, and `docs/13` is cited there independently reaching the same conclusion.

Instead, the renderer drops to a different template by this order:

1. If the owner supplied 3 or more credentials, use T4 Credential Wall.
2. Else if the offer is seasonal or date-driven, use T6 Season Card.
3. Else if two or more service tiers exist, use T5 Tier Card.
4. Else use T2 with the medallion deleted, the photo bed extended to 820, and the headline bar
   carrying the whole message.

Case 4 is the honest floor: a photograph, a name, a line, and the credentials. It is close to
the pure-credential roofing ad in `docs/17` 2.4 that has run for 690 or more days.

### 3.6 Rules that apply to every composited string

- No em-dash and no en-dash. `AGENTS.md` rule 7 covers UI copy; a rasterised string is UI copy
  that happens to be a pixel. Ranges use a hyphen.
- No uppercase eyebrow above the headline bar and no section numbering, per `docs/08` section 6.
  Zones E and F are caps because they are micro-labels at small size, not because caps are the
  house style.
- Owner-supplied strings are untrusted input (`AGENTS.md` rule 4). A tagline is data going into
  a renderer and into an LLM prompt, never an instruction.
- Every string that lands in the image goes through the copy lint, because after compositing it
  is no longer distinguishable from copy. Section 6.7.

---

## 4. What we must collect at intake to build this

The current wizard asks six required questions plus an optional depth section (`AGENTS.md`,
product paragraph). This document does not restate those six because they are not enumerated in
the files I read; what follows is what this composition needs, and whether each item already
exists is a question for the founder (section 8, question 1).

Three states only: **Required** blocks the build. **Optional with fallback** has a named
substitute. **Generated** means we make it and the owner can replace it.

### 4.1 Identity and brand

| Input | State | Fallback or note |
|---|---|---|
| Business name | Required | Already required for the ad itself |
| Logo file (PNG or SVG, transparent) | Optional with fallback | Wordmark lockup, section 4.4 |
| Primary brand colour | Optional with fallback | Section 4.3 |
| Secondary brand colour | Optional with fallback | Derived tint or tone of the primary |
| Tagline | Optional with fallback | Zone F is deleted. Never auto-written (1.7) |
| City or service area | Required | Drives the local proof hook in `docs/17` 2.3 |
| Year established | Optional | Omitted. Never estimated |

### 4.2 Proof and credentials

| Input | State | Fallback or note |
|---|---|---|
| Trust items, chosen from a fixed checklist | Optional with fallback | Row degrades, section 7.4 |
| Licence number and issuing state | Optional | Omitted. Real anchor: `docs/17` 1.1 records a live ad carrying "HVAC Lic#: 93485" in its copy |
| Insured, bonded, background-checked flags | Optional | Omitted if unclaimed |
| Review count and star rating | Optional, **never generated** | Zone E item is dropped. `AGENTS.md` rule 3 and `docs/17` 4.5 both forbid a fabricated number, and `docs/17` 4.5 says the social-proof skeleton should not be offered at all when the real count is unknown |
| Phone number | Optional | Not composited by default. `docs/17` 1.1 shows a real ad putting the number in the primary text, which is where it belongs (1.2, 1.4, 1.7) |
| Privacy policy URL | Required when the ad uses an Instant Form | No fallback. LEAD-01 in `docs/14` is a non-overridable block |

### 4.3 Brand colour derivation, in order

1. Owner typed a hex. Use it.
2. Owner uploaded a logo and no hex. Extract the dominant non-neutral colour by pixel frequency,
   ignoring anything under 12 percent saturation, and show it back for confirmation rather than
   applying it silently. [INFERENCE]
3. Neither. Fall back to a fixed colour per trade category, stored as data, one entry for each
   of the 17 categories in `trades.ts`. [INFERENCE]

Three rules bind all three paths. The product's Cobalt 600 is never used as a customer brand
colour; it is our accent, and `docs/08` 1.A locks it to the product UI. Any colour that fails
the contrast floors in section 7.1 gets darkened or lightened along its own hue until it passes,
and the adjusted value is what ships. At most two brand colours plus one neutral appear in a
single composite.

### 4.4 The fallback when there is no logo, exactly

Most owners will have neither a logo file nor a usable one, so this is a first-class path rather
than an error state. [ASSUMPTION] I have no data on what share of small trades businesses hold a
transparent logo file; I am assuming it is low.

The **Wordmark Lockup**:

- Business name set in the composite's single sans family, weight 700, tracking 0.01em, in the
  primary brand colour, or in the near-black neutral when the band behind it is coloured.
- One line up to 24 characters at cap height 44. From 25 to 32 characters, one step down to cap
  height 36. Over 32 characters, break to two lines at the last word boundary before the
  midpoint, cap height 32, leading 1.15.
- A 4 unit rule underneath, width matched to the text, in the secondary colour. This is the only
  decorative element permitted in zone A.
- Legal suffixes are dropped from the display string ("LLC", "Inc", "Co"), matching the stopword
  list already in `src/lib/trades.ts`. The full legal name still goes in the ad's advertiser
  field, which is Meta's, not ours.
- No monogram badge, no initials in a circle, no generated icon. A generated mark is a logo the
  business does not own and cannot reuse anywhere else. [INFERENCE]

### 4.5 The fallback when there are no photos, exactly

| Situation | What happens |
|---|---|
| No photos at all | Photo bed is generated to the prompt structure in section 5. T1 is not offered |
| One real photo | It is used. T1 is not offered |
| Two real photos, not a matched pair | Both usable in T2 as separate variants. T1 is not offered |
| A matched before and after pair | T1 unlocks |

**The renderer never generates a "before" image, and never generates half of a split.** A
synthetic before is fabricated evidence of work that was not done on a property that does not
exist, which is the same failure `AGENTS.md` rule 3 bans for statistics. It is also the exact
practice `docs/17` 1.3 flags when it documents the same long-form roofing story running verbatim
under two unrelated companies in two different states.

Honest note on the generated photo bed: `docs/17` 6.2 cites research that stock photography and
anything reading as template-produced does not convert, and generated imagery is closer to stock
than to a real truck in a real driveway. The fallback exists because the alternative is no ad at
all, not because it is as good. `docs/17` 6.3 adds that for roofing specifically, polished
creative can cost trust, so the intake should push hardest for real photos in exterior and
restoration.

### 4.6 Offer inputs

| Input | State | Note |
|---|---|---|
| Offer type (named price, free, tiered, none) | Required | Chooses the template |
| Price figure | Required when type is named price | Feeds the section 3.3 budgets |
| Scope line | Required for cleaning | The category watch-out demands scope with the price |
| Recurring rate | Required for outdoor, pool, pets, fitness | Category watch-outs demand disclosure |
| Condition on a free offer | Required when the free offer is conditional | Section 3.4 |
| `offer.expiresAt` | Required when any zone carries urgency or scarcity | URGENCY-01 is a block without it |
| `offer.discountValue` | Required when any zone claims a discount | CLAIM-04 structural check |

---

## 5. Image generation prompt structure, for the photo bed

This section covers generating the photo bed only. It does not cover generating the composite.
The composite is drawn deterministically by our renderer, never by an image model.

### 5.1 The eight-part prompt

Every photo bed prompt is assembled from the same eight parts, in this order. [INFERENCE] The
ordering and the parts are my design; `docs/17` 6.2 supplies what should be depicted, and
`docs/14` section 3 supplies what must not.

1. **Shot type.** Documentary, unposed, single frame.
2. **Subject and action.** A named worker doing a named task on named equipment. Never a portrait,
   never a handshake, never a smiling model, all three named as non-converting in `docs/17` 6.2.
3. **Setting.** A specific ordinary place: a driveway, a side yard, a utility closet, a kerb.
4. **Composition and negative space.** Where the subject sits and which region stays quiet.
   Section 5.2.
5. **Lighting.** Section 5.3.
6. **Colour restraint.** Two or three colours in the frame so the brand colours in the drawn
   zones do not fight the photo.
7. **Camera.** A plausible lens and distance, and a note that the frame is slightly imperfect.
   `docs/13` is cited in `docs/17` 2.3 for the finding that real and slightly imperfect beats
   polished.
8. **Exclusions.** Section 5.4.

### 5.2 Negative space planning

The medallion is a 360 disc at (540, 416) in a 1080 by 568 bed, which is a third of the bed's
width and nearly two thirds of its height. Nothing detailed survives underneath it, so the
prompt has to plan for it rather than let the compositor cover a face.

Three bands, and the prompt names them in plain language rather than in coordinates, because
image models do not honour coordinates. [INFERENCE]

- **Left third.** Subject and action live here. The prompt says "subject positioned to the left
  of frame, facing into the frame".
- **Centre third.** Reserved. The prompt says "the middle of the frame is open, uncluttered, low
  detail, a plain surface or a soft-focus background".
- **Right third.** Context: the truck, the house, the equipment, defocused.

For T1 splits this section does not apply at all. Both panels are the owner's real photographs,
and the work is alignment and cropping, not generation.

### 5.3 Lighting

Ask for the light that makes composited text land, not the light that wins a photography prize.
[INFERENCE]

- Overcast daylight, or open shade, or the hour after sunrise. Even, low contrast, no blown
  highlights.
- No hard direct sun across the centre third, because a bright patch under a light medallion is
  where the contrast check in section 7.1 fails and forces an ugly scrim.
- No lens flare, no bokeh balls, no golden-hour rim light. All three are the polish that
  `docs/17` 6.3 says can cost trust in roofing specifically.
- Slightly darker than neutral in the top strip if zone A is going to sit on the photo.

### 5.4 Why generating text inside the image is a mistake

Four reasons, three of them sourced.

1. `docs/14` section 3 states that large blocks of AI-rendered text inside an image are the most
   common visual tell of AI generation and the most likely place for garbled, misspelled or
   nonsensical text, because image models are weak at rendering legible text.
2. `docs/14` IMG-TEXT-01 measures text area by OCR against a 20 percent threshold. Text we
   composited has a known bounding box and a known area; text the model invented has neither
   until after the fact, so the lint cannot be run before spending the generation.
3. The 20 percent rejection rule is gone, but `docs/14` section 3 says Meta's delivery system
   still down-ranks heavy-text images at auction, so uncontrolled text costs the owner reach.
4. Composited text is editable, re-renderable, and hashable. Generated text is baked in, so any
   copy edit means paying for a new image, which runs straight into the per-organisation cost
   metering in `AGENTS.md` rule 6. [INFERENCE]

The exclusion clause is therefore mandatory on every prompt, in these words or equivalent: no
text, no letters, no numbers, no signage, no logos, no watermarks, no brand marks on vehicles or
uniforms, no readable licence plates.

### 5.5 Worked example, mechanical (HVAC tune-up, T2)

```
Documentary photograph, unposed. An HVAC technician in a plain grey work shirt kneeling
beside an outdoor condenser unit at the side of a single-storey suburban house, one hand
on a gauge manifold, looking at the reading. Technician positioned in the left third of
the frame, facing into the frame, seen from behind and to the side so the face is not the
subject. The middle of the frame is open and low detail: a plain wall of the house and a
patch of gravel, nothing to read. In the right third, a white service van at the kerb,
softly out of focus. Overcast daylight, even and low contrast, no hard shadows across the
centre, no lens flare. Three colours in the whole frame: grey, off-white, muted green.
Shot at 35mm from standing height, slight handheld tilt, ordinary and slightly imperfect.
No text, no letters, no numbers, no signage, no logos, no watermarks, no brand marks on
the van or the uniform, no readable licence plates.
```

### 5.6 Worked example, cleaning (house cleaning flat price, T2 fallback when no photos)

```
Documentary photograph, unposed. A cleaner in a plain uniform wiping down a kitchen
worktop in an ordinary lived-in family kitchen, mid-motion, seen from the side at
three-quarter angle. Cleaner positioned in the left third of the frame. The middle of the
frame is open and low detail: a clear stretch of worktop and a plain painted wall behind
it. In the right third, a kettle and a bowl of fruit, softly out of focus, so the room
reads as a real home rather than a showroom. Bright indoor daylight from a window out of
frame, even, no blown highlights on the worktop, no sun patch in the centre. Three colours
in the whole frame: warm white, pale wood, muted blue. Shot at 35mm from standing height,
slightly imperfect framing. No text, no letters, no numbers, no signage, no logos, no
watermarks, no readable packaging labels.
```

### 5.7 Worked example, outdoor (tree service free estimate, T3)

```
Documentary photograph, unposed. An arborist in a helmet and hearing protection standing
at the base of a large mature oak in a residential front garden, looking up into the
canopy, one hand resting on a coiled climbing rope over the shoulder. Arborist positioned
in the left third of the frame. The middle of the frame is open and low detail: mown grass
and the plain trunk, nothing to read. In the right third, a chipper and a pickup at the
kerb, softly out of focus. Open shade under high cloud, even light, no dappled sun on the
grass in the centre of the frame, no golden rim light. Three colours in the whole frame:
green, brown, off-white. Shot at 35mm from standing height, slight handheld tilt. No text,
no letters, no numbers, no signage, no logos, no watermarks, no brand marks on the truck,
no readable licence plates.
```

---

## 6. Meta policy constraints on the creative specifically

Everything in this section traces to `docs/14-AD-POLICY-RULES.md`.

### 6.1 Before and after imagery

The restriction is a Health and Wellness rule about body-image framing, not a blanket ban on
before and after photography (`docs/14` section 2). A roofing or deck pair is not itself a
violation. It becomes IMG-BA-01, a soft block, when it is paired with a health claim or framed
to manufacture fear about the homeowner's own health or safety rather than about the property.

Applied to T1:

- Allowed by default for the categories marked Yes in section 2.7.
- The classifier that decides IMG-BA-01 reads the image and the copy together (`docs/14` section
  7), so a compliant photo pair can be pushed into a violation by whatever the headline bar or
  the tagline strip says. The headline bar is the highest-risk string in the whole composite for
  this rule. [INFERENCE]
- Never offered for the `fitness` category (section 2.8).
- Restoration is gated to property outcomes only, and mould, asbestos and biohazard are excluded.

### 6.2 The 20 percent text rule in 2026

Dead as a rejection trigger. `docs/14` section 3 cites the removal directly and states that an
image with heavy text overlay will no longer be auto-rejected for that reason alone. Two things
survive it: Meta's delivery system still down-ranks heavy-text images at auction, and heavy
in-image text is the clearest visual tell of AI generation. IMG-TEXT-01 is therefore a WARN, not
a BLOCK, measured as OCR text area over 20 percent of image area, and `docs/14` specifies the
owner-facing message should say this may hurt how many people see the ad rather than cite a
rejection risk that no longer exists.

**This composition will trip IMG-TEXT-01, and the founder should know that before we build it.**
Zones A, D, E and F are all text, and D, E and F alone occupy 380 of 1080 units of height, which
is 35 percent of the canvas before the medallion, the corner labels and the logo are counted.
The OCR text-area ratio measures glyph coverage rather than band area, so the true figure will
be lower than 35 percent, but a four-item trust row plus a full-width headline bar plus a
tagline strip plus a medallion is a lot of glyphs. [INFERENCE] This does not block anything. It
does mean the reference composition trades reach for clarity, and that is a decision the founder
should make on purpose (section 8, question 5).

Two mitigations exist inside the spec already: the character budgets in section 3.2 cap total
glyph count, and the degradation rules in section 7.4 remove trust items rather than pad them.

### 6.3 Personal attributes

ATTR-01 and ATTR-03 are non-overridable blocks; ATTR-02 and ATTR-04 are LLM warnings (`docs/14`
section 6). The operative line, from `docs/14` section 2, is not whether the copy says "you" but
whether "you" attaches to a protected attribute or a claim of surveillance. "Is your AC broken"
is fine because it asserts a fact about equipment.

For the creative specifically:

- The headline bar is the zone most likely to drift, because it is the one that reaches for a
  feeling. The founder's reference headline, "A CLEAN HOME. A BETTER YOU.", is a clean example
  of the risk shape without crossing it: it says something about the reader, but nothing about a
  protected attribute or a health state. [INFERENCE] The same slot filled with a body,
  financial or health state would cross.
- Zone E is safe by construction, because it holds credentials about the business rather than
  statements about the viewer.
- SAC-VISUAL-01 is a WARN on the image itself for housing, employment and credit visual signals.
  `docs/14` section 1 records that Meta's multimodal review scans image and text together and
  applies category restrictions whether or not the advertiser declared them.

### 6.4 Health claims

CLAIM-03 and TRADE-MOLD-01 are soft blocks driven by a shared classifier (`docs/14` sections 5
to 7). The safe framing describes the service, not a medical outcome: mould inspection and
removal is fine, mould destroying a family's health is not.

Composite-specific consequences:

- The tagline strip is a standing risk for this rule, because a tagline is where a business
  reaches for a feeling in fewest words. "Breathe easier" over a duct-cleaning photo is a health
  claim in two words. [INFERENCE]
- The 20 percent of the taxonomy where this fires hardest: `restoration` (all five trades),
  `pest`, `air-duct-cleaning` inside `cleaning`, `veterinary` inside `pets`, and every trade in
  `fitness`. The `trades.ts` watch-outs for pest, restoration and fitness say the same thing in
  the founder's own words.

### 6.5 Financing text in an image

This is the one that costs the most if it is wrong, because it does not reject an ad, it changes
the entire ad set's targeting. `docs/14` section 1 lists what declaring a Special Ad Category
strips: no ZIP-level targeting, a 15-mile minimum radius in the US, age locked to 18-65+, no
detailed interests, no exclusions, no lookalikes.

Rules for the composite:

- No monthly payment figure, no APR, no "0 percent", no "as low as", no lender brand name, in any
  zone. CREDIT_SIGNALS_TIER_A and NAMED_LENDER_BRANDS in `docs/14` section 1 are keyword lists
  and SAC-CRED-01 is a non-overridable block.
- No credit card imagery, no loan calculator, no cash imagery in the photo bed. `docs/14` section
  1 names these as visual credit signals and SAC-VISUAL-01 exists to catch them.
- `docs/17` 1.4 records a real live ad using "credit scores as low as 550", and `docs/17` section
  9 leaves it to the founder whether the product blocks that language outright or allows it with
  a disclosure step. Whichever way that is settled for copy, the medallion is the wrong place for
  it: a financing figure in the disc makes financing the offer rather than a payment option,
  which is exactly the Tier A distinction `docs/14` draws.
- The categories where this fires most, per the `trades.ts` watch-outs: `interior`, `specialty`,
  `exterior`, and the generator and panel work inside `mechanical`.

### 6.6 Resolution, cropping and disclosure

- IMG-RES-01 blocks anything under 1080 on either axis and is not overridable. Rendering at
  1440 gives headroom.
- Excessively cropped images designed to force a click fall under Low Quality or Disruptive
  Experiences (`docs/14` section 3). Practical rule: the medallion, the logo and the headline bar
  never touch or cross the canvas edge, so nothing reads as cut off.
- IMG-AI-DISCLOSURE-01 is a non-overridable block on export pack completeness, not on the ad.
  `docs/14` section 3 states that because every image the product generates is AI-generated by
  definition, the AI disclosure instruction is a mandatory line item in every export pack rather
  than a conditional one.

### 6.7 What the lint must check on the composited creative, not just the copy

This is the largest gap between `docs/14` as written and what this document builds. The rule
table in `docs/14` section 6 applies copy rules to `appliesTo: "copy"`, meaning the headline,
primary text and description fields. **After compositing, the headline bar, the trust row, the
tagline strip and the medallion are text that no copy rule will ever read.** A generated
headline can pass the lint, get composited, and ship with a guarantee word inside the image.

The founder's own reference ad demonstrates it. Its fourth trust item reads "Satisfaction
Guaranteed", and CLAIM-01 in `docs/14` is a regex block on `\bguarantee(d)?\b`. Composited, that
string is invisible to the current lint.

Proposed additions, all `[INFERENCE]`, all new rule ids that do not exist in `docs/14`:

| Proposed id | What it checks | Severity |
|---|---|---|
| COMP-01 | Every composited string is concatenated into a synthetic copy blob and run through every `appliesTo: "copy"` rule in `docs/14` section 6 | inherits each rule's severity |
| COMP-02 | OCR is run over the final rendered PNG and its output is diffed against the strings we believe we composited. Any text OCR finds that we did not draw came from the image model and the photo bed is regenerated | BLOCK |
| COMP-03 | IMG-TEXT-01's OCR area ratio is measured on the final composite, not on the photo bed | WARN |
| COMP-04 | Contrast floors from section 7.1 are met for every drawn text run against its actual local background | BLOCK, not overridable, because it is a measurement rather than a judgement |
| COMP-05 | The rendered image bytes are included in the content hash that the approval gate reads | BLOCK |
| COMP-06 | T1 is not selectable for the `fitness` category, and is gated for `restoration` per section 2.8 | BLOCK |
| COMP-07 | No zone carries a monthly payment, APR, lender brand or credit-signal string (section 6.5) | BLOCK, not overridable |
| COMP-08 | Every trust row item resolves to a credential the owner claimed at intake, with no filler | BLOCK |

COMP-05 deserves its own line because it touches an inviolable rule. `AGENTS.md` rule 1 says no
ad reaches an export pack without a persisted approval record whose content hash matches the
ad's current content, and that editing an ad after approval invalidates the approval by design.
If the composited image is outside the hash, re-rendering it after approval changes what the
owner is about to publish without invalidating anything. Which is why section 7.5 requires a
deterministic renderer.

---

## 7. The compositing rules the renderer must enforce

### 7.1 Contrast minimums over photography

Thresholds are taken from `docs/08` 1.C, which computes WCAG 2.1 relative luminance directly:
4.5:1 for normal text, 3:1 for large text and for non-text elements such as borders and rings.

Applied to a photograph rather than a flat token:

1. For each drawn text run, take its bounding box plus 8 units of padding.
2. Sample the composited pixels underneath at a fixed grid, compute relative luminance per
   sample, and take the **worst** sample, not the mean. A mean passes happily over a photo that
   is half black sky and half white gutter. [INFERENCE]
3. Compare the text colour against that worst sample.
4. Large text is anything at cap height 34 or above, which covers the medallion figure, the
   headline bar and the wordmark. Everything else is normal text.
5. On failure, apply remedies in this order, stopping at the first that passes: a solid plate
   behind the run, then a linear scrim on the underlying region at up to 70 percent, then a
   colour swap to the neutral endpoint of the brand palette. **Never a text shadow and never a
   stroke on the glyphs.** Both are legibility patches that read as amateur and neither produces
   a measurable ratio. [INFERENCE]
6. The medallion ring, the icon strokes in the trust row and the corner label plates are non-text
   and take the 3:1 floor.

Zones D, E and F sit on solid fills, so their ratios are computed once from tokens and are known
before render. Only zone A, zone C and the T1 corner labels sit over photography.

### 7.2 Safe areas

- 48 units of outer margin at both aspect ratios. Background fill may cross it; nothing else may.
- 24 units of clearance between the medallion and any zone boundary, any split seam, and the
  canvas edge.
- No text within 16 units of a zone boundary.
- The medallion never overlaps the T1 seam label plates.
- On a T1 diagonal split, the seam passes behind the medallion and is drawn first, so the disc
  interrupts it cleanly rather than the seam running through a numeral.

### 7.3 Logos, including wide wordmarks

The zone A box is 460 wide by 96 tall. Classify by aspect ratio and fit accordingly.

| Aspect ratio (w:h) | Class | Fit rule |
|---|---|---|
| under 1.4 | Square mark | Fit by height to 96. Width will not exceed 135 |
| 1.4 to 4.0 | Standard lockup | Fit by height to 72, then clamp width to 460 if it exceeds |
| over 4.0 | Wide wordmark | Fit by width to 460 and let height fall, down to a floor of 40 |
| over 11.5 | Unusable | Reject the upload and fall back to the section 4.4 wordmark |

Then centre the fitted result vertically inside the 132 unit band, which keeps a 40 unit tall
wordmark and a 96 unit tall square mark optically in the same place.

Other logo rules:

- A logo with a non-transparent background is placed on a white plate at radius 12 with 12 units
  of padding, rather than keyed out. Keying a JPEG produces fringing. [INFERENCE]
- A logo whose own contrast against the zone A background falls below 3:1 gets the same white
  plate. The logo colours are never altered.
- Logos are never recoloured, tinted, outlined, drop-shadowed or placed inside a circle.
- Rasterised uploads under 2x the fitted size are rejected at intake with a plain-English reason,
  not silently upscaled.

### 7.4 Trust row degradation

Four items is the reference composition. Most owners will claim fewer. [ASSUMPTION]

| Items | Layout | Notes |
|---|---|---|
| 4 | 4 columns of 270, icons 56 | Reference layout |
| 3 | 3 columns of 360, icons 60, same band height | Text budgets unchanged |
| 2 | 2 columns of 400, centred, 140 gutter, icons 64 | Text budgets unchanged |
| 1 | Row deleted, 156 units returned to the photo bed | A single icon in a full-width band reads as a mistake or a missing asset [INFERENCE] |
| 0 | Row deleted, 156 units returned to the photo bed | |

The row never pads to four with a credential the owner did not claim. Icons scale with the
column and the text budget in section 3.2 never changes, so a two-item row is a larger version
of the same thing rather than a different design.

### 7.5 Determinism, and why it is not a nice-to-have

Same inputs must produce the same output bytes. No random seeds in the drawing layer, no
timestamps in metadata, no font fallback that varies by host, no anti-aliasing that varies by
renderer version. `AGENTS.md` rule 1 makes the approval gate hash-based, COMP-05 puts the image
inside that hash, and a non-deterministic renderer would then invalidate every approval on every
re-render. [INFERENCE]

The photo bed is generated once and stored as an input to the composite, not regenerated at
render time. This also keeps `AGENTS.md` rule 6 satisfiable: image generation is metered per
organisation, compositing is local and free, and an owner nudging a headline must not cost a new
generation.

### 7.6 Type discipline inside the composite

- One family for every zone. No second family for the numeral, despite `docs/08` 2.A using a
  mono face for product figures. That choice is about a dashboard readout; the medallion is a
  price on a poster. [INFERENCE]
- No serif anywhere, matching the standing ban in `docs/08` section 6.
- The family must carry an embedding licence that permits rasterised commercial output, since
  every render is a commercial image distributed by a third party. This is unresolved (section 8,
  question 8).
- One radius scale across the composite: 6 for corner labels, 12 for logo plates, 16 for tier and
  season cards. Nothing else has corners.
- Kerning and tracking are set per zone in this document and are not adjusted to make text fit.
  Fitting is the character budget's job.

---

## 8. Open questions for the founder

Stated as questions rather than guessed at.

1. **What are the current six intake questions, exactly?** I could not find them enumerated in
   any file I read, so section 4 lists what this composition needs without knowing what overlaps.
   The delta is what actually gets added to the wizard, and I cannot compute it.

2. **What are Meta's real character limits on primary text, headline and description in 2026?**
   Neither `docs/14` nor `docs/17` states them. Every limit the product enforces on the two
   non-composited fields is a guess until someone reads Ads Manager.

3. **Will owners actually supply a matched before and after pair?** Template T1 is the founder's
   reference composition and it is the only one with a hard input requirement and no fallback. If
   the real answer is that almost nobody uploads two aligned photographs, T1 is a demo rather than
   a product and T2 is the thing to build first.

4. **Does compositing our text over the owner's real photograph count as AI-substantially-modified
   for Meta's AI disclosure?** `docs/14` section 3 makes disclosure mandatory because every image
   we generate is AI-generated, but a real photo with drawn text on it is a different case, and
   `docs/14` also notes that policy is not yet pinned to a stable official URL.

5. **Is the reach cost of this composition acceptable?** Section 6.2 explains that the reference
   layout is text-heavy enough to be a live IMG-TEXT-01 candidate, and `docs/17` 6.2 observes
   real long-running ads keeping the price and offer in the primary text rather than in the
   image. The founder is asking for the opposite. That may well be right, but it should be a
   decision rather than a default.

6. **Should the phone number ever be composited?** Real ads put it in the copy (`docs/17` 1.1).
   Owners are likely to ask for it in the image. I have no evidence either way.

7. **Are there state advertising rules requiring a licence number in the creative?** Several
   `trades.ts` categories are state-licensed, and `docs/17` 1.1 shows a real advertiser putting a
   licence number in the copy. Whether any state requires it in the ad itself is a legal question
   I cannot answer from these documents.

8. **Which typeface can we embed?** Public Sans and IBM Plex Mono are chosen for the product UI in
   `docs/08` 2.A. Rasterising a face into a commercial image distributed by a customer is a
   different licence question from serving it as a webfont, and I did not verify it.

9. **Should brand colour extraction from an uploaded logo be automatic or confirmed?** Section 4.3
   proposes confirmation, which costs a wizard step. Silent extraction is faster and occasionally
   picks a colour the owner hates.

10. **What happens for a genuinely multi-trade business?** `trades.ts` matches one trade per query
    and `docs/17` 2.7 documents cross-trade bundle offers as real but only usable by a business
    that offers both. Whether one composite can carry two trades, or whether that is two ads, is
    unresolved.

11. **Is the trade-category colour fallback in section 4.3 acceptable at all?** It means two
    cleaning companies in the same city with no logos get the same colour. The alternative is
    making the colour question required, which adds friction to intake for an audience that is
    reading a phone between jobs.

12. **Does the founder want the medallion to be able to carry a struck-through anchor price?**
    `docs/17` records a real ad running "$49 (regularly $85)" and section 3.4 currently bans a
    strike-through inside the disc on legibility grounds. That is my call, not evidence.

---

## 9. Amendment, 25 August 2026: measured-width fitting

Operator amendment after the first probe renders of the built compositor. The founder can veto
any line of it; the sizes are frozen in `src/lib/composite/layout.ts` and every one is exercised
by the test suite.

**What was found.** The character budgets in 3.2 bound length but not pixels, and the fixed cap
heights in 1.4, 1.5, 3.3 and 3.4 were set without measuring Public Sans. Rendered at the specified
sizes, the calibration strings this document itself uses as proof of fit did not fit: "FIRST
CLEAN" at cap 36 measures 329 units against a disc chord of 42 at its band, "$99" at cap 168
measures 406 against a 298 chord, the word FREE at cap 116 is wider than the whole 360 disc, and
"A CLEAN HOME. A BETTER YOU." at cap 56 measures 1255 against the 984 units between the bar
margins, so it wrapped and clipped. A circle is narrowest exactly where the label and sub-line
sit, which flat budgets cannot express.

**What changed.** The advance widths of the exact woff files the renderer embeds are now a
generated table (`src/lib/composite/font-metrics.ts`), and every composited run is measured
against its zone geometry before rendering. A run inside its character cap that still measures too
wide is a typed generation failure (`textDoesNotFit`) fed back to the copy model, exactly like an
over-budget count. Nothing autoshrinks; the 3.1 discipline stands. The named fixed sizes were
re-solved so that the worst legal string of each shape fits with margin:

| Run | Was | Now |
|---|---|---|
| Figure, up to 3 glyphs ("$99") | 168 | 124 |
| Figure, 4 to 5 glyphs, no cents ("$999") | 168 | 92 |
| Figure, cents or 6 to 7 glyphs ("$49.95") | 132 | 72 |
| FREE | 116 | 80 |
| Medallion label / sub-line | unstated | 22 / 20 |
| Headline bar | 56, no step | 56, one step to 42 on measured width |
| Tagline step 30 to 26 | at 41 characters | on measured width |
| T4 credential block | unstated | 36, one step to 30, block steps as one |
| T5 tier figure | unstated | 50 (holds "$9,999" in a 3-up card) |
| T6 season line | 40 | 40, or two wrapped lines at 32 |
| Corner label plates (2.1) | fixed 96 by 40 | text width plus 24, minimum 96 ("BEFORE" at cap 22 is 123 wide) |

Two consequences written into code rather than left implicit: a four-figure price in the
medallion is now a typed refusal (`fourFigureInMedallion`), which 3.3 already stated in prose;
and the portrait headline may break to two planned lines at 56 or 42, with the break computed at
validation so the renderer draws exactly what was measured.

**Why the figure shrank so much.** Cap 168 was measured off the founder's reference ad by eye.
The reference disc is proportionally larger than the 360-unit zone C disc this spec fixed, and
the maths does not care: at 168 the numerals plus the 62 percent currency symbol are wider than
any chord of the disc that also holds a label and a sub-line. 124 is the largest short-figure
size at which the full reference stack ("FIRST CLEAN" / "$99" / "3 BED HOMES") sits inside the
circle with real margin. The probe renders before and after are the evidence; the containment
test in `src/lib/__tests__/composite-render.test.ts` keeps it true.
