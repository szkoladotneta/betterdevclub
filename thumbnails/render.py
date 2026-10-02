"""Render a lightweight HTML preview and a 1280 x 720 thumbnail PNG."""

import argparse
import html
import io
import json
import math
import os
import re
import shutil
from pathlib import Path
from string import Template
from urllib.parse import quote

from PIL import Image
from playwright.sync_api import Browser, sync_playwright

if __package__:
    from .file_utils import atomic_write
else:
    from file_utils import atomic_write


ROOT = Path(__file__).resolve().parent
REPOSITORY = ROOT.parent
MAX_TITLE_LINES = 6
EMOJI = re.compile(
    r"[\U0001F300-\U0001FAFF\u2600-\u27BF]"
    r"(?:[\uFE0F\U0001F3FB-\U0001F3FF]|\u200D[\U0001F300-\U0001FAFF\u2600-\u27BF])*"
)


def number(value: object, name: str, minimum: float, maximum: float) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(value)
        or not minimum <= value <= maximum
    ):
        raise ValueError(f"{name} must be a number between {minimum} and {maximum}")
    return float(value)


def asset(path: Path, preview: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"Required thumbnail asset is missing: {path}")
    relative = os.path.relpath(path.resolve(), preview.parent.resolve())
    return quote(relative.replace(os.sep, "/"), safe="/")


def logo_asset(path: Path, preview: Path) -> str:
    with Image.open(path) as original:
        image = original.convert("RGBA")
        bounds = image.getchannel("A").getbbox()
        if bounds is None:
            raise ValueError(f"Logo contains no visible pixels: {path}")
        image = image.crop(bounds)
        output = io.BytesIO()
        image.save(output, format="PNG")
    shared_logo = ROOT / "output/assets/logo-cropped.png"
    shared_logo.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(shared_logo, output.getvalue())
    return asset(shared_logo, preview)


def build_html(config: dict, preview: Path | None = None) -> str:
    preview = preview or ROOT / "output/demo.html"
    brand = json.loads((ROOT / "assets/branding/brand.json").read_text())
    portraits = json.loads((ROOT / "assets/people/portraits.json").read_text())
    colors = brand["colors"]
    for name, color in colors.items():
        if not isinstance(color, str) or not re.fullmatch(r"#[0-9a-fA-F]{6}", color):
            raise ValueError(f"Invalid brand color: {name}")
    episode = number(config.get("episode"), "episode", 1, 9999)
    if not episode.is_integer():
        raise ValueError("episode must be an integer")
    font_size = number(
        config.get("fontSize", brand["title"]["fontSizeMax"]), "fontSize", 24, 160
    )
    head_top = number(config.get("headTop", 170), "headTop", 0, 500)
    eye_offset = number(config.get("eyeOffset", 110), "eyeOffset", 40, 200)
    title_top = number(config.get("titleTop", 260), "titleTop", 40, 600)
    title_center = number(config.get("titleCenterX", 640), "titleCenterX", 100, 1180)
    title_width = number(config.get("titleWidth", 552), "titleWidth", 200, 1000)
    if title_center - title_width / 2 < 0 or title_center + title_width / 2 > 1280:
        raise ValueError("Title area extends outside the cover")
    head_centers = config.get("headCenters", {})
    if not isinstance(head_centers, dict) or set(head_centers) - {"left", "right"}:
        raise ValueError("headCenters may contain only left and right")
    grayscale = config.get("grayscale", True)
    if not isinstance(grayscale, bool):
        raise ValueError("grayscale must be true or false")
    if not isinstance(config.get("people"), dict) or set(config["people"]) != {"left", "right"}:
        raise ValueError("people must contain exactly left and right portrait IDs")

    people = []
    for side, target_x in (("left", 160), ("right", 1120)):
        target_x = number(head_centers.get(side, target_x), f"{side} headCenter", 40, 1240)
        portrait_id = config["people"][side]
        if not isinstance(portrait_id, str) or portrait_id not in portraits:
            raise ValueError(f"Unknown portrait ID for {side}: {portrait_id}")
        metadata = portraits[portrait_id]
        image_path = ROOT / "assets/people/ready" / f"{portrait_id}.png"
        with Image.open(image_path) as image:
            width, height = image.size
        top = number(metadata["headTop"], "portrait headTop", 0, height - 1)
        center = number(metadata["headCenterX"], "portrait headCenterX", 0, width)
        eyes = number(metadata["eyeY"], "portrait eyeY", top + 1, height)
        scale = eye_offset / (eyes - top)
        flip = metadata["side"] != side
        rendered_center = width - center if flip else center
        x = target_x - rendered_center * scale
        y = head_top - top * scale
        people.append(
            f'<div class="person" data-side="{side}" data-head-top="{top}" '
            f'data-scale="{scale}" style="left:{x}px;top:{y}px;'
            f'width:{width * scale}px;height:{height * scale}px">'
            f'<img class="person-image" style="transform:scaleX({-1 if flip else 1})" '
            f'src="{asset(image_path, preview)}" alt="{html.escape(portrait_id)}">'
            "</div>"
        )

    lines = config.get("lines")
    if not isinstance(lines, list) or not 1 <= len(lines) <= MAX_TITLE_LINES:
        raise ValueError(f"lines must contain between one and {MAX_TITLE_LINES} text lines")
    rendered_lines = []
    for line in lines:
        if not isinstance(line, dict) or not isinstance(line.get("text"), str) or not line["text"].strip():
            raise ValueError("Each title line must contain nonempty text")
        color = line.get("color", "primary")
        if not isinstance(color, str) or color not in colors:
            raise ValueError(f"Unknown title color: {color}")
        gap = number(line.get("gapAfter", 0), "line gapAfter", 0, 360)
        line_size = number(line.get("fontSize", font_size), "line fontSize", 24, 160)
        offset = number(line.get("offsetX", 0), "line offsetX", -250, 250)
        text = EMOJI.sub(
            lambda match: f'<span class="emoji">{match.group()}</span>',
            html.escape(line["text"]),
        )
        rendered_lines.append(
            f'<span class="title-line" style="color:{colors[color]};margin-bottom:{gap}px;'
            f'font-size:{line_size}px;transform:translateX({offset}px)">'
            f'{text}</span>'
        )

    template = Template((ROOT / "templates/hosts-split.html").read_text())
    return template.substitute(
        title_font=asset(ROOT / "assets/fonts/LibreFranklin.ttf", preview),
        number_font=asset(ROOT / "assets/fonts/OpenSans.ttf", preview),
        emoji_font=asset(ROOT / "assets/fonts/NotoColorEmoji.ttf", preview),
        background=asset(REPOSITORY / brand["background"], preview),
        logo=logo_asset(REPOSITORY / brand["logo"], preview),
        number_size=f'{number(brand["episodeNumber"]["fontSize"], "number fontSize", 12, 100)}px',
        number_color=colors[brand["episodeNumber"]["color"]],
        title_size=f"{font_size}px",
        title_top=f"{title_top}px",
        title_left=f"{title_center - title_width / 2}px",
        title_width=f"{title_width}px",
        primary=colors["primary"],
        outline=colors["personOutline"],
        grayscale="grayscale(1)" if grayscale else "none",
        episode=int(episode),
        people="\n".join(people),
        lines="\n".join(rendered_lines),
    )


def render_in_browser(config_path: Path, output: Path, browser: Browser) -> None:
    if output.suffix.lower() != ".png":
        raise ValueError("Output must have a .png extension")
    config = json.loads(config_path.read_text())
    if not isinstance(config, dict):
        raise ValueError("Configuration must be a JSON object")
    preview = output.with_suffix(".html")
    document = build_html(config, preview)
    output.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(preview, document.encode("utf-8"))
    page = browser.new_page(viewport={"width": 1280, "height": 720}, device_scale_factor=1)
    try:
        page.goto(preview.resolve().as_uri())
        page.evaluate("""async () => {
            await document.fonts.ready;
            await Promise.all([...document.images].map(image => image.decode()));
            if (!document.fonts.check('900 80px "Libre Franklin"') ||
                !document.fonts.check('800 44px "Open Sans"')) {
                throw new Error("Required fonts did not load");
            }
            if (document.querySelector(".emoji") &&
                !document.fonts.check('400 72px "Noto Color Emoji"', '⚡🤦‍♂️')) {
                throw new Error("Emoji font did not load");
            }
            for (const line of document.querySelectorAll(".title-line")) {
                if (line.scrollWidth > line.clientWidth + 1) {
                    throw new Error("Title line is too wide: " + line.textContent);
                }
                const range = document.createRange();
                range.selectNodeContents(line);
                const bounds = range.getBoundingClientRect();
                if (bounds.left < 20 || bounds.right > 1260) {
                    throw new Error("Title line extends beyond horizontal safe area");
                }
            }
            const title = document.querySelector(".title").getBoundingClientRect();
            if (title.bottom > 700) throw new Error("Title extends below the safe area");
        }""")
        head_positions = page.locator(".person").evaluate_all("""elements => elements.map(
            element => element.getBoundingClientRect().top +
                Number(element.dataset.headTop) * Number(element.dataset.scale)
        )""")
        if max(head_positions) - min(head_positions) > 1:
            raise ValueError(f"Head alignment failed: {head_positions}")
        atomic_write(output, page.locator(".cover").screenshot())
    finally:
        page.close()
    with Image.open(output) as screenshot:
        if screenshot.size != (1280, 720):
            raise ValueError(f"Unexpected output dimensions: {screenshot.size}")
    print(f"PNG: {output}\nHTML: {preview}")


def render(config_path: Path, output: Path, browser_path: str | None = None) -> None:
    executable = browser_path or shutil.which("google-chrome") or shutil.which("chromium")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=executable, headless=True)
        try:
            render_in_browser(config_path, output, browser)
        finally:
            browser.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", nargs="?", type=Path, default=ROOT / "episodes/demo.json")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--browser", help="Path to a local Chrome or Chromium executable")
    args = parser.parse_args()
    render(args.config, args.output or ROOT / "output" / f"{args.config.stem}.png", args.browser)


if __name__ == "__main__":
    main()
