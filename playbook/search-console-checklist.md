# Search Console Setup Checklist

Do this once the current `v5` branch is pushed and deployed (the redirects and meta fixes must be live first).
Total time: ~30 minutes, then 5 minutes/week of monitoring.

## Why this matters

Google's index of rohitmalekar.in is stale: it still shows the old site title ("Stories of craft, culture, community and then some") and old URL structures that now 404. Nothing tells Google to recrawl until you register the site and submit the sitemap. Bing matters too — ChatGPT and Copilot retrieval run on Bing's index.

## Google Search Console (~20 min)

1. Go to https://search.google.com/search-console and sign in with the Google account you want to own this permanently.
2. Add a property → choose **Domain** (not URL prefix) → enter `rohitmalekar.in`.
3. Verify via DNS: GSC gives you a TXT record; add it at your DNS provider (wherever rohitmalekar.in's DNS lives). Propagation can take minutes to a few hours — the "Verify" button can be retried.
4. Once verified: **Sitemaps** (left nav) → submit `https://rohitmalekar.in/sitemap.xml`.
5. **URL Inspection** (top bar) → paste each of these, then click "Request Indexing" for each (quota is ~10/day; do these first, rest tomorrow):
   - `https://rohitmalekar.in/`
   - `https://rohitmalekar.in/work-with-me`
   - `https://rohitmalekar.in/about`
   - `https://rohitmalekar.in/portfolio/`
   - `https://rohitmalekar.in/portfolio/ens-dao-governance-research`
   - `https://rohitmalekar.in/portfolio/gg24-interop-round`
   - `https://rohitmalekar.in/articles/coordination/`
   - Day 2: the other three theme indexes + your 3-4 strongest essays.
6. **Pages** report (Indexing section): note the "Not found (404)" list. Cross-check against `redirects.json` in the repo — if Google reports old URLs we didn't map, add them to `redirects.json` (old path → current slug) and redeploy.

## Bing Webmaster Tools (~10 min)

1. Go to https://www.bing.com/webmasters and sign in (Microsoft account, or import directly from your verified GSC property — the import option does everything in one click).
2. If not importing: add site `rohitmalekar.in`, verify via DNS (same TXT flow).
3. Submit the sitemap: `https://rohitmalekar.in/sitemap.xml`.
4. Optional but useful: URL Submission for the same priority pages as above.

## Weekly (5 min, for the next 6-8 weeks)

- GSC → Pages: 404 count should trend down as redirect stubs get crawled; indexed-pages count should trend up.
- GSC → Performance: watch impressions for the query "rohit malekar" — the goal is rohitmalekar.in in the top 3 within ~6 weeks.
- Search `"Rohit Malekar"` in an incognito window; note what ranks. Also try `site:rohitmalekar.in` — stale titles should progressively refresh.

## Validation (after deploy, before GSC)

- `curl -I https://rohitmalekar.in/Articles/Culture/Litmus+Test+for+Leadership` → expect **200** (redirect stub, was 404)
- `curl -s https://rohitmalekar.in/ | grep canonical` → expect `<link rel="canonical" href="https://rohitmalekar.in/"/>`
- https://search.google.com/test/rich-results on the homepage → expect Person + WebSite detected
- https://validator.schema.org on an essay URL → expect Article
