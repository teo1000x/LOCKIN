# Ad Policy Compliance Ruleset

Status: v1 spec, no application code. Written 2026-08-19.

## 0. Why this document exists

Per the pivot in `docs/01-PRODUCT-SPEC.md`, we do not connect to Meta. The owner posts the ad
themselves, and we get no webhook, no rejection reason, no API visibility of any kind into what
happens after export. If an ad gets rejected, the owner does not distinguish "Meta rejected this"
from "the software gave me a bad ad" - they blame us and they churn. There is no repair step
after export. Prevention before the owner ever sees the ad is the only mechanism we have.

This ruleset is the pre-flight lint: a set of machine-checkable rules that run on every
AI-generated ad (copy, image, targeting spec, lead form, landing page reference) before it
reaches the owner's review screen. It is consumed by application code, not written as
application code here.

Two inviolable rules from `AGENTS.md` bind everything below:
- No em-dash characters anywhere, including inside rule messages shown to owners.
- Every AI-generated decision needs a plain-English reason. A blocked or warned ad must tell
  the owner why in contractor language, not policy-citation language.

## 1. Special Ad Category determination

### What it is and why getting it wrong is expensive

Meta requires self-identification as a Special Ad Category for ads about credit, employment, or
housing (referred to below as HEC). Declaring HEC strips targeting precision: no gender
targeting, no ZIP-level targeting, a 15-mile minimum radius in the US, age locked to 18-65+, no
detailed-interest targeting, no audience exclusions, no Lookalike Audiences.
[Discriminatory Practices, Transparency Center](https://transparency.meta.com/policies/ad-standards/unacceptable-content/discriminatory-practices/)

Two failure modes, both expensive to this product specifically:
1. **We tell the owner to run normal precision targeting, Meta's classifier disagrees, the ad
   gets rejected or the ad account gets flagged.** As of 2026, Meta runs a Multimodal Ad Review
   System (MARS) that scans image and text together and applies HEC restrictions automatically,
   whether or not the advertiser declared the category. Detection now looks at visual content
   too: floor plans, "for sale" signage, hiring/office imagery, credit card mockups, loan
   calculators. Source: 2026 policy update reporting, cross-checked against the official
   Discriminatory Practices and Financial Services pages below. Because we cannot verify MARS
   behavior against an official Meta engineering doc, treat this as a secondary signal that
   raises our own detection bar, not as an official policy citation on its own.
2. **We under-restrict and the owner's account gets a discrimination-policy strike**, which is
   worse than a single rejected ad because strikes accumulate against the whole ad account.

Because our export pack includes generated Ads Manager instructions (not an API call), the
practical effect of this determination is: which targeting-spec instructions we generate, and
whether we insert a mandatory "declare this as a Special Ad Category" instruction step.

### Official sources

- [Introduction to the Advertising Standards](https://transparency.meta.com/policies/ad-standards/) - policy index
- [Discriminatory Practices](https://transparency.meta.com/policies/ad-standards/unacceptable-content/discriminatory-practices/) - the Special Ad Category rule itself
- [Financial and Insurance Products and Services](https://transparency.meta.com/policies/ad-standards/restricted-goods-services/financial-services/) - what counts as a credit/financial ad, licensing, prohibited financial products (payday loans, bail bonds, short-term loans under 90 days)

### Decision tree (executable logic)

Runs on: ad copy (headline, primary text, description), the offer object, and the business
type from intake. Returns zero or more categories; any non-empty result changes the generated
targeting instructions and adds a mandatory disclosure step to the export pack.

```
function determineSpecialAdCategory(input: {
  adCopy: string;          // headline + primary text + description, concatenated
  offer: Offer;            // structured offer object from the wizard
  businessType: TradeType; // hvac | plumbing | roofing | electrical | ...
}): SpecialAdCategory[] {

  const categories: SpecialAdCategory[] = [];

  // --- EMPLOYMENT ---
  // Any recruitment/hiring framing, regardless of trade. This product only generates
  // customer-facing service ads, so a positive hit here almost always means the AI
  // drifted off-brief and should be treated as a generation bug, not just a policy flag.
  if (matchesKeywords(input.adCopy, EMPLOYMENT_SIGNALS)) {
    categories.push("EMPLOYMENT");
  }

  // --- CREDIT / FINANCIAL ---
  // Tier A: the ad's offer or CTA is itself a financing/credit product.
  if (matchesKeywords(input.adCopy, CREDIT_SIGNALS_TIER_A)
      || input.offer.type === "financing"
      || matchesKeywords(input.adCopy, NAMED_LENDER_BRANDS)) {
    categories.push("CREDIT");
  }
  // Tier B: financing is mentioned as one payment option among several, not the offer
  // itself. Does not force the category on its own, but raises the severity of the
  // CLAIM/URGENCY rules below and is always surfaced to the owner as a WARN.
  // (Tier B is handled in the rule table as SAC-CRED-02, not here.)

  // --- HOUSING ---
  // Two distinct triggers: (a) the ad targets landlords/property managers/tenants
  // rather than homeowners, or (b) the ad frames the service around a real estate
  // transaction (resale value, listing prep, mortgage-adjacent language).
  if (matchesKeywords(input.adCopy, HOUSING_SIGNALS)) {
    categories.push("HOUSING");
  }

  return categories;
}
```

Keyword lists (case-insensitive, word-boundary matched, checked against `adCopy` before it is
ever shown to the owner):

**EMPLOYMENT_SIGNALS**: "now hiring", "we're hiring", "join our team", "join the team",
"career opportunity", "employment opportunity", "seeking a technician", "seeking technicians",
"apply today" (only when co-occurring with "position", "job", "opening", "career", or "hiring"
within the same sentence), "full-time position", "part-time position", "send your resume",
"send us your resume", "job opening", "now recruiting".

**CREDIT_SIGNALS_TIER_A** (the offer itself is credit/financing): "0% apr", "0% financing",
"no credit check", "bad credit ok", "bad credit okay", "no credit needed", "get approved",
"get pre-approved", "apply for financing", "buy now pay later", "rent-to-own", "rent to own",
"credit approval", "financing available" when it appears in the headline or is the first
mention in the primary text (position matters, see detection strategy in section 6),
"as low as $X/month with approved credit" (regex, see FIN-CRED-01 in the rule table).

**NAMED_LENDER_BRANDS**: "wisetack", "greensky", "synchrony", "service finance company",
"hearth", "sunlight financial", "ygrene", "enerbank", "mosaic", "foundation finance",
"optimus", "ftl finance". This list needs quarterly refresh; see section 9.

**HOUSING_SIGNALS**: "landlord", "landlords", "property manager", "property management",
"tenant", "tenants", "rental property", "rental properties", "increase your home's resale
value", "boost your resale value", "before you list", "before you sell your home",
"mortgage", "real estate listing", "home appraisal value".

### Worked examples

| Ad copy | Category | Reasoning |
|---|---|---|
| "AC not cooling? Same-day tune-ups from $89." | none | Product-need question about equipment, no HEC signal |
| "0% financing on new HVAC systems, no credit check" | CREDIT | Tier A signal, offer.type likely financing |
| "Ask about financing options when you call" | none (WARN via SAC-CRED-02) | Financing mentioned but not the offer itself |
| "Now hiring licensed plumbers, join our team" | EMPLOYMENT | Direct hiring language |
| "Roof repair for landlords and property managers" | HOUSING | Targets property management relationship |
| "New roof before you sell? Free inspection" | HOUSING | Ties service to a real estate transaction |
| "Free roof inspection after storm damage" | none | Service framing, no HEC signal (see TRADE-ROOF rules instead) |

## 2. Prohibited and restricted copy patterns

### Personal attributes: where the line actually is

Meta's rule: ads must not assert or imply a personal attribute of the viewer, meaning race,
ethnicity, religion, beliefs, age, sexual orientation, gender identity, disability, physical or
mental health condition, vulnerable financial status, voting status, trade union membership,
criminal record, or name.
[Privacy Violations and Personal Attributes, Transparency Center](https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes)

The operative distinction, confirmed by Meta's own paired examples on that page, is not "does
the copy use you/your" but "does you/your attach to a protected attribute or a claim of
surveillance." "Meet Hispanic men online now" is fine; "Meet other black singles near you" is
not, because the second implies Meta told the advertiser the viewer's race. "Are you Christian?"
is prohibited; "Date Christian singles" is allowed, because the first asserts the viewer's own
belief back at them.

Applied to trades copy: **"Is your AC broken?" is not a personal-attribute violation.** It
asserts a fact about a piece of equipment, not about the viewer's body, finances, beliefs, or
any protected class. The pattern that is prohibited is a personal-attribute or vulnerable-status
assertion phrased as a question or statement about the viewer specifically: "Are you drowning in
debt?", "Struggling with anxiety about your bills?", "Do you have bad credit?", "As a senior
citizen, you deserve...". The difference is what the sentence is actually claiming to know:
equipment state (allowed) versus the viewer's body, mind, finances, or protected identity
(prohibited).

This distinction is exactly why rule ATTR-02 below needs an LLM classifier rather than a keyword
list: "is your X broken/leaking/failing" about a service item is allowed regardless of X, but
the same syntax pointed at a health or financial state of the person is not, and no regex can
tell "AC" from "anxiety" as a class.

### Unsupported superlatives and guarantees

Meta prohibits ads likely to deceive through exaggerated outcomes, including absolute guarantees
and claims a typical user will not get. Phrases like "guaranteed results" or "100% effective"
violate the standard because results are not universally verifiable, and Meta's guidance
explicitly favors softened language ("may help", "designed to") over absolutes.
[Fraud, Scams and Deceptive Practices](https://transparency.meta.com/policies/ad-standards/fraud-scams/fraud-scams-deceptive-practices/)

### Misleading urgency and false scarcity

Covered under Unacceptable Business Practices: fake countdowns (a timer that resets), false
"only 3 left" claims that never change, and artificial price inflation used to manufacture a
discount, are all prohibited. Urgency is allowed only when it is real and the landing page or
offer backs it up.
[Unacceptable Business Practices](https://transparency.meta.com/policies/ad-standards/fraud-scams/unacceptable-business-practices/)

### Before-and-after imagery

The restriction is specifically about body-image and health framing: before/after body
transformation comparisons, close-ups of body parts framed to reinforce insecurity, and
messaging that manufactures negative self-perception to sell a health or fitness outcome are
prohibited. This is a Health and Wellness category rule, not a blanket ban on before/after
photography.
[Health and Wellness](https://transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness/)

For trades, this means: a roofing or deck before/after photo pair is not itself a violation
(there is no body-image framing). It becomes a violation when it is paired with a health claim
("see how we saved this family from toxic mold" over a before/after) or framed to manufacture
fear about the homeowner's own health or safety rather than the property. See TRADE-MOLD-01 and
IMG-BA-01 in the rule table.

### Pricing claims requiring substantiation

Discount and savings claims ("save up to 50%", "half off") must be backed by a real,
verifiable discount that the landing page or offer object actually reflects. This falls under
the same deceptive-practices standard cited above; Meta does not publish a separate numeric
substantiation rule, but rejection reports consistently cite unsupported percentage-off and
dollar-savings claims as a trigger. Treat this as WARN-with-structural-check: if the ad claims a
discount, the offer object must contain a matching structured discount value, or the claim is
flagged for the owner to confirm.

## 3. Image policy

### Text-in-image: the 20 percent rule is dead, but the reason it existed is not

Meta removed the hard 20-percent-text rejection rule; an image with heavy text overlay will no
longer be auto-rejected for that reason alone.
[Search Engine Journal, Facebook Removes the 20% Text Limit](https://www.searchenginejournal.com/facebook-removes-the-20-text-limit-on-ad-images/381844/)

It still matters for two reasons that are not the same as the old rule: (1) Meta's delivery
system still down-ranks heavy-text images during auction, so a text-heavy AI-generated image
costs the owner reach even when it is not rejected, and (2) large blocks of AI-rendered text
inside an image are the single most common visual tell of AI generation and the most likely
place for garbled, misspelled, or nonsensical text to appear, since image models are weak at
rendering legible text. Rule IMG-TEXT-01 is therefore WARN, not BLOCK, and its message should
say "this may hurt how many people see your ad" rather than cite a rejection risk that no
longer exists.

### Prohibited imagery

Standard unacceptable-content categories apply to ad images the same as any other Meta content:
no graphic or violent imagery, no shocking gore (relevant for water-damage or mold photos that
lean too graphic), no adult content, no weapons depicted in a threatening context. See the full
category index at
[Introduction to the Advertising Standards](https://transparency.meta.com/policies/ad-standards/),
sections "Unacceptable Content" and "Objectionable Content".

### Quality and resolution minimums

Meta's recommended maximum resolution is 1440x1440 for square placements and 1440x1800 for 4:5.
Below 1080px width, Meta issues a low-resolution delivery warning; the ad can still run but
enters delivery flagged as lower-fidelity creative, which suppresses reach. Minimum usable
resolution for feed placements is 1080x1080. These are delivery-quality figures from current
ad-specs guidance rather than a single official transparency.meta.com page, since Meta
distributes creative specs through Ads Manager and partner documentation rather than the
Advertising Standards policy tree; treat IMG-RES-01 as a structural check against these numbers,
sourced to platform specs rather than policy text.

Excessively cropped images designed to force a click to see the rest of the image, and
disruptive visual tactics like flashing content, fall under Low Quality or Disruptive
Experiences.
[Low Quality or Disruptive Experiences](https://transparency.meta.com/policies/ad-standards/objectionable-content/low-quality-or-disruptive-experiences/)

### AI-generated image disclosure

As of the March 2026 policy update, Meta requires advertisers to disclose AI-generated or
AI-substantially-modified creative through a disclosure control in Ads Manager (the "AI Info"
label). Detection runs through three paths: embedded C2PA/IPTC provenance metadata, Meta's own
classifiers inferring origin from pixel content, and self-disclosure at upload. Because every
image this product generates is AI-generated by definition, this is not a conditional rule, it
is a mandatory line item in every export pack: an explicit instruction telling the owner to
toggle the AI disclosure control before publishing. Treat missing-disclosure-instruction as a
BLOCK on the export pack completeness check, not on the ad content itself.

Primary sourcing note: transparency.meta.com does not yet have this specific policy indexed
under a stable URL as of this research pass; the above is synthesized from multiple 2026 policy
trackers describing the March 2026 update (almcorp.com, auditsocials.com, techjacksolutions.com,
cinerads.com). This is flagged for the quarterly drift check in section 9 to find and swap in
the official transparency.meta.com citation once Meta publishes it under a permanent URL.

## 4. Landing page and destination policy

Applies only when the owner's export pack points to a website rather than (or in addition to)
an Instant Form.

- The destination must be a live, functional page, not a placeholder, broken link, or a page
  that interferes with navigation (pop-up interstitials, forced app-install redirects).
- What the ad promises must be findable on the landing page. If the ad says "$89 tune-up," an
  owner who sends traffic to a generic homepage with no mention of that offer is a mismatch
  Meta can flag, separate from whether the offer itself is real.
- The destination URL and the display URL shown in the ad must resolve to the same domain.
  Mismatches trigger a non-functional-URL flag.
- Avoid link shorteners and redirect chains (bit.ly, tinyurl, and similar); they can trip
  Meta's security filters independent of content.
- Pages should load fast; slow or broken loads are treated the same as non-functional
  destinations.

Source: [Introduction to the Advertising Standards](https://transparency.meta.com/policies/ad-standards/), general destination-quality requirements are distributed across the Unacceptable Business Practices and Low Quality or Disruptive Experiences pages rather than one dedicated URL; both cited above.

### Instant Form (lead ad) specific requirements

- **A privacy policy URL is mandatory on every Instant Form and is the single most commonly
  missed requirement.** The form cannot be completed in Ads Manager without it. The URL must
  resolve to a real, navigable web page describing how the submitted data will be used. A link
  to a PDF, an image, or a direct file download is not accepted.
- If the ad falls under a Special Ad Category (section 1), the Instant Form may require
  additional disclosures or restricted question sets.
- Lead form questions must not request certain protected-category information without separate
  written permission from Meta: disability status, insurance details, and (per the personal
  attributes policy applied to form fields) race, ethnicity, or political affiliation are the
  ones relevant to a trades business that might otherwise ask "do you have insurance covering
  this repair" as a qualifying question.
- Forms must never request full financial account numbers, SSNs, or other sensitive PII the
  Fraud, Scams and Deceptive Practices policy prohibits collecting through ads.

Source: privacy policy requirement confirmed across multiple current guides
(iubenda.com, adsuploader.com, cookieyes.com) cross-checked against Meta's own Ads Manager
Instant Form flow, which will not let an advertiser publish without the field populated. Meta's
canonical Lead Ads policy page returned a 404 during this research pass at the URL tested
(`transparency.meta.com/en-us/policies/ad-standards/product-format-specific-policies/lead-ads/`);
the correct current URL should be re-verified during implementation and is flagged in section 9.

## 5. Trade-specific risk areas

These are the categories most likely to bite this specific customer base, based on the general
deceptive-practices, health, and crisis-exploitation policies applied to actual contractor
marketing patterns.

**Emergency and fear-based framing.** "We answer emergency calls 24/7" is a factual service
statement and is fine. "Your home could burn down tonight if you don't call now" or "your family
is breathing poison right now" is catastrophizing not grounded in the actual service being sold,
and reads as manufactured urgency/fear under the deceptive-practices standard. The line is
whether the statement describes a real, current service capability (allowed) or invents an
imminent, unverifiable catastrophe to force action (not allowed). LLM classifier required, see
TRADE-EMERGENCY-01.

**Health claims: mold, air quality, water quality.** "Toxic mold is making your family sick,"
"eliminate 99% of allergens," "cure your indoor air quality problems" are health claims. Health
claims require the same evidentiary and regulatory backing Meta demands elsewhere in the Health
and Wellness policy, which a residential mold remediation or duct cleaning company almost never
has on hand (that would mean EPA/CDC-backed clinical claims). Safe framing describes the
service, not a medical outcome: "mold inspection and removal" is fine, "mold is destroying your
family's health" is not.
[Health and Wellness](https://transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness/)

**Insurance-related claims, especially roofing after storms.** Two distinct risks stack here.
First, deceptive-practices risk: "we'll get your insurance to cover this" or "$0 out of pocket
guaranteed with insurance" promises an outcome (the insurer's claim decision) that the
contractor does not control, which is the same unverifiable-guarantee pattern as CLAIM-01.
Second, crisis-exploitation risk: ads that name a specific recent storm or disaster and pair it
with urgency language can trigger the Commercial Exploitation of Crises and Controversial Events
policy, which prohibits using an identified crisis for commercial gain.
[Commercial Exploitation of Crises and Controversial Events](https://transparency.meta.com/policies/ad-standards/restricted-goods-services/commercial-exploitation-of-crises-and-controversial-events)
"Free roof inspection" or "storm damage inspection" without naming a specific storm event and
without insurance-outcome promises is the safe pattern.

**Financing language.** Covered in depth in section 1; the trade-specific risk is that HVAC and
roofing are the two trades where financing offers are most common (large-ticket replacements),
so this category will fire more often for those two trades than for a $150 drain-cleaning ad.

## 6. The machine-readable ruleset

### Core types

```typescript
type Severity = "BLOCK" | "WARN" | "INFO";

type RuleCategory =
  | "special_ad_category"
  | "personal_attributes"
  | "unsupported_claims"
  | "urgency_scarcity"
  | "before_after"
  | "pricing_substantiation"
  | "image_policy"
  | "destination_policy"
  | "lead_form"
  | "trade_specific";

type AppliesTo = "copy" | "image" | "destination" | "lead_form" | "targeting_spec" | "all";

type DetectionStrategy =
  | { kind: "keyword"; terms: string[]; matchType: "word_boundary" | "substring"; caseSensitive: false }
  | { kind: "regex"; pattern: string; flags?: string }
  | { kind: "structural"; check: string }
      // e.g. "offer.type === 'financing'", "image.width < 1080",
      // "leadForm.privacyPolicyUrl is empty", "destinationUrl.hostname !== displayUrl.hostname"
  | { kind: "llm_classifier"; classifierId: string }
  | { kind: "composite"; strategies: DetectionStrategy[]; operator: "AND" | "OR" };

interface AdPolicyRule {
  id: string;
  category: RuleCategory;
  severity: Severity;
  appliesTo: AppliesTo;
  metaPolicyReference: string;   // URL, or "internal" if no stable official URL exists yet
  lastVerifiedDate: string;      // ISO date, drives the staleness check in section 9
  detection: DetectionStrategy;
  ownerMessage: string;          // plain-English, no jargon, no em-dash, contractor voice
  suggestedFix: string;
  overridable: boolean;          // can the owner dismiss this and export anyway
  requiresLLM: boolean;
}
```

### Full rule list

Detection strategy choice follows one principle: use the cheapest strategy that will not miss
the real violation. Keyword and regex rules are near-zero cost and run synchronously on every
keystroke of generation; structural rules check data the app already has; LLM classifier rules
are reserved for genuinely semantic judgments a pattern cannot make (see section 7 for why each
one needs it).

| id | category | severity | appliesTo | detection | overridable |
|---|---|---|---|---|---|
| SAC-EMP-01 | special_ad_category | BLOCK | copy | keyword: EMPLOYMENT_SIGNALS | false |
| SAC-CRED-01 | special_ad_category | BLOCK | copy | composite (keyword: CREDIT_SIGNALS_TIER_A OR structural: offer.type === "financing" OR keyword: NAMED_LENDER_BRANDS) | false |
| SAC-CRED-02 | special_ad_category | WARN | copy | keyword: ["financing available", "financing options", "ask about financing", "payment plans available"] (Tier B, position outside headline) | true |
| SAC-HOUS-01 | special_ad_category | WARN | copy | keyword: HOUSING_SIGNALS | true |
| SAC-VISUAL-01 | special_ad_category | WARN | image | llm_classifier: `hec-visual-classifier` | true |
| ATTR-01 | personal_attributes | BLOCK | copy | regex: pairs a protected-attribute noun (race/ethnicity/religion/orientation/gender-identity/disability/criminal-record terms) within 6 words of "you"/"your" | false |
| ATTR-02 | personal_attributes | WARN | copy | llm_classifier: `personal-attribute-nuance` | true |
| ATTR-03 | personal_attributes | BLOCK | copy | keyword: explicit vulnerable-status phrases ("bad credit", "drowning in debt", "struggling financially") paired with "you"/"your" | false |
| ATTR-04 | personal_attributes | WARN | copy | llm_classifier: `personal-attribute-nuance` (indirect/coded framing) | true |
| CLAIM-01 | unsupported_claims | BLOCK | copy | regex: `\b(guarantee(d)?|100% (effective|guaranteed)|always works|never fails)\b` | true (override requires owner to attach substantiation, see section 8) |
| CLAIM-02 | unsupported_claims | WARN | copy | keyword: ["#1 rated", "best in", "top-rated", "highest rated", "top rated"] | true |
| CLAIM-03 | unsupported_claims | BLOCK | copy | llm_classifier: `health-claim-classifier` | true (soft-block, see section 8) |
| CLAIM-04 | pricing_substantiation | WARN | composite | structural: ad claims a percent-off or dollar-savings figure not matched by `offer.discountValue` | true |
| CLAIM-05 | unsupported_claims | BLOCK | copy | regex: guarantee word within the same sentence as a specific outcome number (e.g. `guarantee.{0,20}\d+\s*(leads|jobs|calls|%)`) | false |
| URGENCY-01 | urgency_scarcity | BLOCK | composite | structural: copy contains urgency/scarcity keyword AND `offer.expiresAt` is null | true |
| URGENCY-02 | urgency_scarcity | WARN | copy | keyword frequency: more than 2 of ["act now", "don't wait", "call now", "last chance", "hurry", "before it's too late"] in one ad | true |
| URGENCY-03 | trade_specific | BLOCK | copy | llm_classifier: `fear-catastrophizing-classifier` | true (soft-block) |
| IMG-BA-01 | before_after | BLOCK | image | llm_classifier: `before-after-health-classifier` (before/after visual paired with health-outcome text) | true (soft-block) |
| IMG-RES-01 | image_policy | BLOCK | image | structural: `image.width < 1080 OR image.height < 1080` | false |
| IMG-TEXT-01 | image_policy | WARN | image | structural: OCR text-area ratio > 20% of image area | true |
| IMG-PROHIBITED-01 | image_policy | BLOCK | image | llm_classifier: `prohibited-imagery-classifier` | false |
| IMG-AI-DISCLOSURE-01 | image_policy | BLOCK | all | structural: export pack instructions missing the AI-disclosure toggle step | false |
| DEST-01 | destination_policy | BLOCK | destination | structural: `destinationUrl` is empty or fails URL validation | false |
| DEST-02 | destination_policy | WARN | destination | structural: `destinationUrl.hostname !== displayUrl.hostname` | true |
| DEST-03 | destination_policy | INFO | destination | structural: ad's offer text not found on a fetched copy of the landing page (best-effort, v2 capability) | true |
| DEST-04 | destination_policy | BLOCK | destination | keyword: known shortener domains (bit.ly, tinyurl.com, t.co, ow.ly, is.gd) in `destinationUrl` | false |
| LEAD-01 | lead_form | BLOCK | lead_form | structural: `leadForm.privacyPolicyUrl` is empty | false |
| LEAD-02 | lead_form | WARN | lead_form | regex: `leadForm.privacyPolicyUrl` ends in `.pdf`, `.png`, `.jpg`, `.doc`, `.docx` | false (this one is never overridable either; it is functionally the same failure as LEAD-01) |
| LEAD-03 | lead_form | BLOCK | lead_form | structural: `specialAdCategory.length > 0 AND leadForm.requiredDisclosure` missing | false |
| LEAD-04 | lead_form | BLOCK | lead_form | regex: form field labels matching SSN, full card number, bank account number patterns | false |
| TRADE-ROOF-01 | trade_specific | BLOCK | copy | llm_classifier: `insurance-outcome-classifier` | true (soft-block) |
| TRADE-ROOF-02 | trade_specific | BLOCK | copy | composite (keyword: named-storm/disaster list OR llm_classifier: `crisis-exploitation-classifier`) AND urgency keyword co-occurrence | true (soft-block) |
| TRADE-MOLD-01 | trade_specific | BLOCK | copy | llm_classifier: `health-claim-classifier` (shared with CLAIM-03, mold/air/water specialization) | true (soft-block) |
| TRADE-EMERGENCY-01 | trade_specific | WARN | copy | llm_classifier: `fear-catastrophizing-classifier` (shared with URGENCY-03) | true |
| TRADE-FIN-01 | trade_specific | INFO | copy | structural: cross-reference to SAC-CRED-01/02, surfaces a reminder rather than a separate check | true |

Rules marked "false" under overridable are **hard blocks**: the ad cannot enter an export pack
in that state, full stop, regardless of who is asking. See section 8 for exactly which rules
those are and why.

## 7. What only an LLM can catch

Pattern matching catches syntax. It cannot catch what a sentence actually claims to know about
the reader, whether an image's before/after pairing is read as a health outcome versus a
property outcome, or whether an urgency claim is grounded in something real. The following
rules are LLM-only and the reasons are specific, not generic:

- **ATTR-02, ATTR-04** (personal attributes, nuance and indirect framing). "Is your AC broken"
  and "is your anxiety getting worse" have identical syntax. Only meaning distinguishes them:
  one names equipment, the other names a protected health state. No regex or keyword list can
  make that call without either blocking every "is your X" question in the language (unusable)
  or missing the coded versions ("for people managing blood sugar" implying diabetes without
  saying the word).
- **CLAIM-03 / TRADE-MOLD-01** (health claims). Whether "eliminate mold" is a service
  description or "eliminate mold and protect your family's health" is a medical claim depends on
  whether an outcome is being promised about a person's health, not on any single keyword.
  "Toxic," "allergens," and "air quality" are all legitimate words in a duct-cleaning ad; the
  violation is in the combination and the outcome framing.
- **URGENCY-03 / TRADE-EMERGENCY-01** (fear catastrophizing). "24/7 emergency service" is a
  factual capability. "Your family could die in a house fire tonight" is manufactured fear. Both
  use "emergency," "tonight," "now." The difference is whether the sentence states a real,
  current, verifiable service fact or invents an unverifiable catastrophe.
- **TRADE-ROOF-01** (insurance-outcome claims). Whether "we work with your insurance" (fine,
  describes a service) crosses into "we guarantee your insurance will cover this" (an
  unverifiable outcome claim about a third party's decision) is a claim-structure judgment.
- **TRADE-ROOF-02** (crisis exploitation). Requires recognizing that a named storm plus urgency
  language together read as exploiting a specific, identifiable crisis, versus a general
  "storm season" seasonal service reminder that names no specific event.
- **IMG-BA-01** (before/after paired with health framing). Requires reading the image and the
  copy together: the same before/after deck photo is fine alone and a problem next to "we saved
  this family's health."
- **SAC-VISUAL-01** (HEC visual signals). Mirrors Meta's own multimodal detection: floor plans,
  hiring/office photography, and credit-card mockups are visual patterns, not text patterns.
- **IMG-PROHIBITED-01** (prohibited imagery). Graphic, shocking, or otherwise unacceptable
  visual content is inherently a vision-classification task.

### Classifier prompt

One shared prompt handles the semantic rules above by asking for a structured verdict per rule
ID in a single pass, since they all reason over the same ad content. This keeps LLM calls to one
per ad rather than one per semantic rule.

```
SYSTEM PROMPT: ad-policy-semantic-classifier

You are a compliance classifier for Meta (Facebook/Instagram) advertising policy. You review
one AI-generated ad for a small home service business (HVAC, plumbing, roofing, or electrical)
before the business owner ever sees it. You are not the final decision. You flag risk so a
human can review it.

You will receive:
- The ad's headline, primary text, and description
- A description of the ad image (or the image itself, if vision input is available)
- The structured offer (type, price, expiration if any)
- The business trade type

Evaluate ONLY the following, and return a JSON array with one object per rule, even when there
is no violation:

1. personal-attribute-nuance (rules ATTR-02, ATTR-04): Does the copy assert or imply a
   protected personal attribute of the VIEWER, including race, ethnicity, religion, sexual
   orientation, gender identity, disability, physical or mental health condition, vulnerable
   financial status, criminal record, or immigration status? A question or statement about a
   PIECE OF EQUIPMENT or the PROPERTY's condition ("is your AC broken", "is your roof leaking")
   is NOT a violation. A question or statement about the VIEWER's body, mind, finances, or
   protected identity IS a violation, whether stated directly or implied indirectly (for
   example, referencing a health condition by its management routine rather than its name).

2. health-claim-classifier (rules CLAIM-03, TRADE-MOLD-01): Does the copy promise or strongly
   imply a health or medical outcome for a person (curing, treating, preventing, or protecting
   against illness, disease, or a medical condition), as opposed to describing a service
   (inspection, removal, cleaning, repair)? Flag claims about mold, air quality, or water
   quality that cross from "we remove/clean/inspect X" into "X is making you sick" or "we
   protect your family's health."

3. fear-catastrophizing-classifier (rules URGENCY-03, TRADE-EMERGENCY-01): Does the copy invent
   an unverifiable, imminent catastrophe to create fear, as opposed to stating a real, current
   service capability? "We answer emergency calls 24/7" is a capability statement and is NOT a
   violation. "Your home could burn down tonight" or "your family is breathing poison right
   now" invents an unverifiable catastrophe and IS a violation.

4. insurance-outcome-classifier (rule TRADE-ROOF-01): Does the copy promise or strongly imply
   that an insurance company WILL cover, approve, or pay for the service, as opposed to
   describing that the business assists with or works alongside insurance claims? A promised
   third-party financial decision is a violation.

5. crisis-exploitation-classifier (rule TRADE-ROOF-02): Does the copy name a specific,
   identifiable recent storm, hurricane, or disaster event AND pair it with urgency language
   to drive immediate action? A general seasonal reference ("storm season is here") without
   naming a specific event is NOT a violation.

6. before-after-health-classifier (rule IMG-BA-01): If an image shows a before/after
   comparison, is it paired with copy that frames the "after" state as a health or safety
   outcome for the people in the home, rather than a property/cosmetic outcome? Property
   before/afters (a repaired roof, a cleaned duct system shown as hardware) are NOT a
   violation on their own.

7. hec-visual-classifier (rule SAC-VISUAL-01): Does the image contain visual signals typically
   associated with housing (floor plans, "for sale" signage, real estate staging), employment
   (office/interview imagery, hiring signage), or credit (credit card mockups, loan
   calculators, cash imagery)?

8. prohibited-imagery-classifier (rule IMG-PROHIBITED-01): Does the image contain graphic,
   shocking, violent, adult, or otherwise policy-prohibited visual content?

Return strictly this JSON shape, no prose outside it:

{
  "results": [
    {
      "ruleId": "ATTR-02",
      "violation": boolean,
      "confidence": "low" | "medium" | "high",
      "reasoning": "one sentence, plain English, no jargon",
      "quotedSpan": "the exact phrase that triggered this, or null"
    },
    ... one object per rule listed above ...
  ]
}

Rules for your own output:
- Do not invent a violation to be safe. A false BLOCK on a compliant ad is a real cost to this
  business; only flag what you can point to in quotedSpan or describe concretely for images.
- "confidence: low" results are treated as WARN regardless of the rule's default severity.
  Reserve "high" confidence for cases where the quoted span or image content is unambiguous.
- Never use an em-dash character in reasoning text.
```

Application code maps each `violation: true` result to its rule's configured severity, downgraded
one level if `confidence` is `low`, per the rule above. This keeps the classifier itself
conservative-leaning without hardcoding that behavior into the prompt's binary decision.

## 8. False positive management

Over-blocking is a real product failure, not a safe default. A contractor who cannot get an ad
past the lint after three tries will not read policy text, they will assume the software is
broken and churn exactly as if the ad had been rejected. The design below treats false positives
as a first-class problem, not an edge case.

### What the owner can override

Every rule in section 6 marked `overridable: true` can be dismissed by the owner from the
review screen. The override flow requires two things, not a single click:
1. A **reason code** from a short fixed list (not free text alone, so overrides are analyzable
   in aggregate): `"not applicable to my business"`, `"this is accurate and I can back it up"`,
   `"I disagree with this flag"`, `"I already fixed this elsewhere"`.
2. Optional free text, capped at one sentence, for anything the reason code does not capture.

Overriding a WARN exports the ad as-is. Overriding a BLOCK that is marked `overridable: true`
(the LLM-classifier-sourced ones: CLAIM-01, CLAIM-03, URGENCY-03, IMG-BA-01, TRADE-ROOF-01,
TRADE-ROOF-02, TRADE-MOLD-01) is a **soft block**: it requires the reason code, logs the
override with higher weight (see below), and the resulting ad carries an internal flag visible
only to us, not the owner, for pattern review. It does not require us to review before export;
that would reintroduce the API-visibility problem this document exists to route around. The
friction of the reason-code step is deliberate: it is small enough not to block a legitimate
override, large enough to discourage reflexive dismissal.

### What can never be overridden

These are the rules where getting it wrong risks the owner's Meta account standing, not just a
single ad's approval, or where the underlying requirement is a hard platform mechanic rather
than a judgment call: SAC-EMP-01, ATTR-01, ATTR-03, IMG-RES-01, IMG-PROHIBITED-01,
IMG-AI-DISCLOSURE-01, DEST-01, DEST-04, LEAD-01, LEAD-02, LEAD-03, LEAD-04, CLAIM-05. All of
these are keyword, regex, or structural detections, not LLM judgment calls, which is exactly
why they can be non-overridable: their false-positive rate is bounded and known, unlike a
semantic classifier's.

### Logging for tuning

Every trigger (not just every override) is logged, so we can compute a true false-positive
proxy: override rate per rule. The log record:

```typescript
interface RuleTriggerEvent {
  id: string;
  orgId: string;
  adId: string;
  adContentHash: string;   // ties to the same content hash used by the approval gate
  ruleId: string;
  severityAtTrigger: Severity;
  llmConfidence?: "low" | "medium" | "high"; // only for LLM-sourced rules
  outcome: "fixed" | "overridden" | "pending";
  overrideReasonCode?: string;
  overrideFreeText?: string;
  timestamp: string;
}
```

Tuning rule: if a rule's override rate exceeds 30 percent of its triggers over a trailing window
of 100 triggers, it is flagged for manual review, meaning someone reads a sample of the
overridden cases and decides whether to narrow the keyword list, raise the LLM confidence
threshold, or downgrade the rule's default severity. A rule with a near-zero override rate and a
high trigger count is doing its job; a rule with a high override rate is either miscalibrated or
catching something owners genuinely disagree is a problem, both of which need a human look
rather than an automatic loosening (loosening automatically would let the rule drift toward
uselessness without anyone noticing).

## 9. Maintenance

Meta changes ad policy regularly and we have zero automated visibility into enforcement, so
drift detection has to be deliberate rather than reactive.

- **Every rule carries `metaPolicyReference` and `lastVerifiedDate`.** A rule whose
  `lastVerifiedDate` is more than 90 days old is flagged in an internal dashboard for manual
  re-check against its source URL. This catches silent drift on rules we already have sourced.
- **Quarterly manual pass against the ~10 official transparency.meta.com URLs cited in this
  document.** Fetch each, diff against the prior quarter's saved text, and read the diff.
  Automating the fetch-and-diff (not the reading) is a reasonable v1.5 build: a scheduled job
  that snapshots each cited URL's rendered text and alerts on any change, so the manual review
  is triggered by an actual diff rather than a calendar guess.
- **Unresolved sourcing gaps from this research pass, tracked explicitly rather than left
  implicit:** the AI-disclosure policy (section 3) and the canonical Lead Ads policy URL
  (section 4) could not be pinned to a stable official transparency.meta.com page during this
  research. Both need a follow-up pass to find the permanent citation once Meta's own
  documentation stabilizes; until then, treat IMG-AI-DISCLOSURE-01 and the LEAD-* rules as
  sourced to secondary reporting, flagged with lower confidence in the internal rule metadata.
- **The self-report loop doubles as a drift signal.** `docs/01-PRODUCT-SPEC.md`'s Option B
  (owner self-reporting) should include an optional "did Meta reject or restrict this ad"
  checkbox alongside the leads/booked prompt. It will be sparse data, but even a handful of
  self-reported rejections that our lint did not catch is a direct signal a rule is missing,
  and is the only ground truth this product will ever get without API access.
- **NAMED_LENDER_BRANDS and any other named-entity keyword list needs the fastest refresh
  cadence** (monthly, not quarterly) because financing partners for home services turn over
  faster than Meta's policy text does.
- **Secondary sources used throughout this document** (auditsocials.com, adsuploader.com,
  1clickreport.com, and similar 2026 policy trackers) are useful for real-world rejection
  patterns and dating recent changes, but are not authoritative. Every rule's primary citation
  should be the official transparency.meta.com URL where one exists; secondary sources are
  cited only to fill gaps or to date a change, and are named as such inline above rather than
  presented as official policy.

## Sources

Official Meta policy (Transparency Center):
- [Introduction to the Advertising Standards](https://transparency.meta.com/policies/ad-standards/)
- [Discriminatory Practices](https://transparency.meta.com/policies/ad-standards/unacceptable-content/discriminatory-practices/)
- [Financial and Insurance Products and Services](https://transparency.meta.com/policies/ad-standards/restricted-goods-services/financial-services/)
- [Privacy Violations and Personal Attributes](https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes)
- [Fraud, Scams and Deceptive Practices](https://transparency.meta.com/policies/ad-standards/fraud-scams/fraud-scams-deceptive-practices/)
- [Unacceptable Business Practices](https://transparency.meta.com/policies/ad-standards/fraud-scams/unacceptable-business-practices/)
- [Health and Wellness](https://transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness/)
- [Commercial Exploitation of Crises and Controversial Events](https://transparency.meta.com/policies/ad-standards/restricted-goods-services/commercial-exploitation-of-crises-and-controversial-events)
- [Low Quality or Disruptive Experiences](https://transparency.meta.com/policies/ad-standards/objectionable-content/low-quality-or-disruptive-experiences/)

Secondary sources (used for 2026 policy-change dating and real-world rejection patterns, not as
policy authority):
- [Search Engine Journal, Facebook Removes the 20% Text Limit](https://www.searchenginejournal.com/facebook-removes-the-20-text-limit-on-ad-images/381844/)
- [Meta Ad Policy Updates 2026: What Changed and How to Comply, auditsocials.com](https://www.auditsocials.com/blog/meta-ad-policy-updates-2026-guide)
- [Meta AI Labels on Facebook and Instagram Ads, almcorp.com](https://almcorp.com/news/meta-ai-labels-facebook-instagram-ads-disclosure-2026/)
- [Meta Now Requires Advertisers to Disclose AI-Generated Content, techjacksolutions.com](https://techjacksolutions.com/ai-brief/meta-now-requires-advertisers-to-disclose-ai-generated-conte/)
- [Meta AI Content Label Policy 2026, auditsocials.com](https://www.auditsocials.com/blog/meta-ai-generated-content-label-policy-2026)
- [Facebook Lead Ads Privacy Policy: What It Must Say, adsuploader.com](https://adsuploader.com/blog/facebook-lead-ads-privacy-policy)
- [Meta Beauty and Cosmetic Ads 2026: Before/After and Body Image Rules, auditsocials.com](https://www.auditsocials.com/blog/meta-beauty-cosmetic-ads-before-after-photos-body-image-policy-2026)
