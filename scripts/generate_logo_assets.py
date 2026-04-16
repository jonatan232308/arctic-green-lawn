"""Generate favicon, apple-touch-icon, OG image, and optimized logo variants from source logo."""
from PIL import Image, ImageOps
from pathlib import Path

SRC = Path(r"C:/Users/jonat/OneDrive/Desktop/2026-04-16 00.33.49.jpg")
OUT = Path(r"C:/Users/jonat/arctic-green-lawn/static")
IMG = OUT / "images"
IMG.mkdir(parents=True, exist_ok=True)

src = Image.open(SRC).convert("RGBA")
w, h = src.size
print(f"Source: {w}x{h}")

# Trim white border, keep mark + wordmark
bg = Image.new("RGBA", src.size, (255, 255, 255, 255))
diff = Image.alpha_composite(bg, src)
gray = ImageOps.invert(diff.convert("RGB").convert("L"))
bbox = gray.getbbox()
if bbox:
    src = src.crop(bbox)
    print(f"Trimmed to {src.size}")

# Full color logo (transparent bg) - PNG
def to_transparent(img: Image.Image) -> Image.Image:
    img = img.convert("RGBA")
    pixels = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            if r > 240 and g > 240 and b > 240:
                pixels[x, y] = (255, 255, 255, 0)
    return img

logo_t = to_transparent(src)
logo_t.save(IMG / "logo.png", "PNG", optimize=True)
print("logo.png saved")

# Header logo (smaller, optimized for retina)
header = logo_t.copy()
header.thumbnail((600, 600), Image.LANCZOS)
header.save(IMG / "logo-header.png", "PNG", optimize=True)
header.save(IMG / "logo-header.webp", "WEBP", quality=88, method=6)
print(f"logo-header saved at {header.size}")

# Footer logo - dark-bg variant: keep colored, smaller still
footer = logo_t.copy()
footer.thumbnail((400, 400), Image.LANCZOS)
footer.save(IMG / "logo-footer.png", "PNG", optimize=True)
footer.save(IMG / "logo-footer.webp", "WEBP", quality=88, method=6)
print(f"logo-footer saved at {footer.size}")

# Square favicon source (mark only - left portion)
# Logo aspect ~2:1, mark is leftmost ~28% width
mw = int(src.width * 0.30)
mark = src.crop((0, 0, mw, src.height))
# Pad to square with white
sq_size = max(mark.size)
mark_sq = Image.new("RGB", (sq_size, sq_size), (255, 255, 255))
mark_sq.paste(mark.convert("RGB"), ((sq_size - mark.width) // 2, (sq_size - mark.height) // 2))

# Favicon ICO (multi-size)
favicon = mark_sq.copy()
favicon.save(OUT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print("favicon.ico saved")

# Favicon PNGs
for size in (16, 32, 96, 192, 512):
    f = mark_sq.resize((size, size), Image.LANCZOS)
    f.save(IMG / f"favicon-{size}.png", "PNG", optimize=True)
    print(f"favicon-{size}.png saved")

# Apple touch icon (180x180, no transparency - iOS requirement)
apple = mark_sq.resize((180, 180), Image.LANCZOS)
apple.save(IMG / "apple-touch-icon.png", "PNG", optimize=True)
print("apple-touch-icon.png saved")

# OG image (1200x630)
og = Image.new("RGB", (1200, 630), (255, 255, 255))
logo_og = src.convert("RGB").copy()
logo_og.thumbnail((900, 500), Image.LANCZOS)
ox = (1200 - logo_og.width) // 2
oy = (630 - logo_og.height) // 2
og.paste(logo_og, (ox, oy))
og.save(IMG / "og-image.jpg", "JPEG", quality=88, optimize=True)
print(f"og-image.jpg saved")

print("Done.")
