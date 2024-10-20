import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from cornerdetection import cornerdetection_inputsignal, max_turnaround, to_the_sides, golay_filter_variable_window_size, cornerdetection_outputsignal
from numderivative import nthorderfirstdegreenumderivative
from scipy.signal import savgol_filter

# Load the data
data_228 = pd.read_csv('Data/NewFile0.csv')
data_200 = pd.read_csv('Data/NewFile1.csv')
data_184 = pd.read_csv('Data/NewFile2.csv')
data_160 = pd.read_csv('Data/NewFile3.csv')
data_144 = pd.read_csv('Data/NewFile4.csv')
data_120 = pd.read_csv('Data/NewFile5.csv')
data_100 = pd.read_csv('Data/NewFile6.csv')
data_84 = pd.read_csv('Data/NewFile7.csv')
data_64 = pd.read_csv('Data/NewFile8.csv')
data_40 = pd.read_csv('Data/NewFile9.csv')

data_array = [data_228, data_200, data_184, data_160, data_144, data_120, data_100, data_84, data_64, data_40]


figax = []
# Extract the data
for counter, df in enumerate([data_array[5]]):

    time = df.iloc[1:,0].to_numpy().astype(float)
    input_signal = df.iloc[1:,1].to_numpy().astype(float)
    output_signal = df.iloc[1:,2].to_numpy().astype(float)

    input_signal_peaks = cornerdetection_inputsignal(input_signal, time, True)
    output_signal_peaks = cornerdetection_outputsignal(output_signal, time, True)
    input_signal_throughs = cornerdetection_inputsignal(input_signal, time, False)
    output_signal_throughs = cornerdetection_outputsignal(output_signal, time, False)


    figax.append(plt.subplots())
    figax[counter][1].scatter(time,input_signal , s=1)
    #figax[counter][1].vlines(x=input_signal_peaks, color='red', ymin=min(input_signal), ymax=max(input_signal))
    #figax[counter][1].vlines(x=input_signal_throughs, color='green', ymin=min(input_signal), ymax=max(input_signal))
    figax[counter][1].scatter(time, output_signal, s=1)
    figax[counter][1].scatter(time, savgol_filter(input_signal, 100, 4, deriv=0, delta=(time[1]-time[0])), s=1)
    figax[counter][1].plot(time, golay_filter_variable_window_size(output_signal, 4, time, deriv=0), linewidth=1)
    #figax[counter][1].vlines(x=output_signal_peaks, color='red', ymin=min(output_signal), ymax=max(output_signal))
    #figax[counter][1].vlines(x=output_signal_throughs, color='green', ymin=min(output_signal), ymax=max(output_signal))

    #figax[counter][1].grid()
    plt.show()

