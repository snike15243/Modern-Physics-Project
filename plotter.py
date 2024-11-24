import pandas as pd
import numpy as np
import copy
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

dfa = pd.read_csv(f'Data2.0/cut_off/1_1.1k.xls', skiprows=range(7), delimiter='\t', usecols=[1,2])
dfb = pd.read_csv(f'Data2.0/cut_off/2_1.1k.xls', skiprows=range(7), delimiter='\t', usecols=[2])
dfc = pd.read_csv(f'Data2.0/cut_off/3_1.1k.xls', skiprows=range(7), delimiter='\t', usecols=[2])
dfa.rename(columns={'Voltage': 'Input Voltage'}, inplace=True)
dfb.rename(columns={'Voltage': 'Output Voltage'}, inplace=True)
dfc.rename(columns={'Voltage': 'Amp Voltage'}, inplace=True)
#plot
df = pd.concat([dfa, dfb, dfc], axis=1)
df_numpy2 = df.to_numpy()
time_array = df_numpy2[:,0]
time_array_new = copy.deepcopy(time_array)
for time_moment_index, time_moment in enumerate(np.unique(time_array)):
    copies = np.argwhere(time_array == time_moment)
    num_of_copies = len(copies)
    if time_moment_index >= len(np.unique(time_array)) - 1:
        increment += 0
    else:
        increment = (np.unique(time_array)[time_moment_index + 1] - time_moment) / num_of_copies
    if num_of_copies > 1:
        for copy_index, copy in enumerate(copies):
            time_array_new[copy] += increment*copy_index
time_array = time_array_new
input_voltage_array = df_numpy2[:,1]
output_voltage_array = df_numpy2[:,2]
amp_voltage_array = df_numpy2[:,3]
time = time_array # np.linspace(time_array[0], time_array[-1], 10000)
input_voltage = np.interp(time, time_array, input_voltage_array)
output_voltage = np.interp(time, time_array, output_voltage_array)
amp_voltage = np.interp(time, time_array, amp_voltage_array)
fig, ax = plt.subplots(3,1, sharex='all', figsize=(6,6))
ax[0].plot(time, input_voltage_array)
ax[1].plot(time, output_voltage_array)
ax[2].plot(time, amp_voltage_array)
plt.show()
