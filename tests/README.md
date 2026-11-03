# Browser regression tests

Use Python 3.10+ and Playwright in a virtual environment:

```sh
python3 -m venv .venv
.venv/bin/pip install playwright
.venv/bin/playwright install chromium
python3 tools/build_ssr.py
.venv/bin/python -m unittest discover -s tests -v
```

Tests start an isolated local HTTP server on an available port. They verify archive card containment at desktop/tablet/mobile widths, search, sticky search placement, episode navigation, and the homepage archive link. The existing page loads React, Babel, Tailwind and fonts from CDNs, so tests require network access.
