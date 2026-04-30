---
name: blog-post
description: Generate Hugo blog post for Arctic Green from informational keyword. Use when user provides a question/how-to keyword like "when to mow st augustine in houston" or invokes /blog-post <keyword>.
---

# /blog-post — Arctic Green Hugo blog generator

Generates an informational blog post targeting a single keyword + cluster. Output goes in `content/blog/<slug>.md`.

## When to invoke

- User: `/blog-post when to mow st augustine in houston`
- User: "write a blog post about brown patch fungus"
- After SEMrush keyword validation, batch-build top 10 informational winners

## Inputs needed

1. Primary keyword (informational intent — how/why/when/what)
2. Optional: keyword cluster (or generate from `.claude/seo/keywords/seed-list.md`)

## Pipeline

1. **Read voice files** (same as `/service-page`):
   - voice.md, humor.md, stats.md, stories.md, opinions.md

2. **Build keyword cluster** (3-7 secondary keywords):
   - Pull from `seed-list.md` if related
   - Or generate via Claude (variations + adjacent topics)
   - Goal: rank for 30-50 secondary keywords per post

3. **Steal-the-SERP** — fetch top 3 ranking informational pages (excl. Reddit/YouTube). Extract:
   - Average word count (informational typically 1000-2000)
   - H2 count + question topics
   - Image count
   - Lists, tables, schema markup

4. **Frontmatter**:
   ```yaml
   ---
   title: "[Hooky title that includes primary keyword]"
   description: "[150-160 chars w/ primary keyword in first 100]"
   date: YYYY-MM-DD
   tags: [extracted from cluster]
   keywords_primary: "[primary]"
   keywords_cluster: ["[secondary 1]", "[secondary 2]", ...]
   image: "/images/blog/<slug>-hero.jpg"
   ---
   ```

5. **Body structure**:
   - **Opening** (50-100 words): primary keyword in first 100, ONE humor moment per humor.md opening rule, set up the question
   - **TL;DR box** (3-4 bullets, the answer up front — Google rewards this for featured snippets)
   - **H2: [Direct answer to the keyword question]** — give the answer, not a preamble
   - **H2: [Why this happens / context]** — explain mechanism
   - **H2: [NW-Houston-specific notes]** — pull from stats.md, soil/grass/season specifics
   - **H2: [What to do — step by step]** — actionable list
   - **H2: [Common mistakes]** — opinions.md hot take fits here
   - **H2: [When to call a pro]** — soft CTA
   - **H2: Frequently asked questions** — 4-6 H3 questions from PAA
   - **Inject ONE story** from stories.md if any matches the topic
   - **CTA block**: phone (903) 658-8244 + service-page link if relevant

6. **On-page SEO checklist**:
   - [ ] Primary keyword in title, H1, first 100 words, meta description, URL slug
   - [ ] Cluster keywords sprinkled naturally (1-2 mentions each)
   - [ ] Exactly 1 H1
   - [ ] 5-8 H2 + 4-8 H3
   - [ ] 5-7 internal links: 2-3 service pages, 1-2 area pages, 1-2 related blog posts
   - [ ] 3-5 external links: Texas A&M AgriLife extension, NOAA weather, EPA, USDA hardiness zones
   - [ ] Alt text on all images, primary keyword in hero image alt
   - [ ] Schema.org Article JSON-LD (Hugo partial)
   - [ ] Reading level: 8th grade max (use simple words)
   - [ ] Mobile-readable: short paragraphs (2-3 sentences each)

7. **Image strategy**:
   - 1 hero (Pexels API or local stock — see Pexels API key when added to `.env`)
   - 2-4 in-body images supporting H2 sections
   - All compressed (Hugo image processing or pre-compress)

## File output

`content/blog/<slug>.md` where slug = primary keyword kebab-cased

## Hugo build check

```bash
cd ~/arctic-green-lawn && hugo --quiet 2>&1 | tail -20
```

## Cadence guard

Jono's ramp: day1=1, day2=1, day3=2, day5=3, day8=4. NEVER 1000/day.

Track in `.claude/seo/published-log.md`. Skill blocks if today's count exceeds ramp.

## Steal-the-SERP rule

If top 3 pages average 1500 words and have 8 H2s, our post should match — not beat by 50%, not undershoot. Match the format Google has already validated.

## Hard rules

- Never trigger phrases from voice.md
- Never fabricate stats — only stats.md values + verifiable external (extension service, NOAA)
- Never paywalled-source-only claims — always cite reachable sources
- Never AI-slop intros ("In today's fast-paced...")
- Always 8th-grade reading level — short sentences, plain words

## Related

- `/service-page` — money keyword zipper pages
- `.claude/seo/voice/` — tone files
- `.claude/seo/keywords/seed-list.md` — keyword bank
