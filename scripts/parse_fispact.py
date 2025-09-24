#!/usr/bin/env python3
import json

OUT_JSON = 'fispact_outputs/material_A_plus.json'

def parse_json(path):
    with open(path) as f:
        j = json.load(f)
    dose_1d = None
    for entry in j.get('doses', []):
        if entry.get('cooling_time') in ('1 d', '1 day', '86400'):
            dose_1d = entry.get('contact_dose_uSv_per_h') or entry.get('contact_dose')
    nuclides = j.get('nuclide_inventory', {})
    print('DOSE_1D', dose_1d)
    print('NUCLIDES_SAMPLE', {k: nuclides.get(k) for k in ('Re','Os','Cr')})

if __name__ == '__main__':
    parse_json(OUT_JSON)
