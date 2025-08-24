

🛡️ Autojool - Joomla Security Automation Bot

![Python 3.6+](https://img.shields.io/badge/Python-3.6%2B-blue)
![Kali Linux](https://img.shields.io/badge/Kali-Linux-red)
![Security Scanner](https://img.shields.io/badge/Security-Scanner-green)
![Automation Enabled](https://img.shields.io/badge/Automation-Enabled-success)
![License MIT](https://img.shields.io/badge/License-MIT-yellow)


Powerful Python automation tool by versch-pozzi for automated Joomla security assessments.

✨ Features

· 🔄 Automated Scanning - Multiple websites processing
· 🎯 Smart Filtering - Relevant vulnerabilities only (no XSS)
· ⚡ Critical Priority - SQL Injection highlighted as critical
· 📊 Clean Reporting - Beautiful table-formatted output
· ⏱️ Time-Efficient - Sequential automated scanning

📦 Installation

```bash
# Clone repository
git clone https://github.com/versch-pozzi/Autojool.git
cd Autojool

# Install requirements
sudo apt update
sudo apt install -y joomscan python3 python3-pip
```

🚀 Usage

1. Configure Target Websites

```bash
# Edit targets file
nano sites.txt
```

Example sites.txt:

```txt
https://example.com
http://test-site.org
https://target-website.com
```

2. Run Security Scan

```bash
# Execute main script
python3 main.py sites.txt
```

3. View Results

```bash
# Check scan results
cat scan_results.txt

# Or view with pagination
less scan_results.txt
```

📁 Project Structure

```
Autojool/
├── main.py              # Main automation script
├── sites.txt           # Target websites list
├── scan_results.txt    # Generated results
└── README.md          # Documentation
```

🎯 Vulnerability Classification

Level Type Description
🔴 CRITICAL SQL Injection Database vulnerabilities
⚪ NORMAL Other RCE, LFI, RFI, etc.
🚫 HIDDEN XSS Filtered out

⚙️ Automatic Filtering

Removed from reports:

· ❌ XSS vulnerabilities
· ❌ Cross-Site scripting
· ❌ Admin panel information
· ❌ Path enumeration data

🔧 Setup Commands

Basic Setup:

```bash
git clone https://github.com/versch-pozzi/Autojool.git
cd Autojool
sudo apt install joomscan python3
```

Edit Targets:

```bash
nano sites.txt
```

Run Scan:

```bash
python3 main.py sites.txt
```

Check Results:

```bash
cat scan_results.txt
```

🛡️ Legal Disclaimer

FOR EDUCATIONAL USE ONLY ⚠️

· Use only on websites you own
· Get proper authorization before scanning
· Unauthorized access is illegal
· Developer not responsible for misuse

📄 License

MIT License - see LICENSE file for details.

---

🚀 Quick Start Guide

```bash
# 1. Clone and enter
git clone https://github.com/versch-pozzi/Autojool.git
cd Autojool

# 2. Install tools
sudo apt install joomscan python3

# 3. Configure targets
nano sites.txt

# 4. Run scan
python3 main.py sites.txt

# 5. View results
cat scan_results.txt
```

---

⭐ If this tool helps you, please give it a star! ⭐

Happy ethical security testing! 🚀

Created by versch-pozzi 🎯

---

---

[![GitHub versch-pozzi](https://img.shields.io/badge/GitHub-versch--pozzi-black)](https://github.com/versch-pozzi/Autojool)
[![Status: Working](https://img.shields.io/badge/Status-Working-brightgreen)]()
[![Platform: Kali Linux](https://img.shields.io/badge/Platform-Kali%20Linux-purple)]()
