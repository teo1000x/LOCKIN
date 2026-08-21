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

1. Buy bondedcrew.com, then the sitewide rename can happen in one commit.
2. EIN for CANU Group LLC, then Business Portfolio + Business Verification + dev app
   (`docs/23` and `docs/24`, tomorrow morning's job).
3. Fill .env.local: DATABASE_URL (Supabase pooler), ANTHROPIC_API_KEY, contact email/phone.
4. Sold-out Starter tier: keep, flip, or real count (docs/20 crack 2).
5. Authorise-do-not-charge risk reversal: yes or no (docs/20 section 3.1).
6. Confirm the 15 to 30x ROAS claim is substantiable with records, or it comes down.
7. 20 contractor names for Track C.

## Next build items, in order (operator work)

Auth with organizations, then the six-question intake wizard (`docs/22`) on the 96-trade
taxonomy, then the generation pipeline with per-org cost metering, then the approval UI on the
existing gate, then Stripe, then Meta OAuth and publishing against a dev app while review runs.
