
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from cornerdetection import cornerdetection_inputsignal, max_turnaround, to_the_sides, \
    golay_filter_variable_window_size, cornerdetection_outputsignal, windowsize, \
    golay_filter_variable_window_size_input_signal, golay_filter_variable_window_size_output_signal, \
    windowsize_input_signal, windowsize_output_signal
from numderivative import nthorderfirstdegreenumderivative
from scipy.signal import savgol_filter
import copy

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
for counter, df in enumerate([data_array[0]]):

    time_old = df.iloc[1:,0].to_numpy().astype(float)
    input_signal = df.iloc[1:,1].to_numpy().astype(float)
    output_signal = df.iloc[1:,2].to_numpy().astype(float)

    # time = np.unique(time_old)
    # output_signal = np.zeros_like(time)
    # input_signal = np.zeros_like(time)
    # for i, timer in enumerate(time):
    #     output_signal[i] = np.mean(output_signal_old[time_old == timer])
    #     input_signal[i] = np.mean(input_signal_old[time_old == timer])

    time2 = copy.deepcopy(time_old)
    for index, timer in enumerate(np.unique(time_old)):
        copycount = len(time_old[time_old == timer])
        time_old[time_old == timer] = np.linspace(timer, timer + np.unique(time_old)[1] - np.unique(time_old)[0], copycount)

    time = time_old
    input_signal_peaks = np.unique(cornerdetection_inputsignal(input_signal, time, True))
    output_signal_peaks = np.unique(cornerdetection_outputsignal(output_signal, time, True))
    input_signal_throughs = np.unique(cornerdetection_inputsignal(input_signal, time, False))
    output_signal_throughs = np.unique(cornerdetection_outputsignal(output_signal, time, False))
    #
    for peak_index, peak_time in enumerate(output_signal_peaks):
        corresponding_through_index = np.isclose(output_signal_throughs, peak_time, atol=0., rtol=0.00001).nonzero()[0]
        if len(corresponding_through_index) == 0:
            continue
        else:
            for corindex in corresponding_through_index:
                if corindex != 0:
                    if output_signal_peaks[peak_index-1] < output_signal_throughs[corindex-1]:
                        # take peak before and through after
                        newtime = peak_time + (output_signal_throughs[corindex-1] - peak_time)/2
                        output_signal_peaks[peak_index] = newtime
                    else:
                        #take through before and peak after
                        newtime = peak_time + (output_signal_peaks[peak_index-1] - peak_time)/2
                        output_signal_throughs[corindex] = newtime
                else:
                    if output_signal_peaks[peak_index+1] < output_signal_throughs[corindex+1]:
                        # take peak before and through after
                        newtime = peak_time + (output_signal_peaks[peak_index+1] - peak_time)/2
                        output_signal_throughs[corindex] = newtime
                    else:
                        #take through before and peak after
                        newtime = peak_time + (output_signal_throughs[corindex+1] - peak_time)/2
                        output_signal_peaks[peak_index] = newtime
    deletion_indices = []
    for peak_index, peak_time in enumerate(output_signal_peaks):
        windowsize_val = np.interp(peak_time, time, windowsize_output_signal(output_signal, 4, time, innerwindow=20, innerwindow2=200,
                                                            scalefactor=13000000, max=30, loweroffset=100000000))
        if windowsize_val > 23:
            local_detection_window_size =0.001
        else:
            local_detection_window_size = 0
        window_set_start = [i for i, x in enumerate(output_signal_peaks) if x >= peak_time-local_detection_window_size/2][0]
        window_set_end =  [i for i, x in enumerate(output_signal_peaks) if x <= peak_time+local_detection_window_size/2][-1]
        if window_set_start != window_set_end:
            for close_doubles_index, close_doubles in enumerate(output_signal_peaks[window_set_start:window_set_end]):
                highest_peak_index = np.argmax(np.interp(output_signal_peaks[window_set_start:window_set_end], time, output_signal))
                hightest_peak_time = output_signal_peaks[window_set_start:window_set_end][highest_peak_index]
                if np.isclose(peak_time, hightest_peak_time, atol=0., rtol=0.000001) == False:
                    deletion_indices.append(peak_index)

    output_signal_peaks = np.delete(output_signal_peaks, deletion_indices)

    deletion_indices2 = []
    for through_index, through_time in enumerate(output_signal_throughs):
        windowsize_val = np.interp(through_time, time,
                                   windowsize_output_signal(output_signal, 4, time, innerwindow=20, innerwindow2=200,
                                                            scalefactor=13000000, max=30, loweroffset=100000000))
        if windowsize_val > 23:
            local_detection_window_size = 0.0016
        else:
            local_detection_window_size = 0
        window_set_start = \
        [i for i, x in enumerate(output_signal_throughs) if x >= through_time - local_detection_window_size / 2][0]
        window_set_end = \
        [i for i, x in enumerate(output_signal_throughs) if x <= through_time + local_detection_window_size / 2][-1]
        if window_set_start != window_set_end:
            for close_doubles_index, close_doubles in enumerate(output_signal_throughs[window_set_start:window_set_end]):
                lowest_through_index = np.argmin(
                    np.interp(output_signal_throughs[window_set_start:window_set_end], time, output_signal))
                lowest_through_time = output_signal_throughs[window_set_start:window_set_end][lowest_through_index]
                if np.isclose(through_time, lowest_through_time, atol=0., rtol=0.000001) == False:
                    deletion_indices2.append(through_index)

    output_signal_throughs = np.delete(output_signal_throughs, deletion_indices2)


    switch_points = []
    output_signal_corners = np.sort(np.concatenate((output_signal_peaks, output_signal_throughs)))
    output_signal_corners_arg = np.argsort(np.concatenate((output_signal_peaks, output_signal_throughs)))
    for xi, xf in enumerate(output_signal_corners):

        if np.abs(np.interp(xf, time, output_signal) - np.interp(output_signal_corners[xi-1], time, output_signal)) < 0.2 * np.abs(np.max(output_signal) - np.min(output_signal)):

            switch_points.append(xf)
    print(output_signal_throughs, output_signal_peaks)
    print(input_signal_throughs, input_signal_peaks)

    figax.append(plt.subplots(1,1))
    #figax[counter][1].scatter(time,input_signal , s=1)
    figax[counter][1].vlines(x=input_signal_peaks, color='red', ymin=min(input_signal), ymax=max(input_signal))
    figax[counter][1].vlines(x=input_signal_throughs, color='green', ymin=min(input_signal), ymax=max(input_signal))
    figax[counter][1].scatter(time-np.ones((len(time)))*0.003, output_signal, s=0.5, color='green')
    ##figax[counter][1].scatter(time, savgol_filter(input_signal, 100, 4, deriv=0, delta=(time[1]-time[0])), s=1)
    figax[counter][1].plot(time, golay_filter_variable_window_size_input_signal(input_signal, 4, time, deriv=0, innerwindow=100, innerwindow2=150, scalefactor=30000, max=150, loweroffset=2000000), linewidth=1)
    figax[counter][1].plot(time-np.ones((len(time)))*0.003, golay_filter_variable_window_size_output_signal(output_signal, 4, time, deriv=0, innerwindow=20, innerwindow2=200, scalefactor=13000000, max=30, loweroffset=100000000), linewidth=1)
    figax[counter][1].vlines(x=output_signal_peaks-np.ones((len(output_signal_peaks)))*0.003, color='red', ymin=min(output_signal), ymax=max(output_signal))
    figax[counter][1].vlines(x=output_signal_throughs-np.ones((len(output_signal_throughs)))*0.003, color='green', ymin=min(output_signal), ymax=max(output_signal))
    #figax[counter][1].plot(time,windowsize_input_signal(input_signal, 4, time, innerwindow=100, innerwindow2=150, scalefactor=30000, max=150, loweroffset=2000000))
    # figax[counter][1].plot(time, windowsize_output_signal(output_signal, 4, time, innerwindow=20, innerwindow2=200,
    #                                                         scalefactor=13000000, max=30, loweroffset=100000000), color='red')

    # timepol = np.linspace(time[0], time[-1], 2000)
    # data_array_pol = np.interp(timepol, time, output_signal)
    # #figax[counter][1].plot(timepol, data_array_pol, linewidth=1)
    # func1 = lambda data_array_pol_var: savgol_filter(data_array_pol_var, 20, 4, deriv=2, delta=(timepol[1] - timepol[0]), mode='interp')
    # func2 = lambda data_array_pol_var: np.abs(func1(data_array_pol_var))
    # func3 = lambda data_array_pol_var: savgol_filter(func2(data_array_pol_var), 200, 4, mode='constant')
    # func4 = lambda data_array_pol_var: max_turnaround(func3(data_array_pol_var))
    # func5 = lambda data_array_pol_var: (func4(data_array_pol_var)+100000000)/(13000000)
    # func5_5 = lambda data_array_pol_var: ((func5(data_array_pol_var))**2)/(30)
    # func6 = lambda data_array_pol_var: to_the_sides(func5_5(data_array_pol_var), max=30, power=2)
    # figax[counter][1].plot(timepol, func1(data_array_pol))
    #figax[counter][1].plot(timepol, to_the_sides((((max_turnaround(savgol_filter(np.abs(savgol_filter(data_array_pol, 20, 4, deriv=2, delta=(timepol[1] - timepol[0]), mode='nearest')), 200, 4, mode='constant'))+100000000)/(13000000))**2)/30, max=30, power=2), color='black')


    # figax[counter][1].plot(time, np.array(max_turnaround(
    #      savgol_filter(abs(savgol_filter(input_signal, 100, 4, deriv=2, delta=(time[95+1] - time[95]))), 150,
    #                   4)) / (2.5*10**29)))

    #timepol = np.linspace(time[0], time[-1], 1000)
    #input_signal_pol = np.interp(timepol, time, input_signal)
    #figax[counter][1].plot(to_the_sides(max_turnaround(savgol_filter(np.abs(savgol_filter(input_signal_pol, 100, 4, deriv=2, delta=(timepol[1] - timepol[0]))), 150, 4))/(30000), max=150, power=2))
    #figax[counter][1].plot(savgol_filter(np.abs(savgol_filter(input_signal_pol, 100, 4, deriv=2, delta=(timepol[1] - timepol[0]), mode='nearest')), 150, 4, mode='constant')/(30000))

    #figax[counter][1].grid()

    AB_dist = np.abs(input_signal_peaks[0] - input_signal_throughs[0])
    AB_stretch = [input_signal_throughs[0]+0.25*AB_dist, input_signal_peaks[0]-0.25*AB_dist]
    AB_stretch[0], indexA = [[x, i] for i, x in enumerate(output_signal_peaks) if x >= AB_stretch[0]][0]
    AB_stretch[1], indexB = [[x, i] for i, x in enumerate(output_signal_peaks) if x <= AB_stretch[1]][-1]
    AB_y = np.interp(AB_stretch, time, input_signal)
    figax[counter][1].plot(AB_stretch[0], AB_y[0], color='black',marker='o', markersize=5)
    figax[counter][1].text(AB_stretch[0]+0.0005, AB_y[0], 'A', fontsize=12)
    figax[counter][1].plot(AB_stretch[1], AB_y[1], color='black',marker='o', markersize=5)
    figax[counter][1].text(AB_stretch[1]+0.0005, AB_y[1], 'B', fontsize=12)
    number_of_cycles_between_AB = indexB - indexA
    lambdav = 635 * 10 ** -9
    Responsivity = 0.5*lambdav*number_of_cycles_between_AB/(AB_stretch[1]-AB_stretch[0])
    figax[counter][1].set_title('Responsivity: ' + str(Responsivity) + ' m/V')
    plt.show()

