# HANDOFF: new machine, new session, start here

_Written 19 August 2026, end of the day the backend started. If you are a fresh Claude session
reading this, this file plus `AGENTS.md` is your warm start. Read `AGENTS.md` next, then
`ROADMAP.md`, then `docs/18` and `docs/23`. Delete this file once its setup section is done._

## Where everything lives

| What | Where | Transfers by |
|---|---|---|
| Application code | github.com/teo1000x/SAAS (private), clean and fully pushed at `21756de` | git clone |
| Strategy, specs, research (this folder) | its own private git repo (see below) | git clone |
| Dev server config | `.claude/launch.json`, inside this folder | comes with the clone |
| Claude skills (taste-skill and 12 others) | `transfer/claude-skills.zip`, inside this folder | comes with the clone, unzip to ~/.claude/ |
| Secrets | `~/Projects/ignition/.env.local` on the OLD machine only | AirDrop, never chat or email |

## New machine setup, in order

```bash
# 0. This folder first. The machines use different Apple IDs, so iCloud does
#    not carry it. It lives in a private repo instead (renamed to LOCKIN on
#    GitHub 19 Aug). The old machine's iCloud copy is frozen and stale; the
#    git repo is the only current copy, so always clone or pull, never work
#    from the iCloud folder:
git clone https://github.com/teo1000x/LOCKIN.git ~/Documents/LOCK\ IN

# 1. Code. On local disk, in its own separate clone.
git clone https://github.com/teo1000x/SAAS.git ~/Projects/ignition
cd ~/Projects/ignition && npm install

# 2. Skills.
unzip ~/Documents/LOCK\ IN/transfer/claude-skills.zip -d ~/.claude/

# 3. Secrets: AirDrop .env.local from the old machine into ~/Projects/ignition/
#    (in Finder press Cmd+Shift+. to reveal hidden files).
#    If it was never filled in, just recreate it: .env.example lists every key,
#    and BETTER_AUTH_SECRET / ADMIN_PASSWORD are openssl rand -base64 32.

# 4. Verify.
cd ~/Projects/ignition && npx tsc --noEmit && npx tsx --test src/lib/__tests__/*.test.ts
```

Open Claude Code with the cloned LOCK IN folder as the working directory, same convention as
before. From now on this folder is synced with git like the code: commit and push doc changes
at the end of a session, pull at the start of one.

**Setup status, checked 19 August on the new machine:** steps 0, 1, 2 and 4 are done
(typecheck clean, 10/10 gate tests passing, skills unzipped). Step 3 is half done:
`.env.local` was recreated from `.env.example` and `BETTER_AUTH_SECRET` plus `ADMIN_PASSWORD`
were generated. `DATABASE_URL`, `ANTHROPIC_API_KEY`, the Stripe keys and the public contact
details are still empty and are the founder's to fill. Delete this file once they are in.

## State of play, one paragraph

Landing page, estimator, legal pages and the book-a-call pipeline are built and deployed. The
approval gate is hardened (bytes and composited text in the hash, 10 tests passing). The
/admin/leads queue exists behind fail-closed basic auth. Everything server-side is dark until
DATABASE_URL is set. The product name recommendation is Bonded Crew (`docs/21`,
bondedcrew.com verified free 19 Aug). The Meta filings are NOT started and are the critical
path (`docs/23` is the founder's click-by-click guide, `docs/24` is the verification prep,
now largely resolved: the entity is CANU Group LLC, Wyoming, Active, Articles PDF in hand).

## Session log, 19 August evening (new machine)

Setup verified: typecheck clean, 10/10 gate tests passing. `.env.local` recreated from
`.env.example` with `BETTER_AUTH_SECRET` and `ADMIN_PASSWORD` generated; `DATABASE_URL` and
`ANTHROPIC_API_KEY` still missing. `.env.local` never travels by git, so on another machine
either AirDrop it or regenerate the same way. Docs synced to verified state.
`docs/24-BUSINESS-VERIFICATION-PREP.md` written and mostly resolved: legal name CANU Group
LLC (filed Wyoming 26 April 2026, confirmed Active), business address 3637 Keystone Ave, Los
Angeles, CA 90034, Articles PDF in the founder's Downloads as `images.pdf` (rename it).
bondedcrew.com still free at midnight Eastern 19/20 Aug.

**Tomorrow, in order:** EIN at the irs.gov EIN Assistant (opens 7 a.m. Eastern, walkthrough
in `docs/24`), buy bondedcrew.com and create hello@, enable 2FA on the personal Facebook,
then `docs/23` steps 2 and 3 (Business Portfolio as CANU Group LLC, submit verification).
Tell the operator as each lands so the checklists get checked off.

## Session log, 25 August (Windows machine): first session, compositor fit fix

Windows setup verified working: both repos cloned, `.env.local` in place and renamed, skills
extracted, typecheck clean, tests passing. One machine quirk: Node is on the machine PATH but
a Claude Code session launched before the install may not see it; prefix
`C:\Program Files\nodejs` onto PATH in-session if `npx` is not found. Founder: if not done
yet, delete `env.local` from the WIN11 USB and empty the Recycle Bin.

The queued compositor polish turned out systemic, not cosmetic: probe renders showed the
docs/19 fixed type sizes never fit the spec's own calibration strings ("FIRST CLEAN", "$99"
and the sub-line all escaped the disc; the 27-character calibration headline wrapped and
clipped). Fixed on main at `9305040`: real Public Sans advance widths generated from the
shipped woff files, a pure measurement module, measured-width gates on every composited run
with a new `textDoesNotFit` typed failure that feeds regeneration, four-figure medallion
prices refused, and re-solved fixed sizes (figure 124/92/72 by shape, FREE 80, headline
56 stepping to 42, T5 figure 50, season line wrapping at 32, corner plates hugging their
text). Full reasoning and the before/after table are docs/19 section 9. 173 tests passing
including a new pixel-containment regression test. Probe renders of T1/T2/T3/T5/T6 all
eyeballed clean.

**Next session, in order:** docs/25 item 8, persist + hash + approval workspace wired to
`publish-guard.ts` (operator-written), then item 9, the export walkthrough page. Still
blocked on founder: Anthropic top-up (~$20) and fal.ai top-up (~$10) gate the first live
end-to-end generation; Stripe account gates checkout; Meta filing status still unreported.

## Session log, 25 August evening: item 8 done, Track A on hold

docs/25 **item 8 is DONE** and pushed (`cb5a34d`): the pipeline's artifacts persist as
ad-variant rows whose contentHash covers copy, rendered bytes and drawn strings
(`variant-row.ts` pure + `campaign-persist.ts`); "Build my ads" assembles intake from the
wizard rows (`generate-campaign.ts`, offer type derived deterministically with a reason,
photo/logo dimensions parsed from bytes, credits spent first and refunded when nothing
lands); and the approval workspace runs per-ad approve / edit / reject through real
`approvals` rows. Verified in the browser against the dev database: approve passes
`assertPublishable`, editing an approved ad voids the approval and blocks the gate, a
guarantee-word edit is refused by the deterministic lint, reject is skipped rather than an
error. Dev tools committed: `scripts/seed-approval-workspace.ts` (seeds a walkable workspace
for any signed-up dev user) and `scripts/check-gate.ts` (prints the gate's live decision).
Test fixture in the dev db: user op-item8-walk@example.com, campaigns under Bright Homes
Cleaning. Known v1 gap: generation refuses custom (category-fallback) trades with a plain
message; the pipeline needs a category-pattern path (docs/25 item 6 scope).

**FOUNDER, same day: Track A (EIN, domain, Meta verification) is ON HOLD** per the note in
the open-decisions section. Focus is Stripe test mode plus the V1 loop. Stripe checkout
build (docs/25 item 3) starts the moment `STRIPE_SECRET_KEY` and
`NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY` (test mode) land in `.env.local`.

Windows note: launch.json gained `foreman-dev-win` (cmd wrapper that prefixes the Node dir
onto PATH). Once Claude Code is relaunched fresh, plain `foreman-dev` works and the wrapper
can be dropped.

**Next: docs/25 item 9, the export walkthrough page.** Then Stripe (item 3) when keys land.

## Machine switch to WINDOWS, added 21 Aug

Same model as always: git carries everything except secrets. One-time setup on Windows:

```
# 0. Install once: Git for Windows (git-scm.com, includes Git Bash and the
#    credential manager that signs you into GitHub via browser), Node.js 22 LTS
#    (nodejs.org), and Claude Code (claude.com/claude-code).
# 1. In Git Bash (Start menu after installing git):
git config --global user.name "Mateo Canu"
git config --global user.email "mateo4canu@gmail.com"
#    ^ do NOT skip: an unset identity is why Vercel silently blocked deploys on 20 Aug.
git clone https://github.com/teo1000x/LOCKIN.git "$HOME/Documents/LOCK IN"
git clone https://github.com/teo1000x/SAAS.git "$HOME/Projects/ignition"
cd "$HOME/Projects/ignition" && npm install
# 2. Secrets: already copied to the founder's WIN11 USB drive on 25 Aug as a
#    VISIBLE file named env.local (no leading dot). Copy it into
#    C:\Users\<you>\Projects\ignition\ then rename it in Git Bash:
#      mv "$HOME/Projects/ignition/env.local" "$HOME/Projects/ignition/.env.local"
#    Delete env.local from the USB afterwards and empty the Recycle Bin.
#    Never chat, never email.
# 3. Skills: extract transfer\claude-skills.zip (in this folder) into
#    C:\Users\<you>\.claude\
# 4. Verify: npx tsc --noEmit && npx tsx --test src/lib/__tests__/*.test.ts
#    Expect 166 passing, 1 skipped (the live generation test skips politely).
# 5. Open Claude Code with the LOCK IN folder as working directory:
#    "read HANDOFF.md, pick up where we left off."
```

State at this switch (21 Aug): generation pipeline merged to main (166 tests), real
dashboard live, wizard live behind /login. Blocked on founder: Anthropic top-up (~$20 at
console.anthropic.com Billing) and fal.ai top-up (~$10), which gate the first live
end-to-end generation; Stripe account; Meta filing status still unreported. Operator queue:
compositor visual polish (long square headlines clip, medallion text can overflow the disc,
found by the pipeline agent's probe render), then persistence + approval workspace wired to
publish-guard (docs/25 items 8 and 9).

## Machine switch, 20 Aug evening: work machine back to home machine

Git carries everything except secrets. On the home machine, in order:

1. **AirDrop `~/Projects/ignition/.env.local` from the work machine first.** It now holds
   the live DATABASE_URL (rotated password), ANTHROPIC_API_KEY, FAL_KEY, and the current
   BETTER_AUTH_SECRET and ADMIN_PASSWORD. Reveal it in Finder with Cmd+Shift+. and drop it
   into `~/Projects/ignition/` on the other machine, replacing whatever is there. Without
   this, server work is dark on that machine.
2. `cd ~/Documents/LOCK\ IN && git pull` (this folder).
3. `cd ~/Projects/ignition && git pull && git checkout wip/wizard-lint && npm install`
   (new deps landed today: satori, resvg, fontsource).
4. Sanity check: `npx tsc --noEmit && npx tsx --test src/lib/__tests__/*.test.ts`
   (expect 101 passing).
5. If commits from that machine ever show "Blocked" on Vercel again, set the identity:
   `git config --global user.name "Mateo Canu"` and
   `git config --global user.email "mateo4canu@gmail.com"`. That exact misconfig cost an
   hour today on the work machine.

Then open Claude Code in the LOCK IN folder and say "read HANDOFF.md, pick up where we
left off." The session log below plus `docs/25` carry the full state.

## Session log, 20 August (work machine): the build day

`docs/25-GENERATOR-BUILD-SPEC.md` is the file of record; its checklist carries per-item
status. Summary: founder approved the spec; all three keys are in `.env.local` on the work
machine and verified; Supabase provisioned, 4 migrations applied; site fixes deployed
(squared radii, sans %, credits per tier at 400/1,600/4,000, ten-questions claim); the
deterministic compositor (68 tests) and credit metering (8 tests) are DONE and on main;
Better Auth with organizations is live on production. Vercel deploys were unblocked by
setting the machine's git identity (was unset, Vercel blocked unknown authors) and by
re-entering env vars that an early import had saved with empty values. Production verified
end to end at saas-eight-ebon-56.vercel.app. Test users op-test@example.com,
op-test2@example.com, wizard-check-3002@example.com exist in the dev database.

**Branch `wip/wizard-lint` holds unmerged work:** the agent-built ten-screen intake wizard
(101 tests passed on the agent's run, operator review NOT yet done), the policy lint
(`src/lib/policy-lint.ts`, deterministic docs/14 rules, tests not yet written), and prompt
injection hardening (`src/lib/prompt-safety.ts`, control-character regex needs verifying).
Do not merge to main before: lint + prompt-safety test suites written and passing, the
operator browser-walks the wizard on the dev server, and the docs/08 pre-flight runs on the
wizard screens.

**Next session, in order:** review and merge `wip/wizard-lint`, then the generation
pipeline (blueprint schema, Claude tool-use call, fal.ai photo bed, compositor integration,
credits spend per action), then the approval workspace wired to `publish-guard.ts`. Founder
items: Stripe account (gates checkout), Meta filing status still unreported (EIN, domain,
portfolio: ask), and the Supabase storage keys (`SUPABASE_URL`, `SUPABASE_SECRET_KEY` from
the dashboard's connect dialog) whenever photos should move off local disk.

## Open founder decisions, carried forward

**FOUNDER, 25 Aug: Track A is ON HOLD.** The EIN, the bondedcrew.com purchase, and the whole
Meta Business Portfolio / Business Verification chain (decisions 1 and 2 below) wait until
the founder says go. Consequence, stated once: the two Meta review queues are roughly 8 to 12
weeks and only start when filed, so publishing-to-Meta moves out by at least that long from
whenever the hold lifts. The export walkthrough path does not depend on Meta and stays the
v1 terminal step. Current focus: Stripe test mode end to end, then the V1 loop.

1. Buy bondedcrew.com, then the sitewide rename can happen in one commit. ON HOLD.
2. EIN for CANU Group LLC, then Business Portfolio + Business Verification + dev app
   (`docs/23` and `docs/24`). ON HOLD.
3. Fill .env.local: DATABASE_URL (Supabase pooler), ANTHROPIC_API_KEY, contact email/phone.
4. Sold-out Starter tier: keep, flip, or real count (docs/20 crack 2).
5. Authorise-do-not-charge risk reversal: yes or no (docs/20 section 3.1).
6. Confirm the 15 to 30x ROAS claim is substantiable with records, or it comes down.
7. 20 contractor names for Track C.

## Next build items, in order (operator work)

Auth with organizations, then the six-question intake wizard (`docs/22`) on the 96-trade
taxonomy, then the generation pipeline with per-org cost metering, then the approval UI on the
existing gate, then Stripe, then Meta OAuth and publishing against a dev app while review runs.
