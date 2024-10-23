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

# Load data
