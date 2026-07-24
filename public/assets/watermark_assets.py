import os
from PIL import Image, ImageEnhance

ASSETS = "/Users/VictorAji/jabuike_contents/public/assets"
OUTPUT = "/Users/VictorAji/jabuike_contents/public/content-posts"
LOGO_PATH = os.path.join(ASSETS, "FURD-BASE-main-logo.png")

logo = Image.open(LOGO_PATH).convert("RGBA")

def apply_watermark(img_path, output_path):
    img = Image.open(img_path).convert("RGBA")
    
    logo_w = int(img.width * 0.2)
    aspect = logo.height / logo.width
    logo_h = int(logo_w * aspect)
    logo_resized = logo.resize((logo_w, logo_h), Image.LANCZOS)
    
    alpha = logo_resized.split()[3]
    alpha = alpha.point(lambda p: int(p * 0.15))
    logo_resized.putalpha(alpha)
    
    margin_x = int(img.width * 0.05)
    margin_y = int(img.height * 0.05)
    pos_x = img.width - logo_w - margin_x
    pos_y = img.height - logo_h - margin_y
    
    composite = Image.new("RGBA", img.size, (0, 0, 0, 0))
    composite.paste(img, (0, 0))
    composite.paste(logo_resized, (pos_x, pos_y), logo_resized)
    
    if img_path.lower().endswith(".png"):
        composite.save(output_path, "PNG")
    else:
        composite.convert("RGB").save(output_path, "JPEG", quality=95)

def watermark_all():
    P03_IMAGES = [
        "WhatsApp Image 2026-06-23 at 15.03.39.jpeg",
        "WhatsApp Image 2026-06-23 at 15.03.39 (1).jpeg",
        "WhatsApp Image 2026-06-23 at 15.03.40.jpeg",
        "WhatsApp Image 2026-06-23 at 15.03.40 (1).jpeg",
        "WhatsApp Image 2026-06-23 at 15.03.40 (2).jpeg",
        "WhatsApp Image 2026-06-23 at 15.03.41.jpeg",
        "WhatsApp Image 2026-06-23 at 15.03.42.jpeg",
    ]
    p03_dir = os.path.join(OUTPUT, "P03-foundations-groundwork", "images")
    os.makedirs(p03_dir, exist_ok=True)
    for fname in P03_IMAGES:
        src = os.path.join(ASSETS, fname)
        if os.path.exists(src):
            out = os.path.join(p03_dir, f"wm_{fname}")
            apply_watermark(src, out)
            print(f"P03: Watermarked {fname}")

    P04_IMAGES = [
        "3d-2.jpeg", "3d-3.jpeg", "3d-4.jpeg",
        "3d-5.jpeg", "3d-6.jpeg", "3d-7.jpeg", "3d-8.jpeg",
    ]
    p04_dir = os.path.join(OUTPUT, "P04-3d-layout", "images")
    os.makedirs(p04_dir, exist_ok=True)
    for fname in P04_IMAGES:
        src = os.path.join(ASSETS, fname)
        if os.path.exists(src):
            out = os.path.join(p04_dir, f"wm_{fname}")
            apply_watermark(src, out)
            print(f"P04: Watermarked {fname}")

    P06_IMAGES = [
        "WhatsApp Image 2026-06-23 at 15.04.54.jpeg",
        "WhatsApp Image 2026-06-23 at 15.04.54 (1).jpeg",
        "WhatsApp Image 2026-06-23 at 15.04.54 (2).jpeg",
        "WhatsApp Image 2026-06-23 at 15.04.55.jpeg",
    ]
    p06_dir = os.path.join(OUTPUT, "P06-technical-spotlight", "images")
    os.makedirs(p06_dir, exist_ok=True)
    for fname in P06_IMAGES:
        src = os.path.join(ASSETS, fname)
        if os.path.exists(src):
            out = os.path.join(p06_dir, f"wm_{fname}")
            apply_watermark(src, out)
            print(f"P06: Watermarked {fname}")

    P07_IMAGES = [
        "real-1.jpeg", "real-2.jpeg",
        "WhatsApp Image 2026-06-23 at 15.04.57.jpeg",
        "WhatsApp Image 2026-06-23 at 15.04.58.jpeg",
        "WhatsApp Image 2026-06-23 at 15.04.58 (1).jpeg",
        "WhatsApp Image 2026-06-23 at 15.04.56.jpeg",
    ]
    p07_dir = os.path.join(OUTPUT, "P07-finishing-standard", "images")
    os.makedirs(p07_dir, exist_ok=True)
    for fname in P07_IMAGES:
        src = os.path.join(ASSETS, fname)
        if os.path.exists(src):
            out = os.path.join(p07_dir, f"wm_{fname}")
            apply_watermark(src, out)
            print(f"P07: Watermarked {fname}")

    P10_IMAGES = [
        "3d-2.jpeg", "3d-4.jpeg", "3d-6.jpeg",
        "real-1.jpeg", "real-2.jpeg",
        "WhatsApp Image 2026-06-23 at 15.04.57.jpeg",
        "WhatsApp Image 2026-06-23 at 15.04.58.jpeg",
    ]
    p10_dir = os.path.join(OUTPUT, "P10-master-portfolio", "images")
    os.makedirs(p10_dir, exist_ok=True)
    for fname in P10_IMAGES:
        src = os.path.join(ASSETS, fname)
        if os.path.exists(src):
            out = os.path.join(p10_dir, f"wm_{fname}")
            apply_watermark(src, out)
            print(f"P10: Watermarked {fname}")

if __name__ == "__main__":
    watermark_all()
