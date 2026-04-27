---
name: youtube-shorts
description: 'Generate dynamic YouTube Shorts scripts and metadata based on our Better Dev Club channel strategy. Use when the user asks for a youtube short, scripts for shorts, news-jacking, or short video ideas based on tech news.'
---

# YouTube Shorts Generator for Better Dev Club

This skill orchestrates the creation of YouTube Shorts scripts using the channel's growth strategy (`grow/YOUTUBE_STRATEGY.md`) and previous conversational patterns. It ensures every YouTube Short is perfectly tuned to the channel's style, targeting retention, controversy, and algorithm discovery.

## When to use
- When the user asks you to create a "YouTube Short" script based on an article, URL, or tech news.
- When the user asks you to act as their "YouTube Growth Hacker".
- When creating a promotional script for an episode or a "news-jacking" short.

## Core Rules & Checklists
1. **Analyze the source:** Read the provided URL or text to extract the main tech news.
2. **Link to previous episodes:** Always search `episodes.json` or `transcriptions/*.json` for related topics and mention them to build a Shorts-to-Full-Episode Funnel. 
3. **Pacing and Structure:** The script should be ~45 seconds long and divided into blocks:
    - **[0:00 - 0:08] HOOK:** Controversial, shocking, or surprising fast opening. NEVER say "Hi" or introduce the speakers. Do not ask users to check the description or links here - it kills watch time.
    - *(Wskazówka montażowa / Editing hint)*: Quick visual/meme prompt.
    - **[0:08 - 0:28] MIĘSO (The Meat):** Fast-paced tech info. Focus on conflict, cost, security, or dramatic changes.
    - **[0:28 - 0:35] KONTROWERSJA / TŁO (Controversy / Context):** Elevate the stakes.
    - **[0:35 - 0:45] CTA i PYTANIE (Call to action):** Ask a definitive question to farm comments, and tell them to subscribe. Links to sources are mentioned here or displayed as text at the very end.
4. **Metadata (Description & Tags):**
    - Generate a clickbaity description with relevant links.
    - Create a Pinned Comment template that asks an engaging question.
    - Provide 10-15 exact hashtags combining narrow topics and broad topics (e.g. `#ai`, `#it`, `#programowanie`, `#podcastit`, `#betterdevclub`).
5. **Titles:** Propose 3 title options. Use the viral formula `[Chwytliwy Krótki Tytuł] w #[Narzędzie] #[InneNarzędzie] #betterdevclub #shorts` if appropriate.

## Procedure
1. If the user provides a URL or topic, use tools (`fetch_webpage`, `read_file`, `grep_search`) to grab context from the internet and from `episodes.json` about related episodes.
2. Draft the script utilizing the 4-part structure outlined above.
3. Keep the tone natural, dynamic, and highly pragmatic—you are talking to experienced IT professionals.
4. Output the 3 Title options, the Script, and the Metadata checklist.
