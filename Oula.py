import pandas as pd
import matplotlib.pyplot as plt
import os
import io

file_path = os.path.expanduser("/Users/oula/Downloads/a4.csv")

with open(file_path, 'r') as file:
    file_contents = file.readlines()

cleaned_data = []
for line in file_contents:
    cleaned_line = line.strip().rstrip(',')
    if cleaned_line.count(',') == 2: 
        cleaned_data.append(cleaned_line)

cleaned_csv = "\n".join(cleaned_data)
data_cleaned = pd.read_csv(io.StringIO(cleaned_csv)) 
data_cleaned.columns = ['Second', 'Volt_CH1', 'Volt_CH3']
data_cleaned = data_cleaned[1:].reset_index(drop=True)

data_cleaned = data_cleaned.astype({
    "Second": float,
    "Volt_CH1": float,
    "Volt_CH3": float
})

ch1_max = data_cleaned["Volt_CH1"].max()
ch1_min = data_cleaned["Volt_CH1"].min()

ch3_max = data_cleaned["Volt_CH3"].max()
ch3_min = data_cleaned["Volt_CH3"].min()

data_cleaned["Volt_CH3_Scaled"] = (data_cleaned["Volt_CH3"] - ch3_min) / (ch3_max - ch3_min) * (ch1_max - ch1_min) + ch1_min

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(data_cleaned["Second"], data_cleaned["Volt_CH1"], label="CH1", color="blue")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Input voltage(V)")
ax1.tick_params(axis='y')

ax2 = ax1.twinx()
ax2.plot(data_cleaned["Second"], data_cleaned["Volt_CH3"], label="CH3 (Original)", color="orange")
ax2.set_ylabel("Output voltage of photodiode (V)")
ax2.tick_params(axis='y')

fig.tight_layout()
plt.show()