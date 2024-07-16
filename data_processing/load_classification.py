import os
import pandas as pd
from tqdm import tqdm

def find_consecutive_zeros(file_path, output_path):
    df = pd.read_csv(file_path)

    zero_detected = False
    current_load = 10

    # Initialize tqdm progress bar
    for i in tqdm(range(len(df)), desc="Processing rows"):
        if i < len(df) - 2 and zero_detected == False and (df.iloc[i]['CPU (%)'] == 0.0 and df.iloc[i + 1]['CPU (%)'] == 0.0 and df.iloc[i + 2]['CPU (%)'] == 0.0):
            zero_detected = True
            current_load = current_load + 10
        if df.iloc[i]['CPU (%)'] < current_load + 5 and df.iloc[i]['CPU (%)'] > current_load - 5:
            zero_detected = False
        if zero_detected:
            df.loc[i, 'load'] = 0
        else:
            df.loc[i, 'load'] = current_load

    df.to_csv(output_path, index=False)

def process_folders(base_path):
    algos = ["ackermann", "div8", "gcd", "psi", "union"]
    for algo in algos:
        folder_path = os.path.join(base_path, "ten_values_" + algo)
        if os.path.isdir(folder_path):
            power_file = os.path.join(folder_path, 'cpu_usage_' + algo + '.csv')
            output_file = os.path.join(folder_path, 'cpu_usage_' + algo + '_classified.csv')

            if os.path.exists(power_file):
                print(f"Processing {folder_path}...")
                find_consecutive_zeros(power_file, output_file)
            else:
                print(f"Skipping {folder_path}: missing required files.")

# Define the base path where your folders are located
base_path = 'single_test/rbpi5/ten_values'

# Process all folders in the base path
process_folders(base_path)
