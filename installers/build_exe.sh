#!/bin/bash
set -e

# Install pyinstaller if not present
pip show pyinstaller > /dev/null 2>&1 || pip install pyinstaller

# Create standalone Windows executable
pyinstaller --onefile --name "SentinelOps" ../../src/main.py

echo "Executable created in dist/SentinelOps.exe"
