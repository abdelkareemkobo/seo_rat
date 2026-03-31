
## Todo

1. [x] refactor
2. Correct nbdev doc
3. Async first code
4. [x] Add secondary keywords also the top 5
5. alt text quality
6. manual adding of the focus keyword & automatic for seconday keywords
7.[x] daily synching of the data
   - background script
7. [x] ranking of the website (we already have the data in stored just aggregate it)
8. add other websites
9. what is google discovery and how to use it
10. indexing status

#### SEO analysis

### Issues

- Some keywords don't match the page topic well (e.g. sbak-baldwadmy got شركة كشف تسربات instead of a plumbing keyword)
- Two pages share the same top keyword: شركة عزل بولي يوريا بجدة — that's potential keyword cannibalization

****

Content SEO Essentials

1. [x] Primary keyword placement (title, H1, first paragraph, URL)
2. [x] Heading hierarchy (H2/H3 structure)
3. [x] Content freshness (publishDate age)
4. Full content similarity / near-duplicate detection
5. Keyword cannibalization (multiple pages targeting same keyword)

On-Page Technical SEO
6. URL/slug quality (underscores, length, non-ASCII)

   1. Underscores vs hyphens — Google has said it treats them the same now, but hyphens are still best practice
   2. Slug length — shorter slugs help with CTR (more readable in search results) and are easier to share
   3. Non-ASCII in URLs — this is actually more relevant for your Arabic sites. Browsers display Arabic slugs nicely, but raw URLs get percent-encoded (e.g. %D9%85%D8%B9%D9%84%D9%85) which looks ugly in SERPs and can hurt CTR
   4. Canonical tag detection
   5. Meta robots / noindex detection
   6. Hreflang tags

Link Health

1. [x]Internal link count (flag < 3, suggest related pages)
2. Anchor text quality (flag generic "click here") | needs pattern or small dspy signature
3. Broken link detection (404s)
4. [x] Orphan pages (zero inbound internal links)

Local SEO
15. City + service keyword signals in title, H1, first paragraph
16. Schema markup (LocalBusiness, FAQ, BreadcrumbList)
    1.  [x] validate schema
    2.  [x] extract faq from GSC data
    3.  [ ] compatitor analysis for schema used
    4.  [ ] Page needed Schema Prediction

Media & Rich Results
17. Image optimization (filenames, captions, context)
18. Schema markup detection for rich results

EEAT & Trust (Advanced)
19. Testimonials, author info, sources, real photos

AI-Powered (Future)
20. LLM-powered improvement suggestions per page

**Images**

- Unique of the images
- LazyLoading
- Compressing
- Correct Alt text

****

1. GSC Info
   - optimize and enhance with gsc signals (country, month, goal)
   - NLP for questions and queries and we should include them correctly
2. Other Pages

## Technical update

1. how to make the content_mapper bertter modualr
2. how to map the homepage and other pages that are not jam stack like the other routes?? h
   1. how to conifure them?
   2. how to read it's content (html or source code)
3. making the inserting of articles to the sqlite database more easier and has it's own function that creates the looping
4. add each factor and how it's important to the recent Google Algorthim updates like how grok give you a table

#### AI Features

1. Keywords Suggetionsd

2. Better
   1. Heaings, Description , Title
3. Keywords to add
   1. [x] what is missing keywords
   2. is it already optimized or not?
   3. how to hanlde new days or queries?
4. Better content description for queries or keywords..etc
5. Ideas suggetions
6. Better Alt images

##### Smart Search

1. BM25 Usage and Importance

2. Duplication detection better approach

###### ![Gemini RAG anallysis Tool](https://lilyray.nyc/gemini-rag-analysis-tool/)

#### Index Tracking System

1. What is not indexed
2. Reasons?
3. Solving?
4. Submit
5. Dashboard to track

### Orchestrators

- plan
- execution

#### Questions

1. how ahrefs ans semrash get their data
   1. like domain info vistior,
   2. kewyords...etc

#### Visualizations

#### Architecture Design

1. how to hanlde access a dict that has key and value that are very long like {url:path}??
2. Should i add the lines of the content for the retrieved data or this is uncessry complexity but it helps in making the llm able to detect the chunk to edit and update!

### Syncthing database

1. Backup
2. Daily pulling data into our system

#### Lilyraynyc SEO recommenditions

1. Get all branded questions in your Query search engine and answer them in the content
2. The content should be udpated! not just submit without updates

##### Nice

1. Agentic Commerce Protocal

# Expert Insights for SEO RAT

### 1. Lily Ray - Intent Over Keywords

**Idea:** Understand *why* users search, not just *what* they type.

**For your system:**

- Classify queries by intent: informational, comparison, transactional
- LLM should suggest content that answers the *intent*, not just mentions keywords

---

### 2. Glenn Gabe - Trend Analysis

**Idea:** Compare time periods to spot patterns. Single data points are noise.

**For your system:**

- Add date range comparison to GSC queries
- Auto-flag: rising queries (opportunity) vs declining (needs refresh)

---

### 3. Cindy Krum - Entity/Topic Focus

**Idea:** Google understands *topics and relationships*, not just words.

**For your system:**

- Don't just match keywords - understand what the page is *about*
- LLM should identify the main entity/topic and related concepts
- Suggest secondary keywords that are semantically related

---

### 4. Jono Alderson - User Experience First

**Idea:** Clean architecture, good UX, meaningful content wins long-term.

**For your system:**

- Check heading structure (logical hierarchy)
- Internal linking (pages should connect logically)
- Content should be scannable (your readability module)

---

### 5. Aleyda Solis - Structured Processes

**Idea:** SEO should be repeatable, systematic, not ad-hoc fixes.

**For your system:**

- Your SEO report is exactly this! ✅
- Add: priority scoring (what to fix first?)
- Add: checklist output (actionable tasks)

---

### 6. Jes Scholz - Experimentation

**Idea:** Test changes, measure results, iterate.

**For your system:**

- Track GSC performance before/after content changes
- Store historical data to measure impact of optimizations

---

### 7. Barry Adams - Specificity Matters

**Idea:** Different content types have different rules (news vs blog vs product).

**For your system:**

- Your Quarto blog may need different checks than a product page
- Consider content type in recommendations

---

### 8. Kevin Indig - Strategic Context

**Idea:** SEO exists within business goals, not in isolation.

**For your system:**

- Which pages matter most to you? (traffic? conversions? brand?)
- Prioritize optimization based on business value, not just SEO score

---

### 9. Crystal Carter - Machine Readability

**Idea:** Help Google *understand* your content through structure.

**For your system:**

- Check for structured data opportunities
- Verify metadata is complete and accurate
- Alt text helps Google understand images

---

### 10. Marie Haynes - Quality Alignment

**Idea:** Align with Google's quality direction, not tricks.

**For your system:**

- E-E-A-T signals: author info, expertise shown, sources cited
- Content depth > keyword density
- LLM should suggest quality improvements, not manipulation

---

- Async from first approch
- Test all website:
  kareemai.com
  shelid.com
  awazly.com
  azlzone.com
  emdadelgaz.com
  protineai.com
  gpuvec.com
  samagarden.com
  ...etc

## Test-Drive Approch

1. One-Page SEO report for all websites for basic seo
**Phase 1: Foundation & Current Content**

- [x] Fix remaining bugs (pagetitle fallback, HTML link extraction)
- [x] One-page SEO health report per site
- [ ] smart pull of date , know what was the last day you pulled and then store_date_range for the current day!
- [ ] fill in days that has no data at all
- [ ] i have now the intent in the data but i will needt to create helper function that return the data for specific intent!
- [ ] when we change the article path how this should be reflected in teh database path attribute
- [ ] we need a way to store the queries info
  exmple :
    superproductivity docker compose => is not related to my goal of hte blog and not helpful! it's keyword stuffing!
- [ ] url_mapping will not work with main url!
- [ ] rank tracking based on country for specific keywords
- [ ] Daily GSC data sync

**Phase 2: GSC Signals & Queries**

- [x] Rising vs declining query detection
- [x] Query intent classification (informational, comparison, transactional)
    Rule based need more enhnace in the future
    expand more to :
  - Informational — users seeking knowledge, such as "how to start SEO"
  - Navigational — users looking for a specific brand or website, like "Facebook login"
  - Commercial Investigation — comparison or evaluation behaviour, such as "best SEO tools"
  - Transactional — readiness to take action, like "buy SEO software"
  - Traditionally, SEO recognized five types (adding Local to the above four), but with the rise of AI tools like ChatGPT, there's now a sixth type: Generative search intent.
  - Generative — content creation, problem-solving, data processing requests like "Write a LinkedIn post about..." or "Provide a Python script that..."

- [x] missing queries in the content!
- [x] green_keyword detection (which is a query that is has not'd a lot of impressions but it's increasing and we could lead to a good position and it's positions it's not bad! a rising one!)

**Phase 3: AI Content Suggestions**

- LLM-powered title/description improvements using GSC queries
- Missing keyword detection per page
- Heading structure suggestions
- Alt text suggestions from image context
- Content gap analysis (what queries have no matching page?)

**Phase 4: Index Tracking & Monitoring**

- Not-indexed pages with reasons
- Bulk re-index submission
- Status tracking over time

**Phase 5: Cross-Page & Site-Wide Intelligence**

- Topic cluster detection and mapping
- Internal linking suggestions
- Duplicate/cannibalization resolution recommendations
- Structured data validation
- E-E-A-T signal checks (author info, sources cited)

## Markting helping and trendy

1. Create MCP tool
2. Create Agent Skill feature

## Visualize and General Dashbaord

Country/device breakdown — you already have get_analytics_by(dimension, value), so this is mostly about building a summary view on top of it
Does this breakdown work for you?

## Insights

1. Implement all the insights.canvas features and the must_ai_features also

## Quarto Specific

1. Gneral quarto specifc rules in the frontmatters  like include or exclude code cells especailly in readin .ipynb
2. Quarto has slug: frontmatter option that control the output URL.
