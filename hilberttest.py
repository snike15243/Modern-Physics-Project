import copy

from scipy.signal import hilbert
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Qt5Agg')
datafile = np.load('240data130a0.npz')
datafile2 = np.load('240data140a0.npz')
time = datafile['time']# [942:3027]
time2 = datafile2['time']# [945:3023]
signal = datafile['filtered_output']# [942:3027]
signal2 = datafile2['filtered_output']# [945:3023]
#signal2[1400:2100] = np.linspace(signal2[1400], signal2[2100], 2100-1400)

#time = np.linspace(0, 1, 500)
#signal = 2*np.sin(2 * np.pi * 5 * time) + 0*np.sin(2 * np.pi * 15 * time)
data_to_be_hilbertized = signal
data_to_be_hilbertized = data_to_be_hilbertized - (np.max(data_to_be_hilbertized)+np.min(data_to_be_hilbertized))/2
#data_to_be_hilbertized = data_to_be_hilbertized/np.max(data_to_be_hilbertized)
data_to_be_hilbertized2 = signal2
data_to_be_hilbertized2 = data_to_be_hilbertized2 - (np.max(data_to_be_hilbertized2)+np.min(data_to_be_hilbertized2))/2
#data_to_be_hilbertized2 = data_to_be_hilbertized2/np.max(data_to_be_hilbertized2)
hilbert_data = np.angle(hilbert(data_to_be_hilbertized))
hilbert_data2 = np.unwrap(hilbert_data, discont=np.pi)
hilbert_diff = []
for i, h in enumerate(hilbert_data2):
    if i != len(hilbert_data2)-1:
        hilbert_diff.append(hilbert_data2[i+1] - hilbert_data2[i])
        if np.abs(hilbert_data2[i+1] - hilbert_data2[i]) > 0.5*np.pi:
            hilbert_data2[i+1:] = hilbert_data2[i+1:] - np.pi*np.sign(hilbert_data2[i+1] - hilbert_data2[i])
phase_over_time = np.array([np.trapz(np.abs(np.gradient(hilbert_data2, time))[0:j], time[0:j]) for j, t in enumerate(time)])
hilbertdata2a = np.angle(hilbert(data_to_be_hilbertized2))
hilbertdata2b = np.unwrap(hilbertdata2a, discont=np.pi)
hilbert_diff2 = []
for i, h in enumerate(hilbertdata2b):
    if i != len(hilbertdata2b)-1:
        hilbert_diff2.append(hilbertdata2b[i+1] - hilbertdata2b[i])
        if np.abs(hilbertdata2b[i+1] - hilbertdata2b[i]) > 0.5*np.pi:
            hilbertdata2b[i+1:] = hilbertdata2b[i+1:] - np.pi*np.sign(hilbertdata2b[i+1] - hilbertdata2b[i])
phase_over_time2 = np.array([np.trapz(np.abs(np.gradient(hilbertdata2b, time2))[0:j], time2[0:j]) for j, t in enumerate(time2)])
# find locations intersections with a multiple of 2pi
full_cycle_locs = [0]
phase_over_time_copy = copy.deepcopy(phase_over_time)
for i, p in enumerate(phase_over_time_copy):
    if phase_over_time_copy[i] > 2*np.pi:
        phase_over_time_copy[i:] = phase_over_time_copy[i:] - 2*np.pi
        full_cycle_locs.append(i)




#plot
fig, ax = plt.subplots(2,1, sharex='all', figsize=(6,6))
#ax[0].plot(time, signal, color='b', label='130')
#ax[1].plot(time, phase_over_time/(2*np.pi), color='b')
ax[0].plot(time, signal, color='b', label='130')
ax[1].plot(time, (phase_over_time)/(2*np.pi), color='b')
#ax[0].vlines(time[full_cycle_locs], np.min(signal), np.max(signal), colors='r')
ax[0].plot(time2, signal2, color='r', label='140')
ax[1].plot(time2, (phase_over_time2)/(2*np.pi), color='r')
ax[0].legend()
ax[1].legend()
plt.show()
