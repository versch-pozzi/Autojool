

🛡️ Autojool - Joomla Security Automation Bot

https://img.shields.io/badge/Python-3.6+-blue.svg
 https://img.shields.io/badge/Kali-Linux-red.svg https://img.shields.io/badge/Security-Scanner-green.svg https://img.shields.io/badge/Automation-Enabled-success.svg

A powerful Python automation tool by versch-pozzi that enhances OWASP JoomScan for automated security assessments of Joomla websites. Processes multiple targets, filters results, and provides clean vulnerability reports.

✨ Features

· 🔄 Automated Scanning - Processes multiple websites automatically
· 🎯 Smart Filtering - Shows relevant vulnerabilities (hides XSS)
· ⚡ Critical Priority - Highlights SQL Injection as critical
· 📊 Clean Reporting - Beautiful table-formatted output
· ⏱️ Time-Efficient - Automated sequential scanning
· 🚫 Noise Reduction - Removes unnecessary information
· 🐍 Easy Setup - One-command installation
· 🚀 Quick Start - Simple launch system

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

⚙️ Configuration

The bot automatically filters out:

· ❌ XSS vulnerabilities
· ❌ Cross-Site exploits
· ❌ Admin panel information
· ❌ Path enumeration results

🔧 Troubleshooting

Permission Issues:

```bash
chmod +x *.sh *.py
```

JoomScan Not Found:

```bash
sudo apt install joomscan
```

Python Issues:

```bash
sudo apt install python3 python3-pip
```

🛡️ Legal Disclaimer

For educational and authorized testing only! ⚠️

· Use only on websites you own or have permission to test
· Unauthorized scanning is illegal
· Developer not responsible for misuse

🤝 Contributing

Feel free to contribute! Fork → Branch → PR → Issue

📄 License

MIT License - see LICENSE file for details.

🙏 Acknowledgments

· OWASP for JoomScan
· Kali Linux team
· Python community

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
