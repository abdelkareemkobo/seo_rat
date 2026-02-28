
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
