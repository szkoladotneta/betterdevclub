"""Generate every host-pose pair in both left/right arrangements."""

import argparse
import copy
import html
import io
import itertools
import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

if __package__:
    from .file_utils import atomic_write
    from .render import MAX_TITLE_LINES, ROOT, render_in_browser
else:
    from file_utils import atomic_write
    from render import MAX_TITLE_LINES, ROOT, render_in_browser


LINES = [
    {"text": "SDLC", "color": "primary"},
    {"text": "W ERZE AI", "color": "text"},
    {"text": "Kod  2 DNI ⚡", "color": "primary"},
    {"text": "DeplOY", "color": "text"},
    {"text": "42 tyg. 🤦‍♂️", "color": "highlight"},
]


def build_variants(portraits: dict, content: dict | None = None) -> list[tuple[str, dict]]:
    if content is not None and (
        not isinstance(content, dict)
        or "episode" not in content
        or not isinstance(content.get("lines"), list)
        or not 1 <= len(content["lines"]) <= MAX_TITLE_LINES
    ):
        raise ValueError(f"Content configuration must contain episode and one to {MAX_TITLE_LINES} lines")
    requested_lines = LINES if content is None else content["lines"]
    if any(
        not isinstance(line, dict)
        or not isinstance(line.get("text"), str)
        or not line["text"].strip()
        for line in requested_lines
    ):
        raise ValueError("Each content line must contain nonempty text")
    piotreks = sorted(key for key in portraits if key.startswith("piotrek-"))
    kajetans = sorted(key for key in portraits if key.startswith("kajetan-"))
    if not piotreks or not kajetans:
        raise ValueError("Portrait metadata must contain both hosts")
    profiles = {
        name: json.loads((ROOT / "episodes" / f"layout-{name}.json").read_text())
        for name in ("compact", "palm", "pointing")
    }
    variants = []
    for piotrek, kajetan in itertools.product(piotreks, kajetans):
        for piotrek_side in ("left", "right"):
            people = (
                {"left": piotrek, "right": kajetan}
                if piotrek_side == "left"
                else {"left": kajetan, "right": piotrek}
            )
            gestures = {portraits[key].get("gesture") for key in people.values()} - {None}
            if gestures - {"palm", "point"}:
                raise ValueError(f"Unknown gesture metadata: {gestures}")
            layout = "palm" if "palm" in gestures else "pointing" if "point" in gestures else "compact"
            config = copy.deepcopy(profiles[layout])
            config["people"] = people
            config["layout"] = layout
            profile_lines = config["lines"]
            config["lines"] = [
                {**profile_lines[min(index, len(profile_lines) - 1)], **source}
                for index, source in enumerate(requested_lines)
            ]
            config["lines"][-1].pop("gapAfter", None)
            if content is not None:
                config["episode"] = content["episode"]
                if "grayscale" in content:
                    config["grayscale"] = content["grayscale"]
            if layout != "compact":
                gesture = "palm" if layout == "palm" else "point"
                side = next(side for side, key in people.items() if portraits[key].get("gesture") == gesture)
                original_side = "left" if layout == "palm" else "right"
                if side != original_side:
                    centers = config["headCenters"]
                    config["headCenters"] = {
                        "left": 1280 - centers["right"],
                        "right": 1280 - centers["left"],
                    }
                    config["titleCenterX"] = 1280 - config.get("titleCenterX", 640)
                    for line in config["lines"]:
                        if "offsetX" in line:
                            line["offsetX"] *= -1
            name = f'{piotrek.rsplit("-", 1)[0]}_{kajetan.rsplit("-", 1)[0]}_piotrek-{piotrek_side}'
            variants.append((name, config))
    return variants


def caption(index: int, config: dict) -> str:
    left = config["people"]["left"].rsplit("-", 1)[0]
    right = config["people"]["right"].rsplit("-", 1)[0]
    layout = config["layout"]
    return f"{index:02d} | L: {left} | R: {right} | {layout}"


def write_gallery(variants: list[tuple[str, dict]], output: Path) -> None:
    cards = []
    sheet = Image.new("RGB", (1920, ((len(variants) + 2) // 3) * 400), "#111827")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.truetype(str(ROOT / "assets/fonts/OpenSans.ttf"), 16)
    for index, (name, config) in enumerate(variants, 1):
        label = caption(index, config)
        cards.append(
            f'<figure><a href="{name}.png"><img src="{name}.png" alt="{html.escape(label)}"></a>'
            f'<figcaption>{html.escape(label)} <a href="{name}.html">HTML</a></figcaption></figure>'
        )
        with Image.open(output / f"{name}.png") as image:
            thumbnail = image.convert("RGB").resize((640, 360), Image.Resampling.LANCZOS)
        x, y = ((index - 1) % 3) * 640, ((index - 1) // 3) * 400
        sheet.paste(thumbnail, (x, y))
        draw.text((x + 12, y + 370), label, font=font, fill="white")
    buffer = io.BytesIO()
    sheet.save(buffer, format="PNG")
    atomic_write(output / "contact-sheet.png", buffer.getvalue())
    document = f"""<!doctype html>
<html lang="pl"><meta charset="utf-8">
<title>Better Dev Club — wszystkie kombinacje</title>
<style>
body {{ margin:24px; background:#111827; color:white; font-family:system-ui; }}
main {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(360px,1fr)); gap:20px; }}
figure {{ margin:0; }} img {{ width:100%; display:block; }}
figcaption {{ padding:10px 0; font-size:14px; }} a {{ color:#2ebef7; }}
</style>
<h1>{len(variants)} kombinacji</h1>
<p>Kliknij okładkę, aby otworzyć PNG 1280 × 720. L = lewa strona, R = prawa strona.</p>
<main>{"".join(cards)}</main></html>"""
    atomic_write(output / "index.html", document.encode("utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "output/combinations")
    parser.add_argument("--config", type=Path, help="JSON containing episode and title lines")
    parser.add_argument("--browser")
    args = parser.parse_args()
    portraits = json.loads((ROOT / "assets/people/portraits.json").read_text())
    content = json.loads(args.config.read_text()) if args.config else None
    variants = build_variants(portraits, content)
    configurations = ROOT / "episodes/combinations"
    if args.config:
        configurations /= args.config.stem
    configurations.mkdir(parents=True, exist_ok=True)
    args.output.mkdir(parents=True, exist_ok=True)
    executable = args.browser or shutil.which("google-chrome") or shutil.which("chromium")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=executable, headless=True)
        try:
            for name, config in variants:
                path = configurations / f"{name}.json"
                atomic_write(path, (json.dumps(config, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
                render_in_browser(path, args.output / f"{name}.png", browser)
        finally:
            browser.close()
    write_gallery(variants, args.output)
    print(f"Generated {len(variants)} combinations\nGallery: {args.output / 'index.html'}")


if __name__ == "__main__":
    main()
