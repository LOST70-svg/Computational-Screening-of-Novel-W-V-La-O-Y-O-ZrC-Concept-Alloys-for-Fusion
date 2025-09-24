#!/usr/bin/env bash
set -euo pipefail
INPUT_DIR="$(pwd)/fispact_inputs"
OUTPUT_DIR="$(pwd)/fispact_outputs"
mkdir -p "$OUTPUT_DIR"

docker run --rm -v "$INPUT_DIR":/inputs -v "$OUTPUT_DIR":/outputs fispact/ubuntu:latest \
  /bin/bash -lc "cd /inputs && fispact -i material_A_plus.fis -o /outputs/material_A_plus.out --json /outputs/material_A_plus.json"
