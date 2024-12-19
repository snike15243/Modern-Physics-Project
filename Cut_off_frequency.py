import numpy as np
import pandas as pd
from scipy.signal import hilbert, savgol_filter, find_peaks
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib
import tikzplotlib
from Tikzplotlib_fixer import tikzplotlib_fix_ncols
matplotlib.use('Qt5Agg')

# Determine whether to use plt.show() or tikzplotlib.save()
LaTeX_plot = False

# Determine whether to suppress intermediate figures for every frequency
suppress_figures = True

# Initialze arrays
frequency_array = ['10', '20', '30', '40', '50', '100', '150', '200', '250', '300', '350', '400', '450','500', '600','700',  '800','900', '1000','1100', '1200','1300',  '1400','1500',  '1700', '2000']
Deltax_array = []
predicted_Deltax = []
amplifier_power = []
amplifier_gain = []

# Fit function for the responsivity, obtained from Reponsivity2.py
def Responsivity_function(x):
    return (-1.048e-9) *x**2  + (7.475e-9) * x + 1.038e-6

# Loop over all frequencies
for i, frequency in enumerate(frequency_array[:]):
    print(frequency)

    # Read the data
    df = pd.read_csv(f'Porno/{frequency}.csv', delimiter=',', usecols=[0,1,2,3], skiprows=range(1))
    df_numpy2 = df.to_numpy()
    time_array = df_numpy2[:,0]
    input_voltage_array = df_numpy2[:,1]
    output_voltage_array = df_numpy2[:,3]
    amp_array = df_numpy2[:,2]

    # Interpolate the data to a common time array
    time = np.linspace(time_array[0], time_array[-1], 10000)
    input_voltage = np.interp(time, time_array, input_voltage_array)
    output_voltage = np.interp(time, time_array, output_voltage_array)
    amp_voltage = 20* np.interp(time, time_array, amp_array)

    # Plot the data
    fig, ax = plt.subplots(3,1, sharex='all', figsize=(6,6))
    ax[0].plot(time, input_voltage)
    #ax[0].plot(time, amp_voltage)
    ax[1].plot(time, output_voltage)

    # Filter the data, find the peaks and troughs
    filtered_input = savgol_filter(input_voltage, 1000, 3)
    ax[0].plot(time, filtered_input)
    inputpeaks = find_peaks(filtered_input, prominence=0.1)
    inputtroughs = find_peaks(-filtered_input, prominence=0.03)
    length_beween_peak_and_trough = np.abs(inputpeaks[0][0] - inputtroughs[0][0])
    temp_var = 1.5*-0.007*np.log10(0.000008*int(frequency)) # calculate window size for savgol filter
    filtered_output = savgol_filter(output_voltage, int(length_beween_peak_and_trough*temp_var), 3)
    ax[1].plot(time, filtered_output)

    # Plot the peaks and troughs, set title
    ax[0].vlines(time[inputpeaks[0]], 0, 1, colors='r')
    ax[0].vlines(time[inputtroughs[0]], 0, 1, colors='g')
    fig.gca().set_title(f'Frequency: {frequency} Hz')

    # Calculate the phase over time, calculate Signal Power of the Amplfied Signal
    if inputpeaks[0][0] > inputtroughs[0][0]:
        to_be_hilbertized = filtered_output[inputtroughs[0][0]:inputpeaks[0][0]]
        to_be_hilbertized = to_be_hilbertized - np.min(to_be_hilbertized)
        to_be_hilbertized = to_be_hilbertized/np.max(to_be_hilbertized)
        hilbert_data = np.angle(hilbert(2*to_be_hilbertized - 1))
        hilbert_data2 = np.unwrap(hilbert_data, discont=np.pi)
        hilbert_time = time[inputtroughs[0][0]:inputpeaks[0][0]]
        amplifier_power.append(np.trapz(amp_voltage[inputtroughs[0][0]:inputpeaks[0][0]], time[inputtroughs[0][0]:inputpeaks[0][0]]))
    else:
        to_be_hilbertized = filtered_output[inputpeaks[0][0]:inputtroughs[0][0]]
        to_be_hilbertized = to_be_hilbertized - np.min(to_be_hilbertized)
        to_be_hilbertized = to_be_hilbertized / np.max(to_be_hilbertized)
        hilbert_data = np.angle(hilbert(2*to_be_hilbertized - 1))
        hilbert_data2 = np.unwrap(hilbert_data, discont=np.pi)
        hilbert_time = time[inputpeaks[0][0]:inputtroughs[0][0]]
        amplifier_power.append(np.trapz(amp_voltage[inputpeaks[0][0]:inputtroughs[0][0]], time[inputpeaks[0][0]:inputtroughs[0][0]]))
    phase_over_time = np.array([np.trapz(np.abs(np.gradient(hilbert_data2, hilbert_time))[0:j], hilbert_time[0:j]) for j, t in enumerate(hilbert_time)])
    ax[2].plot(hilbert_time, phase_over_time/(2*np.pi))
    cycle_counter = [np.argmin(np.abs(phase_over_time/(2*np.pi)-m*np.ones(np.shape(phase_over_time)))) for m in range(1,30)]
    ax[2].vlines(hilbert_time[cycle_counter], 0, 3, color='red')

    # Calculate the displacement
    Delta_phi = phase_over_time[-1] - phase_over_time[0]
    Deltax = Delta_phi * 635e-9 / (2 * 2 * np.pi)
    ax[0].set_title(f'Cycles between peaks:{Delta_phi/(2*np.pi)}')
    Deltax_array.append(Deltax)

    # Show the plots
    if not suppress_figures:
        plt.show()
    else:
        plt.close('all')

    # Calculate the predicted displacement and amplifier gain
    Input_Signal_Amplitude = np.abs(input_voltage[inputpeaks[0][0]] - input_voltage[inputtroughs[0][0]])
    predicted_Deltax.append(Responsivity_function(Input_Signal_Amplitude)*Input_Signal_Amplitude)
    Vpp_input_signal = np.abs(input_voltage[inputpeaks[0][0]] - input_voltage[inputtroughs[0][0]])
    Vpp_amp_signal = np.abs(amp_voltage[inputpeaks[0][0]] - amp_voltage[inputtroughs[0][0]])
    amplifier_gain.append(np.abs(Vpp_amp_signal/Vpp_input_signal))


# Plot the results
fig, ax = plt.subplots()
Deltax_decibel = 20*np.log10(Deltax_array/Deltax_array[0])
predicted_Deltax_decibel = 20*np.log10(predicted_Deltax/predicted_Deltax[0])
freqs = [float(freq) for freq in frequency_array] # measured frequencies
ax.plot(freqs, predicted_Deltax_decibel, label='Predicted Displacement Using Responsivity')
input_space = np.logspace(np.log10(np.min(freqs)), np.log10(np.max(freqs)), 100) # frequency space for the fit

# Fit the data using two fit functions
def bode_fit(x, a, b):
    returnarray = []
    for xl in x:
        if xl < a:
            returnarray.append(1)
        else:
            returnarray.append((xl/a)**b)
    return returnarray
def bode_fit2(x, a, b):
    return 1/np.sqrt(1+(x/a)**b)
popt, pcov = curve_fit(bode_fit2, freqs, (Deltax_array/Deltax_array[0]), p0=[100, 0.5])

# Plot the data
ax.plot(input_space, 20*np.log10(bode_fit2(input_space, *popt))-20*np.log10(bode_fit2([np.min(freqs)], *popt)), label='Interferometer Output Signal (Fit)')
ax.plot(freqs, Deltax_decibel-np.ones(np.shape(Deltax_decibel))*20*np.log10(bode_fit2([np.min(freqs)], *popt)), label='Interferometer Output Signal (Measured)')

# Calculate amplifier power and voltage gain spectra
amplifier_power_decibel = 10*np.log10(amplifier_power/amplifier_power[0])
amplifier_gain_decibel = 20 * np.log10(amplifier_gain)

# Calculate the cut-off frequency for the interferometer data
cut_off_frequency = 0
for i, v in enumerate(20*np.log10(bode_fit2(input_space, *popt))-20*np.log10(bode_fit2([np.min(freqs)], *popt))):
    if v < 20*np.log10(0.5):
        cut_off_frequency = input_space[i-1]
        break
ax.vlines(cut_off_frequency, -30, 20*np.log10(0.5), color='black', linestyle='dashed')
ax.hlines(20*np.log10(0.5), np.min(freqs), cut_off_frequency, color='black', linestyle='dashed')

# Calculate the cut-off frequency for the amplifier data
cut_off_frequency_amplifier = 0
gain_interp = np.interp(x=input_space, xp=freqs, fp=amplifier_gain_decibel)
for i, v in enumerate(gain_interp):
    if v-amplifier_gain_decibel[0] < 20*np.log10(0.5):
        cut_off_frequency_amplifier = input_space[i]
        break
ax.vlines(cut_off_frequency_amplifier, -30, 20*np.log10(0.5)+amplifier_gain_decibel[0], color='black', linestyle='dashed')
ax.hlines(amplifier_gain_decibel[0]+20*np.log10(0.5), np.min(freqs), cut_off_frequency_amplifier, color='black', linestyle='dashed')

# Plot the amplifier data
ax.plot(freqs, amplifier_gain_decibel, color='grey', label='Amplifier Gain from amplifier Output Signal (Measured)')

# Plot the cut-off frequencies
ax.scatter([cut_off_frequency, cut_off_frequency_amplifier], [20*np.log10(0.5), 20*np.log10(0.5)+amplifier_gain_decibel[0]], color='black')
if LaTeX_plot:
    ax.text(cut_off_frequency+100, 20*np.log10(0.5), f'$f_{{co}}= \\qty{{{cut_off_frequency:.0f}}}{{\hertz}}$', verticalalignment='bottom', horizontalalignment='left', fontsize=8)
    ax.text(cut_off_frequency_amplifier, 20*np.log10(0.5)+amplifier_gain_decibel[0]+0.5, f'$f_{{co}}= \\qty{{{cut_off_frequency_amplifier:.0f}}}{{\hertz}}$', verticalalignment='bottom', horizontalalignment='left', fontsize=8)
else:
    ax.text(cut_off_frequency+100, 20*np.log10(0.5), f'$f_{{co}}=$: {cut_off_frequency:.0f} Hz', verticalalignment='bottom', horizontalalignment='left', fontsize=8)
    ax.text(cut_off_frequency_amplifier, 20*np.log10(0.5)+amplifier_gain_decibel[0]+0.5, f'$f_{{co}}=$: {cut_off_frequency_amplifier:.0f} Hz', verticalalignment='bottom', horizontalalignment='left', fontsize=8)

# Plot settings
ax.set_xscale('log')
ax.set_xlim(10,5000)
ax.set_ylim(-30,30)
ax.legend(bbox_to_anchor=(0.5,0.01), loc='lower center')
if LaTeX_plot:
    ax.set_xlabel('Frequency [\\si{\\hertz}]')
    ax.set_ylabel('Piezo Displacement [\\si{\\decibel\meter}] \n Amplifier Gain [\\si{\\decibel}]')
else:
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Piezo Displacement (dBm)\nAmplifier Gain (dB)')
plt.yticks(list(plt.yticks()[0]) + [20*np.log10(0.5), amplifier_gain_decibel[0]])

# Save the plot
if LaTeX_plot:
    tikzplotlib_fix_ncols(ax.legend())
    tikzplotlib.save('LaTeX_plots/Cut_off_frequency.tex', extra_tikzpicture_parameters = ['trim axis left', 'trim axis right'])
else:
    plt.show()
