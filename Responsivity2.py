## Before running: Execute the following:
## conda env create -f environment.yaml
## conda activate Modern_Physics_project

uncertainty_in_lambda = 5e-9 # meters
suppress_figures = True

import matplotlib as matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from scipy import odr

matplotlib.use('Qt5Agg')

from scipy.signal import savgol_filter
from scipy.signal import hilbert
from scipy import odr
import tikzplotlib

figax = [] # this will contain all figure and axis objects
responsivities = [] # this will contain all responsivities obtained from taking DeltaX/DeltaV between A and B
uncertainties = [] # this will contain all uncertainties in the responsivities for the first mehod

# Load Amplitude Data, these were the amplitudes in 1/10 V used as input in the different rounds of the experiment
amplitude_names = [42,62,102,122,142,162,182,198,226] # 82 was removed because output was saved wrong: inputfile was saved as outputfile


# This loop obtains the responsivity for each input amplitude
for counter, amplitude_name in enumerate(amplitude_names):
    # Load data
    df = pd.read_csv(f'Data_Variable_Amplitude_Input/{amplitude_name}a.xls', delimiter='\t', header=2)
    df2 = pd.read_csv(f'Data_Variable_Amplitude_Input/{amplitude_name}b.xls', delimiter='\t', header=2)
    df_merged = pd.concat([df, df2], axis=1)
    df_time_and_input = df_merged[['Time', 'Voltage']]
    figax.append(plt.subplots(2,1, sharex='all', figsize=(6,6))) # initialize figure and axis objects
    df_numpy = df_time_and_input.to_numpy()[:,[0,2,3]]
    Time_uncertainty = 1/250000 # 250 kSa/s is the sampling rate of the oscilloscope, so the uncertainty is at most 1/250000 s
    Voltage_uncertainty = np.dot(np.unique(df_numpy[:,1])[0:2], [[1], [-1]]).item() # The uncertainty in the can be obtained from the vertical resolution
    lambdav = 635e-9 # meters

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
    uncertainty_in_phase = np.pi/2 # it is assumed that the phase is uncertain by at most pi/2, as even with the naked eye such a phase difference can be detected

    # Calculate derivative of the input signal
    Voltage_derivative = savgol_filter(filtered_input, 100, 3, deriv=1, delta=float(time[1]-time[0]))
    uncertainty_in_voltage_derivative = np.sqrt(2)*Voltage_uncertainty/Time_uncertainty # uncertainty (calculus approach) in the derivative of the input signal with the conservative estimate of the first order numerical derivative which is most sensitive to noise

    # Find peaks and troughs of the input signal
    input_troughs = time[find_peaks(-filtered_input, distance=1000, prominence=1)[0]]
    input_peaks = time[find_peaks(filtered_input, distance=1000, prominence=1)[0]]

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
    uncertainty_from_lambda2 = (uncertainty_in_lambda/2)*(phase_over_time[AB_indices[1]]-phase_over_time[AB_indices[0]])/(filtered_input[AB_indices[1]]-filtered_input[AB_indices[0]]) # calculus approach for uncertainty
    uncertainty_from_phase_A = (lambdav/2)*(uncertainty_in_phase)/(filtered_input[AB_indices[1]]-filtered_input[AB_indices[0]])
    uncertainty_from_phase_B = (lambdav/2)*(-uncertainty_in_phase)/(filtered_input[AB_indices[1]]-filtered_input[AB_indices[0]])
    uncertainty_from_voltage_A = -(lambdav/2)*(phase_over_time[AB_indices[1]]-phase_over_time[AB_indices[0]])/(filtered_input[AB_indices[1]]-filtered_input[AB_indices[0]])**2*Voltage_uncertainty
    uncertainty_from_voltage_B = (lambdav/2)*(phase_over_time[AB_indices[1]]-phase_over_time[AB_indices[0]])/(filtered_input[AB_indices[1]]-filtered_input[AB_indices[0]])**2*Voltage_uncertainty
    uncertainty_global = np.sqrt(uncertainty_from_lambda2**2 + uncertainty_from_phase_A**2 + uncertainty_from_phase_B**2 + uncertainty_from_voltage_A**2 + uncertainty_from_voltage_B**2) # total uncertainty
    print("Global Resonsivity: ", Responsivity_global)
    responsivities.append(Responsivity_global)
    uncertainties.append(uncertainty_global)

    # Plot A and B labels
    figax[counter][1][0].scatter(time[AB_indices], AB_voltage, s=50, c='black', label=f"Responsivity between A & B: \n {Responsivity_global} $mV^{-1}$")
    figax[counter][1][0].text(time[0],np.max(filtered_input)-0.5, f"Responsivity between A & B: \n {Responsivity_global} $\pm$ {uncertainty_global} $mV^{-1}$", fontsize=5)


    figax[counter][1][0].set_ylabel('Input Signal (V)')
    figax[counter][1][1].set_ylabel('Output Signal (V)')
    if not suppress_figures:
        plt.show()
    else:
        plt.close('all')


# Plot relationship between Responsivity and input amplitude
amplitudes_values = np.array(amplitude_names)/10
fig, ax = plt.subplots()
ax.plot(amplitudes_values, responsivities, color='black', label='Responsivity')
Average_Responsivity_obj = odr.ODR(odr.RealData(amplitudes_values, responsivities, sy=uncertainties), odr.Model(lambda B, x: B[0]*np.ones(np.shape(x))), beta0=[0.000001]).run() # This will calculate the average responsivity with its uncertainty
Average_Responsivity = Average_Responsivity_obj.beta[0]
Average_Responsivity_uncertainty = Average_Responsivity_obj.sd_beta[0]
ax.text(23.5, 1.2e-6, f"Average Responsivity: \qty[exponent-mode = scientific]{{{np.format_float_positional(Average_Responsivity, 2, fractional=False)} \pm {np.format_float_positional(Average_Responsivity_uncertainty,1, fractional=False)}}}{{\meter\per\\volt}}", fontsize=12, verticalalignment='bottom', horizontalalignment='right') # add average responsivity to the plot
ax.fill_between(amplitudes_values, np.array(responsivities) - np.array(uncertainties), np.array(responsivities) + np.array(uncertainties), alpha=0.3, facecolor='gray', edgecolor='black', label='Uncertainty')
ax.set_xlabel('Amplitude of Input Signal (\si{\\volt})')
ax.set_ylabel('Responsivity (\si{\meter\per\\volt})')
ax.legend()
def tikzplotlib_fix_ncols(obj):
    """
    workaround for matplotlib 3.6 renamed legend's _ncol to _ncols, which breaks tikzplotlib
    """
    if hasattr(obj, "_ncols"):
        obj._ncol = obj._ncols
    for child in obj.get_children():
        tikzplotlib_fix_ncols(child)
tikzplotlib_fix_ncols(ax.legend())
#plt.show()
tikzplotlib.save("Responsivity.tex")

