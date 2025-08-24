#!/bin/bash

# 🛡️ JoomScan Automation Bot - Installation Script
# 📋 This script installs all requirements for the JoomScan Automation Bot

echo "🛡️  JoomScan Automation Bot - Installation Script"
echo "══════════════════════════════════════════════════════════════════════════════════"

# Check if running as root
if [ "$EUID" -eq 0 ]; then
    echo "❌ Please do not run this script as root/sudo"
    exit 1
fi

echo "🔍 Checking system requirements..."

# Check if Kali Linux
if grep -q "Kali" /etc/os-release; then
    echo "✅ Kali Linux detected"
else
    echo "⚠️  Warning: This script is optimized for Kali Linux"
    echo "   Other distributions might require manual adjustments"
fi

# Check Python
if command -v python3 &> /dev/null; then
    echo "✅ Python3 is installed: $(python3 --version)"
else
    echo "❌ Python3 is not installed. Installing..."
    sudo apt update
    sudo apt install -y python3 python3-pip
fi

# Check PIP
if command -v pip3 &> /dev/null; then
    echo "✅ pip3 is installed: $(pip3 --version)"
else
    echo "❌ pip3 is not installed. Installing..."
    sudo apt install -y python3-pip
fi

echo ""
echo "📦 Installing JoomScan..."
echo "──────────────────────────────────────────────────────────────────────────────────"

# Check if JoomScan is already installed
if command -v joomscan &> /dev/null; then
    echo "✅ JoomScan is already installed: $(joomscan --version | head -n1)"
else
    echo "📥 Installing JoomScan from Kali repositories..."
    sudo apt update
    sudo apt install -y joomscan
    
    # Verify installation
    if command -v joomscan &> /dev/null; then
        echo "✅ JoomScan installed successfully: $(joomscan --version | head -n1)"
    else
        echo "❌ JoomScan installation failed. Trying alternative installation..."
        
        # Alternative installation from source
        echo "📥 Installing JoomScan from GitHub source..."
        sudo apt install -y git perl
        git clone https://github.com/OWASP/joomscan.git
        cd joomscan
        chmod +x joomscan.pl
        sudo cp joomscan.pl /usr/local/bin/joomscan
        cd ..
        
        if command -v joomscan &> /dev/null; then
            echo "✅ JoomScan installed from source successfully"
        else
            echo "❌ JoomScan installation failed. Please install manually:"
            echo "   sudo apt install joomscan"
            echo "   OR"
            echo "   git clone https://github.com/OWASP/joomscan.git"
            echo "   cd joomscan && chmod +x joomscan.pl"
            echo "   sudo cp joomscan.pl /usr/local/bin/joomscan"
            exit 1
        fi
    fi
fi

echo ""
echo "🐍 Installing Python dependencies..."
echo "──────────────────────────────────────────────────────────────────────────────────"

# Create virtual environment (optional but recommended)
echo "📁 Creating Python virtual environment..."
python3 -m venv joomscan-env
source joomscan-env/bin/activate

# Install Python requirements
echo "📦 Installing Python packages..."
pip3 install --upgrade pip

# Create requirements.txt if it doesn't exist
if [ ! -f requirements.txt ]; then
    cat > requirements.txt << EOL
# JoomScan Automation Bot Requirements
# No additional Python packages needed beyond standard library
# This file is kept for future compatibility

# Standard library imports used:
# - subprocess
# - sys
# - os
# - re
# - time
# - datetime
EOL
fi

pip3 install -r requirements.txt

echo ""
echo "🔧 Setting up the bot..."
echo "──────────────────────────────────────────────────────────────────────────────────"

# Make the main script executable
if [ -f "joomscan_bot.py" ]; then
    chmod +x joomscan_bot.py
    echo "✅ Made joomscan_bot.py executable"
else
    echo "⚠️  Main script joomscan_bot.py not found in current directory"
fi

# Create example sites file
if [ ! -f "sites.txt" ]; then
    cat > sites.txt << EOL
# 🎯 Add your target websites here (one per line)
# Example:
# https://example.com
# http://test-site.org
# https://target-website.com

# Remove the '#' before URLs to activate them
EOL
    echo "✅ Created example sites.txt file"
fi

echo ""
echo "✅ Installation completed successfully!"
echo "══════════════════════════════════════════════════════════════════════════════════"

# Display usage instructions
cat << EOL

🚀 How to use:
─────────────

1. 📝 Edit sites.txt with your target URLs:
   nano sites.txt

2. 🏃 Run the bot:
   python3 joomscan_bot.py sites.txt

3. 📊 View results:
   cat scan_results.txt

🎯 Quick test:
─────────────
python3 joomscan_bot.py sites.txt

📖 For more details, check the README.md file

EOL

echo "💡 Tip: You can activate the virtual environment anytime with:"
echo "      source joomscan-env/bin/activate"
echo ""
echo "🛡️  Happy ethical hacking! Remember to only scan websites you own or have permission to test."
