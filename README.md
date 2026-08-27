# Hi there, I'm Blake Wu (B-law) 👋

嵌入式系統工程師（Embedded Firmware Engineer）。專注於 **ARM Cortex 微控制器韌體開發**、**紅外熱成像與機器視覺系統**、**音訊 DSP / 串流傳輸** 以及 **工廠量產自動化工具鏈**。

---

## 🏢 核心架構與研發專案（Core Projects @ opo200tw）

> *註：主要商業產品韌體與系統架構均託管於 [**@opo200tw**](https://github.com/opo200tw) 組織（核心代碼為 Private 私有保護，對外展示架構與技術棧）*

- 🦌 **[UM-GPM4-AnimalSpeaker](https://github.com/opo200tw/UM-GPM4-AnimalSpeaker)**：凌通 GPM4 晶片雙機無線通訊與音訊播放產品韌體正本（HandUnit + Speaker + Bootloader + BLE）。
- 📷 **[UM-GPM7-camera](https://github.com/opo200tw/UM-GPM7-camera)**：GeneralPlus GPM7 平台之智慧相機主程式韌體（熱成像 + TOF 雷射測距 + RTSP + TUTK P2P）。
- 🩺 **[UM-ND52L15 系列](https://github.com/opo200tw/UM-ND52L15-EMDR)**：Nordic nRF52832（ND52L15）晶片之生醫穿戴與健康監測專案韌體（EMDR & HeartMath）。
- 🏭 **[nrf-command-line-factory](https://github.com/opo200tw/nrf-command-line-factory)**：Nordic nRF52 晶片工廠端量產自動化燒錄與測試桌面程式（Go + J-Link / nrfutil GUI/CLI）。
- 🛠️ **[agents-serial-term](https://github.com/opo200tw/agents-serial-term)**：跨平台高速序列埠除錯終端（TUI + Headless，支援 FTDI / CDC 設備）。
- 🔬 **[感測器與核心模組](https://github.com/opo200tw)**：Heimann HTPAd 熱成像、Melexis MLX90640、ST VL53L4 TOF、Lock-Free RingBuffer、mbedTLS 加密庫。

---

## 🚀 個人原創專案（Personal Projects）

- [**daemon**](https://github.com/opo2000tw/daemon)：輕量級背景常駐服務與行程守護工具（Go）
- [**waterhanspa**](https://github.com/opo2000tw/waterhanspa)：水涵 SPA 官方形象網頁與預約前端應用（Vue.js）

---

## 🛠️ 技術棧與專業領域（Tech Stack & Core Skills）

| 領域 | 技術 / 工具 / 協定 |
| :--- | :--- |
| **硬體晶片架構** | ARM Cortex-A7, ARM Cortex-M4, Nordic nRF52832, GeneralPlus GPM4 / GPM7 |
| **嵌入式軟體與 OS** | FreeRTOS, CMSIS, Bare-metal, Bootloader, OTA Firmware Update |
| **通訊協定與介面** | BLE 5.0, I2C, SPI, UART, USB CDC, RTSP, RTMP, WebRTC, TUTK P2P, TCP/IP (lwIP) |
| **影像與感測系統** | Heimann HTPAd 60×40, MLX90640 32×24, VL53L4 TOF, OpenCV 鏡頭畸變校正 |
| **程式語言** | C, C++, Go, Python, TypeScript / JavaScript, Vue.js, Shell Script |
| **安全與演算法** | mbedTLS (SSL/TLS), Lock-Free SPSC RingBuffer, CRC32, AAC / G.711 Audio Codecs |
| **產線與工程工具** | SEGGER J-Link Automated Flashing, FTDI / CDC USB Serial, CI/CD Actions |

---

## 📫 聯絡方式（Contact）

- **GitHub 組織**: [https://github.com/opo200tw](https://github.com/opo200tw)
- **個人 GitHub**: [https://github.com/opo2000tw](https://github.com/opo2000tw)
- **Email**: `opo2000tw@gmail.com`

---

## ⚙️ 自動同步機制（GitHub Actions Automation）

本主頁目錄由 **GitHub Actions** 搭配 `generate_readme.py` 定期巡檢並自動排除外部 Fork，僅同步個人原創專案。
