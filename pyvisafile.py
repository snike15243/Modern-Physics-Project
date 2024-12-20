import pyvisa
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from numpy import dtype
from scipy.signal import savgol_filter, find_peaks, hilbert




matplotlib.use('Qt5Agg')
import struct
if False:
    rm = pyvisa.ResourceManager() # 'C:\\WINDOWS\\system32\\visa64.dll'
    print(rm.list_resources())
    my_instrument = rm.open_resource('USB0::0x1AB1::0x0488::DS1BA125100508::INSTR')
    my_instrument.timeout = 25000
    my_instrument.write('*IDN?')
    print(my_instrument.read())
    my_instrument.write(':WAV:FORM ASC')
    print(my_instrument.query(':WAV:FORM?'))
    my_instrument.write(':STOP')
    my_instrument.write(':WAV:POIN:MODE RAW')
    my_instrument.write(':WAV:POIN 16840')
    print(my_instrument.query(':WAV:POIN?'))

    my_instrument.write(':WAV:DATA? CHAN1')
    data = my_instrument.read_raw().decode('UTF-8')[12:].split(',')

    my_instrument.write(':WAV:DATA? CHAN3')
    data2 = my_instrument.read_raw().decode('UTF-8')[12:].split(',')
    #data = struct.unpack('f', my_instrument.read_raw())
    my_instrument.write(':RUN')

    #print(my_instrument.query(':WAVeform:XORigin?'))
    dt = float(my_instrument.query(':WAVeform:XINCrement?'))
    input_voltage = np.array(data, dtype=float)
    output_voltage = np.array(data2, dtype=float)
    time = np.arange(0, len(input_voltage) * dt, dt)
else:
    datafile = np.load('data.npz')
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

filtered_input = savgol_filter(input_voltage, 1000, 3)
inputpeaks = find_peaks(filtered_input, prominence=0.1)
inputtroughs = find_peaks(-filtered_input, prominence=0.03)
length_beween_peak_and_trough = np.abs(inputpeaks[0][0] - inputtroughs[0][0])

windowsize_output = 500

filtered_output = savgol_filter(output_voltage, windowsize_output, 3)
#print(data_np)
#print(data_np[0])
fig, ax = plt.subplots(3,1, sharex='all', figsize=(6,6))
ax[0].plot(time, input_voltage)
#ax[0].plot(time, amp_voltage)
ax[1].plot(time, output_voltage)
ax[0].plot(time, filtered_input)
ax[1].plot(time, filtered_output)
ax[0].vlines(time[inputpeaks[0]], 0, 1, colors='r')
ax[0].vlines(time[inputtroughs[0]], 0, 1, colors='g')
divide_by_2 = 1
if inputpeaks[0][0] > inputtroughs[0][0]:
    if len(inputtroughs[0]) > 1:
        data_to_be_hilbertized = filtered_output[inputtroughs[0][0]:inputtroughs[0][1]]
        hilbert_time = time[inputtroughs[0][0]:inputtroughs[0][1]]
        divide_by_2 = 2
    else:
        data_to_be_hilbertized = filtered_output[inputtroughs[0][0]:inputpeaks[0][0]]
        hilbert_time = time[inputtroughs[0][0]:inputpeaks[0][0]]
    data_to_be_hilbertized = data_to_be_hilbertized - np.min(data_to_be_hilbertized)
    data_to_be_hilbertized = data_to_be_hilbertized/np.max(data_to_be_hilbertized)
    hilbert_data = np.angle(hilbert(2*data_to_be_hilbertized - 1))
    hilbert_data2 = np.unwrap(hilbert_data, discont=np.pi)

else:
    if len(inputpeaks[0]) > 1:
        data_to_be_hilbertized = filtered_output[inputpeaks[0][0]:inputpeaks[0][1]]
        hilbert_time = time[inputpeaks[0][0]:inputpeaks[0][1]]
        divide_by_2 = 2
    else:
        data_to_be_hilbertized = filtered_output[inputpeaks[0][0]:inputtroughs[0][0]]
        hilbert_time = time[inputpeaks[0][0]:inputtroughs[0][0]]
    data_to_be_hilbertized = data_to_be_hilbertized - np.min(data_to_be_hilbertized)
    data_to_be_hilbertized = data_to_be_hilbertized / np.max(data_to_be_hilbertized)
    hilbert_data = np.angle(hilbert(2 * data_to_be_hilbertized - 1))
    hilbert_data2 = np.unwrap(hilbert_data, discont=np.pi)
phase_over_time = np.array([np.trapz(np.abs(np.gradient(hilbert_data2, hilbert_time))[0:j], hilbert_time[0:j]) for j, t in
                   enumerate(hilbert_time)])
ax[2].plot(hilbert_time, phase_over_time*(1/(2*np.pi)))
cycle_counter = [np.argmin(np.abs(phase_over_time*(1/(2*np.pi)) - m * np.ones(np.shape(phase_over_time)))) for m in range(1, 10)]
ax[2].vlines(hilbert_time[cycle_counter], 0, 3, color='red')


# Calculate the displacement
Delta_phi = phase_over_time[-1] - phase_over_time[0]
Deltax = Delta_phi * 635e-9 / (2 * divide_by_2 * 2*np.pi)
ax[2].set_title(f'{2*Deltax*1000000} micrometer')
plt.show()

#save all data
#np.savez('data.npz', time=time, input_voltage=input_voltage, output_voltage=output_voltage, filtered_input=filtered_input, filtered_output=filtered_output, hilbert_time=hilbert_time, phase_over_time=phase_over_time, cycle_counter=cycle_counter, Deltax=Deltax)

print(f'{2*Deltax*1000000} micrometer')


