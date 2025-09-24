#!/usr/bin/env bash
set -euo pipefail
INPUT_DIR="$(pwd)/tmap_inputs"
OUTPUT_DIR="$(pwd)/tmap_outputs"
mkdir -p "$OUTPUT_DIR"

if [ -z "${TMAP7_BIN:-}" ]; then
  echo "TMAP7 binary not set. Please install TMAP7 and set TMAP7_BIN env var."
  exit 1
fi

"$TMAP7_BIN" -i "$INPUT_DIR/material_A_plus.inp" -o "$OUTPUT_DIR/material_A_plus_tmap.out"
