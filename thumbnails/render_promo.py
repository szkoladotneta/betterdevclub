"""Append an HTML/CSS call-to-action banner below an existing episode cover."""

import argparse
import html
import json
from pathlib import Path
from string import Template

from PIL import Image

if __package__:
    from .render import ROOT, EMOJI, asset
else:
    from render import ROOT, EMOJI, asset


DEFAULT_TEXT = "link w komentarzu 👇"


def build_html(cover: Path, preview: Path, text: str = DEFAULT_TEXT) -> tuple[str, tuple[int, int]]:
    if not isinstance(text, str) or not text.strip() or any(char in text for char in "\r\n\t"):
        raise ValueError("Banner text must be a nonempty single line without tabs")
    with Image.open(cover) as image:
        width, height = image.size
    banner_height = round(width * 120 / 1280)
    brand = json.loads((ROOT / "assets/branding/brand.json").read_text())
    content = EMOJI.sub(
        lambda match: f'<span class="emoji">{match.group()}</span>', html.escape(text)
    )
    template = Template((ROOT / "templates/episode-promo.html").read_text())
    document = template.substitute(
        width=width, height=height, banner_height=banner_height,
        padding=width * 40 / 1280, font_size=width * 52 / 1280,
        primary=brand["colors"]["primary"], text=content, cover=asset(cover, preview),
        title_font=asset(ROOT / "assets/fonts/LibreFranklin.ttf", preview),
        emoji_font=asset(ROOT / "assets/fonts/NotoColorEmoji.ttf", preview),
    )
    return document, (width, height + banner_height)


def render(cover: Path, output: Path, text: str = DEFAULT_TEXT, browser_path: str | None = None) -> None:
    import shutil
    from playwright.sync_api import sync_playwright
    if __package__:
        from .file_utils import atomic_write
    else:
        from file_utils import atomic_write

    if output.suffix.lower() != ".png":
        raise ValueError("Output must have a .png extension")
    preview = output.with_suffix(".html")
    if output.exists() or preview.exists() or cover.resolve() in (output.resolve(), preview.resolve()):
        raise FileExistsError("Output already exists or would overwrite the source; choose a new filename")
    document, dimensions = build_html(cover, preview, text)
    output.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(preview, document.encode("utf-8"))
    executable = browser_path or shutil.which("google-chrome") or shutil.which("chromium")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=executable, headless=True)
        try:
            page = browser.new_page(viewport={"width": dimensions[0], "height": dimensions[1]}, device_scale_factor=1)
            page.goto(preview.resolve().as_uri())
            page.evaluate("""async () => {
                await document.fonts.ready;
                await Promise.all([...document.images].map(image => image.decode()));
                if (!document.fonts.check('900 52px "Libre Franklin"') ||
                    !document.fonts.check('400 52px "Noto Color Emoji"', '👇')) {
                    throw new Error("Required fonts did not load");
                }
                const cta = document.querySelector('.cta').getBoundingClientRect();
                const banner = document.querySelector('.banner').getBoundingClientRect();
                if (cta.left < banner.left + 20 || cta.right > banner.right - 20 ||
                    cta.top < banner.top || cta.bottom > banner.bottom) {
                    throw new Error("Banner text overflows; use a shorter text");
                }
            }""")
            image = page.locator(".promo").screenshot()
            import io
            with Image.open(io.BytesIO(image)) as result:
                if result.size != dimensions:
                    raise ValueError(f"Unexpected output dimensions: {result.size}")
            atomic_write(output, image)
        finally:
            browser.close()
    print(f"PNG: {output}\nHTML: {preview}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cover", type=Path, help="Existing, published episode cover (never a recreated thumbnail)")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--text", default=DEFAULT_TEXT)
    parser.add_argument("--browser", help="Path to local Chrome or Chromium")
    args = parser.parse_args()
    render(args.cover, args.output, args.text, args.browser)


if __name__ == "__main__":
    main()
