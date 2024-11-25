import numpy as np
import pandas as pd
from scipy.signal import hilbert, savgol_filter, find_peaks
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

frequency_array = ['70', '110', '150', '170', '200', '250', '300', '500', '700', '900', '1000', '1100', '1200', '1300', '1400', '1500'] # remove 90, 130, 400, 600, 800 because it was saved wrong
Deltax_array = []

for frequency in frequency_array[:]:
    dfa = pd.read_csv(f'Data_variable_frequency_input/{frequency}a.xls', skiprows=range(7), delimiter='\t', usecols=[1,2])
    dfa.rename(columns={'Voltage': 'Input Voltage'}, inplace=True)
    dfb = pd.read_csv(f'Data_variable_frequency_input/{frequency}b.xls', skiprows=range(7), delimiter='\t', usecols=[2])
    dfb.rename(columns={'Voltage': 'Output Voltage'}, inplace=True)
    df = pd.concat([dfa, dfb], axis=1)
    df_numpy2 = df.to_numpy()
    time_array = df_numpy2[:,0]
    input_voltage_array = df_numpy2[:,1]
    output_voltage_array = df_numpy2[:,2]
    time = np.linspace(time_array[0], time_array[-1], 10000)
    input_voltage = np.interp(time, time_array, input_voltage_array)
    output_voltage = np.interp(time, time_array, output_voltage_array)
    fig, ax = plt.subplots(3,1, sharex='all', figsize=(6,6))
    ax[0].plot(time, input_voltage)
    ax[1].plot(time, output_voltage)
    filtered_input = savgol_filter(input_voltage, 1000, 3)
    ax[0].plot(time, filtered_input)
    filtered_output = savgol_filter(output_voltage, 500, 3)
    ax[1].plot(time, filtered_output)
    inputpeaks = find_peaks(filtered_input, prominence=0.2)
    inputtroughs = find_peaks(-filtered_input, prominence=0.03)
    ax[0].vlines(time[inputpeaks[0]], 0, 1, colors='r')
    ax[0].vlines(time[inputtroughs[0]], 0, 1, colors='g')
    fig.gca().set_title(f'Frequency: {frequency} Hz')
    if inputpeaks[0][0] > inputtroughs[0][0]:
        hilbert_data = np.angle(hilbert(output_voltage[inputtroughs[0][0]:inputpeaks[0][0]]))
        hilbert_time = time[inputtroughs[0][0]:inputpeaks[0][0]]
    else:
        hilbert_data = np.angle(hilbert(filtered_output[inputpeaks[0][0]:inputtroughs[0][0]]))
        hilbert_time = time[inputpeaks[0][0]:inputtroughs[0][0]]
    phase_over_time = [np.trapz(np.abs(np.gradient(hilbert_data, hilbert_time))[0:j], hilbert_time[0:j]) for j, t in enumerate(hilbert_time)]
    ax[2].plot(hilbert_time, phase_over_time)
    cycle_counter = [np.argmin(np.abs(phase_over_time-m*np.ones(np.shape(phase_over_time)))) for m in range(1,10)]
    ax[2].vlines(hilbert_time[cycle_counter], 0, 3, color='red')
    #ax[2].vlines(hilbert_time[np.where(np.abs(np.gradient(hilbert_data, hilbert_time)) < 10)], 0, 1, color='green')
    plt.show()
    plt.close('all')
    Delta_phi = phase_over_time[-1] - phase_over_time[0]
    Deltax = Delta_phi * 635e-9/2
    Deltax_array.append(Deltax)

fig, ax = plt.subplots()
Deltax_decibel = 20*np.log10(Deltax_array/Deltax_array[0])
freqs = [float(freq) for freq in frequency_array]
ax.plot(freqs, Deltax_decibel)
def bode_fit(x, a, b):
    returnarray = []
    for xl in x:
        if xl < a:
            returnarray.append(1)
        else:
            returnarray.append((xl/a)**b)
    return returnarray
popt, pcov = curve_fit(bode_fit, freqs, Deltax_array/Deltax_array[0], p0=[100, -0.5])
ax.plot(np.linspace(np.min(freqs), np.max(freqs), 100), 20*np.log10(bode_fit(np.linspace(np.min(freqs), np.max(freqs), 100), *popt)))
ax.set_xscale('log')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Piezo Displacement (dBm)')
plt.show()
