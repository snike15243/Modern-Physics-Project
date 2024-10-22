import numpy as np
import pandas as pd
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

def cornerdetection_inputsignal(data_array, time_array, peak_or_through):
    """
    Detect the corner of the input signal
    """
    corner = []
    #y = savgol_filter(data_array, 100, 4, deriv=1, delta=time_array[1]-time_array[0]) #nthorderfirstdegreenumderivative(50, data_array, time_array[1] - time_array[0])
    y = golay_filter_variable_window_size(data_array, 4, time_array, deriv=1, innerwindow=10, innerwindow2=100, scalefactor=2000000, max=20)
    for [counter, derivative], time in zip(enumerate(y), time_array):
        if peak_or_through == True:
            if counter < len(y)-1:
                nextindex = 0
                for i in range(counter+1, len(y)):
                    if time_array[i] > time:
                        nextindex = i
                        break
                previndex = 0
                for i in range(counter-1, 0, -1):
                    if time_array[i] < time:
                        previndex = i
                        break
                if ((derivative >= 0) or (y[previndex] >= 0)) & (y[nextindex] <= 0):
                    corner.append(time)
        else:
            if counter < len(y)-1:
                nextindex = 0
                for i in range(counter + 1, len(y)):
                    if time_array[i] > time:
                        nextindex = i
                        break
                previndex = 0
                for i in range(counter - 1, 0, -1):
                    if time_array[i] < time:
                        previndex = i
                        break
                if ((derivative <= 0) or (y[previndex] <= 0)) & (y[nextindex] >= 0):
                    corner.append(time)
    return corner



def cornerdetection_outputsignal(data_array, time_array,peak_or_through):
    """
    Detect the corner of the output signal
    """
    corner = []
    #local_window_size = np.array(to_the_sides(max_turnaround(savgol_filter(abs(savgol_filter(data_array, 10, 4, deriv=2, delta=(time_array[1] - time_array[0]))),100, 4 ))/2000000))
    y = golay_filter_variable_window_size(data_array, 4, time_array, deriv=1, innerwindow=10, innerwindow2=100, scalefactor=2000000, max=20)

    for [counter, derivative], time in zip(enumerate(y), time_array):
        if peak_or_through == True:
            if counter < len(y)-1:
                nextindex = 0
                for i in range(counter + 1, len(y)):
                    if time_array[i] > time:
                        nextindex = i
                        break
                if (derivative >= 0) & (y[nextindex] <= 0):
                    corner.append(time)
        else:
            if counter < len(y)-1:
                nextindex = 0
                for i in range(counter + 1, len(y)):
                    if time_array[i] > time:
                        nextindex = i
                        break
                if (derivative <= 0) & (y[nextindex] >= 0):
                    corner.append(time)
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