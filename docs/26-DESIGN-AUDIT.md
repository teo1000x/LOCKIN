# Design audit: why V1 reads as generic, and what survives the pivot

_Written 2 September 2026, the design pivot's phase 1. The founder's verdict on V1: "feels
like AI slop, the generic UI of a vibe-coded site." This audit names the causes precisely so
the redesign fixes causes, not symptoms. Diagnosis method: the redesign skill's audit
checklist run against the live code._

## The one-paragraph verdict

Every screen follows docs/08 and the taste rules, and that is exactly the problem: the
system optimised for inoffensiveness. Public Sans (the U.S. government's deliberately
neutral typeface), one safe cobalt on white and cool grey, centered hero with a badge pill
and a filled-plus-outline button pair, three equal proof columns with icons in boxes, white
rounded cards on a grey app shell with a left sidebar. Each choice is defensible; the sum is
a site that could belong to any of ten thousand SaaS products. Nothing on any screen could
ONLY belong to a company that gets tradespeople booked jobs.

## What is genuinely good and must survive

1. **The copy voice.** Plain, specific, leads-jobs-dollars. "Your first clean is $99 for
   most 3 bed homes" is real differentiation; almost no competitor writes like this. The
   redesign amplifies it with type; it does not touch the words' character.
2. **The honesty patterns.** Measured-vs-reported labels, honest empty states, the
   set-aside explainer, no fake numbers. These are brand assets waiting for a brand.
3. **The token discipline.** Every colour, radius and type size routes through
   `globals.css` tokens and docs/08. Swapping the skin is a token rewrite plus targeted
   layout work, not a hunt through hardcoded hex values.
4. **The craft baseline.** 16px inputs, focus rings, reduced-motion support, WCAG-checked
   pairings, no-JS-safe reveals. The Vercel interface guidelines (installed 1 Sep) extend
   this list; nothing regresses.
5. **Founder-locked constraints:** light mode only (contractors in daylight), low motion,
   phone-first reading. The pivot changes the look, not these physics.

## The generic fingerprints, by surface

### Landing page
- **Hero:** centered stack, pill badge above the H1, filled + outline CTA pair, browser
  -chrome product screenshot below. This is the canonical AI-SaaS template, item for item.
- **Type:** Public Sans everywhere; hero caps at 48px desktop, weight 800; the page has no
  typographic moment anyone would remember. Headlines lack presence and there is no display
  face at all.
- **Colour:** the fingerprint cobalt-on-white. Accent saturation and hue sit exactly where
  every default SaaS palette sits. The faint drafting-grid texture is the one original
  gesture and it is tuned to be subliminal (5% alpha).
- **Depth:** zero photography, zero material texture, no overlap, no broken grid. Flat
  vector cleanliness end to end, in a product whose entire subject is physical work.
- **Sections:** three-equal-columns proof strip with icons in rounded boxes; pricing as
  three towers; accordion-adjacent FAQ; footer link columns. All template grammar.

### App shell
- Default left-sidebar dashboard with white cards on `#f6f7f9`. Structurally identical to
  every admin template. The one primary action (New campaign) is right, but the shell
  communicates "generic dashboard", not "your foreman".

### Wizard
- Competent per-screen form. The founder's own critique stands: it renders like a generic
  questionnaire while the per-trade intelligence (radius defaults, offer library, budget
  arithmetic) stays invisible until after generation. The smarts exist in code and never
  perform on stage. (Founder asks noted 1 Sep: denser, recommended settings shown, richer
  metrics; the one-page-versus-per-screen question is settled inside the pivot.)

### Approval workspace and export
- The strongest screens (real ads, real reasons, honest set-asides) rendered in the same
  anonymous card grammar, so the product's most differentiated moment looks the least
  differentiated.

## What the fix is, and is not

Not decoration: no gradients, glassmorphism, or motion for its own sake, and none of it
would survive the audience anyway. The fix is **conviction in four places**:
1. **A typeface with character**, sized like it means it (the checklist's highest-impact,
   lowest-risk change).
2. **A palette that belongs to the trades world**, not to software. The direction boards
   decide it; the current cobalt does not survive by default.
3. **Material and texture**: the product sells physical work and shows none of it.
   Photography, paper, steel, print-shop textures are all candidates; boards decide.
4. **Visible intelligence in the app**: recommendations that announce themselves, a plan
   that assembles beside the questions, numbers set in type that respects them.

## Phase plan (agreed with the founder, 26 Aug)

1. This audit.
2. Three genuinely different direction boards from research; founder reacts.
3. docs/08 rewritten to the chosen direction (it stays the binding authority).
4. Implementation: landing first, app second, checked against taste-skill AND the Vercel
   interface guidelines.

Name status: still "Foreman" as placeholder; boards are built palette-and-type first,
wordmark-light, so the name decision does not block them.
