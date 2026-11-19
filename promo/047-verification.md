# Episode 47 — verification

- Exact Riverside title and clip selected: `Better Dev Club #47 - final`, `6afeeb177b03e227ce7bbefa`; RSTL revision 21 from `/api/v4/clip/{id}`.
- `ffprobe`: final MP4 duration `2728.092993` seconds. RSTL minus synced cuts: `2728.0986666666663` seconds, delta `0.005673666666098143` seconds.
- Composed transcription JSON returned 404; session ASR fallback is explicit. No claim of audio-verified subtitles or cut boundaries.
- Validated: existing 46 episode records unchanged, unique episode IDs, new entry `notPublished: true`, all platform URLs and YouTube ID empty, chapters ordered and within runtime, nonempty transcript, raw ASR copied byte-for-byte, SSR title present.
- Checked raw ASR and mapping audit for URLs/password/token/secret strings: none found. Private signed media URLs and full Riverside clip data are excluded from the repo.
- `python3 tools/build_ssr.py`: PASS, including episode 47 and regenerated archive/data versions.
- `git diff --check`: PASS before commit.
- Unmodified `python3 -m unittest discover -s tests -v`: two tests passed; the card-layout test timed out at all three widths because it hard-codes **44** cards while the current React archive has **46** published episodes. This is a stale test expectation, not a fully green unmodified suite.
- Re-executed the same three tests with only the stale expectation replaced **in memory**, `44 -> 46`, deriving the number from `episodes.json`: **3 tests passed**, including layout at 1280/768/375 px. No repository test/code changes.
- Separate Playwright check: draft title and transcript render, no JS page errors; React archive hides episode 47 and displays 46 published cards.
- Known existing privacy limitation verified: direct draft route renders and says “Opublikowano”; generated static archive includes the draft. Keep this PR unmerged until editorial approval, regardless of `notPublished`.

## Human approval still required

- Listen to chapter and Shorts boundaries, ambiguous model/person names, CPU/cache phrase and C#/Rust joke.
- Verify/supply sources or add a correction for Microsoft headcount/layoff claims and the opening IPO/release claims.
- Confirm date (2026-11-19 is provisional), title, platform IDs/links and actual publication decision.
