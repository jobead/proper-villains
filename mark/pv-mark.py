import math, shutil

def tapered_arc_path(cx, cy, r, start_deg, end_deg, start_width, end_width, segments=200):
    points_outer, points_inner = [], []
    total_span = (end_deg - start_deg) % 360 or 360
    for i in range(segments + 1):
        t = i / segments
        deg = start_deg + t * total_span
        rad = math.radians(deg - 90)
        half_w = (start_width + t * (end_width - start_width)) / 2.0
        nx = math.cos(rad)
        ny = math.sin(rad)
        ax = cx + r * nx
        ay = cy + r * ny
        points_outer.append((ax + half_w * nx, ay + half_w * ny))
        points_inner.append((ax - half_w * nx, ay - half_w * ny))
    d = f"M {points_outer[0][0]:.2f},{points_outer[0][1]:.2f} "
    for x, y in points_outer[1:]:
        d += f"L {x:.2f},{y:.2f} "
    for x, y in reversed(points_inner):
        d += f"L {x:.2f},{y:.2f} "
    d += "Z"
    return d

cx, cy = 150, 150
r = 90
start_w = 10.0
end_w = 0.5
start_deg = 180
span = 255  # CORRECTED: max byte value is 255, not 256

start_rad = math.radians(start_deg - 90)
sx = cx + r * math.cos(start_rad)
sy = cy + r * math.sin(start_rad)
nx_s = math.cos(start_rad)
ny_s = math.sin(start_rad)
hw = start_w / 2

arc_path = tapered_arc_path(cx, cy, r, start_deg, start_deg + span, start_w, end_w)

ext = 4
wt = 9
tick = f'<line x1="{sx + (hw + ext) * nx_s:.2f}" y1="{sy + (hw + ext) * ny_s:.2f}" x2="{sx - (hw + ext) * nx_s:.2f}" y2="{sy - (hw + ext) * ny_s:.2f}" stroke="white" stroke-width="{wt}"/>'

group_shift_x = 0
group_shift_y = -6

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>:^_ v18</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
body {{ background: #0a0a0a; display: flex; justify-content: center; margin: 20px 0 0 0; }}
</style>
</head>
<body>
<svg width="300" height="300" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
  <path d="{arc_path}" fill="#ffffff"/>
  {tick}
  <text id="c0" x="0" y="0" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="67" font-weight="500">:</text>
  <text id="c1" x="0" y="0" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="67" font-weight="500">^</text>
  <text id="c2" x="0" y="0" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="67" font-weight="500">_</text>
</svg>
<script>
document.fonts.ready.then(() => {{
  const cx={cx}, cy={cy};
  const chars = [0,1,2].map(i => document.getElementById('c'+i));
  const bboxes = chars.map(c => c.getBBox());
  const widths = bboxes.map(b => b.width);
  const letterSpacing = 6;
  const totalWidth = widths.reduce((a,b)=>a+b,0) + letterSpacing*2;
  const allTops = bboxes.map(b=>b.y);
  const allBottoms = bboxes.map(b=>b.y+b.height);
  const minTop = Math.min(...allTops);
  const maxBottom = Math.max(...allBottoms);
  const groupHeight = maxBottom - minTop;
  const baselineDy = cy - (minTop + groupHeight/2);
  let startX = cx - totalWidth/2;
  chars.forEach((c,i) => {{
    const bb = bboxes[i];
    const dx = startX - bb.x + {group_shift_x};
    let dy = baselineDy + ({group_shift_y});
    if (i===2) dy += 12;
    c.setAttribute('transform', `translate(${{dx.toFixed(1)}}, ${{dy.toFixed(1)}})`);
    startX += bb.width + letterSpacing;
  }});
}});
</script>
</body>
</html>"""

with open("/tmp/v18.html", "w") as f:
    f.write(html)
shutil.copy("/tmp/v18.html", "/agent/home/pv-mark-iterations/v18-255deg.html")
shutil.copy("/tmp/v18.py", "/agent/home/pv-mark-iterations/v18-255deg.py")
with open("/agent/home/pv-mark-iterations/VERSION_LOG.md", "a") as f:
    f.write("- **v18**: Corrected arc to 255° (max byte value = 255, not 256). Gap is now 105°.\n")
print("done")
