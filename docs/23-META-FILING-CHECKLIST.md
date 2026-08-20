# Meta filing checklist, click by click

_Written 19 August 2026 for the founder's evening session. This is the critical path: two
sequential queues, roughly 8 to 12 weeks combined, zero code required. Detail on the
permissions themselves is in `docs/03-META-PLAYBOOK.md`._

## Have at hand before you start

- Your LLC formation document and EIN letter, as PDFs or photos.
- The business address and a phone number that can receive a verification call or text.
- The domain, once purchased, and an email address AT that domain (hello@yourdomain). Meta
  treats a matching-domain email as identity evidence, so create it before verifying.
- Your personal Facebook account, logged in. Business assets hang off a personal login.
- A card for the domain purchase only. Nothing tonight costs money except the domain.

## Step 1 (5 min): buy the domain

Registrar of your choice (Cloudflare, Porkbun, Namecheap). Verify it is still free first:

```bash
whois -h whois.verisign-grs.com bondedcrew.com | head -3
```

"No match" means free. Buy it, then create the hello@ mailbox (most registrars offer email
forwarding free, which is enough for verification).

## Step 2 (15 min): Business Portfolio

1. business.facebook.com, log in with your personal account.
2. Create a Business Portfolio. Use the LLC's exact legal name as registered, not the brand.
3. Settings, Business info: fill address, phone, website (the new domain), business email
   (the hello@ address). Confirm the email when the code arrives.

## Step 3 (20 min): Business Verification

1. Business settings, Security centre, Start verification.
2. Legal name and address exactly as on the LLC documents. A mismatch is the number one
   rejection cause, so copy character for character.
3. Upload the formation document or EIN letter when asked.
4. Choose phone or email at the domain for the confirmation code.
5. Submit. Typical turnaround is days, can stretch to three weeks. Nothing else in this
   checklist waits on it, so keep going.

## Step 4 (15 min): the developer app

1. developers.facebook.com, Create app, type Business, connect it to the portfolio.
2. Name the app after the brand.
3. App settings, Basic:
   - Privacy policy URL: https://YOURDOMAIN/privacy
   - Terms of service URL: https://YOURDOMAIN/terms
   - Data deletion: choose URL, point at https://YOURDOMAIN/privacy#deletion
   - App icon, 1024px. Ask the operator, the placeholder mark exports at that size.
   - Category: Business and pages.
4. Add the Marketing API product to the app.

These URLs must be live on the real domain first, which means the Vercel deployment needs the
custom domain attached before this step. Vercel, project, Settings, Domains, add it, then set
the DNS records the screen shows at the registrar. Allow an hour for DNS.

## Step 5: App Review, the long queue

Filed from the app dashboard, App Review, Permissions and features. Request the permission set
listed in `docs/03-META-PLAYBOOK.md` (ads_management, ads_read, business_management,
pages_show_list, pages_read_engagement, pages_manage_metadata, leads_retrieval,
instagram_basic).

Each permission needs a written usage description and a screencast showing it in use. The
screencast needs enough real UI to record, which is item A4 on the roadmap and the operator's
job. File Steps 1 to 4 tonight; Step 5 goes in as soon as the screencast exists. Business
Verification (Step 3) reviews in parallel, so no time is lost by the gap.

## What NOT to do tonight

- Do not request permissions with a placeholder screencast. A sloppy first submission earns a
  rejection, and rejections slow later attempts.
- Do not verify under the brand name if the LLC is registered under a different legal name.
- Do not use a personal gmail as the business email if the domain mailbox exists.

## When each thing unblocks

| After | We can |
|---|---|
| Step 1 | Rename the product, rebuild legal pages on the real entity, attach the domain |
| Step 4 | Develop against the Marketing API in dev mode with our own test ad account |
| Step 3 approved | File Step 5 |
| Step 5 approved | Publish to real customer accounts. This is launch. |
