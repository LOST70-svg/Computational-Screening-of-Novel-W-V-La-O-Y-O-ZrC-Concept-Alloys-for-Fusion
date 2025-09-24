# Required Validation Steps (FISPACT-II & TMAP7)

1. Populate `fispact_inputs/material_A_plus.fis` with a validated ITER neutron spectrum for the component location.
2. Run the `scripts/run_fispact.sh` script (Docker). This produces JSON/text outputs in `fispact_outputs/`.
3. Parse the outputs with `scripts/parse_fispact.py`.
4. Build or obtain TMAP7 and run `scripts/run_tmap7.sh` to produce `tmap_outputs/`.
5. Parse TMAP7 outputs with `scripts/parse_tmap7.py`.
6. Run `scripts/aggregate_results.py` to combine results and check ITER thresholds.

> Note: FISPACT requires nuclear data libraries (TENDL/JEFF/ENDF). Use official FISPACT images that bundle data or follow the FISPACT manual to download data.
