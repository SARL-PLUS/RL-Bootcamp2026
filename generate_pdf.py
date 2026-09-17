"""
Generate A0 Landscape PDF from flyer_photowall.html
for print center submission.

A0 Landscape: 1189mm x 841mm
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HTML_FILE = Path(__file__).parent / "assets" / "flyer_photowall.html"
OUTPUT_PDF = Path(__file__).parent / "assets" / "flyer_photowall_A0.pdf"

# Viewport matches the screen container size
VIEWPORT_WIDTH = 1680
VIEWPORT_HEIGHT = int(1680 / 1.414)  # ~1188px


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": VIEWPORT_WIDTH, "height": VIEWPORT_HEIGHT},
            device_scale_factor=2,  # 2x for sharper rendering
        )

        # Load the HTML file
        file_url = HTML_FILE.as_uri()
        print(f"Loading: {file_url}")
        await page.goto(file_url, wait_until="networkidle")

        # Wait for fonts and images to load
        await page.wait_for_timeout(3000)

        # Generate PDF — CSS @page controls A0 size, zoom scales content to fill
        print("Generating A0 landscape PDF (1189mm x 841mm)...")
        await page.pdf(
            path=str(OUTPUT_PDF),
            width="1189mm",
            height="841mm",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            prefer_css_page_size=True,
        )

        await browser.close()
        print(f"\nPDF saved: {OUTPUT_PDF}")
        print(f"Size: 1189mm x 841mm (A0 Landscape)")
        print(f"Ready to send to print center!")


if __name__ == "__main__":
    asyncio.run(main())
