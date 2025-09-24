# Material A+ — Computational Design Package

**Material:** `W-96.95 V-3.00 La2O3-0.05 ZrC-0.01 Y2O3-0.05 (wt%)`

**Status:** Parametric trend analysis (NOT VALIDATED). This repository contains all scripts and templates required to run physics-based validation tools (FISPACT-II for activation and TMAP7 for tritium retention). Experimental irradiation data is required to complete validation.

## Key goals
- Provide a clean, reproducible framework for trend analysis of Material A+.
- Integrate FISPACT-II and TMAP7 templates so reviewers or experimentalists can run physics-based validation.
- Present a clear, concise pitch so labs are motivated to test this composition.

## What to expect
- `simulations/material_A+_analysis/material_A+_physics_model.py`: parametric trend estimator (runs in CI).
- `fispact_inputs/` and `tmap_inputs/`: input templates for FISPACT-II and TMAP7.
- `scripts/`: run & parse scripts for tool integration.
- `docs/required_validation_steps.md`: exact instructions for FISPACT-II and TMAP7 runs.

## Quick start (developer)
1. Clone the repo.
2. Install Python deps: `pip install -r requirements.txt` (or `numpy scipy matplotlib pyyaml`).
3. Run the trend estimator:

```bash
cd simulations/material_A+_analysis
python material_A+_physics_model.py 
