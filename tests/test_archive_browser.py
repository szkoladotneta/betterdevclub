"""Browser regression checks. Run: python3 -m unittest discover -s tests -v"""
import functools
import http.server
from pathlib import Path
import threading
import unittest
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]

class SiteHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split('?')[0]
        if path.rstrip('/') == '/episodes':
            self.path = '/episodes/index.html'
        elif path.startswith('/episodes/episode-') and not path.endswith('.html'):
            self.path = path + '.html'
        super().do_GET()

    def log_message(self, format, *args):
        pass

class ArchiveBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(SiteHandler, directory=str(ROOT)))
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()
        cls.base = f'http://127.0.0.1:{cls.server.server_port}'
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=True)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()
        cls.server.shutdown()
        cls.server.server_close()

    def test_homepage_has_visible_archive_link(self):
        page = self.browser.new_page(viewport={'width': 375, 'height': 900})
        try:
            page.goto(self.base)
            page.wait_for_selector('main')
            link = page.get_by_role('link', name='Zobacz wszystkie odcinki', exact=True)
            self.assertEqual(link.count(), 1)
            self.assertTrue(link.is_visible())
            link.click()
            page.wait_for_selector('input[placeholder^="Grepuj"]')
            self.assertEqual(page.url.rstrip('/'), self.base + '/episodes')
        finally:
            page.close()

    def test_archive_search_and_episode_navigation(self):
        page = self.browser.new_page(viewport={'width': 1280, 'height': 900})
        try:
            page.goto(self.base + '/episodes')
            search = page.locator('input[placeholder^="Grepuj"]')
            search.wait_for()
            page.evaluate('window.scrollTo(0, 500)')
            page.wait_for_timeout(300)
            search_box = search.bounding_box()
            header_box = page.locator('header').bounding_box()
            assert search_box is not None and header_box is not None
            self.assertGreaterEqual(search_box['y'], header_box['height'])
            search.fill('30 tys. zmian dziennie')
            page.wait_for_function("document.querySelectorAll('h3').length === 1")
            self.assertIn('Gita', page.locator('h3').inner_text())
            page.get_by_role('button', name='Odsłuchaj', exact=True).click()
            page.wait_for_url('**/episodes/episode-43')
            page.wait_for_selector('iframe[src*="pabtWyquq6Y"]')
        finally:
            page.close()

    def test_archive_content_stays_inside_cards(self):
        page = self.browser.new_page()
        try:
            for width in (1280, 768, 375):
                with self.subTest(width=width):
                    page.set_viewport_size({'width': width, 'height': 900})
                    page.goto(self.base + '/episodes')
                    page.wait_for_selector('input[placeholder^="Grepuj"]')
                    page.wait_for_function("document.querySelectorAll('h3').length === 44")
                    page.wait_for_timeout(500)
                    metrics = page.evaluate('''() => ({
                        viewport: document.documentElement.clientWidth,
                        width: document.documentElement.scrollWidth,
                        overflowingCards: [...document.querySelectorAll('h3')].filter(h => {
                            const card = h.closest('.group');
                            const rect = card.getBoundingClientRect();
                            return [...card.querySelectorAll('*')].some(e => {
                                const r = e.getBoundingClientRect();
                                return r.width > 0 && (r.right > rect.right + 1 || r.left < rect.left - 1);
                            });
                        }).length
                    })''')
                    self.assertLessEqual(metrics['width'], metrics['viewport'] + 1, metrics)
                    self.assertEqual(metrics['overflowingCards'], 0, metrics)
        finally:
            page.close()
