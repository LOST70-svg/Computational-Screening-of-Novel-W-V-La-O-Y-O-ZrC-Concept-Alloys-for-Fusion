#!/usr/bin/env python3
import re
OUT = 'tmap_outputs/material_A_plus_tmap.out'

def parse_tmap(path):
    with open(path) as f:
        text = f.read()
    m = re.search(r"TOTAL\s+RETENTION\s*=\s*([0-9Ee.+-]+)", text)
    if m:
        return float(m.group(1))
    nums = re.findall(r"RETENTION\s*[:=]\s*([0-9Ee.+-]+)", text)
    if nums:
        return float(nums[-1])
    raise RuntimeError('Could not find retention in TMAP output')

if __name__ == '__main__':
    print('T_RET', parse_tmap(OUT))
