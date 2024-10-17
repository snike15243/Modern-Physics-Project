import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Extract the data
for df in data_array[1]:
    plt.plot(df.iloc[0,2:], [df.iloc[1,2:], df.iloc[2,2:]])
