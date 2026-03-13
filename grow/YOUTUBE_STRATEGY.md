# Better Dev Club - YouTube Growth Strategy

**Created:** 2026-03-13
**Channel:** Better Dev Club (287 subscribers, 19 episodes)
**Hosts:** Piotr Stapp & Kajetan Duszynski (Microsoft MVPs)
**Goal:** Grow the channel & build a community

---

## Current State (March 2026)

- 287 subscribers over ~4.5 months (~64 subs/month average)
- 19 full episodes + ~16 Shorts published
- Weekly publishing schedule (fixed)
- Shorts published 3 days after each episode release
- Average viewer watches ~25% of each episode (improving to 34-39% on recent eps)
- CTR improving consistently: 3.0% (early eps) -> 7.3% (Ep #19)
- Impressions inconsistent: YouTube not recommending consistently yet

### Top Performers (Full Episodes)

| Episode | Views | CTR | Impressions | Watch hrs | Subs |
|---------|-------|-----|-------------|-----------|------|
| #11 Tailwind/StackOverflow | 1,606 | 2.14% | 44,026 | 147.8h | 59 |
| #16 Claude vs Cursor ($3M) | 1,060 | 4.44% | 14,850 | 112.5h | 21 |
| #10 AI Predictions 2026 | 696 | 2.88% | 13,711 | 70.8h | 24 |
| #17 Tomek Ducin (guest) | 336 | 5.99% | 2,336 | 73.3h | 11 |
| #19 Amazon/Spotify/Claude | 256 | 7.27% | 2,297 | 38.5h | 2 |

### Key Insight

Ep #11 was an unexplained outlier (44K impressions vs typical 1.4-14K). Growth hasn't "stopped" -- it's normalizing after that spike. Fundamentals (CTR, retention) are improving.

---

## Weekly Dashboard (Check Every Monday, 5 min)

### 1. Impressions vs CTR Trend
- YouTube Studio > Analytics > Reach tab
- Impressions UP + CTR DOWN = algorithm testing wider audience (good)
- Impressions DOWN + CTR same = algorithm stopped recommending (fix retention)
- Impressions UP + CTR UP = breaking through

### 2. Retention Graphs (Per New Episode)
- Studio > Content > Click video > Analytics > Engagement
- Find the "cliff" -- where the biggest drop happens
- First 30 seconds = hook problem
- Mid-point drop = middle section drags
- Compare across episodes to find patterns

### 3. Traffic Source Split
- Studio > Analytics > Reach > Traffic Source Types
- Goal: "Browse Features" and "Suggested Videos" growing (= algorithm recommending you)
- If mostly "External" or "Direct" = only shared audiences watching

### 4. Returning vs New Viewers
- Studio > Analytics > Audience tab
- Returning viewers growing = loyal community forming (goal #1)
- New viewers spiking = video getting discovered

### 5. Shorts-to-Full-Episode Funnel
- Studio > Analytics > Content > Compare Shorts vs Long-form
- Goal: viewers who watch Shorts should also watch full episodes

---

## Action Plan

### PRIORITY 1: Improve Retention (The Algorithm Fix)

- [ ] **Hook the first 30 seconds:** Start every episode with the most controversial/surprising statement -- NOT "Czesc, witamy w Better Dev Club." Do the intro after the hook.
- [ ] **Tease what's coming:** At the 2-3 minute mark, preview what's later: "Za chwile pokazermy ile kosztuje jeden PR od Claude'a, ale najpierw..."
- [ ] **Add chapters to ALL episodes:** Chapters let viewers jump to topics, preventing full drop-offs. Use `tools/make_chapters.py` or generate manually from Riverside transcripts.

### PRIORITY 2: Maximize Discovery (Impressions)

- [ ] **Add YouTube tags to Ep #01-#18:** Only #19 currently has tags. Add 10-15 relevant tags per video (e.g., "podcast IT", "AI programowanie", "claude code", "vibe coding").
- [ ] **Ride trending topics fast:** Best episodes (#11, #16) coincided with trending topics. Monitor HN/Reddit/X. Consider Shorts-first reactions within 24 hours of breaking news.
- [ ] **Title formula -- lead with hook, not episode number:**
  - BAD: `Better Dev Club #18 - Claude na wojnie`
  - GOOD: `Trump banuje Claude? Akcje IBM spadaja o 20%`
- [ ] **Add tail keywords to titles:** e.g., `| AI w IT 2026` or `| Podcast IT`

### PRIORITY 3: Convert Viewers to Subscribers

- [ ] **Shorts CTA every time:** Last 3 seconds on-screen text: "Subscribe for weekly AI/IT breakdowns." Verbal mention of full episode. Pin a comment linking to the full episode.
- [ ] **Ask a specific question in every episode:** "Co myslicie -- czy Claude Code za 25$ to hit? Napiszcie w komentarzach." Specific > generic.
- [ ] **Pin a comment on every video:** Include a discussion question, link to next/previous episode, link to newsletter.
- [ ] **Add end screens (last 20s):** Point to most recent episode, best episode (#11), and subscribe button.
- [ ] **Add cards (mid-video pop-ups):** When referencing another episode, add a card linking to it.

### PRIORITY 4: Guest Episodes (Biggest Growth Lever)

- [ ] **Aim for 1 guest per month** with their own following (LinkedIn, X, conference speakers).
- [ ] **Guest promo playbook:**
  - Before release: teaser Short (15s) tagging the guest
  - Release day: both you AND guest share on LinkedIn/X (ask explicitly)
  - After release: 3-4 Shorts from best moments, spaced 2-3 days apart
- [ ] **Ep #17 (Ducin) proof:** Best CTR (5.99%), best watch time ratio, highest engagement. Guests work.

### PRIORITY 5: Consistent Cross-Promotion

For EVERY episode, post on ALL platforms (not "depends on episode"):
- [ ] LinkedIn (both Piotr AND Kajetan personal profiles)
- [ ] X/Twitter
- [ ] Facebook dev groups
- [ ] Newsletter

The post should share one controversial take as a hook, not just "new episode out."

### PRIORITY 6: Channel Polish

- [ ] **Create playlists by topic:** "AI w IT", "Narzedzia i IDE", "Goscie Better Dev Club", "Shorts - Najlepsze Momenty"
- [ ] **Use Community tab:** Post polls, behind-the-scenes, episode teasers 1-2 days before release.
- [ ] **Consider a "Best Of" compilation:** 10-15 min video of top moments as a channel "trailer" for new viewers.
- [ ] **Consider a Discord server** for community building (even 20 active members = strong loyalty signal for YouTube).

---

## Backfill Checklist (Old Episodes)

Priority order for adding chapters + tags:

- [ ] Ep #11 - Drama w Tailwindzie (1,606 views, still #1)
- [ ] Ep #16 - Claude vs Cursor $3M (1,060 views)
- [ ] Ep #10 - AI Predictions 2026 (696 views)
- [ ] Ep #17 - Tomek Ducin guest (336 views, best engagement)
- [ ] Ep #15 - Skills.md (439 views)
- [ ] Ep #13 - Linus Torvalds/DHH (375 views)
- [ ] Remaining episodes #01-#09, #12, #14

---

## YouTube Description Template

```
[2-3 sentence hook with the most controversial/interesting topic]

Wszystkie linki: [episode URL]
Zapisz sie na newsletter: https://betterdevclub.pl/newsletter

[2-3 sentence expansion of what the episode covers]

Agenda:
00:00 - Wstep
[chapters here]

O nas:
Piotr Stapp i Kajetan Duszynski. Jestesmy Microsoft MVP i w tym
podcascie gadamy o tym, jak AI i nowe narzedzia wplywaja na nasza
codzienna robote w IT.

#tag1, #tag2, #tag3, #betterdevclub
```

---

## Key Milestones to Track

| Milestone | Current | Target Date | Strategy |
|-----------|---------|-------------|----------|
| 500 subscribers | 287 | ~June 2026 | Guest episodes + Shorts CTAs |
| 1,000 subscribers | 287 | ~Aug-Sep 2026 | Consistent growth + 1 viral topic |
| 40%+ avg retention | ~25-35% | Ongoing | Better hooks, chapters, tighter editing |
| YouTube monetization (1K subs + 4K watch hrs) | 287 subs / 725 watch hrs | ~Oct 2026 | Keep publishing weekly |

---

## Tools Available

| Script | Location | Purpose |
|--------|----------|---------|
| YouTube Stats Fetcher | `tools/get_youtube_stats.py` | Downloads views, likes, comments, tags for all episodes |
| Chapter Generator | `tools/make_chapters.py` | Generates YouTube chapters from transcription JSON files |
| API Key | `tools/youtube.env` | YouTube Data API key (keep secret, do not commit) |
| Transcriptions | `transcriptions/*.json` | All episode transcripts with timestamps |

---

*Strategy last updated: 2026-03-13*
