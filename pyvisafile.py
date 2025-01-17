import copy

import pyvisa
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from numpy import dtype
from scipy.signal import savgol_filter, find_peaks, hilbert
from scipy.ndimage import gaussian_filter1d, uniform_filter1d
import os

from amplitude_list_maker import new_amplitude_list

# Ensure the directory exists
output_dir = '.'
os.makedirs(output_dir, exist_ok=True)


freq = 86
location = 0
attempt = 2

matplotlib.use('Qt5Agg')
import struct
if True:
    rm = pyvisa.ResourceManager() # 'C:\\WINDOWS\\system32\\visa64.dll'
    print(rm.list_resources())
    my_instrument = rm.open_resource('USB0::0x1AB1::0x0488::DS1BA125100508::INSTR')
    my_instrument.timeout = 25000
    my_instrument.write('*IDN?')
    print(my_instrument.read())

    my_instrument.write(':ACQ:TYPE AVERage')
    my_instrument.write(':ACQ:AVER 32')

    my_instrument.write(':WAV:FORM ASC')
    print(my_instrument.query(':WAV:FORM?'))
    my_instrument.write(':STOP')
    my_instrument.write(':WAV:POIN:MODE RAW')
    my_instrument.write(':WAV:POIN 16840')
    print(my_instrument.query(':WAV:POIN?'))

    my_instrument.write(':WAV:DATA? CHAN1')
    data = my_instrument.read_raw().decode('UTF-8')[12:].split(',')

    my_instrument.write(':WAV:DATA? CHAN2')
    data2 = my_instrument.read_raw().decode('UTF-8')[12:].split(',')
    #data = struct.unpack('f', my_instrument.read_raw())
    my_instrument.write(':RUN')

    #print(my_instrument.query(':WAVeform:XORigin?'))
    dt = float(my_instrument.query(':WAVeform:XINCrement?'))
    input_voltage = np.array(data, dtype=float)
    output_voltage = np.array(data2, dtype=float)
    time = np.arange(0, len(input_voltage) * dt, dt)
else:
    datafile = np.load('240data60a0.npz')
    time = datafile['time']
    input_voltage = datafile['input_voltage']
    output_voltage = datafile['output_voltage']
    filtered_input = datafile['filtered_input']
    filtered_output = datafile['filtered_output']
    hilbert_time = datafile['hilbert_time']
    phase_over_time = datafile['phase_over_time']
    cycle_counter = datafile['cycle_counter']
    Deltax = datafile['Deltax']


#print(data)

filtered_input = savgol_filter(input_voltage, 500, 3)
inputpeaks = find_peaks(filtered_input, prominence=0.1)
inputtroughs = find_peaks(-filtered_input, prominence=0.03)
index_length_beween_peak_and_trough = np.abs(inputpeaks[0][0] - inputtroughs[0][0])

windowsize_output = int((1/4)*index_length_beween_peak_and_trough)



#lowess = sm.nonparametric.lowess(output_voltage, time, frac=0.005)
#filtered_output = lowess[:,1]

def adaptive_gaussian_filter(signal, scale, offset=0):
    local_variances = uniform_filter1d(((signal - np.mean(signal))*scale)**2, size=100)  # Local variance
    smoothed_signal = np.zeros_like(signal)
    for i in range(len(signal)):
        smoothed_signal[i] = gaussian_filter1d(signal, sigma=offset+local_variances[i])[i]
        #smoothed_signal[i] = savgol_filter(signal, int(offset + local_variances[i]), 2)[i]
    return smoothed_signal, local_variances

#filtered_output, local_variances = adaptive_gaussian_filter(output_voltage, 1500,offset = 2)
filtered_output = savgol_filter(output_voltage, windowsize_output, 3)

#print(data_np)
#print(data_np[0])
fig, ax = plt.subplots(3,1, sharex='all', figsize=(6,6))
ax[0].plot(time, input_voltage)
#ax[0].plot(time, amp_voltage)
ax[1].plot(time, output_voltage)
#ax[2].plot(time, local_variances)
ax[0].plot(time, filtered_input)
ax[1].plot(time, filtered_output)
ax[0].vlines(time[inputpeaks[0]], 0, 1, colors='r')
ax[0].vlines(time[inputtroughs[0]], 0, 1, colors='g')
#plt.show()
divide_by_2 = 1
index0=0
index1=0
if inputpeaks[0][0] > inputtroughs[0][0]:
    if len(inputtroughs[0]) > 1:
        data_to_be_hilbertized = filtered_output #[inputtroughs[0][0]:inputtroughs[0][1]]
        hilbert_time = time #[inputtroughs[0][0]:inputtroughs[0][1]]
        divide_by_2 = 2
        index0=inputtroughs[0][0]
        index1 = inputtroughs[0][1]
    else:
        data_to_be_hilbertized = filtered_output #[inputtroughs[0][0]:inputpeaks[0][0]]
        hilbert_time = time #[inputtroughs[0][0]:inputpeaks[0][0]]
        index0 = inputtroughs[0][0]
        index1 = inputpeaks[0][0]
    #data_to_be_hilbertized = data_to_be_hilbertized - np.min(data_to_be_hilbertized)
    #data_to_be_hilbertized = data_to_be_hilbertized/np.max(data_to_be_hilbertized)
    data_to_be_hilbertized = data_to_be_hilbertized - (np.max(data_to_be_hilbertized) + np.min(data_to_be_hilbertized)) / 2
    hilbert_data = np.angle(hilbert(data_to_be_hilbertized))
    hilbert_data2 = np.unwrap(hilbert_data, discont=np.pi)

else:
    if len(inputpeaks[0]) > 1:
        data_to_be_hilbertized = filtered_output #[inputpeaks[0][0]:inputpeaks[0][1]]
        hilbert_time = time #[inputpeaks[0][0]:inputpeaks[0][1]]
        divide_by_2 = 2
        index0 = inputpeaks[0][0]
        index1 = inputpeaks[0][1]
    else:
        data_to_be_hilbertized = filtered_output #[inputpeaks[0][0]:inputtroughs[0][0]]
        hilbert_time = time #[inputpeaks[0][0]:inputtroughs[0][0]]
        index0 = inputpeaks[0][0]
        index1 = inputtroughs[0][0]
    #data_to_be_hilbertized = data_to_be_hilbertized - np.min(data_to_be_hilbertized)
    #data_to_be_hilbertized = data_to_be_hilbertized / np.max(data_to_be_hilbertized)
    data_to_be_hilbertized = data_to_be_hilbertized - (np.max(data_to_be_hilbertized) + np.min(data_to_be_hilbertized)) / 2
    hilbert_data = np.angle(hilbert(data_to_be_hilbertized))
    hilbert_data2 = np.unwrap(hilbert_data, discont=np.pi)

hilbert_diff = []
hilbert_data2_old = copy.deepcopy(hilbert_data2)
for i, h in enumerate(hilbert_data2):
    if i != len(hilbert_data2)-1:
        hilbert_diff.append(hilbert_data2[i+1] - hilbert_data2[i])
        if np.abs(hilbert_data2[i+1] - hilbert_data2[i]) > 0.5*np.pi:
            hilbert_data2[i+1:] = hilbert_data2[i+1:] - np.pi*np.sign(hilbert_data2[i+1] - hilbert_data2[i])
phase_over_time = np.array([np.trapz(np.abs(np.gradient(hilbert_data2, hilbert_time))[0:j], hilbert_time[0:j]) for j, t in
                   enumerate(hilbert_time)])[index0:index1]
hilbert_time2 = hilbert_time[index0:index1]
ax[2].plot(hilbert_time2, phase_over_time*(1/(2*np.pi)))
#ax[2].plot(hilbert_time2, data_to_be_hilbertized)
cycle_counter = [np.argmin(np.abs(phase_over_time*(1/(2*np.pi)) - m * np.ones(np.shape(phase_over_time)))) for m in range(1, 10)]
ax[2].vlines(hilbert_time2[cycle_counter], 0, np.max(phase_over_time/(2*np.pi)), color='red')


# Calculate the displacement
Delta_phi = phase_over_time[-1] - phase_over_time[0]
Deltax = Delta_phi * 635e-9 / (2 * divide_by_2 * 2*np.pi)
ax[2].set_title(f'{2*Deltax*1000000} micrometer, {Delta_phi/(2*np.pi*divide_by_2)} ')
#plt.show()

#save all data
print(f'{2*Deltax*1000000} micrometer')
np.savez(os.path.join(output_dir, f'{freq}data{location}a{attempt}.npz'), time=time, input_voltage=input_voltage, output_voltage=output_voltage, filtered_input=filtered_input, filtered_output=filtered_output, hilbert_time=hilbert_time, phase_over_time=phase_over_time, cycle_counter=cycle_counter, Deltax=Deltax)
file = np.load('amplitude_list.npz')
amplitude_list = file['amplitude_list']
cantilever_loc = file['cantilever_loc']

new_amplitude_list = np.append(amplitude_list, 2*Deltax*1000000)
new_cantilever_loc = np.append(cantilever_loc, location)
np.savez('amplitude_list.npz', amplitude_list=new_amplitude_list, cantilever_loc=new_cantilever_loc)


