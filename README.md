
# 🛡️ JoomScan Automation Bot

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Kali Linux](https://img.shields.io/badge/Kali-Linux-red.svg)
![Security](https://img.shields.io/badge/Security-Scanner-green.svg)
![Automation](https://img.shields.io/badge/Automation-Enabled-success.svg)

A powerful Python automation tool that enhances **OWASP JoomScan** to perform automated security assessments of Joomla websites. This bot processes multiple targets, filters results, and provides clean vulnerability reports with critical priority highlighting.

## ✨ Features

- 🔄 **Automated Scanning** - Processes multiple websites from a text file automatically
- 🎯 **Smart Filtering** - Shows only relevant vulnerabilities (hides XSS and Cross-Site Scripting)
- ⚡ **Critical Priority** - Highlights SQL Injection as critical vulnerabilities
- 📊 **Clean Reporting** - Beautiful table-formatted output
- ⏱️ **Time-Efficient** - Automated sequential scanning
- 🚫 **Noise Reduction** - Removes admin panel and unnecessary path information
- 🐍 **Easy Setup** - One-command installation script
- 🚀 **Quick Start** - Simple launch script included

## 📦 Installation

### Quick Installation (Recommended)

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/joomscan-automation-bot.git
cd joomscan-automation-bot
```

2. **Run the installation script**:
```bash
chmod +x install_requirements.sh
./install_requirements.sh
```

### Manual Installation

If you prefer manual setup:

1. **Install JoomScan**:
```bash
sudo apt update
sudo apt install joomscan
```

2. **Verify Python 3.6+ is installed**:
```bash
python3 --version
```

3. **Make scripts executable**:
```bash
chmod +x joomscan_bot.py quick_start.sh
```

## 🗂️ Project Structure

```
joomscan-automation-bot/
├── 📄 joomscan_bot.py          # Main automation script
├── ⚙️ install_requirements.sh   # Automatic installation script
├── 🚀 quick_start.sh           # Quick launch script
├── 📋 requirements.txt         # Python dependencies
├── 🎯 sites.txt               # Target websites file (example)
├── 📊 scan_results.txt        # Generated results file
└── 📖 README.md               # This documentation
```

## 📋 File Descriptions

### `install_requirements.sh`
**Purpose**: Automated installation of all dependencies  
**Features**:
- Checks system requirements
- Installs JoomScan (from repo or source)
- Sets up Python virtual environment
- Creates example configuration files
- Makes scripts executable

### `quick_start.sh` 
**Purpose**: One-command launch of the scanning process  
**Features**:
- Activates virtual environment
- Validates target list
- Runs the scanner
- Provides completion status

### `requirements.txt`
**Purpose**: Python package dependencies  
**Note**: Uses only Python standard library - no external packages required

### `sites.txt`
**Purpose**: Target websites list (one URL per line)  
**Format**: Remove `#` to activate target URLs

## 🚀 Usage

### Method 1: Quick Start (Recommended)
```bash
./quick_start.sh
```

### Method 2: Manual Execution
```bash
# Edit targets file first
nano sites.txt

# Run the scanner
python3 joomscan_bot.py sites.txt

# View results
cat scan_results.txt
```

### Method 3: Using Virtual Environment
```bash
# Activate virtual environment
source joomscan-env/bin/activate

# Run scanner
python3 joomscan_bot.py sites.txt

# Deactivate when done
deactivate
```

## 🎯 Preparing Targets

Edit `sites.txt` with your target URLs:

```bash
nano sites.txt
```

Example content:
```txt
# 🎯 Target websites (remove '#' to activate)
https://example1.com
http://test-site.org
# https://another-site.com
https://target-website.com
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

| Severity | Type | Description | Emoji |
|----------|------|-------------|-------|
| 🔴 **CRITICAL** | SQL Injection | Database manipulation vulnerabilities | 🔴 |
| ⚪ **NORMAL** | Other vulnerabilities | RCE, LFI, RFI, etc. | ⚪ |
| 🚫 **HIDDEN** | XSS/Cross-Site | Intentionally filtered out | 🚫 |

## ⚙️ Configuration

The bot automatically filters out:
- ❌ XSS (Cross-Site Scripting) vulnerabilities
- ❌ Cross-Site related exploits  
- ❌ Admin panel information
- ❌ Path enumeration results

## 🔧 Troubleshooting

### Common Issues:

1. **JoomScan not found**:
   ```bash
   sudo apt install joomscan
   ```

2. **Permission denied**:
   ```bash
   chmod +x *.sh
   chmod +x joomscan_bot.py
   ```

3. **No targets found**:
   ```bash
   nano sites.txt  # Uncomment target URLs
   ```

4. **Python not installed**:
   ```bash
   sudo apt install python3 python3-pip
   ```

## 🛡️ Legal Disclaimer

This tool is designed for **educational purposes** and **authorized security testing** only. 

⚠️ **WARNING**: 
- Use only on websites you own or have explicit permission to test
- Unauthorized scanning is illegal and unethical
- The developers are not responsible for misuse

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request
4. Report issues or suggestions

## 📄 License

MIT License - see LICENSE file for details.

## 🙏 Acknowledgments

- **OWASP** for the amazing JoomScan tool
- **Kali Linux** team for the great security distribution  
- **Python community** for excellent libraries

---

## 🚀 Quick Start Guide

### For First-Time Users:

1. **Clone and setup**:
   ```bash
   git clone https://github.com/versch-pozzi/joomscan-automation-bot.git
   cd joomscan-automation-bot
   ./install_requirements.sh
   ```

2. **Configure targets**:
   ```bash
   nano sites.txt  # Add your target URLs
   ```

3. **Run scanning**:
   ```bash
   ./quick_start.sh
   ```

4. **View results**:
   ```bash
   cat scan_results.txt
   ```

---

**⭐ If you find this useful, please give it a star! ⭐**

**Happy ethical hacking!** 🚀

*Remember: With great power comes great responsibility!* 🕷️
