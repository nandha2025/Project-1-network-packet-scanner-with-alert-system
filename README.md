# 🚀 Network Packet Sniffer & Alert System

<div align="center">
  <img src="banner.png" width="800"/>
  <br><br>
  
  <img alt="Python" src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img alt="Scapy" src="https://img.shields.io/badge/Scapy-2.5%2B-FF6B35?style=for-the-badge&logo=data:image/svg+xml;base64,..."/>
  <img alt="Linux" src="https://img.shields.io/badge/Linux-Kali%2FUbuntu-512DA8?style=for-the-badge&logo=linux&logoColor=white"/>
  <img alt="License" src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=data:image/svg+xml;base64,..."/>
</div>

## 🎯 Features at a Glance

| Feature | Status |
|---------|--------|
| 🔴 Live Packet Capture | ✅ Ready |
| 📊 Real-time Stats | ✅ Ready |
| 🚨 Smart Alerts | ✅ Ready |
| 💾 PCAP Export | ✅ Ready |
| 🎨 GUI Dashboard | ✅ Ready |
| 🔧 CLI Mode | ✅ Ready |

## ⚡ Quick Start (Copy-Paste Ready)

```bash
# 1. Clone & Install
git clone https://github.com/YOUR_USERNAME/packet-sniffer-alert.git
cd packet-sniffer-alert
pip install -r requirements.txt

# 2. Run (Linux/Kali)
sudo python3 sniffer.py --interface eth0 --alerts

# 3. GUI Mode
sudo python3 gui_sniffer.py
# Basic sniffing
sudo python3 sniffer.py --interface wlan0

# HTTP traffic only
sudo python3 sniffer.py --filter "tcp port 80 or 443"

# Full alerts + PCAP save
sudo python3 sniffer.py --alerts --pcap --max_pps 1000
🔴 HIGH: Port Scan Detected (192.168.1.100 → 50 ports)
🟡 WARN: Flood Attack (1000+ PPS from 8.8.8.8)
🔴 CRITICAL: ARP Spoofing (Duplicate MAC detected)
🟡 INFO: Suspicious DNS Query Flood
📁 packet-sniffer-alert/
├── 📄 README.md                 # ← You're reading it!
├── 📦 requirements.txt
├── 🚀 sniffer.py                # Main CLI
├── 🎨 gui_sniffer.py           # GUI Dashboard
├── ⚙️  config.py               # Settings
├── 📊 utils/
│   ├── packet_analyzer.py
│   ├── alert_engine.py
│   └── stats_collector.py
└── 💾 captures/               # PCAP files
┌─────────────────────────────────────────────────────────────┐
│ Network Packet Sniffer v2.0 | Interface: eth0 | 2.3 Mbps    │
├─────────────────────────────────────────────────────────────┤
│ Packets: 12,456 | Hosts: 15 | Alerts: 2 🚨                   │
│ TOP: 192.168.1.10(45%) 8.8.8.8(30%) 1.1.1.1(15%)          │
│ ALERT: Port scan from 192.168.1.100 → ports 22,80,443 🔴    │
└─────────────────────────────────────────────────────────────┘
git clone https://github.com/YOUR_USERNAME/packet-sniffer-alert.git
# Make changes, then:
git checkout -b feature/new-alert-rule
git commit -m "Add DNS flood detection"
git push origin feature/new-alert-rule
MIT License - Free for ethical hacking, cybersecurity education, 
and research purposes only. Not for malicious use.
