import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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
for df in [data_array[0]]:
    fig, ax = plt.subplots()
    ax.scatter(df.iloc[1:,0].to_numpy().astype(float), df.iloc[1:,1].to_numpy().astype(float), s=1)
    ax.scatter(df.iloc[1:,0].to_numpy().astype(float), df.iloc[1:,2].to_numpy().astype(float), s=1)


    ax.grid()
    plt.show()

