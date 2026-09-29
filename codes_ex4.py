import pandas as pd

df = pd.read_csv('./data/Table.csv',sep='\t', decimal='.', index_col=0)
df



rho_g_per_cm3 = 1.03
df['Masse [g]'] = df['Volume [cm3]']* rho_g_per_cm3
df


m_foie_lobe_d = df.loc['lobe_droit','Masse [g]']


import numpy as np

delta_Mev_per_Bq_s = 0.9336
T_y90_s = 64.05*3600
dose_foie_limite_Gy = 120
m_kg=m_foie_lobe_d /1000
delta_J= delta_Mev_per_Bq_s * 1.602e-13
act_1_Bq = (dose_foie_limite_Gy *m_kg * np.log(2)) / (T_y90_s * delta_J)
act_1=act_1_Bq / 1e9
print(f"L'activité à injecter est de {act_1:.2f} GBq pour atteindre {dose_foie_limite_Gy} Gy au lobe droit.")


ratio_tum_lobe = df.loc['tum_dome_SPECT', 'Mean'] / df.loc['lobe_droit', 'Mean']
print(f"Le rapport des concentrations est estimé à {ratio_tum_lobe:.2f}")

m_tum = 11.118026
m_n = 833.848860
A_n = (2.01*10e-3)/ (1+(ratio_tum_lobe*(m_tum/m_n)))
A_t = ratio_tum_lobe * A_n * (m_tum/m_n)
print(f'Les activités dans le foie perfusé et la tumeur sont {A_n*1000:.2f} et {A_t*1000:.2f} MBq respectivement.')


A_t_Bq = A_t *10e6
m_tum_kg = m_tum /1000
dose_t = (A_t_Bq* T_y90_s * delta_J)/ (m_tum_kg * np.log(2))
print(f'La dose à la tumeur est {dose_t:.2f} Gy')


