import urllib.request
import json
import base64
import os

API_KEY = "AQ.Ab8RN6Lxithrwl7a3XChlRU3Y-0arPMPCeHsqtgxvdC-4YYPqQ"
HEADERS = {"X-Goog-Api-Key": API_KEY}

def download_and_extract(url, out_path):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    
    raw = data.get("dataString") or data.get("image") or data.get("html")
    is_img = "imageMetadata" in data or out_path.endswith((".png", ".jpg", ".jpeg"))
    
    if is_img:
        img_bytes = base64.b64decode(raw)
        with open(out_path, "wb") as f:
            f.write(img_bytes)
        print(f"Saved image: {out_path} ({len(img_bytes)} bytes)")
    else:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(raw)
        print(f"Saved text: {out_path} ({len(raw)} chars)")

os.makedirs("assets", exist_ok=True)

# Target screen: Grocery Spotlight — Animated Landing Page (ID: 4a6fc0dff43448ff9581b4473590c861)
download_and_extract("https://stitch.googleapis.com/v1/projects/558176700809783641/files/screenshot_00066006d3895f6e020790cb63393f72:download", "assets/screenshot-animated-landing.png")
download_and_extract("https://stitch.googleapis.com/v1/projects/558176700809783641/files/4a6fc0dff43448ff9581b4473590c861:download", "index.html")

# Additional brand assets and screens from the same project
download_and_extract("https://stitch.googleapis.com/v1/projects/558176700809783641/files/5d1fff526a7b458ba698085df886fab7:download", "assets/logo-refined-mark.svg")
download_and_extract("https://stitch.googleapis.com/v1/projects/558176700809783641/files/screenshot_00066006b17d864903386b00011d71cf:download", "assets/logo-refined-mark.png")
download_and_extract("https://stitch.googleapis.com/v1/projects/558176700809783641/files/55dea759445a480788ee1853cbd70357:download", "assets/logo-pin-produce.svg")
download_and_extract("https://stitch.googleapis.com/v1/projects/558176700809783641/files/screenshot_00066006843059b3033859d29b192ba8:download", "assets/logo-pin-produce.png")
download_and_extract("https://stitch.googleapis.com/v1/projects/558176700809783641/files/04f895ebf2c54a858bd2b2dae8980b2d:download", "prototype-animated-landing.html")
download_and_extract("https://stitch.googleapis.com/v1/projects/558176700809783641/files/16066187567463472281:download", "demo.html")
