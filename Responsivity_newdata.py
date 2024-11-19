## Before running: Execute the following:
## conda env create -f environment.yaml
## conda activate Modern_Physics_project

suppress_figures = False

import matplotlib as matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks

matplotlib.use('Qt5Agg')

from scipy.signal import savgol_filter
from scipy.signal import hilbert

figax = [] # this will contain all figure and axis objects
responsivities = [] # this will contain all responsivities obtained from taking DeltaX/DeltaV between A and B
responsivities2=[] # this will contain all responsivities obtained from averaging dX/dV over the domain in which dX/dV is relatively constant

# Load Amplitude Data, these were the amplitudes in 1/10 V used as input in the different rounds of the experiment
amplitude_names = [42,62,102,122,142,162,182,198,226] # 82 was removed because output was saved wrong: inputfile was saved as outputfile


# This loop obtains the responsivity for each input amplitude
for counter, amplitude_name in enumerate(amplitude_names):
    # Load data
    df = pd.read_csv(f'Data_Variable_Amplitude_Input/{amplitude_name}a.xls', delimiter='\t', header=2)
    df2 = pd.read_csv(f'Data_Variable_Amplitude_Input/{amplitude_name}b.xls', delimiter='\t', header=2)
    df_merged = pd.concat([df, df2], axis=1)
    df_time_and_input = df_merged[['Time', 'Voltage']]
    figax.append(plt.subplots(3,1, sharex='all', figsize=(6,6))) # initialize figure and axis objects
    df_numpy = df_time_and_input.to_numpy()[:,[0,2,3]]

    # Plot Input and Output Signals
    figax[counter][1][0].plot(df_numpy[:,0], df_numpy[:,1])
    figax[counter][1][1].plot(df_numpy[:,0], df_numpy[:,2])

    # Filter input signal
    time = np.arange(df_numpy[:,0][0], df_numpy[:,0][-1], 0.00001)
    input_interp = np.interp(time, df_numpy[:,0], df_numpy[:,1])
    filtered_input = savgol_filter(input_interp, 1000, 3)
    figax[counter][1][0].plot(time, filtered_input) # plot filtered input signal

    # Filter output signal
    data = np.interp(time, df_numpy[:,0], df_numpy[:,2])
    figax[counter][1][1].plot(time, data) # plot output signal

    # Calculate phase of the cyclic signal at every point in time, as well as its derivative
    hilbert_data = np.angle(hilbert(data))
    phase_over_time = [np.trapz(np.abs(np.gradient(hilbert_data, time))[0:j], time[0:j]) for j, t in enumerate(time)]
    phase_derivative = savgol_filter(phase_over_time, 100, 3, deriv=1, delta=float(time[1]-time[0]))

    # Calculate derivative of the input signal
    Voltage_derivative = savgol_filter(filtered_input, 100, 3, deriv=1, delta=float(time[1]-time[0]))

    # Find peaks and troughs of the input signal
    input_troughs = time[find_peaks(-filtered_input, distance=1000, prominence=1)[0]]
    input_peaks = time[find_peaks(filtered_input, distance=1000, prominence=1)[0]]



    #### Obtain the responsivity from averaging dX/dV over the domain in which dX/dV is relatively constant: ####
    # Calculate Responsivity for each point in time
    lambdav = 635e-9
    Responsivity_data = (lambdav / 2) * phase_derivative / Voltage_derivative

    # Plot Responsivity for each point in time
    figax[counter][1][2].plot(time, Responsivity_data)
    figax[counter][1][2].set_yscale('log')

    # Find the longest interval where the responsivity is relatively constant...
    responsivity_derivative = savgol_filter(Responsivity_data, 500, 3, deriv=1, delta=float(time[1]-time[0]))
    # ... so intervals where np.abs(responsivity_derivative) < np.max(np.abs(responsivity_derivative))/8
    true_indices = np.where((np.abs(responsivity_derivative) < np.max(np.abs(responsivity_derivative))/8) & ((time > input_troughs[0]) & (time < input_peaks[0])))[0]
    longest_interval_start = true_indices[0]
    longest_interval_end = true_indices[0]
    current_start = true_indices[0]
    for i in range(1, len(true_indices)): # this loop looks for the longest such interval
        if true_indices[i] != true_indices[i - 1] + 1: # If the current run ends
            current_end = true_indices[i - 1]
            if (time[current_end] - time[current_start]) > (time[longest_interval_end] - time[longest_interval_start]):
                longest_interval_start, longest_interval_end = current_start, current_end
            current_start = true_indices[i] # Start a new run
    current_end = true_indices[-1] # Check the last run
    if (time[current_end] - time[current_start]) > (time[longest_interval_end] - time[longest_interval_start]):
        longest_interval_start, longest_interval_end = current_start, current_end
    averaging_domain = [longest_interval_start, longest_interval_end] # The domain where the responsivity is relatively constant and where dX/dV will be averaged over

    # Calculate the average responsivity over the domain where dX/dV is relatively constant
    Responsivity_avg = np.mean(Responsivity_data[averaging_domain[0]:averaging_domain[1]])
    print("Average Responsivity over flat domain: ", Responsivity_avg)
    responsivities2.append(Responsivity_avg)



    #### Obtain the responsivity from taking DeltaX/DeltaV between A and B: ####
    # Find A and B points
    AB_distance = np.abs(input_peaks[0] - input_troughs[0])
    AB_range = [input_troughs[0] + 0.25 * AB_distance, input_peaks[0] - 0.25 * AB_distance]
    AB_indices = np.searchsorted(time, AB_range)
    AB_voltage = np.interp(AB_range, time, filtered_input)
    figax[counter][1][0].text(time[AB_indices[0]] + 0.002, AB_voltage[0] - 0.2, 'A', fontsize=12, verticalalignment='bottom')  # add A and B labels to the plot
    figax[counter][1][0].text(time[AB_indices[1]] + 0.002, AB_voltage[1] - 0.2, 'B', fontsize=12, verticalalignment='bottom')

    # Calculate Responsivity between A and B
    Responsivity_global = (lambdav/2)*(phase_over_time[AB_indices[1]]-phase_over_time[AB_indices[0]])/(filtered_input[AB_indices[1]]-filtered_input[AB_indices[0]])
    print("Global Resonsivity: ", Responsivity_global)
    responsivities.append(Responsivity_global)

    # Plot Responsivity between A and B
    figax[counter][1][0].scatter(time[AB_indices], AB_voltage, s=50, c='black', label=f"Responsivity between A & B: \n {Responsivity_global} $mV^{-1}$")
    figax[counter][1][0].text(time[0],np.max(filtered_input)-0.5, f"Responsivity between A & B: \n {Responsivity_global} $mV^{-1}$", fontsize=5)

    # Plot Responsivity Between A & B, and Plot Responsivity over Constant Responsivity Domain
    figax[counter][1][2].hlines(Responsivity_global, AB_range[0], AB_range[-1], color='red', linestyle='-', label=f"Responsivity between A & B: \n {Responsivity_global} $mV^{-1}$")
    figax[counter][1][2].hlines(Responsivity_avg, time[longest_interval_start], time[longest_interval_end], color='green')

    figax[counter][1][0].set_ylabel('Input Signal (V)')
    figax[counter][1][1].set_ylabel('Output Signal (V)')
    figax[counter][1][2].set_ylabel('Responsivity ($mV^{-1}$)')
    if not suppress_figures:
        plt.show()
    else:
        plt.close('all')


# Plot relationship between Responsivity and input amplitude
amplitudes_values = np.array(amplitude_names)/10
fig, ax = plt.subplots()
ax.plot(amplitudes_values, responsivities)
ax.plot(amplitudes_values, responsivities2)
ax.set_xlabel('Amplitude of Input Signal (V)')
ax.set_ylabel('Responsivity ($mV^{-1}$)')
plt.show()

