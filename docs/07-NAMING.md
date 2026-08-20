# 07 - Naming

Product: self-serve marketing software for HVAC, plumbing, roofing, and electrical contractors. Owner answers six questions, AI produces a marketing plan, a competitive read of nearby contractors' ads, and ready-to-post Facebook ads. Owner approves every ad, downloads an export pack, posts it themselves in Meta Ads Manager. We never touch their ad account. Price band $499-$1,999/mo. Buyer: a non-technical contractor reading on a phone between jobs.

This document locks one name, backed by a verified-available .com, plus four ranked backups.

---

## Locked recommendation

**Callbackline** - callbackline.com (verified available, see proof below)

---

## Process

Generated and DNS/whois-checked 120 candidates across five batches before filtering to finalists. Every candidate below was actually run through `dig +short <name>.com A`, not just brainstormed. Full candidate list is in the section below, grouped by the batch it was checked in.

### Banned patterns avoided throughout
Anything containing "AI"; "Ad" + generic noun (AdGenius, AdFlow, etc.); coinages ending in -ly, -ify, -io, -hub, -flow, -sync, -wise, -scale; Nexus, Apex, Vertex, Zenith, Catalyst, Momentum, Elevate, Amplify, Boost, Launch, Rocket, Spark, Surge, Pulse, Forge; empty tech-sounding coinages.

### Direction taken
Real trade vocabulary used seriously (framing, roofing, HVAC, and plumbing terms that carry a second meaning relevant to marketing/leads), plus firm-style compounds (-line, -craft, -works, -board) that read like a real business, not a startup. Rejected the surname-firm route (Halloran & Co, Fenwick, Colfax, Draper, Marsh) early - too much of that namespace is occupied by actual law firms, VC firms, and industrial companies, which creates exactly the collision problem Constraint 5 warns about.

---

## Full candidate list (120 checked)

### Batch 1 - trade compounds and common business words (30)
fieldmark, fieldcraft, wrenchline, crewline, routeline, ledgerline, toolbelt, hardline, coreline, groundwork, jobline, jobcraft, trueline, plumbline, squareline, levelline, tradeline, tradecraft, dispatchline, gaugeline, torqueline, milepost, waypoint, signhouse, truebase, corework, fieldline, benchmark, fieldwork, checkpoint

Result: every single one already registered (A record live, or whois shows registration). Zero survivors. This confirmed that generic dictionary-adjacent business words in this space are essentially all domain-squatted.

### Batch 2 - framing/structural/electrical trade terms (40)
plumbcraft, trueframe, framewell, studline, trussline, joistline, rafterline, girderline, beamline, beamwork, truemeter, meterline, panelline, circuitcraft, breakerline, wattline, ampcraft, couplingworks, fittingline, valveline, flangeline, gasketworks, torquework, wrenchworks, toolworks, craftworks, jobworks, tradeworks, fieldworks, crewworks, dispatchworks, routeworks, ledgerworks, gaugeworks, trueworth, fieldworth, craftworth, bearingline, sightcraft, viewcraft

Result: 8 candidates showed no A record (rafterline, girderline, beamwork, breakerline, couplingworks, flangeline, torquework, sightcraft). Whois follow-up showed 5 of those were still registered (parked, no site). 3 confirmed available: **rafterline, girderline, flangeline**.

### Batch 3 - supply house / jobsite / punch-list vocabulary (20)
supplyline, punchlist, walkboard, callsheet, jobticket, workticket, siteboard, curbline, curbcraft, doorline, bidcraft, ordercraft, stockline, partsline, counterline, yardcraft, shopcraft, ladderline, ladderwork, laddercraft

Result: only 2 with no A record (walkboard, counterline); both confirmed registered on whois follow-up. Zero survivors.

### Batch 4 - permit / inspection / spec / roofing-idiom vocabulary (20)
permitline, permitcraft, permitworks, permitboard, inspectline, inspectcraft, specline, speccraft, specworks, shingleline, shinglecraft, hangshingle, eaveline, eavecraft, trueshingle, callbackline, callbackworks, truespec, onspec, codeworks

Result: 6 with no A record (permitline, inspectcraft, shingleline, eavecraft, callbackline, callbackworks). Whois follow-up: permitline and inspectcraft were registered; **shingleline, eavecraft, callbackline, callbackworks confirmed available**.

### Batch 5 - "phone ringing" / callback family, since callback tested strong (10)
ringline, ringworks, ringcraft, truering, calltrue, truecall, callroute, truecallback, callbackboard, callbackcraft

Result: 3 with no A record (ringline, truecallback, callbackboard). Whois: ringline registered; **truecallback and callbackboard confirmed available**.

---

## Verified-available domains (dig + whois proof)

All five finalists below returned **no A record** via `dig +short <name>.com A` (empty output) and **"No match for domain"** via `whois <name>.com` - the definitive signal a .com is unregistered. Raw proof:

### callbackline.com
```
$ dig +short callbackline.com A
(empty)

$ whois callbackline.com | grep -iE "No match|Domain Name:|Creation Date|Registrar:"
No match for domain "CALLBACKLINE.COM".
```

### callbackworks.com
```
$ dig +short callbackworks.com A
(empty)

$ whois callbackworks.com | grep -iE "No match|Domain Name:|Creation Date|Registrar:"
No match for domain "CALLBACKWORKS.COM".
```

### shingleline.com
```
$ dig +short shingleline.com A
(empty)

$ whois shingleline.com | grep -iE "No match|Domain Name:|Creation Date|Registrar:"
No match for domain "SHINGLELINE.COM".
```

### eavecraft.com
```
$ dig +short eavecraft.com A
(empty)

$ whois eavecraft.com | grep -iE "No match|Domain Name:|Creation Date|Registrar:"
No match for domain "EAVECRAFT.COM".
```

### callbackboard.com
```
$ dig +short callbackboard.com A
(empty)

$ whois callbackboard.com | grep -iE "No match|Domain Name:|Creation Date|Registrar:"
No match for domain "CALLBACKBOARD.COM".
```

Note on method: `whois <name>.com | head -25` alone is not reliable for these five - the first ~40 lines of a .com whois response are IANA/Verisign registry boilerplate that appears identically whether the name is taken or free (this is exactly the trap Constraint 1 warns about - "no A record but a live whois registration is taken"). To be certain, the full whois response was pulled and grepped for the actual registrar-level verdict line. For all five finalists that line reads "No match for domain" - meaning the registry has no record of it, not merely that it lacks a live website. This is the strongest available signal short of attempting a live registration.

For contrast, here is what a **taken** domain with no A record looks like (fieldcraft.com, batch 1), to show the failure mode this method avoids:
```
$ dig +short fieldcraft.com A
(empty)

$ whois fieldcraft.com
...
   Domain Name: FIELDCRAFT.COM
   Registrar: GoDaddy.com, LLC
   Creation Date: 2001-12-27T19:28:08Z
   Registrant Organization: Domains By Proxy, LLC
...
```
Registered and parked (privacy-shielded), not available - despite the empty DNS answer. Six other candidates in this run (hardline, coreline, groundwork, tradeline, tradecraft, beamwork, breakerline, couplingworks, torquework, sightcraft, permitline, inspectcraft, ringline) followed this same pattern and were correctly excluded.

---

## Collision findings (web search per finalist)

**Callbackline** - No exact match. Search surfaced general "callback software" category players (call-tracking/lead-attribution tools: CallbackTracker, Callback24, Callback.Market, Callback Technologies Inc, an ad agency called "Callback Studios"). None of these share the name Callbackline or operate in home-services marketing specifically. No meaningful collision.

**Callback Works** - Same "callback software" category noise as above (call tracking, not home-services marketing), no exact or confusable match for "Callback Works." No meaningful collision.

**Shingleline** - No matches at all in home-services software, marketing software, or advertising. Clean.

**Eavecraft** - No matches. Search surfaced unrelated "-craft" named companies (Macecraft Software, AvCraft Technical Services) but nothing close to Eavecraft itself. Clean.

**Callbackboard** - Same callback-software category noise, no exact or confusable match. Clean.

One finding that changed the ranking: a candidate from batch 2 that I had initially favored, **Rafterline**, surfaced a real soft collision on search - "Digital Rafter" (a marketing agency working exclusively with construction businesses and home inspectors) and "RafterOne" (an IPG-owned digital commerce/marketing firm serving industrial brands like Trane and Thermo King). Neither is named "Rafterline" exactly, but "Rafter" as a root is already active in construction-adjacent marketing services. Given Constraint 5's instruction to flag any collision found, I downgraded Rafterline out of the top 5 rather than risk a contractor confusing it with an existing marketing vendor in the same trade vertical.

---

## Ranked top 5

### #1 - Callbackline (callbackline.com) - LOCKED

"Yeah, I use Callbackline for my ads." Passes clean - sounds like a real, slightly old-fashioned service-business name, the kind of thing that could be stitched on a windbreaker.

"Callback" is genuine trade vocabulary shared by all four trades in scope - HVAC, plumbing, roofing, and electrical all use "callback" to mean a return visit on a job. It is not a cute pun on any single trade, which is exactly what Constraint 4 is testing for. At the same time, "callback" is the literal outcome the product is built to produce: an ad that makes the phone ring. That double meaning is not manufactured - it is the actual mechanism of the business, described in real language a contractor already uses, not marketing jargon laid on top. The "-line" suffix reinforces "phone line" (this is a phone-lead business) while also reading as a normal firm-name pattern (Redline, Sideline, Baseline), so it doesn't feel invented. It is short, phonetic, easy to spell after hearing it once, and has zero collision with any named competitor in home-services software, marketing software, or advertising.

### #2 - Shingleline (shingleline.com)

"Shingleline" ties to "hang your shingle" - the old idiom for opening and announcing a business, historically used by tradespeople and professionals alike, not just roofers. It reads as a serious, slightly traditional firm name and passes the phone test cleanly: a plumber or electrician saying it doesn't sound like they're using a roofer's product, because the idiom's meaning (announcing yourself to the market) is bigger than the literal building material. It is the strongest available runner-up because the double meaning is genuine rather than decorative, it's clean on search, and "-line" again nods at the phone/lead mechanic without repeating the word "callback."

### #3 - Callback Works (callbackworks.com)

Same core concept as the #1 pick, different register - "Works" reads like an actual trade shop name (Bodywork, Ironworks, Waterworks), which fits a buyer who trusts businesses with plain, functional names. Slightly weaker than Callbackline only because "Works" is a more common suffix in the call-tracking/lead-gen category generally, so it sits a notch closer to that generic-sounding cluster on search, even though no exact collision was found.

### #4 - Callback Board (callbackboard.com)

Keeps the same trade-and-marketing double meaning as the top pick, with "Board" suggesting the actual product experience - a dashboard where the owner reviews and approves a set of ready-to-post ads before export. It's a legitimate #4: sound, available, no collision, but "board" is a slightly less vivid word than "line" or "works" and reads a bit more like a project-management tool than an ads product.

### #5 - Eavecraft (eavecraft.com)

"Eave" is a real roofing/building term, and "-craft" signals care and skill rather than software - consistent with a product whose whole pitch is "smart defaults do the thinking so you don't have to configure anything." It's the weakest of the five because the trade term (eave) doesn't carry an inherent second meaning pointing back at marketing or leads the way "callback" or "shingle" do - it's a good-sounding, safe, available name rather than a name that argues for itself. Kept in the top 5 because it is clean, pronounceable, collision-free, and a reasonable fallback if Callbackline is somehow lost before purchase.

---

## Rejected notables (for the record)

- **Signpost** - not tested as a candidate; flagged during ideation because Signpost is an actual existing local-business marketing software company. Direct collision, never a real option.
- **Anchor, Signal, Compass, Ironclad, Craftsman, Baseline, Levelset, Cornerstone, Benchmark, Checkpoint, Callbox, Storefront, Pipeline, Blueprint** - all rejected pre-domain-check due to strong existing trademark collisions (Anchor.fm/Spotify, Signal messaging app, Compass real estate, Ironclad contract software, Craftsman/Sears, Cornerstone OnDemand, Check Point Software, Callbox lead-gen, Storefront pop-up retail, Pipeline CRM, multiple Blueprint software products).
- **Rafterline** - domain verified available, but downgraded out of the top 5 after search surfaced "Digital Rafter" and "RafterOne," two real marketing/digital-commerce firms already using the "Rafter" root in construction-adjacent services.
