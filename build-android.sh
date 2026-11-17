#!/usr/bin/env bash
set -euo pipefail
python -m pip install --upgrade pip setuptools wheel
python -m pip install buildozer cython==0.29.34
buildozer -v android debug
