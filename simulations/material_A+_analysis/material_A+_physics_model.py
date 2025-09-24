"""
Material A+ Degradation Trends (PARAMETRIC ESTIMATOR)

WARNING: This is a parametric trend estimator ONLY. REAL validation requires
FISPACT-II (activation), TMAP7 (tritium), and irradiation experiments.
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import yaml
import os

# Load parameters
with open('params.yml', 'r') as f:
    params = yaml.safe_load(f)

ITER = {
    'SWELL_LIMIT': 1.0,       # %
    'TRITIUM_LIMIT': 2.0e16,  # T/m^2
    'DOSE_LIMIT': 100.0,      # µSv/h
    'K_IC_MIN': 10.0,         # MPa*sqrt(m)
    'MAX_DPA': 10.0
}


def degradation_model(t, y, dpa_max=ITER['MAX_DPA']):
    swell, K_IC, T_ret, dose = y
    dpa = (t / (365*24*3600)) * dpa_max

    d_swell_dt = params['swelling']['coefficient'] * (dpa + 1e-9)**params['swelling']['exponent']
    d_K_IC_dt = -params['toughness']['degradation_rate'] * (K_IC - params['toughness']['min_value'])

    T_sat = params['tritium']['saturation']
    uptake_rate = params['tritium']['uptake_rate']
    release_rate = params['tritium']['base_release'] * (1 + params['tritium']['dpa_factor'] * dpa)
    d_T_ret_dt = uptake_rate - release_rate * T_ret

    dose_growth = params['dose']['base_growth'] * (dpa / dpa_max)**params['dose']['exponent']

    return [d_swell_dt, d_K_IC_dt, d_T_ret_dt, dose_growth]


if __name__ == '__main__':
    y0 = [
        params['initial']['swelling'],
        params['initial']['K_IC'],
        params['initial']['T_ret'],
        params['initial']['dose']
    ]

    t_span = [0, 365*24*3600*10]
    sol = solve_ivp(degradation_model, t_span, y0, t_eval=np.linspace(0, t_span[1], 300), method='LSODA')

    results = np.column_stack([
        sol.t / (365*24*3600),
        sol.y.T,
        np.full(len(sol.t), ITER['MAX_DPA']) * (sol.t / t_span[1])
    ])
    os.makedirs('assets', exist_ok=True)
    np.savetxt('assets/material_A+_results.txt', results,
               header='time_yr swelling_% K_IC_MPa_sqrtm T_ret_T_m2 dose_uSv_h dpa', fmt='%.6f')

    # Plots
    t_years = results[:, 0]
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    plt.plot(t_years, results[:, 1], lw=2)
    plt.axhline(ITER['SWELL_LIMIT'], ls='--')
    plt.ylabel('Swelling (%)')

    plt.subplot(2, 2, 2)
    plt.plot(t_years, results[:, 2], lw=2)
    plt.axhline(ITER['K_IC_MIN'], ls='--')
    plt.ylabel('K_IC (MPa*sqrt(m)')

    plt.subplot(2, 2, 3)
    plt.plot(t_years, results[:, 3], lw=2)
    plt.axhline(ITER['TRITIUM_LIMIT'], ls='--')
    plt.yscale('log')
    plt.ylabel('Tritium Retention (T/m^2)')

    plt.subplot(2, 2, 4)
    plt.plot(t_years, results[:, 4], lw=2)
    plt.axhline(ITER['DOSE_LIMIT'], ls='--')
    plt.ylabel('Contact Dose (µSv/h)')

    plt.tight_layout()
    plt.savefig('assets/material_A+_degradation.png', dpi=300)
    print('Trend estimator complete. Results saved to assets/material_A+_results.txt and PNG.')
