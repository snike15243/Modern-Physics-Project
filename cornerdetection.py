import numpy as np
import pandas as pd
from numderivative import nthorderfirstdegreenumderivative, nthorderjthdegreenumderivative
from scipy.signal import savgol_filter



def cornerdetection_inputsignal(data_array, time_array, peak_or_through):
    """
    Detect the corner of the input signal
    """
    corner = []
    y = savgol_filter(data_array, 100, 4, deriv=1, delta=time_array[1]-time_array[0]) #nthorderfirstdegreenumderivative(50, data_array, time_array[1] - time_array[0])
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

def golay_filter_variable_window_size(data_array, polynomial_order, time_array, deriv=0):
    local_window_size = np.array(to_the_sides(max_turnaround(
        savgol_filter(abs(savgol_filter(data_array, 10, polynomial_order, deriv=2, delta=(time_array[1] - time_array[0]))), 100,
                      polynomial_order)) / 2000000))
    for xi, xf in enumerate(local_window_size):
        if xf <= polynomial_order + 1:
            local_window_size[xi] = polynomial_order + 1
    y = np.zeros(len(data_array))
    for i in range(len(y)):
        y[i] = savgol_filter(data_array, int(local_window_size[i]), polynomial_order, deriv=deriv, delta=time_array[1] - time_array[0])[
            i]  # nthorderfirstdegreenumderivative(50, data_array, time_array[1] - time_array[0])
    return y

def cornerdetection_outputsignal(data_array, time_array,peak_or_through):
    """
    Detect the corner of the output signal
    """
    corner = []
    local_window_size = np.array(to_the_sides(max_turnaround(savgol_filter(abs(savgol_filter(data_array, 10, 4, deriv=2, delta=(time_array[1] - time_array[0]))),100, 4 ))/2000000))
    y = golay_filter_variable_window_size(data_array, 4, time_array, deriv=1)

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

def to_the_sides(x):
    for xi, xf in enumerate(x):
        if (xf <= 0) & (xi > 0):
            xf = x[xi-1]
        elif (xf <= 0) & (xi == 0):
            xf = x[1]
    return 20/(1 + (20/x - 1)**2)