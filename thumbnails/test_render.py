import json
import re
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

from render import ROOT, asset, build_html
from render_combinations import LINES, build_variants


class PortraitParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.people = []

    def handle_starttag(self, tag, attributes):
        values = dict(attributes)
        if tag == "div" and values.get("class") == "person":
            self.people.append(values)


class RenderTests(unittest.TestCase):
    def setUp(self):
        self.config = json.loads((ROOT / "episodes/demo.json").read_text())

    def test_all_portraits_align_heads_independently_of_width(self):
        portraits = json.loads((ROOT / "assets/people/portraits.json").read_text())
        for portrait in portraits:
            for side in ("left", "right"):
                with self.subTest(portrait=portrait, side=side):
                    config = {**self.config, "people": {**self.config["people"], side: portrait}}
                    parser = PortraitParser()
                    parser.feed(build_html(config))
                    for person in parser.people:
                        style = dict(
                            declaration.split(":", 1)
                            for declaration in person["style"].split(";")
                            if declaration
                        )
                        top = float(style["top"].removesuffix("px"))
                        scale = float(person["data-scale"])
                        head = float(person["data-head-top"])
                        self.assertAlmostEqual(top + head * scale, config["headTop"])

    def test_preview_links_shared_assets_and_escapes_text(self):
        self.config["lines"] = [{"text": "<script>alert(1)</script>", "color": "text"}]
        document = build_html(self.config)
        self.assertIn("&lt;script&gt;", document)
        self.assertNotIn("<script>", document)
        self.assertIn("../assets/fonts/NotoColorEmoji.ttf", document)
        self.assertIn("../assets/people/ready/", document)
        self.assertNotIn("data:", document)
        self.assertLess(len(document.encode("utf-8")), 10_000)
        self.assertNotIn("https://", document)

    def test_nested_output_resolves_every_shared_asset(self):
        preview = ROOT / "output/layouts/nested/example.html"
        document = build_html(self.config, preview)
        references = [
            reference
            for reference in re.findall(r'(?:src="|url\(")([^"]+)', document)
            if not reference.startswith("#")
        ]
        self.assertEqual(len(references), 7)
        for reference in references:
            with self.subTest(reference=reference):
                self.assertTrue((preview.parent / unquote(reference)).resolve().is_file())

    def test_asset_names_are_encoded_and_missing_assets_are_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "asset with space.png"
            path.write_bytes(b"test")
            preview = Path(folder) / "example.html"
            self.assertEqual(asset(path, preview), "asset%20with%20space.png")
            with self.assertRaises(FileNotFoundError):
                asset(Path(folder) / "missing.png", preview)

    def test_invalid_input_is_rejected(self):
        for field, value in (
            ("episode", True),
            ("episode", 1.5),
            ("fontSize", float("nan")),
            ("grayscale", "yes"),
            ("lines", []),
            ("people", {"left": "missing", "right": "missing"}),
        ):
            with self.subTest(field=field):
                with self.assertRaises(ValueError):
                    build_html({**self.config, field: value})

    def test_split_title_preserves_line_order_and_gap(self):
        self.config["lines"][0]["gapAfter"] = 140
        document = build_html(self.config)
        self.assertIn("margin-bottom:140.0px", document)
        self.assertLess(document.index("TWÓJ"), document.index("TYTUŁ"))
        self.assertLess(document.index("TYTUŁ"), document.index("ODCINKA"))

    def test_invalid_title_gap_is_rejected(self):
        for value in (-1, 361, True, "140"):
            with self.subTest(value=value):
                self.config["lines"][0]["gapAfter"] = value
                with self.assertRaises(ValueError):
                    build_html(self.config)

    def test_emoji_sequences_are_kept_together(self):
        self.config["lines"] = [{"text": "Kod  2 DNI ⚡ / 42 tyg. 🤦‍♂️ 🚀 🤖 🔥", "color": "text"}]
        document = build_html(self.config)
        self.assertIn('<span class="emoji">⚡</span>', document)
        self.assertIn('<span class="emoji">🤦‍♂️</span>', document)
        self.assertIn("Noto Color Emoji", document)
        for emoji in ("🚀", "🤖", "🔥"):
            self.assertIn(f'<span class="emoji">{emoji}</span>', document)

    def test_all_combinations_preserve_requested_text(self):
        portraits = json.loads((ROOT / "assets/people/portraits.json").read_text())
        piotreks = [key for key in portraits if key.startswith("piotrek-")]
        kajetans = [key for key in portraits if key.startswith("kajetan-")]
        expected = {
            arrangement
            for piotrek in piotreks
            for kajetan in kajetans
            for arrangement in ((piotrek, kajetan), (kajetan, piotrek))
        }
        variants = build_variants(portraits)
        self.assertEqual(len(variants), len(expected))
        self.assertEqual(len({name for name, _ in variants}), len(expected))
        arrangements = {
            (config["people"]["left"], config["people"]["right"])
            for _, config in variants
        }
        self.assertEqual(arrangements, expected)
        self.assertEqual(
            sum(config["layout"] != "compact" for _, config in variants),
            sum(
                portraits[left].get("extendsIntoTitle", False)
                or portraits[right].get("extendsIntoTitle", False)
                for left, right in expected
            ),
        )
        for _, config in variants:
            self.assertEqual(
                [line["text"] for line in config["lines"]],
                [line["text"] for line in LINES],
            )
            self.assertIn(config["fontSize"], (72, 88))
        self.assertNotIn("gapAfter", LINES[1])

    def test_gesture_layouts_mirror_text_and_head_positions(self):
        portraits = json.loads((ROOT / "assets/people/portraits.json").read_text())
        variants = dict(build_variants(portraits))
        left = variants["piotrek-03_kajetan-01_piotrek-left"]
        right = variants["piotrek-03_kajetan-01_piotrek-right"]
        self.assertEqual(left["layout"], "pointing")
        self.assertEqual(right["layout"], "pointing")
        self.assertEqual(left["titleCenterX"] + right["titleCenterX"], 1280)
        self.assertEqual(left["lines"][0]["offsetX"], -right["lines"][0]["offsetX"])
        self.assertEqual(left["headCenters"]["left"] + right["headCenters"]["right"], 1280)
        for name, config in variants.items():
            if config["people"]["left"] == "piotrek-02-lewo":
                self.assertEqual(config["layout"], "palm", name)
                self.assertEqual(config["headCenters"]["left"], 120)
            if config["people"]["right"] == "piotrek-02-lewo":
                self.assertEqual(config["layout"], "palm", name)
                self.assertEqual(config["headCenters"]["right"], 1160)

    def test_combinations_use_requested_episode_and_text(self):
        portraits = json.loads((ROOT / "assets/people/portraits.json").read_text())
        content = {
            "episode": 41,
            "grayscale": False,
            "lines": [
                {"text": "INNY TYTUŁ", "color": "text"},
                {"text": "NOWE EMOJI 🚀", "color": "primary"},
                {"text": "NIE DEMO", "color": "highlight"},
            ],
        }
        for _, config in build_variants(portraits, content):
            self.assertEqual(config["episode"], 41)
            self.assertFalse(config["grayscale"])
            self.assertEqual(
                [(line["text"], line["color"]) for line in config["lines"]],
                [(line["text"], line["color"]) for line in content["lines"]],
            )
            self.assertNotIn("gapAfter", config["lines"][-1])
        self.assertNotIn("gapAfter", content["lines"][1])

    def test_invalid_combination_content_is_rejected(self):
        portraits = json.loads((ROOT / "assets/people/portraits.json").read_text())
        for content in ({}, [], {"episode": 41, "lines": []}, {"episode": 41, "lines": [{}]}):
            with self.subTest(content=content):
                with self.assertRaises(ValueError):
                    build_variants(portraits, content)

    def test_six_line_episode_preserves_text_and_spacing(self):
        content = json.loads((ROOT / "episodes/036.json").read_text())
        document = build_html(content)
        self.assertIn("CO     SIĘ", document)
        self.assertIn("A.I.  &amp;  DEV", document)
        self.assertIn('<span class="emoji">🤯</span>', document)
        self.assertIn("white-space: pre", document)
        portraits = json.loads((ROOT / "assets/people/portraits.json").read_text())
        for _, config in build_variants(portraits, content):
            self.assertEqual(len(config["lines"]), 6)
            self.assertEqual(
                [line["text"] for line in config["lines"]],
                [line["text"] for line in content["lines"]],
            )

    def test_seven_lines_are_rejected(self):
        content = {**self.config, "lines": [{"text": "TEST"} for _ in range(7)]}
        with self.assertRaises(ValueError):
            build_html(content)
        portraits = json.loads((ROOT / "assets/people/portraits.json").read_text())
        with self.assertRaises(ValueError):
            build_variants(portraits, content)

    def test_individual_layout_controls_are_rendered(self):
        config = json.loads((ROOT / "episodes/layout-pointing.json").read_text())
        document = build_html(config)
        self.assertIn("left: 290.0px", document)
        self.assertIn("width: 620.0px", document)
        self.assertIn("font-size:96.0px", document)
        self.assertIn("translateX(80.0px)", document)
        parser = PortraitParser()
        parser.feed(document)
        for person in parser.people:
            style = dict(
                declaration.split(":", 1)
                for declaration in person["style"].split(";")
                if declaration
            )
            top = float(style["top"].removesuffix("px"))
            self.assertAlmostEqual(
                top + float(person["data-head-top"]) * float(person["data-scale"]),
                config["headTop"],
            )

    def test_invalid_layout_controls_are_rejected(self):
        for field, value in (
            ("titleCenterX", 100),
            ("titleWidth", 1200),
            ("headCenters", []),
            ("headCenters", {"middle": 640}),
            ("lines", [{"text": "SDLC", "offsetX": 251}]),
            ("lines", [{"text": "SDLC", "fontSize": True}]),
        ):
            with self.subTest(field=field, value=value):
                with self.assertRaises(ValueError):
                    build_html({**self.config, field: value})


if __name__ == "__main__":
    unittest.main()
