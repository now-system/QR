# -*- coding: utf-8 -*-
import json, os, segno
ROOT = r"C:\Users\i\Desktop\QR"
BASE = "https://now-system.github.io/QR"
PRODUCTS = json.load(open(os.path.join(ROOT, "products.json"), encoding="utf-8"))
qrdir = os.path.join(ROOT, "qr"); os.makedirs(qrdir, exist_ok=True)
rows = []
for slug, model, desc in PRODUCTS:
    url = f"{BASE}/{slug}.pdf"
    q = segno.make(url, error="h")          # H = 30% 오류정정, 인쇄물/로고삽입 대비
    png = os.path.join(qrdir, f"QR_{model.replace(' ', '_')}.png")
    svg = os.path.join(qrdir, f"QR_{model.replace(' ', '_')}.svg")
    q.save(png, scale=20, border=4)          # 약 1240px, 인쇄 300dpi에서 10cm
    q.save(svg, scale=20, border=4)
    rows.append((slug, model, desc, url, q.version))
    print(f"{model:14s} v{q.version:<2d} {url}")
json.dump(rows, open(os.path.join(ROOT, "_rows.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
