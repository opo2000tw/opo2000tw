import json
import os
import sys

def main():
    json_path = sys.argv[1] if len(sys.argv) > 1 else "repos.json"
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found")
        sys.exit(1)

    with open(json_path, "r", encoding="utf-8") as f:
        repos = json.load(f)

    prod_repos = []
    agent_repos = []
    web_repos = []
    other_repos = []

    ignored_names = {"opo2000tw"}

    descriptions_override = {
        "nrf-command-line-factory": "工廠端 Nordic nRF52 韌體量產自動化燒錄與測試桌面程式（Go + SEGGER J-Link / nrfutil GUI/CLI）",
        "daemon": "輕量級背景常駐服務與行程守護工具（Go）",
        "baton": "Multi-agent dispatch governance for reliable AI delivery（多 Agent 派工治理框架）",
        "gstack": "Garry Tan 的 Claude Code 15 專屬工具鏈與角色分工套件",
        "huashu-design": "HTML-native design skill for Claude Code（高保真原型 / 幻燈片 / 動畫）",
        "spec-kit": "Spec-Driven Development（規格驅動開發）輔助工具套件",
        "devspace": "Turn ChatGPT into Codex",
        "waterhanspa": "水涵 SPA 官方形象網頁與預約前端應用（Vue.js）",
        "learn-docker-and-k8s": "互動式學習 Docker、Linux 與 Kubernetes 之 AI 驅動環境",
        "mini-taiwan-pulse": "台灣在地即時脈動視覺化與資訊前端",
        "squirrel": "【鼠鬚管】Rime Input Method Engine for Mac",
    }

    for r in repos:
        name = r.get("name", "")
        desc = descriptions_override.get(name, r.get("description") or "")
        is_archived = r.get("isArchived", False)
        is_fork = r.get("isFork", False)
        url = r.get("url", f"https://github.com/opo2000tw/{name}")

        if name in ignored_names or is_archived:
            continue

        item = {
            "name": name,
            "desc": desc,
            "url": url,
            "is_archived": is_archived,
            "is_fork": is_fork
        }

        name_lower = name.lower()
        if "factory" in name_lower or "daemon" in name_lower:
            prod_repos.append(item)
        elif "baton" in name_lower or "gstack" in name_lower or "huashu" in name_lower or "spec" in name_lower or "devspace" in name_lower or "docker" in name_lower:
            agent_repos.append(item)
        elif "spa" in name_lower or "pulse" in name_lower:
            web_repos.append(item)
        else:
            other_repos.append(item)

    prod_repos.sort(key=lambda x: x["name"])
    agent_repos.sort(key=lambda x: x["name"])
    web_repos.sort(key=lambda x: x["name"])
    other_repos.sort(key=lambda x: x["name"])

    lines = [
        "# Hi there, I'm Blake Wu (B-law) 👋",
        "",
        "嵌入式系統工程師（Embedded Firmware Engineer）與 Agentic AI 開發者。專注於 **ARM Cortex 嵌入式微控制器韌體開發**、**紅外熱成像與機器視覺系統**、**音訊 DSP / 串流傳輸** 以及 **AI Agent 自動化開發工具鏈**。",
        "",
        "---",
        "",
        "## 🏢 團隊與組織架構（Organization）",
        "",
        "我是 [**@opo200tw**](https://github.com/opo200tw) 組織的維護者與核心架構師。組織主要維護完整的產品韌體、原廠晶片 SDK 鏡像與感測器驅動體系：",
        "",
        "- 🦌 **[Animal Speaker（雙機式動物呼叫器）](https://github.com/opo200tw/UM-GPM4-AnimalSpeaker)**：凌通 GPM4 晶片雙機無線通訊與音訊播放產品韌體正本。",
        "- 📷 **[UM-GPM7-camera（智慧相機系統）](https://github.com/opo200tw/UM-GPM7-camera)**：GeneralPlus GPM7 平台之智慧相機主程式（熱成像 + TOF 雷射測距 + RTSP + TUTK P2P）。",
        "- 🩺 **[UM-ND52L15 系列（生醫與健康穿戴）](https://github.com/opo200tw/UM-ND52L15-EMDR)**：Nordic nRF52832（ND52L15）晶片之 EMDR 與 HeartMath 專案韌體。",
        "- 🔬 **[感測器與核心通訊模組](https://github.com/opo200tw)**：Heimann HTPAd 熱成像、Melexis MLX90640、ST VL53L4 TOF、Lock-Free RingBuffer、mbedTLS 加密庫。",
        "",
        "---",
        "",
        "## 🚀 精選開源專案（Featured Projects）",
        "",
        "### 🏭 嵌入式與產線工具（Embedded & Production Tools）"
    ]

    for r in prod_repos:
        lines.append(f"- [**{r['name']}**]({r['url']})：{r['desc']}")

    if agent_repos:
        lines.extend([
            "",
            "### 🤖 AI Agent 治理與開發工程（Agentic AI & Engineering Tools）"
        ])
        for r in agent_repos:
            lines.append(f"- [**{r['name']}**]({r['url']})：{r['desc']}")

    if web_repos:
        lines.extend([
            "",
            "### 🌐 網頁與應用專案（Web & Applications）"
        ])
        for r in web_repos:
            lines.append(f"- [**{r['name']}**]({r['url']})：{r['desc']}")

    if other_repos:
        lines.extend([
            "",
            "### 🛠️ 工具與系統組件（Tools & Utilities）"
        ])
        for r in other_repos:
            lines.append(f"- [**{r['name']}**]({r['url']})：{r['desc']}")

    lines.extend([
        "",
        "---",
        "",
        "## 🛠️ 技術棧與專業領域（Tech Stack & Core Skills）",
        "",
        "| 領域 | 技術 / 工具 / 協定 |",
        "| :--- | :--- |",
        "| **硬體晶片架構** | ARM Cortex-A7, ARM Cortex-M4, Nordic nRF52832, GeneralPlus GPM4 / GPM7 |",
        "| **嵌入式軟體與 OS** | FreeRTOS, CMSIS, Bare-metal, Bootloader, OTA Firmware Update |",
        "| **通訊協定與介面** | BLE 5.0, I2C, SPI, UART, USB CDC, RTSP, RTMP, WebRTC, TUTK P2P, TCP/IP (lwIP) |",
        "| **影像與感測系統** | Heimann HTPAd 60×40, MLX90640 32×24, VL53L4 TOF, OpenCV 鏡頭畸變校正 |",
        "| **程式語言** | C, C++, Go, Python, TypeScript / JavaScript, Vue.js, Shell Script |",
        "| **安全與演算法** | mbedTLS (SSL/TLS), Lock-Free SPSC RingBuffer, CRC32, AAC / G.711 Audio Codecs |",
        "| **AI 與工程自動化** | Agentic Coding Workflows, Multi-Agent Systems, GitHub Actions CI/CD, J-Link Flash Automation |",
        "",
        "---",
        "",
        "## 📫 聯絡與社群（Connect）",
        "",
        "- **GitHub 組織**: [https://github.com/opo200tw](https://github.com/opo200tw)",
        "- **個人 GitHub**: [https://github.com/opo2000tw](https://github.com/opo2000tw)",
        "- **Email**: `opo2000tw@mail.fcu.edu.tw`",
        "",
        "---",
        "",
        "## ⚙️ 自動同步機制（GitHub Actions Automation）",
        "",
        "本主頁目錄由 **GitHub Actions** 搭配 `generate_readme.py` 定期巡檢並自動同步維護。"
    ])

    lines.append("")
    output_content = "\n".join(lines)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(output_content)

    print("Generated README.md for opo2000tw successfully.")

if __name__ == "__main__":
    main()
