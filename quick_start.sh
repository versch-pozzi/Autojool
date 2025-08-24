#!/bin/bash

# Quick Start Script for JoomScan Automation Bot

echo "🚀 JoomScan Automation Bot - Quick Start"
echo "────────────────────────────────────────────────────────────────"

# Check if virtual environment exists
if [ ! -d "joomscan-env" ]; then
    echo "❌ Virtual environment not found. Please run install_requirements.sh first"
    exit 1
fi

# Activate virtual environment
source joomscan-env/bin/activate

# Check if sites.txt has actual targets
if grep -q "^[^#]" sites.txt; then
    echo "✅ Found targets in sites.txt"
    echo "📋 Targets:"
    grep "^[^#]" sites.txt | sed 's/^/   /'
else
    echo "⚠️  No active targets found in sites.txt"
    echo "   Please edit sites.txt and uncomment target URLs"
    exit 1
fi

echo ""
echo "🏃 Starting JoomScan Automation Bot..."
echo "────────────────────────────────────────────────────────────────"

# Run the bot
python3 joomscan_bot.py sites.txt

echo ""
echo "✅ Scan completed! Results saved to scan_results.txt"
echo "📊 View results: cat scan_results.txt"
