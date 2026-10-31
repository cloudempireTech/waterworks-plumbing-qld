import os
import requests
from PIL import Image
import io

base_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\waterworks-plumbing-qld\assets\images"

photos = [
    # 1. Copper piping / tools
    ("hero-plumber-copper.jpg", "https://images.unsplash.com/photo-1581578731548-c64695cc6952?q=80&w=1400&auto=format&fit=crop"),
    # 2. Emergency plumbing / wrench
    ("emergency-pipe-burst.jpg", "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?q=80&w=1400&auto=format&fit=crop"),
    # 3. Hot water / heating unit
    ("hot-water-system.jpg", "https://images.unsplash.com/photo-1542013936693-884638332954?q=80&w=1400&auto=format&fit=crop"),
    # 4. Drainage / jetting / pipes
    ("blocked-drain-jetting.jpg", "https://images.unsplash.com/photo-1504307651254-35680f356dfd?q=80&w=1400&auto=format&fit=crop"),
    # 5. Plumbing tools / gauge
    ("cctv-drain-camera.jpg", "https://images.unsplash.com/photo-1581092160607-ee22621dd758?q=80&w=1400&auto=format&fit=crop"),
    # 6. Luxury modern bathroom tapware
    ("bathroom-renovation-tapware.jpg", "https://images.unsplash.com/photo-1584622781564-1d987f7333c1?q=80&w=1400&auto=format&fit=crop"),
    # 7. Pipe connections / gas
    ("gas-fitting-pipes.jpg", "https://images.unsplash.com/photo-1513694203232-719a280e022f?q=80&w=1400&auto=format&fit=crop"),
    # 8. Service tools / van equipment
    ("commercial-plumbing-van.jpg", "https://images.unsplash.com/photo-1581092335397-9583fe92d232?q=80&w=1400&auto=format&fit=crop"),
    # 9. Plumber inspecting sink / fixtures
    ("master-plumber-inspection.jpg", "https://images.unsplash.com/photo-1621905251918-48416bd8575a?q=80&w=1400&auto=format&fit=crop"),
    # 10. Satisfied homeowner / clean water
    ("satisfied-customer-home.jpg", "https://images.unsplash.com/photo-1560518883-ce09059eeffa?q=80&w=1400&auto=format&fit=crop")
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

for filename, url in photos:
    dest_path = os.path.join(base_dir, filename)
    print(f"Downloading {filename}...")
    try:
        r = requests.get(url, headers=headers, timeout=20)
        if r.status_code == 200:
            img = Image.open(io.BytesIO(r.content))
            img = img.convert("RGB")
            # Resize if width > 1600
            if img.width > 1600:
                h = int(img.height * (1600 / img.width))
                img = img.resize((1600, h), Image.Resampling.LANCZOS)
            img.save(dest_path, "JPEG", quality=86, optimize=True)
            print(f"  Saved {filename} ({img.width}x{img.height})")
        else:
            print(f"  FAILED HTTP {r.status_code} for {filename}")
    except Exception as e:
        print(f"  ERROR for {filename}: {e}")

print("Image download routine finished.")
