import os
from PIL import Image, ImageDraw

base_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\waterworks-plumbing-qld\assets\images"
os.makedirs(base_dir, exist_ok=True)

# 1. Create logo.svg and favicon.svg
svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <defs>
    <linearGradient id="waterGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c2a4d"/>
      <stop offset="100%" stop-color="#07172b"/>
    </linearGradient>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#bgGrad)" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Droplet & Pipe Wave Geometry -->
  <path d="M50 16 C50 16 30 38 30 56 C30 67.05 38.95 76 50 76 C61.05 76 70 67.05 70 56 C70 38 50 16 50 16 Z" fill="url(#waterGrad)"/>
  <!-- Inner Dynamic Water Flow Ripple -->
  <path d="M42 50 C46 45 54 45 58 50 C62 55 58 64 50 64 C42 64 38 55 42 50 Z" fill="#ffffff" opacity="0.85"/>
  <circle cx="50" cy="36" r="4" fill="#ffffff" opacity="0.9"/>
</svg>"""

with open(os.path.join(base_dir, "logo.svg"), "w", encoding="utf-8") as f:
    f.write(svg_content)

with open(os.path.join(base_dir, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(svg_content)

print("SVGs written.")

# 2. Render PNG icons with PIL
def draw_water_emblem(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Background circle
    margin = size * 0.04
    draw.ellipse([margin, margin, size - margin, size - margin], fill=(12, 42, 77, 255), outline=(56, 189, 248, 255), width=max(2, int(size * 0.025)))
    
    # Droplet geometry
    cx, cy = size / 2, size * 0.54
    r = size * 0.28
    # Lower circle of droplet
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(2, 132, 199, 255))
    # Top triangle of droplet
    top_y = size * 0.18
    draw.polygon([(cx, top_y), (cx - r * 0.92, cy), (cx + r * 0.92, cy)], fill=(2, 132, 199, 255))
    
    # Inner shine
    inner_r = size * 0.12
    draw.ellipse([cx - inner_r * 0.5, cy - inner_r * 0.8, cx + inner_r * 1.1, cy + inner_r * 0.8], fill=(255, 255, 255, 200))
    draw.ellipse([cx - size * 0.04, size * 0.35, cx + size * 0.04, size * 0.43], fill=(255, 255, 255, 220))
    
    return img

logo_512 = draw_water_emblem(512)
logo_512.save(os.path.join(base_dir, "logo-512.png"), "PNG")

apple_180 = draw_water_emblem(180)
apple_180.save(os.path.join(base_dir, "apple-touch-icon.png"), "PNG")

fav_32 = draw_water_emblem(32)
fav_32.save(os.path.join(base_dir, "favicon-32x32.png"), "PNG")

fav_16 = draw_water_emblem(16)
fav_48 = draw_water_emblem(48)
fav_32.save(os.path.join(base_dir, "favicon.ico"), format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])

print("Favicon suite created successfully!")
