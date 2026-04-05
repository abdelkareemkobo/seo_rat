# SEO RAT — Design & Roadmap

---

## ✅ Completed

### Core Infrastructure

- [x] Refactor codebase
  - make teh auth one time not everytime make ti better flow as a desktop application 
  - Create the Index.ipynb
- [x] Daily GSC data sync (background script)
- [x] Smart pull: detect last pulled day, fill missing date ranges
- [x] Syncthing database — daily pulling into system + backup
- [x] When article path changes, reflect it in the database `path` attribute

### Content SEO

- [x] Primary keyword placement (title, H1, first paragraph, URL)
- [x] Heading hierarchy (H2/H3 structure)
- [x] Content freshness (publishDate age)
- [x] Secondary keywords — top 5 added
- [x] Missing queries in content detection
- [x] Content gap analysis (queries with no matching page)

### Link Health

- [x] Internal link count (flag pages with < 3 internal links)
- [x] Orphan pages (zero inbound internal links)

### GSC Signals & Queries

- [x] Rising vs declining query detection
- [x] Query intent classification (rule-based: informational, navigational, commercial, transactional)
- [x] Green keyword detection (rising impressions, decent position, not yet optimized)
- [x] Rank tracking based on country for specific keywords
- [x] Store queries info per page (detect keyword stuffing / off-topic queries)
- [x] Intent helper functions that return data for a specific intent

### AI Features

- [x] Missing keyword detection per page
- [x] Heading structure suggestions

### Schema & Structured Data

- [x] Schema validation
- [x] FAQ extraction from GSC data

### Index Tracking

- [x] Not-indexed pages with reasons

### Reporting

- [x] One-page SEO health report per site
- [x] Fix remaining bugs (page title fallback, HTML link extraction)

### Tested Websites

- [x] kareemai.com
- [x] awazly.com

---

## 🔄 In Progress / Partially Done

### Content SEO

- [x] **Keyword cannibalization** — multiple pages targeting the same keyword
    - [x] Known case: شركة عزل بولي يوريا بجدة appears on two pages
    - [x] How to Detect Keyword Cannibalization?
        - [x] Content and Metadata Data
        - [x] Similar search queries from GSC?
    - missing the DSPy filter to filter the data from noise signals based on the info we had.

### On-Page Technical SEO

- Canonical tag detection
- Meta robots / noindex detection
- Hreflang tags

### Schema

- [x] Competitor analysis for schema used
    - I build it as an extenion i need to add to the store and buy the 5$ for it.
- [ ] Page-needed schema prediction
    - DSPy app that read the data and curretn schema and suggest the needed schema.
    - but this also still need to know about the compatitors schemas.

### Index Tracking

- [x] **Status tracking over time**
    - [x] Design decision needed: weekly cron job writing to `index_status_history` table
    - [x] Does Google expose raw historical indexing data via API?

### Query Intent Classification

I think the intent classification will not help us for now

- [x] Expand rule-based classifier to cover:
- Local intent
    - Generative intent (e.g. "write a LinkedIn post about…")
    - Decide: stay rule-based or invest in a BERT classifier?

---

## 📋 Backlog (Prioritized)

### High Priority

1. **Alt text suggestions** — last missing item to close Phase 3
2. **Broken link detection** (404s) — use async `httpx` checks
3. **Anchor text quality** — flag generic anchors like "click here" (needs DSPy signature or pattern)
4. [x] **Keyword cannibalization** — finish detection logic (data already available)
5. [x] **Phase 4 index status tracking** — pick simple weekly cron approach and ship it

### Medium Priority

6. **nbdev documentation** — correct and complete
7. **Async-first code** — refactor blocking calls
8. **Manual focus keyword input + automatic secondary keyword assignment**
9. **Internal linking suggestions** — upgrade to embedding-based solution
10. **Add other websites** to the system:
    - [x] shelid.com
    - [x] azlzone.com
    - [x] emdadelgaz.com
    - [x] protineai.com
    - [x] gpuvec.com
    - samagarden.com

### Lower Priority

11. **Full content similarity / near-duplicate detection**
12. [x] **GSC optimization** — filter by country, month, goal
13. **NLP for question/query extraction** — DSPy to catch FAQs not captured by current pattern
14. **Trend analysis** — date range comparison, auto-flag rising vs declining queries
15. **Indexing status dashboard** — submit, track, visualize over time
16. **Content mapper improvements** — handle homepage and non-Jamstack pages
17. **Easier article insertion** — dedicated function with built-in looping

---

## 🖼️ Media & Rich Results

- [ ] Image uniqueness check
- [ ] Lazy loading detection
- [ ] Image compression check

---

## 🌐 Web App (FastHTML)

- [ ] Add your website UI
- [ ] Data sync UI
- [ ] SERPWatcher
- [ ] Backlink Checker
- [ ] Site Explorer

---

## 🔮 Ideas & Future (Not Scheduled)

### AI & Intelligence

- LLM-powered improvement suggestions per page (full content)
- BERT-based query intent classification
- Agentic orchestrator (plan + execution)
- GSC trend pattern analysis (seasonal, weekly spikes, year-over-year)
- Better content description for queries/keywords using LLM
- Better duplicate detection approach

### Schema & Structured Data

- FastHTML use case: pre-configured Google schema.org generator (26 types)
    - Validate the data
    - Pre-compiled library

### Integrations

- Bing integration (IndexNow Protocol + Bing AI trend capture)
- Agentic Commerce Protocol / MCP / Agent Skill

### Architecture Questions

- How to handle large `{url: path}` dicts efficiently?
- Should content lines be stored for LLM chunk editing?
- How do Ahrefs/SEMrush get domain visitor + keyword data?

---

## 🏷️ Self-Branding & Outreach

- [ ] Share with Sherno
- [ ] Share with SolveIt chat — ask Jeremy for help/advice
- [ ] Correct blog post about SEO RAT
- [ ] Test case with fastai blog system (Quarto-based)

---

## 📝 Known Issues

- Some keywords don't match page topic (e.g. `sbak-baldwadmy` got شركة كشف تسربات instead of a plumbing keyword)
- Two pages share the same top keyword: شركة عزل بولي يوريا بجدة → keyword cannibalization

---

## 📚 Expert Insights to Implement

| Glenn Gabe | Date range comparison; auto-flag rising vs declining queries | 🔄 Rising detection done, trend analysis
pending |
| Jes Scholz | Track GSC performance before/after content changes; store historical data | 🔄 Partial |

---

## 🔧 Quarto-Specific Notes

- General Quarto frontmatter rules (include/exclude code cells in `.ipynb`)
- `slug:` frontmatter option controls output URL

## Bing Web Master Features

- Error Detection and Report
- Duplication Detection
- AI Performance

## RankgMath Missing Features

- Social meta (OpenGraph, Twitter Cards)
- PageSpeed tracking per page
- Email SEO reports (weekly/monthly digests)
- llms.txt generator (new AI crawler feature)
- Knowledge Graph markup
- Canonical tag management
- robots.txt / .htaccess editor
- Nofollow/noindex controls