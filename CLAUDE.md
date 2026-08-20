# CLAUDE.md

Claude Code project instructions.

> **Read `AGENTS.md` first.** It holds the product definition, the inviolable rules, the
> design authority, the voice rules, the delegation model, and the document map. This file
> covers only what is specific to running Claude Code on this project.

---

## Where things are

Two directories, on purpose.

| | Path | Contains |
|---|---|---|
| Docs | `~/Library/Mobile Documents/com~apple~CloudDocs/LOCK IN/` | Strategy, research, specs. In iCloud so it syncs across devices. |
| Code | `~/Projects/ignition/` | The Next.js application. On local disk. |

**Never move the application into iCloud.** `node_modules` under iCloud sync produces file
locks, conflicted copies, and build failures that look like code bugs. The session's working
directory is the docs folder, so most code work needs an explicit path or `--prefix`.

---

## Current phase

**Strategy and foundations. Application feature work is paused by the founder.**

Do not start building product features. If asked to build UI or features, confirm the pause
has been lifted first. Existing code (schema, encryption, approval gate) is settled and
should not be rewritten.

---

## Running things

Typecheck and test:

```bash
cd ~/Projects/ignition && npx tsc --noEmit && npx tsx --test src/lib/__tests__/*.test.ts
```

Dev server, via the launch config in `.claude/launch.json`:
use the `foreman-dev` configuration on port 3000. Prefer `preview_start` over running
`npm run dev` in a Bash call, so the server is managed rather than orphaned.

Transcribe a YouTube video to text:

```bash
python3 tools/yt-transcribe.py "https://youtube.com/watch?v=XXXX" output-name
```

Note that `yt-dlp` lives at `~/Library/Python/3.9/bin/yt-dlp` and is not on PATH. The system
Python is 3.9, which caps yt-dlp at an older release, so the script falls back through five
YouTube player clients. The `android` client is the one currently working.

---

## Delegation

The founder has asked that substantive work be delegated to subagents rather than done
inline. Act as operator: scope the task, dispatch, review the returned artifact, integrate.

See the "Delegation model" section of `AGENTS.md` for the six things every agent prompt must
contain and the review checklist. The short version: agents start cold, so give exact file
paths for required reading and for output, and never trust an agent's summary without
verifying the artifact.

Do not delegate the inviolable code paths. The operator writes those directly:
`publish-decision.ts`, `publish-guard.ts`, `crypto.ts`, rate limiting, and cost metering.

---

## Design work

`docs/08-DESIGN-SYSTEM.md` is binding. It derives from the anti-slop skill installed at
`~/.claude/skills/taste-skill/SKILL.md`, which is also available as `/taste-skill` along
with `/redesign-skill`, `/soft-skill`, `/brandkit`, and nine others.

Before shipping any UI, run the pre-flight checklist at the end of the design system doc.
The most commonly violated rules on this project so far have been the em-dash ban, the
warm-cream-plus-clay palette (explicitly banned in the skill's Section 4.2), section-number
eyebrows like `01 / 02 / 03`, decorative status dots, and Inter as a default body font.

---

## Code conventions

- TypeScript strict. No `any` without a comment justifying it.
- All external API calls go through a typed client in `src/lib/`. Never call `fetch` to Meta
  from a route handler or a component.
- Every Inngest function is idempotent and safe to replay.
- Database access through Drizzle only. Migrations committed and reviewed.
- Pure decision logic stays free of I/O imports so it can be tested without a database. The
  approval gate is the reference example: `publish-decision.ts` has zero imports, and
  `publish-guard.ts` does the database work around it.
- Secrets in env vars. Never commit `.env*`. Never log a token.
- Meter LLM and image generation per organization. Every generation call records its cost.
