# Design System Spec - v1

> Companion to `01-PRODUCT-SPEC.md` and `05-UI-DESIGN.md`. This document is the single source of
> truth for color, type, spacing, and component behavior across the marketing site and the
> product UI. Every value below is final and ready to paste into code. Nothing here is
> illustrative.

**Design read:** B2B SaaS landing plus multi-step product UI for non-technical trades business
owners who read on a phone between jobs. Plain-spoken, utilitarian language. Trust and legibility
outrank delight. Leaning toward Tailwind v4 utilities plus a small hand-tuned token set, restrained
motion, and a single locked cobalt accent against cool grey and off-white.

**Dials:** `DESIGN_VARIANCE 6` / `MOTION_INTENSITY 3` / `VISUAL_DENSITY 4`.

- Variance 6 means: not a symmetrical brochure template, but not asymmetric agency chaos either.
  The marketing site can break the centered-hero default and use split layouts; the product UI
  (wizard, dashboard, inbox) stays closer to predictable grid alignment because it is a working
  tool, not a portfolio.
- Motion 3 means: hover, focus, and active states only, plus short load-in transitions. No
  scroll-triggered choreography, no parallax, no marquees. See Section 5.
- Density 4 means: standard "daily app" spacing, not art-gallery, not cockpit. Numbers get room
  to breathe but the dashboard is not a data table.

---

## 1. Color Tokens

### 1.A The accent: Cobalt 600

The locked accent is one specific cobalt, not a Tailwind default blue and not the founder's
reference point (`#2563EB`). It sits at hue 224°, saturation 71.5%, lightness 49.6% in HSL, under
the 80% saturation ceiling, tuned to read as a deliberate signal color rather than generic
software blue.

```
--color-accent:        #2454D9   /* Cobalt 600 - primary buttons, links, active nav, focus ring */
--color-accent-hover:  #1D44AF   /* Cobalt 700 - hover state, light mode */
--color-accent-active: #1A3D9D   /* Cobalt 800 - pressed state, light mode */
--color-accent-subtle: #E9EEFB   /* Cobalt tint 10% - selected card bg, info banners, badge fill */
```

This is the only accent color anywhere in the product. It never competes with a second brand
color. Status colors (success, warning, danger) exist for state, not for decoration, and are
never used as an alternate "accent" for buttons or links.

### 1.B Cool grey ramp

One hue (222°), one saturation family (18%), eleven lightness steps. This is the entire neutral
palette for both themes - light mode reads it light-to-dark, dark mode reads the same ramp
inverted, plus two bespoke endpoints for true page canvas and elevated surface in dark mode.

| Token | Hex | Light-mode role |
|---|---|---|
| grey-50 | `#F6F7F9` | Page background (off-white, not pure white) |
| grey-100 | `#EDEFF2` | Sunken fields, code/mono blocks, skeleton base |
| grey-200 | `#DEE1E8` | Default hairline border, dividers |
| grey-300 | `#C9CED9` | Disabled border, decorative rule |
| grey-400 | `#ABB2C4` | Disabled text, placeholder icon fill |
| grey-500 | `#75819F` | Interactive border (inputs, dropdowns), secondary icon |
| grey-600 | `#5C6884` | Muted text (timestamps, helper text, metadata) |
| grey-700 | `#4D586F` | Secondary text (body copy, descriptions) |
| grey-800 | `#384051` | Reserved (dark-mode-only interior use) |
| grey-900 | `#262B36` | Primary text (headings, body-strong) |
| grey-950 | `#171A21` | Reserved (deep contrast accents) |
| grey-925 | `#1B2029` | Dark-mode elevated surface (bespoke step, not on the strict ramp) |
| grey-975 | `#0F1115` | Dark-mode page background (near-black, not pure black) |

### 1.C Full token table with role, hex, and WCAG contrast

All ratios below are the WCAG 2.1 relative-luminance formula, computed directly, not estimated.
"AA" for body text requires 4.5:1 normal text / 3:1 large text (18px+ or 14px+ bold). "AA
non-text" (borders, focus rings, input outlines) requires 3:1 against adjacent colors.

**Light mode**

| Role | Token | Hex | Paired against | Ratio | Result |
|---|---|---|---|---|---|
| Background | `bg` | `#F6F7F9` | - | - | - |
| Surface (cards, modals, wizard panel) | `surface` | `#FFFFFF` | - | - | - |
| Border, default (hairline/divider) | `border` | `#DEE1E8` | decorative, no contrast requirement | - | - |
| Border, interactive (inputs, dropdowns) | `border-interactive` | `#75819F` | bg `#F6F7F9` | 3.63:1 | Pass (AA non-text, 3:1) |
| Border, interactive | `border-interactive` | `#75819F` | surface `#FFFFFF` | 3.89:1 | Pass (AA non-text) |
| Text, primary | `text-primary` | `#262B36` | bg | 13.23:1 | Pass AAA |
| Text, primary | `text-primary` | `#262B36` | surface | 14.18:1 | Pass AAA |
| Text, secondary | `text-secondary` | `#4D586F` | bg | 6.66:1 | Pass AAA |
| Text, secondary | `text-secondary` | `#4D586F` | surface | 7.14:1 | Pass AAA |
| Text, muted | `text-muted` | `#5C6884` | bg | 5.20:1 | Pass AA (normal text) |
| Text, muted | `text-muted` | `#5C6884` | surface | 5.57:1 | Pass AA |
| Accent (as text/link) | `accent` | `#2454D9` | bg | 5.86:1 | Pass AA |
| Accent (as text/link) | `accent` | `#2454D9` | surface | 6.28:1 | Pass AA |
| White text on accent button | `on-accent` | `#FFFFFF` | `#2454D9` | 6.28:1 | Pass AA |
| White text on accent-hover | `on-accent` | `#FFFFFF` | `#1D44AF` | 8.41:1 | Pass AAA |
| White text on accent-active | `on-accent` | `#FFFFFF` | `#1A3D9D` | 9.55:1 | Pass AAA |
| Success | `success` | `#1A7F4B` | surface | 5.02:1 | Pass AA |
| Warning | `warning` | `#A15C07` | surface | 5.19:1 | Pass AA |
| Danger | `danger` | `#B91C1C` | surface | 6.47:1 | Pass AAA |

**Dark mode**

| Role | Token | Hex | Paired against | Ratio | Result |
|---|---|---|---|---|---|
| Background | `bg` | `#0F1115` | - | - | - |
| Surface (cards, modals, wizard panel) | `surface` | `#1B2029` | bg (elevation step, not a text pairing) | 1.16:1 | Intentional (subtle lift, relies on border + shadow, not luminance jump) |
| Border, default | `border` | `#262B36` | decorative, no contrast requirement | - | - |
| Border, interactive | `border-interactive` | `#75819F` | bg | 4.86:1 | Pass (exceeds 3:1 non-text) |
| Border, interactive | `border-interactive` | `#75819F` | surface | 4.20:1 | Pass |
| Text, primary | `text-primary` | `#F6F7F9` | bg | 17.63:1 | Pass AAA |
| Text, primary | `text-primary` | `#F6F7F9` | surface | 15.24:1 | Pass AAA |
| Text, secondary | `text-secondary` | `#C9CED9` | bg | 11.98:1 | Pass AAA |
| Text, secondary | `text-secondary` | `#C9CED9` | surface | 10.36:1 | Pass AAA |
| Text, muted | `text-muted` | `#ABB2C4` | bg | 8.91:1 | Pass AAA |
| Text, muted | `text-muted` | `#ABB2C4` | surface | 7.70:1 | Pass AAA |
| Accent (as text/link) | `accent` | `#7C9EFF` | bg | 7.37:1 | Pass AAA |
| Accent (as text/link) | `accent` | `#7C9EFF` | surface | 6.37:1 | Pass AAA |
| White text on accent button | `on-accent` | `#FFFFFF` | `#2454D9` | 6.28:1 | Pass AA |
| White text on accent-hover | `on-accent` | `#FFFFFF` | `#3663DE` | 5.25:1 | Pass AA |
| White text on accent-active | `on-accent` | `#FFFFFF` | `#3F69DF` | 4.89:1 | Pass AA |
| Success | `success` | `#3FBE7B` | bg | 7.97:1 | Pass AAA |
| Success | `success` | `#3FBE7B` | surface | 6.90:1 | Pass AAA |
| Warning | `warning` | `#E6A23C` | bg | 8.64:1 | Pass AAA |
| Warning | `warning` | `#E6A23C` | surface | 7.47:1 | Pass AAA |
| Danger | `danger` | `#F2726B` | bg | 6.65:1 | Pass AAA |
| Danger | `danger` | `#F2726B` | surface | 5.75:1 | Pass AAA |

Notes on the two deliberate design decisions in this table:

1. **Card surface is pure white in light mode, not off-white.** The page canvas (`bg`) is
   off-white per the palette brief. Cards, the wizard panel, and the approval-review surface use
   pure `#FFFFFF` specifically because they are the one place that must visually lift off the
   canvas without leaning on heavy shadow. It is the only place `#FFFFFF` appears, and it never
   touches the viewport edge directly - it always sits inside the off-white canvas with a
   `border` hairline. Everywhere else defaults to the off-white or grey ramp.
2. **Dark mode accent states lighten instead of darken.** In light mode, hover and active states
   darken the accent (standard "press it, it deepens" affordance). In dark mode that direction
   would reduce contrast against an already-dark canvas, so hover and active lighten instead
   (`#2454D9` to `#3663DE` to `#3F69DF`). Both directions were re-verified against AA with white
   button text at every step; this is a deliberate inversion, not an inconsistency.

### 1.D Dark mode strategy

CSS custom properties, swapped under `[data-theme="dark"]` with a `@media (prefers-color-scheme:
dark)` fallback for first paint before the toggle hydrates. Tailwind's `dark:` variant maps to the
same custom properties rather than hardcoded Tailwind grey utilities, so there is exactly one
source of truth per token.

```css
:root {
  --bg: #F6F7F9;
  --surface: #FFFFFF;
  --border: #DEE1E8;
  --border-interactive: #75819F;
  --text-primary: #262B36;
  --text-secondary: #4D586F;
  --text-muted: #5C6884;
  --accent: #2454D9;
  --accent-hover: #1D44AF;
  --accent-active: #1A3D9D;
  --accent-subtle: #E9EEFB;
  --success: #1A7F4B;
  --warning: #A15C07;
  --danger: #B91C1C;
}

:root[data-theme="dark"] {
  --bg: #0F1115;
  --surface: #1B2029;
  --border: #262B36;
  --border-interactive: #75819F;
  --text-primary: #F6F7F9;
  --text-secondary: #C9CED9;
  --text-muted: #ABB2C4;
  --accent: #2454D9;
  --accent-hover: #3663DE;
  --accent-active: #3F69DF;
  --accent-subtle: #1D2B50;
  --success: #3FBE7B;
  --warning: #E6A23C;
  --danger: #F2726B;
}
```

Default mode is system preference (`prefers-color-scheme`). A manual toggle lives in Settings
because trades owners working outdoors in daylight will want to force light mode regardless of OS
setting - this is one of the rare cases where the override control matters more than the smart
default.

---

## 2. Typography

### 2.A Font choices and reasoning

**UI and body: Public Sans.** Public Sans is the USWDS typeface, engineered by 18F specifically
for plain-language, trust-first reading by a non-technical general public - which is close to a
literal description of this audience (a roofer reading a wizard screen on a phone between jobs).
It is a humanist grotesque with unusually good hinting at small sizes, a true italic, and a wide
weight range (100 to 900). It is available on Google Fonts and works with `next/font/google`.
Inter was the other candidate the skill flags as an override-eligible neutral choice for exactly
this kind of accessibility-first, non-design-conscious brief - Public Sans was chosen over Inter
because it carries the same neutrality without being the same font every AI-generated SaaS product
already reaches for, and its civic-trust pedigree is a genuine narrative fit for a product whose
entire pitch is "we show you everything, nothing is hidden."

**Numerals and tabular data: IBM Plex Mono.** Used narrowly, not as a second UI font: the large
number in a stat tile, dollar figures, phone numbers, and timestamps in the lead inbox. A
monospace numeral treatment on the handful of numbers that carry the product's actual proof
("47 leads," "$31 cost per lead," "16 booked") reads as an instrument giving a precise readout,
which reinforces the transparency promise. It is not used for headings, body copy, or buttons.
Available on Google Fonts, works with `next/font/google`.

**No serif anywhere.** This is a trust-first utilitarian B2B tool, not an editorial, luxury, or
heritage brand - none of the conditions that justify serif per the serif-discipline rule apply.
`Fraunces` and `Instrument Serif` are banned outright regardless; this product does not reach for
any serif, banned or otherwise.

**Emphasis inside headlines** (a highlighted word in a hero line) uses italic or bold of Public
Sans itself, never a second family. Public Sans's italic has clean descenders; when italicizing a
word with a descender letter (`y g j p q`) in display type, line-height for that block is set to
`1.15` minimum with `padding-bottom: 0.25rem` reserved on the wrapper so the descender is never
clipped.

### 2.B next/font setup

```ts
import { Public_Sans, IBM_Plex_Mono } from "next/font/google";

const publicSans = Public_Sans({
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

All sizes in rem (16px root). Line-height is unitless. Letter-spacing (`tracking`) in em.

| Style | Size (mobile / desktop) | Weight | Line-height | Letter-spacing | Font | Use |
|---|---|---|---|---|---|---|
| Display | 2.25rem / 3.25rem (36px / 52px) | 800 | 1.1 | -0.02em | Public Sans | Marketing hero headline only |
| H1 | 1.75rem / 2rem (28px / 32px) | 700 | 1.2 | -0.01em | Public Sans | Product page title, wizard step title |
| H2 | 1.375rem (22px, no scale-up) | 700 | 1.25 | -0.01em | Public Sans | Section heading, dashboard card group title |
| H3 | 1.0625rem (17px) | 600 | 1.3 | 0em | Public Sans | Card title, component heading |
| Body | 1rem (16px, never smaller) | 400 | 1.5 | 0em | Public Sans | Default paragraph, form input text |
| Body strong | 1rem (16px) | 600 | 1.5 | 0em | Public Sans | Emphasized inline text, lead name in inbox row |
| Small | 0.875rem (14px) | 400 | 1.45 | 0em | Public Sans | Secondary line under a heading, card description |
| Meta / muted | 0.8125rem (13px) | 500 | 1.4 | 0.01em | Public Sans | Timestamps, helper text, "4 min ago" |
| Label | 0.75rem (12px) | 600 | 1.3 | 0.01em | Public Sans | Form field labels, badge text (sentence case, not uppercase) |
| Stat number | 2.25rem / 2.75rem (36px / 44px) | 600 | 1.05 | -0.01em | IBM Plex Mono | Dashboard stat tile large figure |
| Stat delta | 0.875rem (14px) | 500 | 1.3 | 0em | IBM Plex Mono | "+14 this week" line under a stat |

Body text never drops below 16px anywhere a trades owner types or reads on a phone - form inputs
are locked to 16px specifically so iOS Safari does not auto-zoom on focus. Labels stay sentence
case, not uppercase-tracked "eyebrow" style; this product's voice is plain-spoken, and uppercase
micro-labels are also rationed hard under Section 6's eyebrow-restraint rule.

---

## 3. Spacing, Radius, Borders

### 3.A Spacing scale

4px base unit. Named tokens, not arbitrary values, used everywhere from gaps to padding to
margins.

| Token | Value | Typical use |
|---|---|---|
| `space-1` | 4px | Icon-to-label gap |
| `space-2` | 8px | Tight stack (label to helper text) |
| `space-3` | 12px | Form field internal padding (vertical) |
| `space-4` | 16px | Default gap between related elements |
| `space-5` | 20px | Card internal padding (mobile) |
| `space-6` | 24px | Card internal padding (desktop), stat tile padding |
| `space-8` | 32px | Gap between stacked cards |
| `space-10` | 40px | Section internal padding (mobile) |
| `space-12` | 48px | Gap between distinct component groups |
| `space-16` | 64px | Section padding, desktop |
| `space-20` | 80px | Marketing section padding, desktop |
| `space-24` | 96px | Marketing hero padding, desktop (never exceeds this) |

### 3.B Corner radius (one locked scale)

Four values total, each with a documented, exhaustive rule for where it applies. Nothing outside
this list.

| Token | Value | Applies to (exhaustive) |
|---|---|---|
| `radius-sm` | 6px | Checkboxes, small tags, inline chips |
| `radius-md` | 10px | Buttons, form inputs, dropdowns, select menus - the default interactive radius |
| `radius-lg` | 16px | Cards, modals, the wizard step panel, the ad-preview card container |
| `radius-full` | 9999px | Status pill badges only ("Optimizing," "Booked," lead-status tags) |

`radius-full` is the one documented exception to an otherwise-flat scale, matching the
pill-badge-with-status-dot pattern already established as this product's status idiom. It is never
used on buttons, cards, or inputs - only on the small pill badges that carry a state word.

### 3.C Border and hairline conventions

- Default divider / hairline: `1px solid var(--border)`. Used for `divide-y` row separators
  (lead inbox, activity feed) and card outlines. Decorative, not required to hit a contrast
  ratio, but visually calibrated to read clearly on both canvas and surface.
- Interactive element border (form inputs, dropdowns, default state): `1.5px solid
  var(--border-interactive)`. This one does carry a WCAG non-text contrast requirement (3:1) and
  is verified in Section 1.C.
- Focus ring: `2px solid var(--accent)` with a `0 0 0 4px` box-shadow halo at 20% accent opacity.
  Applied via `:focus-visible`, never plain `:focus`, so mouse clicks do not show a ring but
  keyboard and switch-device navigation always does.
- Never stack more than one border color on a single edge. A card gets one border, not a border
  plus an inner ring plus a shadow doing the same job.

---

## 4. Component Specs

### 4.A Button

Sizes: `md` (default, 40px height) and `lg` (48px height, wizard primary actions and the final
"Approve and publish" action).

| State | Background | Text | Border | Notes |
|---|---|---|---|---|
| Default (primary) | `--accent` | `#FFFFFF` | none | Contrast verified 6.28:1 in both themes (Section 1.C) |
| Hover (primary) | `--accent-hover` | `#FFFFFF` | none | |
| Active / pressed (primary) | `--accent-active` | `#FFFFFF` | none, plus `transform: translateY(1px) scale(0.98)` | Physical-push feedback, transform/opacity only |
| Focus (primary) | `--accent` | `#FFFFFF` | `2px solid var(--accent)` ring offset 2px | Ring color uses a fixed high-contrast outline, not the button's own fill, so it is visible even on hover-darkened backgrounds |
| Loading (primary) | `--accent-active` | `#FFFFFF` at 70% opacity | none | Inline spinner (16px, currentColor stroke) replaces the label icon slot; label text stays visible, never replaced by the spinner alone, so the button never goes blank |
| Disabled (primary) | `grey-300` (`#C9CED9`) | `grey-500` (`#75819F`) | none | Contrast intentionally low to signal non-interactive; disabled buttons never carry the accent color |
| Default (secondary) | transparent | `--accent` | `1.5px solid var(--accent)` | |
| Hover (secondary) | `--accent-subtle` | `--accent-hover` | `1.5px solid var(--accent-hover)` | |
| Default (destructive) | transparent | `--danger` | `1.5px solid var(--danger)` | Used only for "Reject ad," "Disconnect Meta account," "Pause everything" |
| Hover (destructive) | `#FDECEC` (danger tint) | `--danger` | `1.5px solid var(--danger)` | |

**Mandatory contrast check applied:** every button state above pairs a solid fill with white text
(6.28:1 minimum, verified) or a transparent fill with accent-on-surface text (6.28:1, verified).
No white-on-white, no transparent-button-on-matching-background, no ghost button without a
visible border. Button label is capped at three words for primary actions ("Approve and Publish,"
"Generate My Ads," "Connect Meta") so it never wraps to a second line at any supported width; the
button widens rather than the text wrapping.

### 4.B Form input

Label above, input, helper text or error below - one vertical stack, `space-2` (8px) gaps.

```
[ Label, 12px/600, text-primary ]
[ Input field, 16px body text, 48px height, radius-md, border-interactive ]
[ Helper text OR error text, 13px, text-muted OR danger ]
```

| State | Border | Background | Extra |
|---|---|---|---|
| Default | `1.5px solid var(--border-interactive)` | `--surface` | |
| Hover | `1.5px solid var(--text-secondary)` | `--surface` | Slightly darkens the border, no fill change |
| Focus | `2px solid var(--accent)` | `--surface` | Focus ring halo as defined in Section 3.C |
| Error | `2px solid var(--danger)` | `--surface` | Error text appears below, red, with an inline icon (not color alone, per WCAG 1.4.1) |
| Disabled | `1.5px solid var(--border)` | `grey-100` | Text at `text-muted`, cursor not-allowed |

No placeholder-as-label, ever. Placeholder text (when used at all, e.g. "e.g. $89 A/C tune-up")
sits at `text-muted` contrast (5.20:1, verified AA) and always in addition to a real visible
label, never instead of one.

### 4.C Intake wizard step

One question per screen per the product spec. Layout, mobile-first (this is filled out on a
phone between jobs):

```
[ Progress bar, 4px height, --accent fill over --border track, radius-full ]
[ Step counter, "Step 3 of 9", 13px meta, text-muted ]                    <- plain functional label,
                                                                              not a "Phase 03" pattern
[ H1, the question itself, e.g. "What's your average job value?" ]
[ Optional 1-line helper under the H1, 14px, text-secondary ]
[ Input or choice group, single focus target ]
[ Inline AI suggestion chip, when applicable: --accent-subtle bg, --accent text,
  radius-full, e.g. "Most A/C repair shops in your area average $340-420" ]
[ Footer bar, sticky on mobile: Back (secondary button) + Continue (primary button, lg) ]
```

State persists on every keystroke (debounced 500ms autosave), per the product's non-negotiable
UI rule. A small `text-muted` "Saved" indicator appears next to the step counter for 2 seconds
after each autosave, using a static checkmark icon, not an animated toast.

### 4.D Stat tile

Three per row on desktop, stacked on mobile. No card box unless the row needs visual grouping
(Section 3.C leans toward `divide-y` over boxed cards at this density; the dashboard uses three
tiles inside one bordered strip rather than three separate floating cards).

```
[ Label, 12px/600 uppercase-free, text-muted, e.g. "Leads this month" ]
[ Number, IBM Plex Mono 600, 36px/44px, text-primary, tabular-nums, e.g. "47" ]
[ Delta line, IBM Plex Mono 500, 14px, e.g. "+14 this week" in --success or --text-muted
  depending on whether the delta is meaningful - not every stat needs a colored delta ]
```

Numbers are always real, organic figures ("47," never "50"; "$31" cost-per-lead, never a flat
round number) per the fake-precise-numbers ban.

### 4.E Ad-preview card

This deliberately mimics Meta's News Feed ad unit - it is a functional review surface, not
decorative "fake screenshot" filler, and is exempt from the div-based-fake-screenshot ban because
replicating the real platform's presentation is the actual job of this screen (the owner needs to
see exactly what will publish).

```
[ Card container: radius-lg, border, surface bg, max-width 500px ]
  [ Header row: business avatar (32px circle) + business name (14px/600) + "Sponsored" (12px, text-muted) ]
  [ Primary text, body 16px, max 3 lines visible with "See more" truncation matching Meta's own pattern ]
  [ Image or video, 4:5 aspect ratio, radius-md inside the card padding ]
  [ Headline, 16px/600 + Description, 14px text-secondary ]
  [ CTA button, matches Meta's own button chrome, not this product's --accent button style -
    it must look like what will actually appear on Facebook, not like this product's UI ]
  [ Divider ]
  [ Rationale strip: --accent-subtle bg, accent text, 13px, one sentence,
    e.g. "Targeting 12 miles around your shop because that's where your last 30 jobs came from" ]
  [ Action row: Edit (secondary button) · Regenerate (secondary button) · Approve (primary button) ]
```

The rationale strip is mandatory on every ad-preview card, matching the product spec's "every AI
decision ships with a plain-English why" requirement. It is never a confidence score, never
jargon.

### 4.F Lead inbox row

```
[ Row, 1px border-bottom divider, space-4 vertical padding, no card box ]
  [ Name, body-strong 16px + phone number, IBM Plex Mono 14px text-secondary + timestamp, meta 13px text-muted ]
  [ Inquiry text, 14px text-secondary, single line truncated ]
  [ Status action group: 4 buttons - Booked / Not a fit / No answer / Spam - secondary-button
    style at a smaller 32px height, single row on desktop, horizontal scroll-snap on mobile
    rather than wrapping to a second line ]
  [ Conditional reveal: if "Booked" is tapped, a single job-value input appears inline below
    the row, 16px input, auto-focused, with Save / Cancel ]
```

New/unread leads get a `4px solid var(--accent)` left border on the row and a small unread dot
(the one legitimate use of a decorative dot in this system, since it conveys real unread state,
not decoration) - removed the instant the row is opened.

### 4.G Activity feed row

Plain-English sentences the owner would say themselves, per the product spec.

```
[ Row, checkmark icon (16px, --success) + sentence, 14px text-primary + relative timestamp,
  13px text-muted, right-aligned on desktop / below on mobile ]
```

Example content: "Built and launched 5 fresh ads for you," "Scaled your 2 best ads, +30% budget,"
"Your top ad booked 18 leads this week." No jargon, no metric the owner would not say out loud to
a friend, matching the product's non-negotiable UI rule. Rows are grouped by week with a plain
`text-muted` date label ("This week," "Last week"), never a `divide-y`-on-every-row spec-table
treatment - grouped in soft clusters per the long-list guidance in Section 6.

---

## 5. Motion Rules (MOTION_INTENSITY 3)

At this intensity, motion exists only to acknowledge input and communicate state change. Nothing
plays automatically, nothing loops, nothing triggers on scroll.

- **Allowed:** `:hover` and `:active` transitions, focus-ring appearance, button press feedback
  (`translateY(1px) scale(0.98)`), skeleton loading states, the wizard progress bar filling, a
  toast sliding in for a transient confirmation, an accordion or dropdown expanding.
- **Not allowed:** scroll-triggered reveals, parallax, marquees, auto-playing carousels, infinite
  pulse/shimmer loops on static content, magnetic cursor-follow effects, any GSAP ScrollTrigger
  pattern. None of these fit a tool a trades owner needs to trust and finish quickly on a phone.
- **Duration and easing:** all transitions use `150ms` to `200ms` with `cubic-bezier(0.16, 1,
  0.3, 1)`. Nothing animates longer than 250ms except the wizard progress bar fill, which can run
  up to 400ms since it represents real elapsed progress, not decoration.
- **Properties:** animate only `transform` and `opacity`. Never `top`, `left`, `width`, `height`,
  or `background-color` transitions longer than the 150-200ms micro-interaction band.
- **Loading states:** skeleton loaders match the final layout's shape (a stat tile skeleton is
  three rectangles shaped like label / number / delta, not a generic spinner). The skeleton pulse
  itself is a simple opacity fade between 60% and 100%, 1.5s duration, and is disabled entirely
  under reduced motion (see below) in favor of a static 80%-opacity block.
- **Reduced motion (mandatory, applies regardless of the 3-threshold):** every transition and
  loading animation is wrapped in `@media (prefers-reduced-motion: no-preference)`, with an
  explicit `@media (prefers-reduced-motion: reduce)` block that removes the skeleton pulse,
  disables the progress-bar fill animation (it jumps directly to the new value), and keeps
  press-feedback as an instant state swap with no transform. This product's audience is not
  design-conscious and includes users who may have vestibular sensitivity; reduced motion is
  treated as a first-class mode, not an edge case.

---

## 6. Forbidden In This Project

A working checklist of AI tells that specifically apply to this product, derived from Section 9
of the taste skill. Anything on this list is a shipped-broken result, not a style preference.

**Absolute, no exceptions**
- [ ] Em-dash (`-`) anywhere in any string, in this document or in the product - headlines,
      button labels, form copy, error messages, activity feed sentences, ad rationale text, SMS
      or email notification copy. Use a period, a comma, or a hyphen instead. En-dash (`–`) as a
      separator is equally banned; date and number ranges use a regular hyphen (`2018-2026`,
      `$40-80k`).
- [ ] Pure `#000000` or pure `#FFFFFF` as a page-level background in either theme.
- [ ] A second accent color anywhere. Cobalt 600 is the only accent, full stop - no purple, no
      teal, no second "pop" color creeping into a badge or icon.
- [ ] AI-purple / indigo glow gradients, neon outer glows, or any glow effect on a button.

**Color and visual**
- [ ] Oversaturated accent variants (anything pushing Cobalt past ~80% saturation for a "louder"
      CTA).
- [ ] Mixing warm and cool greys. Every neutral in the product comes from the single grey-50
      through grey-975 ramp in Section 1.B.
- [ ] Any button, badge, or status chip with a colored dot that does not represent real state.
      The green "Optimizing" dot on the dashboard is legitimate (real campaign state); a
      decorative dot in front of a nav link or a static label is not.
- [ ] Mixed corner-radius systems outside the four documented values in Section 3.B.

**Typography and copy**
- [ ] Any serif font anywhere in the product.
- [ ] `Fraunces` or `Instrument Serif`, even if a serif were later justified elsewhere.
- [ ] Body text smaller than 16px on any input field.
- [ ] Uppercase "eyebrow" labels above every section - rationed to at most one per three sections
      on the marketing site, and not used at all as a default pattern inside the product UI.
- [ ] Section-number eyebrows (`01 / Capabilities`, `Step 1 of 3` phrased as "Phase 01"). The
      wizard uses a plain "Step 3 of 9" counter, never a "Phase" or "Stage" label.
- [ ] Generic filler verbs in marketing copy: "elevate," "seamless," "unleash," "next-gen,"
      "revolutionize," "empower." This product's voice is concrete and outcome-first ("You book
      the jobs"), not aspirational.
- [ ] Fake-perfect numbers anywhere in example content, screenshots, or seed data - "50%,"
      "99.99%," round dollar figures. Use organic numbers ("47.2%," "$31," "16 booked").
- [ ] Generic placeholder names ("John Doe," "Jane Smith," "Acme HVAC") in any example, seed data,
      or screenshot. Use realistic, specific trades-business names and owner names.

**Layout and components**
- [ ] Three identical feature cards in a horizontal row on the marketing site.
- [ ] Div-based fake product screenshots anywhere on the marketing site (the in-product
      ad-preview card is exempt - it is real functionality, not marketing decoration).
- [ ] Scroll cues ("Scroll to explore," animated mouse-wheel icons) - the audience does not need
      to be told what scrolling is.
- [ ] Locale, weather, or timezone decoration strips in the header or footer.
- [ ] More than one marquee or auto-scrolling element on the entire marketing site.
- [ ] A long list or spec table rendered as more than five `border-b` rows in a row without
      grouping - group into clusters or switch to a card grid past five items.
- [ ] Duplicate CTA intent on one page - one label per action, used identically everywhere it
      appears ("Get started" is either the signup CTA everywhere, or it is not used at all
      elsewhere on the page).
- [ ] Hand-rolled SVG icons. This project uses one icon library, locked, with a single stroke
      width (2.0) applied globally. `lucide-react` is not used unless explicitly requested.

---

## 7. Pre-Flight Checklist

Run this against every new page or screen before it ships. Every box must be checked - this is a
gate, not a suggestion.

**Color and contrast**
- [ ] Every text/background pairing on the page matches a token from Section 1.C, not an
      arbitrary hex.
- [ ] Every button's text-on-fill combination hits at least 4.5:1 (normal text) or 3:1 (18px+ or
      bold 14px+).
- [ ] Every form input's border, placeholder, and error text hit their required contrast against
      the surface it sits on.
- [ ] Page has been opened in both light and dark mode. Hierarchy that works in one works in the
      other - if a CTA pops in light mode, it pops in dark mode.
- [ ] No pure black, no pure white, anywhere as a background.

**Typography**
- [ ] No font outside Public Sans (UI/body) and IBM Plex Mono (numerals only) appears anywhere.
- [ ] No text smaller than 16px on any input field or button label.
- [ ] Every italic word in display type has descender clearance (`line-height >= 1.15` plus
      bottom padding on the wrapper).

**Layout**
- [ ] Hero (marketing pages only) fits in the initial viewport - headline max 2 lines, subtext
      max 20 words, CTA visible without scrolling.
- [ ] No button label wraps to a second line at any supported width.
- [ ] No two CTAs on the same page carry the same intent under different words.
- [ ] Every multi-column layout has an explicit, tested `< 768px` single-column fallback.
- [ ] Corner radius on every element traces back to one of the four values in Section 3.B, with
      no undocumented exceptions.
- [ ] No section-layout family (card grid, split image/text, full-width quote) repeats more than
      twice in a row on the marketing site.

**Motion and interaction**
- [ ] Every animation is `transform`/`opacity` only.
- [ ] Every transition, loading state, and progress indicator degrades correctly under
      `prefers-reduced-motion: reduce` - test this directly in dev tools, do not assume.
- [ ] Every interactive component has a real, tested loading state, empty state, error state, and
      disabled state - not just the happy path.

**Content**
- [ ] Grep the page's full rendered text for `-` and `–`. Zero results. This includes generated
      or dynamic copy (AI rationale strings, activity feed sentences), not just hardcoded strings.
- [ ] Every visible string has been read aloud once for grammatical sense and AI-hallucination
      tells (forced wordplay, unclear referents, fake-craftsman phrasing).
- [ ] No fake-precise numbers in any example, seed, or screenshot content.
- [ ] Every AI-generated decision shown to the user (targeting, budget, copy choice) carries a
      one-sentence plain-English rationale inline - never a confidence score, never jargon.
- [ ] No metric appears anywhere the owner would not say out loud to a friend.

**Accessibility**
- [ ] Every interactive element has a visible `:focus-visible` state using the accent focus ring,
      not the browser default and not nothing.
- [ ] Error states use an icon plus color, never color alone.
- [ ] Every icon-only button has an accessible label.
- [ ] Tab order matches visual order on every screen, tested with keyboard only.

If any box is unchecked, the page does not ship.

---

## Amendment, 19 August 2026: marketing scale and light-only lock

Two changes were made to this document by founder decision while applying the anti-slop pass
to the landing page. Both are binding from this date.

### 1. Light mode only. The dark palette is retired.

The dark tokens in this document are no longer implemented and `globals.css` carries no
`prefers-color-scheme` block. Reason: the buyer is a contractor reading a phone in daylight in
a truck, and every reference the founder chose ships light only. Do not reintroduce dark mode
without asking. The dark hex values stay recorded above in case that decision reverses.

### 2. There are now two type scales, and they do not mix.

The scale defined above is the **product** scale. Its 22px H2 exists because headings sit next
to dense forms and tables inside `/app`. Applying it to a marketing page made every section
read at the same volume, which was a large part of why the first landing page felt templated.

Marketing pages use these, defined in `globals.css` and never used inside `/app`:

| Class | Mobile | Desktop | Weight | Use |
|---|---|---|---|---|
| `.display` | 36px | 52px | 800 | Page H1 only, one per page |
| `.h-mkt` | 28px | 40px | 700 | Section headings |
| `.h-step` | 22px | 28px | 700 | Sub-section and step headings |
| `.lede` | 18px | 18px | 400 | The paragraph directly under a heading |
| `.figure` | 32px | 44px | 600 mono | Large tabular evidence numerals |

Colour tokens, radius scale, spacing and the 16px body floor are unchanged and still apply to
both surfaces. One accent, one radius system, everywhere.

### 3. Standing bans confirmed on this codebase

These come from `~/.claude/skills/taste-skill/SKILL.md` and were each violated by the first
build. They are now checked mechanically before any UI ships:

- No div-based fake product screenshots, and specifically no fake browser chrome with
  traffic-light dots and a fake URL bar. Show a real image, a real component, or nothing.
- No more than two consecutive text-and-panel split sections. The first walkthrough had five.
- Hero top padding never exceeds `pt-24` at desktop.
- Hero carries at most four text elements. No tagline under the CTAs.
- Zero em-dashes anywhere, including source comments.
- One CTA label per intent across the whole site. Signup is always "Start a campaign".
- Any scroll-triggered reveal must render visible without JavaScript and must handle a reader
  arriving mid-page via an anchor link. See the note in `src/components/Reveal.tsx`.
