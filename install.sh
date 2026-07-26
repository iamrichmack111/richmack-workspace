#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .

echo
echo "✅ Richmack Workspace installed in .venv"
echo "Run:"
echo "  source .venv/bin/activate"
echo "  richmack"
