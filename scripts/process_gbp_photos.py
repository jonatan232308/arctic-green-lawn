"""Resize + compress GBP photos into /static/images/ for Hugo.

Reads from static/images/gbp/photo-NN.jpg, outputs optimized JPGs to
static/images/ with descriptive names ready for Hugo.
"""
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "static" / "images" / "gbp"
OUT = ROOT / "static" / "images"

# (source_photo_number, output_filename, max_width, max_height, quality)
JOBS = [
    # Hero — big, shown across site
    (18, "hero-lawn.jpg", 1920, 1280, 82),
    # Why-us section photo — medium, distinct from hero
    (16, "why-us-tree.jpg", 1400, 1050, 82),
    # Service card thumbnails — small
    (30, "svc-mowing.jpg",    800, 600, 80),
    (4,  "svc-design.jpg",    800, 600, 80),
    (37, "svc-cleanup.jpg",   800, 600, 80),
    (26, "svc-trimming.jpg",  800, 600, 80),
    (9,  "svc-irrigation.jpg",800, 600, 80),
    (19, "svc-consultation.jpg",800, 600, 80),
    # Commercial social-proof strip — medium
    (24, "commercial-1.jpg",  1200, 900, 80),
    (22, "commercial-2.jpg",  1200, 900, 80),
    (21, "commercial-3.jpg",  1200, 900, 80),
    # Hardscape / pavers gallery
    (32, "hardscape-1.jpg",   1400, 1050, 82),
    (34, "hardscape-2.jpg",   1400, 1050, 82),
    (31, "hardscape-3.jpg",   1400, 1050, 82),
    (36, "hardscape-4.jpg",   1400, 1050, 82),
    (33, "hardscape-5.jpg",   1400, 1050, 82),
]

def process(src: Path, dst: Path, max_w: int, max_h: int, q: int):
    img = Image.open(src)
    img = ImageOps.exif_transpose(img)
    img.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
    img = img.convert("RGB")
    img.save(dst, format="JPEG", quality=q, optimize=True, progressive=True)
    kb = dst.stat().st_size // 1024
    print(f"{dst.name:28s} {img.size[0]}x{img.size[1]:<5} {kb}KB")

for num, name, w, h, q in JOBS:
    src = SRC / f"photo-{num:02d}.jpg"
    dst = OUT / name
    if not src.exists():
        print(f"MISSING: {src}")
        continue
    process(src, dst, w, h, q)

print("\nDone.")
