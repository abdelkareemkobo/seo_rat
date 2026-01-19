## Todo

### Analytics Queries Improvement

1. Get top queries other than ones we optimized
   1. what optimized mean?
   2. should we do this in fly or add it into article class ?
   3. how to keep tracke of these are optimzied?
   4. how to filter the analytics function to exclude these queries

### Missing

#### SEO analysis

1. Internal/external link analysis
2. Content length check
3. Readability scores

#### AI Features

1. Keywords Suggetions

2. Better
   1. Heaings, Description , Title
3. Keywords to add
   1. what is missing keywords
   2. how is it's status?
   3. is it already optimized or not?
   4. how to hanlde new days or queries?
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

1. When to use polars?
   1. i found it more easier to write than sqlite?

2. how ahrefs ans semrash get their data
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

## Summary Table

| Expert | Key Insight | Feature for SEO RAT |
|--------|-------------|---------------------|
| Lily Ray | Intent analysis | Classify queries by user intent |
| Glenn Gabe | Trend tracking | Compare date ranges, flag changes |
| Cindy Krum | Topic/entity focus | Semantic keyword suggestions |
| Jono Alderson | UX + structure | Heading hierarchy, internal links |
| Aleyda Solis | Process + priority | Prioritized task checklist |
| Jes Scholz | Measure changes | Before/after tracking |
| Barry Adams | Content type rules | Different checks per content type |
| Kevin Indig | Business context | Priority by business value |
| Crystal Carter | Machine readable | Structured data, complete metadata |
| Marie Haynes | Quality first | E-E-A-T, depth, sources |

---

**Question:** Which of these insights should we prioritize adding to your system first?
