

🛡️ Autojool - Joomla Security Automation Bot

https://img.shields.io/badge/Python-3.6%2B-blue https://img.shields.io/badge/Kali-Linux-red https://img.shields.io/badge/Security-Scanner-green https://img.shields.io/badge/Automation-Enabled-success https://img.shields.io/badge/License-MIT-yellow

A powerful Python automation tool by versch-pozzi that enhances OWASP JoomScan for automated security assessments of Joomla websites.

✨ Features

· 🔄 Automated Scanning - Processes multiple websites automatically
· 🎯 Smart Filtering - Shows relevant vulnerabilities (hides XSS)
· ⚡ Critical Priority - Highlights SQL Injection as critical
· 📊 Clean Reporting - Beautiful table-formatted output
· ⏱️ Time-Efficient - Automated sequential scanning

📦 Quick Installation

```bash
# Clone the repository
git clone https://github.com/versch-pozzi/Autojool.git
cd Autojool

# Make scripts executable
chmod +x install_requirements.sh quick_start.sh main.py

# Install requirements
./install_requirements.sh
```

🚀 Usage

1. Configure Targets

```bash
nano sites.txt
```

Add your target URLs:

```txt
https://example.com
http://test-site.org
https://target-website.com
```

2. Run Scanning

```bash
# Quick start
./quick_start.sh

# Or directly
python3 main.py sites.txt
```

3. View Results

```bash
cat scan_results.txt
```

📁 Project Structure

```
Autojool/
├── 📄 main.py                 # Main automation script
├── ⚙️ install_requirements.sh # Automatic installation
├── 🚀 quick_start.sh          # Quick launch script
├── 📋 requirements.txt        # Python dependencies
├── 🎯 sites.txt              # Target websites file
├── 📊 scan_results.txt       # Generated results
└── 📖 README.md              # Documentation
```

🎯 Vulnerability Classification

Severity Type Emoji
🔴 CRITICAL SQL Injection 🔴
⚪ NORMAL Other vulnerabilities ⚪
🚫 HIDDEN XSS/Cross-Site 🚫

🔧 Troubleshooting

Permission Issues:

```bash
chmod +x *.sh *.py
```

JoomScan Not Found:

```bash
sudo apt install joomscan
```

🛡️ Legal Disclaimer

For educational and authorized testing only! ⚠️

· Use only on websites you own or have permission to test
· Unauthorized scanning is illegal
· Developer not responsible for misuse

📄 License

MIT License - see LICENSE file for details.

---

🚀 Quick Commands

```bash
# Full setup
git clone https://github.com/versch-pozzi/Autojool.git
cd Autojool
chmod +x *.sh *.py
./install_requirements.sh
nano sites.txt
./quick_start.sh
cat scan_results.txt
```

---

⭐ If you find this useful, please give it a star! ⭐

Happy ethical hacking! 🚀

By versch-pozzi 🎯

---

https://img.shields.io/badge/GitHub-vorsch--pozzi-black https://img.shields.io/badge/Tools-JoomScan%20%2B%20Python-orange https://img.shields.io/badge/Status-Active-brightgreen
