# (주)나우시스템 제품 데이터시트

`https://datasheet.nowsys.co.kr` 에서 서비스되는 정적 사이트입니다.
카탈로그의 제품별 QR 코드는 아래 URL을 가리킵니다.

## 제품 목록 (14종)

| 제품 | 설명 | 데이터시트 URL | QR 파일 |
|---|---|---|---|
| **NW-RC06-D** | Power Supply / Audio Control Unit | `https://datasheet.nowsys.co.kr/nw-rc06-d.pdf` | `qr/QR_NW-RC06-D.png` |
| **NTBS-N50** | 네트워크 방송 서버 (VoIP Server) | `https://datasheet.nowsys.co.kr/ntbs-n50.pdf` | `qr/QR_NTBS-N50.png` |
| **NWPA-GP** | Gooseneck Paging Microphone | `https://datasheet.nowsys.co.kr/nwpa-gp.pdf` | `qr/QR_NWPA-GP.png` |
| **NWIPK-H30** | IP Network Horn Speaker | `https://datasheet.nowsys.co.kr/nwipk-h30.pdf` | `qr/QR_NWIPK-H30.png` |
| **NW-IPS AI** | AI IP Speaker | `https://datasheet.nowsys.co.kr/nw-ips-ai.pdf` | `qr/QR_NW-IPS_AI.png` |
| **SIM-208B** | Network Switch | `https://datasheet.nowsys.co.kr/sim-208b.pdf` | `qr/QR_SIM-208B.png` |
| **D3210GV** | Network Switch | `https://datasheet.nowsys.co.kr/d3210gv.pdf` | `qr/QR_D3210GV.png` |
| **NW-RTU** | Environmental Monitoring Controller | `https://datasheet.nowsys.co.kr/nw-rtu.pdf` | `qr/QR_NW-RTU.png` |
| **NW-RC04** | ON/OFF 전원제어기 | `https://datasheet.nowsys.co.kr/nw-rc04.pdf` | `qr/QR_NW-RC04.png` |
| **JWPA-260** | IP Digital Network AMP | `https://datasheet.nowsys.co.kr/jwpa-260.pdf` | `qr/QR_JWPA-260.png` |
| **AirN-DK** | Composite Sensor (복합 대기질 센서) | `https://datasheet.nowsys.co.kr/airn-dk.pdf` | `qr/QR_AirN-DK.png` |
| **NWIC-F0203WR** | AI Flame Sensor Camera | `https://datasheet.nowsys.co.kr/nwic-f0203wr.pdf` | `qr/QR_NWIC-F0203WR.png` |
| **NWIC-B0505WR** | AI Security Bullet Camera | `https://datasheet.nowsys.co.kr/nwic-b0505wr.pdf` | `qr/QR_NWIC-B0505WR.png` |
| **NWP-MS** | SMART Multi-Detector System | `https://datasheet.nowsys.co.kr/nwp-ms.pdf` | `qr/QR_NWP-MS.png` |

## 구조

```
/                     제품 목록 페이지 (index.html)
/<slug>.pdf           제품별 데이터시트 (QR 연결 대상)
/qr/QR_<모델명>.png   인쇄용 QR (1240px, 오류정정 H)
/qr/QR_<모델명>.svg   인쇄용 QR (벡터)
/CNAME                커스텀 도메인 설정
```

## 데이터시트 교체 방법

**PDF 파일명을 절대 바꾸지 마세요.** 파일명이 곧 QR 주소입니다.
같은 이름으로 덮어쓰고 commit + push 하면 1~2분 내 반영되며, 이미 인쇄된 QR도 그대로 동작합니다.

## DNS 설정 (최초 1회)

도메인 관리 사이트에서 아래 레코드를 추가하세요.

| 타입 | 호스트 | 값 |
|---|---|---|
| CNAME | `datasheet` | `now-system.github.io` |

이후 GitHub 저장소 → Settings → Pages 에서
Source `Deploy from a branch` / Branch `main` `/ (root)`,
Custom domain `datasheet.nowsys.co.kr`, **Enforce HTTPS** 체크.
