# -*- coding: utf-8 -*-
import json, os
ROOT = r"C:\Users\i\Desktop\QR"
rows = json.load(open(os.path.join(ROOT, "_rows.json"), encoding="utf-8"))
CATS = {
 "네트워크 방송": ["ntbs-n50","nwpa-gp","nwipk-h30","nw-ais","jwpa-260","nw-rc06-d"],
 "네트워크 장비": ["sim-208b","d3210gv"],
 "제어 · 감시": ["nw-rtu","nw-rc04","nwp-ms"],
 "환경 · 영상 센서": ["airn-dk","nwic-f0203wr","nwic-b0505wr"],
}
byslug = {r[0]: r for r in rows}
cards = []
for cat, slugs in CATS.items():
    items = "\n".join(
      f'''      <a class="card" href="./{s}.pdf">
        <span class="model">{byslug[s][1]}</span>
        <span class="desc">{byslug[s][2]}</span>
        <span class="go">데이터시트 PDF &rarr;</span>
      </a>''' for s in slugs)
    cards.append(f'    <h2>{cat}</h2>\n    <div class="grid">\n{items}\n    </div>')
body = "\n".join(cards)
html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>(주)나우시스템 제품 데이터시트</title>
<meta name="description" content="나우시스템 네트워크 방송·제어·센서 제품 데이터시트 모음">
<style>
  :root {{ --bg:#f6f7f9; --card:#fff; --fg:#15181d; --sub:#5b6472; --line:#e3e6eb; --accent:#0b5fd1; }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --bg:#12151a; --card:#1b1f26; --fg:#eef1f5; --sub:#9aa4b2; --line:#2a303a; --accent:#5fa8ff; }}
  }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--fg);
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Malgun Gothic","Apple SD Gothic Neo",sans-serif;
    line-height:1.55; }}
  header {{ padding:40px 20px 28px; text-align:center; border-bottom:1px solid var(--line); }}
  header .brand {{ font-size:13px; letter-spacing:.18em; color:var(--sub); text-transform:uppercase; }}
  header h1 {{ margin:8px 0 4px; font-size:26px; letter-spacing:-.02em; }}
  header p {{ margin:0; color:var(--sub); font-size:14px; }}
  main {{ max-width:920px; margin:0 auto; padding:8px 20px 60px; }}
  h2 {{ font-size:15px; color:var(--sub); font-weight:600; margin:34px 0 12px;
       letter-spacing:.02em; }}
  .grid {{ display:grid; gap:12px; grid-template-columns:repeat(auto-fill,minmax(260px,1fr)); }}
  .card {{ display:flex; flex-direction:column; gap:3px; padding:16px 18px; background:var(--card);
    border:1px solid var(--line); border-radius:12px; text-decoration:none; color:inherit;
    transition:border-color .15s, transform .15s; }}
  .card:hover {{ border-color:var(--accent); transform:translateY(-1px); }}
  .model {{ font-weight:700; font-size:16px; letter-spacing:-.01em; }}
  .desc {{ color:var(--sub); font-size:13px; }}
  .go {{ margin-top:8px; color:var(--accent); font-size:12.5px; font-weight:600; }}
  footer {{ text-align:center; color:var(--sub); font-size:12.5px; padding:0 20px 48px; }}
</style>
</head>
<body>
<header>
  <div class="brand">NOW SYSTEM</div>
  <h1>제품 데이터시트</h1>
  <p>제품을 선택하면 데이터시트 PDF가 열립니다</p>
</header>
<main>
{body}
</main>
<footer>&copy; (주)나우시스템 &middot; nowsys.co.kr</footer>
</body>
</html>
'''
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)

# 404 -> index
open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(
 '<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8">'
 '<meta http-equiv="refresh" content="0; url=/QR/"><title>이동 중</title></head>'
 '<body><p>페이지를 찾을 수 없습니다. <a href="/QR/">제품 목록으로 이동</a></p></body></html>')

lines = ["| 제품 | 설명 | 데이터시트 URL | QR 파일 |", "|---|---|---|---|"]
for slug, model, desc, url, ver in rows:
    lines.append(f"| **{model}** | {desc} | `{url}` | `qr/QR_{model.replace(' ','_')}.png` |")
readme = f'''# (주)나우시스템 제품 데이터시트

`https://now-system.github.io/QR/` 에서 서비스되는 정적 사이트입니다.
카탈로그의 제품별 QR 코드는 아래 URL을 가리킵니다.

## 제품 목록 (14종)

{chr(10).join(lines)}

## 구조

```
/                     제품 목록 페이지 (index.html)
/<slug>.pdf           제품별 데이터시트 (QR 연결 대상)
/qr/QR_<모델명>.png   인쇄용 QR (1240px, 오류정정 H)
/qr/QR_<모델명>.svg   인쇄용 QR (벡터)
```

## 데이터시트 교체 방법

**PDF 파일명을 절대 바꾸지 마세요.** 파일명이 곧 QR 주소입니다.
같은 이름으로 덮어쓰고 commit + push 하면 1~2분 내 반영되며, 이미 인쇄된 QR도 그대로 동작합니다.

## GitHub Pages 설정

저장소 → Settings → Pages
Source `Deploy from a branch` / Branch `main` `/ (root)` / Custom domain 비움.

커스텀 도메인을 쓰지 않으므로 도메인 만료·호스팅 해지의 영향을 받지 않습니다.
'''
open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8").write(readme)
print("index.html / 404.html / README.md written")
