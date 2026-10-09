import importlib.util
import tempfile
import unittest
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent


class PromoTests(unittest.TestCase):
    def test_existing_cover_gets_separate_banner_with_local_assets(self):
        spec = importlib.util.spec_from_file_location("render_promo", ROOT / "render_promo.py")
        assert spec is not None and spec.loader is not None and spec.origin is not None
        self.assertTrue(Path(spec.origin).is_file(), "Promo renderer is missing")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "cover with space.png"
            Image.new("RGB", (1280, 720), "navy").save(source)
            preview = Path(folder) / "nested/promo.html"
            document, dimensions = module.build_html(source, preview)
            self.assertEqual(dimensions, (1280, 840))
            self.assertIn('src="../cover%20with%20space.png"', document)
            self.assertIn("link w komentarzu", document)
            self.assertIn("👇", document)
            self.assertIn("#f9fa30", document)
            self.assertIn("NotoColorEmoji.ttf", document)
            self.assertNotIn("data:", document)
            self.assertNotIn("https://", document)
            self.assertIn("height: 720px", document)
            self.assertIn("height: 120px", document)

    def test_empty_or_multiline_cta_is_rejected(self):
        from render_promo import build_html
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "cover.png"
            Image.new("RGB", (1280, 720)).save(source)
            for text in ("", "   ", "link\nw komentarzu", None):
                with self.subTest(text=text), self.assertRaises(ValueError):
                    build_html(source, Path(folder) / "promo.html", text)

    def test_custom_cta_is_literal_and_html_escaped(self):
        from render_promo import build_html
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "cover.png"
            Image.new("RGB", (1280, 720)).save(source)
            document, _ = build_html(source, Path(folder) / "promo.html", "Kliknij  <link> & zobacz 🚀")
            self.assertIn("Kliknij  &lt;link&gt; &amp; zobacz", document)
            self.assertNotIn("<link>", document)
            self.assertIn('<span class="emoji">🚀</span>', document)

    def test_render_preserves_cover_pixels_and_rejects_overwrite(self):
        import render_promo
        self.assertTrue(hasattr(render_promo, "render"), "Browser rendering is missing")
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "cover.png"
            output = Path(folder) / "promo.png"
            Image.new("RGB", (1280, 720), "navy").save(source)
            render_promo.render(source, output)
            with Image.open(output) as result, Image.open(source) as original:
                self.assertEqual(result.size, (1280, 840))
                self.assertEqual(result.crop((0, 0, 1280, 720)).convert("RGB").tobytes(), original.tobytes())
            with self.assertRaises(FileExistsError):
                render_promo.render(source, output)


if __name__ == "__main__":
    unittest.main()
