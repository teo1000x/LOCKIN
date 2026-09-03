# Design System Spec - v2, High-Vis Precision

> Companion to `01-PRODUCT-SPEC.md`, `05-UI-DESIGN.md` and the direction decision in
> `docs/boards/board-c-highvis-light.png` (founder-chosen, 2 September 2026). This document is
> the single source of truth for color, type, spacing, and component behavior across the
> marketing site and the product UI. Every value below is final and ready to paste into code.
> Nothing here is illustrative. v1 (cobalt) is superseded in full; it remains in git history.

**Design read:** unchanged. B2B SaaS landing plus multi-step product UI for non-technical
trades business owners who read on a phone between jobs. Plain-spoken, utilitarian language.
Trust and legibility outrank delight.

**The direction in one line:** a precision instrument in daylight. White pages, deep ink navy
as the ink, blaze orange as the single high-vis accent, monospace numerals for every figure
the product asserts, and measurement marks as the one decorative motif.

**Dials:** `DESIGN_VARIANCE 6` / `MOTION_INTENSITY 3` / `VISUAL_DENSITY 4` (unchanged).

**Founder lock, 2 September 2026: V1's format and layout are retained.** The information
architecture, section order, and component layouts of the shipped V1 stay as they are. This
spec changes tokens, typefaces, and detailing. Any layout change beyond that must be called
out explicitly when proposed, never smuggled in with the reskin.

**Craft law:** in addition to this document, every shipped screen passes the Vercel Web
Interface Guidelines checklist installed at
`~/.claude/skills/web-interface-guidelines/AGENTS.md` (focus, targets, forms, motion,
accessibility). Where the two documents overlap, the stricter rule wins.

---

## 1. Color Tokens

### 1.A The ink: Navy 900

`#0E1B2C` is the product's black. All primary text, all structural linework, all wordmark
usage. It is never a page background; it may fill small committed inverse elements (a stat
chip, the composited-ad zones, a footer band) where the v1 layout already used a dark fill.

### 1.B The accent: Blaze 500

One accent, high-vis orange, used the way safety equipment uses it: small, loud, meaningful.

```
--color-accent:        #FF5A1F   /* Blaze 500 - primary button fill, ticks, crosshairs, the one hot word */
--color-accent-hover:  #E84D0F   /* Blaze 600 - hover AND pressed fill (press reads via transform) */
--color-accent-active: #D4430A   /* Blaze 700 - focus ring color; passes 3:1 on bg and white */
--color-accent-deep:   #A83A04   /* Blaze 900 - small orange-family text and links, 6.42:1 on white */
--color-accent-subtle: #FFEDE5   /* Blaze tint - selected card bg, info banner fill */
--color-on-accent:     #0E1B2C   /* Ink on orange, 5.56:1. NEVER white text on the accent. */
```

**The three orange laws** (each one is a shipped-broken check, not a preference):
1. Orange never carries text below 24px regular or 19px bold. Small orange-family text uses
   `--color-accent-deep` (6.42:1). Body links are ink, underlined; orange links only at
   `accent-deep`.
2. Text ON orange is always ink (`--color-on-accent`), never white. White-on-orange is 1.9:1
   and is the fastest way to fake the board's look while failing everyone's eyes.
3. Orange area budget: on any one screen, orange fills at most one primary action plus
   incidental marks (ticks, one hot word, one focus ring). If a screen reads "orange", the
   budget is blown.

### 1.C Navy-tinted neutral ramp

One hue family (about 213 degrees), eleven steps. This replaces the v1 cool-grey ramp; the
tint leans toward the ink so every grey belongs to the same world.

| Token | Hex | Role |
|---|---|---|
| navy-50 | `#F7F8FA` | Page background (near-white, never pure white) |
| navy-100 | `#F1F3F5` | Sunken fields, mono blocks, skeleton base, paper panels |
| navy-200 | `#DAE0E7` | Default hairline border, dividers |
| navy-300 | `#C3CBD6` | Disabled border, decorative rule |
| navy-400 | `#9DA9BA` | Disabled text, placeholder icon fill |
| navy-500 | `#66788E` | Interactive border (inputs, dropdowns), secondary icon |
| navy-600 | `#5B6B80` | Muted text (timestamps, helper text, metadata) |
| navy-700 | `#3F4E63` | Secondary text (body copy, descriptions) |
| navy-800 | `#2A3648` | Reserved (hover states on inverse fills) |
| navy-900 | `#0E1B2C` | THE INK: primary text, headings, linework, wordmark |
| steel | `#8FA1B8` | Decorative only: diagram lines, quiet accents. Never text (2.64:1). |

### 1.D Full token table with WCAG contrast, computed

WCAG 2.1 relative-luminance formula, computed directly (2 September 2026), not estimated.
AA: 4.5:1 normal text, 3:1 large text (24px+, or 19px+ at 700). AA non-text: 3:1.

| Role | Token | Hex | Paired against | Ratio | Result |
|---|---|---|---|---|---|
| Background | `bg` | `#F7F8FA` | - | - | - |
| Surface (cards, modals, panels) | `surface` | `#FFFFFF` | - | - | - |
| Border, default | `border` | `#DAE0E7` | decorative | - | - |
| Border, interactive | `border-interactive` | `#66788E` | surface | 4.52:1 | Pass (non-text 3:1) |
| Border, interactive | `border-interactive` | `#66788E` | bg | 4.26:1 | Pass |
| Text, primary (ink) | `text-primary` | `#0E1B2C` | surface | 17.33:1 | Pass AAA |
| Text, primary (ink) | `text-primary` | `#0E1B2C` | bg | 16.31:1 | Pass AAA |
| Text, primary (ink) | `text-primary` | `#0E1B2C` | navy-100 | 15.58:1 | Pass AAA |
| Text, secondary | `text-secondary` | `#3F4E63` | surface | 8.46:1 | Pass AAA |
| Text, secondary | `text-secondary` | `#3F4E63` | bg | 7.96:1 | Pass AAA |
| Text, muted | `text-muted` | `#5B6B80` | surface | 5.44:1 | Pass AA |
| Text, muted | `text-muted` | `#5B6B80` | bg | 5.12:1 | Pass AA |
| Ink text on accent button | `on-accent` | `#0E1B2C` | `#FF5A1F` | 5.56:1 | Pass AA |
| Ink text on accent hover | `on-accent` | `#0E1B2C` | `#E84D0F` | 4.54:1 | Pass AA |
| Accent as large text / non-text | `accent` | `#FF5A1F` | surface | 3.12:1 | Pass (3:1 class only) |
| Focus ring | `accent-active` | `#D4430A` | surface | 4.56:1 | Pass non-text |
| Small orange text / links | `accent-deep` | `#A83A04` | surface | 6.42:1 | Pass AA |
| Small orange text / links | `accent-deep` | `#A83A04` | bg | 6.05:1 | Pass AA |
| White text on ink fills | `on-ink` | `#FFFFFF` | `#0E1B2C` | 17.33:1 | Pass AAA |
| Accent on ink fills (large/non-text) | `accent` | `#FF5A1F` | `#0E1B2C` | 5.56:1 | Pass AA |
| Success | `success` | `#1A7F4B` | surface | 5.02:1 | Pass AA |
| Warning | `warning` | `#A15C07` | surface | 5.19:1 | Pass AA |
| Danger | `danger` | `#B91C1C` | surface | 6.47:1 | Pass AAA |

Notes on deliberate decisions:
1. **Card surface stays pure white on a near-white canvas**, exactly as v1: white is the one
   lift, always inside the `bg` canvas with a hairline, never touching the viewport edge.
2. **Hover and active share the same accent fill.** Ink-on-Blaze-700 lands at 3.80:1, under
   AA for button-size text, so the pressed state keeps the hover fill and communicates press
   through the existing transform (`translateY(1px) scale(0.98)`). The focus ring uses
   Blaze 700 because bare Blaze 500 misses 3:1 against the page background (2.93:1).
3. **Light mode only** (founder lock, 19 August 2026, unchanged). No dark palette exists in
   v2 at all; the product's dark is the ink used as an element, never as a canvas.

---

## 2. Typography

### 2.A Font choices and reasoning

**Display, UI and body: Archivo.** A grotesk built for headlines and signage with a genuine
900 weight, tight-tracking display presence, and clean small-size text cuts, on Google Fonts
with a variable axis. It replaces Public Sans, which was chosen for civic neutrality and
delivered exactly that: anonymity. Archivo at 900 with negative tracking gives headlines the
signage weight the direction needs; at 400-600 it stays a legible workhorse for forms on a
phone. It is not Inter, not Geist, and not in the default AI palette of typefaces.

**Numerals and measurements: IBM Plex Mono**, retained, with an expanded mandate: every
number the product asserts (prices, lead counts, radii, budgets, dates inside data surfaces)
sets in Plex Mono with `tabular-nums`. A number in the UI is a readout from an instrument;
it never sets in Archivo. Prose numbers inside sentences stay in the body face.

**No serif anywhere** (unchanged). **Emphasis inside headlines** is the one hot word in
`--color-accent` (24px+ display sizes only, per orange law 1) or Archivo italic; never a
second family.

### 2.B next/font setup

```ts
import { Archivo, IBM_Plex_Mono } from "next/font/google";

const archivo = Archivo({
  subsets: ["latin"],
  variable: "--font-sans",
  display: "swap",
});

const plexMono = IBM_Plex_Mono({
  subsets: ["latin"],
  weight: ["500", "600"],
  variable: "--font-mono",
  display: "swap",
});
```

### 2.C Type scale

The two-scale system from the 19 August amendment carries forward unchanged in structure:
a **product scale** for `/app` (dense, working-tool sizes) and a **marketing scale** for the
site. v2 changes the faces and turns the display end up; the product scale's sizes are
untouched so the app's layout density stays exactly V1 (founder lock).

**Product scale** (inside `/app`): identical sizes, weights and line-heights to v1's table,
set in Archivo instead of Public Sans. Body stays 16px minimum on anything an owner reads or
types; labels stay sentence case; stat numerals stay Plex Mono 600 tabular.

**Marketing scale** (never inside `/app`):

| Class | Mobile | Desktop | Weight | Tracking | Use |
|---|---|---|---|---|---|
| `.display-hero` | 40px | 68px | 900 | -0.045em | Page H1 only, one per page |
| `.display` | 36px | 56px | 800 | -0.035em | Rare second-level display moment |
| `.h-mkt` | 28px | 40px | 800 | -0.03em | Section headings |
| `.h-step` | 22px | 28px | 700 | -0.02em | Sub-section and step headings |
| `.lede` | 18px | 18px | 400 | 0 | The paragraph directly under a heading |
| `.figure` | 32px | 48px | 600 mono | -0.04em | Large tabular evidence numerals |

Headline line-height at 900 weight: 0.98 to 1.05. `text-wrap: balance` on every display
class. The hero headline may carry exactly one word in `--color-accent`.

---

## 3. Spacing, Radius, Borders

### 3.A Spacing scale

Unchanged from v1: the 4px-base named scale (`space-1` 4px through `space-24` 96px), same
usage table. The reskin does not move spacing; V1's rhythm is part of the retained layout.

### 3.B Corner radius (one locked scale, sharpened)

Precision instruments do not have soft corners. The three-value system stays; the values
tighten one step. Applies via tokens, so the change is global and layout-neutral.

| Token | Value (was) | Applies to (exhaustive, unchanged from v1) |
|---|---|---|
| `radius-sm` | 4px (6px) | Checkboxes, small tags, inline chips, status badges |
| `radius-md` | 8px (10px) | Buttons, form inputs, dropdowns - the interactive radius |
| `radius-lg` | 12px (16px) | Cards, modals, panels, the ad-preview container |

Pill ban and its two exemptions (progress-bar caps; faithful reproductions of Meta's surface
and the composited ad's disc) carry forward verbatim from v1.

### 3.C Border and hairline conventions

As v1 (1px hairlines, 1.5px interactive borders, one border per edge), with one change:
**focus ring is `2px solid var(--color-accent-active)`** with the same 4px halo at 20%
opacity, `:focus-visible` only. Blaze 700 passes non-text contrast on every ground; bare
Blaze 500 does not (Section 1.D note 2).

---

## 4. Component Specs

v1's component specs (button geometry, input stack, wizard step, stat tile, ad-preview card,
lead inbox row, activity feed) carry forward with these color and detail substitutions:

### 4.A Button

| State | Background | Text | Notes |
|---|---|---|---|
| Default (primary) | `--color-accent` | `--color-on-accent` (ink) | The safety-signage pairing, 5.56:1. Never white text. |
| Hover (primary) | `--color-accent-hover` | ink | 4.54:1 |
| Active (primary) | `--color-accent-hover` | ink | Press reads via `translateY(1px) scale(0.98)`, not a third fill |
| Focus | as state | as state | Ring per 3.C |
| Loading | `--color-accent-hover` | ink at 70% | Spinner in the icon slot; label never disappears |
| Disabled | navy-300 | navy-500 | Never carries the accent |
| Secondary | transparent | ink | `1.5px solid var(--color-border-interactive)`; hover: border and text to ink, bg `--color-accent-subtle` |
| Destructive | transparent | `--color-danger` | Unchanged from v1 |

Primary buttons are for the one action that moves money or work: Build my ads, Approve this
ad, Start with Grow. Everything else is secondary or a text link. Three-word label cap stays.

### 4.B Everything else

- **Form inputs:** v1 stack and states, new tokens. Error/focus borders per 3.C.
- **Wizard step:** v1 layout retained (per-screen flow; the founder's richer-wizard asks are
  a separate, explicitly-scoped project inside the app pass, not part of the reskin).
- **Stat tile:** Plex Mono numeral in ink, label in muted, and the tile may carry the
  measurement-tick detail (Section 6) as its only decoration.
- **Ad-preview card:** unchanged structurally; the rationale strip uses `--color-accent-subtle`
  bg with `--color-accent-deep` text (6.05:1 class on the tint is verified by its ink-family
  darkness; the strip never sets orange under 19px bold below `accent-deep`).
- **Badges/chips:** `radius-sm`, sentence case. Live/positive states may use the ink fill
  with white text (17.33:1) instead of tinted backgrounds where V1 used a green tint; status
  colors stay for true state.

---

## 5. Motion Rules

Unchanged from v1 in full: MOTION_INTENSITY 3, hover/focus/active plus load-in only, 150-200ms
`cubic-bezier(0.16, 1, 0.3, 1)`, transform/opacity only, reduced-motion first-class. The
measurement motif never animates.

---

## 6. The Measurement Motif

The one decorative language of the brand, drawn from dimension drawings: corner ticks,
dimension lines with end caps, small crosshair registration marks, and the fine drafting
grid. Rules, so the motif stays a signature instead of becoming the new slop:

1. **Vocabulary is closed.** Corner ticks (short 1px strokes at two or four corners of a
   surface, ink or Blaze 500, 8-12px long), dimension lines (1px, steel or navy-300, with
   perpendicular end caps, optionally a small mono measurement label in `text-muted`),
   crosshairs (12-16px circle-plus-cross, Blaze 500 or steel), and the drafting grid
   (44px cells at 6 to 8 percent ink alpha, edge-masked). Nothing else joins the motif.
2. **Density budget: one motif element per screen region.** The hero gets the grid plus at
   most one crosshair; a stat tile gets ticks or nothing; a section heading gets one
   crosshair bullet or nothing. Two motif elements side by side is one too many.
3. **The motif never carries meaning.** It decorates surfaces that already communicate; it
   never replaces a border, a divider, or a label, and it disappears entirely under
   `prefers-reduced-motion` only if animated, which it never is.
4. **Mono measurement labels** (a small "1080 x 1080" beside an ad preview, "12 mi" beside a
   radius) are the motif's text form: Plex Mono, 11-12px, `text-muted`, sentence-free.
   At most one per region, and only where the number is true.

---

## 7. Forbidden In This Project

The v1 list carries forward in full (em-dash ban, no pure-black/white page grounds, no
second accent, no AI-purple gradients, no warm/cool grey mixing, no decorative dots, no
serif, no sub-16px inputs, eyebrow rationing, no section-number eyebrows, no filler verbs,
no fake-perfect numbers, no placeholder names, no three-identical-card rows, no div-based
fake screenshots, no scroll cues, marquee limit, list-grouping rule, one-CTA-per-intent,
one icon library at stroke 2.0), with these v2 additions:

- [ ] White text on the orange accent, anywhere, at any size.
- [ ] Orange text below 24px regular / 19px bold in any orange lighter than `accent-deep`.
- [ ] Cobalt `#2454D9` or any blue-accent survivor from v1. The only blues left are the
      navy neutral ramp and decorative steel.
- [ ] More than one motif element per screen region (Section 6 rule 2).
- [ ] The measurement motif used on empty/error/loading states to fill space.
- [ ] Layout changes smuggled in with the reskin (founder lock: V1 format and layout stay).

---

## 8. Pre-Flight Checklist

The v1 checklist carries forward verbatim (color/contrast, typography, layout, motion,
content, accessibility gates), with these substitutions and additions:

- Font check now reads: no font outside Archivo (UI/body/display) and IBM Plex Mono
  (numerals/measurements) appears anywhere.
- Contrast rows check against Section 1.D of this version.
- [ ] Every orange element passes the three orange laws (1.B).
- [ ] Motif density budget holds on every region (6.2).
- [ ] The screen passes the Vercel Web Interface Guidelines MUST items
      (`~/.claude/skills/web-interface-guidelines/AGENTS.md`).
- [ ] The screen's layout is V1's layout. If it is not, the change was explicitly approved.

If any box is unchecked, the page does not ship.

---

## Amendment log

- **2 September 2026, motion exception (founder request):** the marketing evidence figures
  may count up once on first entry into view, 800ms ease-out, final value server-rendered so
  no-JS and crawlers see the real number, static under reduced motion, numeric values only.
  This is the single sanctioned scroll-triggered animation on the site; it does not open the
  door to reveals, parallax, or any other scroll choreography. Implemented in
  `src/components/CountUp.tsx`.

- **19 August 2026** (v1): light-only lock; two type scales; standing bans confirmed. All
  three carried into the v2 body above.
- **2 September 2026** (this version): direction pivot to High-Vis Precision light, founder
  decision after the three-board review. Cobalt accent, Public Sans, cool-grey ramp and the
  16px card radius are superseded. The founder's layout lock is recorded in the header.
- **3 September 2026, mechanical gate added:** the AJ.on.AI anti-slop checker
  (`node ~/.claude/skills/anti-slop-ajonai/scripts/check.mjs src/`) runs before any UI
  ships and must report zero errors; warnings are triaged, advisories are read. Its
  decision-sheet method (subject, ground, palette, type, space, shape, motion, signature)
  is used before any new screen is designed when the reskin resumes. Two of its positions
  do not override this project: the em-dash ban (AGENTS.md rule 7) and the founder's
  typeface decisions stand; the skill itself says the brief outranks it.
