#!/bin/bash
set -e

# Install pdoc if not available
pip show pdoc > /dev/null 2>&1 || pip install pdoc

# Create documentation directory
mkdir -p ../docs/code

# Generate documentation from src
pdoc ../src --html --output-dir ../docs/code --force

echo "Documentation generated in docs/code/"
