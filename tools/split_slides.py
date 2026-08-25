# -*- coding: utf-8 -*-
import fitz, os, json
ROOT = r"C:\Users\i\Desktop\QR"
PRODUCTS = [
    ("nw-rc06-d",     "NW-RC06-D",     "Power Supply / Audio Control Unit"),
    ("ntbs-n50",      "NTBS-N50",      "네트워크 방송 서버 (VoIP Server)"),
    ("nwpa-gp",       "NWPA-GP",       "Gooseneck Paging Microphone"),
    ("nwipk-h30",     "NWIPK-H30",     "IP Network Horn Speaker"),
    ("nw-ips-ai",     "NW-IPS AI",     "AI IP Speaker"),
    ("sim-208b",      "SIM-208B",      "Network Switch"),
    ("d3210gv",       "D3210GV",       "Network Switch"),
    ("nw-rtu",        "NW-RTU",        "Environmental Monitoring Controller"),
    ("nw-rc04",       "NW-RC04",       "ON/OFF 전원제어기"),
    ("jwpa-260",      "JWPA-260",      "IP Digital Network AMP"),
    ("airn-dk",       "AirN-DK",       "Composite Sensor (복합 대기질 센서)"),
    ("nwic-f0203wr",  "NWIC-F0203WR",  "AI Flame Sensor Camera"),
    ("nwic-b0505wr",  "NWIC-B0505WR",  "AI Security Bullet Camera"),
    ("nwp-ms",        "NWP-MS",        "SMART Multi-Detector System"),
]
src = fitz.open(os.path.join(ROOT, "_all.pdf"))
assert src.page_count == len(PRODUCTS), (src.page_count, len(PRODUCTS))
os.makedirs(os.path.join(ROOT, "pdf"), exist_ok=True)
for i, (slug, model, desc) in enumerate(PRODUCTS):
    d = fitz.open()
    d.insert_pdf(src, from_page=i, to_page=i)
    d.set_metadata({"title": f"{model} - {desc}", "author": "(주)나우시스템 NOW SYSTEM",
                    "subject": "Product Datasheet", "keywords": model})
    p = os.path.join(ROOT, "pdf", slug + ".pdf")
    d.save(p, garbage=4, deflate=True)
    d.close()
    print(slug, os.path.getsize(p))
json.dump(PRODUCTS, open(os.path.join(ROOT, "products.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
