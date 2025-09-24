#!/usr/bin/env python3
import json

def load_fispact():
    with open('fispact_outputs/material_A_plus.json') as f:
        j = json.load(f)
    dose_1d = None
    for d in j.get('doses', []):
        if d.get('cooling_time') in ('1 d','1 day','86400'):
            dose_1d = d.get('contact_dose_uSv_per_h') or d.get('contact_dose')
    nuclide = j.get('nuclide_inventory', {})
    return dose_1d, nuclide

def load_tmap():
    with open('tmap_outputs/material_A_plus_tmap.out') as f:
        txt = f.read()
    import re
    m = re.search(r"TOTAL\s+RETENTION\s*=\s*([0-9Ee.+-]+)", txt)
    if m:
        return float(m.group(1))
    return None

if __name__ == '__main__':
    dose, nucl = load_fispact()
    t_ret = load_tmap()
    report = {
        'dose_1d_uSv_h': dose,
        'tritium_ret_T_m2': t_ret,
        'Re_mass': nucl.get('Re', {}).get('mass_wt') if isinstance(nucl, dict) else None,
        'iter_dose_limit_uSv_h': 100.0,
        'iter_tritium_limit_T_m2': 2.0e16,
        'dose_pass': dose is not None and dose < 100.0,
        'tritium_pass': t_ret is not None and t_ret < 2.0e16
    }
    print(json.dumps(report, indent=2))
