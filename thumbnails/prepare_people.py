"""Remove Canva's solid magenta background and crop individual portraits."""

import argparse
import io
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter

if __package__:
    from .file_utils import atomic_write
else:
    from file_utils import atomic_write


BACKGROUND = (255, 0, 255)
ROOT = Path(__file__).resolve().parent


def prepare(image: Image.Image, padding: int = 40) -> Image.Image:
    image = image.convert("RGBA")
    rgb = image.convert("RGB")
    channels = rgb.split()
    red = channels[0].point(lambda value: 255 if value >= 247 else 0)
    green = channels[1].point(lambda value: 255 if value <= 8 else 0)
    blue = channels[2].point(lambda value: 255 if value >= 247 else 0)
    background = ImageChops.multiply(ImageChops.multiply(red, green), blue)
    background = ImageChops.lighter(
        background, image.getchannel("A").point(lambda value: 255 if value == 0 else 0)
    )
    magenta_excess = ImageChops.subtract(
        ImageChops.darker(channels[0], channels[2]), channels[1]
    ).point(lambda value: 255 if value > 40 else 0)
    spill = ImageChops.multiply(
        background.filter(ImageFilter.MaxFilter(41)), magenta_excess
    )
    edge_region = ImageChops.lighter(
        background.filter(ImageFilter.MaxFilter(13)), spill
    )
    edges = ImageChops.subtract(edge_region, background)
    pixels = image.load()
    background_pixels = background.load()
    edge_pixels = edges.load()
    excluded = edge_region.load()
    source = rgb.load()
    width, height = image.size
    offsets = sorted(
        (
            (dx, dy)
            for dx in range(-24, 25)
            for dy in range(-24, 25)
            if dx or dy
        ),
        key=lambda offset: offset[0] ** 2 + offset[1] ** 2,
    )

    for y in range(height):
        for x in range(width):
            if background_pixels[x, y]:
                pixels[x, y] = (0, 0, 0, 0)
                continue
            if not edge_pixels[x, y]:
                continue

            color = source[x, y]
            excess = max(0, min(color[0], color[2]) - color[1])
            foreground = None
            for dx, dy in offsets:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height and not excluded[nx, ny]:
                    candidate = source[nx, ny]
                    if excess <= 40 or min(candidate[0], candidate[2]) - candidate[1] <= 40:
                        foreground = candidate
                        break
            if foreground is None:
                if excess <= 40:
                    continue
                # Thin hair strands lack an interior sample; neutralize key spill.
                foreground = (color[0] - excess, color[1], color[2] - excess)

            direction = tuple(bg - fg for bg, fg in zip(BACKGROUND, foreground))
            denominator = sum(value * value for value in direction)
            if denominator == 0:
                continue
            mixture = sum(
                (value - fg) * delta
                for value, fg, delta in zip(color, foreground, direction)
            ) / denominator
            coverage = 1 - min(1, max(0, mixture))
            alpha = round(pixels[x, y][3] * coverage)
            if alpha == 0:
                pixels[x, y] = (0, 0, 0, 0)
                continue
            # Undo the magenta contribution instead of leaving a colored fringe.
            restored = tuple(
                min(255, max(0, round((value - (1 - coverage) * bg) / coverage)))
                for value, bg in zip(color, BACKGROUND)
            )
            residual_spill = max(0, min(restored[0], restored[2]) - restored[1] - 10)
            restored = (
                restored[0] - residual_spill,
                min(restored[1], max(restored[0] - residual_spill, restored[2] - residual_spill) + 2),
                restored[2] - residual_spill,
            )
            pixels[x, y] = (*restored, alpha)

    bounds = image.getchannel("A").getbbox()
    if bounds is None:
        raise ValueError("Image contains no foreground after background removal")
    cropped = image.crop(bounds)
    result = Image.new(
        "RGBA", (cropped.width + 2 * padding, cropped.height + 2 * padding)
    )
    result.paste(cropped, (padding, padding))
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT / "assets/people/source")
    parser.add_argument("--output", type=Path, default=ROOT / "assets/people/ready")
    parser.add_argument("--padding", type=int, default=40)
    args = parser.parse_args()
    if args.padding < 0:
        parser.error("--padding must not be negative")
    if args.source.resolve() == args.output.resolve():
        parser.error("Source and output directories must be different")
    paths = sorted(args.source.glob("*.png"))
    if not paths:
        parser.error(f"No PNG files found in {args.source}")
    args.output.mkdir(parents=True, exist_ok=True)
    for path in paths:
        with Image.open(path) as image:
            result = prepare(image, args.padding)
        output = args.output / path.name
        buffer = io.BytesIO()
        result.save(buffer, format="PNG", optimize=True)
        atomic_write(output, buffer.getvalue())
        print(f"{path.name}: {result.width} x {result.height} -> {output}")


if __name__ == "__main__":
    main()
