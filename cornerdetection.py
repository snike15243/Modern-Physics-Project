import copy

import numpy as np
import pandas as pd
from numpy.core.defchararray import lower

from numderivative import nthorderfirstdegreenumderivative, nthorderjthdegreenumderivative
from scipy.signal import savgol_filter

def windowsize(data_array,polynomial_order, time_array, innerwindow=10, innerwindow2=100, scalefactor=2000000, max=20):
    #if i <= len(data_array):
    timepol = np.linspace(time_array[0], time_array[-1], 1000)
    data_array_pol = np.interp(timepol, time_array, data_array)
    out = to_the_sides(max_turnaround(savgol_filter(np.abs(savgol_filter(data_array_pol, innerwindow, polynomial_order, deriv=2, delta=(timepol[1] - timepol[0]), mode='nearest')), innerwindow2, polynomial_order, mode='constant'))/(scalefactor), max=max, power=2)
        # out =  np.array(to_the_sides(max_turnaround(
        #     savgol_filter(
        #         abs( np.array([savgol_filter(data_array, innerwindow, polynomial_order, deriv=2, delta=(time_array[j+1] - time_array[j]))[j] for j in range(len(time_array)-1)])), innerwindow2, polynomial_order))/(scalefactor), max=max, power=2))[i] #savgol_filter(data_array, innerwindow, polynomial_order, deriv=2, delta=(time_array[i+1] - time_array[i]))), innerwindow2,
        #         #polynomial_order)) / scalefactor, max=max))[i]
    # else:
    #     out =  np.array(to_the_sides(max_turnaround(
    #         savgol_filter(
    #             abs(np.array([savgol_filter(data_array, innerwindow, polynomial_order, deriv=2,
    #                                         delta=(time_array[j] - time_array[j-1]))[j] for j in
    #                           range(len(time_array) - 1)])), innerwindow2, polynomial_order)) / (scalefactor), max=max,
    #                                  power=2))[[i]] #abs( savgol_filter(data_array, innerwindow, polynomial_order, deriv=2, delta=(time_array[i] - time_array[i-1]))), innerwindow2,
    #             #polynomial_order)) / scalefactor))[i]
    # if out <= polynomial_order + 1:
    #     out = polynomial_order + 1
    for outindex, entry in enumerate(out):
        if entry <= polynomial_order + 1:
            out[outindex] = polynomial_order + 1
    out2 = np.interp(time_array, timepol, out)
    return out2

def windowsize_input_signal(data_array,polynomial_order, time_array, innerwindow=10, innerwindow2=100, scalefactor=2000000, max=20, loweroffset=1000):
    #if i <= len(data_array):
    timepol = np.linspace(time_array[0], time_array[-1], 1000)
    data_array_pol = np.interp(timepol, time_array, data_array)
    out = to_the_sides((max_turnaround(savgol_filter(np.abs(savgol_filter(data_array_pol, innerwindow, polynomial_order, deriv=2, delta=(timepol[1] - timepol[0]), mode='nearest')), innerwindow2, polynomial_order, mode='constant'))+loweroffset)/(scalefactor), max=max, power=2)
        # out =  np.array(to_the_sides(max_turnaround(
        #     savgol_filter(
        #         abs( np.array([savgol_filter(data_array, innerwindow, polynomial_order, deriv=2, delta=(time_array[j+1] - time_array[j]))[j] for j in range(len(time_array)-1)])), innerwindow2, polynomial_order))/(scalefactor), max=max, power=2))[i] #savgol_filter(data_array, innerwindow, polynomial_order, deriv=2, delta=(time_array[i+1] - time_array[i]))), innerwindow2,
        #         #polynomial_order)) / scalefactor, max=max))[i]
    # else:
    #     out =  np.array(to_the_sides(max_turnaround(
    #         savgol_filter(
    #             abs(np.array([savgol_filter(data_array, innerwindow, polynomial_order, deriv=2,
    #                                         delta=(time_array[j] - time_array[j-1]))[j] for j in
    #                           range(len(time_array) - 1)])), innerwindow2, polynomial_order)) / (scalefactor), max=max,
    #                                  power=2))[[i]] #abs( savgol_filter(data_array, innerwindow, polynomial_order, deriv=2, delta=(time_array[i] - time_array[i-1]))), innerwindow2,
    #             #polynomial_order)) / scalefactor))[i]
    # if out <= polynomial_order + 1:
    #     out = polynomial_order + 1
    for outindex, entry in enumerate(out):
        if entry <= polynomial_order + 1:
            out[outindex] = polynomial_order + 1
    out2 = np.interp(time_array, timepol, out)
    return out2

def windowsize_output_signal(data_array,polynomial_order, time_array, innerwindow=10, innerwindow2=100, scalefactor=2000000, max=20, loweroffset=1000):
    #if i <= len(data_array):
    timepol = np.linspace(time_array[0], time_array[-1], 2000)
    data_array_pol = np.interp(timepol, time_array, data_array)
    out = to_the_sides((((max_turnaround(savgol_filter(np.abs(savgol_filter(data_array_pol, innerwindow, polynomial_order, deriv=2, delta=(timepol[1] - timepol[0]), mode='interp')), innerwindow2, polynomial_order, mode='constant'))+loweroffset)/(scalefactor))**2)/max, max=max, power=2)
        # out =  np.array(to_the_sides(max_turnaround(
        #     savgol_filter(
        #         abs( np.array([savgol_filter(data_array, innerwindow, polynomial_order, deriv=2, delta=(time_array[j+1] - time_array[j]))[j] for j in range(len(time_array)-1)])), innerwindow2, polynomial_order))/(scalefactor), max=max, power=2))[i] #savgol_filter(data_array, innerwindow, polynomial_order, deriv=2, delta=(time_array[i+1] - time_array[i]))), innerwindow2,
        #         #polynomial_order)) / scalefactor, max=max))[i]
    # else:
    #     out =  np.array(to_the_sides(max_turnaround(
    #         savgol_filter(
    #             abs(np.array([savgol_filter(data_array, innerwindow, polynomial_order, deriv=2,
    #                                         delta=(time_array[j] - time_array[j-1]))[j] for j in
    #                           range(len(time_array) - 1)])), innerwindow2, polynomial_order)) / (scalefactor), max=max,
    #                                  power=2))[[i]] #abs( savgol_filter(data_array, innerwindow, polynomial_order, deriv=2, delta=(time_array[i] - time_array[i-1]))), innerwindow2,
    #             #polynomial_order)) / scalefactor))[i]
    # if out <= polynomial_order + 1:
    #     out = polynomial_order + 1
    for outindex, entry in enumerate(out):
        if entry <= polynomial_order + 1:
            out[outindex] = polynomial_order + 1
    out2 = np.interp(time_array, timepol, out)
    return out2


def golay_filter_variable_window_size(data_array, polynomial_order, time_array, deriv=0, innerwindow=10, innerwindow2=100, scalefactor=2000000, max=20):


    local_window_size = windowsize(data_array, polynomial_order, time_array, innerwindow=innerwindow,
                                   innerwindow2=innerwindow2, scalefactor=scalefactor, max=max)

    timepol = np.linspace(time_array[0], time_array[-1], 1000)
    data_array_pol = np.interp(timepol, time_array, data_array)
    local_window_size_pol = np.interp(timepol, time_array, local_window_size)
    y = np.zeros(len(data_array_pol))
    for i in range(len(y)):

        y[i] = savgol_filter(data_array_pol, int(local_window_size_pol[i]), polynomial_order, deriv=0, delta=timepol[1] - timepol[0])[
            i]  # nthorderfirstdegreenumderivative(50, data_array, time_array[1] - time_array[0])
    # local_window_size_last = local_window_size[-1] #windowsize(-1, data_array, polynomial_order, time_array, innerwindow=innerwindow, innerwindow2=innerwindow2, scalefactor=scalefactor,max=max)
    # y[-1] = savgol_filter(data_array, int(local_window_size_last), polynomial_order, deriv=deriv, delta=time_array[-1] - time_array[-2])[-1]
    # if deriv == 1:
    #     y[-1] = y[-2]
    if deriv > 0:
        y = nthorderjthdegreenumderivative(deriv, 10, y, timepol[1] - timepol[0])
    y2 = np.interp( time_array, timepol, y)

    return y2

def golay_filter_variable_window_size_input_signal(data_array, polynomial_order, time_array, deriv=0, innerwindow=10, innerwindow2=100, scalefactor=2000000, max=20, loweroffset=1000):


    local_window_size = windowsize_input_signal(data_array, polynomial_order, time_array, innerwindow=innerwindow,
                                   innerwindow2=innerwindow2, scalefactor=scalefactor, max=max, loweroffset=loweroffset)

    timepol = np.linspace(time_array[0], time_array[-1], 1000)
    data_array_pol = np.interp(timepol, time_array, data_array)
    local_window_size_pol = np.interp(timepol, time_array, local_window_size)
    y = np.zeros(len(data_array_pol))
    for i in range(len(y)):
        data_array_pol_copy = copy.deepcopy(data_array_pol)
        slopeextra = (data_array_pol[-1] - data_array_pol[-50])/(timepol[-1] - timepol[-50])
        data_array_pol_copy = np.concatenate((data_array_pol_copy, np.array([data_array_pol[-1] + slopeextra*(timepol[-1] - timepol[-2])*step for step in range(1, 21)])))
        y[i] = savgol_filter(data_array_pol_copy, int(local_window_size_pol[i]), polynomial_order, deriv=0, delta=timepol[1] - timepol[0])[
            i]  # nthorderfirstdegreenumderivative(50, data_array, time_array[1] - time_array[0])
    # local_window_size_last = local_window_size[-1] #windowsize(-1, data_array, polynomial_order, time_array, innerwindow=innerwindow, innerwindow2=innerwindow2, scalefactor=scalefactor,max=max)
    # y[-1] = savgol_filter(data_array, int(local_window_size_last), polynomial_order, deriv=deriv, delta=time_array[-1] - time_array[-2])[-1]
    # if deriv == 1:
    #     y[-1] = y[-2]
    if deriv > 0:
        ynew = copy.deepcopy(y)
        slope = (y[-1] - y[-50])/(timepol[-1] - timepol[-50])
        ynew = np.concatenate((ynew, np.array([y[-1] + slope*(timepol[-1] - timepol[-2])*step for step in range(1, 11)])))
        y = nthorderjthdegreenumderivative(deriv, 10, ynew, timepol[1] - timepol[0])[0:len(y)]
    y2 = np.interp( time_array, timepol, y)

    return y2


def golay_filter_variable_window_size_output_signal(data_array, polynomial_order, time_array, deriv=0, innerwindow=10, innerwindow2=100, scalefactor=2000000, max=20, loweroffset=1000):


    local_window_size = windowsize_output_signal(data_array, polynomial_order, time_array, innerwindow=innerwindow,
                                   innerwindow2=innerwindow2, scalefactor=scalefactor, max=max, loweroffset=loweroffset)

    timepol = np.linspace(time_array[0], time_array[-1], 4000)
    data_array_pol = np.interp(timepol, time_array, data_array)
    local_window_size_pol = np.interp(timepol, time_array, local_window_size)
    y = np.zeros(len(data_array_pol))
    for i in range(len(y)):
        data_array_pol_copy = copy.deepcopy(data_array_pol)
        slopeextra = (data_array_pol[-1] - data_array_pol[-3]) / (timepol[-1] - timepol[-3])
        data_array_pol_copy = np.concatenate((data_array_pol_copy, np.array(
            [data_array_pol[-1] + slopeextra * (timepol[-1] - timepol[-2]) * step for step in range(1, 21)])))
        y[i] = savgol_filter(data_array_pol_copy, 2*int(local_window_size_pol[i]), polynomial_order, deriv=0, delta=timepol[1] - timepol[0])[
            i]  # nthorderfirstdegreenumderivative(50, data_array, time_array[1] - time_array[0])
    # local_window_size_last = local_window_size[-1] #windowsize(-1, data_array, polynomial_order, time_array, innerwindow=innerwindow, innerwindow2=innerwindow2, scalefactor=scalefactor,max=max)
    # y[-1] = savgol_filter(data_array, int(local_window_size_last), polynomial_order, deriv=deriv, delta=time_array[-1] - time_array[-2])[-1]
    # if deriv == 1:
    #     y[-1] = y[-2]
    if deriv > 0:
        ynew = copy.deepcopy(y)
        slope = (y[-1] - y[-3]) / (timepol[-1] - timepol[-3])
        ynew = np.concatenate(
            (ynew, np.array([y[-1] + slope * (timepol[-1] - timepol[-2]) * step for step in range(1, 11)])))
        y = nthorderjthdegreenumderivative(deriv, 10, ynew, timepol[1] - timepol[0])[0:len(y)]
    y2 = np.interp( time_array, timepol, y)

    return y2


def cornerdetection_inputsignal(data_array, time_array, peak_or_through):
    """
    Detect the corner of the input signal
    """
    corner = []
    #y = savgol_filter(data_array, 100, 4, deriv=1, delta=time_array[1]-time_array[0]) #nthorderfirstdegreenumderivative(50, data_array, time_array[1] - time_array[0])
    y = golay_filter_variable_window_size_input_signal(data_array, 4, time_array, deriv=1, innerwindow=100, innerwindow2=150, scalefactor=30000, max=150, loweroffset=2000000)
    for [counter, derivative], time in zip(enumerate(y), time_array):
        if peak_or_through == True:
            if counter < len(y)-1:

                def zerocross_statement(derivative2, y2, counter2, time_array2, time2):
                    nextindex = 0
                    for i in range(counter2 + 1, len(y2)):
                        if time_array2[i] > time2:
                            nextindex = i
                            break
                    previndex = 0
                    for i in range(counter2 - 1, 0, -1):
                        if time_array2[i] < time2:
                            previndex = i
                            break
                    return (derivative2 >= 0) & (y2[nextindex] <= 0)
                def zerocross_statement2(derivative2, y2, counter2, time_array2, time2):
                    nextindex = 0
                    for i in range(counter2 + 1, len(y2)):
                        if time_array2[i] > time2:
                            nextindex = i
                            break
                    previndex = 0
                    for i in range(counter2 - 1, 0, -1):
                        if time_array2[i] < time2:
                            previndex = i
                            break
                    return (derivative2 <= 0) & (y2[nextindex] >= 0)
                if zerocross_statement(derivative, y, counter, time_array, time) & ((zerocross_statement(y[counter-1], y, counter-1, time_array, time_array[counter-1]) or zerocross_statement2(y[counter-1], y, counter-1, time_array, time_array[counter-1])) == False):
                    corner.append(time)
        else:
            if counter < len(y)-1:
                def zerocross_statement(derivative2, y2, counter2, time_array2, time2):
                    nextindex = 0
                    for i in range(counter2 + 1, len(y2)):
                        if time_array2[i] > time2:
                            nextindex = i
                            break
                    previndex = 0
                    for i in range(counter2 - 1, 0, -1):
                        if time_array2[i] < time2:
                            previndex = i
                            break
                    return (derivative2 >= 0) & (y2[nextindex] <= 0)
                def zerocross_statement2(derivative2, y2, counter2, time_array2, time2):
                    nextindex = 0
                    for i in range(counter2 + 1, len(y2)):
                        if time_array2[i] > time2:
                            nextindex = i
                            break
                    previndex = 0
                    for i in range(counter2 - 1, 0, -1):
                        if time_array2[i] < time2:
                            previndex = i
                            break
                    return (derivative2 <= 0) & (y2[nextindex] >= 0)

                if zerocross_statement2(derivative, y, counter, time_array, time) & ((zerocross_statement2(y[counter - 1],
                                                                                                         y, counter - 1,
                                                                                                         time_array,
                                                                                                         time_array[
                                                                                                             counter - 1]) or zerocross_statement(
                        y[counter - 1], y, counter - 1, time_array, time_array[counter - 1])) == False):
                    corner.append(time)
    return corner



def cornerdetection_outputsignal(data_array, time_array,peak_or_through):
    """
    Detect the corner of the output signal
    """
    corner = []
    #local_window_size = np.array(to_the_sides(max_turnaround(savgol_filter(abs(savgol_filter(data_array, 10, 4, deriv=2, delta=(time_array[1] - time_array[0]))),100, 4 ))/2000000))
    y = golay_filter_variable_window_size_output_signal(data_array, 4, time_array, deriv=1, innerwindow=20, innerwindow2=200, scalefactor=13000000, max=30, loweroffset=100000000)

    for [counter, derivative], time in zip(enumerate(y), time_array):
        if peak_or_through == True:
            if counter < len(y) - 1:

                def zerocross_statement(derivative2, y2, counter2, time_array2, time2):
                    nextindex = 0
                    for i in range(counter2 + 1, len(y2)):
                        if time_array2[i] > time2:
                            nextindex = i
                            break
                    previndex = 0
                    for i in range(counter2 - 1, 0, -1):
                        if time_array2[i] < time2:
                            previndex = i
                            break
                    return (derivative2 >= 0) & (y2[nextindex] <= 0)

                def zerocross_statement2(derivative2, y2, counter2, time_array2, time2):
                    nextindex = 0
                    for i in range(counter2 + 1, len(y2)):
                        if time_array2[i] > time2:
                            nextindex = i
                            break
                    previndex = 0
                    for i in range(counter2 - 1, 0, -1):
                        if time_array2[i] < time2:
                            previndex = i
                            break
                    return (derivative2 <= 0) & (y2[nextindex] >= 0)

                if zerocross_statement(derivative, y, counter, time_array, time) & ((zerocross_statement(y[counter-1], y, counter-1, time_array, time_array[counter-1])) == False):
                    corner.append(time_array[counter+1])
        else:
            if counter < len(y) - 1:
                def zerocross_statement(derivative2, y2, counter2, time_array2, time2):
                    nextindex = 0
                    for i in range(counter2 + 1, len(y2)):
                        if time_array2[i] > time2:
                            nextindex = i
                            break
                    previndex = 0
                    for i in range(counter2 - 1, 0, -1):
                        if time_array2[i] < time2:
                            previndex = i
                            break
                    return (derivative2 >= 0) & (y2[nextindex] <= 0)

                def zerocross_statement2(derivative2, y2, counter2, time_array2, time2):
                    nextindex = 0
                    for i in range(counter2 + 1, len(y2)):
                        if time_array2[i] > time2:
                            nextindex = i
                            break
                    previndex = 0
                    for i in range(counter2 - 1, 0, -1):
                        if time_array2[i] < time2:
                            previndex = i
                            break
                    return (derivative2 <= 0) & (y2[nextindex] >= 0)

                if zerocross_statement2(derivative, y, counter, time_array, time) & ((zerocross_statement2(y[counter-1],y, counter-1, time_array, time_array[counter-1])) == False):
                    corner.append(time_array[counter+1])
    return corner

def max_turnaround(x):
    return max(x)*np.ones(len(x)) - x

def to_the_sides(x, max=20, power=2):
    for xi, xf in enumerate(x):
        if (xf <= 0) & (xi > 0):
            x[xi] = x[xi-1]
        elif (xf <= 0) & (xi == 0):
            x[xi] = x[x != 0][0]
    return max/(1 + (max/x - 1)**power)