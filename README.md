# Autojool
Automated joolscan on python


# 🛡️ JoomScan Automation Bot

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Kali Linux](https://img.shields.io/badge/Kali-Linux-red.svg)
![Security](https://img.shields.io/badge/Security-Scanner-green.svg)

A powerful Python automation tool that enhances **OWASP JoomScan** to perform automated security assessments of Joomla websites. This bot processes multiple targets, filters results, and provides clean vulnerability reports.

## ✨ Features

- 🔄 **Automated Scanning** - Processes multiple websites from a text file
- 🎯 **Smart Filtering** - Shows only relevant vulnerabilities (hides XSS and Cross-Site Scripting)
- ⚡ **Critical Priority** - Highlights SQL Injection as critical vulnerabilities
- 📊 **Clean Reporting** - Beautiful table-formatted output
- ⏱️ **Time-Efficient** - Automated sequential scanning
- 🚫 **Noise Reduction** - Removes admin panel and unnecessary path information

## 📋 Requirements

### System Requirements
- **Kali Linux** (or any Linux with security tools)
- **Python 3.6+**
- **OWASP JoomScan**

### Installation

1. **Install JoomScan** (if not already installed):
```bash
sudo apt update
sudo apt install joomscan
```

2. **Or install from source**:
```bash
git clone https://github.com/OWASP/joomscan.git
cd joomscan
chmod +x joomscan.pl
sudo cp joomscan.pl /usr/local/bin/joomscan
```

3. **Clone this repository**:
```bash
git clone https://github.com/yourusername/joomscan-automation-bot.git
cd joomscan-automation-bot
```

## 🚀 Usage

### 1. Create targets file
Create a text file (`sites.txt`) with target URLs (one per line):
```bash
nano sites.txt
```

Example content:
```
https://example1.com
http://test-site.org
https://target-website.com
```

### 2. Run the scanner
```bash
python3 joomscan_bot.py sites.txt
```

### 3. View results
Results are saved in `scan_results.txt` with beautiful formatting:
```bash
cat scan_results.txt
```

## 📊 Sample Output

```
╔══════════════════════════════════════════════════════════════════════════════════╗
║ 🔍 Site: https://example.com                                                     ║
║ 🕒 Time: 2024-01-15 14:30:25                                                     ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║ 📋 Joomla version 3.4.5 identified                                               ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║ 🚨 VULNERABILITIES:                                                              ║
╠──────────────────────────────────────────────────────────────────────────────────╣
║ 🔴 CRITICAL: SQL Injection in com_content component                              ║
║ ⚪ NORMAL: Joomla! 1.5.x - Remote Admin Change Password                           ║
║ ⚪ NORMAL: CVE-2015-8562: Remote Code Execution                                   ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║ 💥 EXPLOITS:                                                                     ║
╠──────────────────────────────────────────────────────────────────────────────────╣
║ 📌 CRITICAL: SQL Injection in com_content component                              ║
║    🔗 Link:  EDB : https://www.exploit-db.com/exploits/12345/                    ║
║                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝
```

## 🎯 Vulnerability Classification

| Severity | Type | Description |
|----------|------|-------------|
| 🔴 **CRITICAL** | SQL Injection | Database manipulation vulnerabilities |
| ⚪ **NORMAL** | Other vulnerabilities | RCE, LFI, RFI, etc. |
| 🚫 **HIDDEN** | XSS/Cross-Site | intentionally filtered out |

## ⚙️ Configuration

The bot automatically filters out:
- ❌ XSS (Cross-Site Scripting) vulnerabilities
- ❌ Cross-Site related exploits
- ❌ Admin panel information
- ❌ Path enumeration results

## 📁 File Structure

```
joomscan-automation-bot/
├── joomscan_bot.py      # Main automation script
├── sites.txt            # Example targets file
├── scan_results.txt     # Generated results
└── README.md           # This file
```

## 🛡️ Legal Disclaimer

This tool is designed for **educational purposes** and **authorized security testing** only. 

⚠️ **WARNING**: 
- Use only on websites you own or have explicit permission to test
- Unauthorized scanning is illegal and unethical
- The developers are not responsible for misuse

## 🤝 Contributing

Feel free to contribute by:
1. Forking the repository
2. Creating a feature branch
3. Submitting a pull request
4. Reporting issues or suggestions

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **OWASP** for the amazing JoomScan tool
- **Kali Linux** team for the great security distribution
- **Python community** for excellent libraries

---

**Happy ethical hacking!** 🚀

*Remember: With great power comes great responsibility!* 🕷️

## 📞 Support

If you have any questions or issues:
1. Check the existing [Issues](../../issues)
2. Create a new Issue with detailed description
3. Provide your OS, Python version, and error messages

---

**⭐ If you find this useful, please give it a star! ⭐**
