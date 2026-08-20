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
#    not carry it. It lives in a private repo instead:
git clone https://github.com/teo1000x/lockin.git ~/Documents/LOCK\ IN

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

## State of play, one paragraph

Landing page, estimator, legal pages and the book-a-call pipeline are built and deployed. The
approval gate is hardened (bytes and composited text in the hash, 10 tests passing). The
/admin/leads queue exists behind fail-closed basic auth. Everything server-side is dark until
DATABASE_URL is set. The product name recommendation is Bonded Crew (`docs/21`,
bondedcrew.com verified free 19 Aug). The Meta filings are NOT started and are the critical
path (`docs/23` is the founder's click-by-click guide).

## Open founder decisions, carried forward

1. Buy bondedcrew.com, then the sitewide rename can happen in one commit.
2. Meta: Business Portfolio + Business Verification + dev app (`docs/23`, tonight's job).
3. Fill .env.local: DATABASE_URL (Supabase pooler), ANTHROPIC_API_KEY, contact email/phone.
4. Sold-out Starter tier: keep, flip, or real count (docs/20 crack 2).
5. Authorise-do-not-charge risk reversal: yes or no (docs/20 section 3.1).
6. Confirm the 15 to 30x ROAS claim is substantiable with records, or it comes down.
7. 20 contractor names for Track C.

## Next build items, in order (operator work)

Auth with organizations, then the six-question intake wizard (`docs/22`) on the 96-trade
taxonomy, then the generation pipeline with per-org cost metering, then the approval UI on the
existing gate, then Stripe, then Meta OAuth and publishing against a dev app while review runs.
