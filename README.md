# (주)나우시스템 제품 데이터시트

`https://now-system.github.io/QR/` 에서 서비스되는 정적 사이트입니다.
카탈로그의 제품별 QR 코드는 아래 URL을 가리킵니다.

## 제품 목록 (14종)

| 제품 | 설명 | 데이터시트 URL | QR 파일 |
|---|---|---|---|
| **NW-RC06-D** | Power Supply / Audio Control Unit | `https://now-system.github.io/QR/nw-rc06-d.pdf` | `qr/QR_NW-RC06-D.png` |
| **NTBS-N50** | 네트워크 방송 서버 (VoIP Server) | `https://now-system.github.io/QR/ntbs-n50.pdf` | `qr/QR_NTBS-N50.png` |
| **NWPA-GP** | Gooseneck Paging Microphone | `https://now-system.github.io/QR/nwpa-gp.pdf` | `qr/QR_NWPA-GP.png` |
| **NWIPK-H30** | IP Network Horn Speaker | `https://now-system.github.io/QR/nwipk-h30.pdf` | `qr/QR_NWIPK-H30.png` |
| **NW-IPS AI** | AI IP Speaker | `https://now-system.github.io/QR/nw-ips-ai.pdf` | `qr/QR_NW-IPS_AI.png` |
| **SIM-208B** | Network Switch | `https://now-system.github.io/QR/sim-208b.pdf` | `qr/QR_SIM-208B.png` |
| **D3210GV** | Network Switch | `https://now-system.github.io/QR/d3210gv.pdf` | `qr/QR_D3210GV.png` |
| **NW-RTU** | Environmental Monitoring Controller | `https://now-system.github.io/QR/nw-rtu.pdf` | `qr/QR_NW-RTU.png` |
| **NW-RC04** | ON/OFF 전원제어기 | `https://now-system.github.io/QR/nw-rc04.pdf` | `qr/QR_NW-RC04.png` |
| **JWPA-260** | IP Digital Network AMP | `https://now-system.github.io/QR/jwpa-260.pdf` | `qr/QR_JWPA-260.png` |
| **AirN-DK** | Composite Sensor (복합 대기질 센서) | `https://now-system.github.io/QR/airn-dk.pdf` | `qr/QR_AirN-DK.png` |
| **NWIC-F0203WR** | AI Flame Sensor Camera | `https://now-system.github.io/QR/nwic-f0203wr.pdf` | `qr/QR_NWIC-F0203WR.png` |
| **NWIC-B0505WR** | AI Security Bullet Camera | `https://now-system.github.io/QR/nwic-b0505wr.pdf` | `qr/QR_NWIC-B0505WR.png` |
| **NWP-MS** | SMART Multi-Detector System | `https://now-system.github.io/QR/nwp-ms.pdf` | `qr/QR_NWP-MS.png` |

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
