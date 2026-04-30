"""
Add a castle-on-mountain outline to the bottom-right corner of bootcamp.jpg
Version 3: Properly sized, subtle, elegant outline in the corner
"""
from PIL import Image, ImageDraw
import os

# Open the ORIGINAL backup image
img_path = r"c:\Users\iolga\PycharmProjects\RL-Bootcamp2026\assets\bootcamp.jpg"
backup_path = r"c:\Users\iolga\PycharmProjects\RL-Bootcamp2026\assets\bootcamp_original_backup.jpg"
img = Image.open(backup_path).convert("RGBA")
w, h = img.size
print(f"Original image size: {w}x{h}")

# Create a transparent overlay
overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# Colors - white/light for visibility against both sky and trees
outline_color = (255, 255, 255, 160)   # white, semi-transparent
line_w = 2

# =============================================
# Position: bottom-right corner
# Castle scene should be compact, ~200px wide, ~150px tall
# Anchored to bottom-right corner of image
# =============================================

# Right edge offset
rx = w - 30   # right margin
by = h - 20   # bottom margin

# Mountain base line
mt_pts = [
    (rx - 260, by),          # far left ground
    (rx - 220, by - 40),     # left rise
    (rx - 180, by - 65),     # left shoulder
    (rx - 150, by - 55),     # small valley
    (rx - 120, by - 85),     # main peak
    (rx - 90,  by - 80),     # right of peak
    (rx - 55,  by - 60),     # right slope
    (rx - 20,  by - 35),     # far right slope
    (rx + 10,  by),          # right ground
]
draw.line(mt_pts, fill=outline_color, width=line_w + 1)

# =============================================
# Castle sits on the main peak
# =============================================
pk_x = rx - 120  # peak x
pk_y = by - 85   # peak y

# Main wall
wl = pk_x - 30
wr = pk_x + 30
wt = pk_y - 15
wb = pk_y
draw.line([(wl, wb), (wl, wt), (wr, wt), (wr, wb)], fill=outline_color, width=line_w)

# Battlements on wall
for i in range(5):
    bx = wl + i * 12
    if i % 2 == 0:
        draw.rectangle([bx, wt - 5, bx + 10, wt], outline=outline_color, width=1)

# Left tower
lt_l = wl - 3
lt_w = 14
lt_h = 35
draw.rectangle([lt_l, wt - lt_h, lt_l + lt_w, wb], outline=outline_color, width=line_w)
# Left tower roof
draw.line([
    (lt_l - 2, wt - lt_h),
    (lt_l + lt_w // 2, wt - lt_h - 16),
    (lt_l + lt_w + 2, wt - lt_h),
], fill=outline_color, width=line_w)
# Left tower window
draw.rectangle([lt_l + 4, wt - lt_h + 10, lt_l + 10, wt - lt_h + 18], outline=outline_color, width=1)
draw.rectangle([lt_l + 4, wt - lt_h + 22, lt_l + 10, wt - lt_h + 30], outline=outline_color, width=1)

# Right tower
rt_l = wr - 11
rt_w = 14
rt_h = 28
draw.rectangle([rt_l, wt - rt_h, rt_l + rt_w, wb], outline=outline_color, width=line_w)
# Right tower roof
draw.line([
    (rt_l - 2, wt - rt_h),
    (rt_l + rt_w // 2, wt - rt_h - 13),
    (rt_l + rt_w + 2, wt - rt_h),
], fill=outline_color, width=line_w)
# Right tower window
draw.rectangle([rt_l + 4, wt - rt_h + 8, rt_l + 10, wt - rt_h + 16], outline=outline_color, width=1)

# Center tower (the keep - tallest)
ct_l = pk_x - 9
ct_w = 18
ct_h = 48
draw.rectangle([ct_l, wt - ct_h, ct_l + ct_w, wt], outline=outline_color, width=line_w)
# Center tower roof
draw.line([
    (ct_l - 3, wt - ct_h),
    (ct_l + ct_w // 2, wt - ct_h - 20),
    (ct_l + ct_w + 3, wt - ct_h),
], fill=outline_color, width=line_w)
# Center tower windows
draw.rectangle([ct_l + 5, wt - ct_h + 10, ct_l + 13, wt - ct_h + 18], outline=outline_color, width=1)
draw.rectangle([ct_l + 5, wt - ct_h + 24, ct_l + 13, wt - ct_h + 32], outline=outline_color, width=1)

# Flag on center tower
flag_x = ct_l + ct_w // 2
flag_y = wt - ct_h - 20
draw.line([(flag_x, flag_y), (flag_x, flag_y - 12)], fill=outline_color, width=2)
draw.line([
    (flag_x, flag_y - 12),
    (flag_x + 10, flag_y - 9),
    (flag_x, flag_y - 6),
], fill=outline_color, width=2)

# Gate archway
gate_x = pk_x
gate_y = wb - 10
draw.arc([gate_x - 5, gate_y - 5, gate_x + 5, gate_y + 5], 180, 0, fill=outline_color, width=1)
draw.line([(gate_x - 5, gate_y), (gate_x - 5, wb)], fill=outline_color, width=1)
draw.line([(gate_x + 5, gate_y), (gate_x + 5, wb)], fill=outline_color, width=1)

# Small turret on left mountain shoulder
turr_x = rx - 185
turr_y = by - 65
draw.rectangle([turr_x, turr_y - 18, turr_x + 10, turr_y], outline=outline_color, width=1)
draw.line([
    (turr_x - 1, turr_y - 18),
    (turr_x + 5, turr_y - 26),
    (turr_x + 11, turr_y - 18),
], fill=outline_color, width=1)

# =============================================
# Composite
# =============================================
result = Image.alpha_composite(img, overlay)
result_rgb = result.convert("RGB")
result_rgb.save(img_path, "JPEG", quality=95)
print(f"Saved updated image to: {img_path}")
print(f"Final size: {result_rgb.size}")
